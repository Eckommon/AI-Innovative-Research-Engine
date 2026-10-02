#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv, hashlib, io, json, os, re, tempfile, zipfile, subprocess

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-PHMSA-PIPE-F01/evidence"
JSON_OUT=OUTDIR/"attempt-02.json"
MD_OUT=OUTDIR/"attempt-02.md"
CONTRACT_SHA="42e8195cf0749a48f73039729a991352c201efc7"
ISSUE=190
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"

ANNUAL_PAGE="https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids"
INCIDENT_PAGE="https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data"
SOURCE_PAGE="https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data"
OPID_PAGE="https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids"
ANNUAL_INSTR="https://www.phmsa.dot.gov/forms/gas-transmission-and-gathering-annual-report-instructions-f-71002-1"
INCIDENT_INSTR="https://www.phmsa.dot.gov/forms/gas-transmission-gathering-and-ungs-incident-report-instructions-f-71002-1"

ANNUAL_ZIP="https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/data_statistics/pipeline/annual_gas_transmission_gathering_2010_present.zip"
INCIDENT_ZIP="https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/data_statistics/pipeline/incident_gas_transmission_gathering_jan2010_present.zip"
YEARS=list(range(2018,2026))

csv.field_size_limit(1024*1024*128)

def norm(s):
    return re.sub(r"[^a-z0-9]+","",str(s or "").strip().lower())

def opid(v):
    s=str(v or "").strip()
    return s if re.fullmatch(r"[0-9]+",s) else None

def parse_num(v):
    s=str(v or "").strip().replace(",","")
    if not s: return None
    try: return float(s)
    except ValueError: return None

def parse_date(v):
    s=str(v or "").strip()
    if not s: return None
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y","%m/%d/%Y %H:%M:%S","%Y-%m-%d %H:%M:%S"):
        try:return datetime.strptime(s,f)
        except ValueError:pass
    return None

def sha_bytes(b): return hashlib.sha256(b).hexdigest()

def _parse_headers(path:Path):
    blocks=[];cur={}
    for line in path.read_text("latin-1",errors="replace").splitlines():
        if line.startswith("HTTP/"):
            if cur: blocks.append(cur)
            parts=line.split()
            cur={"status":int(parts[1]) if len(parts)>1 and parts[1].isdigit() else None}
        elif ":" in line:
            k,v=line.split(":",1);cur[k.strip().lower()]=v.strip()
    if cur: blocks.append(cur)
    return blocks[-1] if blocks else {}

def _curl(url:str,out:Path,referer:str|None=None,timeout=600):
    hdr=out.with_suffix(out.suffix+".headers")
    cmd=["curl","--fail","--silent","--show-error","--location","--http1.1",
         "--connect-timeout","30","--max-time",str(timeout),
         "-A",UA,"-H","Accept: text/html,application/xhtml+xml,application/zip,application/octet-stream,*/*;q=0.8",
         "-H","Accept-Language: en-US,en;q=0.9",
         "-D",str(hdr),"-o",str(out)]
    if referer: cmd += ["-e",referer]
    cmd += [url]
    cp=subprocess.run(cmd,capture_output=True,text=True)
    if cp.returncode!=0:
        raise RuntimeError(f"CURL_FAILED[{cp.returncode}]:{url}:{cp.stderr.strip()[:1000]}")
    h=_parse_headers(hdr)
    if not out.exists():
        raise RuntimeError(f"CURL_NO_BODY:{url}")
    return h

def fetch_meta(url, timeout=120):
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/"body"
        h=_curl(url,p,referer=SOURCE_PAGE if url!=SOURCE_PAGE else None,timeout=timeout)
        b=p.read_bytes()
        return {"status":h.get("status"),"requested_url":url,"final_url":url,
                "content_type":h.get("content-type"),"last_modified":h.get("last-modified"),
                "etag":h.get("etag"),"bytes":len(b),"sha256":sha_bytes(b),
                "transport":"curl-http1.1-browser-headers"}

def download(url,path,timeout=600):
    ref=ANNUAL_PAGE if url==ANNUAL_ZIP else INCIDENT_PAGE if url==INCIDENT_ZIP else SOURCE_PAGE
    h=_curl(url,path,referer=ref,timeout=timeout)
    bsha=hashlib.sha256()
    n=0
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            bsha.update(chunk);n+=len(chunk)
    return {"status":h.get("status"),"requested_url":url,"final_url":url,
            "content_type":h.get("content-type"),"last_modified":h.get("last-modified"),
            "etag":h.get("etag"),"content_length_header":h.get("content-length"),
            "bytes":n,"sha256":bsha.hexdigest(),"transport":"curl-http1.1-browser-headers"}

def decode_member(zf,name):
    b=zf.read(name)
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return b.decode(enc),b
        except UnicodeDecodeError:pass
    return b.decode("latin-1",errors="replace"),b

def rows_from_text(text):
    lines=text.splitlines()
    if not lines:return [],[]
    sample="\n".join(lines[:5])
    delim="\t" if sample.count("\t")>=sample.count(",") else ","
    rdr=csv.reader(lines,delimiter=delim)
    arr=list(rdr)
    if not arr:return [],[]
    headers=[str(x or "").strip() for x in arr[0]]
    return headers,arr[1:]

def find_col(headers, predicates):
    ns=[norm(h) for h in headers]
    for pred in predicates:
        for i,h in enumerate(ns):
            if pred(h): return i
    return None

def rowv(row,i):
    return row[i] if i is not None and i<len(row) else ""

def choose_year_member(zf,year):
    candidates=[]
    for info in zf.infolist():
        n=info.filename
        base=Path(n).name.lower()
        if info.is_dir() or str(year) not in base: continue
        if not (base.endswith(".txt") or base.endswith(".csv")): continue
        candidates.append((info.file_size,n))
    if not candidates:return None
    return max(candidates)[1]

def choose_incident_data(zf):
    candidates=[]
    for info in zf.infolist():
        if info.is_dir():continue
        base=Path(info.filename).name.lower()
        if not (base.endswith(".txt") or base.endswith(".csv")):continue
        penalty=1 if any(x in base for x in ("field","desc","readme","layout")) else 0
        candidates.append((penalty,-info.file_size,info.filename))
    if not candidates:return None
    candidates.sort()
    return candidates[0][2]

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-02 evidence exists")
    started=datetime.now(timezone.utc).isoformat()
    ev={"research":"US-PHMSA-PIPE-F01","attempt":2,"issue":ISSUE,"contract_sha":CONTRACT_SHA,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"runner_start_utc":started,
        "incremental_monetary_cost_usd":0,"later_incident_refresh_opened":False,
        "future_incident_membership_opened":False,"future_entity_rows_consumed":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
        "causal_claim_made":False,"prohibited_incident_enforcement_exposure_computed":False,
        "identity_repair_used":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261002-US-PHMSA-PIPE-F01-ACTIVE" and cp.get("active_issue")==190
            and cp.get("active_research")=="US-PHMSA-PIPE-F01" and cp.get("last_decision")=="DEC-292")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("PHMSA_PIPE_F01_BOUND")=="1" and os.environ.get("PHMSA_PIPE_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":190,"contract_sha":os.environ.get("PHMSA_PIPE_F01_CONTRACT_SHA")}})

        docs={}
        for k,u in {"source":SOURCE_PAGE,"annual":ANNUAL_PAGE,"incident":INCIDENT_PAGE,"opid":OPID_PAGE,"annual_instr":ANNUAL_INSTR,"incident_instr":INCIDENT_INSTR}.items():
            try:docs[k]=fetch_meta(u,120)
            except Exception as e:docs[k]={"error":f"{type(e).__name__}:{e}","requested_url":u}
        g3=all(docs.get(k,{}).get("status")==200 for k in docs)
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0);ap=td/"annual.zip";ip=td/"incident.zip"
            ameta=download(ANNUAL_ZIP,ap);imeta=download(INCIDENT_ZIP,ip)
            ev["annual_zip"]=ameta;ev["incident_zip"]=imeta
            try:
                az=zipfile.ZipFile(ap); annual_bad=az.testzip()
            except Exception as e:
                raise RuntimeError(f"ANNUAL_ZIP_PARSE:{e}")
            annual_profiles={};opids_by_year={};qualified_by_year={}
            years_ok=True; schemas_ok=True; support_ok=True
            annual_exact_nonblank=annual_exact_valid=0
            selected_struct_groups=None
            completeness_2025={"rows":0,"mileage":0,"additional":0}
            for y in YEARS:
                m=choose_year_member(az,y)
                if not m:
                    years_ok=False;annual_profiles[str(y)]={"member":None};continue
                text,b=decode_member(az,m)
                headers,rows=rows_from_text(text)
                ns=[norm(h) for h in headers]
                opi=find_col(headers,[lambda h:"operatorid" in h,lambda h:h in {"opid","operatornumber"}])
                # deterministically find transmission-mileage concepts
                mile_cols=[i for i,h in enumerate(ns) if "transmission" in h and ("mile" in h or "mileage" in h)]
                type_cols=[i for i,h in enumerate(ns) if h in {"systemtype","facilitytype","pipelinetype","formtype"} or ("system" in h and "type" in h)]
                groups={
                    "material":[i for i,h in enumerate(ns) if any(k in h for k in ("material","steel","plastic"))],
                    "vintage":[i for i,h in enumerate(ns) if any(k in h for k in ("install","vintage","decade"))],
                    "commodity":[i for i,h in enumerate(ns) if any(k in h for k in ("commodity","gasproduct","product"))],
                    "facility":[i for i,h in enumerate(ns) if any(k in h for k in ("compressor","storagefield","facility","station"))],
                }
                available=[k for k,v in groups.items() if v]
                if selected_struct_groups is None and y==2025:selected_struct_groups=available[:2]
                schema=(opi is not None and bool(mile_cols) and len(available)>=2)
                schemas_ok=schemas_ok and schema
                yop=set();yqual=set(); rows_n=0
                for r in rows:
                    if not any(str(x).strip() for x in r):continue
                    rows_n+=1
                    raw=rowv(r,opi)
                    if str(raw).strip():annual_exact_nonblank+=1
                    oid=opid(raw)
                    if oid:
                        annual_exact_valid+=1;yop.add(oid)
                    # source-native transmission qualification: any transmission mileage field > 0
                    vals=[parse_num(rowv(r,i)) for i in mile_cols]
                    is_trans=any(v is not None and v>0 for v in vals)
                    if oid and is_trans:yqual.add(oid)
                    if y==2025 and oid and is_trans:
                        completeness_2025["rows"]+=1
                        if any(v is not None for v in vals):completeness_2025["mileage"]+=1
                        if selected_struct_groups:
                            gok=True
                            for g in selected_struct_groups:
                                if not any(str(rowv(r,i)).strip() for i in groups[g]):gok=False
                            if gok:completeness_2025["additional"]+=1
                opids_by_year[y]=yop;qualified_by_year[y]=yqual
                if len(yqual)<500:support_ok=False
                annual_profiles[str(y)]={"member":m,"member_bytes":len(b),"member_sha256":sha_bytes(b),
                    "headers":headers,"rows":rows_n,"opid_col":headers[opi] if opi is not None else None,
                    "transmission_mileage_columns":[headers[i] for i in mile_cols],
                    "structural_groups":{k:[headers[i] for i in v[:20]] for k,v in groups.items() if v},
                    "distinct_opids":len(yop),"qualified_transmission_opids":len(yqual)}
            az.close()
            ev["annual_profiles"]=annual_profiles
            g4=years_ok and all(annual_profiles[str(y)].get("member_sha256") for y in YEARS)
            ev["gates"].append({"gate":4,"pass":g4,"observed":{"years":annual_profiles,"annual_zip":ameta}})
            ev["gates"].append({"gate":5,"pass":schemas_ok,"observed":{"per_year":{y:{"opid":p.get("opid_col"),"transmission_mileage_columns":p.get("transmission_mileage_columns"),"structural_groups":list((p.get("structural_groups") or {}).keys())} for y,p in annual_profiles.items()}}})
            arate=annual_exact_valid/annual_exact_nonblank if annual_exact_nonblank else 0
            ev["gates"].append({"gate":6,"pass":arate>=0.999,"observed":{"nonblank":annual_exact_nonblank,"valid_numeric_source_representation":annual_exact_valid,"rate":arate,"threshold":0.999}})
            ev["gates"].append({"gate":7,"pass":support_ok,"observed":{"qualified_opids_by_year":{str(y):len(qualified_by_year.get(y,set())) for y in YEARS},"threshold_each":500}})
            base25=qualified_by_year.get(2025,set())
            long=sum(1 for oid in base25 if sum(oid in qualified_by_year.get(y,set()) for y in YEARS)>=6)
            lrate=long/len(base25) if base25 else 0
            ev["gates"].append({"gate":8,"pass":lrate>=0.70,"observed":{"qualified_2025":len(base25),"present_6plus_years":long,"rate":lrate,"threshold":0.70}})
            mr=completeness_2025["mileage"]/completeness_2025["rows"] if completeness_2025["rows"] else 0
            sr=completeness_2025["additional"]/completeness_2025["rows"] if completeness_2025["rows"] else 0
            ev["gates"].append({"gate":9,"pass":mr>=0.95 and sr>=0.90,"observed":{**completeness_2025,"mileage_rate":mr,"additional_structural_rate":sr,"groups":selected_struct_groups,"thresholds":{"mileage":0.95,"additional":0.90}}})

            try:
                iz=zipfile.ZipFile(ip); incident_bad=iz.testzip()
            except Exception as e:
                raise RuntimeError(f"INCIDENT_ZIP_PARSE:{e}")
            im=choose_incident_data(iz)
            if not im: raise RuntimeError("INCIDENT_DATA_MEMBER_NOT_FOUND")
            itext,ib=decode_member(iz,im);headers,rows=rows_from_text(itext);ns=[norm(h) for h in headers]
            oi=find_col(headers,[lambda h:"operatorid" in h,lambda h:h in {"opid","operatornumber"}])
            ri=find_col(headers,[lambda h:"reportnumber" in h,lambda h:"incidentid" in h,lambda h:"reportid" in h])
            di=find_col(headers,[lambda h:"localdatetime" in h,lambda h:"incidentdate" in h,lambda h:"localdate" in h,lambda h:"date"==h])
            ti=find_col(headers,[lambda h:"systemtype" in h,lambda h:"pipelinesystemtype" in h,lambda h:"facilitytype" in h])
            fi=find_col(headers,[lambda h:"fatal" in h])
            ii=find_col(headers,[lambda h:"injur" in h])
            incident_schema=all(x is not None for x in (oi,ri,di,ti)) and (fi is not None or ii is not None)
            ev["gates"].append({"gate":10,"pass":incident_bad is None,"observed":{"incident_zip":imeta,"member":im,"member_bytes":len(ib),"member_sha256":sha_bytes(ib)}})
            ev["gates"].append({"gate":11,"pass":incident_schema,"observed":{"headers":headers,"mapping":{"opid":headers[oi] if oi is not None else None,"report_id":headers[ri] if ri is not None else None,"incident_date":headers[di] if di is not None else None,"system_type":headers[ti] if ti is not None else None,"fatality":headers[fi] if fi is not None else None,"injury":headers[ii] if ii is not None else None}}})
            recognized=focal=0; focal_ids=set(); focal_reports=set(); focal_date=0; inc_nonblank=inc_valid=0
            system_counts=Counter()
            for r in rows:
                if not any(str(x).strip() for x in r):continue
                tv=str(rowv(r,ti)).strip()
                if tv:system_counts[tv]+=1
                tnorm=norm(tv)
                # deterministic classification only on explicit source value containing transmission
                is_trans="transmission" in tnorm and "gather" not in tnorm
                is_known=bool(tv) and any(k in tnorm for k in ("transmission","gather","storage"))
                if is_known:recognized+=1
                if not is_trans:continue
                focal+=1
                raw=rowv(r,oi)
                if str(raw).strip():inc_nonblank+=1
                oid=opid(raw)
                if oid:inc_valid+=1;focal_ids.add(oid)
                rep=str(rowv(r,ri)).strip()
                if rep:focal_reports.add(rep)
                if parse_date(rowv(r,di)):focal_date+=1
            iz.close()
            class_rate=recognized/sum(system_counts.values()) if system_counts else 0
            ev["gates"].append({"gate":12,"pass":class_rate>=0.99 and focal>0,"observed":{"system_type_counts":dict(system_counts),"recognized_rate":class_rate,"focal_transmission_rows":focal,"threshold":0.99}})
            irate=inc_valid/inc_nonblank if inc_nonblank else 0
            annual_union=set().union(*(opids_by_year.get(y,set()) for y in YEARS))
            matched=len(focal_ids & annual_union)
            jrate=matched/len(focal_ids) if focal_ids else 0
            ev["gates"].append({"gate":13,"pass":irate>=0.99 and jrate>=0.95,"observed":{"incident_opid_nonblank":inc_nonblank,"valid":inc_valid,"syntax_rate":irate,"distinct_focal_opids":len(focal_ids),"matched_annual_opids":matched,"join_rate":jrate,"thresholds":{"syntax":0.99,"join":0.95}}})
            ev["gates"].append({"gate":14,"pass":len(focal_reports)>=1000,"observed":{"distinct_focal_report_ids":len(focal_reports),"threshold":1000}})
            dr=focal_date/focal if focal else 0
            ev["gates"].append({"gate":15,"pass":dr>=0.99,"observed":{"focal_rows":focal,"parseable_dates":focal_date,"rate":dr,"threshold":0.99}})
            g16=not ev["later_incident_refresh_opened"] and not ev["future_incident_membership_opened"] and ev["future_entity_rows_consumed"]==0
            ev["gates"].append({"gate":16,"pass":g16,"observed":{"runner_start_utc":started,"later_refresh_opened":False,"future_membership_opened":False,"future_rows":0}})
            g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],ev["prohibited_incident_enforcement_exposure_computed"],ev["identity_repair_used"]])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,"ranking":False,"causal":False,"prohibited_exposure":False,"identity_repair":False}})
            g18=(re.fullmatch(r"[0-9a-f]{64}",ameta["sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}",imeta["sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{"annual_zip_sha256":ameta["sha256"],"incident_zip_sha256":imeta["sha256"],"runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True;ev["pass_count"]=18-len(failed);ev["failed_gates"]=failed
        ev["disposition"]="PASS_US_PHMSA_PIPE_F01_GAS_TRANSMISSION_EXACT_OPID_FUTURE_INCIDENT_DESIGN_READY" if not failed else "HOLD_US_PHMSA_PIPE_F01_GAS_TRANSMISSION_EXACT_OPID_FUTURE_INCIDENT_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_PHMSA_PIPE_F01_ATTEMPT_02"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-PHMSA-PIPE-F01 — Attempt 02","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Later incident refresh opened: **{ev['later_incident_refresh_opened']}**",
           f"- Future incident membership opened: **{ev['future_incident_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No later PHMSA incident refresh was opened and no exposure→outcome relationship was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__": main()
