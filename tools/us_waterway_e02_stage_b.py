#!/usr/bin/env python3
"""Frozen US-WATERWAY-E02 signed-flow relationship test.

Reuses the already validated E01 USACE pagination, panel construction, fixed-
effect residualization and two-way CR1 implementation. The only scientific
source-semantic change is the prospectively frozen E02 rule: every finite
published Daily USGS 00060/00003 value is admissible with its sign preserved.
E01 remains terminal HOLD and is never rewritten.
"""
from __future__ import annotations

import json
import math
import time
import urllib.parse
from collections import defaultdict
from pathlib import Path

import us_waterway_e01_stage_b as base

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-E02"
MAP = ROOT / "research" / "US-WATERWAY-E01" / "STAGE_A_GAGE_LOCK_MAP.csv"
UA = "AI-Innovative-Research-Engine/US-WATERWAY-E02-stage-b"

# Redirect the validated E01 machinery to the new prospective E02 artifact set.
base.OUT = OUT
base.MAP = MAP
base.UA = UA


def fetch_usgs_daily_signed(gages):
    """Fetch frozen Daily 00060/00003 data, preserving every finite signed value."""
    params = {
        "f": "json",
        "monitoring_location_id": ",".join(sorted(gages)),
        "parameter_code": "00060",
        "statistic_id": "00003",
        "datetime": f"{base.START}/{base.END}",
        "limit": "10000",
        "api_key": "DEMO_KEY",
        "properties": "monitoring_location_id,parameter_code,statistic_id,time,value,unit_of_measure,approval_status,qualifier",
    }
    url = base.USGS_DAILY + "?" + urllib.parse.urlencode(params, safe=",")
    values = defaultdict(dict)
    conflicts = []
    manifest = []
    seen_urls = set()
    page = 0
    negative_records = 0
    negative_gages = set()

    while url:
        if url in seen_urls:
            raise RuntimeError("USGS pagination loop")
        seen_urls.add(url)
        obj, meta = base.fetch_json(url)
        page += 1
        page_negative = 0
        meta["page"] = page
        meta["numberReturned"] = obj.get("numberReturned")

        for feat in obj.get("features", []):
            p = feat.get("properties") or {}
            gid = str(p.get("monitoring_location_id") or "")
            if gid not in gages:
                continue
            if str(p.get("parameter_code")) != "00060" or str(p.get("statistic_id")) != "00003":
                continue
            day = str(p.get("time") or "")[:10]
            if not (base.START <= day <= base.END):
                continue
            try:
                val = float(p.get("value"))
            except Exception:
                # Frozen E02 contract: null/blank/non-numeric alone are missing.
                continue
            if not math.isfinite(val):
                continue
            if val < 0:
                negative_records += 1
                page_negative += 1
                negative_gages.add(gid)
            prior = values[gid].get(day)
            if prior is not None and not math.isclose(prior, val, rel_tol=0.0, abs_tol=0.0):
                conflicts.append({"gage": gid, "date": day, "a": prior, "b": val})
            else:
                values[gid][day] = val

        meta["negative_records_on_page"] = page_negative
        manifest.append(meta)
        next_url = None
        for link in obj.get("links", []):
            if link.get("rel") == "next" and link.get("href"):
                next_url = str(link["href"])
                break
        url = next_url

    if conflicts:
        raise RuntimeError(f"conflicting USGS duplicate gage/date values: {conflicts[:5]}")

    # Derived source-semantics counts only; no raw observation series persisted here.
    if manifest:
        manifest[0]["signed_value_contract"] = True
        manifest[0]["negative_record_count_all_pages"] = negative_records
        manifest[0]["negative_gage_count_all_pages"] = len(negative_gages)
    return values, manifest


def fit_primary_e02(panel, exposure_key="extreme_share"):
    result = _original_fit(panel, exposure_key)
    mapping = {
        "PASS_US_WATERWAY_E01_POSITIVE_MATERIAL_EXTREME_FLOW_DELAY_ASSOCIATION":
            "PASS_US_WATERWAY_E02_POSITIVE_MATERIAL_SIGNED_EXTREME_FLOW_DELAY_ASSOCIATION",
        "DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01":
            "DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E02",
        "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP":
            "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP",
    }
    result["gate"] = mapping[result["gate"]]
    return result


def rewrite_e02_artifacts() -> None:
    """Rename inherited E01 labels only; never alter any computed number."""
    replacements = {
        "HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT":
            "HOLD_US_WATERWAY_E02_SOURCE_PANEL_OR_INFERENCE_SUPPORT",
        "PASS_US_WATERWAY_E01_POSITIVE_MATERIAL_EXTREME_FLOW_DELAY_ASSOCIATION":
            "PASS_US_WATERWAY_E02_POSITIVE_MATERIAL_SIGNED_EXTREME_FLOW_DELAY_ASSOCIATION",
        "DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01":
            "DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E02",
        "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP":
            "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP",
        "US-WATERWAY-E01 Stage B Result": "US-WATERWAY-E02 Stage B Result",
    }
    for name in [
        "STAGE_B_PRIMARY_RESULT.json",
        "STAGE_B_SENSITIVITY_RESULT.json",
        "STAGE_B_RESULT.md",
    ]:
        p = OUT / name
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8")
        for old, new in replacements.items():
            s = s.replace(old, new)
        p.write_text(s, encoding="utf-8")


_original_fit = base.fit_primary
base.fetch_usgs_daily = fetch_usgs_daily_signed
base.fit_primary = fit_primary_e02


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    base.main()
    rewrite_e02_artifacts()


if __name__ == "__main__":
    main()
