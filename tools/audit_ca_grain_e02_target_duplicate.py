#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import json
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-E02"
OUT.mkdir(parents=True, exist_ok=True)
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
GRAINS = {"Amber Durum","Barley","Beans","Canaryseed","Canola","Chick Peas","Corn","Flaxseed","Lentils","Mustard Seed","Oats","Peas","Rye","Soybeans","Wheat"}
REGIONS = {"Alberta","British Columbia","Manitoba","Saskatchewan"}
TARGET_WEEK = date(2025, 6, 2)
UA = "AI-Innovative-Research-Engine/CA-GRAIN-E02 targeted duplicate provenance audit"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def decode(b: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    raise RuntimeError("cannot decode source")


def hnorm(s: str) -> str:
    return re.sub(r"[_\-\s]+", " ", (s or "").strip()).casefold()


def exact(headers: list[str], *names: str) -> str | None:
    lookup = {hnorm(h): h for h in headers}
    for name in names:
        hit = lookup.get(hnorm(name))
        if hit is not None:
            return hit
    return None


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def parse_gsw_date(raw: str) -> date | None:
    s = (raw or "").strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def monday(d: date) -> date:
    return d - timedelta(days=d.weekday())


records: list[dict] = []
for crop_file, url in GSW_URLS.items():
    reader = csv.DictReader(io.StringIO(decode(fetch(url))))
    headers = reader.fieldnames or []
    hm = {
        "crop_year": exact(headers, "crop_year", "Crop Year"),
        "grain_week": exact(headers, "grain_week", "Grain Week"),
        "date": exact(headers, "week_ending_date", "Week Ending Date"),
        "worksheet": exact(headers, "worksheet"),
        "metric": exact(headers, "metric"),
        "period": exact(headers, "period"),
        "grain": exact(headers, "grain"),
        "grade": exact(headers, "grade"),
        "region": exact(headers, "region", "Region"),
    }
    if not all(hm.values()):
        raise RuntimeError(f"schema mismatch {crop_file}: {hm}")

    for row in reader:
        if norm(row.get(hm["worksheet"], "")) != norm("Primary"):
            continue
        if norm(row.get(hm["metric"], "")) != norm("Deliveries"):
            continue
        if norm(row.get(hm["period"], "")) != norm("Current Week"):
            continue
        if (row.get(hm["grade"], "") or "").strip() != "":
            continue
        grain = (row.get(hm["grain"], "") or "").strip()
        region = (row.get(hm["region"], "") or "").strip()
        if grain not in GRAINS or region not in REGIONS:
            continue
        raw_date = (row.get(hm["date"], "") or "").strip()
        parsed = parse_gsw_date(raw_date)
        if parsed is None or monday(parsed) != TARGET_WEEK:
            continue
        records.append({
            "crop_file": crop_file,
            "crop_year": (row.get(hm["crop_year"], "") or "").strip(),
            "grain_week": (row.get(hm["grain_week"], "") or "").strip(),
            "raw_week_ending_date": raw_date,
            "parsed_week_ending_date": parsed.isoformat(),
            "normalized_monday": TARGET_WEEK.isoformat(),
            "grain": grain,
            "region": region,
        })

by_component: dict[tuple[str, str], list[dict]] = defaultdict(list)
for rec in records:
    by_component[(rec["grain"], rec["region"])].append(rec)

source_identity_counter = Counter(
    (r["crop_file"], r["crop_year"], r["grain_week"], r["raw_week_ending_date"])
    for r in records
)
source_identities = [
    {
        "crop_file": k[0],
        "crop_year": k[1],
        "grain_week": k[2],
        "raw_week_ending_date": k[3],
        "parsed_week_ending_date": parse_gsw_date(k[3]).isoformat() if parse_gsw_date(k[3]) else None,
        "row_count": count,
    }
    for k, count in sorted(source_identity_counter.items())
]

duplicate_components = []
for (grain, region), items in sorted(by_component.items()):
    if len(items) > 1:
        duplicate_components.append({
            "grain": grain,
            "region": region,
            "occurrence_count": len(items),
            "source_identities": [
                {
                    "crop_file": x["crop_file"],
                    "crop_year": x["crop_year"],
                    "grain_week": x["grain_week"],
                    "raw_week_ending_date": x["raw_week_ending_date"],
                    "parsed_week_ending_date": x["parsed_week_ending_date"],
                }
                for x in items
            ],
        })

raw_dates = sorted({r["raw_week_ending_date"] for r in records})
crop_files = sorted({r["crop_file"] for r in records})
component_counts = Counter((r["grain"], r["region"]) for r in records)
all_expected_components_present = len(component_counts) == len(GRAINS) * len(REGIONS)
all_components_duplicate = all(v > 1 for v in component_counts.values()) if component_counts else False

if len(crop_files) > 1:
    classification = "CROP_FILE_OVERLAP"
elif len(raw_dates) > 1 and duplicate_components:
    classification = "MONDAY_COLLISION_DISTINCT_SOURCE_DATES"
elif duplicate_components:
    exact_identity_duplicates = True
    for comp in duplicate_components:
        ids = {
            (x["crop_file"], x["crop_year"], x["grain_week"], x["raw_week_ending_date"])
            for x in comp["source_identities"]
        }
        if len(ids) != 1:
            exact_identity_duplicates = False
            break
    classification = "SOURCE_DUPLICATE_EXACT_IDENTITY" if exact_identity_duplicates else "DISTINCT_SOURCE_IDENTITIES_SAME_WEEK"
else:
    classification = "NO_DUPLICATE_AT_TARGET_WEEK"

out = {
    "id": "CA-GRAIN-E02-TARGET-DUPLICATE-PROVENANCE",
    "issue": 110,
    "target_normalized_week": TARGET_WEEK.isoformat(),
    "values_read": False,
    "relationship_computed": False,
    "date_semantics": "GSW slash dates parsed DD/MM/YYYY",
    "matching_rows": len(records),
    "distinct_component_keys": len(component_counts),
    "expected_component_keys": len(GRAINS) * len(REGIONS),
    "all_expected_components_present": all_expected_components_present,
    "all_components_duplicate": all_components_duplicate,
    "crop_files": crop_files,
    "raw_week_ending_dates": raw_dates,
    "source_identities": source_identities,
    "duplicate_component_count": len(duplicate_components),
    "duplicate_components": duplicate_components,
    "classification": classification,
    "adjudication_rule": {
        "SOURCE_DUPLICATE_EXACT_IDENTITY": "Issue #110 duplicate-key fail-closed condition is source-real; E02 remains HOLD.",
        "CROP_FILE_OVERLAP": "Do not deduplicate automatically; require separate technical adjudication because Issue #110 froze both files.",
        "MONDAY_COLLISION_DISTINCT_SOURCE_DATES": "The frozen ISO-Monday mapping itself creates the collision; do not repair E02 post-value. E02 remains HOLD unless a new separately preregistered descendant changes temporal identity prospectively.",
        "DISTINCT_SOURCE_IDENTITIES_SAME_WEEK": "Do not choose or merge identities post-value; E02 remains HOLD.",
        "NO_DUPLICATE_AT_TARGET_WEEK": "Prior corrected runner likely has an implementation defect; technical correction may be permitted without changing the frozen scientific contract.",
    }[classification],
    "incremental_monetary_cost_usd": 0,
}

(OUT / "TARGET_DUPLICATE_PROVENANCE.json").write_text(
    json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(json.dumps({
    "classification": classification,
    "matching_rows": len(records),
    "duplicate_component_count": len(duplicate_components),
    "raw_dates": raw_dates,
    "crop_files": crop_files,
    "values_read": False,
}))
