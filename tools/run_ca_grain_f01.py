#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import urllib.request
import zipfile
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-F01"
OUT.mkdir(parents=True, exist_ok=True)

TC_URL = "https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip"
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
START = date(2023, 8, 1)
END = date(2025, 7, 31)
UA = "AI-Innovative-Research-Engine/CA-GRAIN-F01 outcome-blind source probe"
INITIAL_RUN = 34673025029


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
        hit = lookup.get(hnorm(name))
        if hit is not None:
            return hit
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
    m = re.fullmatch(r"(20\d\d)[-_/](\d\d?)[-_/](\d\d?)", s)
    if m:
        try:
            return date(*map(int, m.groups()))
        except ValueError:
            pass
    return None


def week_monday(d: date) -> str:
    return (d - timedelta(days=d.weekday())).isoformat()


manifest: dict = {
    "id": "CA-GRAIN-F01",
    "issue": 106,
    "probe_revision": 2,
    "technical_correction": {
        "supersedes_initial_run": INITIAL_RUN,
        "reason": [
            "initial header substring resolution selected *_SortId fields instead of textual label fields",
            "initial probe inspected only the first English annual Transport Canada CSV rather than all 2023-2025 members covering the frozen interval",
        ],
        "frozen_contract_changed": False,
    },
    "boundary": {
        "relationship_computed": False,
        "grain_magnitudes_analyzed_or_persisted": False,
        "dwell_magnitudes_analyzed_or_persisted": False,
        "numeric_source_values_persisted": False,
    },
    "frozen_interval": [START.isoformat(), END.isoformat()],
    "transport_canada": {},
    "gsw": {},
    "incremental_monetary_cost_usd": 0,
}

# Transport Canada full-data ZIP: inspect only schema, textual identities,
# explicit dates and nonblank presence. Numeric measure magnitudes are ignored.
tc_bytes, tc_meta = fetch(TC_URL)
manifest["transport_canada"]["download"] = tc_meta

candidate_dates: set[date] = set()
carriers: set[str] = set()
geographies: set[str] = set()
candidate_rows = 0
available_rows = 0
member_summaries: list[dict] = []

with zipfile.ZipFile(io.BytesIO(tc_bytes)) as z:
    members = [n for n in z.namelist() if n.lower().endswith(".csv")]
    manifest["transport_canada"]["csv_members"] = members

    annual_members = []
    for year in (2023, 2024, 2025):
        pattern = re.compile(rf"(^|/)weekly_rail_system_performance_indicators_eng_{year}\.csv$", re.I)
        hits = [n for n in members if pattern.search(n)]
        if len(hits) != 1:
            raise RuntimeError(f"expected exactly one English Transport Canada CSV for {year}, found {hits}")
        annual_members.append(hits[0])

    manifest["transport_canada"]["selected_members"] = annual_members

    resolved_reference = None
    for member in annual_members:
        text = decode(z.read(member))
        reader = csv.DictReader(io.StringIO(text))
        headers = reader.fieldnames or []

        # Exact textual-label resolution; never allow *_SortId to satisfy label identities.
        h_date = exact_header(headers, "Reference_Date", "Reference Date")
        h_carrier = exact_header(headers, "Carrier")
        h_commodity = exact_header(headers, "Commodity")
        h_measure = exact_header(headers, "Measure")
        h_geography = exact_header(headers, "Geography")
        h_status = exact_header(headers, "Status_of_Value", "Status of Value")
        h_value = exact_header(headers, "Measure_Value", "Measure Value")

        resolved = {
            "reference_date": h_date,
            "carrier": h_carrier,
            "commodity": h_commodity,
            "measure": h_measure,
            "geography": h_geography,
            "status": h_status,
            "measure_value_presence_only": h_value,
        }
        if not all(resolved[k] is not None for k in ("reference_date", "carrier", "commodity", "measure")):
            raise RuntimeError(f"required label/date headers missing in {member}: {resolved}")

        if resolved_reference is None:
            resolved_reference = resolved
        else:
            for key in ("reference_date", "carrier", "commodity", "measure"):
                if hnorm(resolved_reference[key] or "") != hnorm(resolved[key] or ""):
                    raise RuntimeError(f"header identity drift for {key}: {resolved_reference[key]} vs {resolved[key]}")

        member_rows = 0
        member_dates: set[date] = set()
        member_carriers: set[str] = set()
        for row in reader:
            commodity = row.get(h_commodity, "") if h_commodity else ""
            measure = row.get(h_measure, "") if h_measure else ""
            if norm(commodity) != norm("All Western grain"):
                continue
            if norm(measure) != norm("Average Dwell Time at Origin"):
                continue

            d = date_from_text(row.get(h_date, "") if h_date else "")
            if not d or not (START <= d <= END):
                continue

            candidate_rows += 1
            member_rows += 1
            candidate_dates.add(d)
            member_dates.add(d)

            if h_carrier and row.get(h_carrier):
                carrier = row[h_carrier].strip()
                carriers.add(carrier)
                member_carriers.add(carrier)
            if h_geography and row.get(h_geography):
                geographies.add(row[h_geography].strip())

            # Presence only: do not parse, convert, store, compare, rank or aggregate Measure_Value.
            if h_value and bool((row.get(h_value) or "").strip()):
                available_rows += 1

        member_summaries.append({
            "member": member,
            "headers": headers,
            "resolved_headers": resolved,
            "target_rows": member_rows,
            "distinct_dates": len(member_dates),
            "carriers": sorted(member_carriers),
        })

manifest["transport_canada"]["member_summaries"] = member_summaries
manifest["transport_canada"]["resolved_headers"] = resolved_reference or {}
manifest["transport_canada"]["target_identity"] = {
    "commodity": "All Western grain",
    "measure": "Average Dwell Time at Origin",
    "candidate_rows": candidate_rows,
    "nonblank_measure_presence_rows": available_rows,
    "distinct_dates": len(candidate_dates),
    "carriers": sorted(carriers),
    "geographies": sorted(geographies),
}

# Canadian Grain Commission GSW: inspect only headers and temporal identity.
gsw_week_keys: set[str] = set()
for crop, url in GSW_URLS.items():
    b, meta = fetch(url)
    text = decode(b)
    reader = csv.DictReader(io.StringIO(text))
    headers = reader.fieldnames or []

    temporal_headers = [
        h for h in headers
        if any(x in hnorm(h) for x in ("week", "date", "period", "crop year"))
    ]
    detected_dates: set[date] = set()
    detected_week_labels: set[int] = set()
    row_count = 0

    for row in reader:
        row_count += 1
        for h in temporal_headers:
            raw = (row.get(h) or "").strip()
            d = date_from_text(raw)
            if d and START <= d <= END:
                detected_dates.add(d)
            if "week" in hnorm(h) and raw:
                m = re.search(r"\b(?:week\s*)?(\d{1,2})\b", raw, re.I)
                if m and 1 <= int(m.group(1)) <= 53:
                    detected_week_labels.add(int(m.group(1)))

    for d in detected_dates:
        gsw_week_keys.add(week_monday(d))

    manifest["gsw"][crop] = {
        "download": meta,
        "headers": headers,
        "temporal_headers": temporal_headers,
        "rows": row_count,
        "detected_date_identities": len(detected_dates),
        "detected_week_labels": len(detected_week_labels),
    }

tc_week_keys = {week_monday(d) for d in candidate_dates}
common = sorted(tc_week_keys & gsw_week_keys)
manifest["prospective_join"] = {
    "tc_week_keys": len(tc_week_keys),
    "gsw_week_keys_from_explicit_dates": len(gsw_week_keys),
    "common_week_keys_from_explicit_dates": len(common),
    "calendar_rule": "normalize explicit source dates to ISO Monday week key; do not infer missing dates from magnitudes",
}

both_sources = tc_meta["status"] == 200 and all(
    v["download"]["status"] == 200 for v in manifest["gsw"].values()
)
resolved_headers = manifest["transport_canada"]["resolved_headers"]
schema_ok = all(
    resolved_headers.get(k) is not None
    for k in ("reference_date", "carrier", "commodity", "measure")
)
identity_ok = candidate_rows > 0 and len(carriers) >= 2 and len(candidate_dates) >= 80
gsw_ok = all(
    v["rows"] > 0
    and (v["detected_date_identities"] > 0 or v["detected_week_labels"] >= 40)
    for v in manifest["gsw"].values()
)
join_ok = len(common) >= 80

if both_sources and schema_ok and identity_ok and gsw_ok and join_ok:
    gate = "PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE"
elif both_sources and schema_ok and identity_ok and gsw_ok:
    gate = "PARTIAL_CA_GRAIN_F01_SOURCE_READY_JOIN_SEMANTICS_PENDING"
else:
    gate = "HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT"
manifest["gate"] = gate

(OUT / "SOURCE_PANEL_MANIFEST.json").write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

result = f"""---
id: CA-GRAIN-F01-RESULT
type: outcome-blind-source-join-feasibility
issue: 106
probe_revision: 2
supersedes_initial_run: {INITIAL_RUN}
gate: {gate}
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 Result

**`{gate}`**

The initial Run `{INITIAL_RUN}` HOLD was invalidated by the technical audit in `PROBE_AUDIT.md`; the frozen scientific/source contract was not changed.

- Transport Canada full-data download: HTTP {tc_meta['status']}; annual English CSVs inspected for 2023, 2024 and 2025 outcome-blind.
- Frozen identity: `All Western grain` × `Average Dwell Time at Origin`, resolved against exact textual label columns.
- Structurally supported target rows: **{candidate_rows}**; distinct source dates: **{len(candidate_dates)}**; carriers: **{len(carriers)}**.
- GSW frozen crop-year CSVs accessible: **{sum(1 for v in manifest['gsw'].values() if v['download']['status'] == 200)}/2**.
- GSW explicit date-derived week keys: **{len(gsw_week_keys)}**; TC week keys: **{len(tc_week_keys)}**; explicit-date common week keys: **{len(common)}**.
- No grain-volume or dwell-time magnitude was analyzed or persisted; no relationship was computed.

PASS/PARTIAL remains source/join feasibility only and does not authorize an effect test.
"""
(OUT / "RESULT.md").write_text(result, encoding="utf-8")

print(json.dumps({
    "gate": gate,
    "tc_dates": len(candidate_dates),
    "carriers": len(carriers),
    "common_weeks": len(common),
    "cost_usd": 0,
}))
