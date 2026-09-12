#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-RCRA-F01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "us-rcra-f01"
TMP.mkdir(parents=True, exist_ok=True)

RCRA_URL = "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
GIS_QUERY_URL = "https://echogeo.epa.gov/arcgis/rest/services/ECHO/Facilities/MapServer/3/query"
FEMA_V2_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
UA = "AI-Innovative-Research-Engine/US-RCRA-F01 outcome-blind feasibility"

FEMA_START = date(2015, 1, 1)
FEMA_END = date(2024, 12, 31)
RCRA_YEARS = set(range(2015, 2026))
MIN_OPERATING = 500
MIN_GIS_COVERAGE = 0.80
MIN_STATES = 30
MIN_OVERLAP_STATES = 30


def norm(s: str | None) -> str:
    return re.sub(r"\s+", "", (s or "").strip()).upper()


def parse_date(s: str | None) -> date | None:
    s = (s or "").strip()
    if not s:
        return None
    for fmt, n in (("%m/%d/%Y", 10), ("%Y-%m-%d", 10), ("%Y-%m-%dT%H:%M:%S", 19)):
        try:
            return datetime.strptime(s[:n], fmt).date()
        except ValueError:
            pass
    return None


def member(names: list[str], target: str) -> str:
    hits = [n for n in names if n.rsplit("/", 1)[-1].casefold() == target.casefold()]
    if len(hits) != 1:
        raise RuntimeError(f"expected one {target}, got {hits}")
    return hits[0]


def csv_rows(z: zipfile.ZipFile, name: str):
    raw = z.open(name)
    text = io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")
    return csv.DictReader(text)


def download(url: str, path: Path) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    h = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            h.update(chunk)
            total += len(chunk)
    return total, h.hexdigest()


def post_form(url: str, params: dict[str, str]) -> dict:
    body = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": UA,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def query_gis_for_ids(ids: list[str]) -> tuple[dict[str, set[str]], Counter, int]:
    fips_by_id: dict[str, set[str]] = defaultdict(set)
    systems = Counter()
    feature_count = 0
    batch_size = 75
    for start in range(0, len(ids), batch_size):
        batch = ids[start:start + batch_size]
        escaped = [x.replace("'", "''") for x in batch]
        where = "SOURCE_ID IN (" + ",".join(f"'{x}'" for x in escaped) + ")"
        offset = 0
        while True:
            data = post_form(GIS_QUERY_URL, {
                "f": "json",
                "where": where,
                "outFields": "SOURCE_ID,EPA_SYSTEM,REGISTRY_ID,RCR_STATE,RCR_COUNTY,RCR_FIPS_CODE,FAC_LAT,FAC_LONG",
                "returnGeometry": "false",
                "resultOffset": str(offset),
                "resultRecordCount": "1000",
            })
            if "error" in data:
                raise RuntimeError(f"GIS query error: {data['error']}")
            feats = data.get("features") or []
            for feat in feats:
                a = feat.get("attributes") or {}
                sid = norm(a.get("SOURCE_ID"))
                if not sid:
                    continue
                feature_count += 1
                systems[(a.get("EPA_SYSTEM") or "").strip()] += 1
                fips = (a.get("RCR_FIPS_CODE") or "").strip()
                if re.fullmatch(r"\d{5}", fips):
                    fips_by_id[sid].add(fips)
            if not data.get("exceededTransferLimit") and len(feats) < 1000:
                break
            if not feats:
                break
            offset += len(feats)
    return fips_by_id, systems, feature_count


def fetch_fema_v2() -> tuple[list[dict], dict]:
    all_rows: list[dict] = []
    skip = 0
    top = 1000
    pages = 0
    while True:
        qs = urllib.parse.urlencode({"$top": top, "$skip": skip, "$format": "json"})
        req = urllib.request.Request(FEMA_V2_URL + "?" + qs, headers={"User-Agent": UA, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
        rows = data.get("DisasterDeclarationsSummaries")
        if rows is None:
            rows = next((v for v in data.values() if isinstance(v, list)), None)
        if rows is None:
            raise RuntimeError(f"cannot locate FEMA records in response keys={list(data)}")
        pages += 1
        all_rows.extend(rows)
        if len(rows) < top:
            break
        skip += len(rows)
        if pages > 200:
            raise RuntimeError("unexpected FEMA pagination >200 pages")
    return all_rows, {"pages": pages, "records_all_versions": len(all_rows)}


rcra_path = TMP / "rcra_downloads.zip"
rcra_bytes, rcra_sha256 = download(RCRA_URL, rcra_path)
if not zipfile.is_zipfile(rcra_path):
    raise RuntimeError("RCRA source is not a ZIP")

operating_ids: set[str] = set()
operating_code_counts = Counter()
active_site_labels: set[str] = set()
invalid_operating_codes = Counter()
facility_states: dict[str, str] = {}
facility_latlon_valid = 0
facility_rows = 0

eval_rows = 0
eval_ids: set[str] = set()
eval_years: set[int] = set()
found_violation_domain: set[str] = set()

vio_rows = 0
vio_ids: set[str] = set()
vio_years: set[int] = set()
violation_types: set[str] = set()

hist_rows = 0
hist_ids: set[str] = set()
hist_min: str | None = None
hist_max: str | None = None

with zipfile.ZipFile(rcra_path) as z:
    names = z.namelist()
    required = ["RCRA_FACILITIES.csv", "RCRA_EVALUATIONS.csv", "RCRA_VIOLATIONS.csv", "RCRA_VIOSNC_HISTORY.csv"]
    resolved = {t: member(names, t) for t in required}

    reader = csv_rows(z, resolved["RCRA_FACILITIES.csv"])
    facility_headers = reader.fieldnames or []
    req_fac = {"ID_NUMBER", "ACTIVITY_LOCATION", "ACTIVE_SITE", "OPERATING_TSDF", "LATITUDE83", "LONGITUDE83"}
    miss = sorted(req_fac - set(facility_headers))
    if miss:
        raise RuntimeError(f"missing RCRA facility headers: {miss}")
    for r in reader:
        facility_rows += 1
        rid = norm(r.get("ID_NUMBER"))
        if not rid:
            continue
        facility_states[rid] = (r.get("ACTIVITY_LOCATION") or "").strip().upper()
        active_site_labels.add((r.get("ACTIVE_SITE") or "").strip())
        code = (r.get("OPERATING_TSDF") or "").strip().upper()
        if code:
            operating_code_counts[code] += 1
            valid_chars = set(code) <= set("LIBSTH")
            has_operating = bool(set(code) & set("LIBST"))
            if valid_chars and has_operating:
                operating_ids.add(rid)
            else:
                invalid_operating_codes[code] += 1
        try:
            lat = float((r.get("LATITUDE83") or "").strip())
            lon = float((r.get("LONGITUDE83") or "").strip())
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                facility_latlon_valid += 1
        except ValueError:
            pass

    reader = csv_rows(z, resolved["RCRA_EVALUATIONS.csv"])
    eval_headers = reader.fieldnames or []
    req_eval = {"ID_NUMBER", "EVALUATION_START_DATE", "FOUND_VOLATION"}
    miss = sorted(req_eval - set(eval_headers))
    if miss:
        raise RuntimeError(f"missing RCRA evaluation headers: {miss}")
    for r in reader:
        eval_rows += 1
        rid = norm(r.get("ID_NUMBER"))
        if rid:
            eval_ids.add(rid)
        found_violation_domain.add((r.get("FOUND_VOLATION") or "").strip())
        d = parse_date(r.get("EVALUATION_START_DATE"))
        if d:
            eval_years.add(d.year)

    reader = csv_rows(z, resolved["RCRA_VIOLATIONS.csv"])
    vio_headers = reader.fieldnames or []
    req_vio = {"ID_NUMBER", "VIOLATION_TYPE", "DATE_VIOLATION_DETERMINED"}
    miss = sorted(req_vio - set(vio_headers))
    if miss:
        raise RuntimeError(f"missing RCRA violation headers: {miss}")
    for r in reader:
        vio_rows += 1
        rid = norm(r.get("ID_NUMBER"))
        if rid:
            vio_ids.add(rid)
        vt = (r.get("VIOLATION_TYPE") or "").strip()
        if vt:
            violation_types.add(vt)
        d = parse_date(r.get("DATE_VIOLATION_DETERMINED"))
        if d:
            vio_years.add(d.year)

    reader = csv_rows(z, resolved["RCRA_VIOSNC_HISTORY.csv"])
    hist_headers = reader.fieldnames or []
    req_hist = {"ID_NUMBER", "YRMONTH", "VIO_FLAG", "SNC_FLAG"}
    miss = sorted(req_hist - set(hist_headers))
    if miss:
        raise RuntimeError(f"missing RCRA history headers: {miss}")
    for r in reader:
        hist_rows += 1
        rid = norm(r.get("ID_NUMBER"))
        if rid:
            hist_ids.add(rid)
        ym = (r.get("YRMONTH") or "").strip()
        if re.fullmatch(r"\d{6}", ym):
            hist_min = ym if hist_min is None or ym < hist_min else hist_min
            hist_max = ym if hist_max is None or ym > hist_max else hist_max

operating_list = sorted(operating_ids)
fips_by_id, gis_systems, gis_feature_count = query_gis_for_ids(operating_list)
qualified: dict[str, str] = {}
conflicting_fips: dict[str, list[str]] = {}
for rid in operating_list:
    vals = sorted(fips_by_id.get(rid, set()))
    if len(vals) == 1:
        qualified[rid] = vals[0]
    elif len(vals) > 1:
        conflicting_fips[rid] = vals

qualified_states = {fips[:2] for fips in qualified.values()}
gis_coverage = (len(qualified) / len(operating_ids)) if operating_ids else 0.0

fema_rows, fema_meta = fetch_fema_v2()
fema_headers = sorted({k for r in fema_rows[:50] for k in r})
required_fema = {"fipsStateCode", "fipsCountyCode", "incidentBeginDate", "incidentType", "disasterNumber", "declarationType"}
miss = sorted(required_fema - set(fema_headers))
if miss:
    raise RuntimeError(f"missing FEMA v2 fields: {miss}")

fema_county_fips: set[str] = set()
fema_states: set[str] = set()
fema_incident_types: set[str] = set()
fema_disasters: set[str] = set()
fema_modern_rows = 0
for r in fema_rows:
    d = parse_date(r.get("incidentBeginDate"))
    if d is None or not (FEMA_START <= d <= FEMA_END):
        continue
    sf = str(r.get("fipsStateCode") or "").strip().zfill(2)
    cf = str(r.get("fipsCountyCode") or "").strip().zfill(3)
    if not (re.fullmatch(r"\d{2}", sf) and re.fullmatch(r"\d{3}", cf)):
        continue
    if cf == "000":
        continue
    fema_modern_rows += 1
    fema_county_fips.add(sf + cf)
    fema_states.add(sf)
    it = str(r.get("incidentType") or "").strip()
    if it:
        fema_incident_types.add(it)
    dn = str(r.get("disasterNumber") or "").strip()
    if dn:
        fema_disasters.add(dn)

overlap_states = qualified_states & fema_states
qualified_counties = set(qualified.values())
overlap_counties = qualified_counties & fema_county_fips
qualified_facilities_in_fema_counties = sum(1 for f in qualified.values() if f in fema_county_fips)

temporal_eval_pass = RCRA_YEARS.issubset(eval_years)
temporal_vio_pass = RCRA_YEARS.issubset(vio_years)
temporal_hist_pass = bool(hist_min and hist_max and hist_min <= "201501" and hist_max >= "202512")
temporal_pass = temporal_eval_pass and temporal_vio_pass and temporal_hist_pass

join_pass = (
    len(operating_ids) >= MIN_OPERATING
    and gis_coverage >= MIN_GIS_COVERAGE
    and len(qualified_states) >= MIN_STATES
    and len(overlap_states) >= MIN_OVERLAP_STATES
)
if not join_pass:
    gate = "HOLD_US_RCRA_F01_SOURCE_OR_JOIN_SUPPORT"
elif not temporal_pass:
    gate = "PARTIAL_US_RCRA_F01_JOIN_READY_TEMPORAL_IDENTITY_PENDING"
else:
    gate = "PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY"

manifest = {
    "id": "US-RCRA-F01-FEASIBILITY-MANIFEST",
    "issue": 121,
    "gate": gate,
    "relationship_computed": False,
    "disaster_linked_compliance_outcomes_opened": False,
    "disaster_linked_violation_or_evaluation_counts_computed": False,
    "sources": {
        "rcra_info": {
            "url": RCRA_URL,
            "bytes_transient": rcra_bytes,
            "sha256": rcra_sha256,
            "zip_valid": True,
            "facility_rows": facility_rows,
            "facility_headers": facility_headers,
            "evaluation_headers": eval_headers,
            "violation_headers": vio_headers,
            "viosnc_headers": hist_headers,
        },
        "echo_rcra_gis": {
            "query_url": GIS_QUERY_URL,
            "queried_only_operating_tsdf_ids": True,
            "returned_feature_count": gis_feature_count,
            "epa_system_label_counts_for_returned_features": dict(gis_systems),
        },
        "fema": {
            "endpoint": FEMA_V2_URL,
            "version": 2,
            "headers_observed": fema_headers,
            **fema_meta,
        },
    },
    "rcra_operating_tsdf": {
        "definition": "OPERATING_TSDF nonblank valid combination of L/I/B/S/T with optional H; H alone excluded",
        "unique_ids": len(operating_ids),
        "operating_code_counts": dict(sorted(operating_code_counts.items())),
        "invalid_nonblank_code_counts": dict(sorted(invalid_operating_codes.items())),
        "active_site_label_domain": sorted(active_site_labels),
        "facility_rows_with_valid_latlon": facility_latlon_valid,
        "pass_min_500": len(operating_ids) >= MIN_OPERATING,
    },
    "exact_gis_join": {
        "qualified_unique_id_with_one_fips": len(qualified),
        "coverage_fraction": gis_coverage,
        "missing_or_invalid_fips_ids": len(operating_ids) - len(qualified) - len(conflicting_fips),
        "conflicting_multi_fips_ids": len(conflicting_fips),
        "qualified_state_fips_count": len(qualified_states),
        "qualified_county_fips_count": len(qualified_counties),
        "pass_80pct": gis_coverage >= MIN_GIS_COVERAGE,
        "pass_30_states": len(qualified_states) >= MIN_STATES,
        "no_fuzzy_matching": True,
    },
    "fema_modern_identity": {
        "window": [FEMA_START.isoformat(), FEMA_END.isoformat()],
        "county_coded_rows": fema_modern_rows,
        "distinct_county_fips": len(fema_county_fips),
        "distinct_state_fips": len(fema_states),
        "distinct_disaster_numbers": len(fema_disasters),
        "incident_type_catalog": sorted(fema_incident_types),
        "overlap_state_fips_count_with_qualified_tsdf": len(overlap_states),
        "overlap_county_fips_count_with_qualified_tsdf": len(overlap_counties),
        "qualified_tsdf_facilities_in_any_modern_fema_county": qualified_facilities_in_fema_counties,
        "pass_30_overlap_states": len(overlap_states) >= MIN_OVERLAP_STATES,
    },
    "rcra_compliance_temporal_identity": {
        "required_years": sorted(RCRA_YEARS),
        "evaluation_rows": eval_rows,
        "evaluation_distinct_ids": len(eval_ids),
        "evaluation_years_observed": sorted(eval_years),
        "found_violation_label_domain": sorted(found_violation_domain),
        "violation_rows": vio_rows,
        "violation_distinct_ids": len(vio_ids),
        "violation_years_observed": sorted(vio_years),
        "violation_type_distinct_count": len(violation_types),
        "viosnc_rows": hist_rows,
        "viosnc_distinct_ids": len(hist_ids),
        "viosnc_yrmonth_min": hist_min,
        "viosnc_yrmonth_max": hist_max,
        "evaluation_2015_2025_complete": temporal_eval_pass,
        "violation_2015_2025_complete": temporal_vio_pass,
        "viosnc_spans_2015_2025": temporal_hist_pass,
        "pass_temporal_identity": temporal_pass,
    },
    "raw_source_bytes_persisted": False,
    "incremental_monetary_cost_usd": 0,
}

(OUT / "FEASIBILITY_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({
    "gate": gate,
    "operating_tsdf": len(operating_ids),
    "gis_qualified": len(qualified),
    "gis_coverage": gis_coverage,
    "qualified_states": len(qualified_states),
    "fema_overlap_states": len(overlap_states),
    "temporal_pass": temporal_pass,
    "relationship_computed": False,
}))
shutil.rmtree(TMP, ignore_errors=True)
