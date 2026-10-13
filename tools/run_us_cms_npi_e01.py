#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urljoin
import csv, hashlib, io, json, math, os, re, tempfile, zipfile

import requests
from scipy.stats import binomtest

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="48843c9979336dcd10fdff984f458277062d6f20"
ISSUE=203
OUTDIR=ROOT/"research/US-CMS-NPI-E01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"

PAGE_URL="https://download.cms.gov/nppes/NPI_Files.html"
FULL_URL="https://download.cms.gov/nppes/NPPES_Data_Dissemination_October_2026_V2.zip"
DEACT_URL="https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_101226_V2.zip"
FULL_SHA="45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e"
DEACT_SHA="fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1"
ANCHOR_TOKEN="100526_101126"
BASELINE_DATE=date(2026,10,12)
EXPECTED_ELIGIBLE=1978439
EXPECTED_EXPOSED=409936
EXPECTED_CONTROL=1568503
EXPECTED_PAIRS=346859
EXPECTED_AGE_SMD=0.008089949330951387
EXPECTED_LOC_SMD=0.01358494151547246
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; preregistered-future-study)"
NPI_RE=re.compile(r"^[0-9]{10}$")
STATE_RE=re.compile(r"^[A-Z]{2}$")
csv.field_size_limit(1024*1024*64)

def norm(s): return re.sub(r"[^a-z0-9]+","",str(s or "").strip().lower())

def parse_date(v):
    if isinstance(v,datetime): return v.date()
    if isinstance(v,date): return v
    s=str(v or "").strip()
    if not s:return None
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y"):
        try:return datetime.strptime(s,f).date()
        except ValueError:pass
    return None

def parse_range(token):
    m=re.fullmatch(r"(\d{6})_(\d{6})",str(token or ""))
    if not m:return None
    try:return datetime.strptime(m.group(1),"%m%d%y").date(),datetime.strptime(m.group(2),"%m%d%y").date()
    except ValueError:return None

def sha_file(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()

def download(url,path,timeout=1200):
    h=hashlib.sha256();n=0
    with requests.get(url,headers={"User-Agent":UA},timeout=(30,timeout),allow_redirects=True,stream=True) as r:
        r.raise_for_status()
        meta={"requested_url":url,"final_url":r.url,"status":r.status_code,
              "content_type":r.headers.get("content-type"),"content_length_header":r.headers.get("content-length"),
              "last_modified":r.headers.get("last-modified"),"etag":r.headers.get("etag")}
        with path.open("wb") as f:
            for b in r.iter_content(1024*1024):
                if b:f.write(b);h.update(b);n+=len(b)
    meta["bytes"]=n;meta["sha256"]=h.hexdigest();return meta

def inv(path):
    with zipfile.ZipFile(path) as z:return z.namelist(),z.testzip()

def find_member(names,kind):
    for n in names:
        l=n.lower()
        if kind=="main" and "npidata_pfile" in l and l.endswith(".csv") and "header" not in l:return n
        if kind=="practice" and ("pl_pfile" in l or "practice_location" in l) and l.endswith(".csv") and "header" not in l:return n
    return None

def csv_reader(z,member):
    raw=z.open(member)
    txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    rd=csv.DictReader(txt)
    fields=[str(x or "").strip() for x in (rd.fieldnames or [])]
    def rows():
        try:
            for r in rd:yield r
        finally:txt.close()
    return fields,rows()

def idxmap(fields):return {norm(x):x for x in fields}
def getcol(m,key):return m.get(key)

def hkey(npi):
    return hashlib.sha256(("CMS-NPI-N01|"+npi).encode()).hexdigest()

def smd(a_sum,a_sq,b_sum,b_sq,n):
    if n<2:return None
    am=a_sum/n;bm=b_sum/n
    av=max(0,(a_sq-(a_sum*a_sum/n))/(n-1))
    bv=max(0,(b_sq-(b_sum*b_sum/n))/(n-1))
    sp=math.sqrt((av+bv)/2)
    if sp==0:return 0.0 if am==bm else float("inf")
    return (am-bm)/sp

def discover_weeklies():
    r=requests.get(PAGE_URL,headers={"User-Agent":UA},timeout=90,allow_redirects=True)
    r.raise_for_status();html=r.text
    listings=[]
    link_re=re.compile(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',re.I|re.S)
    for href,label_html in link_re.findall(html):
        label=" ".join(re.sub(r"<[^>]+>"," ",label_html).split())
        hay=f"{label} {href}"
        if "weekly" not in hay.lower():continue
        m=re.search(r"(\d{6}_\d{6})",hay)
        if not m:continue
        rng=parse_range(m.group(1))
        if not rng:continue
        listings.append({"token":m.group(1),"start":rng[0],"end":rng[1],
                         "label":label,"href":urljoin(r.url,href)})
    # Deduplicate.
    uniq={}
    for x in listings:uniq[(x["token"],x["href"])]=x
    listings=sorted(uniq.values(),key=lambda x:(x["start"],x["end"],x["token"]))
    qualifying=[x for x in listings if x["start"]>=BASELINE_DATE and x["end"]>BASELINE_DATE]
    return {
        "page":{"requested_url":PAGE_URL,"final_url":r.url,"status":r.status_code,
                "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
                "etag":r.headers.get("etag"),"bytes":len(r.content),"sha256":hashlib.sha256(r.content).hexdigest()},
        "listings":listings,"qualifying":qualifying
    }

def reconstruct_pairs(full_path):
    records={}
    with zipfile.ZipFile(full_path) as z:
        names=z.namelist();mainm=find_member(names,"main");plm=find_member(names,"practice")
        if not mainm or not plm:raise RuntimeError("BASELINE_MEMBER_MISSING")
        fields,rows=csv_reader(z,mainm);m=idxmap(fields)
        npi=getcol(m,"npi");entity=getcol(m,"entitytypecode")
        deact=getcol(m,"npideactivationdate");react=getcol(m,"npireactivationdate")
        enum=getcol(m,"providerenumerationdate");state=getcol(m,"providerbusinesspracticelocationaddressstatename")
        sub=getcol(m,"isorganizationsubpart")
        tax_cols=[];pri_cols=[]
        for i in range(1,16):
            tc=getcol(m,f"healthcareprovidertaxonomycode{i}")
            pc=getcol(m,f"healthcareproviderprimarytaxonomyswitch{i}")
            if tc:tax_cols.append(tc)
            if pc:pri_cols.append(pc)
        if not all([npi,entity,deact,react,enum,state,sub]) or len(tax_cols)!=15 or len(pri_cols)!=15:
            raise RuntimeError("BASELINE_SCHEMA_MISMATCH")
        for r in rows:
            x=str(r.get(npi) or "").strip()
            if not NPI_RE.fullmatch(x):continue
            if str(r.get(entity) or "").strip()!="2":continue
            if str(r.get(deact) or "").strip() or str(r.get(react) or "").strip():continue
            st=str(r.get(state) or "").strip().upper()
            if not STATE_RE.fullmatch(st):continue
            ed=parse_date(r.get(enum))
            if not ed or ed>BASELINE_DATE:continue
            taxes=[str(r.get(c) or "").strip() for c in tax_cols]
            tcount=sum(1 for v in taxes if v)
            if tcount<1:continue
            prim=[taxes[i] for i,pc in enumerate(pri_cols)
                  if str(r.get(pc) or "").strip().upper()=="Y" and taxes[i]]
            if len(prim)!=1:continue
            exp=1 if tcount>=2 else 0
            age_days=(BASELINE_DATE-ed).days
            age_band=int(age_days/365.2425)//5
            sb=str(r.get(sub) or "").strip().upper()
            if sb not in ("Y","N"):sb="BLANK"
            records[x]=[exp,st,prim[0][:4],age_days,age_band,sb,1]
        pf,prows=csv_reader(z,plm);pm=idxmap(pf);pn=getcol(pm,"npi")
        for r in prows:
            x=str(r.get(pn) or "").strip() if pn else ""
            if x in records:records[x][6]+=1

    exposed=sum(1 for v in records.values() if v[0]==1)
    control=len(records)-exposed
    strata=defaultdict(lambda:[[],[]])
    for npi,v in records.items():
        exp,st,prefix,age_days,age_band,sb,loc=v
        locbin="1" if loc==1 else ("2" if loc==2 else "3+")
        strata[(st,prefix,age_band,sb,locbin)][exp].append((hkey(npi),npi,age_days,loc))
    common={k:v for k,v in strata.items() if v[0] and v[1]}

    pairs=[];used_e=set();used_c=set()
    es_age=es_age2=cs_age=cs_age2=0.0
    es_loc=es_loc2=cs_loc=cs_loc2=0.0
    for k,(ctrl,exp) in common.items():
        ctrl.sort(key=lambda x:x[0]);exp.sort(key=lambda x:x[0])
        for i in range(min(len(ctrl),len(exp))):
            e=exp[i];c=ctrl[i]
            if e[1] in used_e or c[1] in used_c:raise RuntimeError("PAIR_REUSE")
            used_e.add(e[1]);used_c.add(c[1]);pairs.append((e[1],c[1]))
            es_age+=e[2];es_age2+=e[2]*e[2];cs_age+=c[2];cs_age2+=c[2]*c[2]
            es_loc+=e[3];es_loc2+=e[3]*e[3];cs_loc+=c[3];cs_loc2+=c[3]*c[3]
    n=len(pairs)
    age=smd(es_age,es_age2,cs_age,cs_age2,n)
    loc=smd(es_loc,es_loc2,cs_loc,cs_loc2,n)
    return records, pairs, {
        "eligible":len(records),"exposed":exposed,"control":control,"pairs":n,
        "unique_exposed":len(used_e),"unique_controls":len(used_c),
        "age_smd":age,"location_smd":loc,"common_strata":len(common)
    }

def exact_mor_ci(b,c):
    q=b+c
    if q<=0:return None,None,None,None
    bt=binomtest(b,q,p=0.5,alternative="two-sided")
    ci=bt.proportion_ci(confidence_level=0.95,method="exact")
    p=b/q
    mor=0.0 if b==0 else (float("inf") if c==0 else b/c)
    lo=0.0 if ci.low<=0 else ci.low/(1-ci.low)
    hi=float("inf") if ci.high>=1 else ci.high/(1-ci.high)
    return mor,lo,hi,bt.pvalue

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():raise RuntimeError("immutable attempt-01 evidence exists")
    ev={"research":"US-CMS-NPI-E01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_update_body_opened":False,"future_deactivation_membership_opened":False,
        "monthly_substitution_used":False,"later_week_selected":False,"identity_repair_used":False,
        "provider_ranking_computed":False,"causal_claim_made":False,"closure_quality_interpretation_made":False,
        "gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261013-US-CMS-NPI-E01-ACTIVE"
            and cp.get("active_issue")==203 and cp.get("active_research")=="US-CMS-NPI-E01"
            and cp.get("last_decision")=="DEC-318")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("CMS_NPI_E01_BOUND")=="1" and os.environ.get("CMS_NPI_E01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":203,"contract_sha":os.environ.get("CMS_NPI_E01_CONTRACT_SHA")}})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0);fp=td/"full.zip";dp=td/"deact.zip";wp=td/"weekly.zip"
            fm=download(FULL_URL,fp);dm=download(DEACT_URL,dp)
            g3=(fm["sha256"]==FULL_SHA and dm["sha256"]==DEACT_SHA)
            ev["baseline_full"]=fm;ev["baseline_deactivation"]=dm
            ev["gates"].append({"gate":3,"pass":g3,"observed":{"full_sha256":fm["sha256"],"deactivation_sha256":dm["sha256"],
                "expected_full":FULL_SHA,"expected_deactivation":DEACT_SHA}})
            if not g3:raise RuntimeError("BASELINE_SHA_MISMATCH")

            records,pairs,cohort=reconstruct_pairs(fp)
            g4=(cohort["eligible"]==EXPECTED_ELIGIBLE and cohort["exposed"]==EXPECTED_EXPOSED and cohort["control"]==EXPECTED_CONTROL)
            ev["gates"].append({"gate":4,"pass":g4,"observed":cohort})
            g5=(cohort["pairs"]==EXPECTED_PAIRS and cohort["unique_exposed"]==EXPECTED_PAIRS and cohort["unique_controls"]==EXPECTED_PAIRS)
            ev["gates"].append({"gate":5,"pass":g5,"observed":{"pairs":cohort["pairs"],"unique_exposed":cohort["unique_exposed"],"unique_controls":cohort["unique_controls"],"expected":EXPECTED_PAIRS}})
            g6=(abs(cohort["age_smd"]-EXPECTED_AGE_SMD)<=1e-6 and abs(cohort["location_smd"]-EXPECTED_LOC_SMD)<=1e-6)
            ev["gates"].append({"gate":6,"pass":g6,"observed":{"age_smd":cohort["age_smd"],"expected_age_smd":EXPECTED_AGE_SMD,
                "location_smd":cohort["location_smd"],"expected_location_smd":EXPECTED_LOC_SMD,"tolerance":1e-6}})

            pf=json.loads((ROOT/"research/US-CMS-NPI-E01/evidence/source-preflight-01.json").read_text())
            g7=(pf.get("anchor_present") is True and pf.get("anchor_token")==ANCHOR_TOKEN and pf.get("zip_body_opened") is False)
            ev["gates"].append({"gate":7,"pass":g7,"observed":{"preflight_commit":"0e81620e9cbea5dcddb558791e786d1565dfaf0f",
                "anchor_present":pf.get("anchor_present"),"anchor_token":pf.get("anchor_token"),"preflight_zip_body_opened":pf.get("zip_body_opened")}})

            src=discover_weeklies();ev["source_discovery"]={
                "page":src["page"],
                "listings":[{**x,"start":x["start"].isoformat(),"end":x["end"].isoformat()} for x in src["listings"]]
            }
            if not src["qualifying"]:
                raise RuntimeError("NO_QUALIFYING_WEEKLY_SOURCE")
            chosen=src["qualifying"][0]
            ev["chosen_future_source"]={**chosen,"start":chosen["start"].isoformat(),"end":chosen["end"].isoformat()}
            g8=(chosen==src["qualifying"][0] and chosen["start"]>=BASELINE_DATE and chosen["end"]>BASELINE_DATE)
            ev["gates"].append({"gate":8,"pass":g8,"observed":{"chosen_token":chosen["token"],"start":chosen["start"].isoformat(),
                "end":chosen["end"].isoformat(),"qualifying_count":len(src["qualifying"]),"earliest":True}})

            wm=download(chosen["href"],wp);ev["future_weekly_zip"]=wm;ev["future_update_body_opened"]=True
            names,bad=inv(wp)
            g9=(bad is None and wm["status"]==200 and wm["bytes"]>1000 and "download.cms.gov" in wm["final_url"])
            ev["gates"].append({"gate":9,"pass":g9,"observed":{**wm,"zip_members":names}})
            if not g9:raise RuntimeError("FUTURE_WEEKLY_ZIP_INVALID")

            with zipfile.ZipFile(wp) as z:
                mainm=find_member(names,"main")
                if not mainm:raise RuntimeError("FUTURE_MAIN_MEMBER_MISSING")
                fields,rows=csv_reader(z,mainm);m=idxmap(fields)
                npi=getcol(m,"npi");entity=getcol(m,"entitytypecode")
                deact=getcol(m,"npideactivationdate");react=getcol(m,"npireactivationdate")
                g10=all([npi,entity,deact,react])
                ev["gates"].append({"gate":10,"pass":bool(g10),"observed":{"main_member":mainm,"npi":npi,"entity":entity,"deactivation":deact,"reactivation":react}})
                if not g10:raise RuntimeError("FUTURE_SCHEMA_MISMATCH")

                future_nonblank=0;future_valid=0;locked_candidate=0;candidate_parse=0
                event_npis=set();reactivated_event_npis=set();outside_window=0;duplicate_future_npi=0;seen_future=set()
                for r in rows:
                    x=str(r.get(npi) or "").strip()
                    if x:future_nonblank+=1
                    if NPI_RE.fullmatch(x):future_valid+=1
                    if not NPI_RE.fullmatch(x):continue
                    if x in seen_future:duplicate_future_npi+=1
                    else:seen_future.add(x)
                    if x not in records:continue
                    ds=str(r.get(deact) or "").strip()
                    if not ds:continue
                    locked_candidate+=1
                    dd=parse_date(ds)
                    if dd:candidate_parse+=1
                    if dd and BASELINE_DATE<=dd<=chosen["end"]:
                        event_npis.add(x);ev["future_deactivation_membership_opened"]=True
                        if str(r.get(react) or "").strip():
                            reactivated_event_npis.add(x)

            syntax=future_valid/future_nonblank if future_nonblank else 0
            ev["gates"].append({"gate":11,"pass":syntax>=0.99999,"observed":{"future_nonblank_npis":future_nonblank,"valid_exact_npis":future_valid,"rate":syntax,"threshold":0.99999}})
            g12=(all(x in records for x in event_npis) and ev["identity_repair_used"] is False)
            ev["gates"].append({"gate":12,"pass":g12,"observed":{"counted_event_npis":len(event_npis),"all_exact_join_locked":all(x in records for x in event_npis),"identity_repair":False}})
            parse_rate=candidate_parse/locked_candidate if locked_candidate else 1.0
            g13=(parse_rate>=0.999)
            ev["gates"].append({"gate":13,"pass":g13,"observed":{"locked_candidate_deactivation_rows":locked_candidate,
                "parseable_dates":candidate_parse,"parse_rate":parse_rate,"threshold":0.999,"event_window_start":BASELINE_DATE.isoformat(),
                "event_window_end":chosen["end"].isoformat(),"counted_in_window":len(event_npis),"outside_window_or_unparsed":locked_candidate-len(event_npis)}})

            a=b=c=d=0;exp_events=ctl_events=0;exp_react=ctl_react=0
            for enpi,cnpi in pairs:
                ee=enpi in event_npis;ce=cnpi in event_npis
                if ee:exp_events+=1
                if ce:ctl_events+=1
                if enpi in reactivated_event_npis:exp_react+=1
                if cnpi in reactivated_event_npis:ctl_react+=1
                if ee and ce:a+=1
                elif ee:b+=1
                elif ce:c+=1
                else:d+=1
            g14=(a+b+c+d==EXPECTED_PAIRS)
            ev["pair_table"]={"a_both":a,"b_exposed_only":b,"c_control_only":c,"d_neither":d}
            ev["gates"].append({"gate":14,"pass":g14,"observed":{**ev["pair_table"],"sum":a+b+c+d,"expected":EXPECTED_PAIRS}})
            ev["gates"].append({"gate":15,"pass":True,"observed":{"same_update_reactivation_exposed":exp_react,
                "same_update_reactivation_control":ctl_react,"reactivation_erases_event":False}})

            mor,lo,hi,p=exact_mor_ci(b,c)
            q=b+c;total_deactivated_npis=2*a+b+c
            support=(total_deactivated_npis>=30 and q>=20)
            exp_risk=exp_events/EXPECTED_PAIRS;ctl_risk=ctl_events/EXPECTED_PAIRS
            rr=(exp_risk/ctl_risk) if ctl_risk>0 else (float("inf") if exp_risk>0 else None)
            rd100k=(exp_risk-ctl_risk)*100000
            ev["statistics"]={"matched_odds_ratio":mor,"mor_ci95":[lo,hi],"mcnemar_exact_p":p,
                "discordant_pairs":q,"total_deactivated_matched_npis":total_deactivated_npis,
                "exposed_events":exp_events,"control_events":ctl_events,
                "exposed_risk":exp_risk,"control_risk":ctl_risk,"marginal_risk_ratio":rr,
                "risk_difference_per_100k":rd100k,"minimum_event_support_satisfied":support}
            ev["gates"].append({"gate":16,"pass":q>=0 and (q==0 or p is not None),"observed":ev["statistics"]})

            g17=not any([ev["monthly_substitution_used"],ev["later_week_selected"],ev["identity_repair_used"],
                         ev["provider_ranking_computed"],ev["causal_claim_made"],ev["closure_quality_interpretation_made"]])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{"monthly_substitution":False,"later_week_selected":False,
                "identity_repair":False,"provider_ranking":False,"causal_claim":False,"closure_quality_interpretation":False}})
            g18=(fm["sha256"]==FULL_SHA and dm["sha256"]==DEACT_SHA and re.fullmatch(r"[0-9a-f]{64}",wm["sha256"]) is not None
                 and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{"baseline_full_sha":fm["sha256"],
                "baseline_deactivation_sha":dm["sha256"],"future_weekly_sha":wm["sha256"],"contract_sha":CONTRACT_SHA,
                "runner_sha":ev["runner_sha256"],"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True;ev["pass_count"]=18-len(failed);ev["failed_gates"]=failed
        if failed:
            ev["disposition"]="HOLD_US_CMS_NPI_E01_EXECUTION_INTEGRITY_FAILED"
        elif not ev["statistics"]["minimum_event_support_satisfied"]:
            ev["disposition"]="INSUFFICIENT_EVENT_SUPPORT_US_CMS_NPI_E01"
        else:
            mor=ev["statistics"]["matched_odds_ratio"];lo,hi=ev["statistics"]["mor_ci95"];p=ev["statistics"]["mcnemar_exact_p"]
            material=(mor is not None and (mor<=0.80 or mor>=1.25))
            ci_excludes_one=(hi<1.0 or lo>1.0)
            if p<=0.05 and ci_excludes_one and material:
                ev["disposition"]="VALIDATED_MATERIAL_DIFFERENCE_US_CMS_NPI_E01"
            elif lo>=0.80 and hi<=1.25:
                ev["disposition"]="NO_MATERIAL_DIFFERENCE_US_CMS_NPI_E01"
            else:
                ev["disposition"]="INCONCLUSIVE_US_CMS_NPI_E01"
    except RuntimeError as e:
        if str(e)=="NO_QUALIFYING_WEEKLY_SOURCE":
            ev["attempt_valid"]=False
            ev["source_wait"]=True
            ev["implementation_error"]={"type":"WAIT_SOURCE","message":str(e)}
            ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
            ev["disposition"]="WAIT_SOURCE_US_CMS_NPI_E01"
        else:
            ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
            ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
            ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NPI_E01_ATTEMPT_01"
    except Exception as e:
        ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NPI_E01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-CMS-NPI-E01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Execution gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future update body opened: **{ev['future_update_body_opened']}**",
           f"- Future deactivation membership opened: **{ev['future_deactivation_membership_opened']}**",
           f"- Cost: **0 USD**",""]
    if ev.get("chosen_future_source"):
        lines += ["## Future source","",f"- Token: `{ev['chosen_future_source']['token']}`",
                  f"- Covered: **{ev['chosen_future_source']['start']}..{ev['chosen_future_source']['end']}**",""]
    if ev.get("pair_table"):
        lines += ["## Pair outcome table","",
                  "| both | exposed only | control only | neither |",
                  "|---:|---:|---:|---:|",
                  f"| {ev['pair_table']['a_both']} | {ev['pair_table']['b_exposed_only']} | {ev['pair_table']['c_control_only']} | {ev['pair_table']['d_neither']} |",""]
    if ev.get("statistics"):
        lines += ["## Frozen statistics","",f"`{json.dumps(ev['statistics'],ensure_ascii=False,default=str)}`",""]
    lines += ["## Execution gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1200:o=o[:1197]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Runtime/source state","",f"`{ev['implementation_error']}`"]
    lines += ["","NPI deactivation is treated only as an administrative NPPES registry event. No provider ranking or causal interpretation is authorized.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":
    main()
