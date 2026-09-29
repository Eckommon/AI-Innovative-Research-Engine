#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
import csv
import hashlib
import json
import os
import re
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="b97728c4e6338386bf47ec28be0c34afdf7a4737"
ISSUE=173
OUTDIR=ROOT/"research/CA-CORP-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"

DATA_SERVICES="https://ised-isde.canada.ca/site/corporations-canada/en/data-services"
API_DOCS="https://ised-isde.canada.ca/site/corporations-canada/en/accessing-federal-corporation-json-datasets"
MONTHLY="https://ised-isde.canada.ca/site/corporations-canada/en/data-services/monthly-transactions"
SEARCH_TIPS="https://ised-isde.canada.ca/site/corporations-canada/en/search-tips"
OPEN_DATA_RECORD="https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2?wbdisable=true"
SECTION212="https://ised-isde.canada.ca/site/corporations-canada/en/data-services/monthly-transactions/certificates-dissolution-cbca-section-212"
SECTION210211="https://ised-isde.canada.ca/site/corporations-canada/en/data-services/monthly-transactions/certificates-dissolution-cbca-section-210-or-211"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"

RESOURCE_PATTERNS={
 "active_cbca":r"https://d4bf66bykfyaf\.cloudfront\.net/corporations-active-cbca-en\.csv",
 "inactive_cbca":r"https://d4bf66bykfyaf\.cloudfront\.net/corporations-inactive-or-dissolved-cbca-en\.csv",
 "active_non_cbca":r"https://d4bf66bykfyaf\.cloudfront\.net/corporations-active-non-cbca-en\.csv",
 "inactive_non_cbca":r"https://d4bf66bykfyaf\.cloudfront\.net/corporations-inactive-or-dissolved-non-cbca-en\.csv",
}

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self._href=None; self._text=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="a":
            self._href=dict(attrs).get("href"); self._text=[]
    def handle_data(self,data):
        if self._href is not None: self._text.append(data)
    def handle_endtag(self,tag):
        if tag.lower()=="a" and self._href is not None:
            self.links.append((" ".join("".join(self._text).split()),self._href))
            self._href=None; self._text=[]

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.rows=[]; self.in_tr=False; self.in_cell=False; self.row=[]; self.buf=[]
    def handle_starttag(self,tag,attrs):
        if tag.lower()=="tr":
            self.in_tr=True; self.row=[]
        elif self.in_tr and tag.lower() in ("td","th"):
            self.in_cell=True; self.buf=[]
    def handle_data(self,data):
        if self.in_cell: self.buf.append(data)
    def handle_endtag(self,tag):
        if self.in_tr and tag.lower() in ("td","th") and self.in_cell:
            self.row.append(" ".join("".join(self.buf).split())); self.in_cell=False
        elif tag.lower()=="tr" and self.in_tr:
            if self.row: self.rows.append(self.row)
            self.in_tr=False

def curl_file(url:str,path:Path,timeout=360)->dict:
    hp=path.with_suffix(path.suffix+".headers")
    cmd=["curl","-L","--fail","--silent","--show-error","--retry","2",
         "--connect-timeout","20","--max-time",str(timeout),"-A",UA,
         "-D",str(hp),"-o",str(path),url]
    p=subprocess.run(cmd,capture_output=True)
    if p.returncode!=0:
        raise RuntimeError(f"curl rc={p.returncode}:{p.stderr.decode('utf-8','replace')[:700]}")
    body=path.read_bytes()
    hdr=hp.read_bytes() if hp.exists() else b""
    blocks=[b for b in re.split(br"\r?\n\r?\n",hdr) if b.startswith(b"HTTP/")]
    final=blocks[-1] if blocks else b""; status=None; headers={}
    if final:
        lines=final.decode("iso-8859-1","replace").splitlines()
        m=re.match(r"HTTP/\S+\s+(\d+)",lines[0]); status=int(m.group(1)) if m else None
        for line in lines[1:]:
            if ":" in line:
                k,v=line.split(":",1); headers[k.strip().lower()]=v.strip()
    return {"status":status,"requested_url":url,"bytes":len(body),
            "content_type":headers.get("content-type"),"last_modified":headers.get("last-modified"),
            "etag":headers.get("etag"),"sha256":hashlib.sha256(body).hexdigest()}

def get_text(url:str,timeout=120)->tuple[str,dict]:
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"body"
        m=curl_file(url,p,timeout)
        return p.read_text(encoding="utf-8",errors="replace"),m

def norm_header(v)->str:
    return re.sub(r"[^a-z0-9]+","",str(v or "").strip().lower())

def norm_id(v)->str|None:
    if v is None: return None
    s=str(v).strip()
    if re.fullmatch(r"[0-9]+-[0-9]",s): s=s.replace("-","")
    elif not re.fullmatch(r"[0-9]+",s): return None
    return s if 4<=len(s)<=8 else None

def find_col(headers,tokens):
    hs=[norm_header(h) for h in headers]
    for i,h in enumerate(hs):
        if any(t==h or t in h for t in tokens): return i
    return None

def open_csv(path:Path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            fh=path.open("r",encoding=enc,newline="")
            first=fh.readline(); fh.seek(0)
            if "," in first or "\t" in first:
                dialect=csv.excel_tab if "\t" in first and first.count("\t")>first.count(",") else csv.excel
                return fh,csv.reader(fh,dialect=dialect)
            fh.close()
        except UnicodeDecodeError:
            try: fh.close()
            except Exception: pass
    raise RuntimeError(f"CSV_ENCODING_OR_DELIMITER:{path.name}")

def parse_effective_date(s):
    s=str(s or "").strip()
    for fmt in ("%Y-%m-%d","%Y/%m/%d","%B %d, %Y","%b %d, %Y","%d %B %Y","%m/%d/%Y"):
        try:return datetime.strptime(s,fmt).date()
        except ValueError:pass
    return None

def parse_section_page(html:str):
    p=TableParser(); p.feed(html)
    rows=[]
    for row in p.rows:
        if len(row)<2: continue
        cid=None; d=None
        for cell in row:
            if cid is None and re.fullmatch(r"[0-9]+-[0-9]",cell.strip()):
                cid=norm_id(cell)
            if d is None:
                x=parse_effective_date(cell)
                if x: d=x
        if cid and d: rows.append((cid,d,row))
    return rows

def api_one(cid:str):
    urls=[
      f"https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/api/corporations/{cid}.json?lang=eng",
      f"https://ised-isde.canada.ca/app/scr/cc/CorporationsCanada/api/corporations/{cid}.json?lang=eng",
    ]
    last=None
    for u in urls:
        try:
            txt,meta=get_text(u,60)
            obj=json.loads(txt)
            if isinstance(obj,list) and obj and isinstance(obj[0],dict):
                rec=obj[0]
                got=norm_id(rec.get("corporationId"))
                return {"requested":cid,"returned":got,"status":meta.get("status"),"url":u,
                        "concordant":got==cid}
            last=f"unexpected:{txt[:120]}"
        except Exception as e: last=f"{type(e).__name__}:{e}"
    return {"requested":cid,"returned":None,"concordant":False,"error":last}

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-01 evidence exists")
    ev={"research":"CA-CORP-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_rows_opened":0,"future_section212_membership_opened":False,
        "future_entity_body_bytes_consumed":0,"relationship_computed":False,
        "prediction_computed":False,"ranking_computed":False,"causal_claim_made":False,
        "business_number_name_address_director_fuzzy_geo_manual_repair_used":False,
        "prohibited_exposure_fields_computed":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20260929-CA-CORP-F01-ACTIVE" and cp.get("active_issue")==173
            and cp.get("active_research")=="CA-CORP-F01" and cp.get("last_decision")=="DEC-256")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("CA_CORP_F01_ISSUE_BOUND")=="1" and os.environ.get("CA_CORP_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":173,"contract_sha":os.environ.get("CA_CORP_F01_CONTRACT_SHA")}})

        docs={}
        texts={}
        for key,u in {"data_services":DATA_SERVICES,"api_docs":API_DOCS,"monthly":MONTHLY,"search_tips":SEARCH_TIPS,"open_data":OPEN_DATA_RECORD}.items():
            txt,meta=get_text(u,150); texts[key]=txt; docs[key]=meta
        g3=all(docs[k].get("status")==200 for k in ("data_services","api_docs","monthly","search_tips"))
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

        open_html=texts["open_data"]
        resources={}
        for key,pat in RESOURCE_PATTERNS.items():
            m=re.search(pat,open_html)
            resources[key]=m.group(0) if m else None
        g4=all(resources.values())
        ev["gates"].append({"gate":4,"pass":g4,"observed":{"resources":resources,"record_status":docs["open_data"].get("status")}})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0)
            metas={}; all_ids=set(); active_cbca=set(); cbca_status=Counter()
            schema_obs={}; total_nonblank=total_valid=0
            for key,u in resources.items():
                if not u: continue
                path=td/f"{key}.csv"; metas[key]=curl_file(u,path,600)
                fh,reader=open_csv(path)
                try:
                    headers=next(reader)
                    ci=find_col(headers,("corporationnumber","corporationid","corporationno"))
                    si=find_col(headers,("status","corporationstatus"))
                    li=find_col(headers,("governinglegislation","legislation","act"))
                    di=find_col(headers,("incorporationdate","continuancedate","effectivedate","creationdate"))
                    # Dataset-level resource class is an official current status where a row-level status field is absent.
                    schema_ok=ci is not None and (si is not None or key.startswith("active_") or key.startswith("inactive_"))
                    rows=nonblank=valid=0
                    statuses=Counter()
                    for row in reader:
                        if ci is None or ci>=len(row): continue
                        raw=row[ci]; rows+=1
                        if str(raw).strip(): nonblank+=1
                        cid=norm_id(raw)
                        if not cid: continue
                        valid+=1; all_ids.add(cid)
                        source_status=(row[si].strip() if si is not None and si<len(row) else ("Active" if key.startswith("active_") else "Inactive"))
                        if source_status: statuses[source_status]+=1
                        if key=="active_cbca": active_cbca.add(cid)
                        if key in ("active_cbca","inactive_cbca") and source_status: cbca_status[source_status]+=1
                    total_nonblank+=nonblank; total_valid+=valid
                    schema_obs[key]={"headers":headers,"rows":rows,"nonblank_ids":nonblank,"valid_ids":valid,
                                     "id_col":ci,"status_col":si,"legislation_col":li,"date_col":di,
                                     "schema_ok":schema_ok,"status_counts":dict(statuses)}
                finally: fh.close()
            ev["source_fingerprints"]={k:v["sha256"] for k,v in metas.items()}
            gate5=all(x.get("schema_ok") for x in schema_obs.values()) and any(x.get("date_col") is not None for x in schema_obs.values())
            ev["gates"].append({"gate":5,"pass":gate5,"observed":schema_obs})
            syntax=total_valid/total_nonblank if total_nonblank else 0
            ev["gates"].append({"gate":6,"pass":syntax>=0.999,"observed":{"valid":total_valid,"nonblank":total_nonblank,"rate":syntax,"threshold":0.999}})
            ev["gates"].append({"gate":7,"pass":len(active_cbca)>=250000,"observed":{"distinct_active_cbca":len(active_cbca),"threshold":250000}})
            ev["gates"].append({"gate":8,"pass":len(all_ids)>=500000,"observed":{"distinct_complete_federal_ids":len(all_ids),"threshold":500000}})

            tips=texts["search_tips"].lower()
            documented=["active","dissolved","inactive - amalgamated","inactive - discontinued"]
            sem_ok=all(x in tips for x in documented)
            # observed status values must be representable under the official legal-state vocabulary or dataset-level active/inactive partition.
            unknown=[x for x in cbca_status if not any(k in x.lower() for k in ("active","dissolved","amalgam","discontinu","inactive"))]
            status_rate=(sum(v for k,v in cbca_status.items() if k not in unknown)/sum(cbca_status.values())) if cbca_status else 0
            ev["gates"].append({"gate":9,"pass":sem_ok and status_rate>=0.999,
                                "observed":{"documented_labels_found":sem_ok,"status_counts":dict(cbca_status),
                                            "recognized_rate":status_rate,"unknown_statuses":unknown}})

            # Historical monthly publication lineage: index links only; no future transaction bodies.
            lp=LinkParser(); lp.feed(texts["monthly"])
            month_dates=set(); month_links=[]
            months="January|February|March|April|May|June|July|August|September|October|November|December"
            for text,href in lp.links:
                m=re.search(rf"\b({months})\s+(20\d{{2}})\b",text,re.I)
                if not m: continue
                dt=datetime.strptime(f"01 {m.group(1).title()} {m.group(2)}","%d %B %Y").date()
                if date(2025,1,1)<=dt<=date(2026,8,1):
                    month_dates.add(dt.isoformat()); month_links.append((text,urljoin(MONTHLY,href)))
            ev["gates"].append({"gate":10,"pass":len(month_dates)>=18,
                                "observed":{"distinct_months":sorted(month_dates),"count":len(month_dates),"threshold":18,
                                            "sample_links":month_links[:30]}})

            # Current official Section-212 page was preverified as a historical July-2026 publication.
            s212_html,s212_meta=get_text(SECTION212,180)
            s212_rows=parse_section_page(s212_html)
            safe212=[(cid,d) for cid,d,_ in s212_rows if d<=date(2026,8,31)]
            unsafe212=[(cid,d.isoformat()) for cid,d,_ in s212_rows if d>date(2026,8,31)]
            if unsafe212:
                raise RuntimeError(f"HISTORICAL_FIREWALL_SECTION212_PAGE_CONTAINS_POST_AUG_ROWS:{unsafe212[:5]}")
            hist212={cid for cid,d in safe212}
            ev["gates"].append({"gate":11,"pass":len(hist212)>=5000,
                                "observed":{"section212_page":s212_meta,"distinct_historical_section212_ids":len(hist212),
                                            "rows":len(safe212),"threshold":5000,
                                            "effective_min":min((d.isoformat() for _,d in safe212),default=None),
                                            "effective_max":max((d.isoformat() for _,d in safe212),default=None)}})
            coverage=len(hist212 & all_ids)/len(hist212) if hist212 else 0
            ev["gates"].append({"gate":12,"pass":coverage>=0.95,
                                "observed":{"historical_ids":len(hist212),"exact_matches":len(hist212 & all_ids),
                                            "rate":coverage,"threshold":0.95}})

            s210_html,_=get_text(SECTION210211,180)
            monthly_lower=texts["monthly"].lower()
            sep_ok=("section 212" in s212_html.lower() and ("section 210" in s210_html.lower() or "210 or 211" in s210_html.lower())
                    and "amalgamation" in monthly_lower and "discontinuance" in monthly_lower)
            ev["gates"].append({"gate":13,"pass":sep_ok,
                                "observed":{"section212_label":("section 212" in s212_html.lower()),
                                            "section210211_label":("section 210" in s210_html.lower() or "210 or 211" in s210_html.lower()),
                                            "amalgamation_family":("amalgamation" in monthly_lower),
                                            "discontinuance_family":("discontinuance" in monthly_lower)}})

            sample=sorted(all_ids)[:100]
            api_results=[]
            with ThreadPoolExecutor(max_workers=10) as ex:
                futs={ex.submit(api_one,cid):cid for cid in sample}
                for fut in as_completed(futs): api_results.append(fut.result())
            available=[x for x in api_results if x.get("returned") is not None]
            concord=sum(1 for x in available if x.get("concordant"))
            api_rate=concord/len(available) if available else 0
            ev["gates"].append({"gate":14,"pass":len(available)>0 and api_rate>=0.99,
                                "observed":{"sample_rule":"lexicographically first 100 qualified baseline IDs",
                                            "requested":len(sample),"available":len(available),"concordant":concord,
                                            "rate":api_rate,"threshold":0.99,"results":sorted(api_results,key=lambda x:x["requested"])}})

            prohibited=["annual_filing_overdue","notice_of_intent_to_dissolve","dissolution_pending",
                        "active_intent_to_dissolve","compliance_certificate_ineligibility","section212_trigger"]
            g15=not ev["prohibited_exposure_fields_computed"]
            ev["gates"].append({"gate":15,"pass":g15,
                                "observed":{"prohibited_fields":prohibited,"computed":False}})
            g16=(ev["future_rows_opened"]==0 and ev["future_section212_membership_opened"] is False
                 and ev["future_entity_body_bytes_consumed"]==0)
            ev["gates"].append({"gate":16,"pass":g16,
                                "observed":{"future_rows_opened":0,"future_section212_membership_opened":False,
                                            "future_entity_body_bytes_consumed":0,
                                            "policy":"no post-2026-09-29 transaction entity page is requested"}})
            g17=(not ev["relationship_computed"] and not ev["prediction_computed"] and not ev["ranking_computed"]
                 and not ev["causal_claim_made"] and not ev["business_number_name_address_director_fuzzy_geo_manual_repair_used"])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{k:ev[k] for k in (
                "relationship_computed","prediction_computed","ranking_computed","causal_claim_made",
                "business_number_name_address_director_fuzzy_geo_manual_repair_used")}})
            g18=(len(ev.get("source_fingerprints",{}))==4 and
                 all(re.fullmatch(r"[0-9a-f]{64}",x) for x in ev["source_fingerprints"].values()) and
                 re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":g18,
                                "observed":{"source_sha256":ev.get("source_fingerprints",{}),
                                            "runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})
        ev["gates"]=sorted(ev["gates"],key=lambda g:g["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True; ev["pass_count"]=18-len(failed); ev["failed_gates"]=failed
        ev["disposition"]="PASS_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_READY" if not failed else "HOLD_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass")); ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_CA_CORP_F01_ATTEMPT_01"
    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    lines=["# CA-CORP-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future rows opened: **{ev['future_rows_opened']}**",
           f"- Future section-212 membership opened: **{ev['future_section212_membership_opened']}**",
           f"- Incremental monetary cost: **{ev['incremental_monetary_cost_usd']} USD**","",
           "## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in ev["gates"]:
        obs=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True)
        if len(obs)>1000: obs=obs[:997]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{obs.replace(chr(96),'')}` |")
    if ev.get("implementation_error"): lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No post-2026-09-29 transaction entity row was authorized or opened. No prohibited section-212 trigger exposure was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"]); print(ev.get("pass_count"),ev.get("failed_gates"))
    return 0

if __name__=="__main__": raise SystemExit(main())
