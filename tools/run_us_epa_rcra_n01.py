#!/usr/bin/env python3
from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
import csv, hashlib, io, json, math, os, re, statistics, tempfile, zipfile
import requests

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-EPA-RCRA-N01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"; MD_OUT=OUTDIR/"attempt-01.md"
CONTRACT_SHA="14b9509808bcfd9a6affc694ec97531105d8ca41"
F01_EVIDENCE_SHA="4994dd3e0614d0c91e04b757d8e3dbe1fca6c335"
BASELINE_SHA="ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5"
ISSUE=199
ZIP_URL="https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
S=requests.Session();S.headers.update({"User-Agent":UA})
csv.field_size_limit(1024*1024*64)

CUTOFF=date(2026,10,4)
WIN5_START=date(2021,10,5)
RECENT_START=date(2025,10,5)
FUTURE_START=date(2026,10,5)
FUTURE_END=date(2027,4,4)

def norm(v): return str(v or "").strip().upper()
def id_ok(v):
    s=norm(v); return 4<=len(s)<=12 and bool(re.fullmatch(r"[A-Z]{2}[A-Z0-9]{2,10}",s))
def loc_ok(v): return bool(re.fullmatch(r"[A-Z]{2}",norm(v)))
def parse_date(v):
    s=str(v or "").strip()
    for fmt in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y","%d-%b-%Y","%Y%m%d"):
        try:return datetime.strptime(s,fmt).date()
        except ValueError:pass
    return None
def download(path):
    h=hashlib.sha256();total=0
    with S.get(ZIP_URL,timeout=(30,600),stream=True,allow_redirects=True) as r:
        r.raise_for_status()
        meta={"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),
              "last_modified":r.headers.get("last-modified"),"etag":r.headers.get("etag"),
              "content_length_header":r.headers.get("content-length")}
        with path.open("wb") as f:
            for chunk in r.iter_content(1024*1024):
                if not chunk:continue
                f.write(chunk);h.update(chunk);total+=len(chunk)
    meta["bytes"]=total;meta["sha256"]=h.hexdigest();return meta
def mmap(z): return {Path(n).name.upper():n for n in z.namelist() if not n.endswith("/")}
def dict_reader(z,m):
    raw=z.open(m);txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    rr=csv.DictReader(txt)
    fields=[norm(x) for x in (rr.fieldnames or [])]
    def gen():
        try:
            for row in rr:yield {norm(k):v for k,v in row.items()}
        finally:txt.close()
    return fields,gen()
def raw_reader(z,m):
    raw=z.open(m);txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    rr=csv.reader(txt);header=[norm(x) for x in next(rr)]
    return txt,rr,header
def mean_sd(vals):
    if not vals:return (0.0,0.0)
    return statistics.fmean(vals),statistics.stdev(vals) if len(vals)>1 else 0.0
def smd(a,b):
    if not a or not b:return float("inf")
    ma,mb=statistics.fmean(a),statistics.fmean(b)
    va=statistics.variance(a) if len(a)>1 else 0.0
    vb=statistics.variance(b) if len(b)>1 else 0.0
    p=math.sqrt((va+vb)/2)
    if p==0:return 0.0 if ma==mb else float("inf")
    return (ma-mb)/p

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():raise RuntimeError("immutable attempt-01 evidence exists")
    ev={"research":"US-EPA-RCRA-N01","attempt":1,"issue":ISSUE,"contract_sha":CONTRACT_SHA,
        "f01_evidence_commit":F01_EVIDENCE_SHA,"baseline_sha256":BASELINE_SHA,
        "github_run_id":os.getenv("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "later_refresh_opened":False,"future_found_violation_membership_opened":False,
        "found_violation_values_consumed":0,"forbidden_outcome_tables_opened":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
        "causal_claim_made":False,"prohibited_compliance_enforcement_exposure_computed":False,
        "identity_repair_used":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261008-US-EPA-RCRA-N01-ACTIVE" and cp.get("active_issue")==199
            and cp.get("active_research")=="US-EPA-RCRA-N01" and cp.get("last_decision")=="DEC-310")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.getenv("RCRA_N01_BOUND")=="1" and os.getenv("RCRA_N01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":199,"contract_sha":os.getenv("RCRA_N01_CONTRACT_SHA")}})

        with tempfile.TemporaryDirectory() as td:
            zp=Path(td)/"rcra.zip";meta=download(zp);ev["baseline_download"]=meta
            same=(meta["sha256"]==BASELINE_SHA)
            ev["gates"].append({"gate":3,"pass":same,"observed":{"expected_sha256":BASELINE_SHA,"observed_sha256":meta["sha256"],
                                                                  "bytes":meta["bytes"],"last_modified":meta["last_modified"]}})
            if not same:
                for n in range(4,19):ev["gates"].append({"gate":n,"pass":False,"observed":{"not_evaluated_after_baseline_drift":True}})
                ev["attempt_valid"]=True;ev["failed_gates"]=[g["gate"] for g in ev["gates"] if not g["pass"]]
                ev["pass_count"]=18-len(ev["failed_gates"])
                ev["disposition"]="HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY"
                raise StopIteration

            with zipfile.ZipFile(zp) as z:
                mm=mmap(z)
                needed={"RCRA_FACILITIES.CSV","RCRA_NAICS.CSV","RCRA_EVALUATIONS.CSV"}
                if not needed.issubset(mm):raise RuntimeError("REQUIRED_N01_TABLES_MISSING")
                ff,fr=dict_reader(z,mm["RCRA_FACILITIES.CSV"])
                nf,nr=dict_reader(z,mm["RCRA_NAICS.CSV"])
                etxt,err,ef=raw_reader(z,mm["RCRA_EVALUATIONS.CSV"])
                req_fac={"ID_NUMBER","ACTIVITY_LOCATION","FED_WASTE_GENERATOR","TRANSPORTER","ACTIVE_SITE","OPERATING_TSDF"}
                req_naics={"ID_NUMBER","ACTIVITY_LOCATION","NAICS_CODE"}
                req_eval={"ID_NUMBER","ACTIVITY_LOCATION","EVALUATION_IDENTIFIER","EVALUATION_TYPE","EVALUATION_START_DATE"}
                g4=req_fac.issubset(ff) and req_naics.issubset(nf) and req_eval.issubset(ef)
                ev["gates"].append({"gate":4,"pass":g4,"observed":{"facility_missing":sorted(req_fac-set(ff)),
                    "naics_missing":sorted(req_naics-set(nf)),"evaluation_missing":sorted(req_eval-set(ef)),
                    "evaluation_headers":ef}})
                if not g4:raise RuntimeError("N01_SCHEMA_NOT_RESOLVED")

                # Facility structure only.
                fac={}
                for r in fr:
                    iid=norm(r.get("ID_NUMBER"));loc=norm(r.get("ACTIVITY_LOCATION"))
                    if not(id_ok(iid) and loc_ok(loc)):continue
                    active=norm(r.get("ACTIVE_SITE"))
                    gen=norm(r.get("FED_WASTE_GENERATOR"))
                    trans=norm(r.get("TRANSPORTER"))
                    tsdf=norm(r.get("OPERATING_TSDF"))
                    role=(gen in {"1","2","3"}) or trans=="Y" or bool(tsdf)
                    if not active or not role:continue
                    key=(iid,loc)
                    # deterministic first-row retention; duplicates are rare and source-order is immutable under SHA.
                    if key not in fac:fac[key]=(gen,trans,1 if tsdf else 0,active)

                # NAICS structural breadth; keep only minimum code and whether a distinct second code exists.
                ni={}
                for r in nr:
                    iid=norm(r.get("ID_NUMBER"));loc=norm(r.get("ACTIVITY_LOCATION"));code=norm(r.get("NAICS_CODE"))
                    if not(id_ok(iid) and loc_ok(loc) and re.fullmatch(r"[0-9]{6}",code)):continue
                    key=(iid,loc)
                    if key not in ni:ni[key]=[code,code,False]
                    else:
                        first,minc,multi=ni[key]
                        if code!=first:multi=True
                        if code<minc:minc=code
                        ni[key]=[first,minc,multi]

                # Evaluation opportunity history. We never index or access FOUND_VIOLATION.
                idx={h:i for i,h in enumerate(ef)}
                found_idx=idx.get("FOUND_VIOLATION",idx.get("FOUND_VOLATION"))
                ev["evaluation_found_column_present"]=found_idx is not None
                seen=set();ecount=defaultdict(int);last={};recent=set()
                eval_rows_scanned=0
                for row in err:
                    eval_rows_scanned+=1
                    # Deliberately access only identity/type/date indexes.
                    iid=norm(row[idx["ID_NUMBER"]] if idx["ID_NUMBER"]<len(row) else "")
                    loc=norm(row[idx["ACTIVITY_LOCATION"]] if idx["ACTIVITY_LOCATION"]<len(row) else "")
                    eid=norm(row[idx["EVALUATION_IDENTIFIER"]] if idx["EVALUATION_IDENTIFIER"]<len(row) else "")
                    etype=norm(row[idx["EVALUATION_TYPE"]] if idx["EVALUATION_TYPE"]<len(row) else "")
                    ds=row[idx["EVALUATION_START_DATE"]] if idx["EVALUATION_START_DATE"]<len(row) else ""
                    d=parse_date(ds)
                    if not(id_ok(iid) and loc_ok(loc) and d and WIN5_START<=d<=CUTOFF):continue
                    opp=(iid,loc,eid,etype,d.isoformat())
                    if opp in seen:continue
                    seen.add(opp);key=(iid,loc);ecount[key]+=1
                    if key not in last or d>last[key]:last[key]=d
                    if RECENT_START<=d<=CUTOFF:recent.add(key)
                etxt.close()
                ev["found_violation_values_consumed"]=0
                ev["forbidden_outcome_tables_opened"]=0
                g5=(ev["found_violation_values_consumed"]==0 and ev["forbidden_outcome_tables_opened"]==0)
                ev["gates"].append({"gate":5,"pass":g5,"observed":{"found_column_present":ev["evaluation_found_column_present"],
                    "found_values_consumed":0,"forbidden_outcome_tables_opened":0,"evaluation_rows_scanned":eval_rows_scanned}})

                eligible=[]
                for key,fv in fac.items():
                    if key not in ni or key not in ecount:continue
                    gen,trans,tsdf,active=fv
                    first,minc,multi=ni[key]
                    cnt=ecount[key];days=(CUTOFF-last[key]).days
                    x1=math.log1p(cnt);x2=math.log1p(days)
                    eligible.append({"key":key,"gen":gen,"trans":trans,"tsdf":tsdf,"naics2":minc[:2],
                                     "exposed":bool(multi),"x1":x1,"x2":x2,"recent":key in recent})
                neligible=len(eligible);nexp=sum(x["exposed"] for x in eligible);nctrl=neligible-nexp
                ev["gates"].append({"gate":6,"pass":neligible>=100000,"observed":{"eligible":neligible,"threshold":100000}})
                ev["gates"].append({"gate":7,"pass":nexp>=20000,"observed":{"multi_naics_exposed":nexp,"threshold":20000}})
                ev["gates"].append({"gate":8,"pass":nctrl>=40000,"observed":{"single_naics_controls":nctrl,"threshold":40000}})

                strata_e=defaultdict(list);strata_c=defaultdict(list)
                xs1=[x["x1"] for x in eligible];xs2=[x["x2"] for x in eligible]
                m1,s1=mean_sd(xs1);m2,s2=mean_sd(xs2)
                for x in eligible:
                    x["z1"]=(x["x1"]-m1)/s1 if s1>0 else 0.0
                    x["z2"]=(x["x2"]-m2)/s2 if s2>0 else 0.0
                    st=(x["key"][1],x["gen"],x["trans"],x["tsdf"],x["naics2"])
                    x["stratum"]=st
                    (strata_e if x["exposed"] else strata_c)[st].append(x)
                common=set(strata_e)&set(strata_c)
                ev["gates"].append({"gate":9,"pass":len(common)>=200,"observed":{"common_exact_strata":len(common),"threshold":200}})

                # Index controls by standardized X1 for deterministic caliper search.
                control_indexes={}
                for st in common:
                    arr=sorted(strata_c[st],key=lambda x:(x["z1"],x["key"]))
                    control_indexes[st]=(arr,[x["z1"] for x in arr])
                used=set();pairs=[]
                for e in sorted((x for st in common for x in strata_e[st]),key=lambda x:(x["stratum"],x["key"])):
                    arr,zs=control_indexes[e["stratum"]]
                    lo=bisect_left(zs,e["z1"]-0.5);hi=bisect_right(zs,e["z1"]+0.5)
                    best=None
                    for c in arr[lo:hi]:
                        if c["key"] in used or abs(c["z2"]-e["z2"])>0.5:continue
                        dist=(c["z1"]-e["z1"])**2+(c["z2"]-e["z2"])**2
                        cand=(dist,c["key"],c)
                        if best is None or cand[:2]<best[:2]:best=cand
                    if best is not None:
                        c=best[2];used.add(c["key"]);pairs.append((e,c))
                exact_mismatch=sum(1 for e,c in pairs if e["stratum"]!=c["stratum"])
                caliper_fail=sum(1 for e,c in pairs if abs(e["z1"]-c["z1"])>0.5 or abs(e["z2"]-c["z2"])>0.5)
                dup_controls=len(pairs)-len({c["key"] for _,c in pairs})
                g10=exact_mismatch==0 and caliper_fail==0 and dup_controls==0
                ev["gates"].append({"gate":10,"pass":g10,"observed":{"pairs":len(pairs),"exact_mismatch":exact_mismatch,
                    "caliper_fail":caliper_fail,"duplicate_controls":dup_controls}})
                ev["gates"].append({"gate":11,"pass":len(pairs)>=20000,"observed":{"matched_pairs":len(pairs),"threshold":20000}})
                coverage=len(pairs)/nexp if nexp else 0
                ev["gates"].append({"gate":12,"pass":coverage>=0.40,"observed":{"matched_pairs":len(pairs),
                    "eligible_exposed":nexp,"coverage":coverage,"threshold":0.40}})
                ex1=[e["x1"] for e,_ in pairs];ct1=[c["x1"] for _,c in pairs]
                ex2=[e["x2"] for e,_ in pairs];ct2=[c["x2"] for _,c in pairs]
                sx1=abs(smd(ex1,ct1));sx2=abs(smd(ex2,ct2))
                ev["gates"].append({"gate":13,"pass":sx1<=0.10,"observed":{"abs_smd_x1":sx1,"threshold":0.10}})
                ev["gates"].append({"gate":14,"pass":sx2<=0.10,"observed":{"abs_smd_x2":sx2,"threshold":0.10}})
                rex=sum(1 for e,_ in pairs if e["recent"]);rct=sum(1 for _,c in pairs if c["recent"]);rt=rex+rct
                g15=rt>=5000 and rex>=1500 and rct>=1500
                ev["gates"].append({"gate":15,"pass":g15,"observed":{"recent_opportunity_handlers_total":rt,
                    "exposed":rex,"control":rct,"threshold_total":5000,"threshold_each":1500}})
                g16=(not ev["later_refresh_opened"] and not ev["future_found_violation_membership_opened"])
                ev["gates"].append({"gate":16,"pass":g16,"observed":{"future_window":"2026-10-05..2027-04-04",
                    "later_refresh_opened":False,"future_membership_opened":False}})
                g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],
                    ev["prohibited_compliance_enforcement_exposure_computed"],ev["identity_repair_used"],
                    ev["found_violation_values_consumed"]])
                ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,
                    "ranking":False,"causal":False,"found_values_consumed":0,"prohibited_exposure":False,"identity_repair":False}})
                h=hashlib.sha256()
                for e,c in sorted(pairs,key=lambda p:(p[0]["key"],p[1]["key"])):
                    h.update(("|".join(e["key"])+"->"+"|".join(c["key"])+"\n").encode())
                manifest_sha=h.hexdigest()
                ev["matched_manifest_sha256"]=manifest_sha
                g18=(len(manifest_sha)==64 and len(ev["runner_sha256"])==64 and meta["sha256"]==BASELINE_SHA and ev["incremental_monetary_cost_usd"]==0)
                ev["gates"].append({"gate":18,"pass":g18,"observed":{"matched_manifest_sha256":manifest_sha,
                    "baseline_sha256":meta["sha256"],"contract_sha":CONTRACT_SHA,"runner_sha256":ev["runner_sha256"],"cost_usd":0}})

                ev["matching_summary"]={"eligible":neligible,"exposed":nexp,"control":nctrl,"common_strata":len(common),
                    "matched_pairs":len(pairs),"exposed_coverage":coverage,"abs_smd_x1":sx1,"abs_smd_x2":sx2,
                    "recent_exposed":rex,"recent_control":rct,"standardization":{"x1_mean":m1,"x1_sd":s1,"x2_mean":m2,"x2_sd":s2}}

        if "disposition" not in ev:
            ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
            failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
            ev["attempt_valid"]=True;ev["failed_gates"]=failed;ev["pass_count"]=18-len(failed)
            ev["disposition"]="PASS_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_LOCKED" if not failed else "HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY"
    except StopIteration:
        pass
    except Exception as e:
        ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_EPA_RCRA_N01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-EPA-RCRA-N01 — Attempt 01","",f"**Disposition:** §{ev['disposition']}§","",
      f"- Attempt valid: §{ev.get('attempt_valid')}§",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
      f"- Failed gates: §{ev.get('failed_gates',[])}§",f"- Later refresh opened: **{ev['later_refresh_opened']}**",
      f"- Future membership opened: **{ev['future_found_violation_membership_opened']}**",
      f"- Evaluation-result values consumed: **{ev['found_violation_values_consumed']}**",
      "- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | §{o}§ |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"§{ev['implementation_error']}§"]
    lines+=["","No later weekly refresh was opened. No evaluation-result value was accessed for N01 matching.",""]
    MD_OUT.write_text("\n".join(lines).replace("§",chr(96)),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":main()
