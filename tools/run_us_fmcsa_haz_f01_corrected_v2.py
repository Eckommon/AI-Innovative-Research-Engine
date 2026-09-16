#!/usr/bin/env python3
"""Second corrected execution wrapper for US-FMCSA-HAZ-F01.

This wrapper changes only the implementation treatment of the already-frozen
FMCSA native `insp_date` field when Socrata reports it as text. It aggregates
that same field by exact value, parses deterministic common date formats, and
computes a weighted parse rate/year support. Source identity, thresholds,
carrier identity, outcome boundary, and cost boundary remain unchanged.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from tools import run_us_fmcsa_haz_f01 as b
from tools import run_us_fmcsa_haz_f01_corrected as c

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FMCSA-HAZ-F01"
CORRECTS_RUN = 35057504925
CORRECTION_CHAIN = [35045639924, 35057504925]


def parse_text_date(value: object) -> int | None:
    s = str(value or "").strip()
    if not s:
        return None
    candidates = [s]
    if re.fullmatch(r"\d{8}", s):
        candidates = [s]
        fmts = ["%Y%m%d", "%m%d%Y"]
    else:
        fmts = [
            "%Y-%m-%dT%H:%M:%S.%f",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d",
            "%m/%d/%Y %H:%M:%S",
            "%m/%d/%Y",
            "%Y/%m/%d",
        ]
    for candidate in candidates:
        for fmt in fmts:
            try:
                y = datetime.strptime(candidate, fmt).year
                return y if 1900 <= y <= 2100 else None
            except ValueError:
                pass
    return None


def date_support_text_aware(dataset_id: str, carrier_field: str, date_field: str, date_type: str):
    if "text" not in str(date_type or "").lower():
        return _ORIGINAL_DATE_SUPPORT(dataset_id, carrier_field, date_field, date_type)

    audits: list[dict] = []
    total, a = b.scalar_count(dataset_id, f"{carrier_field} is not null")
    audits.append(a)

    rows, a = b.socrata_query(dataset_id, {
        "$select": f"{date_field}, count(*) as n",
        "$where": f"{carrier_field} is not null AND {date_field} is not null",
        "$group": date_field,
        "$order": date_field,
        "$limit": 50000,
    })
    audits.append(a)
    if len(rows) >= 50000:
        raise RuntimeError("text-date distinct-value safety bound reached; parse support incomplete")

    dated = 0
    parsed = 0
    years: set[int] = set()
    distinct_values = 0
    parsed_distinct_values = 0
    for row in rows:
        distinct_values += 1
        try:
            n = int(float(row.get("n", 0)))
        except Exception:
            n = 0
        dated += n
        y = parse_text_date(row.get(date_field))
        if y is not None:
            parsed += n
            years.add(y)
            parsed_distinct_values += 1

    return {
        "valid_carrier_rows": total,
        "dated_valid_carrier_rows": dated,
        "date_parse_success_rows": parsed,
        "date_parse_rate": (parsed / total) if total else 0.0,
        "date_nonnull_rate": (dated / total) if total else 0.0,
        "date_years": sorted(years),
        "distinct_date_years": len(years),
        "date_field_type": date_type,
        "distinct_raw_date_values": distinct_values,
        "parsed_distinct_raw_date_values": parsed_distinct_values,
        "date_support_method": "exact-text-value-grouping-weighted-deterministic-parse",
    }, audits


_ORIGINAL_DATE_SUPPORT = b.date_support


def main() -> None:
    # Patch only the date-support implementation used by the already-reviewed
    # corrected runner, then identify the immediately superseded run.
    b.date_support = date_support_text_aware
    c.CORRECTS_RUN = CORRECTS_RUN
    c.main()

    # Add explicit correction-chain metadata after the base corrected runner
    # has written the outcome-blind staging artifacts.
    rp = OUT / "STAGING_RESULT.json"
    ap = OUT / "STAGING_SOURCE_AUDIT.json"
    r = json.loads(rp.read_text(encoding="utf-8"))
    a = json.loads(ap.read_text(encoding="utf-8"))
    r["correction_chain"] = CORRECTION_CHAIN
    r["text_date_parser_correction"] = True
    a["correction_chain"] = CORRECTION_CHAIN
    a["text_date_parser_correction"] = True
    a["correction_scope"] = "same-native-insp-date-deterministic-text-parsing-only"
    rp.write_text(json.dumps(r, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ap.write_text(json.dumps(a, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
