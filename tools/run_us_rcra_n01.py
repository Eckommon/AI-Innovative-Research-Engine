#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import time
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-RCRA-N01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "us-rcra-n01"
TMP.mkdir(parents=True, exist_ok=True)

RCRA_URL = "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
GIS_QUERY_URL = "https://echogeo.epa.gov/arcgis/rest/services/ECHO/Facilities/MapServer/3/query"
FEMA_V2_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
UA = "AI-Innovative-Research-Engine/US-RCRA-N01 outcome-blind paired-CEI probe"

INDEX_START = date(2018, 1, 1)
INDEX_END = date(2023, 12, 31)
FEMA_SCAN_START = date(2017, 1, 1)
FEMA_SCAN_END = date(2025, 12, 31)
WASHOUT_DAYS = 365
PAIR_WINDOW_DAYS = 730
MIN_PAIRS = 100
MIN_STATES = 20
MIN_AGENCY = 0.95

PHYSICAL_HAZARDS = {
    "Coastal Storm",
    "Dam/Levee Break",
    "Earthquake",
    "Fire",
    "Flood",
    "Hurricane",
    "Mud/Landslide",
    "Severe Ice Storm",
    "Severe Storm",
    "Snowstorm",
    "Straight-Line Winds",
    "Tornado",
    "Tropical Storm",
    "Typhoon",
    "Volcanic Eruption",
    "Winter Storm",
}


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
    last_exc: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as exc:
            last_exc = exc
            if attempt == 3:
                raise
            time.sleep(2**attempt)
    assert last_exc is not None
    raise last_exc


def query_gis_for_ids(ids: list[str]) -> tuple[dict[str, set[str]], int]:
    fips_by_id: dict[str, set[str]] = defaultdict(set)
    feature_count = 0
    batch_size = 25
    for start in range(0, len(ids), batch_size):
        batch = ids[start:start + batch_size]
        escaped = [x.replace("'", "''") for x in batch]
        where = "SOURCE_ID IN (" + ",".join(f"'{x}'" for x in escaped) + ")"
        offset = 0
        while True:
            data = post_form(
                GIS_QUERY_URL,
                {
                    "f": "json",
                    "where": where,
                    "outFields": "SOURCE_ID,RCR_FIPS_CODE",
                    "returnGeometry": "false",
                    "resultOffset": str(offset),
                    "resultRecordCount": "1000",
                },
            )
            if "error" in data:
                raise RuntimeError(f"GIS query error: {data['error']}")
            feats = data.get("features") or []
            for feat in feats:
                a = feat.get("attributes") or {}
                sid = norm(a.get("SOURCE_ID"))
                fips = str(a.get("RCR_FIPS_CODE") or "").strip()
                if sid:
                    feature_count += 1
                    if re.fullmatch(r"\d{5}", fips):
                        fips_by_id[sid].add(fips)
            if not data.get("exceededTransferLimit") and len(feats) < 1000:
                break
            if not feats:
                break
            offset += len(feats)
    return fips_by_id, feature_count


def fetch_fema_v2() -> tuple[list[dict], dict]:
    all_rows: list[dict] = []
    top = 1000
    skip = 0
    pages = 0
    while True:
        qs = urllib.parse.urlencode({"$top": top, "$skip": skip, "$format": "json"})
        req = urllib.request.Request(
            FEMA_V2_URL + "?" + qs,
            headers={"User-Agent": UA, "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
        rows = data.get("DisasterDeclarationsSummaries")
        if rows is None:
            rows = next((v for v in data.values() if isinstance(v, list)), None)
        if rows is None:
            raise RuntimeError(f"cannot locate FEMA records in keys={list(data)}")
        all_rows.extend(rows)
        pages += 1
        if len(rows) < top:
            break
        skip += len(rows)
        if pages > 200:
            raise RuntimeError("unexpected FEMA pagination >200 pages")
    return all_rows, {"pages": pages, "records_all_versions": len(all_rows)}


def choose_ce_pair(rows: list[tuple[date, str, str]]) -> tuple[tuple[date, str, str] | None, bool]:
    """Choose one event from rows already restricted to one side/window.

    rows are (date, evaluation_identifier, agency). Caller chooses min/max date.
    Tie rule: lexicographically smallest nonblank identifier; all-blank tie is ambiguous.
    """
    if not rows:
        return None, False
    ids = [r for r in rows if r[1]]
    if len(rows) == 1:
        return rows[0], False
    if ids:
        return sorted(ids, key=lambda x: x[1])[0], False
    return None, True


rcra_path = TMP / "rcra_downloads.zip"
rcra_bytes, rcra_sha256 = download(RCRA_URL, rcra_path)
if not zipfile.is_zipfile(rcra_path):
    raise RuntimeError("RCRA source is not ZIP")

operating_ids: set[str] = set()
operating_code_counts = Counter()
eval_catalog: dict[str, Counter] = defaultdict(Counter)
cei_rows_by_id: dict[str, list[tuple[date, str, str]]] = defaultdict(list)
cei_rows_total = 0
cei_rows_missing_date = 0
cei_rows_missing_identifier = 0
cei_rows_missing_agency = 0
found_violation_header_present = False

with zipfile.ZipFile(rcra_path) as z:
    names = z.namelist()
    facilities_name = member(names, "RCRA_FACILITIES.csv")
    eval_name = member(names, "RCRA_EVALUATIONS.csv")

    # Facility universe: use only ID_NUMBER and OPERATING_TSDF identities.
    raw = z.open(facilities_name)
    text = io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")
    reader = csv.DictReader(text)
    headers = reader.fieldnames or []
    for required in ("ID_NUMBER", "OPERATING_TSDF"):
        if required not in headers:
            raise RuntimeError(f"missing facility header {required}")
    for r in reader:
        rid = norm(r.get("ID_NUMBER"))
        code = (r.get("OPERATING_TSDF") or "").strip().upper()
        if not rid or not code:
            continue
        operating_code_counts[code] += 1
        valid_chars = set(code) <= set("LIBSTH-")
        has_operating = bool(set(code) & set("LIBST"))
        if valid_chars and has_operating:
            operating_ids.add(rid)

    # Evaluation projection: values from FOUND_VIOLATION are never accessed or persisted.
    raw = z.open(eval_name)
    text = io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")
    rows = csv.reader(text)
    eval_headers = next(rows)
    idx = {h: i for i, h in enumerate(eval_headers)}
    required_eval = {
        "ID_NUMBER",
        "EVALUATION_IDENTIFIER",
        "EVALUATION_TYPE",
        "EVALUATION_DESC",
        "EVALUATION_AGENCY",
        "EVALUATION_START_DATE",
    }
    missing = sorted(required_eval - set(idx))
    if missing:
        raise RuntimeError(f"missing evaluation identity headers: {missing}")
    found_violation_header_present = "FOUND_VIOLATION" in idx

    for row in rows:
        if len(row) < len(eval_headers):
            continue
        rid = norm(row[idx["ID_NUMBER"]])
        if rid not in operating_ids:
            continue
        etype = row[idx["EVALUATION_TYPE"]].strip().upper()
        edesc = row[idx["EVALUATION_DESC"]].strip()
        if etype:
            eval_catalog[etype][edesc] += 1
        if etype != "CEI":
            continue
        cei_rows_total += 1
        d = parse_date(row[idx["EVALUATION_START_DATE"]])
        evid = row[idx["EVALUATION_IDENTIFIER"]].strip()
        agency = row[idx["EVALUATION_AGENCY"]].strip().upper()
        if d is None:
            cei_rows_missing_date += 1
            continue
        if not evid:
            cei_rows_missing_identifier += 1
        if not agency:
            cei_rows_missing_agency += 1
        cei_rows_by_id[rid].append((d, evid, agency))

operating_list = sorted(operating_ids)
if len(operating_list) < 500:
    raise RuntimeError(f"F01 operating-universe invariant failed: {len(operating_list)}")

fips_sets, gis_feature_count = query_gis_for_ids(operating_list)
fips_by_id: dict[str, str] = {}
conflicting_fips: dict[str, list[str]] = {}
for rid in operating_list:
    vals = sorted(fips_sets.get(rid, set()))
    if len(vals) == 1:
        fips_by_id[rid] = vals[0]
    elif len(vals) > 1:
        conflicting_fips[rid] = vals

if len(fips_by_id) < 500:
    raise RuntimeError(f"F01 exact-GIS invariant failed: {len(fips_by_id)}")

# FEMA exposure identity only; no RCRA result is joined here.
fema_rows, fema_meta = fetch_fema_v2()
required_fema = {
    "fipsStateCode",
    "fipsCountyCode",
    "incidentBeginDate",
    "incidentType",
    "disasterNumber",
    "declarationType",
}
fema_headers = {k for r in fema_rows[:100] for k in r}
missing_fema = sorted(required_fema - fema_headers)
if missing_fema:
    raise RuntimeError(f"missing FEMA fields: {missing_fema}")

events_by_fips: dict[str, list[tuple[date, int, str]]] = defaultdict(list)
seen_events: set[tuple[str, int, date]] = set()
qualifying_fema_rows = 0
hazard_counts = Counter()
for r in fema_rows:
    if str(r.get("declarationType") or "").strip().upper() != "DR":
        continue
    itype = str(r.get("incidentType") or "").strip()
    if itype not in PHYSICAL_HAZARDS:
        continue
    d = parse_date(str(r.get("incidentBeginDate") or ""))
    if d is None or not (FEMA_SCAN_START <= d <= FEMA_SCAN_END):
        continue
    sf_raw = str(r.get("fipsStateCode") or "").strip()
    cf_raw = str(r.get("fipsCountyCode") or "").strip()
    if not sf_raw or not cf_raw:
        continue
    sf = sf_raw.zfill(2)
    cf = cf_raw.zfill(3)
    if not (re.fullmatch(r"\d{2}", sf) and re.fullmatch(r"\d{3}", cf)) or cf == "000":
        continue
    try:
        dn = int(str(r.get("disasterNumber") or "").strip())
    except ValueError:
        continue
    fips = sf + cf
    key = (fips, dn, d)
    if key in seen_events:
        continue
    seen_events.add(key)
    events_by_fips[fips].append((d, dn, itype))
    qualifying_fema_rows += 1
    hazard_counts[itype] += 1

for fips in events_by_fips:
    events_by_fips[fips].sort(key=lambda x: (x[0], x[1], x[2]))

# Freeze one index event per facility using only FEMA identity/time.
index_by_id: dict[str, tuple[date, int, str]] = {}
index_same_day_multi_disaster = 0
facilities_with_any_index_period_event = 0
for rid, fips in fips_by_id.items():
    events = events_by_fips.get(fips, [])
    candidates = [e for e in events if INDEX_START <= e[0] <= INDEX_END]
    if candidates:
        facilities_with_any_index_period_event += 1
    chosen = None
    for e in candidates:
        d = e[0]
        prior = [p for p in events if d - timedelta(days=WASHOUT_DAYS) <= p[0] < d]
        if prior:
            continue
        same_day = [x for x in candidates if x[0] == d]
        if len({x[1] for x in same_day}) > 1:
            index_same_day_multi_disaster += 1
        chosen = sorted(same_day, key=lambda x: (x[1], x[2]))[0]
        break
    if chosen is not None:
        index_by_id[rid] = chosen

# Construct last-pre / first-post CEI pairs using no compliance-result values.
paired: dict[str, dict] = {}
no_pre = 0
no_post = 0
ambiguous_pre = 0
ambiguous_post = 0
multi_disaster_excluded = 0
for rid, index_event in index_by_id.items():
    index_date, index_dn, index_type = index_event
    rows = cei_rows_by_id.get(rid, [])
    pre_candidates = [r for r in rows if index_date - timedelta(days=PAIR_WINDOW_DAYS) <= r[0] <= index_date - timedelta(days=1)]
    post_candidates = [r for r in rows if index_date + timedelta(days=1) <= r[0] <= index_date + timedelta(days=PAIR_WINDOW_DAYS)]
    if not pre_candidates:
        no_pre += 1
        continue
    if not post_candidates:
        no_post += 1
        continue

    pre_date = max(r[0] for r in pre_candidates)
    post_date = min(r[0] for r in post_candidates)
    pre_same_date = [r for r in pre_candidates if r[0] == pre_date]
    post_same_date = [r for r in post_candidates if r[0] == post_date]
    pre, pre_amb = choose_ce_pair(pre_same_date)
    post, post_amb = choose_ce_pair(post_same_date)
    if pre_amb or pre is None:
        ambiguous_pre += 1
        continue
    if post_amb or post is None:
        ambiguous_post += 1
        continue

    fips = fips_by_id[rid]
    later_events = [
        e for e in events_by_fips.get(fips, [])
        if index_date < e[0] <= post[0] and e[1] != index_dn
    ]
    if later_events:
        multi_disaster_excluded += 1
        continue

    paired[rid] = {
        "state_fips": fips[:2],
        "county_fips": fips,
        "index_date": index_date.isoformat(),
        "index_disaster_number": index_dn,
        "index_incident_type": index_type,
        "pre_cei_date": pre[0].isoformat(),
        "pre_evaluation_identifier": pre[1],
        "pre_agency_present": bool(pre[2]),
        "post_cei_date": post[0].isoformat(),
        "post_evaluation_identifier": post[1],
        "post_agency_present": bool(post[2]),
    }

paired_states = sorted({v["state_fips"] for v in paired.values()})
pre_agency_present = sum(1 for v in paired.values() if v["pre_agency_present"])
post_agency_present = sum(1 for v in paired.values() if v["post_agency_present"])
pair_n = len(paired)
pre_agency_fraction = pre_agency_present / pair_n if pair_n else 0.0
post_agency_fraction = post_agency_present / pair_n if pair_n else 0.0

cei_desc_counts = dict(eval_catalog.get("CEI", {}))
cei_identity_deterministic = bool(cei_desc_counts) and any(
    "COMPLIANCE EVALUATION INSPECTION" in desc.upper() for desc in cei_desc_counts
)
disaster_identity_pass = bool(index_by_id) and qualifying_fema_rows > 0
pair_support_pass = pair_n >= MIN_PAIRS and len(paired_states) >= MIN_STATES
agency_pass = pre_agency_fraction >= MIN_AGENCY and post_agency_fraction >= MIN_AGENCY
literature = (OUT / "LITERATURE_ADJUDICATION.md").read_text(encoding="utf-8")
near_identical_found = "near_identical_found: true" in literature.lower()

if not cei_identity_deterministic:
    gate = "HOLD_US_RCRA_N01_CEI_IDENTITY_UNAVAILABLE"
elif not disaster_identity_pass:
    gate = "HOLD_US_RCRA_N01_DISASTER_IDENTITY_SUPPORT"
elif not pair_support_pass or not agency_pass:
    gate = "HOLD_US_RCRA_N01_PAIRED_SUPPORT_INSUFFICIENT"
elif near_identical_found:
    gate = "HOLD_US_RCRA_N01_NOVELTY_OVERLAP"
else:
    gate = "PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE"

manifest = {
    "id": "US-RCRA-N01-DESIGN-MANIFEST",
    "issue": 123,
    "gate": gate,
    "boundary": {
        "found_violation_header_present": found_violation_header_present,
        "found_violation_values_accessed_or_persisted": False,
        "disaster_linked_violation_counts_or_rates_computed": False,
        "relationship_computed": False,
        "raw_source_bytes_persisted": False,
    },
    "preregistration": {
        "facility_universe": "US-RCRA-F01 current operating TSDF semantics",
        "declaration_type": "DR",
        "physical_hazard_set": sorted(PHYSICAL_HAZARDS),
        "index_period": [INDEX_START.isoformat(), INDEX_END.isoformat()],
        "fema_scan_period": [FEMA_SCAN_START.isoformat(), FEMA_SCAN_END.isoformat()],
        "washout_days": WASHOUT_DAYS,
        "pre_post_pair_window_days": PAIR_WINDOW_DAYS,
        "pair_rule": "same facility; CEI only; last pre / first post; tie by lexicographically smallest nonblank EVALUATION_IDENTIFIER; all-blank tied date excluded",
        "multi_disaster_rule": "exclude if another qualifying FEMA DR begins after index and on/before selected post CEI",
        "minimum_pairs": MIN_PAIRS,
        "minimum_state_territory_fips": MIN_STATES,
        "minimum_pre_and_post_agency_identity_fraction": MIN_AGENCY,
    },
    "source": {
        "rcra_url": RCRA_URL,
        "rcra_bytes_transient": rcra_bytes,
        "rcra_sha256": rcra_sha256,
        "operating_tsdf_unique_ids": len(operating_ids),
        "operating_code_counts": dict(sorted(operating_code_counts.items())),
        "gis_exact_single_fips_ids": len(fips_by_id),
        "gis_feature_count": gis_feature_count,
        "gis_conflicting_fips_ids": len(conflicting_fips),
        "fema_endpoint": FEMA_V2_URL,
        "fema_pages": fema_meta["pages"],
        "fema_records_all_versions": fema_meta["records_all_versions"],
    },
    "cei_identity": {
        "evaluation_type_catalog_for_operating_tsdf": {
            k: dict(v) for k, v in sorted(eval_catalog.items())
        },
        "cei_description_counts": cei_desc_counts,
        "cei_identity_deterministic": cei_identity_deterministic,
        "cei_rows_total_for_operating_tsdf": cei_rows_total,
        "cei_rows_missing_date": cei_rows_missing_date,
        "cei_rows_missing_identifier": cei_rows_missing_identifier,
        "cei_rows_missing_agency": cei_rows_missing_agency,
    },
    "fema_identity": {
        "qualifying_unique_county_disaster_rows": qualifying_fema_rows,
        "hazard_counts": dict(sorted(hazard_counts.items())),
        "facilities_with_any_index_period_event": facilities_with_any_index_period_event,
        "facilities_with_frozen_index_after_washout": len(index_by_id),
        "same_day_multi_disaster_index_facilities": index_same_day_multi_disaster,
        "disaster_identity_pass": disaster_identity_pass,
    },
    "paired_cei_structural_support": {
        "paired_facilities": pair_n,
        "paired_state_territory_fips_count": len(paired_states),
        "paired_state_territory_fips": paired_states,
        "no_pre_cei": no_pre,
        "no_post_cei": no_post,
        "ambiguous_pre_tie_excluded": ambiguous_pre,
        "ambiguous_post_tie_excluded": ambiguous_post,
        "multi_disaster_contaminated_excluded": multi_disaster_excluded,
        "pre_agency_identity_fraction": pre_agency_fraction,
        "post_agency_identity_fraction": post_agency_fraction,
        "pass_minimum_pairs_and_states": pair_support_pass,
        "pass_agency_identity": agency_pass,
    },
    "literature_overlap": {
        "bounded_note": "research/US-RCRA-N01/LITERATURE_ADJUDICATION.md",
        "near_identical_found": near_identical_found,
        "novelty_proven": False,
    },
    "incremental_monetary_cost_usd": 0,
}

(OUT / "DESIGN_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

# Remove downloaded raw bytes after derived manifest exists.
try:
    shutil.rmtree(TMP)
except FileNotFoundError:
    pass

print(json.dumps({
    "gate": gate,
    "operating_tsdf": len(operating_ids),
    "indexed_facilities": len(index_by_id),
    "paired_facilities": pair_n,
    "paired_states": len(paired_states),
    "pre_agency_fraction": pre_agency_fraction,
    "post_agency_fraction": post_agency_fraction,
    "found_violation_values_accessed": False,
    "cost_usd": 0,
}))
