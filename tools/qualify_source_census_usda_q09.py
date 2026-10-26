#!/usr/bin/env python3
"""First-party Census TIGER year/county archive listing discovery, never ZIP body."""
from datetime import datetime,timezone
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
from urllib.request import build_opener,Request,HTTPRedirectHandler

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"research/SOURCE-REGISTRY-S01/qualifications"
OUT=BASE/"CENSUS-USDA-Q09/evidence/attempt-01.json"
CONTRACT_COMMIT="7d1bfb8e03e4c7eb253748c1293029b08d088de8"
SOURCES={
    "2023":("https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/","tl_2023_us_county.zip"),
    "2024":("https://www2.census.gov/geo/tiger/TIGER2024/COUNTY/","tl_2024_us_county.zip"),
}
LIMIT=256*1024
PASS="PASS_Q09_OFFICIAL_TIGER_2023_2024_COUNTY_ARCHIVES_LISTED__GEOMETRY_UNOPENED"

class RejectRedirect(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

class AnchorReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()!="a":return
        for key,value in attrs:
            if key.lower()=="href" and value is not None:self.hrefs.append(value)

def source_fetch(year,opener=None):
    if year not in SOURCES:raise ValueError("year not frozen")
    url,_=SOURCES[year]
    client=opener or build_opener(RejectRedirect())
    with client.open(Request(url,method="GET",headers={"User-Agent":"S01-Q09-catalog-metadata/1.0"}),
                     timeout=40) as resp:
        if resp.status!=200 or resp.geturl()!=url:
            raise ValueError("original Census directory redirected or non-200")
        raw=resp.read(LIMIT+1)
        if not raw or len(raw)>LIMIT:raise ValueError("original directory body invalid size")
        return raw,{"official_listing_url":url,"http_status":200,
                    "listing_bytes":len(raw),
                    "listing_sha256":hashlib.sha256(raw).hexdigest(),
                    "observed_utc":datetime.now(timezone.utc).isoformat(),
                    "first_publication_timestamp_verified":False}

def check_listing(year,raw):
    if year not in SOURCES:raise ValueError("year not frozen")
    _,required=SOURCES[year]
    text=raw.decode("utf-8",errors="strict")
    if "<a" not in text.lower():raise ValueError("no official hyperlinks")
    reader=AnchorReader();reader.feed(text)
    if reader.hrefs.count(required)!=1:raise ValueError("exact national county ZIP href missing/ambiguous")
    return {"required_archive_basename":required,"exact_relative_href_count":1,
            "archive_body_downloaded":False,"polygon_geometry_read":False}

def verify_context():
    cp=json.loads((ROOT/"context/checkpoint.json").read_text())
    if cp.get("active_issue")!=244 or cp.get("last_decision")!="DEC-324" or cp.get("last_completed_issue")!=203:
        raise RuntimeError("S01 canonical active context mismatch")
    if not (BASE/"CENSUS-USDA-Q09/CONTRACT.md").is_file():
        raise RuntimeError("Q09 prospective contract absent")
    q08=json.loads((BASE/"CENSUS-USDA-Q08/evidence/attempt-01.json").read_text())
    m=q08.get("aggregate_syntax_metrics") or {}
    if (q08.get("disposition")!="PASS_Q08_CENSUS_2023_2024_GEOID_SYNTAX_SUPPORT_ONLY__BOUNDARY_EQUIVALENCE_UNVERIFIED"
            or m.get("census_2023_unique_geoid")!=3222
            or m.get("census_2024_unique_geoid")!=3222
            or m.get("distinct_geoid_overlap")!=3222
            or q08.get("science_f01_authorized") is not False):
        raise RuntimeError("Q08 exact prior source-native key proof missing")
    if not (BASE/"CENSUS-USDA-Q08/RESULT.md").exists():
        raise RuntimeError("Q08 terminal RESULT not in canonical main")

def run(fetch=source_fetch,out=OUT):
    if out.exists():raise RuntimeError("immutable Q09 attempt exists")
    verify_context()
    result={"qualification":"CENSUS-USDA-Q09","parent_issue":244,"contract_commit":CONTRACT_COMMIT,
            "run_id":os.getenv("GITHUB_RUN_ID"),"observed_utc":datetime.now(timezone.utc).isoformat(),
            "source_catalog_receipts":{},"disposition":None,"failure_type":None,
            "archive_bodies_opened":False,"geographic_boundary_equivalence_verified":False,
            "source_case_rows_emitted":False,"individual_identifiers_emitted":False,
            "future_outcome_values_emitted":False,"science_f01_authorized":False,
            "incremental_monetary_cost_usd":0}
    try:
        for year in ("2023","2024"):
            raw,receipt=fetch(year)
            requirement=check_listing(year,raw)
            result["source_catalog_receipts"][year]={**receipt,**requirement}
        result["disposition"]=PASS
    except Exception as exc:
        result["disposition"]="HOLD_Q09_OFFICIAL_CATALOG_OR_SOURCE_ACCESS"
        result["failure_type"]=type(exc).__name__
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    (out.parent/"attempt-01.md").write_text(
        "# Q09 original Census TIGER county listing only / 공식 원본 목록검증\n\n"
        f"- Verdict: `{result['disposition']}`\n"
        f"- Catalogs observed (metadata only): `{json.dumps(result['source_catalog_receipts'],sort_keys=True)}`\n"
        f"- Failure type: `{result['failure_type']}`\n"
        "- No polygon ZIP GET; no geographic boundary equality or F01 authorized.\n"
        "- Large national county archives require distinct Q10 preregistration. Cost 0 USD.\n")
    print("CENSUS_USDA_Q09",result["disposition"],"LISTINGS",len(result["source_catalog_receipts"]))
    return result

if __name__=="__main__":run()
