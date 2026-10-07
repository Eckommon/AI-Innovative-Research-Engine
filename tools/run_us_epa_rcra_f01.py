#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
import csv, hashlib, io, json, os, re, tempfile, zipfile
import requests

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-EPA-RCRA-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"
CONTRACT_SHA="ffbb1d89ea614c4c82cc39483383ccb09e23accf"
ISSUE=198

DOWNLOAD_PAGE="https://echo.epa.gov/tools/data-downloads"
DICT_PAGE="https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary"
ZIP_URL="https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
S=requests.Session(); S.headers.update({"User-Agent":UA})
csv.field_size_limit(1024*1024*64)

REQUIRED={
 "RCRA_FACILITIES.CSV","RCRA_ENFORCEMENTS.CSV","RCRA_EVALUATIONS.CSV",
 "RCRA_VIOLATIONS.CSV","RCRA_NAICS.CSV","RCRA_VIOSNC_HISTORY.CSV"
}
FAC_REQUIRED={"ID_NUMBER","ACTIVITY_LOCATION","FED_WASTE_GENERATOR","TRANSPORTER","ACTIVE_SITE","OPERATING_TSDF"}
EVAL_ID_ALIASES=("EVALUATION_IDENTIFIER","EVALUATION_IDENTIFER")
FOUND_ALIASES=("FOUND_VIOLATION","FOUND_VOLATION")
EVAL_CORE={"ID_NUMBER","ACTIVITY_LOCATION","EVALUATION_TYPE","EVALUATION_START_DATE"}

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def norm(v): return str(v or "").strip().upper()
def id_ok(v):
    s=norm(v)
    return 4<=len(s)<=12 and bool(re.fullmatch(r"[A-Z]{2}[A-Z0-9]{2,10}",s))
def loc_ok(v): return bool(re.fullmatch(r"[A-Z]{2}",norm(v)))
def ym_ok(v):
    s=norm(v)
    if not re.fullmatch(r"20[0-9]{2}(0[1-9]|1[0-2])",s): return False
    return True
def date_ok(v):
    s=str(v or "").strip()
    if not s:return False
    for fmt in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y","%d-%b-%Y","%Y%m%d"):
        try: datetime.strptime(s,fmt); return True
        except ValueError: pass
    return False

def fetch_meta(url,timeout=120):
    r=S.get(url,timeout=timeout,allow_redirects=True)
    r.raise_for_status()
    return r,{"status":r.status_code,"requested_url":url,"final_url":r.url,
              "content_type":r.headers.get("content-type"),"bytes":len(r.content),
              "sha256":sha_bytes(r.content),"last_modified":r.headers.get("last-modified"),
              "etag":r.headers.get("etag")}

def download(path):
    h=hashlib.sha256(); total=0
    with S.get(ZIP_URL,timeout=(30,600),allow_redirects=True,stream=True) as r:
        r.raise_for_status()
        meta={"status":r.status_code,"requested_url":ZIP_URL,"final_url":r.url,
              "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
              "etag":r.headers.get("etag"),"content_length_header":r.headers.get("content-length")}
        with path.open("wb") as f:
            for chunk in r.iter_content(1024*1024):
                if not chunk: continue
                f.write(chunk);h.update(chunk);total+=len(chunk)
    meta["bytes"]=total;meta["sha256"]=h.hexdigest()
    return meta

def member_map(z):
    return {Path(n).name.upper():n for n in z.namelist() if not n.endswith("/")}

def reader(z,member):
    raw=z.open(member)
    txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    rr=csv.DictReader(txt)
    if not rr.fieldnames: raise RuntimeError(f"NO_HEADER:{member}")
    fields=[str(x or "").strip().upper() for x in rr.fieldnames]
    def gen():
        try:
            for row in rr:
                yield {str(k or "").strip().upper():v for k,v in row.items()}
        finally: txt.close()
    return fields,gen()

def choose(fields,aliases):
    fs=set(fields)
    return next((a for a in aliases if a in fs),None)

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-01 evidence exists")
    ev={"research":"US-EPA-RCRA-F01","attempt":1,"issue":ISSUE,"contract_sha":CONTRACT_SHA,
        "github_run_id":os.getenv("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "later_refresh_opened":False,"future_evaluation_violation_membership_opened":False,
        "future_rows_consumed":0,"relationship_computed":False,"prediction_computed":False,
        "ranking_computed":False,"causal_claim_made":False,
        "prohibited_compliance_exposure_computed":False,"identity_repair_used":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261008-US-EPA-RCRA-F01-ACTIVE"
            and cp.get("active_issue")==198 and cp.get("active_research")=="US-EPA-RCRA-F01"
            and cp.get("last_decision")=="DEC-308")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.getenv("RCRA_F01_BOUND")=="1" and os.getenv("RCRA_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":198,"contract_sha":os.getenv("RCRA_F01_CONTRACT_SHA")}})

        docs={}
        for k,u in {"downloads":DOWNLOAD_PAGE,"dictionary":DICT_PAGE}.items():
            try:
                _,docs[k]=fetch_meta(u,90)
            except Exception as e:
                docs[k]={"error":f"{type(e).__name__}:{e}","requested_url":u}
        g3=all(docs.get(k,{}).get("status")==200 for k in ("downloads","dictionary"))
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

        with tempfile.TemporaryDirectory() as td0:
            zp=Path(td0)/"rcra_downloads.zip"
            zmeta=download(zp);ev["baseline_zip"]=zmeta
            zip_valid=False
            try:
                with zipfile.ZipFile(zp) as z: zip_valid=(z.testzip() is None)
            except Exception: zip_valid=False
            g4=(zip_valid and zmeta["bytes"]>=50*1024*1024 and zmeta["final_url"].startswith("https://echo.epa.gov/"))
            ev["gates"].append({"gate":4,"pass":g4,"observed":{"zip_valid":zip_valid,**zmeta}})
            if not zip_valid: raise RuntimeError("BASELINE_ZIP_NOT_PARSEABLE")

            with zipfile.ZipFile(zp) as z:
                mm=member_map(z)
                ev["zip_members"]=sorted(z.namelist())
                present=REQUIRED & set(mm)
                g5=present==REQUIRED
                ev["gates"].append({"gate":5,"pass":g5,"observed":{"required":sorted(REQUIRED),"present":sorted(present)}})
                if not g5:
                    missing=sorted(REQUIRED-present)
                    raise RuntimeError("REQUIRED_TABLES_MISSING:"+",".join(missing))

                # Facility baseline.
                ff,fr=reader(z,mm["RCRA_FACILITIES.CSV"])
                ev["facility_schema"]=ff
                g6=FAC_REQUIRED.issubset(set(ff))
                ev["gates"].append({"gate":6,"pass":g6,"observed":{"headers":ff,"missing":sorted(FAC_REQUIRED-set(ff))}})

                facility_rows=0;id_nonblank=0;id_valid=0;loc_nonblank=0;loc_valid=0
                facility_keys=set();structural_keys=set()
                for r in fr:
                    facility_rows+=1
                    iid=norm(r.get("ID_NUMBER"));loc=norm(r.get("ACTIVITY_LOCATION"))
                    if iid:
                        id_nonblank+=1
                        if id_ok(iid): id_valid+=1
                    if loc:
                        loc_nonblank+=1
                        if loc_ok(loc): loc_valid+=1
                    if id_ok(iid) and loc_ok(loc):
                        key=(iid,loc);facility_keys.add(key)
                        if any(str(r.get(k) or "").strip() for k in ("ACTIVE_SITE","FED_WASTE_GENERATOR","OPERATING_TSDF","TRANSPORTER")):
                            structural_keys.add(key)
                idrate=id_valid/id_nonblank if id_nonblank else 0
                locrate=loc_valid/loc_nonblank if loc_nonblank else 0
                ev["gates"].append({"gate":7,"pass":idrate>=0.99 and locrate>=0.99,
                    "observed":{"facility_rows":facility_rows,"id_nonblank":id_nonblank,"id_valid":id_valid,"id_rate":idrate,
                                "loc_nonblank":loc_nonblank,"loc_valid":loc_valid,"loc_rate":locrate}})
                ev["gates"].append({"gate":8,"pass":len(facility_keys)>=500000,
                    "observed":{"distinct_exact_handler_keys":len(facility_keys),"threshold":500000}})
                ev["gates"].append({"gate":9,"pass":len(structural_keys)>=100000,
                    "observed":{"distinct_structurally_usable_handler_keys":len(structural_keys),"threshold":100000}})

                # Monthly compliance history; used only for structural lineage/support, never exposure.
                hf,hr=reader(z,mm["RCRA_VIOSNC_HISTORY.CSV"])
                ev["history_schema"]=hf
                months=set();hist_keys=set();history_rows=0
                for r in hr:
                    history_rows+=1
                    ym=norm(r.get("YRMONTH"))
                    if ym_ok(ym):months.add(ym)
                    iid=norm(r.get("ID_NUMBER"));loc=norm(r.get("ACTIVITY_LOCATION"))
                    if id_ok(iid) and loc_ok(loc): hist_keys.add((iid,loc))
                ev["gates"].append({"gate":10,"pass":len(months)>=36,
                    "observed":{"history_rows":history_rows,"distinct_valid_yrmonth":len(months),
                                "min_yrmonth":min(months) if months else None,"max_yrmonth":max(months) if months else None,
                                "threshold":36}})
                hm=len(hist_keys & facility_keys);hrate=hm/len(hist_keys) if hist_keys else 0
                ev["gates"].append({"gate":11,"pass":hrate>=0.99,
                    "observed":{"distinct_history_keys":len(hist_keys),"matched_facility_keys":hm,"rate":hrate,"threshold":0.99}})

                # Evaluations.
                ef,er=reader(z,mm["RCRA_EVALUATIONS.CSV"])
                ev["evaluation_schema"]=ef
                eid_field=choose(ef,EVAL_ID_ALIASES)
                found_field=choose(ef,FOUND_ALIASES)
                g12=(EVAL_CORE.issubset(set(ef)) and eid_field is not None and found_field is not None)
                ev["resolved_evaluation_headers"]={"evaluation_identifier":eid_field,"found_violation":found_field}
                ev["gates"].append({"gate":12,"pass":g12,
                    "observed":{"headers":ef,"evaluation_identifier_header":eid_field,"found_violation_header":found_field,
                                "missing_core":sorted(EVAL_CORE-set(ef))}})
                if not g12: raise RuntimeError("EVALUATION_SCHEMA_NOT_RESOLVED")

                eval_rows=0;eval_keys=set();eval_handler_keys=set();found_nonblank=0;found_recognized=0
                positive_keys=set();date_good=set()
                for r in er:
                    eval_rows+=1
                    iid=norm(r.get("ID_NUMBER"));loc=norm(r.get("ACTIVITY_LOCATION"))
                    eidentifier=norm(r.get(eid_field));etype=norm(r.get("EVALUATION_TYPE"))
                    d=str(r.get("EVALUATION_START_DATE") or "").strip()
                    if id_ok(iid) and loc_ok(loc):
                        hk=(iid,loc);eval_handler_keys.add(hk)
                        opp=(iid,loc,eidentifier,etype,d)
                        eval_keys.add(opp)
                        if date_ok(d): date_good.add(opp)
                        fv=norm(r.get(found_field))
                        if fv:
                            found_nonblank+=1
                            if fv in {"Y","N","U"}:found_recognized+=1
                        if fv=="Y": positive_keys.add(opp)
                ev["gates"].append({"gate":13,"pass":len(eval_keys)>=100000,
                    "observed":{"evaluation_rows":eval_rows,"distinct_evaluation_opportunities":len(eval_keys),"threshold":100000}})
                semrate=found_recognized/found_nonblank if found_nonblank else 0
                ev["gates"].append({"gate":14,"pass":semrate>=0.99 and len(positive_keys)>=20000,
                    "observed":{"found_nonblank":found_nonblank,"recognized_YNU":found_recognized,"semantic_rate":semrate,
                                "distinct_positive_Y_opportunities":len(positive_keys),"positive_threshold":20000}})
                drate=len(date_good)/len(eval_keys) if eval_keys else 0
                ev["gates"].append({"gate":15,"pass":drate>=0.99,
                    "observed":{"distinct_evaluation_opportunities":len(eval_keys),"parseable_date_opportunities":len(date_good),
                                "rate":drate,"threshold":0.99}})
                em=len(eval_handler_keys & facility_keys);erate=em/len(eval_handler_keys) if eval_handler_keys else 0
                ev["gates"].append({"gate":16,"pass":erate>=0.99,
                    "observed":{"distinct_evaluation_handler_keys":len(eval_handler_keys),"matched_facility_keys":em,
                                "rate":erate,"threshold":0.99}})

                g17=not any([ev["later_refresh_opened"],ev["future_evaluation_violation_membership_opened"],
                    ev["future_rows_consumed"],ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],
                    ev["causal_claim_made"],ev["prohibited_compliance_exposure_computed"],ev["identity_repair_used"]])
                ev["gates"].append({"gate":17,"pass":g17,"observed":{
                    "later_refresh_opened":False,"future_membership_opened":False,"future_rows":0,"relationship":False,
                    "prediction":False,"ranking":False,"causal":False,"prohibited_exposure":False,"identity_repair":False}})
                g18=(len(zmeta["sha256"])==64 and len(ev["runner_sha256"])==64 and ev["incremental_monetary_cost_usd"]==0)
                ev["gates"].append({"gate":18,"pass":g18,"observed":{"baseline_sha256":zmeta["sha256"],
                    "runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True;ev["failed_gates"]=failed;ev["pass_count"]=18-len(failed)
        ev["disposition"]="PASS_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_READY" if not failed else "HOLD_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_NOT_READY"
    except RuntimeError as e:
        if str(e).startswith("REQUIRED_TABLES_MISSING"):
            seen={g["gate"] for g in ev["gates"]}
            for n in range(6,19):
                if n not in seen:ev["gates"].append({"gate":n,"pass":False,"observed":{"not_evaluated_after_decisive_inventory_failure":True}})
            ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
            failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
            ev["attempt_valid"]=True;ev["failed_gates"]=failed;ev["pass_count"]=18-len(failed)
            ev["disposition"]="HOLD_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_NOT_READY"
        else:
            ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
            ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
            ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_RCRA_F01_ATTEMPT_01"
    except Exception as e:
        ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_RCRA_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-EPA-RCRA-F01 — Attempt 01","",f"**Disposition:** §{ev['disposition']}§","",
           f"- Attempt valid: §{ev.get('attempt_valid')}§",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: §{ev.get('failed_gates',[])}§",f"- Later refresh opened: **{ev['later_refresh_opened']}**",
           f"- Future evaluation violation membership opened: **{ev['future_evaluation_violation_membership_opened']}**",
           "- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | §{o}§ |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"§{ev['implementation_error']}§"]
    lines+=["","The raw EPA ZIP was transient only. No later weekly refresh was opened and no predictive/outcome relation was computed.",""]
    MD_OUT.write_text("\n".join(lines).replace("§","§"),encoding="utf-8")
    # replace placeholder after construction
    MD_OUT.write_text(MD_OUT.read_text(encoding="utf-8").replace("§",chr(96)),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__": main()
