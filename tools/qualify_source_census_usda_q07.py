#!/usr/bin/env python3
"""Q07 independently preregistered first-party 2023 Census county ZIP D2 header only."""
from __future__ import annotations
from datetime import datetime,timezone
import hashlib
import io
import json
import os
from pathlib import Path
from urllib.request import Request,build_opener,HTTPRedirectHandler
import zipfile

from tools.qualify_source_census_usda_q04 import header_from_line

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"research/SOURCE-REGISTRY-S01/qualifications"
Q07=BASE/"CENSUS-USDA-Q07"
OUT=Q07/"evidence/attempt-01.json"
CONTRACT_COMMIT="42ec3673a00a62fceaa7812868e79a38a4ee8456"
URL="https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_Gaz_counties_national.zip"
MEMBER="2023_Gaz_counties_national.txt"
MAX_COMPRESSED=2*1024*1024
MAX_UNCOMPRESSED=4*1024*1024
HEADER_MAX=32768

class BlockRedirect(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def fetch(opener=None):
    client=opener or build_opener(BlockRedirect())
    req=Request(URL,method="GET",headers={
        "User-Agent":"AI-Innovative-Research-Engine-Q07/1.0 official-metadata-header-only",
        "Accept":"application/zip,*/*"})
    with client.open(req,timeout=40) as rsp:
        if rsp.status!=200 or rsp.geturl()!=URL:
            raise ValueError("official first-party 2023 source redirected or non-200")
        raw=rsp.read(MAX_COMPRESSED+1)
        if not raw or len(raw)>MAX_COMPRESSED:
            raise ValueError("Q07 source empty or exceeds frozen maximum")
        meta={
            "source_url":URL,
            "http_status":rsp.status,
            "source_body_bytes":len(raw),
            "source_body_sha256":hashlib.sha256(raw).hexdigest(),
            "observed_utc":datetime.now(timezone.utc).isoformat(),
            "content_type":rsp.headers.get("Content-Type"),
            "http_etag":rsp.headers.get("ETag"),
            "http_last_modified":rsp.headers.get("Last-Modified"),
            "http_date_is_publication_time":False,
        }
    return raw,meta

def inspect_header_only(raw):
    if not raw.startswith(b"PK\x03\x04"):
        raise ValueError("official Census compressed header not ZIP")
    with zipfile.ZipFile(io.BytesIO(raw)) as zipf:
        members=[m for m in zipf.infolist() if not m.is_dir()]
        if len(members)!=1:
            raise ValueError("single national county TXT member required")
        member=members[0]
        if (member.filename!=MEMBER or member.flag_bits&1
            or member.file_size<=0 or member.file_size>MAX_UNCOMPRESSED):
            raise ValueError("unapproved ZIP member name/encryption/size")
        with zipf.open(member) as stream:
            header=stream.readline(HEADER_MAX+1)
        if not header.endswith(b"\n") or len(header)>HEADER_MAX:
            raise ValueError("header overrun or missing newline")
        names=header_from_line(header,"\t")
        if names.count("GEOID")!=1:
            raise ValueError("2023 header missing exact unique GEOID")
        return {
            "zip_member":MEMBER,
            "zip_member_uncompressed_bytes":member.file_size,
            "tab_header_fields":names,
            "geoid_literal_present":True,
            "county_rows_opened":False,
            "area_or_latlong_fields_opened":False,
            "county_row_count_computed":False,
        }

def verify_context():
    checkpoint=json.loads((ROOT/"context/checkpoint.json").read_text(encoding="utf-8"))
    if not (checkpoint.get("active_issue")==244 and checkpoint.get("last_completed_issue")==203
            and checkpoint.get("last_decision")=="DEC-324"):
        raise RuntimeError("not in frozen S01 post-E01 state")
    if not (Q07/"CONTRACT.md").is_file():
        raise RuntimeError("Q07 prospective contract absent")
    q06=json.loads((BASE/"CENSUS-USDA-Q06/evidence/attempt-01.json").read_text(encoding="utf-8"))
    if q06.get("disposition")!="PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED":
        raise RuntimeError("prior Q06 provenance gate missing")
    if not (BASE/"CENSUS-USDA-Q06/RESULT.md").is_file():
        raise RuntimeError("Q06 terminal result missing from main")

def run(*,source_fetch=fetch,out=OUT):
    if out.exists():
        raise RuntimeError("single original Q07 attempt already recorded")
    verify_context()
    receipt={
        "qualification":"CENSUS-USDA-Q07",
        "contract_commit":CONTRACT_COMMIT,
        "parent_issue":244,
        "original_attempt":1,
        "github_run_id":os.getenv("GITHUB_RUN_ID"),
        "observed_utc":datetime.now(timezone.utc).isoformat(),
        "official_catalog":"https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2023.html",
        "source_receipt":None,
        "original_header_only":None,
        "disposition":None,
        "failure_type":None,
        "source_case_rows_emitted":False,
        "individual_identifiers_emitted":False,
        "future_outcome_values_emitted":False,
        "science_f01_authorized":False,
        "county_2023_2024_geography_equivalent_verified":False,
        "usda_rucc_attribute_or_value_read":False,
        "incremental_monetary_cost_usd":0,
    }
    try:
        raw,meta=source_fetch()
        receipt["source_receipt"]=meta
        receipt["original_header_only"]=inspect_header_only(raw)
        receipt["disposition"]="PASS_Q07_2023_CENSUS_GAZETTEER_D2_HEADERS_ONLY__GEOGRAPHY_BRIDGE_UNPROVEN"
    except Exception as exc:
        receipt["disposition"]="HOLD_Q07_SOURCE_ACCESS_OR_SCHEMA"
        receipt["failure_type"]=type(exc).__name__
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    (out.parent/(out.stem+".md")).write_text(
        "# Q07 original Census 2023 Gazetteer D2 / 2023 군 경계자료 원본 입수 검증\n\n"
        f"- Verdict / 판정: `{receipt['disposition']}`\n"
        f"- Contract: `{CONTRACT_COMMIT}`\n"
        f"- Original full ZIP body & header metadata: `{json.dumps(receipt['source_receipt'],sort_keys=True)}`\n"
        f"- Header only: `{json.dumps(receipt['original_header_only'],sort_keys=True)}`\n"
        "- No 2023 case rows, identifiers, population, geography or RUCC values inspected.\n"
        "- 2023↔2024 same county boundaries NOT proven; Q08 separately preregistered.\n"
        "- Original source request 1 only, 0 USD.\n",
        encoding="utf-8")
    print("CENSUS_USDA_Q07",receipt["disposition"],"SOURCE_BYTES",
          receipt["source_receipt"]["source_body_bytes"] if receipt["source_receipt"] else None,
          "ERROR",receipt["failure_type"])
    return receipt

if __name__=="__main__":
    run()
