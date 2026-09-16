#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FTA-TRANSIT-N01" / "OUTCOME_SCHEMA_PREFLIGHT.json"
URL = "https://data.transportation.gov/api/views/9ivb-8ae9.json"
UA = "AI-Innovative-Research-Engine/US-FTA-TRANSIT-N01 downstream-schema-preflight"
TERMS = [
    "event", "incident", "safety", "security", "major", "collision", "derail",
    "fatal", "injur", "assault", "fire", "evac", "property", "threshold",
]


def norm(x: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(x or "").lower()).strip()


def main() -> None:
    req = urllib.request.Request(URL, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    meta = json.loads(raw)
    cols = [c for c in meta.get("columns", []) if isinstance(c, dict)]
    selected = []
    for c in cols:
        hay = " ".join([norm(c.get("name")), norm(c.get("fieldName")), norm(c.get("description"))])
        if any(t in hay for t in TERMS):
            selected.append({
                "name": c.get("name"),
                "fieldName": c.get("fieldName"),
                "dataTypeName": c.get("dataTypeName"),
                "description": c.get("description"),
            })
    result = {
        "protocol": "US-FTA-TRANSIT-N01-OUTCOME-SCHEMA-PREFLIGHT",
        "evaluated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "dataset_id": "9ivb-8ae9",
        "metadata_sha256": hashlib.sha256(raw).hexdigest(),
        "column_count": len(cols),
        "selected_schema_columns": selected,
        "outcome_row_values_opened": False,
        "relationship_computed": False,
        "incremental_monetary_cost_usd": 0,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"column_count": len(cols), "selected": len(selected)}, sort_keys=True))


if __name__ == "__main__":
    main()
