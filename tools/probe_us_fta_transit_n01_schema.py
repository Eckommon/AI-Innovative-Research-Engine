#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FTA-TRANSIT-N01" / "SCHEMA_PREFLIGHT.json"
BASE = "https://data.transportation.gov"
UA = "AI-Innovative-Research-Engine/US-FTA-TRANSIT-N01 schema-preflight"
DATASETS = {
    "breakdowns": "amkt-4ehs",
    "monthly_modal": "5ti2-5uiv",
    "major_safety_events": "9ivb-8ae9",
}


def norm(x: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(x or "").lower()).strip()


def get_meta(did: str) -> tuple[dict, bytes]:
    url = f"{BASE}/api/views/{did}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    obj = json.loads(raw)
    assert isinstance(obj, dict) and isinstance(obj.get("columns"), list)
    return obj, raw


def col(c: dict) -> dict:
    return {
        "name": c.get("name"),
        "fieldName": c.get("fieldName"),
        "dataTypeName": c.get("dataTypeName"),
        "description": c.get("description"),
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "protocol": "US-FTA-TRANSIT-N01-SCHEMA-PREFLIGHT",
        "evaluated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "outcome_values_opened": False,
        "relationship_computed": False,
        "incremental_monetary_cost_usd": 0,
        "sources": {},
    }
    for name, did in DATASETS.items():
        meta, raw = get_meta(did)
        columns = [c for c in meta["columns"] if isinstance(c, dict)]
        if name == "breakdowns":
            keep = columns
        elif name == "monthly_modal":
            terms = {
                "ntd", "mode", "type of service", "tos", "year", "month",
                "vehicle revenue", "revenue miles", "vrm", "vehicle miles",
                "service", "reporter", "upt", "unlinked passenger", "voms",
            }
            keep = [c for c in columns if any(t in (norm(c.get("name")) + " " + norm(c.get("fieldName")) + " " + norm(c.get("description"))) for t in terms)]
        else:
            # Structural metadata only for the outcome source; do not catalogue outcome/severity measures here.
            structural_terms = {"ntd id", "mode", "incident date", "event date", "year", "month"}
            keep = [c for c in columns if any(t in (norm(c.get("name")) + " " + norm(c.get("fieldName"))) for t in structural_terms)]
        result["sources"][name] = {
            "dataset_id": did,
            "metadata_name": meta.get("name"),
            "metadata_sha256": hashlib.sha256(raw).hexdigest(),
            "column_count": len(columns),
            "selected_schema_columns": [col(c) for c in keep],
        }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: len(v["selected_schema_columns"]) for k, v in result["sources"].items()}, sort_keys=True))


if __name__ == "__main__":
    main()
