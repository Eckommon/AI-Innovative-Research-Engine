#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
import csv, hashlib, io, json, os, re, tempfile, zipfile

import requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="18646fff22a499fedb058df397269281e62793b8"
ISSUE=201
OUTDIR=ROOT/"research/US-CMS-NPI-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"

FILES_PAGE="https://download.cms.gov/nppes/NPI_Files.html"
DISSEMINATION="https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination"
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
NPI_RE=re.compile(r"^[0-9]{10}$")
csv.field_size_limit(1024*1024*64)

def norm(s):
    return re.sub(r"[^a-z0-9]+","",str(s or "").strip().lower())

def parse_date(s):
    s=str(s or "").strip()
    if not s: return False
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y"):
        try:
            datetime.strptime(s,f); return True
        except ValueError:
            pass
    return False

def sha_file(path:Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def get_page(url):
    r=requests.get(url,headers={"User-Agent":UA},timeout=120,allow_redirects=True)
    r.raise_for_status()
    return r

def resolve_current_links(html,base):
    soup=BeautifulSoup(html,"html.parser")
    rows=[]
    for a in soup.find_all("a",href=True):
        text=" ".join(a.get_text(" ",strip=True).split())
        href=urljoin(base,a["href"])
        if "zip" in href.lower() or "zip" in text.lower():
            rows.append({"text":text,"url":href})
    full=None; deact=None; weekly=None
    for x in rows:
        t=x["text"].lower()
        if "v.2" in t or "version 2" in t or "v2" in t:
            if "deactivation" in t and "monthly" in t:
                if deact is None: deact=x
            elif "weekly" in t:
                if weekly is None: weekly=x
            elif "nppes data dissemination" in t and "deactivation" not in t:
                if full is None: full=x
    # Fallbacks based on URL/text families.
    if full is None:
        for x in rows:
            t=x["text"].lower(); u=x["url"].lower()
            if "deactivation" not in t+u and "weekly" not in t+u and ("nppes" in t+u or "npidata" in t+u):
                full=x; break
    if deact is None:
        for x in rows:
            if "deactivation" in (x["text"]+" "+x["url"]).lower():
                deact=x; break
    if weekly is None:
        for x in rows:
            if "weekly" in (x["text"]+" "+x["url"]).lower():
                weekly=x; break
    return {"full":full,"deactivation":deact,"weekly":weekly,"candidates":rows[:100]}

def head_meta(url):
    r=requests.head(url,headers={"User-Agent":UA},timeout=120,allow_redirects=True)
    if r.status_code>=400:
        r=requests.get(url,headers={"User-Agent":UA,"Range":"bytes=0-0"},timeout=120,allow_redirects=True,stream=True)
    return {"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),
            "content_length":r.headers.get("content-length"),"last_modified":r.headers.get("last-modified"),
            "etag":r.headers.get("etag")}

def download(url,path):
    h=hashlib.sha256(); total=0
    with requests.get(url,headers={"User-Agent":UA},timeout=(30,1200),allow_redirects=True,stream=True) as r:
        r.raise_for_status()
        meta={"status":r.status_code,"requested_url":url,"final_url":r.url,
              "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
              "etag":r.headers.get("etag"),"content_length_header":r.headers.get("content-length")}
        with path.open("wb") as f:
            for chunk in r.iter_content(1024*1024):
                if chunk:
                    f.write(chunk); h.update(chunk); total+=len(chunk)
    meta["bytes"]=total; meta["sha256"]=h.hexdigest()
    return meta

def zip_inventory(path):
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        return z.namelist(),bad

def find_member(names,kind):
    lower=[(n,n.lower()) for n in names if not n.endswith("/")]
    if kind=="main":
        for n,l in lower:
            if ("npidata_pfile" in l or "npidata" in l) and l.endswith(".csv") and "header" not in l:
                return n
    if kind=="practice":
        for n,l in lower:
            if ("pl_pfile" in l or "practice_location" in l or "practice location" in l) and l.endswith(".csv"):
                return n
    if kind=="deactivation":
        for n,l in lower:
            if "deactiv" in l and l.endswith(".csv"):
                return n
        for n,l in lower:
            if l.endswith(".csv"):
                return n
    return None

def reader_from_zip(zf,member):
    raw=zf.open(member)
    txt=io.TextIOWrapper(raw,encoding="utf-8-sig",errors="replace",newline="")
    rd=csv.DictReader(txt)
    if not rd.fieldnames:
        raise RuntimeError(f"NO_HEADER:{member}")
    fields=[str(x or "").strip() for x in rd.fieldnames]
    def rows():
        try:
            for r in rd:
                yield r
        finally:
            txt.close()
    return fields,rows()

def idx_map(fields):
    return {norm(x):x for x in fields}

def pick(m,*needles):
    for k,v in m.items():
        if any(n==k or n in k for n in needles):
            return v
    return None

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable attempt-01 evidence exists")

    ev={
        "research":"US-CMS-NPI-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "weekly_body_opened":False,"later_monthly_body_opened":False,
        "future_deactivation_membership_opened":False,"future_entity_rows_consumed":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
        "causal_claim_made":False,"deactivation_history_exposure_computed":False,
        "identity_repair_used":False,"gates":[]
    }
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261013-US-CMS-NPI-F01-ACTIVE"
            and cp.get("active_issue")==201 and cp.get("active_research")=="US-CMS-NPI-F01"
            and cp.get("last_decision")=="DEC-314")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("CMS_NPI_F01_BOUND")=="1" and os.environ.get("CMS_NPI_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":201,"contract_sha":os.environ.get("CMS_NPI_F01_CONTRACT_SHA")}})

        fp=get_page(FILES_PAGE); dp=get_page(DISSEMINATION)
        links=resolve_current_links(fp.text,fp.url)
        g3=(fp.status_code==200 and dp.status_code==200 and all(links.get(k) for k in ("full","deactivation","weekly")))
        ev["source_resolution"]={"files_page_status":fp.status_code,"dissemination_status":dp.status_code,"links":links}
        ev["gates"].append({"gate":3,"pass":g3,"observed":{"files_page":fp.url,"dissemination":dp.url,
            "full":links.get("full"),"deactivation":links.get("deactivation"),"weekly":links.get("weekly")}})
        if not g3:
            raise RuntimeError("CURRENT_V2_LINK_FAMILY_NOT_RESOLVED")

        ev["weekly_metadata"]=head_meta(links["weekly"]["url"])

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0)
            fullp=td/"full.zip"; deactp=td/"deactivation.zip"
            fullmeta=download(links["full"]["url"],fullp)
            deactmeta=download(links["deactivation"]["url"],deactp)
            ev["full_zip"]=fullmeta; ev["deactivation_zip"]=deactmeta

            finv,fbad=zip_inventory(fullp)
            dinv,dbad=zip_inventory(deactp)
            ev["full_zip_inventory"]=finv
            ev["deactivation_zip_inventory"]=dinv
            g4=(fbad is None and fullmeta["bytes"]>=500*1024*1024)
            g5=(dbad is None and deactmeta["bytes"]>=1*1024*1024)
            ev["gates"].append({"gate":4,"pass":g4,"observed":{"zip_valid":fbad is None,**fullmeta}})
            ev["gates"].append({"gate":5,"pass":g5,"observed":{"zip_valid":dbad is None,**deactmeta}})
            if fbad is not None or dbad is not None:
                raise RuntimeError("BASELINE_ZIP_NOT_PARSEABLE")

            with zipfile.ZipFile(fullp) as zf:
                mainm=find_member(finv,"main"); plm=find_member(finv,"practice")
                if not mainm:
                    raise RuntimeError("MAIN_DISSEMINATION_CSV_NOT_FOUND")
                fields,rows=reader_from_zip(zf,mainm)
                im=idx_map(fields)
                npi_col=pick(im,"npi")
                entity_col=pick(im,"entitytypecode")
                enum_col=pick(im,"providerenumerationdate")
                upd_col=pick(im,"lastupdatedate")
                deact_col=pick(im,"npideactivationdate")
                react_col=pick(im,"npireactivationdate")
                tax_cols=[v for k,v in im.items() if "healthcareprovidertaxonomycode" in k]
                schema_ok=all([npi_col,entity_col,enum_col,upd_col,deact_col,react_col]) and len(tax_cols)>=1
                ev["gates"].append({"gate":6,"pass":bool(schema_ok),"observed":{"main_member":mainm,"headers":fields,
                    "resolved":{"npi":npi_col,"entity":entity_col,"enumeration":enum_col,"last_update":upd_col,
                                "deactivation":deact_col,"reactivation":react_col,"taxonomy_columns":tax_cols}}})

                total_npi=valid_npi=0; exact_seen=set(); duplicate_exact=0
                active_type2=0; active_type2_tax=0; single_tax=0; multi_tax=0
                for r in rows:
                    raw=str(r.get(npi_col) or "").strip() if npi_col else ""
                    if raw:
                        total_npi+=1
                    good=bool(NPI_RE.fullmatch(raw))
                    if good:
                        valid_npi+=1
                        if raw in exact_seen: duplicate_exact+=1
                        else: exact_seen.add(raw)
                    if not good or not entity_col or not deact_col:
                        continue
                    if str(r.get(entity_col) or "").strip()=="2" and not str(r.get(deact_col) or "").strip():
                        active_type2+=1
                        tc=sum(1 for c in tax_cols if str(r.get(c) or "").strip())
                        if tc>=1:
                            active_type2_tax+=1
                            if tc==1: single_tax+=1
                            else: multi_tax+=1

                syntax_rate=valid_npi/total_npi if total_npi else 0
                uniq_rate=(valid_npi-duplicate_exact)/valid_npi if valid_npi else 0
                ev["gates"].append({"gate":7,"pass":syntax_rate>=0.99999,"observed":{"nonblank":total_npi,"valid":valid_npi,"rate":syntax_rate,"threshold":0.99999}})
                ev["gates"].append({"gate":8,"pass":uniq_rate>=0.99999,"observed":{"exact_rows":valid_npi,"duplicate_exact":duplicate_exact,"rate":uniq_rate,"threshold":0.99999}})
                ev["gates"].append({"gate":9,"pass":active_type2>=500000,"observed":{"active_type2":active_type2,"threshold":500000}})
                tax_rate=active_type2_tax/active_type2 if active_type2 else 0
                ev["gates"].append({"gate":10,"pass":tax_rate>=0.95,"observed":{"active_type2":active_type2,"with_taxonomy":active_type2_tax,"rate":tax_rate,"threshold":0.95}})
                g11=(single_tax>=100000 and multi_tax>=100000)
                ev["gates"].append({"gate":11,"pass":g11,"observed":{"single_taxonomy":single_tax,"multi_taxonomy":multi_tax,"threshold_each":100000}})

                if not plm:
                    ev["gates"].append({"gate":12,"pass":False,"observed":{"practice_location_member":None}})
                else:
                    pf,prows=reader_from_zip(zf,plm)
                    pm=idx_map(pf); pn=pick(pm,"npi")
                    pl_nonblank=pl_valid=0; pl_ids=set()
                    for r in prows:
                        x=str(r.get(pn) or "").strip() if pn else ""
                        if x: pl_nonblank+=1
                        if NPI_RE.fullmatch(x):
                            pl_valid+=1; pl_ids.add(x)
                    pl_syntax=pl_valid/pl_nonblank if pl_nonblank else 0
                    matched=sum(1 for x in pl_ids if x in exact_seen)
                    join=matched/len(pl_ids) if pl_ids else 0
                    ev["gates"].append({"gate":12,"pass":pl_syntax>=0.999 and join>=0.99,
                        "observed":{"practice_location_member":plm,"rows_nonblank_npi":pl_nonblank,"valid_npi":pl_valid,
                                    "syntax_rate":pl_syntax,"distinct_npi":len(pl_ids),"matched_main":matched,"join_rate":join}})

            with zipfile.ZipFile(deactp) as zf:
                dm=find_member(dinv,"deactivation")
                if not dm:
                    raise RuntimeError("DEACTIVATION_CSV_NOT_FOUND")
                df,drows=reader_from_zip(zf,dm)
                mm=idx_map(df)
                dn=pick(mm,"npi")
                dd=pick(mm,"deactivationdate","npideactivationdate")
                g13=bool(dn and dd)
                ev["gates"].append({"gate":13,"pass":g13,"observed":{"member":dm,"headers":df,"npi_column":dn,"date_column":dd}})
                d_nonblank=d_valid=d_date_nonblank=d_date_ok=0; d_ids=set()
                for r in drows:
                    n=str(r.get(dn) or "").strip() if dn else ""
                    d=str(r.get(dd) or "").strip() if dd else ""
                    if n: d_nonblank+=1
                    if NPI_RE.fullmatch(n):
                        d_valid+=1; d_ids.add(n)
                    if d:
                        d_date_nonblank+=1
                        if parse_date(d): d_date_ok+=1
                ds=d_valid/d_nonblank if d_nonblank else 0
                dr=d_date_ok/d_date_nonblank if d_date_nonblank else 0
                ev["gates"].append({"gate":14,"pass":ds>=0.9999 and dr>=0.999,
                    "observed":{"npi_nonblank":d_nonblank,"npi_valid":d_valid,"npi_rate":ds,
                                "date_nonblank":d_date_nonblank,"date_parseable":d_date_ok,"date_rate":dr}})
                ev["gates"].append({"gate":15,"pass":len(d_ids)>=50000,"observed":{"distinct_deactivated_npis":len(d_ids),"threshold":50000}})

            g16=(ev["weekly_body_opened"] is False and ev["later_monthly_body_opened"] is False
                 and ev["future_deactivation_membership_opened"] is False and ev["future_entity_rows_consumed"]==0
                 and ev["weekly_metadata"].get("status") in (200,206))
            ev["gates"].append({"gate":16,"pass":g16,"observed":{"weekly_metadata":ev["weekly_metadata"],
                "weekly_body_opened":False,"later_monthly_body_opened":False,"future_membership_opened":False,"future_rows":0}})
            g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],
                         ev["causal_claim_made"],ev["deactivation_history_exposure_computed"],ev["identity_repair_used"]])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,"ranking":False,
                "causal":False,"deactivation_history_exposure":False,"identity_repair":False}})
            g18=(re.fullmatch(r"[0-9a-f]{64}",fullmeta["sha256"]) is not None
                 and re.fullmatch(r"[0-9a-f]{64}",deactmeta["sha256"]) is not None
                 and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None
                 and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{"full_sha256":fullmeta["sha256"],
                "deactivation_sha256":deactmeta["sha256"],"runner_sha256":ev["runner_sha256"],
                "contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
        ev["attempt_valid"]=True
        ev["pass_count"]=18-len(failed)
        ev["failed_gates"]=failed
        ev["disposition"]="PASS_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_READY" if not failed else "HOLD_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NPI_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-CMS-NPI-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",
           f"- Weekly body opened: **{ev['weekly_body_opened']}**",
           f"- Future deactivation membership opened: **{ev['future_deactivation_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):
        lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","Raw CMS ZIP bodies were transient only. Weekly and later update row bodies remained sealed; no deactivation relationship was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":
    main()
