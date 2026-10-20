#!/usr/bin/env python3
"""Census 2024 × USDA 2023 ID-only, preregistered Q05 structural support.

No source rows/individual FIPS, names, values, RUCC codes or coordinates emitted.
Full source SHAs checked BEFORE reading any row ID.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import zipfile
from tools.qualify_source_census_usda_q04 import fetch_original, CENSUS, USDA, SOURCES

ROOT=Path(__file__).resolve().parents[1]
Q05=ROOT/"research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q05"
Q04=ROOT/"research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q04"
OUT=Q05/"evidence/attempt-01.json"
CONTRACT_COMMIT="b46760beb68b8b6db2ae667e90e0191673f1706b"
EXPECTED={
 "CENSUS_2024_COUNTIES":(141679,"3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0"),
 "USDA_2023_RUCC":(629322,"ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7"),
}
CENSUS_MEMBER="2024_Gaz_counties_national.txt"
USDA_HEADER=b"FIPS,State,County_Name,Attribute,Value"
MIN_CENSUS=3000
MIN_USDA=3000
MIN_OVERLAP=3000
MIN_SHARE=0.95
MIN_STATES=50

class RotatedSource(ValueError):
    pass
class UnexpectedCensusGrain(ValueError):
    pass

def norm_key(raw:bytes):
    # Only ASCII whitespace trimming. Do not zfill, normalize integer or fuzzy repair.
    val=raw.strip(b" \t\r\n")
    if not re.fullmatch(rb"[0-9]{5}",val):
        return None
    if val[:2]==b"00" or val[2:] in (b"000",b"999"):
        return None
    return val  # ephemeral non-persisted source-only FIPS bytes

def require_original(label,raw,receipt):
    expected_len,expected_sha=EXPECTED[label]
    actual=hashlib.sha256(raw).hexdigest()
    if len(raw)!=expected_len or actual!=expected_sha or receipt.get("full_body_sha256")!=expected_sha or receipt.get("full_body_bytes")!=expected_len:
        raise RotatedSource("exact frozen source SHA or length changed")

def read_census_keys(raw, *, expected_uncompressed=647830):
    if not raw.startswith(b"PK\x03\x04"):
        raise ValueError("Census ZIP signature changed")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        files=[i for i in archive.infolist() if not i.is_dir()]
        if len(files)!=1 or files[0].filename!=CENSUS_MEMBER or files[0].flag_bits&1 or files[0].file_size!=expected_uncompressed:
            raise ValueError("Census expected ZIP member/header/vintage changed")
        keys=set()
        invalid=0
        duplicates=0
        with archive.open(files[0]) as stream:
            header=stream.readline(32769)
            if len(header)>32768 or not header.endswith(b"\n"):
                raise ValueError("Census header too long/missing newline")
            cols=header.rstrip(b"\r\n").split(b"\t")
            if cols.count(b"GEOID")!=1:
                raise ValueError("source-native Census GEOID unavailable")
            idx=cols.index(b"GEOID")
            for line in stream:
                # Split only at tab boundaries; NEVER decode county NAME or geographic outcomes.
                columns=line.rstrip(b"\r\n").split(b"\t")
                if len(columns)!=len(cols):
                    raise ValueError("Census tab schema row malformed")
                key=norm_key(columns[idx])
                if key is None:
                    invalid+=1
                    continue
                if key in keys:
                    duplicates+=1
                keys.add(key)
    if duplicates:
        raise UnexpectedCensusGrain("Census source does not have 1 row per unique GEOID")
    return keys,{"invalid_census_key_rows":invalid,"census_duplicate_key_rows":duplicates}

def read_usda_keys(raw):
    rawline=io.BytesIO(raw)
    header=rawline.readline(32769).rstrip(b"\r\n")
    if header != USDA_HEADER:
        raise ValueError("USDA exact five-column source header changed")
    keys=set()
    invalid=0
    duplicates=0
    # FIPS is frozen as first CSV field, unquoted 5 digit token. No parsing of Attribute/Value.
    for line in rawline:
        token=line.split(b",",1)[0]
        key=norm_key(token)
        if key is None:
            invalid+=1
            continue
        if key in keys:
            duplicates+=1
        keys.add(key)
    return keys,{"invalid_usda_key_rows":invalid,"usda_duplicate_fips_rows":duplicates}

def metrics(census,usda,cs,us):
    overlap=census&usda
    n=len(usda)
    result={
      "census_2024_unique_5digit_geoid":len(census),
      "usda_2023_unique_5digit_fips":n,
      "distinct_key_overlap":len(overlap),
      "usda_keys_not_present_in_2024_census":len(usda-census),
      "census_keys_not_present_in_usda":len(census-usda),
      "overlap_share_of_usda_keys":round(len(overlap)/n,8) if n else 0.0,
      "distinct_state_prefixes_in_overlap":len({k[:2] for k in overlap}),
      **cs,**us,
    }
    passed=(len(census)>=MIN_CENSUS and n>=MIN_USDA and len(overlap)>=MIN_OVERLAP
        and (len(overlap)/n if n else 0)>=MIN_SHARE
        and result["distinct_state_prefixes_in_overlap"]>=MIN_STATES
        and result["usda_duplicate_fips_rows"]>0
        and result["census_duplicate_key_rows"]==0)
    return result, ("PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED"
                    if passed else "HOLD_Q05_INSUFFICIENT_NATIVE_FIPS_SUPPORT")

def verify_context():
    cp=json.loads((ROOT/"context/checkpoint.json").read_text(encoding="utf-8"))
    if not (cp.get("active_issue")==244 and cp.get("last_completed_issue")==203 and cp.get("last_decision")=="DEC-324"):
        raise RuntimeError("original S01 only-active context changed")
    if not (Q05/"CONTRACT.md").is_file():
        raise RuntimeError("preregistered Q05 contract missing")
    prior=json.loads((Q04/"evidence/attempt-01.json").read_text(encoding="utf-8"))
    if prior.get("disposition")!="PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN":
        raise RuntimeError("prior Q04 D2 receipt not durable")
    for label,(size,sha) in EXPECTED.items():
        sr=prior["source_receipts"][label]
        if sr.get("full_body_sha256")!=sha or sr.get("full_body_bytes")!=size:
            raise RuntimeError("unmatched frozen Q04 source original body")
    if not (Q04/"RESULT.md").exists():
        raise RuntimeError("Q04 terminal result not durable")

def run(*,fetch=fetch_original,out=OUT):
    if out.exists():
        raise RuntimeError("second same Q05 attempt prohibited")
    verify_context()
    data={
      "qualification":"CENSUS-USDA-Q05",
      "attempt":1,
      "parent_issue":244,
      "contract_commit":CONTRACT_COMMIT,
      "github_run_id":os.getenv("GITHUB_RUN_ID"),
      "checked_utc":datetime.now(timezone.utc).isoformat(),
      "source_receipts":{},
      "aggregated_source_native_support":None,
      "disposition":None,
      "failure_type":None,
      "scientific_inference_performed":False,
      "geographic_vintage_2023_2024_equivalent_verified":False,
      "source_native_exact_semantic_county_join_verified":False,
      "science_f01_authorized":False,
      "source_case_rows_emitted":False,
      "future_outcome_values_emitted":False,
      "individual_identifiers_emitted":False,
      "usda_attribute_or_rucc_value_opened":False,
      "geography_names_areas_coordinates_opened":False,
      "incremental_monetary_cost_usd":0,
    }
    try:
        blobs={}
        for label,url in SOURCES:
            raw,receipt=fetch(label,url)
            data["source_receipts"][label]=receipt
            blobs[label]=raw
        # Verify BOTH source bodies match frozen Q04, BEFORE any record FIPS projection.
        for label,_ in SOURCES:
            require_original(label,blobs[label],data["source_receipts"][label])
        census,cstats=read_census_keys(blobs["CENSUS_2024_COUNTIES"])
        usda,ustats=read_usda_keys(blobs["USDA_2023_RUCC"])
        summary,verdict=metrics(census,usda,cstats,ustats)
        data["aggregated_source_native_support"]=summary
        data["disposition"]=verdict
    except RotatedSource:
        data["disposition"]="HOLD_Q05_SOURCE_VINTAGE_CHANGED"
        data["failure_type"]="RotatedSource"
    except UnexpectedCensusGrain:
        data["disposition"]="HOLD_Q05_UNEXPECTED_CENSUS_KEY_GRAIN"
        data["failure_type"]="UnexpectedCensusGrain"
    except Exception as exc:
        data["disposition"]="HOLD_Q05_SOURCE_ACCESS_OR_SCHEMA"
        data["failure_type"]=type(exc).__name__
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (out.parent/(out.stem+".md")).write_text(
      "# Census USDA Q05 — only county key syntax / 군코드 형식적 중복 검사\n\n"
      f"- Verdict / 판정: `{data['disposition']}`\n"
      f"- Contract: `{CONTRACT_COMMIT}`\n"
      f"- Aggregated counts only / 비식별 집계: `{json.dumps(data['aggregated_source_native_support'],sort_keys=True)}`\n"
      f"- Exception type / 오류유형: `{data['failure_type']}`\n"
      "- 2023 USDA and 2024 Census county geography vintages NOT equivalence-proven.\n"
      "- RUCC Attribute/Value, individual county names and outcomes were never inspected.\n"
      "- County matching is syntactic only; scientific F01 is NOT authorized; cost 0 USD.\n",
      encoding="utf-8")
    print("CENSUS_USDA_Q05",data["disposition"],
          "OVERLAP", data["aggregated_source_native_support"]["distinct_key_overlap"] if data["aggregated_source_native_support"] else None,
          "ERROR",data["failure_type"])
    return data

if __name__=="__main__":
    run()
