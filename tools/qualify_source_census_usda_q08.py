#!/usr/bin/env python3
"""Preregistered Q08: ephemeral Census 2023/24 GEOID only, no county outcome rows."""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import zipfile
from datetime import datetime, timezone
from tools.qualify_source_census_usda_q04 import fetch_original, CENSUS
from tools.qualify_source_census_usda_q07 import fetch as fetch_2023

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"research/SOURCE-REGISTRY-S01/qualifications"
OUT=BASE/"CENSUS-USDA-Q08/evidence/attempt-01.json"
CONTRACT_COMMIT="f46c0a1b5989c44de803f6466866fb0b9ba0be6b"
SOURCES={
 "CENSUS_2023_COUNTIES":(141650,"919df59ba90759cce85468c0337e898e4b39c08eaffce86ddd88fa41f1f7f0c8","2023_Gaz_counties_national.txt",647830),
 "CENSUS_2024_COUNTIES":(141679,"3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0","2024_Gaz_counties_national.txt",647830),
}
PASS="PASS_Q08_CENSUS_2023_2024_GEOID_SYNTAX_SUPPORT_ONLY__BOUNDARY_EQUIVALENCE_UNVERIFIED"
HOLD_SUPPORT="HOLD_Q08_INSUFFICIENT_GEOID_SYNTAX_SUPPORT"

class SourceVintageChanged(ValueError):pass
class UnexpectedKeyGrain(ValueError):pass

def check_original(label,raw,record):
    n,sha,_,_=SOURCES[label]
    if (len(raw)!=n or hashlib.sha256(raw).hexdigest()!=sha
            or record.get("bytes")!=n or record.get("sha256")!=sha):
        raise SourceVintageChanged("original source changed")

def validate_key(token):
    x=token.strip(b" \t\n\r")
    if not re.fullmatch(rb"[0-9]{5}",x) or x[:2]==b"00" or x[2:] in (b"000",b"999"):
        return None
    return x

def read_only_geoid(raw,label):
    _,_,member_name,uncompressed_size=SOURCES[label]
    if not raw.startswith(b"PK\x03\x04"):raise ValueError("unexpected ZIP")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        members=[m for m in archive.infolist() if not m.is_dir()]
        if (len(members)!=1 or members[0].filename!=member_name
                or members[0].file_size!=uncompressed_size or members[0].flag_bits&1):
            raise ValueError("unexpected source member")
        keys=set();bad=0;dupes=0
        with archive.open(members[0]) as stream:
            header=stream.readline(32769)
            if len(header)>32768 or not header.endswith(b"\n"):raise ValueError("header invalid")
            columns=header.rstrip(b"\r\n").split(b"\t")
            if columns.count(b"GEOID")!=1:raise ValueError("missing unique GEOID")
            idx=columns.index(b"GEOID")
            for row in stream:
                vals=row.rstrip(b"\r\n").split(b"\t")
                if len(vals)!=len(columns):raise ValueError("malformed original tab row")
                key=validate_key(vals[idx])
                if key is None:
                    bad+=1;continue
                if key in keys:dupes+=1
                keys.add(key)
    if dupes:raise UnexpectedKeyGrain("repeated original Census GEOID")
    return keys,{"invalid_rows":bad,"duplicate_rows":dupes}

def summarize(keys23,keys24,stat23,stat24):
    common=keys23&keys24
    denominator=min(len(keys23),len(keys24))
    metrics={
        "census_2023_unique_geoid":len(keys23),
        "census_2024_unique_geoid":len(keys24),
        "distinct_geoid_overlap":len(common),
        "only_2023_unique_geoid":len(keys23-keys24),
        "only_2024_unique_geoid":len(keys24-keys23),
        "overlap_share_smaller_vintage":round(len(common)/denominator,8) if denominator else 0,
        "shared_jurisdiction_prefixes":len({x[:2] for x in common}),
        "invalid_2023_rows":stat23["invalid_rows"],
        "invalid_2024_rows":stat24["invalid_rows"],
        "duplicate_2023_rows":stat23["duplicate_rows"],
        "duplicate_2024_rows":stat24["duplicate_rows"],
    }
    yes=(len(keys23)>=3000 and len(keys24)==3222 and len(common)>=3000
         and denominator>0 and len(common)/denominator>=.95
         and metrics["shared_jurisdiction_prefixes"]>=50
         and all(metrics[x]==0 for x in
             ("invalid_2023_rows","invalid_2024_rows","duplicate_2023_rows","duplicate_2024_rows")))
    return metrics,(PASS if yes else HOLD_SUPPORT)

def verify_context():
    cp=json.loads((ROOT/"context/checkpoint.json").read_text())
    if cp.get("active_issue")!=244 or cp.get("last_completed_issue")!=203 or cp.get("last_decision")!="DEC-324":
        raise RuntimeError("S01 no longer authorized")
    if not (BASE/"CENSUS-USDA-Q08/CONTRACT.md").exists():raise RuntimeError("Q08 contract missing")
    p23=json.loads((BASE/"CENSUS-USDA-Q07/evidence/attempt-01.json").read_text())
    p24=json.loads((BASE/"CENSUS-USDA-Q04/evidence/attempt-01.json").read_text())
    if not p23["disposition"].startswith("PASS_Q07_") or not p24["disposition"].startswith("PASS_Q04_"):
        raise RuntimeError("previous original metadata qualifications missing")
    if p23["source_receipt"]["source_body_sha256"]!=SOURCES["CENSUS_2023_COUNTIES"][1]:
        raise RuntimeError("unmatched 2023 source receipt")
    if p24["source_receipts"]["CENSUS_2024_COUNTIES"]["full_body_sha256"]!=SOURCES["CENSUS_2024_COUNTIES"][1]:
        raise RuntimeError("unmatched 2024 source receipt")

def normal_fetch(label):
    if label=="CENSUS_2023_COUNTIES":
        raw,meta=fetch_2023()
        return raw,{"bytes":meta["source_body_bytes"],"sha256":meta["source_body_sha256"]}
    if label=="CENSUS_2024_COUNTIES":
        raw,meta=fetch_original(label,CENSUS)
        return raw,{"bytes":meta["full_body_bytes"],"sha256":meta["full_body_sha256"]}
    raise ValueError("unapproved source")

def run(fetch=normal_fetch,out=OUT):
    if out.exists():raise RuntimeError("Q08 immutable attempt already exists")
    verify_context()
    receipt={
       "qualification":"CENSUS-USDA-Q08","parent_issue":244,
       "contract_commit":CONTRACT_COMMIT,"run_id":os.getenv("GITHUB_RUN_ID"),
       "observed_utc":datetime.now(timezone.utc).isoformat(),
       "disposition":None,"failure_type":None,"raw_original_shas_verified":False,
       "aggregate_syntax_metrics":None,"geography_boundary_equivalence_verified":False,
       "source_case_rows_emitted":False,"individual_identifiers_emitted":False,
       "future_outcome_values_emitted":False,"science_f01_authorized":False,
       "rucc_attribute_value_read":False,"names_area_coordinates_read":False,
       "incremental_monetary_cost_usd":0}
    try:
        blobs={}; records={}
        for name in ("CENSUS_2023_COUNTIES","CENSUS_2024_COUNTIES"):
            raw,meta=fetch(name);blobs[name]=raw;records[name]=meta
        for name in blobs:check_original(name,blobs[name],records[name])
        receipt["raw_original_shas_verified"]=True
        k23,s23=read_only_geoid(blobs["CENSUS_2023_COUNTIES"],"CENSUS_2023_COUNTIES")
        k24,s24=read_only_geoid(blobs["CENSUS_2024_COUNTIES"],"CENSUS_2024_COUNTIES")
        summary,verdict=summarize(k23,k24,s23,s24)
        receipt["aggregate_syntax_metrics"]=summary;receipt["disposition"]=verdict
    except SourceVintageChanged:
        receipt["disposition"]="HOLD_Q08_SOURCE_VINTAGE_CHANGED";receipt["failure_type"]="SourceVintageChanged"
    except UnexpectedKeyGrain:
        receipt["disposition"]="HOLD_Q08_UNEXPECTED_KEY_GRAIN";receipt["failure_type"]="UnexpectedKeyGrain"
    except Exception as exc:
        receipt["disposition"]="HOLD_Q08_SOURCE_ACCESS_OR_SCHEMA";receipt["failure_type"]=type(exc).__name__
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    (out.parent/"attempt-01.md").write_text(
      "# Q08 Census 2023/2024 GEOID syntax-only / 코드 형식적 지원\n\n"
      f"- Verdict: `{receipt['disposition']}`\n"
      f"- Frozen contract: `{CONTRACT_COMMIT}`\n"
      f"- Aggregate only: `{json.dumps(receipt['aggregate_syntax_metrics'],sort_keys=True)}`\n"
      "- Neither stable county geography boundaries nor USDA effects established.\n"
      "- No individual GEOID/NAME/geometry/RUCC value emitted. Cost 0 USD.\n")
    print("CENSUS_USDA_Q08",receipt["disposition"],"SOURCE_LOCK",receipt["raw_original_shas_verified"])
    return receipt

if __name__=="__main__":run()
