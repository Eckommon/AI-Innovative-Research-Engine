#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FTA-TRANSIT-F01" / "STAGING_RESULT.json"
CONTRACT = ROOT / "research" / "US-FTA-TRANSIT-F01" / "README.md"
ISSUE = 147
CONTRACT_COMMIT = "70c41fc8202579436ad7560118548fc1c2a34593"
BASE = "https://data.transportation.gov"
DATASETS = {
    "breakdowns": "amkt-4ehs",
    "monthly_modal": "5ti2-5uiv",
    "major_safety_events": "9ivb-8ae9",
}
UA = "AI-Innovative-Research-Engine/US-FTA-TRANSIT-F01 outcome-blind feasibility"
PAGE = 50000
MAX_PAGES = 100


class ImplementationFailure(RuntimeError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_lines(lines: Iterable[str]) -> str:
    h = hashlib.sha256()
    for line in sorted(set(lines)):
        h.update(line.encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def norm_label(v: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(v or "").strip().lower()).strip()


def norm_id(v: Any) -> str | None:
    if v is None:
        return None
    s = str(v).strip()
    return s if s else None


def norm_mode(v: Any) -> str | None:
    s = norm_id(v)
    return s.upper() if s else None


def norm_tos(v: Any) -> str | None:
    return norm_id(v)


def parse_int_year(v: Any) -> int | None:
    if v is None or isinstance(v, bool):
        return None
    s = str(v).strip()
    m = re.fullmatch(r"(19|20)\d{2}(?:\.0+)?", s)
    if m:
        return int(s[:4])
    m = re.search(r"\b((?:19|20)\d{2})\b", s)
    if m:
        return int(m.group(1))
    return None


def parse_month(v: Any) -> int | None:
    if v is None or isinstance(v, bool):
        return None
    s = str(v).strip()
    if re.fullmatch(r"\d{1,2}(?:\.0+)?", s):
        n = int(float(s))
        return n if 1 <= n <= 12 else None
    names = {m.lower(): i for i, m in enumerate(
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 1
    )}
    key = s.lower()
    if key in names:
        return names[key]
    for name, n in names.items():
        if key == name[:3]:
            return n
    iso = re.match(r"^(?:19|20)\d{2}[-/]([01]?\d)", s)
    if iso:
        n = int(iso.group(1))
        return n if 1 <= n <= 12 else None
    return None


def is_numeric(v: Any) -> bool:
    if v is None or str(v).strip() == "":
        return True
    try:
        x = float(str(v).replace(",", "").strip())
        return math.isfinite(x)
    except ValueError:
        return False


def get_bytes(url: str, attempts: int = 4, timeout: int = 60) -> bytes:
    last: Exception | None = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                status = getattr(r, "status", 200)
                if status >= 500 or status == 429:
                    raise urllib.error.HTTPError(url, status, "retryable", r.headers, None)
                return r.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            code = getattr(exc, "code", None)
            if code is not None and code not in {429, 500, 502, 503, 504}:
                raise ImplementationFailure(f"non-retryable HTTP failure for {url}: {exc}") from exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise ImplementationFailure(f"transient/source transport failure after retries for {url}: {last}")


def get_json(url: str) -> Any:
    raw = get_bytes(url)
    try:
        return json.loads(raw), raw
    except json.JSONDecodeError as exc:
        raise ImplementationFailure(f"invalid JSON from {url}: {exc}") from exc


def metadata(dataset_id: str) -> tuple[dict[str, Any], bytes]:
    obj, raw = get_json(f"{BASE}/api/views/{dataset_id}.json")
    if not isinstance(obj, dict) or not isinstance(obj.get("columns"), list):
        raise ImplementationFailure(f"unexpected metadata shape for {dataset_id}")
    return obj, raw


def columns_index(meta: dict[str, Any]) -> list[dict[str, Any]]:
    return [c for c in meta.get("columns", []) if isinstance(c, dict) and c.get("fieldName")]


def choose_exact(columns: list[dict[str, Any]], labels: set[str], purpose: str) -> str | None:
    matches: list[str] = []
    for c in columns:
        fn = str(c.get("fieldName", ""))
        names = {norm_label(fn), norm_label(c.get("name"))}
        if names & labels:
            matches.append(fn)
    uniq = sorted(set(matches))
    if len(uniq) == 1:
        return uniq[0]
    if len(uniq) > 1:
        raise ImplementationFailure(f"ambiguous structural field for {purpose}: {uniq}")
    return None


def choose_event_time(columns: list[dict[str, Any]]) -> tuple[str | None, str | None, str | None]:
    # Deterministic structural resolver only; no event outcome field is eligible.
    exact_date = {
        "event date", "event date and time", "event datetime", "date of event",
        "event date time", "event date timestamp",
    }
    f = choose_exact(columns, exact_date, "major event time")
    if f:
        return f, None, None
    year = choose_exact(columns, {"event year", "year of event"}, "major event year")
    month = choose_exact(columns, {"event month", "month of event"}, "major event month")
    if year and month:
        return None, year, month
    return None, None, None


def soda_rows(dataset_id: str, fields: list[str]) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    bytes_read = 0
    select = ",".join(fields)
    for page in range(MAX_PAGES):
        params = urllib.parse.urlencode({"$select": select, "$limit": PAGE, "$offset": page * PAGE})
        url = f"{BASE}/resource/{dataset_id}.json?{params}"
        obj, raw = get_json(url)
        bytes_read += len(raw)
        if not isinstance(obj, list):
            raise ImplementationFailure(f"unexpected SODA row shape for {dataset_id}")
        rows.extend(r for r in obj if isinstance(r, dict))
        if len(obj) < PAGE:
            return rows, bytes_read
    raise ImplementationFailure(f"pagination safety limit exceeded for {dataset_id}")


def pair_string(pair: tuple[str, str]) -> str:
    return f"{pair[0]}\x1f{pair[1]}"


def check(pass_: bool, evidence: str) -> dict[str, Any]:
    return {"pass": bool(pass_), "evidence": evidence}


def main() -> None:
    contract = CONTRACT.read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "19. No unofficial mirror" in contract
    assert "candidate_outcome_opened: false" in contract
    assert "relationship_computed: false" in contract

    metas: dict[str, dict[str, Any]] = {}
    meta_raw: dict[str, bytes] = {}
    source: dict[str, Any] = {}
    for name, did in DATASETS.items():
        m, raw = metadata(did)
        metas[name] = m
        meta_raw[name] = raw
        source[name] = {
            "dataset_id": did,
            "metadata_bytes": len(raw),
            "metadata_sha256": sha256_bytes(raw),
            "metadata_name": m.get("name"),
            "metadata_rows_updated_at": m.get("rowsUpdatedAt"),
        }

    bc = columns_index(metas["breakdowns"])
    mc = columns_index(metas["monthly_modal"])
    ec = columns_index(metas["major_safety_events"])

    b_id = choose_exact(bc, {"ntd id", "ntd agency id"}, "breakdowns NTD ID")
    b_mode = choose_exact(bc, {"mode", "mode code"}, "breakdowns mode")
    b_tos = choose_exact(bc, {"type of service", "tos", "type of service code"}, "breakdowns TOS")
    b_year = choose_exact(bc, {"report year", "reporting year"}, "breakdowns report year")
    b_major = choose_exact(bc, {"major mechanical failures", "major mechanical failure"}, "major mechanical failures")
    b_other = choose_exact(bc, {"other mechanical failures", "other mechanical failure"}, "other mechanical failures")
    b_total = choose_exact(bc, {"total mechanical failures", "total mechanical failure"}, "total mechanical failures")

    m_id = choose_exact(mc, {"ntd id", "ntd agency id"}, "monthly NTD ID")
    m_mode = choose_exact(mc, {"mode", "mode code"}, "monthly mode")
    m_year = choose_exact(mc, {"year", "report year", "calendar year"}, "monthly year")
    m_month = choose_exact(mc, {"month", "report month", "calendar month"}, "monthly month")

    e_id = choose_exact(ec, {"ntd id", "ntd agency id"}, "major events NTD ID")
    e_mode = choose_exact(ec, {"mode", "mode code"}, "major events mode")
    e_date, e_year, e_month = choose_event_time(ec)

    resolved = {
        "breakdowns": {"ntd_id": b_id, "mode": b_mode, "tos": b_tos, "report_year": b_year,
                       "major_mechanical_failures": b_major, "other_mechanical_failures": b_other,
                       "total_mechanical_failures": b_total},
        "monthly_modal": {"ntd_id": m_id, "mode": m_mode, "year": m_year, "month": m_month},
        "major_safety_events": {"ntd_id": e_id, "mode": e_mode, "event_time": e_date,
                                "event_year": e_year, "event_month": e_month},
    }

    # A structurally absent required field is a valid scientific HOLD, not an implementation failure.
    b_required = all([b_id, b_mode, b_tos, b_year, b_major, b_other, b_total])
    m_required = all([m_id, m_mode, m_year, m_month])
    e_required = all([e_id, e_mode]) and bool(e_date or (e_year and e_month))

    # Only query datasets whose required structural fields resolve. No downstream outcome columns are requested.
    b_rows: list[dict[str, Any]] = []
    m_rows: list[dict[str, Any]] = []
    e_rows: list[dict[str, Any]] = []
    b_query_bytes = m_query_bytes = e_query_bytes = 0
    if b_required:
        b_fields = [b_id, b_mode, b_tos, b_year, b_major, b_other, b_total]  # type: ignore[list-item]
        b_rows, b_query_bytes = soda_rows(DATASETS["breakdowns"], b_fields)
    if m_required:
        m_rows, m_query_bytes = soda_rows(DATASETS["monthly_modal"], [m_id, m_mode, m_year, m_month])  # type: ignore[list-item]
    if e_required:
        e_fields = [e_id, e_mode]  # type: ignore[list-item]
        if e_date:
            e_fields.append(e_date)
        else:
            e_fields.extend([e_year, e_month])  # type: ignore[list-item]
        e_rows, e_query_bytes = soda_rows(DATASETS["major_safety_events"], e_fields)

    # Breakdowns structural diagnostics.
    b_years: set[int] = set()
    b_pairs: set[tuple[str, str]] = set()
    b_pair_years: dict[tuple[str, str], set[int]] = defaultdict(set)
    b_keys: dict[tuple[str, str, str, int], tuple[str, str, str]] = {}
    b_duplicate_rows = 0
    b_conflicting_keys = 0
    b_null_structural = 0
    b_bad_numeric = 0
    if b_required:
        for r in b_rows:
            iid, mode, tos, year = norm_id(r.get(b_id)), norm_mode(r.get(b_mode)), norm_tos(r.get(b_tos)), parse_int_year(r.get(b_year))  # type: ignore[arg-type]
            if not iid or not mode or not tos or year is None:
                b_null_structural += 1
                continue
            vals = tuple(str(r.get(f, "")).strip() for f in (b_major, b_other, b_total))  # type: ignore[arg-type]
            if not all(is_numeric(r.get(f)) for f in (b_major, b_other, b_total)):  # type: ignore[arg-type]
                b_bad_numeric += 1
            key = (iid, mode, tos, year)
            if key in b_keys:
                b_duplicate_rows += 1
                if b_keys[key] != vals:
                    b_conflicting_keys += 1
            else:
                b_keys[key] = vals
            b_years.add(year)
            pair = (iid, mode)
            b_pairs.add(pair)
            b_pair_years[pair].add(year)

    # Monthly structural diagnostics only: no safety/service measure is requested.
    m_years: set[int] = set()
    m_periods: set[tuple[int, int]] = set()
    m_pairs: set[tuple[str, str]] = set()
    m_keys: set[tuple[str, str, int, int]] = set()
    m_duplicate_rows = 0
    m_null_structural = 0
    if m_required:
        for r in m_rows:
            iid, mode = norm_id(r.get(m_id)), norm_mode(r.get(m_mode))  # type: ignore[arg-type]
            year, month = parse_int_year(r.get(m_year)), parse_month(r.get(m_month))  # type: ignore[arg-type]
            if not iid or not mode or year is None or month is None:
                m_null_structural += 1
                continue
            key = (iid, mode, year, month)
            if key in m_keys:
                m_duplicate_rows += 1
            m_keys.add(key)
            m_pairs.add((iid, mode))
            m_years.add(year)
            m_periods.add((year, month))

    # Major-event structural diagnostics only. We intentionally do not retain per-pair event counts.
    e_years: set[int] = set()
    e_periods: set[tuple[int, int | None]] = set()
    e_pairs: set[tuple[str, str]] = set()
    e_null_structural = 0
    if e_required:
        for r in e_rows:
            iid, mode = norm_id(r.get(e_id)), norm_mode(r.get(e_mode))  # type: ignore[arg-type]
            if e_date:
                raw_time = r.get(e_date)
                year = parse_int_year(raw_time)
                month = parse_month(raw_time)
                if month is None:
                    s = str(raw_time or "")
                    mm = re.search(r"(?:19|20)\d{2}[-/]([01]\d)", s)
                    month = int(mm.group(1)) if mm else None
            else:
                year = parse_int_year(r.get(e_year))  # type: ignore[arg-type]
                month = parse_month(r.get(e_month))  # type: ignore[arg-type]
            if not iid or not mode or year is None:
                e_null_structural += 1
                continue
            e_pairs.add((iid, mode))
            e_years.add(year)
            e_periods.add((year, month))

    repeated_b_pairs = {p for p, ys in b_pair_years.items() if len(ys) >= 2}
    b_m_inter = b_pairs & m_pairs
    b_e_inter = b_pairs & e_pairs
    b_m_coverage = len(b_m_inter) / len(b_pairs) if b_pairs else 0.0

    fingerprints = {
        "breakdowns_ntd_id_mode_pairs_sha256": sha256_lines(pair_string(p) for p in b_pairs),
        "monthly_modal_ntd_id_mode_pairs_sha256": sha256_lines(pair_string(p) for p in m_pairs),
        "major_safety_events_ntd_id_mode_pairs_sha256": sha256_lines(pair_string(p) for p in e_pairs),
        "breakdowns_intersect_monthly_pairs_sha256": sha256_lines(pair_string(p) for p in b_m_inter),
        "breakdowns_intersect_major_events_pairs_sha256": sha256_lines(pair_string(p) for p in b_e_inter),
    }

    source["breakdowns"].update({"query_bytes": b_query_bytes, "rows_read": len(b_rows), "resolved_fields": resolved["breakdowns"]})
    source["monthly_modal"].update({"query_bytes": m_query_bytes, "rows_read": len(m_rows), "resolved_fields": resolved["monthly_modal"]})
    source["major_safety_events"].update({"query_bytes": e_query_bytes, "rows_read": len(e_rows), "resolved_fields": resolved["major_safety_events"]})

    latest_year = dt.datetime.now(dt.timezone.utc).year
    checks = {
        "1": check(all(meta_raw.values()), "Official Socrata metadata read and SHA-256 fingerprinted for all three frozen dataset IDs."),
        "2": check(bool(b_rows) and bool(m_rows) and bool(e_rows), f"Actual structural-only query rows read: breakdowns={len(b_rows)}, monthly={len(m_rows)}, major={len(e_rows)}."),
        "3": check(b_required, f"Breakdowns required structural/mechanical fields resolved={b_required}."),
        "4": check({2022, 2023, 2024}.issubset(b_years), f"Breakdowns years={sorted(b_years)}."),
        "5": check(len(b_pairs) >= 150, f"Distinct valid Breakdowns NTD ID x mode pairs={len(b_pairs)}."),
        "6": check(len(repeated_b_pairs) >= 100, f"Breakdowns pairs represented in >=2 years={len(repeated_b_pairs)}."),
        "7": check(b_required and b_conflicting_keys == 0, f"Exact source-grain keys={len(b_keys)}, duplicate rows={b_duplicate_rows}, conflicting duplicate keys={b_conflicting_keys}."),
        "8": check(m_required and bool(m_years) and min(m_years) <= 2014 and max(m_years) >= latest_year,
                   f"Monthly required fields={m_required}; years={min(m_years) if m_years else None}..{max(m_years) if m_years else None}; evaluation_year={latest_year}."),
        "9": check(b_m_coverage >= 0.90, f"Breakdowns pairs represented in Monthly={len(b_m_inter)}/{len(b_pairs)}={b_m_coverage:.6f}."),
        "10": check(e_required and len(e_years) >= 10 and bool(e_years) and min(e_years) <= 2014,
                    f"Major-event required fields={e_required}; distinct years={len(e_years)}; range={min(e_years) if e_years else None}..{max(e_years) if e_years else None}."),
        "11": check(len(b_e_inter) >= 75, f"Exact aggregate Breakdowns∩Major NTD ID x mode pairs={len(b_e_inter)}."),
        "12": check(True, "Only exact normalized source-native NTD ID x mode is used; no agency-name/address/manual/fuzzy repair is implemented."),
        "13": check(b_required, f"TOS retained in exact Breakdowns key before pair projection; exact source-grain keys={len(b_keys)}."),
        "14": check(True, "Official recent-safety validation lag is frozen in contract; runner does not use recent safety measures and does not treat them as complete outcome support."),
        "15": check(all(len(v) == 64 for v in fingerprints.values()), "SHA-256 fingerprints persisted for all three pair sets and both exact intersections."),
        "16": check(True, "breakdown_conditioned_major_safety_event_occurrence_opened=false"),
        "17": check(True, "row_level_breakdown_event_join_persisted=false"),
        "18": check(True, "relationship_computed=false; predictive_metric_computed=false; causal_claim_made=false"),
        "19": check(True, "Only frozen official DOT/FTA endpoints and standard public-repository runner; incremental monetary cost=0 USD."),
    }
    disposition = (
        "PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY"
        if all(v["pass"] for v in checks.values())
        else "HOLD_US_FTA_TRANSIT_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY"
    )

    result = {
        "protocol": "US-FTA-TRANSIT-F01",
        "issue": ISSUE,
        "contract_commit": CONTRACT_COMMIT,
        "evaluated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "valid_evaluation": True,
        "disposition": disposition,
        "source_evidence": source,
        "structural_diagnostics": {
            "breakdowns": {
                "distinct_years": sorted(b_years),
                "valid_source_grain_keys": len(b_keys),
                "duplicate_source_grain_rows": b_duplicate_rows,
                "conflicting_duplicate_source_grain_keys": b_conflicting_keys,
                "null_or_unparseable_structural_rows": b_null_structural,
                "non_numeric_mechanical_rows": b_bad_numeric,
                "distinct_ntd_id_mode_pairs": len(b_pairs),
                "pairs_in_at_least_two_breakdown_years": len(repeated_b_pairs),
            },
            "monthly_modal": {
                "year_min": min(m_years) if m_years else None,
                "year_max": max(m_years) if m_years else None,
                "distinct_calendar_periods": len(m_periods),
                "distinct_ntd_id_mode_pairs": len(m_pairs),
                "duplicate_structural_rows": m_duplicate_rows,
                "null_or_unparseable_structural_rows": m_null_structural,
            },
            "major_safety_events": {
                "year_min": min(e_years) if e_years else None,
                "year_max": max(e_years) if e_years else None,
                "distinct_years": len(e_years),
                "distinct_calendar_periods": len(e_periods),
                "distinct_ntd_id_mode_pairs": len(e_pairs),
                "null_or_unparseable_structural_rows": e_null_structural,
            },
            "cross_source": {
                "breakdowns_pairs_in_monthly": len(b_m_inter),
                "breakdowns_pair_monthly_coverage": round(b_m_coverage, 9),
                "breakdowns_pairs_in_major_events": len(b_e_inter),
            },
        },
        "fingerprints": fingerprints,
        "checks": checks,
        "boundaries": {
            "agency_name_repair_used": False,
            "manual_or_fuzzy_identity_repair_used": False,
            "breakdown_conditioned_major_safety_event_occurrence_opened": False,
            "row_level_breakdown_event_join_persisted": False,
            "relationship_computed": False,
            "predictive_metric_computed": False,
            "causal_claim_made": False,
        },
        "incremental_monetary_cost_usd": 0,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "disposition": disposition,
        "failed_checks": [k for k, v in checks.items() if not v["pass"]],
        "breakdowns_pairs": len(b_pairs),
        "repeated_breakdowns_pairs": len(repeated_b_pairs),
        "monthly_coverage": round(b_m_coverage, 6),
        "breakdowns_major_overlap": len(b_e_inter),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
