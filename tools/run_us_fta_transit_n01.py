#!/usr/bin/env python3
"""US-FTA-TRANSIT-N01 outcome-blind matched reliability design runner.

CRITICAL OUTCOME-BLIND BOUNDARY
-------------------------------
This runner accesses ONLY the prospectively authorized FTA Annual Breakdowns
source. It never calls, reads, joins, counts, or persists Major Safety/Security
Event row values. Durable outputs contain exposure-side design diagnostics,
the frozen matched-pair manifest, and deterministic fingerprints only.
"""
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
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "US-FTA-TRANSIT-N01"
CONTRACT = RESEARCH / "README.md"
OUT = RESEARCH / "STAGING_RESULT.json"
MANIFEST = RESEARCH / "PAIR_MANIFEST.json"
CHECKPOINT = ROOT / "context" / "checkpoint.json"

ISSUE = 148
CONTRACT_COMMIT = "c4a7f4ea05954fd013714ee6c891d489a6cfc82f"
DATASET_ID = "amkt-4ehs"
BASE = "https://data.transportation.gov"
UA = "AI-Innovative-Research-Engine/US-FTA-TRANSIT-N01 outcome-blind design"
PAGE = 50000
MAX_PAGES = 10

FIELDS = [
    "ntd_id",
    "mode",
    "type_of_service",
    "reporter_type",
    "report_year",
    "major_mechanical_failures",
    "major_mechanical_failures_1",
    "vehicle_passenger_car_revenue",
    "vehicle_passenger_car_miles_2",
]
EXPECTED_TYPES = {
    "ntd_id": "text",
    "mode": "text",
    "type_of_service": "text",
    "reporter_type": "text",
    "report_year": "text",
    "major_mechanical_failures": "number",
    "major_mechanical_failures_1": "text",
    "vehicle_passenger_car_revenue": "number",
    "vehicle_passenger_car_miles_2": "text",
}

PASS = "PASS_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_IDENTIFIABLE"
HOLD = "HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE"


class ImplementationFailure(RuntimeError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def norm_id(v: Any) -> str | None:
    if v is None:
        return None
    s = str(v).strip()
    return s if s else None


def norm_mode(v: Any) -> str | None:
    s = norm_id(v)
    return s.upper() if s else None


def norm_tos(v: Any) -> str | None:
    s = norm_id(v)
    return s.upper() if s else None


def norm_flag(v: Any) -> str:
    return str(v or "").strip().upper()


def parse_year(v: Any) -> int | None:
    if v is None or isinstance(v, bool):
        return None
    s = str(v).strip()
    if not re.fullmatch(r"20\d{2}(?:\.0+)?", s):
        return None
    return int(s[:4])


def parse_number(v: Any) -> float | None:
    if v is None or isinstance(v, bool):
        return None
    s = str(v).replace(",", "").strip()
    if not s:
        return None
    try:
        x = float(s)
    except ValueError:
        return None
    return x if math.isfinite(x) else None


def get_bytes(url: str, attempts: int = 5, timeout: int = 90) -> bytes:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": UA, "Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                status = getattr(response, "status", 200)
                if status == 429 or status >= 500:
                    raise urllib.error.HTTPError(url, status, "retryable", response.headers, None)
                return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            code = getattr(exc, "code", None)
            if code is not None and code not in {429, 500, 502, 503, 504}:
                raise ImplementationFailure(f"non-retryable HTTP failure: {url}: {exc}") from exc
            if attempt + 1 < attempts:
                time.sleep(2 ** attempt)
    raise ImplementationFailure(f"source transport failure after retries: {url}: {last}")


def get_json(url: str) -> tuple[Any, bytes]:
    raw = get_bytes(url)
    try:
        return json.loads(raw), raw
    except json.JSONDecodeError as exc:
        raise ImplementationFailure(f"invalid JSON from {url}: {exc}") from exc


def read_metadata() -> tuple[dict[str, Any], bytes]:
    obj, raw = get_json(f"{BASE}/api/views/{DATASET_ID}.json")
    if not isinstance(obj, dict) or not isinstance(obj.get("columns"), list):
        raise ImplementationFailure("unexpected Breakdowns metadata shape")
    return obj, raw


def soda_rows(fields: list[str]) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    total_bytes = 0
    select = ",".join(fields)
    for page in range(MAX_PAGES):
        params = urllib.parse.urlencode({"$select": select, "$limit": PAGE, "$offset": page * PAGE})
        obj, raw = get_json(f"{BASE}/resource/{DATASET_ID}.json?{params}")
        total_bytes += len(raw)
        if not isinstance(obj, list):
            raise ImplementationFailure("unexpected Breakdowns SODA row shape")
        rows.extend(r for r in obj if isinstance(r, dict))
        if len(obj) < PAGE:
            return rows, total_bytes
    raise ImplementationFailure("Breakdowns pagination safety limit exceeded")


def evidence(pass_: bool, text: str) -> dict[str, Any]:
    return {"pass": bool(pass_), "evidence": text}


def main() -> None:
    RESEARCH.mkdir(parents=True, exist_ok=True)
    contract = CONTRACT.read_text(encoding="utf-8")
    checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    if checkpoint.get("active_issue") != ISSUE or checkpoint.get("active_research") != "US-FTA-TRANSIT-N01":
        raise ImplementationFailure(f"N01 is not the canonical active mission: {checkpoint}")
    for required in [
        "status: CONTRACT_FROZEN_PRE_ISSUE",
        "17. No paid source/API/runner",
        PASS,
        HOLD,
        "safety_outcome_row_values_opened: false",
        "relationship_computed: false",
    ]:
        if required not in contract:
            raise ImplementationFailure(f"frozen contract assertion missing: {required}")

    meta, meta_raw = read_metadata()
    columns = {
        str(c.get("fieldName")): c
        for c in meta.get("columns", [])
        if isinstance(c, dict) and c.get("fieldName")
    }
    fields_present = all(f in columns for f in FIELDS)
    types_match = all(
        f in columns and str(columns[f].get("dataTypeName")) == EXPECTED_TYPES[f]
        for f in FIELDS
    )

    # Missing required schema is a valid scientific HOLD. Network/JSON failures above remain implementation failures.
    rows: list[dict[str, Any]] = []
    query_bytes = 0
    if fields_present:
        rows, query_bytes = soda_rows(FIELDS)

    # Source-grain rows are canonicalized first. Conflicting duplicates invalidate the source key.
    grouped: dict[tuple[str, str, str, int], list[tuple[str, float | None, str, float | None, str]]] = defaultdict(list)
    out_of_scope_rows = 0
    malformed_identity_rows = 0
    for row in rows:
        iid = norm_id(row.get("ntd_id"))
        mode = norm_mode(row.get("mode"))
        tos = norm_tos(row.get("type_of_service"))
        reporter = str(row.get("reporter_type") or "").strip()
        year = parse_year(row.get("report_year"))
        if not iid or not mode or not tos or year is None:
            malformed_identity_rows += 1
            continue
        if reporter != "Full Reporter" or tos not in {"DO", "PT"} or year not in {2022, 2023, 2024}:
            out_of_scope_rows += 1
            continue
        grouped[(iid, mode, tos, year)].append(
            (
                reporter,
                parse_number(row.get("major_mechanical_failures")),
                norm_flag(row.get("major_mechanical_failures_1")),
                parse_number(row.get("vehicle_passenger_car_revenue")),
                norm_flag(row.get("vehicle_passenger_car_miles_2")),
            )
        )

    canonical: dict[tuple[str, str, str, int], tuple[str, float | None, str, float | None, str]] = {}
    conflicting_keys: set[tuple[str, str, str, int]] = set()
    identical_duplicate_rows = 0
    for key, values in grouped.items():
        uniq = set(values)
        if len(uniq) > 1:
            conflicting_keys.add(key)
            continue
        if len(values) > 1:
            identical_duplicate_rows += len(values) - 1
        canonical[key] = values[0]

    # Build agency-mode-year support. Every present TOS component must be clean; no flagged component is dropped.
    amy_keys: dict[tuple[str, str, int], set[tuple[str, str, str, int]]] = defaultdict(set)
    for key in grouped:
        iid, mode, _tos, year = key
        amy_keys[(iid, mode, year)].add(key)

    exposure_aggs: dict[tuple[str, str, int], dict[str, Any]] = {}
    service_aggs: dict[tuple[str, str, int], dict[str, Any]] = {}
    quality_invalid_amys: set[tuple[str, str, int]] = set()
    numeric_invalid_amys: set[tuple[str, str, int]] = set()
    conflict_invalid_amys: set[tuple[str, str, int]] = set()

    for amy, keys in amy_keys.items():
        if any(k in conflicting_keys for k in keys):
            conflict_invalid_amys.add(amy)
            continue
        vals = [(k, canonical[k]) for k in keys if k in canonical]
        if len(vals) != len(keys):
            conflict_invalid_amys.add(amy)
            continue

        tos_profile = "+".join(sorted(k[2] for k, _v in vals))
        service_ok = True
        exposure_ok = True
        vrm_sum = 0.0
        major_sum = 0.0
        saw_quality_problem = False
        saw_numeric_problem = False
        for _key, (_reporter, major, major_flag, vrm, vrm_flag) in vals:
            if vrm_flag != "":
                service_ok = False
                exposure_ok = False
                saw_quality_problem = True
            if vrm is None or vrm <= 0:
                service_ok = False
                exposure_ok = False
                saw_numeric_problem = True
            if major_flag != "":
                exposure_ok = False
                saw_quality_problem = True
            if major is None or major < 0:
                exposure_ok = False
                saw_numeric_problem = True
            if vrm is not None:
                vrm_sum += vrm
            if major is not None:
                major_sum += major

        if saw_quality_problem:
            quality_invalid_amys.add(amy)
        if saw_numeric_problem:
            numeric_invalid_amys.add(amy)
        if service_ok and vrm_sum > 0:
            service_aggs[amy] = {"vrm": vrm_sum, "tos_profile": tos_profile}
        if exposure_ok and vrm_sum > 0:
            exposure_aggs[amy] = {
                "major_failures": major_sum,
                "vrm": vrm_sum,
                "tos_profile": tos_profile,
                "intensity": 1_000_000.0 * major_sum / vrm_sum,
            }

    # Earliest eligible cohort per native agency-mode.
    by_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for (iid, mode, year), exp in exposure_aggs.items():
        if year not in {2022, 2023}:
            continue
        follow = service_aggs.get((iid, mode, year + 1))
        if not follow or follow["tos_profile"] != exp["tos_profile"]:
            continue
        by_pair[(iid, mode)].append(
            {
                "ntd_id": iid,
                "mode": mode,
                "exposure_year": year,
                "followup_year": year + 1,
                "tos_profile": exp["tos_profile"],
                "major_failures": exp["major_failures"],
                "exposure_vrm": exp["vrm"],
                "followup_vrm": follow["vrm"],
                "intensity": exp["intensity"],
            }
        )

    earliest_pair_units: list[dict[str, Any]] = []
    for _pair, candidates in by_pair.items():
        earliest_pair_units.append(sorted(candidates, key=lambda x: x["exposure_year"])[0])

    # One unit per agency: largest exposure-year VRM, lexical mode, earlier exposure year.
    by_agency: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for unit in earliest_pair_units:
        by_agency[unit["ntd_id"]].append(unit)
    units: list[dict[str, Any]] = []
    for _iid, candidates in by_agency.items():
        chosen = sorted(
            candidates,
            key=lambda x: (-x["exposure_vrm"], x["mode"], x["exposure_year"]),
        )[0]
        units.append(chosen)

    # Frozen strata, quartiles, strict separation, then deterministic matching.
    strata: dict[tuple[str, int, str], list[dict[str, Any]]] = defaultdict(list)
    for unit in units:
        strata[(unit["mode"], unit["exposure_year"], unit["tos_profile"])].append(unit)

    eligible_strata: dict[tuple[str, int, str], dict[str, Any]] = {}
    dropped_small = 0
    dropped_no_separation = 0
    for stratum, members in strata.items():
        if len(members) < 12:
            dropped_small += 1
            continue
        ordered = sorted(members, key=lambda x: (x["intensity"], x["ntd_id"]))
        k = len(ordered) // 4
        lows = ordered[:k]
        highs = ordered[-k:]
        if not lows or not highs or min(x["intensity"] for x in highs) <= max(x["intensity"] for x in lows):
            dropped_no_separation += 1
            continue
        eligible_strata[stratum] = {"n": len(ordered), "k": k, "lows": lows, "highs": highs}

    pairs: list[dict[str, Any]] = []
    for stratum in sorted(eligible_strata):
        info = eligible_strata[stratum]
        unused = {x["ntd_id"]: x for x in info["lows"]}
        highs = sorted(info["highs"], key=lambda x: (-x["intensity"], x["ntd_id"]))
        for high in highs:
            if not unused:
                break
            low = min(
                unused.values(),
                key=lambda x: (
                    abs(math.log10(high["exposure_vrm"]) - math.log10(x["exposure_vrm"])),
                    abs(math.log10(high["followup_vrm"]) - math.log10(x["followup_vrm"])),
                    x["ntd_id"],
                ),
            )
            del unused[low["ntd_id"]]
            exp_distance = abs(math.log10(high["exposure_vrm"]) - math.log10(low["exposure_vrm"]))
            fol_distance = abs(math.log10(high["followup_vrm"]) - math.log10(low["followup_vrm"]))
            pairs.append(
                {
                    "high_ntd_id": high["ntd_id"],
                    "low_ntd_id": low["ntd_id"],
                    "mode": high["mode"],
                    "exposure_year": high["exposure_year"],
                    "followup_year": high["followup_year"],
                    "tos_profile": high["tos_profile"],
                    "high_major_failures": high["major_failures"],
                    "low_major_failures": low["major_failures"],
                    "high_exposure_vrm": high["exposure_vrm"],
                    "low_exposure_vrm": low["exposure_vrm"],
                    "high_followup_vrm": high["followup_vrm"],
                    "low_followup_vrm": low["followup_vrm"],
                    "high_intensity_per_million_vrm": high["intensity"],
                    "low_intensity_per_million_vrm": low["intensity"],
                    "exposure_log10_vrm_distance": exp_distance,
                    "followup_log10_vrm_distance": fol_distance,
                }
            )

    # Pair IDs are assigned only after the outcome-blind matching is frozen.
    manifest: list[dict[str, Any]] = []
    for idx, pair in enumerate(pairs, 1):
        manifest.append({"pair_id": f"FTA-N01-P{idx:04d}", **pair})
    manifest_bytes = canonical_json_bytes(manifest)
    manifest_sha = sha256_bytes(manifest_bytes)
    MANIFEST.write_bytes(manifest_bytes)

    matched_modes = sorted({p["mode"] for p in manifest})
    all_ids = [x for p in manifest for x in (p["high_ntd_id"], p["low_ntd_id"])]
    no_reuse = len(all_ids) == len(set(all_ids))
    strict_pairs = all(
        p["high_intensity_per_million_vrm"] > p["low_intensity_per_million_vrm"]
        for p in manifest
    )
    balanced = 0
    for p in manifest:
        r0 = p["high_exposure_vrm"] / p["low_exposure_vrm"]
        r1 = p["high_followup_vrm"] / p["low_followup_vrm"]
        if (1 / 3) <= r0 <= 3 and (1 / 3) <= r1 <= 3:
            balanced += 1
    balance_fraction = balanced / len(manifest) if manifest else 0.0

    schema_semantics_ok = fields_present and types_match
    exact_scope_ok = malformed_identity_rows == 0 and out_of_scope_rows == 0
    conflict_exclusion_ok = True
    for unit in units:
        for year in (unit["exposure_year"], unit["followup_year"]):
            amy = (unit["ntd_id"], unit["mode"], year)
            if amy in conflict_invalid_amys:
                conflict_exclusion_ok = False

    checks = {
        "1": evidence(fields_present and len(rows) > 0, f"Official {DATASET_ID} metadata and actual rows readable; rows={len(rows)}."),
        "2": evidence(schema_semantics_ok, f"Frozen fields present={fields_present}; exact metadata types match={types_match}."),
        "3": evidence(exact_scope_ok, f"Malformed identity rows={malformed_identity_rows}; out-of-scope rows={out_of_scope_rows}; exact Full Reporter/DO-PT/2022-2024 rule enforced."),
        "4": evidence(True, f"Whole agency-mode-year fail-closed quality rule enforced; quality-invalid agency-mode-years={len(quality_invalid_amys)}."),
        "5": evidence(conflict_exclusion_ok, f"Conflicting source-grain keys={len(conflicting_keys)}; conflict-invalid agency-mode-years={len(conflict_invalid_amys)}; none included in retained units={conflict_exclusion_ok}."),
        "6": evidence(len(units) >= 400, f"Unique retained agencies after temporal eligibility and one-unit-per-agency={len(units)} (>=400 required)."),
        "7": evidence(len(eligible_strata) >= 8, f"Design-eligible strict-separation strata={len(eligible_strata)} (>=8 required)."),
        "8": evidence(len(manifest) >= 100, f"Deterministic HIGH/LOW matched pairs={len(manifest)} (>=100 required)."),
        "9": evidence(len(matched_modes) >= 5, f"Distinct matched mode codes={len(matched_modes)}: {matched_modes} (>=5 required)."),
        "10": evidence(balance_fraction >= 0.80, f"Pairs with both exposure/follow-up HIGH:LOW VRM ratios in [1/3,3]={balanced}/{len(manifest)}={balance_fraction:.6f} (>=0.80 required)."),
        "11": evidence(strict_pairs, f"Every final pair has HIGH intensity > LOW intensity={strict_pairs}."),
        "12": evidence(no_reuse, f"No NTD ID reused in final manifest={no_reuse}; manifest identities={len(all_ids)}, unique={len(set(all_ids))}."),
        "13": evidence(bool(manifest_sha) and sha256_bytes(MANIFEST.read_bytes()) == manifest_sha, f"Canonical pair manifest SHA-256={manifest_sha}."),
        "14": evidence(True, "major_safety_event_row_values_opened=false; runner has no safety-event dataset endpoint."),
        "15": evidence(True, "future_safety_event_membership_opened=false."),
        "16": evidence(True, "relationship_computed=false; predictive_metric_computed=false; causal_claim_made=false."),
        "17": evidence(True, "Official zero-cost DOT/FTA source and standard public GitHub runner only; incremental monetary cost=0 USD."),
    }
    disposition = PASS if all(v["pass"] for v in checks.values()) else HOLD

    strata_summary = []
    for key in sorted(eligible_strata):
        info = eligible_strata[key]
        strata_summary.append(
            {
                "mode": key[0],
                "exposure_year": key[1],
                "tos_profile": key[2],
                "n": info["n"],
                "quartile_k": info["k"],
                "low_max_intensity": max(x["intensity"] for x in info["lows"]),
                "high_min_intensity": min(x["intensity"] for x in info["highs"]),
            }
        )

    result = {
        "protocol": "US-FTA-TRANSIT-N01",
        "issue": ISSUE,
        "contract_commit": CONTRACT_COMMIT,
        "evaluated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "valid_evaluation": True,
        "disposition": disposition,
        "incremental_monetary_cost_usd": 0,
        "source_evidence": {
            "dataset_id": DATASET_ID,
            "metadata_name": meta.get("name"),
            "metadata_bytes": len(meta_raw),
            "metadata_sha256": sha256_bytes(meta_raw),
            "query_bytes": query_bytes,
            "rows_read": len(rows),
            "authorized_fields": FIELDS,
        },
        "diagnostics": {
            "source_grain_keys": len(grouped),
            "canonical_source_grain_keys": len(canonical),
            "identical_duplicate_rows": identical_duplicate_rows,
            "conflicting_source_grain_keys": len(conflicting_keys),
            "quality_invalid_agency_mode_years": len(quality_invalid_amys),
            "numeric_invalid_agency_mode_years": len(numeric_invalid_amys),
            "conflict_invalid_agency_mode_years": len(conflict_invalid_amys),
            "valid_exposure_agency_mode_years": len(exposure_aggs),
            "valid_service_agency_mode_years": len(service_aggs),
            "earliest_eligible_agency_modes": len(earliest_pair_units),
            "retained_unique_agencies": len(units),
            "all_strata": len(strata),
            "dropped_small_strata": dropped_small,
            "dropped_no_strict_separation_strata": dropped_no_separation,
            "design_eligible_strata": len(eligible_strata),
            "matched_pairs": len(manifest),
            "matched_modes": matched_modes,
            "vrm_balanced_pairs": balanced,
            "vrm_balance_fraction": balance_fraction,
            "eligible_strata_summary": strata_summary,
        },
        "manifest": {
            "path": "research/US-FTA-TRANSIT-N01/PAIR_MANIFEST.json",
            "sha256": manifest_sha,
            "pairs": len(manifest),
        },
        "boundaries": {
            "major_safety_event_row_values_opened": False,
            "future_safety_event_membership_opened": False,
            "row_level_breakdown_event_join_persisted": False,
            "relationship_computed": False,
            "predictive_metric_computed": False,
            "causal_claim_made": False,
            "manual_or_fuzzy_identity_repair_used": False,
        },
        "checks": checks,
    }
    OUT.write_bytes(canonical_json_bytes(result))
    print(disposition)
    print(f"retained_agencies={len(units)}")
    print(f"eligible_strata={len(eligible_strata)}")
    print(f"matched_pairs={len(manifest)}")
    print(f"matched_modes={matched_modes}")
    print(f"vrm_balance_fraction={balance_fraction:.6f}")
    print(f"manifest_sha256={manifest_sha}")
    print("failed_checks=", [k for k, v in checks.items() if not v["pass"]])


if __name__ == "__main__":
    main()
