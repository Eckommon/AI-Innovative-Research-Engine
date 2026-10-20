#!/usr/bin/env python3
"""S01 Q04 first-party original-byte SHA plus CSV/ZIP header-only qualification.

A prospectively frozen, one-attempt, non-inferential source qualification.
No row content, RUCC values or geographic join are read.
"""
from __future__ import annotations
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
from urllib.request import Request, build_opener, HTTPRedirectHandler
import zipfile

ROOT=Path(__file__).resolve().parents[1]
Q04=ROOT/"research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q04"
OUT=Q04/"evidence/attempt-01.json"
CONTRACT_COMMIT="2dff1a76c99d5ac0699d21ddd0e0fa0a796eb1b5"
CENSUS="https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip"
USDA="https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=89142"
SOURCES=(("CENSUS_2024_COUNTIES",CENSUS),("USDA_2023_RUCC",USDA))
LIMIT=2*1024*1024
HEADER_LIMIT=32768
ZIP_UNCOMPRESSED_MAX=4*1024*1024

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def fetch_original(label,url,opener=None):
    if (label,url) not in SOURCES:
        raise ValueError("unapproved source or redirect target")
    opener=opener or build_opener(NoRedirect())
    request=Request(url,method="GET",headers={"User-Agent":"S01-Q04-source-receipt/1.0","Accept":"*/*"})
    with opener.open(request,timeout=40) as rsp:
        if rsp.status!=200 or rsp.geturl()!=url:
            raise ValueError("non-200 or changed final first-party source")
        data=rsp.read(LIMIT+1)
        if not data or len(data)>LIMIT:
            raise ValueError("oversize or empty exact source body")
        sha=hashlib.sha256(data).hexdigest()  # BEFORE any member/header read
        receipt={
          "url":url, "status":200, "full_body_bytes":len(data),
          "full_body_sha256":sha,
          "content_type":rsp.headers.get("Content-Type"),
          "etag":rsp.headers.get("ETag"),
          "last_modified_http":rsp.headers.get("Last-Modified"),
          "observed_utc":datetime.now(timezone.utc).isoformat(),
          "first_publication_time_verified":False,
          "rows_opened":False,
        }
        return data,receipt

def header_from_line(raw,delimiter):
    if b"\n" not in raw or len(raw)>HEADER_LIMIT:
        raise ValueError("source header missing or too long")
    line=raw.split(b"\n",1)[0].decode("utf-8-sig",errors="strict").rstrip("\r")
    names=next(csv.reader([line],delimiter=delimiter))
    if not names or any(not n.strip() for n in names) or len(set(names))!=len(names):
        raise ValueError("incomplete or duplicate original header")
    if any(len(n)>512 for n in names):
        raise ValueError("unexpected header length")
    return names

def inspect_census(data):
    if not data.startswith(b"PK\x03\x04"):
        raise ValueError("Census ZIP magic invalid")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        files=[m for m in archive.infolist() if not m.is_dir()]
        if len(files)!=1:
            raise ValueError("exact one first-party Census national TXT required")
        member=files[0]
        if (not member.filename.endswith(".txt") or "/" in member.filename
            or "\\" in member.filename or member.filename.startswith(".")
            or member.flag_bits&1 or member.file_size>ZIP_UNCOMPRESSED_MAX):
            raise ValueError("unsafe census member structure")
        with archive.open(member) as s:
            first=s.readline(HEADER_LIMIT+1)
    names=header_from_line(first if first.endswith(b"\n") else first+b"\n", "\t")
    if "GEOID" not in names:
        raise ValueError("literal GEOID missing from Census source header")
    return {"member_filename":member.filename,"member_uncompressed_bytes":member.file_size,
            "header_fields":names,"literal_geoid_present":True,
            "row_count_computed":False,"member_data_values_opened":False}

def inspect_usda(data):
    first=data.split(b"\n",1)[0]
    if len(first)>HEADER_LIMIT or b"\n" not in data:
        raise ValueError("USDA CSV header missing/too long")
    names=header_from_line(first+b"\n",",")
    if "FIPS" not in names:
        raise ValueError("literal FIPS missing from USDA source header")
    return {"header_fields":names,"literal_fips_present":True,
            "row_count_computed":False,"county_rucc_codes_opened":False}

def verify_context():
    cp=json.loads((ROOT/"context/checkpoint.json").read_text(encoding="utf-8"))
    if (cp.get("checkpoint_id")!="CHK-20261020-SOURCE-REGISTRY-S01-ACTIVE"
        or cp.get("active_issue")!=244 or cp.get("last_completed_issue")!=203
        or cp.get("last_decision")!="DEC-324"):
        raise RuntimeError("incorrect sole-active S01 checkpoint")
    if not (Q04/"CONTRACT.md").is_file():
        raise RuntimeError("Q04 preregistration missing from main")
    q03=json.loads((ROOT/"research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q03/evidence/source-structure-01-recovery.json").read_text())
    if q03.get("terminal_operational_disposition")!="HOLD_Q03_OPERATIONAL_INTEGRITY":
        raise RuntimeError("terminal Q03 must be preserved")
    if not (ROOT/"research/US-CMS-NPI-E01/evidence/attempt-01.json").is_file():
        raise RuntimeError("E01 terminal result must be preserved")

def run(*,fetch=fetch_original,out=OUT):
    if out.exists():
        raise RuntimeError("immutable Q04 attempt already exists")
    verify_context()
    receipt={
        "qualification":"CENSUS-USDA-Q04",
        "attempt":1,
        "parent_issue":244,
        "contract_commit":CONTRACT_COMMIT,
        "run_id":os.getenv("GITHUB_RUN_ID"),
        "checked_utc":datetime.now(timezone.utc).isoformat(),
        "source_receipts":{},
        "disposition":None,
        "failure_category":None,
        "original_source_body_sha_before_header":True,
        "geography_vintage_same_verified":False,
        "source_native_county_key_bridge_verified":False,
        "statistical_analysis_authorized":False,
        "science_f01_authorized":False,
        "source_case_rows_emitted":False,
        "future_outcome_values_emitted":False,
        "individual_identifiers_emitted":False,
        "census_area_coordinates_or_names_opened":False,
        "usda_rucc_value_opened":False,
        "incremental_monetary_cost_usd":0,
    }
    try:
        # Exactly 1 nonredirecting GET in frozen order for EACH original body;
        # late failure cannot cause a second request or alternative source.
        for label,url in SOURCES:
            data,record=fetch(label,url)
            receipt["source_receipts"][label]=record
            if label=="CENSUS_2024_COUNTIES":
                receipt["source_receipts"][label]["header"]=inspect_census(data)
            else:
                receipt["source_receipts"][label]["header"]=inspect_usda(data)
        receipt["disposition"]="PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN"
    except Exception as exc:
        receipt["disposition"]="HOLD_Q04_SOURCE_ACCESS_OR_SCHEMA"
        receipt["failure_category"]=type(exc).__name__
        # Never publish response body, row samples, county IDs or exception body.
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (out.parent/(out.stem+".md")).write_text(
      "# CENSUS×USDA Q04 Source-only Receipt / 독립 D2 헤더 검사\n\n"
      f"- Verdict / 판정: `{receipt['disposition']}`\n"
      f"- Contract: `{CONTRACT_COMMIT}`\n"
      f"- Original transport receipts: `{len(receipt['source_receipts'])}`\n"
      f"- Failure type (if any): `{receipt['failure_category']}`\n"
      "- Full-byte SHA fingerprint must precede any header access. No rows opened.\n"
      "- 전체 바이트 지문과 헤더만 검사. 군별 원본값·조인·통계는 미열람.\n"
      "- Not an F01 or county-vintage validation; 0 USD.\n",
      encoding="utf-8")
    print("S01_CENSUS_USDA_Q04",receipt["disposition"],"SOURCE_RECEIPTS",len(receipt["source_receipts"]))
    return receipt

if __name__=="__main__":
    run()
