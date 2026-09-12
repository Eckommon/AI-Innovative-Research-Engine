#!/usr/bin/env python3
"""US-RCRA-E01 Pass 1: reproduce/freeze N01 pair identities without outcomes."""
from __future__ import annotations

import hashlib
import io
import json
import runpy
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-RCRA-E01"
OUT.mkdir(parents=True, exist_ok=True)
FEMA_HOST = "www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
_original_urlopen = urllib.request.urlopen

class BufferedResponse(io.BytesIO):
    def __init__(self, payload: bytes, response, url: str):
        super().__init__(payload)
        self.headers = getattr(response, "headers", None)
        self.url = getattr(response, "url", url)
        self.status = getattr(response, "status", 200)
    def __enter__(self): return self
    def __exit__(self, *args): self.close(); return False
    def getcode(self): return self.status

def resilient_urlopen(req, *args, **kwargs):
    url = req.full_url if isinstance(req, urllib.request.Request) else str(req)
    if FEMA_HOST not in url:
        return _original_urlopen(req, *args, **kwargs)
    for attempt in range(5):
        try:
            with _original_urlopen(req, *args, **kwargs) as r:
                return BufferedResponse(r.read(), r, url)
        except Exception:
            if attempt == 4: raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")

urllib.request.urlopen = resilient_urlopen
g = runpy.run_path(str(ROOT / "tools" / "run_us_rcra_n01.py"), run_name="__main__")
paired = g["paired"]
assert len(paired) == 297, len(paired)
states = sorted({v["state_fips"] for v in paired.values()})
assert len(states) == 43, len(states)

rows = []
for rid, p in sorted(paired.items()):
    rows.append({
        "id_number": rid,
        "state_fips": p["state_fips"],
        "county_fips": p["county_fips"],
        "index_date": p["index_date"],
        "index_disaster_number": p["index_disaster_number"],
        "index_incident_type": p["index_incident_type"],
        "pre_cei_date": p["pre_cei_date"],
        "pre_evaluation_identifier": p["pre_evaluation_identifier"],
        "post_cei_date": p["post_cei_date"],
        "post_evaluation_identifier": p["post_evaluation_identifier"],
    })

canonical = json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
fingerprint = hashlib.sha256(canonical).hexdigest()
manifest = {
    "id": "US-RCRA-E01-PAIR-MANIFEST",
    "issue": 125,
    "outcomes_opened": False,
    "found_violation_values_accessed_or_persisted": False,
    "pair_count": len(rows),
    "state_territory_fips_count": len(states),
    "state_territory_fips": states,
    "pair_identity_sha256": fingerprint,
    "pair_identity_canonicalization": "sorted by ID_NUMBER; canonical compact JSON with sorted keys",
    "pairs": rows,
    "incremental_monetary_cost_usd": 0,
}
(OUT / "PAIR_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"pair_count": len(rows), "states": len(states), "sha256": fingerprint}, indent=2))
