#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import json
import re
import urllib.request
import zipfile
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-F01"
OUT.mkdir(parents=True, exist_ok=True)
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
TC_URL = "https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip"
ARCHIVE_URL = "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/archived.html"
UA = "AI-Innovative-Research-Engine/CA-GRAIN week-identity technical revalidation"
START = date(2023, 8, 1)
END = date(2025, 7, 31)

# Official CGC archive anchors. Weeks 1-51 are seven-day increments; week 52 is the published crop-year close.
OFFICIAL = {
    "2023-24": {"week1_end": date(2023, 8, 6), "week52_end": date(2024, 7, 31)},
    "2024-25": {"week1_end": date(2024, 8, 11), "week52_end": date(2025, 7, 31)},
}


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
    raise RuntimeError("decode")


def hnorm(s: str) -> str:
    return re.sub(r"[_\-\s]+", " ", (s or "").strip()).casefold()


def exact(headers: list[str], *names: str) -> str | None:
    lookup = {hnorm(h): h for h in headers}
    for n in names:
        if hnorm(n) in lookup:
            return lookup[hnorm(n)]
    return None


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def monday(d: date) -> date:
    return d - timedelta(days=d.weekday())


def official_end(crop: str, week: int) -> date:
    if week == 52:
        return OFFICIAL[crop]["week52_end"]
    return OFFICIAL[crop]["week1_end"] + timedelta(days=7 * (week - 1))


def parse_isoish(raw: str) -> date | None:
    s = (raw or "").strip()
    if re.match(r"^20\d{2}-\d{2}-\d{2}", s):
        s = s[:10]
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


gsw_week_labels: dict[str, set[int]] = defaultdict(set)
family_weeks: dict[str, set[str]] = defaultdict(set)
raw_date_mismatches = []

for crop, url in GSW_URLS.items():
    reader = csv.DictReader(io.StringIO(decode(fetch(url))))
    headers = reader.fieldnames or []
    hwk = exact(headers, "grain_week", "Grain Week")
    hdate = exact(headers, "week_ending_date", "Week Ending Date")
    hws = exact(headers, "worksheet")
    hm = exact(headers, "metric")
    hp = exact(headers, "period")
    if not all((hwk, hdate, hws, hm, hp)):
        raise RuntimeError(f"GSW schema mismatch {crop}")
    seen_raw_week_identity = set()
    for row in reader:
        raw_week = (row.get(hwk) or "").strip()
        try:
            week = int(float(raw_week))
        except ValueError:
            continue
        if not 1 <= week <= 52:
            continue
        gsw_week_labels[crop].add(week)
        off = official_end(crop, week)
        wk = monday(off).isoformat()
        family = None
        if norm(row.get(hws)) == norm("Primary") and norm(row.get(hm)) == norm("Deliveries") and norm(row.get(hp)) == norm("Current Week"):
            family = "Primary/Deliveries/Current Week"
        elif norm(row.get(hws)) == norm("Process") and norm(row.get(hm)) == norm("Producer Deliveries") and norm(row.get(hp)) == norm("Current Week"):
            family = "Process/Producer Deliveries/Current Week"
        if family:
            family_weeks[family].add(wk)

        identity = (crop, week, (row.get(hdate) or "").strip())
        if identity not in seen_raw_week_identity:
            seen_raw_week_identity.add(identity)
            raw = identity[2]
            parsed_candidates = []
            for fmt in ("%d/%m/%Y", "%m/%d/%Y"):
                try:
                    parsed_candidates.append(datetime.strptime(raw, fmt).date().isoformat())
                except ValueError:
                    pass
            if off.isoformat() not in parsed_candidates and raw:
                raw_date_mismatches.append({
                    "crop": crop,
                    "grain_week": week,
                    "raw_week_ending_date": raw,
                    "official_week_ending_date": off.isoformat(),
                    "candidate_slash_parses": sorted(set(parsed_candidates)),
                })

# Transport Canada structural weeks for the frozen outcome; never read Measure_Value.
tc_bytes = fetch(TC_URL)
tc_carrier_weeks = {"CN": set(), "CPKC": set()}
with zipfile.ZipFile(io.BytesIO(tc_bytes)) as z:
    members = [n for n in z.namelist() if n.lower().endswith(".csv")]
    for year in (2023, 2024, 2025):
        pat = re.compile(rf"(^|/)weekly_rail_system_performance_indicators_eng_{year}\.csv$", re.I)
        hits = [n for n in members if pat.search(n)]
        if len(hits) != 1:
            raise RuntimeError(f"TC file mismatch {year}: {hits}")
        reader = csv.DictReader(io.StringIO(decode(z.read(hits[0]))))
        headers = reader.fieldnames or []
        hd = exact(headers, "Reference_Date", "Reference Date")
        hc = exact(headers, "Carrier")
        hco = exact(headers, "Commodity")
        hm = exact(headers, "Measure")
        hg = exact(headers, "Geography")
        if not all((hd, hc, hco, hm, hg)):
            raise RuntimeError("TC schema mismatch")
        for row in reader:
            if norm(row.get(hco)) != norm("All Western grain"):
                continue
            if norm(row.get(hm)) != norm("Average Dwell Time at Origin"):
                continue
            if norm(row.get(hg)) != norm("Canada"):
                continue
            carrier = (row.get(hc) or "").strip()
            if carrier not in tc_carrier_weeks:
                continue
            d = parse_isoish(row.get(hd, ""))
            if d is None or not (START <= d <= END):
                continue
            tc_carrier_weeks[carrier].add(monday(d).isoformat())

official_gsw_weeks = set()
for crop in OFFICIAL:
    for w in range(1, 53):
        official_gsw_weeks.add(monday(official_end(crop, w)).isoformat())

common_by_carrier = {
    c: len(official_gsw_weeks & weeks) for c, weeks in tc_carrier_weeks.items()
}
common_both = len(official_gsw_weeks & tc_carrier_weeks["CN"] & tc_carrier_weeks["CPKC"])

out = {
    "id": "CA-GRAIN-GSW-WEEK-IDENTITY-REVALIDATION",
    "scope": ["CA-GRAIN-F01", "CA-GRAIN-E01", "CA-GRAIN-E02"],
    "values_read": False,
    "relationship_computed": False,
    "official_archive_url": ARCHIVE_URL,
    "official_schedule_rule": "Use CGC grain_week identity and published crop-year schedule; weeks 1-51 advance by 7 days from published Week 1, Week 52 uses published crop-year-close date.",
    "gsw_grain_week_labels": {crop: sorted(v) for crop, v in gsw_week_labels.items()},
    "gsw_distinct_official_week_keys": len(official_gsw_weeks),
    "family_official_week_counts": {k: len(v) for k, v in family_weeks.items()},
    "tc_carrier_week_counts": {k: len(v) for k, v in tc_carrier_weeks.items()},
    "common_official_week_keys_by_carrier": common_by_carrier,
    "common_official_week_keys_both_carriers": common_both,
    "raw_date_semantics_mismatch_count": len(raw_date_mismatches),
    "raw_date_semantics_mismatch_examples": raw_date_mismatches[:20],
    "adjudication": {
        "F01": "PASS feasibility remains valid if common_official_week_keys_both_carriers >= 80; prior explicit-date count must not be cited.",
        "E01": "Terminal ambiguity HOLD remains valid because it depends on two semantic families, not the invalid raw-date parsing; prior lag-support count must not be cited.",
        "E02": "Issue #110 explicitly froze explicit-source-date to ISO-Monday mapping; post-value replacement with grain_week is not allowed, so E02 structural HOLD is not repaired by this revalidation.",
    },
    "incremental_monetary_cost_usd": 0,
}
if common_both < 80:
    raise RuntimeError(f"F01 revalidation below frozen threshold: {common_both}")
if len(family_weeks.get("Primary/Deliveries/Current Week", set())) < 80:
    raise RuntimeError("Primary family revalidation below 80 weeks")
if len(family_weeks.get("Process/Producer Deliveries/Current Week", set())) < 80:
    raise RuntimeError("Process family revalidation below 80 weeks")

(OUT / "DATE_SEMANTICS_REVALIDATION.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "gsw_week_keys": len(official_gsw_weeks),
    "tc_cn": len(tc_carrier_weeks["CN"]),
    "tc_cpkc": len(tc_carrier_weeks["CPKC"]),
    "common_both": common_both,
    "raw_date_mismatches": len(raw_date_mismatches),
    "values_read": False,
}))
