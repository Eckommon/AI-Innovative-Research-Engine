#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
import csv, hashlib, io, json, os, re, tempfile

import requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="25ec9b9c9031e6ee48ea1e4e47ddb27826506331"
ISSUE=192
OUTDIR=ROOT/"research/CA-CRA-CHARITY-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"

DATASETS={
  2018:"206f5517-12c3-40e0-9494-c75d2e410c64",
  2019:"21118663-1847-48ce-81ce-1ac7cff674c0",
  2020:"5577f7aa-7a96-4c59-bc01-47ad54203930",
  2021:"3e8a4d9f-9a12-4498-9a0b-a5c81d3281b4",
  2022:"b2acb3be-c720-4329-a8c0-d4d36c8db61e",
  2023:"05b3abd0-e70f-4b3b-a9c5-acc436bd15b6",
  2024:"80c00cdb-1358-415c-bb8b-0de7f12675b8",
}
REVOCATIONS="https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/revoking-registered-status/list-published-revocations-charities-oqd.html"
SEARCH_TIPS="https://www.canada.ca/en/revenue-agency/services/charities-giving/list-charities/search-tips-charities-listings.html"
ANNULMENT="https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/revoking-registered-status/annulment-charitable-registration.html"
REVOCATION_TYPES="https://www.canada.ca/en/revenue-agency/services/charities-giving/charities/revoking-registered-status/types-revocation.html"
BN_RE=re.compile(r"^[0-9]{9}RR[0-9]{4}$")

csv.field_size_limit(1024*1024*64)

def sha_bytes(b:bytes): return hashlib.sha256(b).hexdigest()

def fetch(url,timeout=180):
    r=requests.get(url,headers={"User-Agent":UA},timeout=timeout,allow_redirects=True)
    r.raise_for_status()
    return r, {
      "status":r.status_code,"requested_url":url,"final_url":r.url,
      "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
      "etag":r.headers.get("etag"),"bytes":len(r.content),"sha256":sha_bytes(r.content)
    }

def norm_bn(v):
    s=str(v or "").strip().replace(" ","").upper()
    return s if BN_RE.fullmatch(s) else None

def parse_csv_bytes(b):
    text=None
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            text=b.decode(enc);break
        except UnicodeDecodeError: pass
    if text is None: raise RuntimeError("CSV_ENCODING_UNRESOLVED")
    sample=text[:20000]
    try: dialect=csv.Sniffer().sniff(sample,delimiters=",;\t")
    except Exception: dialect=csv.excel
    rr=csv.DictReader(io.StringIO(text),dialect=dialect)
    fields=[str(x or "").strip() for x in (rr.fieldnames or [])]
    rows=[{str(k or "").strip():v for k,v in r.items()} for r in rr]
    return fields,rows

def dataset_page(year):
    did=DATASETS[year]
    return f"https://open.canada.ca/data/en/dataset/{did}"

def discover_csvs(year):
    r,meta=fetch(dataset_page(year),120)
    soup=BeautifulSoup(r.text,"html.parser")
    urls=[]
    for a in soup.find_all("a",href=True):
        u=urljoin(r.url,a["href"])
        ul=u.lower()
        if "/download/" in ul and ".csv" in ul:
            urls.append(u)
    urls=list(dict.fromkeys(urls))
    def pick(token):
        c=[u for u in urls if token in u.lower()]
        return c[0] if c else None
    return {
      "page_meta":meta,"all_csv_count":len(urls),
      "identification":pick("ident_"),
      "general":pick("financial_section_a_b_and_c_"),
      "financial":pick("financial_d_and_schedule_6_")
    }

def parse_date(s):
    s=str(s or "").strip()
    for f in ("%Y-%m-%d","%Y/%m/%d","%m/%d/%Y","%Y-%m-%dT%H:%M:%S"):
        try:return datetime.strptime(s,f).date()
        except ValueError:pass
    return None

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-01 evidence exists")

    ev={
      "research":"CA-CRA-CHARITY-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
      "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
      "later_status_refresh_opened":False,"future_revocation_membership_opened":False,
      "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
      "causal_claim_made":False,"prohibited_compliance_exposure_computed":False,
      "identity_repair_used":False,"gates":[]
    }
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261002-CA-CRA-CHARITY-F01-ACTIVE"
            and cp.get("active_issue")==192 and cp.get("active_research")=="CA-CRA-CHARITY-F01"
            and cp.get("last_decision")=="DEC-296")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})

        bound=os.environ.get("CRA_CHARITY_F01_BOUND")=="1" and os.environ.get("CRA_CHARITY_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":192,"contract_sha":os.environ.get("CRA_CHARITY_F01_CONTRACT_SHA")}})

        docs={}
        for k,u in {"revocations":REVOCATIONS,"search_tips":SEARCH_TIPS,"annulment":ANNULMENT,"revocation_types":REVOCATION_TYPES}.items():
            try:
                rr,mm=fetch(u,120); docs[k]=mm; docs[k]["text"]=BeautifulSoup(rr.text,"html.parser").get_text(" ",strip=True)[:20000]
            except Exception as e:
                docs[k]={"error":f"{type(e).__name__}:{e}","url":u}

        annual={}
        annual_ids={}
        all_annual_ids=set()
        annual_lineage_ok=True
        schema_ok=True
        syntax_year={}
        support_year={}

        for year in range(2018,2025):
            d=discover_csvs(year)
            if not d["identification"]:
                annual_lineage_ok=False
                annual[year]={"discovery":d,"error":"IDENTIFICATION_CSV_NOT_RESOLVED"}
                continue
            rr,mm=fetch(d["identification"],240)
            fields,rows=parse_csv_bytes(rr.content)
            bn_field=next((x for x in fields if x.strip().upper()=="BN"),None)
            if bn_field is None: schema_ok=False

            nonblank=valid=0; ids=set()
            if bn_field:
                for row in rows:
                    raw=str(row.get(bn_field) or "")
                    if raw.strip(): nonblank+=1
                    b=norm_bn(raw)
                    if b: valid+=1;ids.add(b)
            rate=valid/nonblank if nonblank else 0
            annual_ids[year]=ids
            all_annual_ids.update(ids)
            syntax_year[year]={"rows":len(rows),"nonblank":nonblank,"valid":valid,"rate":rate}
            support_year[year]={"distinct_exact":len(ids)}
            annual[year]={
              "discovery":d,"identification_meta":mm,"headers":fields,
              "row_count":len(rows),"bn_field":bn_field,
              "distinct_exact":len(ids),"syntax_rate":rate
            }

        # Gate 3: annual landing pages + CRA semantic anchors reachable.
        annual_pages_ok=all(annual.get(y,{}).get("discovery",{}).get("page_meta",{}).get("status")==200 for y in range(2018,2025))
        docs_ok=all(docs.get(k,{}).get("status")==200 for k in ("revocations","search_tips","annulment","revocation_types"))
        ev["gates"].append({"gate":3,"pass":annual_pages_ok and docs_ok,
                            "observed":{"annual_pages_ok":annual_pages_ok,"cra_docs":{k:{kk:vv for kk,vv in v.items() if kk!="text"} for k,v in docs.items()}}})

        g4=annual_lineage_ok and all(annual.get(y,{}).get("row_count",0)>0 and annual.get(y,{}).get("identification_meta",{}).get("bytes",0)>0 for y in range(2018,2025))
        ev["gates"].append({"gate":4,"pass":g4,"observed":{"years":{str(y):{"url":annual.get(y,{}).get("discovery",{}).get("identification"),"rows":annual.get(y,{}).get("row_count"),"sha256":annual.get(y,{}).get("identification_meta",{}).get("sha256")} for y in range(2018,2025)}}})

        g5=schema_ok and all(annual.get(y,{}).get("bn_field") is not None for y in range(2018,2025))
        ev["gates"].append({"gate":5,"pass":g5,"observed":{"years":{str(y):{"bn_field":annual.get(y,{}).get("bn_field"),"headers":annual.get(y,{}).get("headers",[])[:20]} for y in range(2018,2025)}}})

        g6=all(syntax_year.get(y,{}).get("rate",0)>=0.999 for y in range(2018,2025))
        ev["gates"].append({"gate":6,"pass":g6,"observed":{"threshold":0.999,"years":syntax_year}})

        g7=all(support_year.get(y,{}).get("distinct_exact",0)>=50000 for y in range(2018,2025))
        ev["gates"].append({"gate":7,"pass":g7,"observed":{"threshold":50000,"years":support_year}})

        ids24=annual_ids.get(2024,set())
        recurring=0
        for b in ids24:
            hits=sum(1 for y in range(2018,2025) if b in annual_ids.get(y,set()))
            if hits>=5: recurring+=1
        continuity=recurring/len(ids24) if ids24 else 0
        ev["gates"].append({"gate":8,"pass":continuity>=0.70,
                            "observed":{"qualified_2024":len(ids24),"in_at_least_5_of_7":recurring,"rate":continuity,"threshold":0.70}})

        # 2024 structural support: identification category/designation + top non-tautological fields from general/financial.
        structural={"ident_category_rate":0,"ident_designation_rate":0,"general":{},"financial":{}}
        a24=annual.get(2024,{})
        # refetch identification for exact support counts
        if a24.get("discovery",{}).get("identification"):
            rr,_=fetch(a24["discovery"]["identification"],240); fields,rows=parse_csv_bytes(rr.content)
            cat=next((x for x in fields if x.strip().lower()=="category"),None)
            des=next((x for x in fields if x.strip().lower()=="designation"),None)
            denom=len(rows) or 1
            structural["ident_category_rate"]=sum(1 for r in rows if cat and str(r.get(cat) or "").strip())/denom
            structural["ident_designation_rate"]=sum(1 for r in rows if des and str(r.get(des) or "").strip())/denom

        concept_rates=[]
        for kind in ("general","financial"):
            u=a24.get("discovery",{}).get(kind)
            if not u: continue
            rr,mm=fetch(u,240); fields,rows=parse_csv_bytes(rr.content)
            # evaluate source-native non-identity columns; exclude direct IDs.
            denom=len(rows) or 1
            rates={}
            for col in fields:
                cu=col.strip().upper()
                if cu in {"BN","FORM ID"}: continue
                rate=sum(1 for r in rows if str(r.get(col) or "").strip() not in {"","NA","N/A"})/denom
                rates[col]=rate
                # FPE, Section Used, program structure and financial-line concepts are all non-outcome fields.
                if rate>=0.90: concept_rates.append((kind,col,rate))
            structural[kind]={"url":u,"sha256":mm["sha256"],"rows":len(rows),"headers":fields,"top_support":sorted(rates.items(),key=lambda x:x[1],reverse=True)[:12]}

        structural["qualified_concepts"]=sorted(concept_rates,key=lambda x:x[2],reverse=True)[:20]
        g9=(structural["ident_category_rate"]>=0.90 and structural["ident_designation_rate"]>=0.90 and len(concept_rates)>=3)
        ev["gates"].append({"gate":9,"pass":g9,"observed":structural})

        # Revocation/status source fingerprint and row extraction.
        rev_meta={k:v for k,v in docs["revocations"].items() if k!="text"}
        ev["revocation_source"]=rev_meta
        g10=docs.get("revocations",{}).get("status")==200 and docs.get("revocations",{}).get("sha256") is not None
        ev["gates"].append({"gate":10,"pass":g10,"observed":rev_meta})

        blob=" ".join(docs.get(k,{}).get("text","") for k in ("revocations","search_tips","annulment","revocation_types")).lower()
        g11=("registered" in blob and "revoked" in blob and "annul" in blob
             and "effective" in blob and "canada gazette" in blob and "publication" in blob)
        ev["gates"].append({"gate":11,"pass":g11,"observed":{
          "registered":("registered" in blob),"revoked":("revoked" in blob),"annulled":("annul" in blob),
          "effective":("effective" in blob),"canada_gazette":("canada gazette" in blob),"publication":("publication" in blob)}})

        rev_r,_=fetch(REVOCATIONS,120)
        soup=BeautifulSoup(rev_r.text,"html.parser")
        events=[]
        for tr in soup.find_all("tr"):
            cells=[" ".join(td.stripped_strings) for td in tr.find_all(["th","td"])]
            if len(cells)<4: continue
            m=BN_RE.search(cells[0].replace(" ","").upper())
            if not m: continue
            bn=m.group(0)
            typ=cells[2].strip()
            dt=parse_date(cells[3].strip())
            events.append({"bn":bn,"type":typ,"date":dt.isoformat() if dt else None})
        # dedupe exact event records
        uniq={(e["bn"],e["type"],e["date"]):e for e in events}
        events=list(uniq.values())
        nonblank=len(events)
        valid=sum(1 for e in events if norm_bn(e["bn"]))
        valid_rate=valid/nonblank if nonblank else 0
        exact_rev={e["bn"] for e in events if norm_bn(e["bn"])}
        ev["revocation_event_type_counts"]=dict(Counter(e["type"] for e in events))
        ev["gates"].append({"gate":12,"pass":valid_rate>=0.99,
                            "observed":{"rows":len(events),"exact_valid":valid,"rate":valid_rate,"threshold":0.99}})
        matched=len(exact_rev & all_annual_ids)
        join_rate=matched/len(exact_rev) if exact_rev else 0
        ev["gates"].append({"gate":13,"pass":join_rate>=0.95,
                            "observed":{"distinct_revoked_exact":len(exact_rev),"matched_2018_2024":matched,"rate":join_rate,"threshold":0.95}})
        ev["gates"].append({"gate":14,"pass":len(exact_rev)>=1000,
                            "observed":{"distinct_historical_revoked_exact":len(exact_rev),"threshold":1000}})
        dated=sum(1 for e in events if e["date"])
        date_rate=dated/len(events) if events else 0
        ev["gates"].append({"gate":15,"pass":date_rate>=0.95,
                            "observed":{"events":len(events),"parseable_dates":dated,"rate":date_rate,"threshold":0.95}})

        g16=("reinstat" in docs.get("revocations",{}).get("text","").lower()
             or "re-applied" in docs.get("revocations",{}).get("text","").lower())
        ev["gates"].append({"gate":16,"pass":g16,"observed":{
          "reinstatement_documented":("reinstat" in docs.get("revocations",{}).get("text","").lower()),
          "reapplication_documented":("re-applied" in docs.get("revocations",{}).get("text","").lower())}})

        g17=not any([ev["later_status_refresh_opened"],ev["future_revocation_membership_opened"],
                     ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],
                     ev["prohibited_compliance_exposure_computed"],ev["identity_repair_used"]])
        ev["gates"].append({"gate":17,"pass":g17,"observed":{
          "later_refresh_opened":False,"future_membership_opened":False,"relationship":False,
          "prediction":False,"ranking":False,"causal":False,"prohibited_exposure":False,"identity_repair":False}})

        fingerprints={str(y):annual.get(y,{}).get("identification_meta",{}).get("sha256") for y in range(2018,2025)}
        g18=(all(isinstance(x,str) and re.fullmatch(r"[0-9a-f]{64}",x) for x in fingerprints.values())
             and isinstance(rev_meta.get("sha256"),str) and re.fullmatch(r"[0-9a-f]{64}",rev_meta["sha256"])
             and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) and ev["incremental_monetary_cost_usd"]==0)
        ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{
          "annual_identification_sha256":fingerprints,"revocation_sha256":rev_meta.get("sha256"),
          "contract_sha":CONTRACT_SHA,"runner_sha256":ev["runner_sha256"],"cost_usd":0}})

        ev["annual"]=annual
        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True
        ev["pass_count"]=18-len(failed)
        ev["failed_gates"]=failed
        ev["disposition"]="PASS_CA_CRA_CHARITY_F01_EXACT_REGISTRATION_FUTURE_REVOCATION_DESIGN_READY" if not failed else "HOLD_CA_CRA_CHARITY_F01_EXACT_REGISTRATION_FUTURE_REVOCATION_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_CA_CRA_CHARITY_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# CA-CRA-CHARITY-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Later status refresh opened: **{ev['later_status_refresh_opened']}**",
           f"- Future revocation membership opened: **{ev['future_revocation_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):
        lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","Annual raw CSV bytes were transient. No later status refresh was opened and no prediction/relationship metric was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":
    main()
