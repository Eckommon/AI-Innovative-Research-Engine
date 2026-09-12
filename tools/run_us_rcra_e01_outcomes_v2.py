#!/usr/bin/env python3
"""US-RCRA-E01 Pass 2. Uses only the committed frozen pair manifest."""
from __future__ import annotations
import csv, hashlib, io, json, math, os, urllib.request, zipfile
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"research"/"US-RCRA-E01"
TMP=Path(os.environ.get("RUNNER_TEMP","/tmp"))/"us-rcra-e01-v2"; TMP.mkdir(parents=True,exist_ok=True)
RCRA_URL="https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
UA="AI-Innovative-Research-Engine/US-RCRA-E01 frozen-pair outcome pass"

def iso_date(s:str)->str:
    s=(s or "").strip()
    for fmt,n in (("%m/%d/%Y",10),("%Y-%m-%d",10),("%Y-%m-%dT%H:%M:%S",19)):
        try:return datetime.strptime(s[:n],fmt).date().isoformat()
        except ValueError:pass
    return ""

def exact_p(ny:int,yn:int):
    m=ny+yn
    if m==0:return None
    lo=min(ny,yn)
    return min(1.0,2.0*sum(math.comb(m,k) for k in range(lo+1))/(2**m))

def oc(v:str)->str:
    u=(v or "").strip().upper()
    return u if u in {"Y","N","U"} else "BLANK_OTHER"

pm=json.loads((OUT/"PAIR_MANIFEST.json").read_text(encoding="utf-8"))
assert pm["issue"]==125 and pm["pair_count"]==297 and pm["state_territory_fips_count"]==43
assert pm["outcomes_opened"] is False and pm["found_violation_values_accessed_or_persisted"] is False
pairs=pm["pairs"]
canon=json.dumps(pairs,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
fp=hashlib.sha256(canon).hexdigest(); assert fp==pm["pair_identity_sha256"]

# Frozen exact row identity is facility + selected CEI date + evaluation identifier.
selected=set()
for p in pairs:
    selected.add((p["id_number"],p["pre_cei_date"],p["pre_evaluation_identifier"]))
    selected.add((p["id_number"],p["post_cei_date"],p["post_evaluation_identifier"]))

zp=TMP/"rcra_downloads.zip"; h=hashlib.sha256(); total=0
req=urllib.request.Request(RCRA_URL,headers={"User-Agent":UA,"Accept":"*/*"})
with urllib.request.urlopen(req,timeout=300) as r,open(zp,"wb") as f:
    while True:
        b=r.read(1024*1024)
        if not b:break
        f.write(b); h.update(b); total+=len(b)
if not zipfile.is_zipfile(zp):raise RuntimeError("RCRA source not ZIP")

rows=defaultdict(list)
with zipfile.ZipFile(zp) as z:
    hits=[n for n in z.namelist() if n.rsplit("/",1)[-1].casefold()=="rcra_evaluations.csv"]
    if len(hits)!=1:raise RuntimeError(f"evaluation member drift: {hits}")
    reader=csv.DictReader(io.TextIOWrapper(z.open(hits[0]),encoding="utf-8-sig",errors="replace",newline=""))
    required={"ID_NUMBER","EVALUATION_IDENTIFIER","EVALUATION_TYPE","EVALUATION_START_DATE","EVALUATION_AGENCY","FOUND_VIOLATION"}
    miss=sorted(required-set(reader.fieldnames or []))
    if miss:raise RuntimeError(f"missing headers: {miss}")
    for r in reader:
        rid=(r.get("ID_NUMBER") or "").strip().upper(); eid=(r.get("EVALUATION_IDENTIFIER") or "").strip(); d=iso_date(r.get("EVALUATION_START_DATE") or "")
        key=(rid,d,eid)
        if key in selected:
            rows[key].append({k:(r.get(k) or "").strip() for k in required})
try:zp.unlink()
except FileNotFoundError:pass

resolved={}
for key in selected:
    rr=[r for r in rows.get(key,[]) if r["EVALUATION_TYPE"].strip().upper()=="CEI"]
    if len(rr)!=1:raise RuntimeError(f"frozen selected row identity drift {key}: {len(rr)}")
    resolved[key]=rr[0]
assert len(resolved)==len(selected)

pre_counts=Counter(); post_counts=Counter(); ct=Counter(); agency_change=0
pre_days=[]; post_days=[]; same_pairs=[]; hazard=defaultdict(Counter)
for p in pairs:
    pre=resolved[(p["id_number"],p["pre_cei_date"],p["pre_evaluation_identifier"])]
    post=resolved[(p["id_number"],p["post_cei_date"],p["post_evaluation_identifier"])]
    a=oc(pre["FOUND_VIOLATION"]); b=oc(post["FOUND_VIOLATION"])
    pre_counts[a]+=1; post_counts[b]+=1
    same=pre["EVALUATION_AGENCY"]==post["EVALUATION_AGENCY"]
    agency_change+=0 if same else 1
    idx=date.fromisoformat(p["index_date"]); pd=date.fromisoformat(p["pre_cei_date"]); qd=date.fromisoformat(p["post_cei_date"])
    pre_days.append((idx-pd).days); post_days.append((qd-idx).days)
    if a in {"Y","N"} and b in {"Y","N"}:
        ct[a+b]+=1; hazard[p["index_incident_type"]][a+b]+=1
        if same:same_pairs.append((a,b))

nn,ny,yn,yy=ct["NN"],ct["NY"],ct["YN"],ct["YY"]
n=nn+ny+yn+yy; disc=ny+yn; pval=exact_p(ny,yn); rd=None if n==0 else (ny-yn)/n
if n<100 or disc<20:gate="HOLD_US_RCRA_E01_INSUFFICIENT_OUTCOME_SUPPORT"
elif rd>=0.05 and pval is not None and pval<0.05:gate="PASS_POSITIVE_MATERIAL_US_RCRA_E01_RELATIONSHIP"
elif rd is not None and 0<rd<0.05 and pval is not None and pval<0.05:gate="POSITIVE_BELOW_MATERIALITY_US_RCRA_E01_RELATIONSHIP"
else:gate="NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP"

sct=Counter(a+b for a,b in same_pairs); sn=sum(sct.values()); sd=sct["NY"]+sct["YN"]
same_diag={"analyzable_pairs":sn,"discordant_pairs":sd}
if sn>=50 and sd>=10:
    same_diag.update({"n_NN":sct["NN"],"n_NY":sct["NY"],"n_YN":sct["YN"],"n_YY":sct["YY"],"risk_difference":(sct["NY"]-sct["YN"])/sn,"p_exact_two_sided":exact_p(sct["NY"],sct["YN"])})

res={
 "id":"US-RCRA-E01-EXECUTION-RESULT","issue":125,"gate":gate,"pair_identity_sha256":fp,
 "pair_count_frozen":297,"state_territory_fips_count_frozen":43,"pair_identity_drift":False,
 "selected_outcomes_opened":True,"relationship_computed":n>=100 and disc>=20,
 "source":{"rcra_url":RCRA_URL,"bytes_transient":total,"sha256":h.hexdigest(),"raw_source_bytes_persisted":False},
 "outcome_coding":{"Y":1,"N":0,"U":"missing","blank_or_other":"missing"},
 "value_counts":{"pre":dict(pre_counts),"post":dict(post_counts)},
 "primary_support":{"analyzable_pairs":n,"discordant_pairs":disc,"minimum_analyzable":100,"minimum_discordant":20},
 "primary":{"n_NN":nn,"n_NY":ny,"n_YN":yn,"n_YY":yy,"pre_risk":None if n==0 else (yy+yn)/n,"post_risk":None if n==0 else (yy+ny)/n,"risk_difference":rd,"p_exact_two_sided_mcnemar":pval,"materiality_floor":0.05},
 "diagnostics_non_rescuing":{"agency_change_pairs":agency_change,"agency_change_fraction":agency_change/297,"same_agency_subset":same_diag,"pre_cei_distance_days":{"min":min(pre_days),"max":max(pre_days),"mean":sum(pre_days)/len(pre_days)},"post_cei_distance_days":{"min":min(post_days),"max":max(post_days),"mean":sum(post_days)/len(post_days)},"hazard_contingencies":{k:dict(v) for k,v in sorted(hazard.items())}},
 "claim_boundary":"non-causal monitoring/compliance association; FOUND_VIOLATION is an inspection-result field",
 "incremental_monetary_cost_usd":0}
(OUT/"EXECUTION_RESULT.json").write_text(json.dumps(res,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"gate":gate,"analyzable":n,"discordant":disc,"RD":rd,"p":pval},indent=2))
