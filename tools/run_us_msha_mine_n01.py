#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, date
from pathlib import Path
from statistics import mean, stdev
import csv, hashlib, io, json, math, os, re, subprocess, tempfile, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-MSHA-MINE-N01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"
COHORT_OUT=OUTDIR/"locked-cohort.csv"

CONTRACT_SHA="1d5f60ac0fca0aa81fad325bfc12e716ef370fec"
ISSUE=178
BASE="https://arlweb.msha.gov/OpenGovernmentData/DataSets/"
URLS={
    "mines": BASE+"Mines.zip",
    "employment": BASE+"MinesProdQuarterly.zip",
    "accidents": BASE+"Accidents.zip",
}
EXPECTED={
    "mines":"3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7",
    "employment":"4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960",
    "accidents":"db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6",
}
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
OPERATING={"Active","Intermittent","NonProducing","Temporarily Idled"}
CUTOFF=date(2026,9,29)
FUTURE_START=date(2026,9,30)
PRIOR_START=date(2025,9,30)
PLAUS_START=date(2026,3,30)

def curl(url,path,timeout=600):
    hp=path.with_suffix(path.suffix+".headers")
    cmd=["curl","-L","--fail","--silent","--show-error","--retry","2",
         "--connect-timeout","20","--max-time",str(timeout),"-A",UA,
         "-D",str(hp),"-o",str(path),url]
    p=subprocess.run(cmd,capture_output=True)
    if p.returncode:
        raise RuntimeError(f"curl rc={p.returncode}:{p.stderr.decode('utf-8','replace')[:500]}")
    b=path.read_bytes()
    h=hp.read_bytes() if hp.exists() else b""
    blocks=[x for x in re.split(br"\r?\n\r?\n",h) if x.startswith(b"HTTP/")]
    final=blocks[-1] if blocks else b""
    status=None; headers={}
    if final:
        lines=final.decode("iso-8859-1","replace").splitlines()
        m=re.match(r"HTTP/\S+\s+(\d+)",lines[0])
        status=int(m.group(1)) if m else None
        for line in lines[1:]:
            if ":" in line:
                k,v=line.split(":",1);headers[k.strip().lower()]=v.strip()
    return {"status":status,"url":url,"bytes":len(b),
            "content_type":headers.get("content-type"),"last_modified":headers.get("last-modified"),
            "etag":headers.get("etag"),"sha256":hashlib.sha256(b).hexdigest()}

def decode_bytes(b):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return b.decode(enc)
        except UnicodeDecodeError:pass
    return b.decode("latin-1")

def choose_member(z):
    files=[x for x in z.infolist() if not x.is_dir()]
    preferred=[x for x in files if x.filename.lower().endswith((".txt",".csv",".dat"))]
    if not (preferred or files): raise RuntimeError("EMPTY_ZIP")
    return max(preferred or files,key=lambda x:x.file_size)

def reader_from_zip(path):
    with zipfile.ZipFile(path) as z:
        member=choose_member(z); raw=z.read(member)
    txt=decode_bytes(raw)
    first=txt.splitlines()[0] if txt.splitlines() else ""
    counts={d:first.count(d) for d in ("|","\t",",",";")}
    delim=max(counts,key=counts.get)
    if counts[delim]==0: raise RuntimeError(f"DELIMITER_NOT_FOUND:{member.filename}")
    rdr=csv.DictReader(io.StringIO(txt),delimiter=delim)
    return rdr, (rdr.fieldnames or []), member.filename, delim

def norm_id(v):
    s=str(v or "").strip()
    return s if re.fullmatch(r"[0-9]{7}",s) else None

def num(v):
    s=str(v or "").strip().replace(",","")
    if not s:return None
    try:
        x=float(s)
        return x if math.isfinite(x) else None
    except ValueError:return None

def pdate(v):
    s=str(v or "").strip()
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y"):
        try:return datetime.strptime(s,f).date()
        except ValueError:pass
    return None

def nh(v): return re.sub(r"[^A-Z0-9]+","",str(v or "").upper())
def getcol(headers,*names):
    km={nh(h):h for h in headers}
    for n in names:
        if nh(n) in km:return km[nh(n)]
    return None

def smd(a,b):
    if not a or not b:return float("inf")
    ma,mb=mean(a),mean(b)
    va=stdev(a)**2 if len(a)>1 else 0.0
    vb=stdev(b)**2 if len(b)>1 else 0.0
    pooled=math.sqrt((va+vb)/2.0)
    if pooled==0:return 0.0 if ma==mb else float("inf")
    return (ma-mb)/pooled

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    for p in (JSON_OUT,MD_OUT,COHORT_OUT):
        if p.exists():raise RuntimeError(f"immutable evidence exists:{p.name}")
    ev={
        "research":"US-MSHA-MINE-N01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_serious_fatal_event_membership_opened":False,"future_rows_opened":0,
        "future_relationship_computed":False,"future_rr_computed":False,"future_rd_computed":False,
        "future_pvalue_computed":False,"ranking_computed":False,"causal_claim_made":False,
        "operator_controller_name_address_fuzzy_geo_manual_repair_used":False,"gates":[]
    }
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20260929-US-MSHA-MINE-N01-ACTIVE"
            and cp.get("active_issue")==178 and cp.get("active_research")=="US-MSHA-MINE-N01"
            and cp.get("last_decision")=="DEC-266")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=(os.environ.get("MSHA_N01_BOUND")=="1"
               and os.environ.get("MSHA_N01_CONTRACT_SHA")==CONTRACT_SHA)
        ev["gates"].append({"gate":2,"pass":bound,
                            "observed":{"issue":ISSUE,"contract_sha":os.environ.get("MSHA_N01_CONTRACT_SHA")}})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0); paths={}; metas={}
            for k,u in URLS.items():
                p=td/f"{k}.zip"; metas[k]=curl(u,p); paths[k]=p
            fp={k:v["sha256"] for k,v in metas.items()}
            g3=(fp==EXPECTED and all(metas[k].get("status")==200 for k in EXPECTED))
            ev["source_fingerprints"]=fp
            ev["gates"].append({"gate":3,"pass":g3,
                                "observed":{"actual":fp,"expected":EXPECTED,
                                            "http":{k:metas[k].get("status") for k in metas}}})
            if not g3:
                raise RuntimeError("FROZEN_BASELINE_FINGERPRINT_MISMATCH")

            # Mines
            mr,mh,mmember,mdelim=reader_from_zip(paths["mines"])
            midc=getcol(mh,"MINE_ID"); statc=getcol(mh,"CURRENT_MINE_STATUS")
            statec=getcol(mh,"STATE"); cmc=getcol(mh,"COAL_METAL_IND"); typec=getcol(mh,"CURRENT_MINE_TYPE")
            # Employment
            er,eh,emember,edelim=reader_from_zip(paths["employment"])
            emid=getcol(eh,"MINE_ID"); ey=getcol(eh,"CAL_YR"); eq=getcol(eh,"CAL_QTR")
            eemp=getcol(eh,"AVG_EMPLOYEE_CNT"); ehrs=getcol(eh,"HOURS_WORKED")
            # Accidents
            ar,ah,amember,adelim=reader_from_zip(paths["accidents"])
            amid=getcol(ah,"MINE_ID"); adt=getcol(ah,"ACCIDENT_DT")
            adeg=getcol(ah,"DEGREE_INJURY_CD"); aimm=getcol(ah,"IMMED_NOTIFY_CD")
            schema_ok=all(x is not None for x in
                          (midc,statc,statec,cmc,typec,emid,ey,eq,eemp,ehrs,amid,adt,adeg,aimm))
            ev["gates"].append({"gate":4,"pass":schema_ok,
                                "observed":{"mines_member":mmember,"mines_delimiter":mdelim,"mines_headers":mh,
                                            "employment_member":emember,"employment_delimiter":edelim,"employment_headers":eh,
                                            "accidents_member":amember,"accidents_delimiter":adelim,"accidents_headers":ah}})
            if not schema_ok: raise RuntimeError("REQUIRED_SCHEMA_MISSING")

            mine_meta={}
            for r in mr:
                mid=norm_id(r.get(midc,""))
                if not mid:continue
                st=str(r.get(statc,"")).strip()
                if st not in OPERATING:continue
                state=str(r.get(statec,"")).strip()
                cm=str(r.get(cmc,"")).strip()
                mt=str(r.get(typec,"")).strip()
                if not state or not cm or not mt:continue
                mine_meta[mid]={"state":state,"coal_metal":cm,"mine_type":mt,"status":st}

            # Q1/Q2 aggregate
            agg=defaultdict(lambda:{1:{"emp":0.0,"hours":0.0,"rows":0},2:{"emp":0.0,"hours":0.0,"rows":0}})
            for r in er:
                mid=norm_id(r.get(emid,""))
                if not mid or mid not in mine_meta:continue
                try:y=int(float(str(r.get(ey,"")).strip())); q=int(float(str(r.get(eq,"")).strip()))
                except Exception:continue
                if y!=2026 or q not in (1,2):continue
                emp=num(r.get(eemp)); hrs=num(r.get(ehrs))
                if emp is None or hrs is None:continue
                agg[mid][q]["emp"]+=emp;agg[mid][q]["hours"]+=hrs;agg[mid][q]["rows"]+=1

            eligible={}
            for mid,meta in mine_meta.items():
                a=agg.get(mid)
                if not a:continue
                q1,q2=a[1],a[2]
                if q1["rows"]<1 or q2["rows"]<1:continue
                if q1["emp"]<3 or q2["emp"]<3 or q1["hours"]<500 or q2["hours"]<500:continue
                i1=q1["hours"]/q1["emp"]; i2=q2["hours"]/q2["emp"]
                if not (math.isfinite(i1) and math.isfinite(i2) and i1>0 and i2>0):continue
                eligible[mid]={**meta,
                    "emp_q1":q1["emp"],"emp_q2":q2["emp"],
                    "hours_q1":q1["hours"],"hours_q2":q2["hours"],
                    "intensity_q1":i1,"intensity_q2":i2,
                    "ramp":math.log(i2/i1),
                    "x1":math.log1p(q1["hours"]),
                    "x2":math.log1p(q1["emp"]),
                    "x3":math.log(i1),
                    "prior_severe":0,
                }
            ev["gates"].append({"gate":5,"pass":len(eligible)>=5000,
                                "observed":{"eligible_mines":len(eligible),"threshold":5000}})

            # Pre-outcome severe history only. Rows on/after future start are not severity-inspected.
            plausible_mines=set(); prior_mines=set(); future_rows_seen=0
            for r in ar:
                d=pdate(r.get(adt,""))
                if not d:continue
                if d>=FUTURE_START:
                    future_rows_seen+=1
                    continue
                if d>CUTOFF:continue
                mid=norm_id(r.get(amid,""))
                if not mid:continue
                deg=str(r.get(adeg,"")).strip().zfill(2)
                imm=str(r.get(aimm,"")).strip().zfill(2)
                severe=(deg in {"01","02"} or imm in {"01","02"})
                if not severe:continue
                if PRIOR_START<=d<=CUTOFF:prior_mines.add(mid)
                if PLAUS_START<=d<=CUTOFF and mid in eligible:plausible_mines.add(mid)
            for mid in eligible:
                eligible[mid]["prior_severe"]=1 if mid in prior_mines else 0
            ev["future_rows_seen_sealed"]=future_rows_seen
            ev["gates"].append({"gate":9,"pass":True,
                                "observed":{"prior_window_start":PRIOR_START.isoformat(),
                                            "prior_window_end":CUTOFF.isoformat(),
                                            "distinct_prior_severe_mines":len(prior_mines),
                                            "construction":"pre-cutoff frozen rows only; Degree 01/02 or Immediate 01/02"}})

            # Exposure groups
            rank_strata=defaultdict(list)
            for mid,d in eligible.items():
                rank_strata[(d["coal_metal"],d["mine_type"])].append(mid)
            qualifying={k:v for k,v in rank_strata.items() if len(v)>=40}
            ev["gates"].append({"gate":6,"pass":len(qualifying)>=8,
                                "observed":{"qualifying_strata":len(qualifying),"threshold":8,
                                            "strata_sizes":{"|".join(k):len(v) for k,v in sorted(qualifying.items())}}})
            exposed=[]; controls=[]
            group={}
            for k,mids in qualifying.items():
                ordered=sorted(mids,key=lambda m:(eligible[m]["ramp"],m))
                n=len(ordered)
                q25=math.ceil(0.25*n);q75=math.ceil(0.75*n)
                for pos,mid in enumerate(ordered,1):
                    if pos>q75:
                        group[mid]="RAMP_UP";exposed.append(mid)
                    elif q25<pos<=q75:
                        group[mid]="MODERATE_CHANGE";controls.append(mid)
            ev["gates"].append({"gate":7,"pass":len(exposed)>=1000,
                                "observed":{"ramp_up_mines":len(exposed),"threshold":1000}})
            ev["gates"].append({"gate":8,"pass":len(controls)>=2000,
                                "observed":{"comparator_mines":len(controls),"threshold":2000}})

            # Standardize across complete eligible cohort
            zparams={}
            for x in ("x1","x2","x3"):
                vals=[d[x] for d in eligible.values()]
                mu=mean(vals); sd=stdev(vals)
                if sd<=0:raise RuntimeError(f"ZERO_SD:{x}")
                zparams[x]=(mu,sd)
                for d in eligible.values():d["z_"+x]=(d[x]-mu)/sd

            # Pools by exact matching stratum
            pools=defaultdict(list)
            for mid in controls:
                d=eligible[mid]
                key=(d["state"],d["coal_metal"],d["mine_type"],d["prior_severe"])
                pools[key].append(mid)
            for k in pools:pools[k].sort()
            used=set();pairs=[]
            for eid in sorted(exposed):
                e=eligible[eid]
                key=(e["state"],e["coal_metal"],e["mine_type"],e["prior_severe"])
                best=None
                for cid in pools.get(key,[]):
                    if cid in used:continue
                    c=eligible[cid]
                    diffs=[abs(e["z_"+x]-c["z_"+x]) for x in ("x1","x2","x3")]
                    if any(x>0.50 for x in diffs):continue
                    dist=sum(x*x for x in diffs)
                    cand=(dist,cid)
                    if best is None or cand<best:best=cand
                if best:
                    cid=best[1];used.add(cid)
                    pairs.append((eid,cid,best[0]))
            coverage=len(pairs)/len(exposed) if exposed else 0.0
            ev["gates"].append({"gate":10,"pass":len(pairs)>=800,
                                "observed":{"matched_pairs":len(pairs),"threshold":800}})
            ev["gates"].append({"gate":11,"pass":coverage>=0.60,
                                "observed":{"exposed":len(exposed),"matched_pairs":len(pairs),
                                            "coverage":coverage,"threshold":0.60}})

            exids=[a for a,b,d in pairs];coids=[b for a,b,d in pairs]
            smds={}
            for x,gate_no in (("x1",12),("x2",13),("x3",14)):
                s=smd([eligible[m][x] for m in exids],[eligible[m][x] for m in coids])
                smds[x]=s
                ev["gates"].append({"gate":gate_no,"pass":abs(s)<=0.10,
                                    "observed":{"smd":s,"abs_smd":abs(s),"threshold":0.10}})
            ev["gates"].append({"gate":15,"pass":len(plausible_mines)>=40,
                                "observed":{"historical_plausibility_window":[PLAUS_START.isoformat(),CUTOFF.isoformat()],
                                            "distinct_eligible_serious_fatal_mines":len(plausible_mines),"threshold":40}})
            ev["gates"].append({"gate":16,"pass":ev["future_serious_fatal_event_membership_opened"] is False,
                                "observed":{"future_rows_seen_but_severity_not_used":future_rows_seen,
                                            "future_membership_opened":False}})
            g17=(not ev["future_relationship_computed"] and not ev["future_rr_computed"] and
                 not ev["future_rd_computed"] and not ev["future_pvalue_computed"] and
                 not ev["ranking_computed"] and not ev["causal_claim_made"] and
                 not ev["operator_controller_name_address_fuzzy_geo_manual_repair_used"])
            ev["gates"].append({"gate":17,"pass":g17,
                                "observed":{"future_relationship":False,"future_rr":False,"future_rd":False,
                                            "future_pvalue":False,"ranking":False,"causal":False,"identity_repair":False}})
            g18=(ev["source_fingerprints"]==EXPECTED and
                 re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and
                 ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":g18,
                                "observed":{"source_sha256":ev["source_fingerprints"],
                                            "runner_sha256":ev["runner_sha256"],
                                            "contract_sha":CONTRACT_SHA,"cost_usd":0}})

            # Persist locked pair cohort; no future outcomes.
            with COHORT_OUT.open("w",newline="",encoding="utf-8") as fh:
                w=csv.writer(fh)
                w.writerow(["pair_id","ramp_up_mine_id","comparator_mine_id",
                            "state","coal_metal_ind","mine_type","prior_severe_12m",
                            "ramp_up_ramp","comparator_ramp",
                            "ramp_up_hours_q1","comparator_hours_q1",
                            "ramp_up_emp_q1","comparator_emp_q1",
                            "ramp_up_intensity_q1","comparator_intensity_q1",
                            "distance_sq"])
                for i,(eid,cid,dist) in enumerate(pairs,1):
                    e,c=eligible[eid],eligible[cid]
                    w.writerow([i,eid,cid,e["state"],e["coal_metal"],e["mine_type"],e["prior_severe"],
                                f'{e["ramp"]:.12g}',f'{c["ramp"]:.12g}',
                                f'{e["hours_q1"]:.12g}',f'{c["hours_q1"]:.12g}',
                                f'{e["emp_q1"]:.12g}',f'{c["emp_q1"]:.12g}',
                                f'{e["intensity_q1"]:.12g}',f'{c["intensity_q1"]:.12g}',
                                f'{dist:.12g}'])
            ev["locked_cohort_sha256"]=hashlib.sha256(COHORT_OUT.read_bytes()).hexdigest()
            ev["locked_cohort_pairs"]=len(pairs)
            ev["exposure_support"]={"eligible":len(eligible),"qualifying_strata":len(qualifying),
                                    "ramp_up":len(exposed),"comparators":len(controls),"matched_pairs":len(pairs),
                                    "match_coverage":coverage,"smd":smds,
                                    "historical_plausibility_mines":len(plausible_mines)}

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
        ev["attempt_valid"]=True;ev["pass_count"]=18-len(failed);ev["failed_gates"]=failed
        ev["disposition"]=("PASS_US_MSHA_MINE_N01_PROSPECTIVE_COHORT_LOCKED"
                            if not failed else "HOLD_US_MSHA_MINE_N01_PROSPECTIVE_DESIGN_NOT_READY")
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_MSHA_MINE_N01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-MSHA-MINE-N01 — Baseline Attempt 01","",
           f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",
           f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",
           f"- Future membership opened: **{ev['future_serious_fatal_event_membership_opened']}**",
           f"- Locked cohort pairs: **{ev.get('locked_cohort_pairs',0)}**",
           f"- Cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in ev["gates"]:
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1200:o=o[:1197]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):
        lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No post-2026-09-29 serious/fatal event membership or future relationship statistic was opened/computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"),ev.get("locked_cohort_pairs"))

if __name__=="__main__":
    main()
