#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-MINE-F01"
START_YEAR = 2019
END_YEAR = 2025
BASE = "https://arlweb.msha.gov/OpenGovernmentData/DataSets/"

SOURCES = {
    "mines": ("Mines.zip", "Mines_Definition_File.txt"),
    "employment": ("MinesProdQuarterly.zip", "MineSProdQuarterly_Definition_File.txt"),
    "accidents": ("Accidents.zip", "Accidents_Definition_File.txt"),
}

MINE_FIELDS = ["MINE_ID", "COAL_METAL_IND", "STATE"]
EMP_FIELDS = ["MINE_ID", "SUBUNIT_CD", "CAL_YR", "CAL_QTR", "HOURS_WORKED", "COAL_PRODUCTION", "COAL_METAL_IND"]
ACC_FIELDS = ["MINE_ID", "DOCUMENT_NO", "SUBUNIT_CD", "CAL_YR", "CAL_QTR", "CONTRACTOR_ID", "COAL_METAL_IND"]
FORBIDDEN_ACC_FIELDS = {
    "DEGREE_INJURY_CD", "DEGREE_INJURY", "NO_INJURIES", "DAYS_RESTRICT", "DAYS_LOST",
    "SCHEDULE_CHARGE", "CLASSIFICATION_CD", "CLASSIFICATION", "ACCIDENT_TYPE_CD", "ACCIDENT_TYPE",
    "INJURY_SOURCE_CD", "INJURY_SOURCE", "NATURE_INJURY_CD", "NATURE_INJURY",
    "INJ_BODY_PART_CD", "INJ_BODY_PART", "RETURN_TO_WORK_DT",
}
assert not (set(ACC_FIELDS) & FORBIDDEN_ACC_FIELDS)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "AI-Innovative-Research-Engine/US-MINE-F01"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read()


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
        candidates = []
        for n in members:
            b = zf.read(n)
            candidates.append((len(b), n, b))
        _, name, data = max(candidates)
        return name, data


def iter_selected(table_bytes: bytes, selected: list[str]):
    text = decode_text(table_bytes)
    rdr = csv.reader(io.StringIO(text), delimiter="|")
    header = next(rdr)
    header = [h.strip().lstrip("\ufeff") for h in header]
    missing = [f for f in selected if f not in header]
    assert not missing, f"missing fields: {missing}"
    idx = {f: header.index(f) for f in selected}
    for row in rdr:
        if not row:
            continue
        if len(row) < len(header):
            row += [""] * (len(header) - len(row))
        yield {f: row[i].strip() if i < len(row) else "" for f, i in idx.items()}


def valid_year_quarter(y: str, q: str) -> tuple[int, int] | None:
    try:
        yi, qi = int(y), int(q)
    except (TypeError, ValueError):
        return None
    if not (START_YEAR <= yi <= END_YEAR and 1 <= qi <= 4):
        return None
    return yi, qi


def main() -> None:
    manifest = {}
    tables = {}
    definitions = {}
    for label, (zip_name, def_name) in SOURCES.items():
        zip_url = BASE + zip_name
        def_url = BASE + def_name
        zb = download(zip_url)
        db = download(def_url)
        member_name, tb = extract_single_table(zb)
        manifest[label] = {
            "zip_url": zip_url,
            "zip_sha256": sha256(zb),
            "zip_bytes": len(zb),
            "member_name": member_name,
            "member_sha256": sha256(tb),
            "member_bytes": len(tb),
            "definition_url": def_url,
            "definition_sha256": sha256(db),
            "definition_bytes": len(db),
        }
        tables[label] = tb
        definitions[label] = decode_text(db)

    # Definition/source schema identity only; no forbidden outcome values are selected.
    for f in MINE_FIELDS:
        assert f in definitions["mines"]
    for f in EMP_FIELDS:
        assert f in definitions["employment"]
    for f in ACC_FIELDS:
        assert f in definitions["accidents"]

    mine_by_id: dict[str, tuple[str, str]] = {}
    mine_rows = 0
    mine_duplicate_ids = 0
    mine_conflicting_ids = 0
    for r in iter_selected(tables["mines"], MINE_FIELDS):
        mine_rows += 1
        mid = r["MINE_ID"]
        if not mid:
            continue
        sig = (r["COAL_METAL_IND"], r["STATE"])
        if mid in mine_by_id:
            mine_duplicate_ids += 1
            if mine_by_id[mid] != sig:
                mine_conflicting_ids += 1
        else:
            mine_by_id[mid] = sig

    emp_keys: dict[tuple[str, int, int, str], tuple[str, bool, bool]] = {}
    emp_rows_window = 0
    emp_duplicate_keys = 0
    emp_conflicting_keys = 0
    emp_mine_quarters: dict[str, set[tuple[int, int]]] = defaultdict(set)
    sector_rows = defaultdict(int)
    sector_hours_nonblank = defaultdict(int)
    sector_production_nonblank = defaultdict(int)
    for r in iter_selected(tables["employment"], EMP_FIELDS):
        yq = valid_year_quarter(r["CAL_YR"], r["CAL_QTR"])
        if yq is None or not r["MINE_ID"] or not r["SUBUNIT_CD"]:
            continue
        y, q = yq
        emp_rows_window += 1
        mid = r["MINE_ID"]
        sector = r["COAL_METAL_IND"]
        hours_nb = bool(r["HOURS_WORKED"])
        prod_nb = bool(r["COAL_PRODUCTION"])
        key = (mid, y, q, r["SUBUNIT_CD"])
        sig = (sector, hours_nb, prod_nb)
        if key in emp_keys:
            emp_duplicate_keys += 1
            if emp_keys[key] != sig:
                emp_conflicting_keys += 1
        else:
            emp_keys[key] = sig
        emp_mine_quarters[mid].add((y, q))
        sector_rows[sector] += 1
        sector_hours_nonblank[sector] += int(hours_nb)
        sector_production_nonblank[sector] += int(prod_nb)

    repeated_emp_mines = {m for m, qs in emp_mine_quarters.items() if len(qs) >= 2}
    sector_hours_rate = {
        s: (sector_hours_nonblank[s] / sector_rows[s] if sector_rows[s] else 0.0)
        for s in sorted(sector_rows)
    }
    sector_prod_rate = {
        s: (sector_production_nonblank[s] / sector_rows[s] if sector_rows[s] else 0.0)
        for s in sorted(sector_rows)
    }

    accident_rows_window = 0
    operator_accident_records = 0
    operator_accident_keys: set[tuple[str, int, int, str]] = set()
    accident_document_ids: set[str] = set()
    duplicate_document_ids = 0
    for r in iter_selected(tables["accidents"], ACC_FIELDS):
        yq = valid_year_quarter(r["CAL_YR"], r["CAL_QTR"])
        if yq is None:
            continue
        accident_rows_window += 1
        doc = r["DOCUMENT_NO"]
        if doc:
            if doc in accident_document_ids:
                duplicate_document_ids += 1
            accident_document_ids.add(doc)
        # Structural operator attribution only; no injury outcome field is accessed.
        if r["CONTRACTOR_ID"]:
            continue
        mid, sub = r["MINE_ID"], r["SUBUNIT_CD"]
        if not mid or not sub:
            continue
        y, q = yq
        operator_accident_records += 1
        operator_accident_keys.add((mid, y, q, sub))

    overlap_keys = operator_accident_keys & set(emp_keys)
    overlap_rate = len(overlap_keys) / len(operator_accident_keys) if operator_accident_keys else 0.0
    overlap_mines = {k[0] for k in overlap_keys}
    overlap_states = {mine_by_id[m][1] for m in overlap_mines if m in mine_by_id and mine_by_id[m][1]}

    req = {
        "sources_accessible": len(manifest) == 3,
        "mine_id_unique": mine_duplicate_ids == 0 and mine_conflicting_ids == 0,
        "employment_key_no_conflicts": emp_conflicting_keys == 0,
        "repeated_operator_mines_ge_3000": len(repeated_emp_mines) >= 3000,
        "both_c_and_m_present": sector_rows.get("C", 0) > 0 and sector_rows.get("M", 0) > 0,
        "hours_nonblank_c_ge_95pct": sector_hours_rate.get("C", 0.0) >= 0.95,
        "hours_nonblank_m_ge_95pct": sector_hours_rate.get("M", 0.0) >= 0.95,
        "operator_accident_key_overlap_ge_80pct": overlap_rate >= 0.80,
        "overlap_states_ge_30": len(overlap_states) >= 30,
        "production_scope_restricted": True,
        "prohibited_outcome_fields_accessed": False,
        "relationship_computed": False,
    }

    hard_identity = (
        req["sources_accessible"] and req["mine_id_unique"] and req["employment_key_no_conflicts"]
        and len(emp_keys) > 0 and len(operator_accident_keys) > 0
    )
    if all(req.values()):
        gate = "PASS_US_MINE_F01_STRUCTURAL_JOIN_READY__PRODUCTION_SCOPE_RESTRICTED"
    elif hard_identity:
        gate = "PARTIAL_US_MINE_F01_IDENTITY_READY__JOIN_OR_HOURS_SUPPORT_PENDING"
    else:
        gate = "HOLD_US_MINE_F01_SOURCE_OR_IDENTITY_SUPPORT"

    result = {
        "research_id": "US-MINE-F01",
        "issue": 134,
        "support_window": {"start_year": START_YEAR, "end_year": END_YEAR},
        "gate": gate,
        "source_manifest": manifest,
        "mine_identity": {
            "rows": mine_rows,
            "distinct_mine_ids": len(mine_by_id),
            "duplicate_mine_id_rows": mine_duplicate_ids,
            "conflicting_mine_ids": mine_conflicting_ids,
        },
        "employment_structural_support": {
            "window_rows": emp_rows_window,
            "distinct_keys": len(emp_keys),
            "duplicate_key_rows": emp_duplicate_keys,
            "conflicting_duplicate_keys": emp_conflicting_keys,
            "distinct_mines": len(emp_mine_quarters),
            "mines_with_ge_2_distinct_quarters": len(repeated_emp_mines),
            "sector_rows": dict(sorted(sector_rows.items())),
            "hours_worked_nonblank_rate_by_sector": sector_hours_rate,
            "coal_production_nonblank_rate_by_sector": sector_prod_rate,
            "hours_worked_magnitude_parsed": False,
            "coal_production_magnitude_parsed": False,
        },
        "accident_structural_support": {
            "window_records": accident_rows_window,
            "operator_attributed_valid_records": operator_accident_records,
            "distinct_operator_mine_quarter_subunit_keys": len(operator_accident_keys),
            "distinct_document_ids": len(accident_document_ids),
            "duplicate_document_ids": duplicate_document_ids,
            "exact_employment_overlap_keys": len(overlap_keys),
            "exact_employment_overlap_rate": overlap_rate,
            "overlapping_mine_ids": len(overlap_mines),
            "overlapping_states": len(overlap_states),
        },
        "requirements": req,
        "production_scope_restricted": True,
        "injury_outcome_values_opened": False,
        "prohibited_outcome_fields_accessed": False,
        "relationship_computed": False,
        "post_execution_rescue_used": False,
        "incremental_monetary_cost_usd": 0,
    }
    audit = {
        "research_id": "US-MINE-F01",
        "issue": 134,
        "selected_fields": {
            "mines": MINE_FIELDS,
            "employment": EMP_FIELDS,
            "accidents": ACC_FIELDS,
        },
        "forbidden_accident_fields": sorted(FORBIDDEN_ACC_FIELDS),
        "forbidden_fields_selected": sorted(set(ACC_FIELDS) & FORBIDDEN_ACC_FIELDS),
        "source_manifest": manifest,
        "injury_outcome_values_opened": False,
        "relationship_computed": False,
        "raw_source_bytes_persisted": False,
        "incremental_monetary_cost_usd": 0,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "STAGING_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "STAGING_SOURCE_AUDIT.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "gate": gate,
        "employment_keys": len(emp_keys),
        "repeated_mines": len(repeated_emp_mines),
        "operator_accident_keys": len(operator_accident_keys),
        "overlap_rate": overlap_rate,
        "overlap_states": len(overlap_states),
        "injury_outcome_values_opened": False,
        "relationship_computed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
