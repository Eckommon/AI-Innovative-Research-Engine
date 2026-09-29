#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import csv, hashlib, io, json, os, re, tempfile, zipfile

import requests

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="5546edebea1c09f68eb98075b286b3f20bd69b46"
ISSUE=182
OUTDIR=ROOT/"research/US-EPA-SDWIS-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"

DOWNLOAD_PAGE="https://echo.epa.gov/tools/data-downloads"
DICT_PAGE="https://echo.epa.gov/tools/data-downloads/sdwa-download-summary"
FAQ_PAGE="https://echo.epa.gov/help/sdwa-faqs"
ZIP_URL="https://echo.epa.gov/files/echodownloads/SDWA_latest_downloads.zip"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
PWS_RE=re.compile(r"^[A-Z0-9]{2}[0-9]{7}$")
csv.field_size_limit(1024*1024*64)

REQUIRED_MEMBERS={
    "SDWA_PUB_WATER_SYSTEMS.CSV",
    "SDWA_FACILITIES.CSV",
    "SDWA_VIOLATIONS_ENFORCEMENT.CSV",
    "SDWA_REF_CODE_VALUES.CSV",
}
PWS_REQUIRED={
    "SUBMISSIONYEARQUARTER","PWSID","PWS_ACTIVITY_CODE","PWS_TYPE_CODE",
    "PRIMARY_SOURCE_CODE","OWNER_TYPE_CODE","POPULATION_SERVED_COUNT","PWS_DEACTIVATION_DATE"
}
VIOL_REQUIRED={
    "SUBMISSIONYEARQUARTER","PWSID","VIOLATION_ID","NON_COMPL_PER_BEGIN_DATE",
    "VIOLATION_CATEGORY_CODE","IS_HEALTH_BASED_IND","VIOLATION_STATUS","RULE_CODE",
    "ENFORCEMENT_ID","ENFORCEMENT_DATE","ENF_ACTION_CATEGORY"
}

def sha_file(path:Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def get_meta(url:str, body=True, timeout=120):
    r=requests.get(url,headers={"User-Agent":UA},timeout=timeout,allow_redirects=True,stream=not body)
    r.raise_for_status()
    if body:
        data=r.content
        return {"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),
                "last_modified":r.headers.get("last-modified"),"etag":r.headers.get("etag"),
                "bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
    return {"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),
            "last_modified":r.headers.get("last-modified"),"etag":r.headers.get("etag")}

def download_zip(path:Path):
    h=hashlib.sha256(); total=0
    with requests.get(ZIP_URL,headers={"User-Agent":UA},timeout=(30,600),allow_redirects=True,stream=True) as r:
        r.raise_for_status()
        meta={"status":r.status_code,"requested_url":ZIP_URL,"final_url":r.url,
              "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
              "etag":r.headers.get("etag"),"content_length_header":r.headers.get("content-length")}
        with path.open("wb") as f:
            for chunk in r.iter_content(1024*1024):
                if not chunk: continue
                f.write(chunk); h.update(chunk); total+=len(chunk)
    meta["bytes"]=total; meta["sha256"]=h.hexdigest()
    return meta

def qkey(s):
    s=str(s or "").strip().upper().replace(" ","")
    m=re.search(r"(20[0-9]{2})[^0-9]*Q(?:TR)?[^0-9]*([1-4])",s)
    if not m:
        m=re.fullmatch(r"(20[0-9]{2})([1-4])",s)
    return (int(m.group(1)),int(m.group(2))) if m else None

def date_ok(s):
    s=str(s or "").strip()
    if not s: return False
    for fmt in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y"):
        try: datetime.strptime(s,fmt); return True
        except ValueError: pass
    return False

def member_map(zf):
    return {Path(n).name.upper():n for n in zf.namelist() if not n.endswith("/")}

def open_dict_reader(zf, member):
    raw=zf.open(member)
    txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    reader=csv.DictReader(txt)
    if reader.fieldnames is None:
        raise RuntimeError(f"NO_HEADER:{member}")
    # Preserve source names in evidence, but normalize keys to uppercase/strip in row stream.
    fields=[str(x or "").strip().upper() for x in reader.fieldnames]
    def rows():
        try:
            for r in reader:
                yield {str(k or "").strip().upper():v for k,v in r.items()}
        finally:
            txt.close()
    return fields,rows()

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable attempt-01 evidence already exists")
    ev={
        "research":"US-EPA-SDWIS-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "later_refresh_opened":False,"future_health_based_violation_membership_opened":False,
        "future_entity_rows_consumed":0,"relationship_computed":False,"prediction_computed":False,
        "ranking_computed":False,"causal_claim_made":False,
        "prohibited_compliance_enforcement_exposure_computed":False,
        "identity_repair_used":False,"gates":[]
    }
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20260930-US-EPA-SDWIS-F01-ACTIVE"
            and cp.get("active_issue")==182 and cp.get("active_research")=="US-EPA-SDWIS-F01"
            and cp.get("last_decision")=="DEC-274")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("SDWIS_F01_BOUND")=="1" and os.environ.get("SDWIS_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":182,"contract_sha":os.environ.get("SDWIS_F01_CONTRACT_SHA")}})

        docs={}
        for k,u in {"downloads":DOWNLOAD_PAGE,"dictionary":DICT_PAGE,"faq":FAQ_PAGE}.items():
            try: docs[k]=get_meta(u,body=True,timeout=90)
            except Exception as e: docs[k]={"error":f"{type(e).__name__}:{e}","url":u}
        g3=all(docs.get(k,{}).get("status")==200 for k in ("downloads","dictionary","faq"))
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0); zp=td/"SDWA_latest_downloads.zip"
            zmeta=download_zip(zp); ev["baseline_zip"]=zmeta
            zip_ok=False
            try:
                with zipfile.ZipFile(zp) as zf:
                    bad=zf.testzip()
                    zip_ok=(bad is None)
            except Exception:
                zip_ok=False
            g4=(zip_ok and zmeta["bytes"]>=100*1024*1024 and zmeta["final_url"].lower().startswith("https://echo.epa.gov/"))
            ev["gates"].append({"gate":4,"pass":g4,"observed":{"zip_valid":zip_ok,**zmeta}})

            if not zip_ok:
                raise RuntimeError("BASELINE_ZIP_NOT_PARSEABLE")

            with zipfile.ZipFile(zp) as zf:
                mm=member_map(zf)
                ev["zip_members"]=sorted(zf.namelist())
                present={x for x in REQUIRED_MEMBERS if x in mm}
                g5=(present==REQUIRED_MEMBERS)
                ev["gates"].append({"gate":5,"pass":g5,"observed":{"required":sorted(REQUIRED_MEMBERS),"present":sorted(present)}})
                if not g5:
                    # still valid empirical if official ZIP lacks frozen files
                    raise RuntimeError("REQUIRED_TABLES_MISSING")

                # Public-water-system table full pass.
                pfields,prows=open_dict_reader(zf,mm["SDWA_PUB_WATER_SYSTEMS.CSV"])
                pset=set(pfields)
                g6=PWS_REQUIRED.issubset(pset)
                ev["gates"].append({"gate":6,"pass":g6,"observed":{"headers":pfields,"missing":sorted(PWS_REQUIRED-pset)}})

                pws_rows=0; pws_nonblank=0; pws_valid=0; duplicate_keys=0
                keys=set(); all_pws=set(); quarters=set()
                active_ids_by_q=defaultdict(set)
                active_struct_total=Counter(); active_struct_complete=Counter()
                for r in prows:
                    pws_rows+=1
                    qraw=str(r.get("SUBMISSIONYEARQUARTER") or "").strip()
                    q=qkey(qraw)
                    if q: quarters.add(q)
                    raw=str(r.get("PWSID") or "").strip().upper()
                    if raw: pws_nonblank+=1
                    good=bool(PWS_RE.fullmatch(raw))
                    if good:
                        pws_valid+=1; all_pws.add(raw)
                        if q:
                            k=(q,raw)
                            if k in keys: duplicate_keys+=1
                            else: keys.add(k)
                        if q and str(r.get("PWS_ACTIVITY_CODE") or "").strip()=="A":
                            active_ids_by_q[q].add(raw)
                            active_struct_total[q]+=1
                            vals=[r.get("PWS_TYPE_CODE"),r.get("PRIMARY_SOURCE_CODE"),r.get("POPULATION_SERVED_COUNT")]
                            if all(str(v or "").strip() for v in vals):
                                active_struct_complete[q]+=1

                syntax=pws_valid/pws_nonblank if pws_nonblank else 0
                ev["gates"].append({"gate":7,"pass":syntax>=0.9999,"observed":{"rows":pws_rows,"nonblank":pws_nonblank,"valid":pws_valid,"rate":syntax,"threshold":0.9999}})
                unique_rate=(pws_rows-duplicate_keys)/pws_rows if pws_rows else 0
                ev["gates"].append({"gate":8,"pass":unique_rate>=0.9999,"observed":{"rows":pws_rows,"duplicate_quarter_pwsid_keys":duplicate_keys,"rate":unique_rate,"threshold":0.9999}})

                qsorted=sorted(quarters)
                qlabels=[f"{y}Q{q}" for y,q in qsorted]
                maxq=qsorted[-1] if qsorted else None
                maxq_label=f"{maxq[0]}Q{maxq[1]}" if maxq else None
                ev["baseline_max_submission_quarter"]=maxq_label
                g9=len(qsorted)>=8 and maxq is not None
                ev["gates"].append({"gate":9,"pass":g9,"observed":{"distinct_quarters":len(qsorted),"quarters":qlabels,"max_quarter":maxq_label,"threshold":8}})

                latest_active=len(active_ids_by_q.get(maxq,set())) if maxq else 0
                ev["gates"].append({"gate":10,"pass":latest_active>=140000,"observed":{"max_quarter":maxq_label,"distinct_active_pwsids":latest_active,"threshold":140000}})
                st_total=active_struct_total.get(maxq,0) if maxq else 0
                st_complete=active_struct_complete.get(maxq,0) if maxq else 0
                st_rate=st_complete/st_total if st_total else 0
                ev["gates"].append({"gate":11,"pass":st_rate>=0.90,"observed":{"active_rows":st_total,"complete_type_source_population":st_complete,"rate":st_rate,"threshold":0.90}})

                # Violation/enforcement table full pass.
                vfields,vrows=open_dict_reader(zf,mm["SDWA_VIOLATIONS_ENFORCEMENT.CSV"])
                vset=set(vfields); g12=VIOL_REQUIRED.issubset(vset)
                ev["gates"].append({"gate":12,"pass":g12,"observed":{"headers":vfields,"missing":sorted(VIOL_REQUIRED-vset)}})

                viol_rows=0; vp_nonblank=0; vp_valid=0; viol_pws=set()
                hi_nonblank=0; hi_recognized=0
                health_events=set(); health_date_ok=0
                health_categories=Counter(); violation_statuses=Counter()
                for r in vrows:
                    viol_rows+=1
                    pid=str(r.get("PWSID") or "").strip().upper()
                    if pid:
                        vp_nonblank+=1; viol_pws.add(pid)
                        if PWS_RE.fullmatch(pid): vp_valid+=1
                    hi=str(r.get("IS_HEALTH_BASED_IND") or "").strip().upper()
                    if hi:
                        hi_nonblank+=1
                        if hi in {"Y","N"}: hi_recognized+=1
                    vs=str(r.get("VIOLATION_STATUS") or "").strip()
                    if vs: violation_statuses[vs]+=1
                    if hi=="Y" and PWS_RE.fullmatch(pid):
                        vid=str(r.get("VIOLATION_ID") or "").strip()
                        if vid:
                            e=(pid,vid)
                            if e not in health_events:
                                health_events.add(e)
                                if date_ok(r.get("NON_COMPL_PER_BEGIN_DATE")): health_date_ok+=1
                            cat=str(r.get("VIOLATION_CATEGORY_CODE") or "").strip()
                            if cat: health_categories[cat]+=1

                vp_rate=vp_valid/vp_nonblank if vp_nonblank else 0
                matched=len({x for x in viol_pws if x in all_pws})
                join_rate=matched/len(viol_pws) if viol_pws else 0
                g13=(vp_rate>=0.999 and join_rate>=0.99)
                ev["gates"].append({"gate":13,"pass":g13,"observed":{"violation_rows":viol_rows,"pwsid_nonblank":vp_nonblank,"pwsid_valid":vp_valid,"syntax_rate":vp_rate,"distinct_violation_pwsids":len(viol_pws),"matched_to_pws_table":matched,"join_rate":join_rate}})

                hi_rate=hi_recognized/hi_nonblank if hi_nonblank else 0
                g14=(hi_rate>=0.99 and len(health_events)>=10000)
                ev["gates"].append({"gate":14,"pass":g14,"observed":{"health_indicator_nonblank":hi_nonblank,"recognized_YN":hi_recognized,"semantic_rate":hi_rate,"distinct_health_events":len(health_events),"event_threshold":10000,"categories":dict(health_categories)}})
                hd_rate=health_date_ok/len(health_events) if health_events else 0
                ev["gates"].append({"gate":15,"pass":hd_rate>=0.99,"observed":{"health_events":len(health_events),"parseable_begin_dates":health_date_ok,"rate":hd_rate,"threshold":0.99}})

                g16=(ev["later_refresh_opened"] is False and ev["future_health_based_violation_membership_opened"] is False and ev["future_entity_rows_consumed"]==0)
                ev["gates"].append({"gate":16,"pass":g16,"observed":{"baseline_sha256":zmeta["sha256"],"baseline_max_quarter":maxq_label,"later_refresh_opened":False,"future_membership_opened":False,"future_rows_consumed":0}})
                g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],ev["prohibited_compliance_enforcement_exposure_computed"],ev["identity_repair_used"]])
                ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,"ranking":False,"causal":False,"prohibited_exposure":False,"identity_repair":False}})
                g18=(re.fullmatch(r"[0-9a-f]{64}",zmeta["sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
                ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{"baseline_sha256":zmeta["sha256"],"runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        # Missing table/schema is a valid empirical failure once official baseline is downloaded.
        failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
        ev["attempt_valid"]=True
        ev["pass_count"]=18-len(failed)
        ev["failed_gates"]=failed
        ev["disposition"]="PASS_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_READY" if not failed else "HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY"
    except RuntimeError as e:
        # Only errors before a complete valid empirical gate ledger are implementation blocks.
        if str(e) in {"BASELINE_ZIP_NOT_PARSEABLE"}:
            ev["attempt_valid"]=False
            ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
            ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
            ev["failed_gates"]=[]
            ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_SDWIS_F01_ATTEMPT_01"
        elif str(e)=="REQUIRED_TABLES_MISSING":
            # Preserve already-observed scientific gate failure; fill remaining gates as false/not evaluated.
            seen={x["gate"] for x in ev["gates"]}
            for g in range(6,19):
                if g not in seen: ev["gates"].append({"gate":g,"pass":False,"observed":{"not_evaluated_after_decisive_gate5":True}})
            ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
            failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
            ev["attempt_valid"]=True;ev["pass_count"]=18-len(failed);ev["failed_gates"]=failed
            ev["disposition"]="HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY"
        else:
            ev["attempt_valid"]=False
            ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
            ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
            ev["failed_gates"]=[]
            ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_SDWIS_F01_ATTEMPT_01"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_SDWIS_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-EPA-SDWIS-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Later quarterly refresh opened: **{ev['later_refresh_opened']}**",
           f"- Future health-based membership opened: **{ev['future_health_based_violation_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1200:o=o[:1197]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):
        lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","The raw EPA ZIP was transient only. No later quarterly refresh body was opened and no predictive/outcome relation was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":
    main()
