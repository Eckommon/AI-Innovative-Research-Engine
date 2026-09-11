#!/usr/bin/env python3
"""US-UTIL-F01 final outcome-blind county/FIPS join qualification.

Uses EIA-861 2024 final identity/geography only, Census 2024 county Gazetteer
as the county universe, and NOAA Storm Events 2024 county FIPS. Reliability
magnitudes and AMI meter magnitudes are never parsed.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import sys
import urllib.request
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import us_util_f01_source_preflight as base  # noqa: E402
import us_util_f01_source_preflight_sheetfix as sheetfix  # noqa: E402

base.choose_sheet = sheetfix.choose_sheet

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-UTIL-F01"
CENSUS_URL = "https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip"

JOIN_MAP = OUT / "UTILITY_COUNTY_JOIN_MAP.csv"
COUNTY_XWALK = OUT / "COUNTY_CROSSWALK_DIAGNOSTIC.csv"
JOIN_MANIFEST = OUT / "JOIN_SOURCE_MANIFEST.csv"
RESULT = OUT / "JOIN_QUALIFICATION.md"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": base.UA})
    with urllib.request.urlopen(req, timeout=240) as response:
        return response.read(), getattr(response, "status", 200), response.geturl()


def parse_census(payload: bytes):
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        members = [n for n in zf.namelist() if n.lower().endswith(".txt")]
        if len(members) != 1:
            raise RuntimeError(f"unexpected Census Gazetteer members: {zf.namelist()}")
        member = members[0]
        text = io.TextIOWrapper(zf.open(member), encoding="utf-8-sig", errors="replace", newline="")
        reader = csv.DictReader(text, delimiter="\t")
        fields = [str(x or "").strip() for x in (reader.fieldnames or [])]
        lookup = defaultdict(set)
        geoid_to_name = {}
        for row in reader:
            clean = {str(k or "").strip(): v for k, v in row.items()}
            usps = str(clean.get("USPS", "")).strip().upper()
            geoid = str(clean.get("GEOID", "")).strip().zfill(5)
            name = str(clean.get("NAME", "")).strip()
            key = (usps, base.norm_county(name))
            if usps and geoid and key[1]:
                lookup[key].add(geoid)
                geoid_to_name[geoid] = name
    return member, fields, lookup, geoid_to_name


def parse_noaa_event_counts(payload: bytes):
    counts = Counter()
    with gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") as gz:
        text = io.TextIOWrapper(gz, encoding="utf-8-sig", errors="replace", newline="")
        reader = csv.DictReader(text)
        fields = reader.fieldnames or []
        required = {"STATE_FIPS", "CZ_FIPS", "CZ_TYPE"}
        missing = required.difference(fields)
        if missing:
            raise RuntimeError(f"NOAA details missing keys {sorted(missing)}")
        for row in reader:
            if str(row.get("CZ_TYPE", "")).strip().upper() != "C":
                continue
            sf = str(row.get("STATE_FIPS", "")).strip().zfill(2)
            cf = str(row.get("CZ_FIPS", "")).strip().zfill(3)
            if sf.isdigit() and cf.isdigit():
                counts[sf + cf] += 1
    return fields, counts


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    eia_bytes, eia_http, eia_final = base.get(base.EIA_URL)
    with zipfile.ZipFile(io.BytesIO(eia_bytes)) as zf:
        members = sorted(zf.namelist())
    rel_member = base.choose_eia_member(members, "reliability")
    ami_member = base.choose_eia_member(members, "ami")
    service_member = base.choose_eia_member(members, "service")

    rel_ids, rel_meta = base.read_id_set(eia_bytes, rel_member)
    ami_ids, ami_meta = base.read_id_set(eia_bytes, ami_member)
    service_rows, service_ids, _eia_counties, service_meta = base.read_service(eia_bytes, service_member)

    eligible_identity_ids = rel_ids & ami_ids & service_ids
    eligible_service_rows = sorted(
        (u, s, c) for (u, s, c) in service_rows if u in eligible_identity_ids
    )

    census_bytes, census_http, census_final = get(CENSUS_URL)
    census_member, census_fields, census_lookup, census_geoid_name = parse_census(census_bytes)

    index_bytes, _index_http, _index_final = base.get(base.NOAA_INDEX)
    index_text = index_bytes.decode("utf-8", errors="replace")
    details_name = base.resolve_noaa(index_text, "StormEvents_details")
    details_url = base.NOAA_INDEX + details_name
    details_bytes, details_http, details_final = base.get(details_url)
    noaa_fields, event_counts = parse_noaa_event_counts(details_bytes)

    # EIA county key -> Census GEOID exact deterministic mapping only.
    key_status = {}
    for _u, state, county in eligible_service_rows:
        key = (state, county)
        geoids = sorted(census_lookup.get(key, set()))
        if len(geoids) == 1:
            key_status[key] = ("MATCH", geoids[0])
        elif not geoids:
            key_status[key] = ("UNMATCHED", "")
        else:
            key_status[key] = ("AMBIGUOUS", "|".join(geoids))

    by_utility = defaultdict(list)
    for u, state, county in eligible_service_rows:
        status, geoid = key_status[(state, county)]
        by_utility[u].append((state, county, status, geoid))

    fully_mapped_utilities = {
        u for u, rows in by_utility.items()
        if rows and all(status == "MATCH" for _s, _c, status, _g in rows)
    }
    qualified_rows = []
    for u in sorted(fully_mapped_utilities, key=lambda x: (len(x), x)):
        for state, county, status, geoid in sorted(by_utility[u]):
            qualified_rows.append({
                "utility_id": u,
                "state": state,
                "eia_county_normalized": county,
                "census_geoid": geoid,
                "census_county_name": census_geoid_name.get(geoid, ""),
                "noaa_2024_event_records": event_counts.get(geoid, 0),
                "noaa_event_key_present": geoid in event_counts,
            })

    matched_keys = sum(1 for v in key_status.values() if v[0] == "MATCH")
    unmatched_keys = sum(1 for v in key_status.values() if v[0] == "UNMATCHED")
    ambiguous_keys = sum(1 for v in key_status.values() if v[0] == "AMBIGUOUS")
    partially_or_unmapped_utilities = set(by_utility) - fully_mapped_utilities

    # Reapply the frozen initial thresholds to the stricter fully-mapped subset.
    t_rel = len(fully_mapped_utilities) >= 300
    t_ami = len(fully_mapped_utilities) >= 250  # all entered from rel∩AMI∩service
    t_map = len(qualified_rows) >= 1000
    t_noaa = len(event_counts) > 0
    passed = t_rel and t_ami and t_map and t_noaa
    gate = "PASS_US_UTIL_F01_JOIN_READY" if passed else "HOLD_US_UTIL_F01_COUNTY_JOIN_QUALIFICATION"

    with JOIN_MAP.open("w", encoding="utf-8", newline="") as handle:
        fields = ["utility_id", "state", "eia_county_normalized", "census_geoid", "census_county_name", "noaa_2024_event_records", "noaa_event_key_present"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(qualified_rows)

    with COUNTY_XWALK.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["state", "eia_county_normalized", "status", "census_geoid"])
        for (state, county), (status, geoid) in sorted(key_status.items()):
            writer.writerow([state, county, status, geoid])

    manifest_rows = [
        {"source":"EIA861_2024_FINAL_ZIP","url":base.EIA_URL,"http":eia_http,"final_url":eia_final,"bytes":len(eia_bytes),"sha256":sha256(eia_bytes)},
        {"source":"CENSUS_2024_COUNTY_GAZETTEER","url":CENSUS_URL,"http":census_http,"final_url":census_final,"bytes":len(census_bytes),"sha256":sha256(census_bytes)},
        {"source":"NOAA_STORM_EVENTS_2024_DETAILS","url":details_url,"http":details_http,"final_url":details_final,"bytes":len(details_bytes),"sha256":sha256(details_bytes)},
    ]
    with JOIN_MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source","url","http","final_url","bytes","sha256"])
        writer.writeheader(); writer.writerows(manifest_rows)

    total_qualified_event_rows = sum(int(r["noaa_2024_event_records"]) for r in qualified_rows)
    zero_event_keys = sum(1 for r in qualified_rows if int(r["noaa_2024_event_records"]) == 0)

    lines = [
        "---",
        "id: US-UTIL-F01-JOIN-QUALIFICATION",
        "type: outcome-blind-join-qualification",
        "created: 2026-09-11",
        "issue: 94",
        f"gate: {gate}",
        "reliability_magnitudes_parsed: false",
        "ami_meter_magnitudes_parsed: false",
        "relationship_computed: false",
        "incremental_monetary_cost_usd: 0",
        "---",
        "",
        "# US-UTIL-F01 County/FIPS Join Qualification",
        "# US-UTIL-F01 County/FIPS 결합 자격검증",
        "",
        "## Identity rule / identity 규칙",
        "",
        "EIA Service Territory county names are normalized deterministically and joined by exact `USPS state × normalized county name` to the official 2024 Census national county Gazetteer. The unique Census GEOID is then the join key to NOAA Storm Events `STATE_FIPS + CZ_FIPS` for `CZ_TYPE=C`. No fuzzy matching is allowed. / EIA county를 Census GEOID로 정확히 고정한 뒤 NOAA FIPS에 결합하며 fuzzy matching을 사용하지 않는다.",
        "",
        "A county with a valid Census GEOID but no NOAA 2024 Storm Events row is retained as **zero recorded county-event rows**, not treated as an unmapped geography. / Census county는 존재하지만 NOAA event가 없으면 unmapped가 아니라 0-event로 구분한다.",
        "",
        "## Source integrity / source 무결성",
        "",
        f"- EIA-861 final ZIP SHA-256: `{sha256(eia_bytes)}`",
        f"- Census Gazetteer member: `{census_member}`; SHA-256 `{sha256(census_bytes)}`",
        f"- NOAA details: `{details_name}`; SHA-256 `{sha256(details_bytes)}`",
        f"- Census headers: `{', '.join(census_fields)}`",
        "",
        "## Utility identity support / utility identity 지원",
        "",
        f"- Reliability IDs: **{len(rel_ids):,}**",
        f"- Advanced Metering IDs: **{len(ami_ids):,}**",
        f"- Service Territory IDs: **{len(service_ids):,}**",
        f"- Reliability ∩ AMI ∩ Service Territory IDs entering county qualification: **{len(eligible_identity_ids):,}**",
        f"- utilities with **100% of reported Service Territory counties** uniquely Census-mapped: **{len(fully_mapped_utilities):,}**",
        f"- utilities excluded for >=1 unmatched/ambiguous county: **{len(partially_or_unmapped_utilities):,}**",
        "",
        "## County / exposure-key support / county·노출 key 지원",
        "",
        f"- unique EIA state×county keys in eligible utilities: **{len(key_status):,}**",
        f"- exact unique Census matches: **{matched_keys:,}**",
        f"- unmatched Census keys: **{unmatched_keys:,}**",
        f"- ambiguous Census keys: **{ambiguous_keys:,}**",
        f"- qualified utility×county rows after whole-utility completeness rule: **{len(qualified_rows):,}**",
        f"- qualified utility×county rows with zero NOAA event records: **{zero_event_keys:,}**",
        f"- NOAA county event records attached to qualified mappings (diagnostic exposure support only): **{total_qualified_event_rows:,}**",
        "",
        "No storm severity/damage field and no reliability magnitude is used for qualification. NOAA event-row count is only a source-key support diagnostic and is not related to SAIDI/SAIFI here. / 폭풍 강도·피해 및 신뢰도 값은 자격판정에 사용하지 않는다.",
        "",
        "## Frozen structural gate reapplied / 고정 구조 gate 재적용",
        "",
        f"- >=300 fully county-qualified reliability utilities: **{t_rel}** ({len(fully_mapped_utilities):,})",
        f"- >=250 with AMI support: **{t_ami}** ({len(fully_mapped_utilities):,})",
        f"- >=1,000 qualified utility×county mappings: **{t_map}** ({len(qualified_rows):,})",
        f"- NOAA 2024 FIPS route reproducible: **{t_noaa}**",
        "",
        "## Gate / 판정",
        "",
        f"**`{gate}`**",
        "",
        "If PASS, F01 is JOIN_READY only. Any AMI × storm × reliability relationship requires a new preregistered experiment and must address many-to-many exposure aggregation, major-event-day definitions, utility reporting comparability and dependence before outcome values are opened. / PASS여도 JOIN_READY일 뿐이며 효과실험은 별도 사전등록이 필요하다.",
        "",
        "## Durable derived artifacts / 영속 파생 산출물",
        "",
        "- `research/US-UTIL-F01/UTILITY_COUNTY_JOIN_MAP.csv`",
        "- `research/US-UTIL-F01/COUNTY_CROSSWALK_DIAGNOSTIC.csv`",
        "- `research/US-UTIL-F01/JOIN_SOURCE_MANIFEST.csv`",
        "",
        "Raw source bytes remain transient.",
        "",
        "Incremental monetary cost remained **0 USD**.",
    ]
    RESULT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "gate": gate,
        "eligible_identity_ids": len(eligible_identity_ids),
        "fully_mapped_utilities": len(fully_mapped_utilities),
        "qualified_utility_county": len(qualified_rows),
        "matched_county_keys": matched_keys,
        "unmatched_county_keys": unmatched_keys,
        "ambiguous_county_keys": ambiguous_keys,
        "zero_event_utility_county": zero_event_keys,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
