#!/usr/bin/env python3
"""Prospective Q06: official jurisdiction-scope verification for 13 unmatched FIPS.

Read ONLY already preregistered Census GEOID and USDA FIPS, no county
names, RUCC Attribute/Value, geography, population, or outcomes.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path

from tools.qualify_source_census_usda_q04 import fetch_original, SOURCES
from tools.qualify_source_census_usda_q05 import (
    EXPECTED, RotatedSource, UnexpectedCensusGrain,
    require_original, read_census_keys, read_usda_keys,
)

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"research/SOURCE-REGISTRY-S01/qualifications"
Q05=BASE/"CENSUS-USDA-Q05"
Q06=BASE/"CENSUS-USDA-Q06"
OUT=Q06/"evidence/attempt-01.json"
CONTRACT_COMMIT="120930e4bb234ba0c6e652df1c9713fc94e3a2a6"
ISLAND_PREFIXES={
    b"60":"American Samoa",
    b"66":"Guam",
    b"69":"Northern Mariana Islands",
    b"78":"U.S. Virgin Islands",
}
REQUIRED_Q05={
    "census_2024_unique_5digit_geoid":3222,
    "usda_2023_unique_5digit_fips":3235,
    "distinct_key_overlap":3222,
    "usda_keys_not_present_in_2024_census":13,
    "census_keys_not_present_in_usda":0,
    "distinct_state_prefixes_in_overlap":52,
    "usda_duplicate_fips_rows":6468,
    "invalid_census_key_rows":0,
    "invalid_usda_key_rows":0,
    "census_duplicate_key_rows":0,
}
DOCUMENTS={
    "census_gazetteer_2024_scope":"https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2024.html",
    "usda_2023_rucc_scope":"https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation",
    "census_ansi_state_fips":"https://www.census.gov/library/reference/code-lists/ansi.html",
    "census_substantial_county_changes":"https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.html",
}
PASS="PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED"
HOLD_SCOPE="HOLD_Q06_SCOPE_CANNOT_EXPLAIN_ALL_13"
HOLD_RECONCILE="HOLD_Q06_SOURCE_ID_RECONCILIATION"

def verify_context():
    cp=json.loads((ROOT/"context/checkpoint.json").read_text(encoding="utf-8"))
    if not(cp.get("active_issue")==244 and cp.get("last_completed_issue")==203
           and cp.get("last_decision")=="DEC-324"):
        raise RuntimeError("S01 no longer sole active")
    if not (Q06/"CONTRACT.md").is_file() or not (Q05/"RESULT.md").is_file():
        raise RuntimeError("frozen Q06 contract or original Q05 terminal evidence unavailable")
    prior=json.loads((Q05/"evidence/attempt-01.json").read_text(encoding="utf-8"))
    if prior.get("disposition")!="PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED":
        raise RuntimeError("Q05 source-native identity support not documented")
    actual=prior.get("aggregated_source_native_support") or {}
    if any(actual.get(k)!=v for k,v in REQUIRED_Q05.items()) or actual.get("overlap_share_of_usda_keys")!=0.99598145:
        raise RuntimeError("Q05 original totals differ from frozen Q06 contract")
    if prior.get("science_f01_authorized") is not False:
        raise RuntimeError("Q05 science firewall missing")
    for label,(n,sha) in EXPECTED.items():
        p=prior["source_receipts"][label]
        if p.get("full_body_bytes")!=n or p.get("full_body_sha256")!=sha:
            raise RuntimeError("Q05 original source fingerprint changed")
    return prior

def aggregate_scope(census,usda,census_stats,usda_stats):
    common=census&usda
    missing=usda-census
    census_extra=census-usda
    by_prefix={prefix.decode("ascii"):sum(1 for x in missing if x[:2]==prefix)
               for prefix in ISLAND_PREFIXES}
    outside=sum(1 for x in missing if x[:2] not in ISLAND_PREFIXES)
    census_in_excluded=sum(1 for x in census if x[:2] in ISLAND_PREFIXES)
    totals={
        "census_2024_unique_5digit_geoid":len(census),
        "usda_2023_unique_5digit_fips":len(usda),
        "distinct_key_overlap":len(common),
        "usda_keys_not_present_in_2024_census":len(missing),
        "census_keys_not_present_in_usda":len(census_extra),
        "distinct_state_prefixes_in_overlap":len({x[:2] for x in common}),
        "usda_duplicate_fips_rows":usda_stats["usda_duplicate_fips_rows"],
        "invalid_census_key_rows":census_stats["invalid_census_key_rows"],
        "invalid_usda_key_rows":usda_stats["invalid_usda_key_rows"],
        "census_duplicate_key_rows":census_stats["census_duplicate_key_rows"],
    }
    groups={ISLAND_PREFIXES[p]:by_prefix[p.decode("ascii")] for p in ISLAND_PREFIXES}
    result={
        "original_q05_key_count_reconciliation":totals,
        "prospectively_documented_island_area_prefix_totals":groups,
        "excluded_island_area_prefix_count_total":sum(groups.values()),
        "nonexcluded_usda_only_fips_count":outside,
        "census_keys_in_excluded_island_area_prefixes":census_in_excluded,
        "unmatched_key_geography_classification_only":True,
        "individual_county_keys_saved":False,
        "different_geographic_vintages_equivalent_proven":False,
    }
    if any(totals[k]!=v for k,v in REQUIRED_Q05.items()):
        return result,HOLD_RECONCILE
    if (len(missing)!=13 or outside!=0 or census_in_excluded!=0
        or sum(groups.values())!=13 or len(census_extra)!=0):
        return result,HOLD_SCOPE
    return result,PASS

def run(*,fetch=fetch_original,out=OUT):
    if out.exists():
        raise RuntimeError("Q06 original attempt is immutable and may not be repeated")
    verify_context()     # Before source GET or county FIPS projection.
    receipt={
        "qualification":"CENSUS-USDA-Q06",
        "parent_issue":244,
        "attempt":1,
        "contract_commit":CONTRACT_COMMIT,
        "original_q05_disposition":"PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED",
        "observed_utc":datetime.now(timezone.utc).isoformat(),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "documentation":DOCUMENTS,
        "prospectively_excluded_area_prefix_codes":["60","66","69","78"],
        "frozen_q05_comparison_totals":REQUIRED_Q05,
        "source_transport":{},
        "scope_provenance_aggregates":None,
        "disposition":None,
        "failure_type":None,
        "scientific_f01_authorized":False,
        "science_f01_authorized":False,
        "source_case_rows_emitted":False,
        "individual_identifiers_emitted":False,
        "future_outcome_values_emitted":False,
        "usda_attribute_rucc_value_opened":False,
        "census_county_names_coordinates_areas_opened":False,
        "county_2023_2024_boundary_equivalence_verified":False,
        "incremental_monetary_cost_usd":0,
    }
    try:
        blobs={}
        for label,url in SOURCES:
            raw,meta=fetch(label,url)
            blobs[label]=raw
            receipt["source_transport"][label]={
                "url":url,
                "observed_utc":meta.get("observed_utc"),
                "full_body_sha256":meta.get("full_body_sha256"),
                "full_body_bytes":meta.get("full_body_bytes"),
                "http_status":meta.get("status"),
                "source_record_identifiers_not_emitted":True,
            }
        # Verify BOTH complete original full-body SHA and byte count before ID access.
        for label,_ in SOURCES:
            require_original(label,blobs[label],{
                "full_body_sha256":receipt["source_transport"][label]["full_body_sha256"],
                "full_body_bytes":receipt["source_transport"][label]["full_body_bytes"],
            })
        census,cstats=read_census_keys(blobs["CENSUS_2024_COUNTIES"])
        usda,ustats=read_usda_keys(blobs["USDA_2023_RUCC"])
        summary,verdict=aggregate_scope(census,usda,cstats,ustats)
        receipt["scope_provenance_aggregates"]=summary
        receipt["disposition"]=verdict
    except RotatedSource:
        receipt["disposition"]="HOLD_Q06_SOURCE_VINTAGE_CHANGED"
        receipt["failure_type"]="RotatedSource"
    except UnexpectedCensusGrain:
        receipt["disposition"]=HOLD_RECONCILE
        receipt["failure_type"]="UnexpectedCensusGrain"
    except Exception as exc:
        receipt["disposition"]="HOLD_Q06_SOURCE_ACCESS_OR_SCHEMA"
        receipt["failure_type"]=type(exc).__name__
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    (out.parent/(out.stem+".md")).write_text(
        "# Census×USDA Q06 Island Area scope verification / 13개 군코드 지리범위 검증\n\n"
        f"- Verdict / 판정: `{receipt['disposition']}`\n"
        f"- Contract: `{CONTRACT_COMMIT}`\n"
        f"- Official docs / 공식 문서: Census 2024 Gazetteer; USDA 2023 RUCC; Census ANSI FIPS; Census historical county changes\n"
        f"- Scope counts only / 영토별 비식별 집계: `{json.dumps(receipt['scope_provenance_aggregates'],sort_keys=True)}`\n"
        f"- Failure class / 예외 유형: `{receipt['failure_type']}`\n"
        "- 2023↔2024 boundary equivalence remains UNVERIFIED; shared code never validates same area.\n"
        "- No county identifiers, RUCC values, county names, areas or outcomes saved; 0 USD.\n",
        encoding="utf-8")
    print("CENSUS_USDA_Q06",receipt["disposition"],
          "USDA_ONLY",receipt["scope_provenance_aggregates"]["original_q05_key_count_reconciliation"]["usda_keys_not_present_in_2024_census"] if receipt["scope_provenance_aggregates"] else None,
          "ERROR",receipt["failure_type"])
    return receipt

if __name__=="__main__":
    run()
