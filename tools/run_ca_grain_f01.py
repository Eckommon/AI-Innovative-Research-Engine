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
OUT = ROOT / 'research' / 'CA-GRAIN-F01'
OUT.mkdir(parents=True, exist_ok=True)

TC_URL = 'https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip'
GSW_URLS = {
    '2023-24': 'https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv',
    '2024-25': 'https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv',
}
START = date(2023, 8, 1)
END = date(2025, 7, 31)
UA = 'AI-Innovative-Research-Engine/CA-GRAIN-F01 outcome-blind source probe'


def fetch(url: str) -> tuple[bytes, dict]:
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=120) as r:
        b = r.read()
        return b, {
            'requested_url': url,
            'final_url': r.geturl(),
            'status': getattr(r, 'status', 200),
            'bytes': len(b),
            'sha256': hashlib.sha256(b).hexdigest(),
            'content_type': r.headers.get('Content-Type'),
        }


def decode(b: bytes) -> str:
    for enc in ('utf-8-sig', 'utf-8', 'cp1252', 'latin-1'):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    raise RuntimeError('cannot decode source text')


def norm(s: str) -> str:
    return re.sub(r'\s+', ' ', (s or '').strip()).casefold()


def date_from_text(s: str):
    s = (s or '').strip()
    for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    m = re.fullmatch(r'(20\d\d)[-_/](\d\d?)[-_/](\d\d?)', s)
    if m:
        try:
            return date(*map(int, m.groups()))
        except ValueError:
            pass
    return None


def week_monday(d: date) -> str:
    return (d - timedelta(days=d.weekday())).isoformat()


manifest: dict = {
    'id': 'CA-GRAIN-F01',
    'issue': 106,
    'boundary': {
        'relationship_computed': False,
        'grain_magnitudes_parsed_or_persisted': False,
        'dwell_magnitudes_parsed_or_persisted': False,
        'numeric_source_values_persisted': False,
    },
    'frozen_interval': [START.isoformat(), END.isoformat()],
    'transport_canada': {},
    'gsw': {},
    'incremental_monetary_cost_usd': 0,
}

# Transport Canada full-data ZIP: inspect identity/schema/date support only.
tc_bytes, tc_meta = fetch(TC_URL)
manifest['transport_canada']['download'] = tc_meta
with zipfile.ZipFile(io.BytesIO(tc_bytes)) as z:
    members = [n for n in z.namelist() if n.lower().endswith('.csv')]
    manifest['transport_canada']['csv_members'] = members
    english_candidates = [n for n in members if re.search(r'(eng|en|anglais|english)', n, re.I)]
    member = english_candidates[0] if english_candidates else members[0]
    text = decode(z.read(member))

reader = csv.DictReader(io.StringIO(text))
headers = reader.fieldnames or []
manifest['transport_canada']['selected_member'] = member
manifest['transport_canada']['headers'] = headers

hmap = {norm(h): h for h in headers}
def hfind(*needles):
    for n in needles:
        nn = norm(n)
        for k, raw in hmap.items():
            if nn == k or nn in k:
                return raw
    return None

h_date = hfind('reference date', 'reference_date', 'date')
h_carrier = hfind('carrier')
h_commodity = hfind('commodity')
h_measure = hfind('measure')
h_geography = hfind('geography')
h_status = hfind('status of value', 'status')

required_headers = {'reference_date': h_date, 'carrier': h_carrier, 'commodity': h_commodity,
                    'measure': h_measure, 'geography': h_geography, 'status': h_status}
manifest['transport_canada']['resolved_headers'] = required_headers

candidate_dates, carriers, geographies = set(), set(), set()
candidate_rows = 0
available_rows = 0
for row in reader:
    commodity = (row.get(h_commodity, '') if h_commodity else '')
    measure = (row.get(h_measure, '') if h_measure else '')
    if norm(commodity) != norm('All Western grain'):
        continue
    if norm(measure) != norm('Average Dwell Time at Origin'):
        continue
    d = date_from_text(row.get(h_date, '') if h_date else '')
    if not d or not (START <= d <= END):
        continue
    candidate_rows += 1
    candidate_dates.add(d)
    if h_carrier and row.get(h_carrier): carriers.add(row[h_carrier].strip())
    if h_geography and row.get(h_geography): geographies.add(row[h_geography].strip())
    if h_status:
        sv = norm(row.get(h_status, ''))
        if sv.startswith('0') or 'available' in sv and 'not available' not in sv:
            available_rows += 1

manifest['transport_canada']['target_identity'] = {
    'commodity': 'All Western grain',
    'measure': 'Average Dwell Time at Origin',
    'candidate_rows': candidate_rows,
    'available_presence_rows': available_rows,
    'distinct_dates': len(candidate_dates),
    'carriers': sorted(carriers),
    'geographies': sorted(geographies),
}

# Canadian Grain Commission GSW: inspect headers and temporal identity only.
gsw_week_keys = set()
for crop, url in GSW_URLS.items():
    b, meta = fetch(url)
    text = decode(b)
    reader = csv.DictReader(io.StringIO(text))
    headers = reader.fieldnames or []
    temporal_headers = [h for h in headers if any(x in norm(h) for x in ('week', 'date', 'period', 'crop year', 'crop_year'))]
    detected_dates = set()
    detected_week_labels = set()
    row_count = 0
    for row in reader:
        row_count += 1
        for h in temporal_headers:
            raw = (row.get(h) or '').strip()
            d = date_from_text(raw)
            if d and START <= d <= END:
                detected_dates.add(d)
            if 'week' in norm(h) and raw:
                # Week labels are identity metadata only; do not interpret other numeric columns.
                m = re.search(r'\b(?:week\s*)?(\d{1,2})\b', raw, re.I)
                if m and 1 <= int(m.group(1)) <= 53:
                    detected_week_labels.add(int(m.group(1)))
    # Official GSW crop-year calendar: derive weekly Mondays prospectively from published crop-year convention
    # only when a date field is available; otherwise retain week-label support and classify PARTIAL.
    for d in detected_dates:
        gsw_week_keys.add(week_monday(d))
    manifest['gsw'][crop] = {
        'download': meta,
        'headers': headers,
        'temporal_headers': temporal_headers,
        'rows': row_count,
        'detected_date_identities': len(detected_dates),
        'detected_week_labels': len(detected_week_labels),
    }

# TC weekly keys from source reference dates.
tc_week_keys = {week_monday(d) for d in candidate_dates}
common = sorted(tc_week_keys & gsw_week_keys)
manifest['prospective_join'] = {
    'tc_week_keys': len(tc_week_keys),
    'gsw_week_keys_from_explicit_dates': len(gsw_week_keys),
    'common_week_keys_from_explicit_dates': len(common),
    'calendar_rule': 'normalize explicit source dates to ISO Monday week key; if GSW cumulative CSV lacks explicit dates, do not infer them from magnitudes or repair post hoc',
}

both_sources = tc_meta['status'] == 200 and all(v['download']['status'] == 200 for v in manifest['gsw'].values())
identity_ok = candidate_rows > 0 and len(carriers) >= 2 and len(candidate_dates) >= 80
schema_ok = all(required_headers[k] is not None for k in ('reference_date','carrier','commodity','measure'))
gsw_ok = all(v['rows'] > 0 and (v['detected_date_identities'] > 0 or v['detected_week_labels'] >= 40) for v in manifest['gsw'].values())
join_ok = len(common) >= 80

if both_sources and schema_ok and identity_ok and gsw_ok and join_ok:
    gate = 'PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE'
elif both_sources and schema_ok and identity_ok and gsw_ok:
    gate = 'PARTIAL_CA_GRAIN_F01_SOURCE_READY_JOIN_SEMANTICS_PENDING'
else:
    gate = 'HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT'
manifest['gate'] = gate

(OUT / 'SOURCE_PANEL_MANIFEST.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

result = f'''---
id: CA-GRAIN-F01-RESULT
type: outcome-blind-source-join-feasibility
issue: 106
gate: {gate}
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 Result

**`{gate}`**

- Transport Canada full-data download: HTTP {tc_meta['status']}; CSV schema inspected outcome-blind.
- Frozen identity: `All Western grain` × `Average Dwell Time at Origin`.
- Structurally supported target rows: **{candidate_rows}**; distinct source dates: **{len(candidate_dates)}**; carriers: **{len(carriers)}**.
- GSW frozen crop-year CSVs accessible: **{sum(1 for v in manifest['gsw'].values() if v['download']['status'] == 200)}/2**.
- GSW explicit date-derived week keys: **{len(gsw_week_keys)}**; TC week keys: **{len(tc_week_keys)}**; explicit-date common week keys: **{len(common)}**.
- No grain-volume or dwell-time magnitude was persisted or analyzed; no relationship was computed.

If the result is `PARTIAL`, the unresolved point is calendar/week identity semantics, not an observed relationship. Any repair must be prospectively specified before an effect test.
'''
(OUT / 'RESULT.md').write_text(result, encoding='utf-8')
print(json.dumps({'gate': gate, 'tc_dates':len(candidate_dates), 'carriers':len(carriers), 'common_weeks':len(common), 'cost_usd':0}))
