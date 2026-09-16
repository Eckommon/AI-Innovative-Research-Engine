#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FTA-TRANSIT-N01" / "QUALITY_FLAG_PREFLIGHT.json"
BASE = "https://data.transportation.gov/resource/amkt-4ehs.json"
FIELDS = [
    "type_of_service",
    "reporter_type",
    "major_mechanical_failures_1",
    "vehicle_passenger_car_miles_2",
]
UA = "AI-Innovative-Research-Engine/US-FTA-TRANSIT-N01 quality-flag-preflight"


def clean(v: object) -> str:
    return str(v if v is not None else "").strip()


def main() -> None:
    params = urllib.parse.urlencode({"$select": ",".join(FIELDS), "$limit": 10000})
    req = urllib.request.Request(f"{BASE}?{params}", headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.loads(r.read())
    assert isinstance(rows, list) and rows
    distinct = {f: sorted({clean(r.get(f)) for r in rows if isinstance(r, dict)}) for f in FIELDS}
    counts = {f: {} for f in FIELDS}
    for r in rows:
        if not isinstance(r, dict):
            continue
        for f in FIELDS:
            v = clean(r.get(f))
            counts[f][v] = counts[f].get(v, 0) + 1
    result = {
        "protocol": "US-FTA-TRANSIT-N01-QUALITY-FLAG-PREFLIGHT",
        "evaluated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "rows_read": len(rows),
        "fields": FIELDS,
        "distinct_values": distinct,
        "value_counts": counts,
        "exposure_magnitudes_persisted": False,
        "safety_outcome_values_opened": False,
        "relationship_computed": False,
        "incremental_monetary_cost_usd": 0,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(distinct, sort_keys=True))


if __name__ == "__main__":
    main()
