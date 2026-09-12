#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import urllib.request
import zipfile
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-E01"
OUT.mkdir(parents=True, exist_ok=True)

TC_URL = "https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip"
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
START = date(2023, 8, 1)
END = date(2025, 7, 31)
UA = "AI-Innovative-Research-Engine/CA-GRAIN-E01 Stage A outcome-blind probe"


def fetch(url: str) -> tuple[bytes, dict]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=120) as r:
        b = r.read()
        return b, {
            "requested_url": url,
            "final_url": r.geturl(),
            "status": getattr(r, "status", 200),
            "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest(),
            "content_type": r.headers.get("Content-Type"),
        }


def decode(b: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    raise RuntimeError("cannot decode source text")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def hnorm(s: str) -> str:
    return re.sub(r"[_\-\s]+", " ", (s or "").strip()).casefold()


def exact_header(headers: list[str], *names: str) -> str | None:
    lookup = {hnorm(h): h for h in headers}
    for name in names:
        if hnorm(name) in lookup:
            return lookup[hnorm(name)]
    return None


def date_from_text(s: str):
    s = (s or "").strip()
    if re.match(r"^20\d\d-\d\d-\d\d", s):
        s = s[:10]
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def week_monday(d: date) -> str:
    return (d - timedelta(days=d.weekday())).isoformat()


def semantic_delivery(text: str) -> bool:
    n = norm(text)
    upstream = ("producer" in n and "deliver" in n) or ("primary" in n and ("deliver" in n or "receipt" in n))
    downstream = "shipment" in n or "export" in n or "terminal" in n
    return upstream and not downstream


def current_week(text: str) -> bool:
    n = norm(text)
    return ("current" in n and "week" in n) or n in {"week", "weekly", "current week"}


def aggregate_label(text: str) -> bool:
    n = norm(text)
    return n in {"total", "all", "all grain", "all grains", "total grain", "total grains", "all grains and oilseeds"} or ("all" in n and "grain" in n)


def aggregate_grade(text: str) -> bool:
    n = norm(text)
    return n in {"", "total", "all", "all grades", "all grade"} or ("all" in n and "grade" in n)


def western_aggregate(text: str) -> bool:
    n = norm(text)
    return n in {"western canada", "west", "western", "total", "canada"} or "western canada" in n


manifest: dict = {
    "id": "CA-GRAIN-E01-STAGE-A",
    "issue": 108,
    "boundary": {
        "relationship_computed": False,
        "grain_magnitudes_analyzed_or_persisted": False,
        "dwell_magnitudes_analyzed_or_persisted": False,
        "numeric_source_values_persisted": False,
    },
    "frozen_interval": [START.isoformat(), END.isoformat()],
    "frozen_direction": "GSW upstream current-week delivery pressure at t-1 -> TC Canada All Western grain origin dwell at t",
    "gsw": {},
    "transport_canada": {},
    "incremental_monetary_cost_usd": 0,
}

# ---------------- GSW textual identity probe ----------------
# Numeric Ktonnes cells are never parsed, converted, summed, ranked or persisted.
family_weeks: dict[tuple[str, str, str], set[str]] = defaultdict(set)
family_nonblank_weeks: dict[tuple[str, str, str], set[str]] = defaultdict(set)
family_grains: dict[tuple[str, str, str], set[str]] = defaultdict(set)
family_grades: dict[tuple[str, str, str], set[str]] = defaultdict(set)
family_regions: dict[tuple[str, str, str], set[str]] = defaultdict(set)
all_identity_catalog = {"worksheet": set(), "metric": set(), "period": set(), "grain": set(), "grade": set(), "region": set()}

for crop, url in GSW_URLS.items():
    b, meta = fetch(url)
    text = decode(b)
    reader = csv.DictReader(io.StringIO(text))
    headers = reader.fieldnames or []
    hm = {
        "date": exact_header(headers, "week_ending_date", "Week Ending Date"),
        "worksheet": exact_header(headers, "worksheet"),
        "metric": exact_header(headers, "metric"),
        "period": exact_header(headers, "period"),
        "grain": exact_header(headers, "grain"),
        "grade": exact_header(headers, "grade"),
        "region": exact_header(headers, "region"),
        "value": exact_header(headers, "Ktonnes"),
    }
    if not all(hm[k] for k in ("date", "worksheet", "metric", "period", "grain", "region", "value")):
        raise RuntimeError(f"GSW required headers unavailable for {crop}: {hm}")

    rows_in_interval = 0
    for row in reader:
        d = date_from_text(row.get(hm["date"], ""))
        if not d or not (START <= d <= END):
            continue
        rows_in_interval += 1
        vals = {
            "worksheet": (row.get(hm["worksheet"]) or "").strip(),
            "metric": (row.get(hm["metric"]) or "").strip(),
            "period": (row.get(hm["period"]) or "").strip(),
            "grain": (row.get(hm["grain"]) or "").strip(),
            "grade": (row.get(hm["grade"]) or "").strip() if hm["grade"] else "",
            "region": (row.get(hm["region"]) or "").strip(),
        }
        for k, v in vals.items():
            if v:
                all_identity_catalog[k].add(v)

        semantic = f"{vals['worksheet']} | {vals['metric']}"
        if not semantic_delivery(semantic) or not current_week(vals["period"]):
            continue
        fam = (vals["worksheet"], vals["metric"], vals["period"])
        wk = week_monday(d)
        family_weeks[fam].add(wk)
        # Presence only. Never parse or retain numeric source value.
        if bool((row.get(hm["value"]) or "").strip()):
            family_nonblank_weeks[fam].add(wk)
        if vals["grain"]:
            family_grains[fam].add(vals["grain"])
        family_grades[fam].add(vals["grade"])
        if vals["region"]:
            family_regions[fam].add(vals["region"])

    manifest["gsw"][crop] = {
        "download": meta,
        "headers": headers,
        "resolved_headers": hm,
        "rows_in_frozen_interval": rows_in_interval,
    }

families = []
for fam in sorted(family_weeks):
    worksheet, metric, period = fam
    grains = sorted(family_grains[fam])
    grades = sorted(family_grades[fam])
    regions = sorted(family_regions[fam])
    explicit_grain_aggregates = sorted([x for x in grains if aggregate_label(x)])
    explicit_region_aggregates = sorted([x for x in regions if western_aggregate(x)])
    aggregate_grades = sorted([x for x in grades if aggregate_grade(x)])
    families.append({
        "worksheet": worksheet,
        "metric": metric,
        "period": period,
        "week_keys": len(family_weeks[fam]),
        "nonblank_presence_week_keys": len(family_nonblank_weeks[fam]),
        "grains": grains,
        "grades": grades,
        "regions": regions,
        "explicit_grain_aggregates": explicit_grain_aggregates,
        "explicit_region_aggregates": explicit_region_aggregates,
        "aggregate_grade_identities": aggregate_grades,
    })

manifest["gsw"]["identity_catalog"] = {k: sorted(v) for k, v in all_identity_catalog.items()}
manifest["gsw"]["upstream_current_week_families"] = families

# Fail closed on semantic family ambiguity before considering component aggregation.
exposure_resolution = {"status": "UNRESOLVED"}
if len(families) == 1:
    f = families[0]
    if f["nonblank_presence_week_keys"] >= 80:
        # Prefer exactly one explicit all-grain aggregate. If absent, freeze complete component list.
        if len(f["explicit_grain_aggregates"]) == 1:
            grain_rule = {"mode": "EXPLICIT_AGGREGATE", "identity": f["explicit_grain_aggregates"][0]}
        elif len(f["explicit_grain_aggregates"]) == 0 and len(f["grains"]) >= 2:
            grain_rule = {"mode": "FIXED_COMPLETE_COMPONENT_SUM", "identities": f["grains"]}
        else:
            grain_rule = None

        # Prefer one explicit Canada/Western aggregate; otherwise freeze western regions present.
        if len(f["explicit_region_aggregates"]) == 1:
            region_rule = {"mode": "EXPLICIT_AGGREGATE", "identity": f["explicit_region_aggregates"][0]}
        elif len(f["explicit_region_aggregates"]) == 0:
            western_tokens = ("manitoba", "saskatchewan", "alberta", "british columbia", "b.c", "bc", "prairie")
            western_regions = [r for r in f["regions"] if any(t in norm(r) for t in western_tokens)]
            region_rule = {"mode": "FIXED_WESTERN_COMPONENT_SUM", "identities": sorted(western_regions)} if western_regions else None
        else:
            region_rule = None

        # Grade must have a deterministic aggregate/blank identity; otherwise ambiguous.
        grade_rule = None
        if len(f["aggregate_grade_identities"]) == 1:
            grade_rule = {"mode": "AGGREGATE_GRADE", "identity": f["aggregate_grade_identities"][0]}
        elif set(f["grades"]) in ({""}, set()):
            grade_rule = {"mode": "NO_GRADE_DIMENSION"}

        if grain_rule and region_rule and grade_rule:
            exposure_resolution = {
                "status": "IDENTIFIABLE",
                "worksheet": f["worksheet"],
                "metric": f["metric"],
                "period": f["period"],
                "grain_rule": grain_rule,
                "region_rule": region_rule,
                "grade_rule": grade_rule,
                "structural_week_keys": f["week_keys"],
                "nonblank_presence_week_keys": f["nonblank_presence_week_keys"],
            }
        else:
            exposure_resolution = {
                "status": "AMBIGUOUS_COMPONENT_IDENTITIES",
                "grain_rule": grain_rule,
                "region_rule": region_rule,
                "grade_rule": grade_rule,
            }
elif len(families) > 1:
    exposure_resolution = {"status": "AMBIGUOUS_SEMANTIC_FAMILIES", "family_count": len(families)}
else:
    exposure_resolution = {"status": "NO_UPSTREAM_CURRENT_WEEK_FAMILY"}

manifest["gsw"]["exposure_resolution"] = exposure_resolution

# ---------------- Transport Canada frozen outcome support ----------------
tc_bytes, tc_meta = fetch(TC_URL)
outcome_carrier_weeks: dict[str, set[str]] = {"CN": set(), "CPKC": set()}
outcome_nonblank_carrier_weeks: dict[str, set[str]] = {"CN": set(), "CPKC": set()}
selected_members = []

with zipfile.ZipFile(io.BytesIO(tc_bytes)) as z:
    members = [n for n in z.namelist() if n.lower().endswith(".csv")]
    for year in (2023, 2024, 2025):
        pattern = re.compile(rf"(^|/)weekly_rail_system_performance_indicators_eng_{year}\.csv$", re.I)
        hits = [n for n in members if pattern.search(n)]
        if len(hits) != 1:
            raise RuntimeError(f"expected one TC English member for {year}: {hits}")
        selected_members.append(hits[0])

    resolved = None
    for member in selected_members:
        reader = csv.DictReader(io.StringIO(decode(z.read(member))))
        headers = reader.fieldnames or []
        hm = {
            "date": exact_header(headers, "Reference_Date", "Reference Date"),
            "carrier": exact_header(headers, "Carrier"),
            "commodity": exact_header(headers, "Commodity"),
            "measure": exact_header(headers, "Measure"),
            "geography": exact_header(headers, "Geography"),
            "value": exact_header(headers, "Measure_Value", "Measure Value"),
        }
        if not all(hm.values()):
            raise RuntimeError(f"TC required headers unavailable: {hm}")
        resolved = hm
        for row in reader:
            if norm(row.get(hm["commodity"], "")) != norm("All Western grain"):
                continue
            if norm(row.get(hm["measure"], "")) != norm("Average Dwell Time at Origin"):
                continue
            if norm(row.get(hm["geography"], "")) != norm("Canada"):
                continue
            carrier = (row.get(hm["carrier"]) or "").strip()
            if carrier not in outcome_carrier_weeks:
                continue
            d = date_from_text(row.get(hm["date"], ""))
            if not d or not (START <= d <= END):
                continue
            wk = week_monday(d)
            outcome_carrier_weeks[carrier].add(wk)
            if bool((row.get(hm["value"]) or "").strip()):
                outcome_nonblank_carrier_weeks[carrier].add(wk)

manifest["transport_canada"] = {
    "download": tc_meta,
    "selected_members": selected_members,
    "resolved_headers": resolved,
    "frozen_outcome": {
        "commodity": "All Western grain",
        "measure": "Average Dwell Time at Origin",
        "geography": "Canada",
        "carriers": ["CN", "CPKC"],
        "carrier_week_keys": {k: len(v) for k, v in outcome_carrier_weeks.items()},
        "nonblank_presence_carrier_week_keys": {k: len(v) for k, v in outcome_nonblank_carrier_weeks.items()},
    },
}

# Relationship-ready lag support is structural only: exposure week t-1 and outcome t.
if exposure_resolution.get("status") == "IDENTIFIABLE":
    fam_key = (
        exposure_resolution["worksheet"], exposure_resolution["metric"], exposure_resolution["period"]
    )
    exposure_weeks = set(family_nonblank_weeks[fam_key])
else:
    exposure_weeks = set()

lagged_support = {}
for carrier in ("CN", "CPKC"):
    count = 0
    for wk in outcome_nonblank_carrier_weeks[carrier]:
        d = date.fromisoformat(wk)
        prev = (d - timedelta(days=7)).isoformat()
        if prev in exposure_weeks:
            count += 1
    lagged_support[carrier] = count
manifest["prospective_panel"] = {
    "one_week_lag_support_by_carrier": lagged_support,
    "min_carrier_lagged_weeks": min(lagged_support.values()) if lagged_support else 0,
    "relationship_computed": False,
}

if exposure_resolution.get("status") != "IDENTIFIABLE":
    gate = "HOLD_CA_GRAIN_E01_EXPOSURE_IDENTITY_AMBIGUOUS"
elif min(lagged_support.values()) < 80:
    gate = "HOLD_CA_GRAIN_E01_PANEL_SUPPORT"
else:
    gate = "PASS_CA_GRAIN_E01_STAGE_A_DESIGN_IDENTIFIABLE"
manifest["gate"] = gate

(OUT / "STAGE_A_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

result = f"""---
id: CA-GRAIN-E01-STAGE-A-RESULT
type: outcome-blind-design-identifiability
issue: 108
gate: {gate}
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E01 Stage A Result

**`{gate}`**

- Upstream current-week semantic GSW families found: **{len(families)}**.
- Exposure resolution: **`{exposure_resolution.get('status')}`**.
- Frozen TC outcome: `All Western grain` × `Average Dwell Time at Origin` × `Canada`; carriers exactly `CN`, `CPKC`.
- Outcome nonblank structural weeks: CN **{len(outcome_nonblank_carrier_weeks['CN'])}**, CPKC **{len(outcome_nonblank_carrier_weeks['CPKC'])}**.
- One-week-lag structurally supported weeks: CN **{lagged_support['CN']}**, CPKC **{lagged_support['CPKC']}**.
- No grain-volume or dwell-time magnitude was parsed, analyzed or persisted; no relationship was computed.

Stage A PASS, if obtained, does not authorize Stage B. Separate adjudication is mandatory.
"""
(OUT / "STAGE_A_RESULT.md").write_text(result, encoding="utf-8")

print(json.dumps({
    "gate": gate,
    "exposure_resolution": exposure_resolution.get("status"),
    "semantic_families": len(families),
    "lagged_support": lagged_support,
    "cost_usd": 0,
}))
