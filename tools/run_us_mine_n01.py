#!/usr/bin/env python3
from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import math
import urllib.request
import zipfile
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-MINE-N01"
F01_AUDIT = ROOT / "research" / "US-MINE-F01" / "STAGING_SOURCE_AUDIT.json"
BASE = "https://arlweb.msha.gov/OpenGovernmentData/DataSets/"
START_YEAR = 2019
END_YEAR = 2025
ISSUE = 135

SOURCES = {
    "mines": ("Mines.zip", "Mines_Definition_File.txt"),
    "employment": ("MinesProdQuarterly.zip", "MineSProdQuarterly_Definition_File.txt"),
}
MINE_FIELDS = ["MINE_ID", "COAL_METAL_IND", "STATE"]
EMP_FIELDS = ["MINE_ID", "SUBUNIT_CD", "CAL_YR", "CAL_QTR", "HOURS_WORKED", "COAL_METAL_IND"]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-Innovative-Research-Engine/US-MINE-N01"})
    with urllib.request.urlopen(req, timeout=180) as response:
        return response.read()


def decode_text(data: bytes) -> str:
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            pass
    raise AssertionError("unable to decode source text")


def extract_single_table(zip_bytes: bytes) -> tuple[str, bytes]:
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        assert members, "empty ZIP"
        candidates = [(len(zf.read(n)), n, zf.read(n)) for n in members]
        _, name, data = max(candidates)
        return name, data


def iter_selected(table_bytes: bytes, selected: list[str]):
    rdr = csv.reader(io.StringIO(decode_text(table_bytes)), delimiter="|")
    header = [h.strip().lstrip("\ufeff") for h in next(rdr)]
    missing = [f for f in selected if f not in header]
    assert not missing, f"missing fields: {missing}"
    idx = {f: header.index(f) for f in selected}
    for row in rdr:
        if not row:
            continue
        if len(row) < len(header):
            row += [""] * (len(header) - len(row))
        yield {f: row[i].strip() if i < len(row) else "" for f, i in idx.items()}


def yq_tuple(y: str, q: str) -> tuple[int, int] | None:
    try:
        yi, qi = int(y), int(q)
    except (TypeError, ValueError):
        return None
    if START_YEAR <= yi <= END_YEAR and 1 <= qi <= 4:
        return yi, qi
    return None


def ordinal(y: int, q: int) -> int:
    return y * 4 + (q - 1)


def from_ordinal(value: int) -> tuple[int, int]:
    return value // 4, value % 4 + 1


def nearest_rank(values: list[float], p: float) -> float:
    assert values
    xs = sorted(values)
    i = max(0, min(len(xs) - 1, math.ceil(p * len(xs)) - 1))
    return xs[i]


def assign_decile(value: float, cutpoints: list[float]) -> int:
    # Equality remains in the lower decile.
    decile = 1
    for cp in cutpoints:
        if value > cp:
            decile += 1
        else:
            break
    return decile


def fmt_decimal(value: Decimal) -> str:
    if value == value.to_integral():
        return str(value.quantize(Decimal("1")))
    return format(value.normalize(), "f")


def main() -> None:
    expected = json.loads(F01_AUDIT.read_text(encoding="utf-8"))["source_manifest"]
    manifest: dict[str, dict] = {}
    tables: dict[str, bytes] = {}
    source_hash_match = True

    for label, (zip_name, def_name) in SOURCES.items():
        zb = download(BASE + zip_name)
        db = download(BASE + def_name)
        member_name, tb = extract_single_table(zb)
        actual = {
            "zip_url": BASE + zip_name,
            "zip_sha256": sha256(zb),
            "member_name": member_name,
            "member_sha256": sha256(tb),
            "definition_url": BASE + def_name,
            "definition_sha256": sha256(db),
        }
        exp = expected[label]
        actual["matches_f01"] = (
            actual["zip_sha256"] == exp["zip_sha256"]
            and actual["member_name"] == exp["member_name"]
            and actual["member_sha256"] == exp["member_sha256"]
            and actual["definition_sha256"] == exp["definition_sha256"]
        )
        source_hash_match = source_hash_match and actual["matches_f01"]
        manifest[label] = actual
        tables[label] = tb

    OUT.mkdir(parents=True, exist_ok=True)

    if not source_hash_match:
        result = {
            "research_id": "US-MINE-N01",
            "issue": ISSUE,
            "gate": "HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT",
            "source_hash_match_f01": False,
            "source_manifest": manifest,
            "hold_reason": "HOLD_SOURCE_DRIFT",
            "accident_source_read": False,
            "injury_outcome_values_opened": False,
            "production_magnitude_parsed": False,
            "relationship_computed": False,
            "incremental_monetary_cost_usd": 0,
        }
        (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"gate": result["gate"], "hold_reason": result["hold_reason"]}))
        return

    mine_by_id: dict[str, tuple[str, str]] = {}
    mine_conflicts = 0
    for r in iter_selected(tables["mines"], MINE_FIELDS):
        mid = r["MINE_ID"]
        if not mid:
            continue
        sig = (r["COAL_METAL_IND"], r["STATE"])
        if mid in mine_by_id and mine_by_id[mid] != sig:
            mine_conflicts += 1
        else:
            mine_by_id[mid] = sig

    # Exact subunit rows are de-duplicated before mine-quarter aggregation.
    subunit_rows: dict[tuple[str, int, int, str], tuple[str, Decimal]] = {}
    conflicting_subunit_rows = 0
    invalid_hours_values = 0
    for r in iter_selected(tables["employment"], EMP_FIELDS):
        yq = yq_tuple(r["CAL_YR"], r["CAL_QTR"])
        if yq is None or not r["MINE_ID"] or not r["SUBUNIT_CD"]:
            continue
        raw = r["HOURS_WORKED"].replace(",", "").strip()
        if not raw:
            continue
        try:
            hours = Decimal(raw)
        except InvalidOperation:
            invalid_hours_values += 1
            continue
        key = (r["MINE_ID"], yq[0], yq[1], r["SUBUNIT_CD"])
        sig = (r["COAL_METAL_IND"], hours)
        if key in subunit_rows:
            if subunit_rows[key] != sig:
                conflicting_subunit_rows += 1
        else:
            subunit_rows[key] = sig

    mq_hours: dict[tuple[str, int, int], Decimal] = defaultdict(lambda: Decimal(0))
    mq_sectors: dict[tuple[str, int, int], set[str]] = defaultdict(set)
    for (mid, y, q, _sub), (sector, hours) in subunit_rows.items():
        mq_hours[(mid, y, q)] += hours
        mq_sectors[(mid, y, q)].add(sector)

    conflicting_mq_sector = sum(1 for sectors in mq_sectors.values() if len(sectors) != 1)
    sector_mine_mismatches = 0
    quarter: dict[tuple[str, int], dict] = {}
    for (mid, y, q), hours in mq_hours.items():
        sectors = mq_sectors[(mid, y, q)]
        if len(sectors) != 1:
            continue
        sector = next(iter(sectors))
        mine = mine_by_id.get(mid)
        if mine is None:
            continue
        mine_sector, state = mine
        if mine_sector and sector and mine_sector != sector:
            sector_mine_mismatches += 1
            continue
        quarter[(mid, ordinal(y, q))] = {
            "mine_id": mid,
            "year": y,
            "quarter": q,
            "sector": sector,
            "state": state,
            "hours": hours,
        }

    eligible: list[dict] = []
    eligible_mines: set[str] = set()
    for (mid, o), cur in sorted(quarter.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        prev = quarter.get((mid, o - 1))
        nxt = quarter.get((mid, o + 1))
        if prev is None or nxt is None:
            continue
        if not (prev["hours"] > 0 and cur["hours"] > 0 and nxt["hours"] > 0):
            continue
        if not (prev["sector"] == cur["sector"] == nxt["sector"]):
            continue
        if not cur["state"]:
            continue
        ramp = math.log(float(cur["hours"] / prev["hours"]))
        obs = {
            "mine_id": mid,
            "year": cur["year"],
            "quarter": cur["quarter"],
            "ordinal": o,
            "sector": cur["sector"],
            "state": cur["state"],
            "hours_prev": prev["hours"],
            "hours_t": cur["hours"],
            "hours_next": nxt["hours"],
            "ramp": ramp,
        }
        eligible.append(obs)
        eligible_mines.add(mid)

    strata: dict[tuple[str, int, int], list[dict]] = defaultdict(list)
    for obs in eligible:
        strata[(obs["sector"], obs["year"], obs["quarter"])].append(obs)

    candidates: list[dict] = []
    strata_summary = []
    for key in sorted(strata):
        rows = strata[key]
        ramps = [x["ramp"] for x in rows]
        q40 = nearest_rank(ramps, 0.40)
        q60 = nearest_rank(ramps, 0.60)
        q80 = nearest_rank(ramps, 0.80)
        baseline_logs = [math.log(float(x["hours_prev"])) for x in rows]
        decile_cuts = [nearest_rank(baseline_logs, p / 10.0) for p in range(1, 10)]
        exp_n = 0
        ctl_n = 0
        for x in rows:
            baseline_log = math.log(float(x["hours_prev"]))
            role = None
            if x["ramp"] > 0 and x["ramp"] >= q80:
                role = "EXPOSED"
                exp_n += 1
            elif q40 <= x["ramp"] <= q60:
                role = "CONTROL"
                ctl_n += 1
            if role:
                y = dict(x)
                y["role"] = role
                y["baseline_log"] = baseline_log
                y["baseline_decile"] = assign_decile(baseline_log, decile_cuts)
                candidates.append(y)
        strata_summary.append({
            "sector": key[0], "year": key[1], "quarter": key[2],
            "eligible": len(rows), "exposed_candidates": exp_n, "control_candidates": ctl_n,
            "q40_ramp": q40, "q60_ramp": q60, "q80_ramp": q80,
        })

    # Earliest eligible candidate role per mine, frozen before matching.
    first_role: dict[str, dict] = {}
    for c in sorted(candidates, key=lambda x: (x["ordinal"], x["mine_id"], x["role"])):
        first_role.setdefault(c["mine_id"], c)
    role_rows = list(first_role.values())
    role_counts = Counter((x["sector"], x["role"]) for x in role_rows)

    control_pools: dict[tuple[str, int, int, str, int], list[dict]] = defaultdict(list)
    exposed_rows: list[dict] = []
    for x in role_rows:
        key = (x["sector"], x["year"], x["quarter"], x["state"], x["baseline_decile"])
        if x["role"] == "CONTROL":
            control_pools[key].append(x)
        else:
            exposed_rows.append(x)
    for pool in control_pools.values():
        pool.sort(key=lambda x: (x["baseline_log"], x["mine_id"]))

    used_controls: set[str] = set()
    pairs: list[dict] = []
    for e in sorted(exposed_rows, key=lambda x: (x["ordinal"], x["mine_id"])):
        key = (e["sector"], e["year"], e["quarter"], e["state"], e["baseline_decile"])
        available = [c for c in control_pools.get(key, []) if c["mine_id"] not in used_controls]
        if not available:
            continue
        c = min(available, key=lambda x: (abs(x["baseline_log"] - e["baseline_log"]), x["mine_id"]))
        used_controls.add(c["mine_id"])
        pairs.append({
            "sector": e["sector"],
            "state": e["state"],
            "year": e["year"],
            "quarter": e["quarter"],
            "baseline_decile": e["baseline_decile"],
            "exposed_mine_id": e["mine_id"],
            "control_mine_id": c["mine_id"],
            "exposed_ramp_log": round(e["ramp"], 12),
            "control_ramp_log": round(c["ramp"], 12),
            "exposed_hours_prev": fmt_decimal(e["hours_prev"]),
            "exposed_hours_t": fmt_decimal(e["hours_t"]),
            "exposed_hours_next": fmt_decimal(e["hours_next"]),
            "control_hours_prev": fmt_decimal(c["hours_prev"]),
            "control_hours_t": fmt_decimal(c["hours_t"]),
            "control_hours_next": fmt_decimal(c["hours_next"]),
        })

    pair_lines = [json.dumps(p, sort_keys=True, separators=(",", ":"), ensure_ascii=False) for p in pairs]
    pair_bytes = (("\n".join(pair_lines) + "\n") if pair_lines else "").encode("utf-8")
    pair_sha = sha256(pair_bytes)
    (OUT / "PAIR_IDENTITIES.jsonl.gz").write_bytes(gzip.compress(pair_bytes, compresslevel=9, mtime=0))

    pair_sector = Counter(p["sector"] for p in pairs)
    pair_states = {p["state"] for p in pairs}
    both_candidate_support = all(role_counts[(s, "EXPOSED")] > 0 and role_counts[(s, "CONTROL")] > 0 for s in ("C", "M"))

    req = {
        "source_hash_match_f01": source_hash_match,
        "mine_identity_no_conflicts": mine_conflicts == 0,
        "employment_subunit_no_conflicts": conflicting_subunit_rows == 0,
        "mine_quarter_sector_no_conflicts": conflicting_mq_sector == 0,
        "sector_matches_mines": sector_mine_mismatches == 0,
        "hours_values_parseable": invalid_hours_values == 0,
        "eligible_mines_ge_8000": len(eligible_mines) >= 8000,
        "both_sectors_have_exposed_and_control": both_candidate_support,
        "matched_pairs_ge_2000": len(pairs) >= 2000,
        "matched_states_ge_30": len(pair_states) >= 30,
        "coal_pairs_ge_300": pair_sector.get("C", 0) >= 300,
        "metal_nonmetal_pairs_ge_300": pair_sector.get("M", 0) >= 300,
        "accident_source_not_read": True,
        "injury_outcomes_not_opened": True,
        "production_magnitude_not_parsed": True,
        "relationship_not_computed": True,
    }

    hard_design = (
        source_hash_match and mine_conflicts == 0 and conflicting_subunit_rows == 0
        and conflicting_mq_sector == 0 and sector_mine_mismatches == 0 and invalid_hours_values == 0
        and len(eligible) > 0 and both_candidate_support
    )
    if all(req.values()):
        gate = "PASS_US_MINE_N01_HOURS_RAMP_MATCHED_DESIGN_IDENTIFIABLE"
    elif hard_design and len(pairs) > 0:
        gate = "PARTIAL_US_MINE_N01_EXPOSURE_IDENTIFIABLE__MATCH_SUPPORT_PENDING"
    else:
        gate = "HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT"

    result = {
        "research_id": "US-MINE-N01",
        "issue": ISSUE,
        "gate": gate,
        "support_window": {"start_year": START_YEAR, "end_year": END_YEAR},
        "exposure_family": "ALL_SECTOR_OPERATOR_HOURS_RAMP_UP",
        "source_manifest": manifest,
        "source_hash_match_f01": source_hash_match,
        "structural_diagnostics": {
            "mine_identity_conflicts": mine_conflicts,
            "employment_conflicting_subunit_rows": conflicting_subunit_rows,
            "mine_quarter_sector_conflicts": conflicting_mq_sector,
            "sector_mine_mismatches": sector_mine_mismatches,
            "invalid_hours_values": invalid_hours_values,
            "aggregated_mine_quarters": len(quarter),
            "eligible_three_quarter_observations": len(eligible),
            "eligible_mines": len(eligible_mines),
        },
        "candidate_support": {
            "first_role_mines": len(role_rows),
            "counts_by_sector_role": {f"{k[0]}_{k[1]}": v for k, v in sorted(role_counts.items())},
        },
        "matching": {
            "pairs": len(pairs),
            "pairs_by_sector": dict(sorted(pair_sector.items())),
            "states": len(pair_states),
            "pair_identity_sha256": pair_sha,
            "pair_identity_file": "research/US-MINE-N01/PAIR_IDENTITIES.jsonl.gz",
        },
        "requirements": req,
        "strata_summary": strata_summary,
        "accident_source_read": False,
        "injury_outcome_values_opened": False,
        "production_magnitude_parsed": False,
        "relationship_computed": False,
        "post_execution_rescue_used": False,
        "incremental_monetary_cost_usd": 0,
    }
    audit = {
        "research_id": "US-MINE-N01",
        "issue": ISSUE,
        "selected_fields": {"mines": MINE_FIELDS, "employment": EMP_FIELDS},
        "accident_source_read": False,
        "injury_outcome_values_opened": False,
        "production_magnitude_parsed": False,
        "source_manifest": manifest,
        "pair_identity_sha256": pair_sha,
        "raw_source_bytes_persisted": False,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "gate": gate,
        "eligible_mines": len(eligible_mines),
        "pairs": len(pairs),
        "pairs_by_sector": dict(pair_sector),
        "states": len(pair_states),
        "pair_identity_sha256": pair_sha,
        "accident_source_read": False,
        "injury_outcome_values_opened": False,
        "relationship_computed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
