#!/usr/bin/env python3
"""US-BRIDGE-F01 outcome-blind FHWA NBI × FEMA feasibility runner.

CRITICAL: NBI condition values at legacy Items 58/59/60/62 are NEVER sliced,
decoded, parsed, summarized, ranked, persisted, or compared. Their existence is
verified only from the official fixed-width schema and minimum record length.
"""
from __future__ import annotations

import hashlib
import html.parser
import json
import os
import re
import tempfile
import time
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-BRIDGE-F01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "us-bridge-f01"
TMP.mkdir(parents=True, exist_ok=True)
UA = "AI-Innovative-Research-Engine/US-BRIDGE-F01 outcome-blind feasibility"
YEARS = list(range(2015, 2026))
FEMA_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
FEMA_START = date(2015, 1, 1)
FEMA_END = date(2024, 12, 31)
PHYSICAL_HAZARDS = {
    "Coastal Storm", "Dam/Levee Break", "Earthquake", "Fire", "Flood",
    "Hurricane", "Mud/Landslide", "Severe Ice Storm", "Severe Storm",
    "Snowstorm", "Straight-Line Winds", "Tornado", "Tropical Storm",
    "Typhoon", "Volcanic Eruption", "Winter Storm",
}
ALLOWED_GATES = {
    "PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY",
    "PARTIAL_US_BRIDGE_F01_PANEL_READY_INSPECTION_IDENTITY_PENDING",
    "HOLD_US_BRIDGE_F01_SOURCE_OR_IDENTITY_SUPPORT",
}

# One-based official FHWA positions are documented here only. The condition
# positions are NEVER used to index record bytes.
SCHEMA = {
    "STATE_CODE_001": [1, 3],
    "STRUCTURE_NUMBER_008": [4, 18],
    "COUNTY_CODE_003": [30, 32],
    "DATE_OF_INSPECT_090": [287, 290],
    "DECK_COND_058": [259, 259],
    "SUPERSTRUCTURE_COND_059": [260, 260],
    "SUBSTRUCTURE_COND_060": [261, 261],
    "CULVERT_COND_062": [263, 263],
}
CONDITION_FIELDS = ["DECK_COND_058", "SUPERSTRUCTURE_COND_059", "SUBSTRUCTURE_COND_060", "CULVERT_COND_062"]


def req(url: str, *, accept: str = "*/*", timeout: int = 180):
    return urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept}), timeout


def fetch_bytes(url: str, *, tries: int = 4, timeout: int = 180) -> bytes:
    last = None
    for attempt in range(tries):
        try:
            request, tout = req(url, timeout=timeout)
            with urllib.request.urlopen(request, timeout=tout) as r:
                return r.read()
        except Exception as exc:
            last = exc
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)
    raise last  # pragma: no cover


class Anchors(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self._href = None
        self._text = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._text = []
    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)
    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._href is not None:
            self.items.append((self._href, " ".join(self._text).strip()))
            self._href = None
            self._text = []


def anchors(url: str) -> list[tuple[str, str]]:
    body = fetch_bytes(url).decode("utf-8", errors="replace")
    p = Anchors(); p.feed(body)
    return p.items


def resolve_nbi_zip(year: int) -> tuple[str, str, str]:
    page = f"https://www.fhwa.dot.gov/bridge/nbi/ascii{year}.cfm"
    items = anchors(page)
    # Frozen route: fixed-width/no-delimiter, all highway bridges, national one-file.
    marker = f"{year}hwybronefile"
    hits = []
    for href, text in items:
        low = href.lower()
        if "disclaim.cfm" in low and marker in low and f"{marker}del" not in low:
            hits.append(href)
    if len(hits) != 1:
        raise RuntimeError(f"{year}: expected exactly one fixed-width national one-file disclaimer route, got {hits}")
    disclaimer = urllib.parse.urljoin(page, hits[0])
    proceed = [(h, t) for h, t in anchors(disclaimer) if "proceed to data" in t.lower()]
    if len(proceed) != 1:
        raise RuntimeError(f"{year}: expected one Proceed to Data link, got {proceed}")
    data_url = urllib.parse.urljoin(disclaimer, proceed[0][0])
    return page, disclaimer, data_url


def download(url: str, path: Path) -> tuple[int, str]:
    h = hashlib.sha256(); total = 0; last = None
    for attempt in range(4):
        try:
            request, tout = req(url, timeout=300)
            with urllib.request.urlopen(request, timeout=tout) as r, open(path, "wb") as f:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk: break
                    f.write(chunk); h.update(chunk); total += len(chunk)
            return total, h.hexdigest()
        except Exception as exc:
            last = exc
            try: path.unlink()
            except FileNotFoundError: pass
            h = hashlib.sha256(); total = 0
            if attempt == 3: raise
            time.sleep(2 ** attempt)
    raise last  # pragma: no cover


def parse_mm_yy(raw: bytes) -> str | None:
    s = raw.decode("ascii", errors="strict").strip()
    if not re.fullmatch(r"\d{4}", s): return None
    mm, yy = int(s[:2]), int(s[2:])
    if not 1 <= mm <= 12: return None
    yyyy = 1900 + yy if yy >= 50 else 2000 + yy
    return f"{yyyy:04d}-{mm:02d}-01"


def parse_year(year: int, support: Counter, dates: dict[str, set[str]], county_first: dict[str, str], county_ok: dict[str, bool]) -> dict:
    page, disclaimer, data_url = resolve_nbi_zip(year)
    zpath = TMP / f"nbi-{year}.zip"
    zbytes, zsha = download(data_url, zpath)
    if not zipfile.is_zipfile(zpath):
        raise RuntimeError(f"{year}: resolved source is not a ZIP: {data_url}")
    year_data: dict[str, tuple[str | None, str | None]] = {}
    duplicates = 0; rows = 0; parseable_dates = 0
    min_len = None; max_len = 0
    member_sha = hashlib.sha256(); member_bytes = 0
    with zipfile.ZipFile(zpath) as z:
        candidates = [i for i in z.infolist() if not i.is_dir()]
        if not candidates: raise RuntimeError(f"{year}: empty ZIP")
        target = max(candidates, key=lambda i: i.file_size)
        with z.open(target) as f:
            for raw_line in f:
                member_sha.update(raw_line); member_bytes += len(raw_line)
                line = raw_line.rstrip(b"\r\n")
                if not line: continue
                rows += 1; L = len(line); min_len = L if min_len is None else min(min_len, L); max_len = max(max_len, L)
                if L < 290: raise RuntimeError(f"{year}: short fixed-width record {L}")
                # ONLY identity/time slices below. Never touch bytes 258:263 (Items 58/59/60/62).
                state3 = line[0:3].decode("ascii", errors="strict")
                if not re.fullmatch(r"\d{3}", state3): raise RuntimeError(f"{year}: invalid state code {state3!r}")
                sf = state3[:2]
                structure = line[3:18].decode("ascii", errors="replace").strip()
                if not structure: raise RuntimeError(f"{year}: blank structure number")
                key = sf + "|" + structure
                county3 = line[29:32].decode("ascii", errors="strict").strip()
                county = sf + county3 if re.fullmatch(r"\d{3}", county3) and county3 != "000" else None
                ins = parse_mm_yy(line[286:290])
                if ins is not None: parseable_dates += 1
                if key in year_data:
                    duplicates += 1
                else:
                    year_data[key] = (county, ins)
    schema_supported = (min_len or 0) >= 290
    # Duplicate canonical keys fail closed for the whole state-year contribution.
    if duplicates == 0 and schema_supported:
        for key, (county, ins) in year_data.items():
            support[key] += 1
            if ins is not None: dates[key].add(ins)
            if key not in county_ok: county_ok[key] = True
            if county is None:
                county_ok[key] = False
            elif key not in county_first:
                county_first[key] = county
            elif county_first[key] != county:
                county_ok[key] = False
    try: zpath.unlink()
    except FileNotFoundError: pass
    return {
        "year": year, "page_url": page, "disclaimer_url": disclaimer, "resolved_data_url": data_url,
        "zip_bytes": zbytes, "zip_sha256": zsha, "member_name": target.filename,
        "member_bytes": member_bytes, "member_sha256": member_sha.hexdigest(), "rows": rows,
        "unique_bridge_keys": len(year_data), "duplicate_canonical_keys": duplicates,
        "parseable_inspection_rows": parseable_dates, "min_record_length": min_len, "max_record_length": max_len,
        "fixed_width_identity_positions_supported": schema_supported,
        "condition_schema_positions_documented": True,
        "condition_values_accessed": False,
    }


def parse_date(s) -> date | None:
    s = str(s or "").strip()
    if not s: return None
    try: return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError: return None


def fetch_fema() -> tuple[set[str], dict]:
    top = 1000; skip = 0; pages = 0; total = 0; qualifying_rows = 0
    identities = set(); counties = set(); hazards = Counter(); required_checked = False
    while True:
        qs = urllib.parse.urlencode({"$top": top, "$skip": skip, "$format": "json"})
        payload = fetch_bytes(FEMA_URL + "?" + qs, timeout=180)
        data = json.loads(payload)
        rows = data.get("DisasterDeclarationsSummaries")
        if rows is None: rows = next((v for v in data.values() if isinstance(v, list)), None)
        if rows is None: raise RuntimeError(f"cannot locate FEMA records in {list(data)}")
        if rows and not required_checked:
            reqd = {"fipsStateCode", "fipsCountyCode", "incidentBeginDate", "incidentType", "disasterNumber"}
            missing = sorted(reqd - set(rows[0]))
            if missing: raise RuntimeError(f"missing FEMA identity fields: {missing}")
            required_checked = True
        for r in rows:
            total += 1
            d = parse_date(r.get("incidentBeginDate")); itype = str(r.get("incidentType") or "").strip()
            if d is None or not (FEMA_START <= d <= FEMA_END) or itype not in PHYSICAL_HAZARDS: continue
            sf = str(r.get("fipsStateCode") or "").strip().zfill(2)
            cf = str(r.get("fipsCountyCode") or "").strip().zfill(3)
            if not re.fullmatch(r"\d{2}", sf) or not re.fullmatch(r"\d{3}", cf) or cf == "000": continue
            dn = str(r.get("disasterNumber") or "").strip()
            if not dn: continue
            county = sf + cf
            identity = (county, dn, d.isoformat(), itype)
            if identity in identities: continue
            identities.add(identity); counties.add(county); hazards[itype] += 1; qualifying_rows += 1
        pages += 1
        if len(rows) < top: break
        skip += len(rows)
        if pages > 200: raise RuntimeError("unexpected FEMA pagination >200")
    return counties, {"api": FEMA_URL, "pages": pages, "records_scanned": total, "qualifying_identity_rows": qualifying_rows,
        "unique_qualified_counties": len(counties), "incident_type_counts": dict(sorted(hazards.items()))}


support = Counter(); dates = defaultdict(set); county_first = {}; county_ok = {}
years_manifest = []
for y in YEARS:
    print(f"US-BRIDGE-F01 NBI {y}", flush=True)
    years_manifest.append(parse_year(y, support, dates, county_first, county_ok))

repeated = {k for k, n in support.items() if n >= 6}
date_supported = {k for k in repeated if len(dates.get(k, ())) >= 2}
county_qualified = {k for k in repeated if county_ok.get(k, False) and k in county_first}
county_rate = (len(county_qualified) / len(repeated)) if repeated else 0.0
repeated_states = {k.split("|", 1)[0] for k in repeated}
nbi_counties = {county_first[k] for k in county_qualified}

print("US-BRIDGE-F01 FEMA", flush=True)
fema_counties, fema_meta = fetch_fema()
overlap = nbi_counties & fema_counties
overlap_states = {x[:2] for x in overlap}

all_sources = len(years_manifest) == 11
all_schema = all(m["fixed_width_identity_positions_supported"] and m["condition_schema_positions_documented"] for m in years_manifest)
no_dupes = all(m["duplicate_canonical_keys"] == 0 for m in years_manifest)
base_panel = all_sources and all_schema and no_dupes and len(repeated) >= 300000 and county_rate >= 0.90 and len(repeated_states) >= 45 and len(overlap_states) >= 30 and len(overlap) >= 500
if base_panel and len(date_supported) >= 250000:
    gate = "PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY"
elif base_panel:
    gate = "PARTIAL_US_BRIDGE_F01_PANEL_READY_INSPECTION_IDENTITY_PENDING"
else:
    gate = "HOLD_US_BRIDGE_F01_SOURCE_OR_IDENTITY_SUPPORT"
assert gate in ALLOWED_GATES

result = {
    "research_id": "US-BRIDGE-F01", "issue": 127, "gate": gate,
    "years": [2015, 2025], "annual_sources": 11,
    "canonical_bridges_ge_6_of_11": len(repeated),
    "repeated_bridges_ge_2_distinct_inspection_dates": len(date_supported),
    "county_qualified_repeated_bridges": len(county_qualified),
    "county_qualification_rate": county_rate,
    "repeated_support_state_fips_count": len(repeated_states),
    "qualified_nbi_counties": len(nbi_counties),
    "fema_overlap_state_fips_count": len(overlap_states),
    "fema_overlap_counties": len(overlap),
    "all_years_schema_supported": all_schema,
    "all_years_zero_duplicate_canonical_keys": no_dupes,
    "condition_rating_values_opened": False,
    "condition_rating_row_bytes_sliced": False,
    "relationship_computed": False,
    "fuzzy_repair_used": False,
    "incremental_monetary_cost_usd": 0,
    "raw_source_bytes_persisted": False,
    "implementation_rule": "stable single county across all retained repeated-support observations",
    "fema_declaration_type_restriction_added": False,
    "fema": fema_meta,
}
manifest = {
    "research_id": "US-BRIDGE-F01", "official_record_format": "https://www.fhwa.dot.gov/bridge/nbi/format.cfm",
    "schema_positions": SCHEMA, "condition_fields": CONDITION_FIELDS,
    "condition_values_accessed": False, "annual_sources": years_manifest,
    "fema": fema_meta, "incremental_monetary_cost_usd": 0,
}
(OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(OUT / "EXECUTION_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
