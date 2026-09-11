#!/usr/bin/env python3
"""PORTFOLIO-R15 outcome-blind USGS negative-discharge semantics probe.

Reads the frozen US-WATERWAY-E01 Stage-A gage cohort, queries only official USGS
Daily 00060/00003 data for 2016-2025, and persists ONLY source-semantics summaries
for negative values. It never reads USACE delay outcomes and never computes a
cross-source relationship.
"""
from __future__ import annotations

import csv, json, urllib.parse, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "research" / "US-WATERWAY-E01" / "STAGE_A_GAGE_LOCK_MAP.csv"
OUT = ROOT / "research" / "PORTFOLIO-R15"
DAILY = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items"
LEGACY = "https://waterservices.usgs.gov/nwis/dv/"
UA = "AI-Innovative-Research-Engine/PORTFOLIO-R15-source-semantics"


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def modern(gage: str) -> tuple[int, list[dict]]:
    q = urllib.parse.urlencode({
        "f": "json",
        "limit": "10000",
        "monitoring_location_id": gage,
        "datetime": "2016-01-01/2025-12-31",
        "statistic_id": "00003",
        "parameter_code": "00060",
        "properties": "monitoring_location_id,time,value,unit_of_measure,approval_status,qualifier,time_series_id,last_modified",
    })
    data = get_json(f"{DAILY}?{q}")
    neg = []
    for feat in data.get("features", []):
        p = feat.get("properties") or {}
        v = p.get("value")
        if v is None or str(v).strip() == "":
            continue
        try:
            x = float(v)
        except ValueError:
            continue
        if x < 0:
            neg.append({
                "monitoring_location_id": p.get("monitoring_location_id"),
                "time": p.get("time"),
                "value": str(v),
                "unit_of_measure": p.get("unit_of_measure"),
                "approval_status": p.get("approval_status"),
                "qualifier": p.get("qualifier"),
                "time_series_id": p.get("time_series_id"),
                "last_modified": p.get("last_modified"),
            })
    return int(data.get("numberMatched") or data.get("numberReturned") or len(data.get("features", []))), neg


def legacy(site: str, day: str) -> list[dict]:
    q = urllib.parse.urlencode({
        "format": "json", "sites": site, "startDT": day, "endDT": day,
        "parameterCd": "00060", "statCd": "00003", "siteStatus": "all",
    })
    try:
        data = get_json(f"{LEGACY}?{q}")
    except Exception as e:
        return [{"legacy_error": f"{type(e).__name__}: {e}"}]
    out = []
    for ts in (((data.get("value") or {}).get("timeSeries")) or []):
        var = ts.get("variable") or {}
        for block in ts.get("values") or []:
            for item in block.get("value") or []:
                out.append({
                    "value": item.get("value"),
                    "qualifiers": item.get("qualifiers"),
                    "dateTime": item.get("dateTime"),
                    "unit": ((var.get("unit") or {}).get("unitCode")),
                    "variableCode": [x.get("value") for x in var.get("variableCode") or []],
                })
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with MAP.open(encoding="utf-8-sig", newline="") as f:
        gages = sorted({r["usgs_id"] for r in csv.DictReader(f)})

    per_gage = []
    negatives = []
    for g in gages:
        n, neg = modern(g)
        per_gage.append({"gage": g, "records_returned_or_matched": n, "negative_record_count": len(neg)})
        for r in neg:
            site = g.split("-", 1)[-1]
            r["legacy_same_day"] = legacy(site, str(r["time"]))
            negatives.append(r)

    result = {
        "boundary": {
            "usace_delay_opened": False,
            "relationship_computed": False,
            "positive_usgs_values_persisted": False,
            "negative_source_semantics_only": True,
        },
        "period": ["2016-01-01", "2025-12-31"],
        "gage_count": len(gages),
        "negative_record_count": len(negatives),
        "negative_gage_count": len({r["monitoring_location_id"] for r in negatives}),
        "per_gage": per_gage,
        "negative_records": negatives,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "USGS_NEGATIVE_DISCHARGE_SEMANTICS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# PORTFOLIO-R15 — USGS Negative-Discharge Source-Semantics Probe", "",
        "Outcome-blind source qualification only. No USACE delay outcome was opened and no relationship was computed.", "",
        f"- Frozen Stage-A gages checked: **{len(gages)}**",
        f"- Negative Daily `00060/00003` records in 2016–2025: **{len(negatives)}**",
        f"- Gages containing any negative record: **{len({r['monitoring_location_id'] for r in negatives})}**", "",
        "## Negative records",
    ]
    if not negatives:
        lines.append("- None.")
    for r in negatives:
        lines.append(
            f"- `{r['monitoring_location_id']}` `{r['time']}` value=`{r['value']}` {r.get('unit_of_measure')}; "
            f"approval=`{r.get('approval_status')}`; qualifier=`{r.get('qualifier')}`; legacy=`{r.get('legacy_same_day')}`"
        )
    lines += ["", "Incremental monetary cost: **0 USD**."]
    (OUT / "USGS_NEGATIVE_DISCHARGE_SEMANTICS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
