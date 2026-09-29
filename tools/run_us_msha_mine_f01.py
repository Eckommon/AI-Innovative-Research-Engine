#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter
from datetime import datetime,date
from pathlib import Path
import csv, hashlib, io, json, os, re, subprocess, tempfile, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-MSHA-MINE-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"; MD_OUT=OUTDIR/"attempt-01.md"
CONTRACT_SHA="18a90079c3566641bc3856f7d802acdc75b53388"; ISSUE=177
BASE="https://arlweb.msha.gov/OpenGovernmentData/DataSets/"
PORTAL="https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp"
MDRS="https://www.msha.gov/mine-data-retrieval-system"
URLS={
 "mines":BASE+"Mines.zip",
 "employment":BASE+"MinesProdQuarterly.zip",
 "accidents":BASE+"Accidents.zip",
 "mines_def":BASE+"Mines_Definition_File.txt",
 "employment_def":BASE+"MineSProdQuarterly_Definition_File.txt",
 "accidents_def":BASE+"Accidents_Definition_File.txt",
}
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
CUTOFF=date(2026,9,29); FUTURE_START=date(2026,9,30)
OPERATING={"Active","Intermittent","NonProducing","Temporarily Idled"}

def curl(url,path,timeout=300):
    hp=path.with_suffix(path.suffix+".headers")
    cmd=["curl","-L","--fail","--silent","--show-error","--retry","2","--connect-timeout","20","--max-time",str(timeout),"-A",UA,"-D",str(hp),"-o",str(path),url]
    p=subprocess.run(cmd,capture_output=True)
    if p.returncode: raise RuntimeError(f"curl rc={p.returncode}:{p.stderr.decode('utf-8','replace')[:500]}")
    b=path.read_bytes(); h=hp.read_bytes() if hp.exists() else b""
    blocks=[x for x in re.split(br"\r?\n\r?\n",h) if x.startswith(b"HTTP/")]
    final=blocks[-1] if blocks else b""; status=None; headers={}
    if final:
        lines=final.decode("iso-8859-1","replace").splitlines()
        m=re.match(r"HTTP/\S+\s+(\d+)",lines[0]);status=int(m.group(1)) if m else None
        for line in lines[1:]:
            if ":" in line:
                k,v=line.split(":",1);headers[k.strip().lower()]=v.strip()
    return {"status":status,"url":url,"bytes":len(b),"content_type":headers.get("content-type"),"last_modified":headers.get("last-modified"),"etag":headers.get("etag"),"sha256":hashlib.sha256(b).hexdigest()}

def text_url(url):
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"x";m=curl(url,p,120)
        return p.read_text("utf-8",errors="replace"),m

def norm_id(v):
    s=str(v or "").strip()
    return s if re.fullmatch(r"[0-9]{7}",s) else None

def pdate(v):
    s=str(v or "").strip()
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y"):
        try:return datetime.strptime(s,f).date()
        except ValueError:pass
    return None

def decode_bytes(b):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return b.decode(enc)
        except UnicodeDecodeError:pass
    return b.decode("latin-1")

def choose_member(z):
    files=[x for x in z.infolist() if not x.is_dir()]
    if not files: raise RuntimeError("EMPTY_ZIP")
    preferred=[x for x in files if x.filename.lower().endswith((".txt",".csv",".dat"))]
    return max(preferred or files,key=lambda x:x.file_size)

def rows_from_zip(path):
    with zipfile.ZipFile(path) as z:
        member=choose_member(z)
        raw=z.read(member)
    txt=decode_bytes(raw)
    first=txt.splitlines()[0] if txt.splitlines() else ""
    counts={d:first.count(d) for d in ("|","\t",",",";")}
    delim=max(counts,key=counts.get)
    if counts[delim]==0: raise RuntimeError(f"DELIMITER_NOT_FOUND:{member.filename}")
    reader=csv.DictReader(io.StringIO(txt),delimiter=delim)
    headers=reader.fieldnames or []
    return headers,reader,member.filename,delim

def keymap(headers):
    return {re.sub(r"[^A-Z0-9]+","",str(h or "").upper()):h for h in headers}

def getcol(km,*names):
    for n in names:
        x=re.sub(r"[^A-Z0-9]+","",n.upper())
        if x in km:return km[x]
    return None

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists(): raise RuntimeError("immutable attempt-01 exists")
    ev={"research":"US-MSHA-MINE-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_rows_seen":0,"future_serious_fatal_event_membership_opened":False,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,"causal_claim_made":False,
        "operator_controller_name_address_fuzzy_geo_manual_repair_used":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=cp.get("checkpoint_id")=="CHK-20260929-US-MSHA-MINE-F01-ACTIVE" and cp.get("active_issue")==177 and cp.get("last_decision")=="DEC-264"
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("MSHA_F01_BOUND")=="1" and os.environ.get("MSHA_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":177,"contract_sha":os.environ.get("MSHA_F01_CONTRACT_SHA")}})
        docs={};defs={}
        for k,u in {"portal":PORTAL,"mdrs":MDRS,"mines_def":URLS["mines_def"],"employment_def":URLS["employment_def"],"accidents_def":URLS["accidents_def"]}.items():
            t,m=text_url(u);docs[k]=m;defs[k]=t
        g3=all(x.get("status")==200 for x in docs.values())
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})
        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0); metas={}; paths={}
            for k in ("mines","employment","accidents"):
                p=td/f"{k}.zip";metas[k]=curl(URLS[k],p,600);paths[k]=p
            g4=all(metas[k].get("status")==200 and zipfile.is_zipfile(paths[k]) for k in paths)
            ev["gates"].append({"gate":4,"pass":g4,"observed":metas})
            ev["source_fingerprints"]={k:v["sha256"] for k,v in metas.items()}

            # Mines
            mh,mr,mmember,mdelim=rows_from_zip(paths["mines"]); mkm=keymap(mh)
            midc=getcol(mkm,"MINE_ID"); statc=getcol(mkm,"CURRENT_MINE_STATUS"); sdtc=getcol(mkm,"CURRENT_STATUS_DT")
            typec=getcol(mkm,"CURRENT_MINE_TYPE"); statec=getcol(mkm,"STATE")
            g5=all(x is not None for x in (midc,statc,sdtc,typec,statec))
            all_ids=set(); operating=set(); nonblank=valid=0; status_counts=Counter(); mine_rows=0
            for r in mr:
                mine_rows+=1; raw=r.get(midc,"") if midc else ""
                if str(raw).strip():nonblank+=1
                mid=norm_id(raw)
                if not mid:continue
                valid+=1;all_ids.add(mid)
                st=str(r.get(statc,"")).strip() if statc else "";status_counts[st]+=1
                if st in OPERATING:operating.add(mid)
            ev["gates"].append({"gate":5,"pass":g5,"observed":{"member":mmember,"delimiter":mdelim,"headers":mh,"rows":mine_rows,"status_counts":dict(status_counts)}})
            rate=valid/nonblank if nonblank else 0
            ev["gates"].append({"gate":6,"pass":rate>=0.999,"observed":{"valid":valid,"nonblank":nonblank,"rate":rate,"threshold":0.999}})
            ev["gates"].append({"gate":7,"pass":len(all_ids)>=50000,"observed":{"distinct_mine_ids":len(all_ids),"threshold":50000}})
            ev["gates"].append({"gate":8,"pass":len(operating)>=10000,"observed":{"operating_ids":len(operating),"threshold":10000}})

            # Employment Q1/Q2 2026
            eh,er,emember,edelim=rows_from_zip(paths["employment"]); ekm=keymap(eh)
            emid=getcol(ekm,"MINE_ID"); ey=getcol(ekm,"CAL_YR"); eq=getcol(ekm,"CAL_QTR"); esub=getcol(ekm,"SUBUNIT_CD")
            eavg=getcol(ekm,"AVG_EMPLOYEE_CNT"); ehours=getcol(ekm,"HOURS_WORKED")
            g9=all(x is not None for x in (emid,ey,eq,esub,eavg,ehours))
            emp_ids=set(); emp_rows=0
            for r in er:
                try:y=int(float(str(r.get(ey,"")).strip()));q=int(float(str(r.get(eq,"")).strip()))
                except Exception:continue
                if y!=2026 or q not in (1,2):continue
                emp_rows+=1;mid=norm_id(r.get(emid,""))
                if mid:emp_ids.add(mid)
            ev["gates"].append({"gate":9,"pass":g9,"observed":{"member":emember,"delimiter":edelim,"headers":eh,"frozen_rows":emp_rows}})
            ev["gates"].append({"gate":10,"pass":len(emp_ids)>=8000,"observed":{"distinct_q1q2_ids":len(emp_ids),"threshold":8000}})
            cov=len(emp_ids&all_ids)/len(emp_ids) if emp_ids else 0
            ev["gates"].append({"gate":11,"pass":cov>=0.99,"observed":{"employment_ids":len(emp_ids),"exact_matches":len(emp_ids&all_ids),"rate":cov,"threshold":0.99}})

            # Accidents
            ah,ar,amember,adelim=rows_from_zip(paths["accidents"]); akm=keymap(ah)
            amid=getcol(akm,"MINE_ID"); docc=getcol(akm,"DOCUMENT_NO"); dtc=getcol(akm,"ACCIDENT_DT")
            degc=getcol(akm,"DEGREE_INJURY_CD"); immc=getcol(akm,"IMMED_NOTIFY_CD"); ay=getcol(akm,"CAL_YR"); aq=getcol(akm,"CAL_QTR")
            g12=all(x is not None for x in (amid,docc,dtc,degc,immc,ay,aq))
            hist_acc_ids=set(); severe_docs=set(); severe_mines=set(); severe_rows=0; severe_integrity=0; pre_rows=0
            for r in ar:
                d=pdate(r.get(dtc,"")) if dtc else None
                if d and d>=FUTURE_START:
                    ev["future_rows_seen"]+=1
                    continue
                if not d or d>CUTOFF:continue
                pre_rows+=1;mid=norm_id(r.get(amid,""))
                if mid:hist_acc_ids.add(mid)
                deg=str(r.get(degc,"")).strip().zfill(2) if degc else ""
                imm=str(r.get(immc,"")).strip().zfill(2) if immc else ""
                qual=(deg in {"01","02"} or imm in {"01","02"})
                if qual:
                    severe_rows+=1
                    doc=str(r.get(docc,"")).strip()
                    if doc:severe_docs.add(doc)
                    if mid:severe_mines.add(mid)
                    if d and mid and qual:severe_integrity+=1
            ev["gates"].append({"gate":12,"pass":g12,"observed":{"member":amember,"delimiter":adelim,"headers":ah,"historical_rows":pre_rows}})
            acov=len(hist_acc_ids&all_ids)/len(hist_acc_ids) if hist_acc_ids else 0
            ev["gates"].append({"gate":13,"pass":acov>=0.99,"observed":{"historical_accident_mine_ids":len(hist_acc_ids),"exact_matches":len(hist_acc_ids&all_ids),"rate":acov,"threshold":0.99}})
            g14=len(severe_docs)>=1000 and len(severe_mines)>=500
            ev["gates"].append({"gate":14,"pass":g14,"observed":{"distinct_serious_fatal_documents":len(severe_docs),"distinct_mines":len(severe_mines),"threshold_documents":1000,"threshold_mines":500}})
            sir=severe_integrity/severe_rows if severe_rows else 0
            ev["gates"].append({"gate":15,"pass":sir>=0.99,"observed":{"severe_rows":severe_rows,"integrity_rows":severe_integrity,"rate":sir,"threshold":0.99}})
            ad=defs["accidents_def"]
            g16=all(x in ad for x in ("01) Fatality","02) Permanent total or permanent partial disability","(01) Death","(02) Serious injury"))
            ev["gates"].append({"gate":16,"pass":g16,"observed":{"degree_fatal":("01) Fatality" in ad),"degree_permanent":("02) Permanent total or permanent partial disability" in ad),"immediate_death":("(01) Death" in ad),"immediate_serious":("(02) Serious injury" in ad)}})
            g17=(ev["future_serious_fatal_event_membership_opened"] is False and not ev["relationship_computed"] and not ev["prediction_computed"] and not ev["ranking_computed"] and not ev["causal_claim_made"] and not ev["operator_controller_name_address_fuzzy_geo_manual_repair_used"])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{"future_rows_seen_sealed":ev["future_rows_seen"],"future_membership_opened":False,"relationship":False,"prediction":False,"ranking":False,"causal":False,"identity_repair":False}})
            g18=len(ev["source_fingerprints"])==3 and all(re.fullmatch(r"[0-9a-f]{64}",x) for x in ev["source_fingerprints"].values()) and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0
            ev["gates"].append({"gate":18,"pass":g18,"observed":{"source_sha256":ev["source_fingerprints"],"runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})
        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
        ev["attempt_valid"]=True;ev["pass_count"]=18-len(failed);ev["failed_gates"]=failed
        ev["disposition"]="PASS_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_READY" if not failed else "HOLD_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_MSHA_MINE_F01_ATTEMPT_01"
    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n")
    lines=["# US-MSHA-MINE-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future rows seen but sealed: **{ev['future_rows_seen']}**",f"- Future serious/fatal membership opened: **{ev['future_serious_fatal_event_membership_opened']}**",f"- Cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in ev["gates"]:
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1200:o=o[:1197]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No post-2026-09-29 serious/fatal event membership was opened.",""]
    MD_OUT.write_text("\n".join(lines))
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))
if __name__=="__main__":main()
