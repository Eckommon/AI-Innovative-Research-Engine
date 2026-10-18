#!/usr/bin/env python3
"""Immutable R59 source-frontdoor access preflight (official metadata, never outcomes).

Only first four bytes of two ZIPs; HEAD for SEC/USPTO. No redirects,
no private credentials, no API queries about a person, patent, or filer.
"""
from __future__ import annotations
import datetime as dt
import json
from pathlib import Path
import urllib.error
import urllib.request

OUT=Path(__file__).resolve().parents[1]/"research/PORTFOLIO-R59/evidence/source-frontdoor-01.json"
URLS={
 "IPEDS_2023_24_final_zip":("https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2023-24_Final.zip","ZIP4"),
 "SCORECARD_2025_institution_zip":("https://ed-public-download.scorecard.network/downloads/Most-Recent-Cohorts-Institution_05192025.zip","ZIP4"),
 "SEC_submissions_bulk_zip":("https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip","HEAD"),
 "SEC_companyfacts_bulk_zip":("https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip","HEAD"),
 "USPTO_fee_catalog":("https://data.uspto.gov/bulkdata/datasets/ptmnfee2","HEAD"),
 "USPTO_product_api_documented_key":("https://api.uspto.gov/api/v1/datasets/products/search","HEAD"),
}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

def check(url,method,opener=None):
    if (url,method) not in URLS.values():
        raise ValueError("nonfrozen source or request method")
    opener=opener or urllib.request.build_opener(NoRedirect())
    req=urllib.request.Request(url,method=("GET" if method=="ZIP4" else "HEAD"),
        headers={"User-Agent":"AI-Innovative-Research-Engine (https://github.com/Eckommon/AI-Innovative-Research-Engine; metadata-only, no personal cases)","Accept":"*/*"})
    r={"url":url,"method":req.get_method(),"status":None,"content_type":None,
       "length_header":None,"location":None,"read_bytes":0,
       "zip_magic_verified":False,"result":"UNVERIFIED","outcome_rows_opened":False}
    try:
        with opener.open(req,timeout=20) as resp:
            if resp.geturl()!=url: raise RuntimeError("redirect unexpected")
            r["status"]=resp.status
            r["content_type"]=resp.headers.get("Content-Type")
            r["length_header"]=resp.headers.get("Content-Length")
            r["location"]=resp.headers.get("Location")
            if method=="ZIP4":
                b=resp.read(4)
                r["read_bytes"]=len(b)
                r["zip_magic_verified"]=b in (b"PK\x03\x04",b"PK\x05\x06",b"PK\x07\x08")
                r["result"]="ZIP_SIGNATURE_ONLY_NOT_ARCHIVE_PROVEN" if r["zip_magic_verified"] else "ZIP_SIGNATURE_NOT_CONFIRMED"
            else:
                r["result"]="HEAD_METADATA_ONLY_NOT_SOURCE_BODY_PROVEN"
    except urllib.error.HTTPError as ex:
        r.update(status=ex.code,content_type=ex.headers.get("Content-Type"),
                 length_header=ex.headers.get("Content-Length"),location=ex.headers.get("Location"),
                 result="HTTP_UNVERIFIED_NO_ABSENCE_CLAIM")
    except (urllib.error.URLError,TimeoutError,OSError) as ex:
        r.update(result="TRANSPORT_INCONCLUSIVE",error_type=type(ex).__name__)
    return r

def main():
    if OUT.exists():raise RuntimeError("immutable source preflight already exists")
    vals={k:check(url,method) for k,(url,method) in URLS.items()}
    data={
      "research":"PORTFOLIO-R59","issue":237,
      "contract_commit":"22f68ed247c7e6468c60b477fadd17e30d199076",
      "checked_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
      "results":vals,
      "source_semantics":{
        "IPEDS":"NCES 2023-24 final archive, published link; UNITID untested",
        "College_Scorecard":"ED catalog-linked nongov distribution; UNITID/OPEID6 join untested; 2025 file vintage, not proven latest",
        "SEC":"SEC bulk ZIP HEAD only; EDGAR CIK and filings future event rows unopened",
        "USPTO":"USPTO portal/API officially declares 2026 sign-in and API key requirements; HEAD cannot authorize bypass",
      },
      "outcome_rows_opened":False,
      "full_zip_downloads":False,
      "exact_unit_joins_evaluated":False,
      "scores_assigned":False,
      "future_events_exposed":False,
      "incremental_monetary_cost_usd":0,
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=[
      "# R59 first-party frontdoor source preflight / 원천 입구 실측","",
      "- At UTC: \`"+data["checked_at_utc"]+"\`",
      "- **No future outcome rows, no whole ZIP bodies, no exact entity joins, no scores**.",
      "",
      "| Frozen source | HTTP | Method | Bytes read | Signal |",
      "|---|---:|---|---:|---|",
    ]
    for k,v in vals.items():
        lines.append(f"| \`{k}\` | {v['status']} | {v['method']} | {v['read_bytes']} | \`{v['result']}\` |")
    lines += ["","**Caveat / 제한:** 200 HTTP or ZIP magic proves only a particular metadata/prefix response, not whole file, source-unit equivalence or future releases. SEC 403 is not necessarily absence; USPTO account/API-key restrictions cannot be bypassed. College Scorecard delivery URL is ED Data.gov-catalog-linked but a nongov host, not automatically independent first-party.","","Additional cost: **0 USD**.",""]
    OUT.with_suffix(".md").write_text("\n".join(lines),encoding="utf-8")
    print("R59_SOURCE_FRONTDOOR", {k:(v["status"],v["result"]) for k,v in vals.items()})

if __name__=="__main__":
    main()
