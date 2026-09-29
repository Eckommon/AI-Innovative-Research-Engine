#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse
import csv, hashlib, json, os, re, tempfile, time

import requests
from openpyxl import load_workbook
from pypdf import PdfReader
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="d1ccc1e745c0881a64f8cf7e2ab481fb69215adc"
ISSUE=180
OUTDIR=ROOT/"research/US-USDA-ORG-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"
CUTOFF=date(2026,9,29)

INTEGRITY="https://organic.ams.usda.gov/Integrity/"
ENFORCEMENT="https://www.ams.usda.gov/services/enforcement/organic"
DECISIONS="https://www.ams.usda.gov/services/enforcement/organic/ams-decisions"
DICT_PDF="https://www.ams.usda.gov/sites/default/files/media/INTEGRITY%20Data%20Dictionary.pdf"
FAQ_PDF="https://www.ams.usda.gov/sites/default/files/media/INTEGRITY%20FAQ.pdf"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36"

STATUS_ALLOWED={
    "Certified","Surrendered","Suspended","Revoked","Transitional",
    "Denied Certification","Withdrew with NONC","Withdrew from Transitional"
}

def norm_header(v):
    return re.sub(r"[^a-z0-9]+","",str(v or "").strip().lower())

def norm_id(v):
    s=str(v or "").strip()
    return s if re.fullmatch(r"[0-9]{10}",s) else None

def parse_date(v):
    if isinstance(v,datetime): return v.date()
    if isinstance(v,date): return v
    s=str(v or "").strip()
    for f in ("%m/%d/%Y","%Y-%m-%d","%m/%d/%y","%Y/%m/%d","%d-%b-%Y"):
        try:return datetime.strptime(s,f).date()
        except ValueError:pass
    return None

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as fh:
        for b in iter(lambda:fh.read(1024*1024),b""):h.update(b)
    return h.hexdigest()

def fetch(url,path,timeout=120):
    r=requests.get(url,timeout=timeout,headers={"User-Agent":UA},allow_redirects=True)
    r.raise_for_status()
    path.write_bytes(r.content)
    return {"status":r.status_code,"requested_url":url,"final_url":r.url,
            "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
            "etag":r.headers.get("etag"),"bytes":len(r.content),"sha256":hashlib.sha256(r.content).hexdigest()}

def pdf_text(path):
    return "\n".join((p.extract_text() or "") for p in PdfReader(str(path)).pages)

def idx(headers,*alts):
    hs=[norm_header(h) for h in headers]
    for i,h in enumerate(hs):
        if any(a==h or a in h for a in alts): return i
    return None

def read_export(path):
    magic=path.read_bytes()[:4]
    if magic.startswith(b"PK"):
        wb=load_workbook(path,read_only=True,data_only=True)
        for ws in wb.worksheets:
            for ridx,row in enumerate(ws.iter_rows(min_row=1,max_row=30,values_only=True),1):
                headers=[str(x or "") for x in row]
                hs=[norm_header(x) for x in headers]
                if any("operationid" in h or "nopid" in h for h in hs) and any("status" in h for h in hs):
                    rows=list(ws.iter_rows(min_row=ridx+1,values_only=True))
                    return headers,rows,ws.title
        raise RuntimeError("EXPORT_HEADER_NOT_FOUND_XLSX")
    raw=path.read_bytes()
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:text=raw.decode(enc);break
        except UnicodeDecodeError:continue
    else: raise RuntimeError("EXPORT_ENCODING_UNKNOWN")
    first=text.splitlines()[0] if text.splitlines() else ""
    delim="\t" if first.count("\t")>first.count(",") else ","
    rr=list(csv.reader(text.splitlines(),delimiter=delim))
    for i,row in enumerate(rr[:30]):
        hs=[norm_header(x) for x in row]
        if any("operationid" in h or "nopid" in h for h in hs) and any("status" in h for h in hs):
            return row,rr[i+1:],"text"
    raise RuntimeError("EXPORT_HEADER_NOT_FOUND_TEXT")

def browser_export(download_path:Path):
    obs={"responses":[],"ui_steps":[]}
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        page=browser.new_page(accept_downloads=True,user_agent=UA)
        def on_response(resp):
            try:
                ct=(resp.headers.get("content-type") or "").lower()
                u=resp.url.lower()
                if any(k in u for k in ("export","excel",".xlsx",".xls",".csv","report")) or any(k in ct for k in ("spreadsheet","excel","csv")):
                    obs["responses"].append({"url":resp.url,"status":resp.status,"content_type":ct})
            except Exception:pass
        page.on("response",on_response)
        page.goto(INTEGRITY,wait_until="domcontentloaded",timeout=90000)
        page.wait_for_timeout(12000)
        obs["initial_url"]=page.url
        obs["initial_text"]=page.locator("body").inner_text(timeout=20000)[:12000]
        # Navigate toward public operation search if the landing route exposes a menu.
        nav_patterns=[r"operation search",r"search operations",r"certified operations",r"operations"]
        for pat in nav_patterns:
            loc=page.get_by_text(re.compile(pat,re.I))
            if loc.count():
                try:
                    loc.first.click(timeout=5000)
                    page.wait_for_timeout(4000)
                    obs["ui_steps"].append(f"clicked:{pat}")
                    break
                except Exception:pass
        # Run a blank/default search. Try common button names without changing scientific filters.
        for pat in (r"^search$",r"search operations",r"apply",r"submit"):
            loc=page.get_by_role("button",name=re.compile(pat,re.I))
            if not loc.count(): loc=page.get_by_text(re.compile(pat,re.I))
            if loc.count():
                try:
                    loc.first.click(timeout=5000)
                    page.wait_for_timeout(7000)
                    obs["ui_steps"].append(f"clicked-search:{pat}")
                    break
                except Exception:pass
        obs["post_search_url"]=page.url
        obs["post_search_text"]=page.locator("body").inner_text(timeout=20000)[:15000]
        # Prefer a true browser download.
        export_locs=[]
        for pat in (r"export",r"excel",r"download"):
            for role in ("button","link"):
                try:
                    loc=page.get_by_role(role,name=re.compile(pat,re.I))
                    if loc.count(): export_locs.append((pat,role,loc.first))
                except Exception:pass
        downloaded=False
        for pat,role,loc in export_locs:
            try:
                with page.expect_download(timeout=30000) as di:
                    loc.click(timeout=8000)
                dl=di.value
                dl.save_as(str(download_path))
                obs["ui_steps"].append(f"download:{role}:{pat}:{dl.suggested_filename}")
                obs["suggested_filename"]=dl.suggested_filename
                downloaded=True
                break
            except Exception:
                continue
        # If no download event, try a direct official response URL discovered during the browser session.
        if not downloaded:
            candidates=[x["url"] for x in obs["responses"] if any(k in (x.get("content_type") or "") for k in ("spreadsheet","excel","csv")) or re.search(r"\.(xlsx?|csv)(?:\?|$)",x["url"],re.I)]
            obs["response_export_candidates"]=candidates[:20]
            for u in candidates:
                try:
                    m=fetch(u,download_path,180)
                    if m["bytes"]>1000:
                        obs["direct_response_fetch"]=m;downloaded=True;break
                except Exception:continue
        browser.close()
    obs["downloaded"]=downloaded
    return obs

def profile_one(cid,status):
    u=f"https://organic.ams.usda.gov/Integrity/CP/OPP?nopid={cid}"
    try:
        r=requests.get(u,timeout=45,headers={"User-Agent":UA},allow_redirects=True)
        if r.status_code!=200:return {"id":cid,"available":False,"status_code":r.status_code}
        txt=re.sub(r"<[^>]+>"," ",r.text)
        txt=" ".join(txt.split())
        id_ok=cid in txt
        status_ok=status.lower() in txt.lower()
        return {"id":cid,"available":id_ok,"id_ok":id_ok,"status_ok":status_ok,"status_code":r.status_code,"url":r.url}
    except Exception as e:return {"id":cid,"available":False,"error":f"{type(e).__name__}:{e}"}

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():raise RuntimeError("immutable attempt-01 evidence exists")
    ev={"research":"US-USDA-ORG-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_suspended_revoked_membership_opened":False,"future_entity_rows_consumed_for_membership":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,"causal_claim_made":False,
        "identity_repair_used":False,"prohibited_precursor_exposure_computed":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20260929-US-USDA-ORG-F01-ACTIVE" and cp.get("active_issue")==180
            and cp.get("active_research")=="US-USDA-ORG-F01" and cp.get("last_decision")=="DEC-270")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("USDA_ORG_F01_BOUND")=="1" and os.environ.get("USDA_ORG_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":180,"contract_sha":os.environ.get("USDA_ORG_F01_CONTRACT_SHA")}})

        with tempfile.TemporaryDirectory() as td0:
            td=Path(td0)
            docs={}
            for key,url in {"enforcement":ENFORCEMENT,"decisions":DECISIONS,"dictionary":DICT_PDF,"faq":FAQ_PDF}.items():
                p=td/(key+".pdf" if url.lower().endswith(".pdf") else key+".html")
                try:docs[key]=fetch(url,p,120)
                except Exception as e:docs[key]={"error":f"{type(e).__name__}:{e}","requested_url":url}
            try:
                r=requests.get(INTEGRITY,timeout=90,headers={"User-Agent":UA},allow_redirects=True)
                docs["integrity"]={"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),"bytes":len(r.content),"sha256":hashlib.sha256(r.content).hexdigest()}
            except Exception as e:docs["integrity"]={"error":f"{type(e).__name__}:{e}"}
            g3=all(docs.get(k,{}).get("status")==200 for k in ("enforcement","decisions","dictionary","faq")) and docs.get("integrity",{}).get("status")==200
            ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

            export_path=td/"integrity-export.xlsx"
            browser_obs=browser_export(export_path)
            ev["export_discovery"]=browser_obs
            g4=browser_obs.get("downloaded") and export_path.exists() and export_path.stat().st_size>1000
            ev["gates"].append({"gate":4,"pass":bool(g4),"observed":{"browser":browser_obs,"bytes":export_path.stat().st_size if export_path.exists() else 0}})
            if not g4:
                raise RuntimeError("PUBLIC_EXPORT_NOT_RESOLVED_BY_OFFICIAL_UI")

            ev["export_sha256"]=sha256(export_path)
            headers,rows,sheet=read_export(export_path)
            oi=idx(headers,"operationid","nopid")
            pi=idx(headers,"program")
            si=idx(headers,"operationcertificationstatus","certificationstatus")
            di=idx(headers,"effectivedateofoperationstatus","operationstatuseffectivedate","statuseffectivedate")
            schema_ok=all(x is not None for x in (oi,pi,si,di))
            ev["gates"].append({"gate":5,"pass":schema_ok,"observed":{"sheet":sheet,"headers":headers,"indices":{"operation_id":oi,"program":pi,"status":si,"status_date":di}}})
            if not schema_ok:
                # Valid empirical result: export is readable but required frozen schema is absent.
                rows_focal=[]
            else:
                rows_focal=[]
                for r in rows:
                    program=str(r[pi] if pi<len(r) else "").strip()
                    # Keep only USDA-NOP when explicitly available; accept exact NOP/USDA Organic wording.
                    if not re.search(r"(USDA|NOP|National Organic Program)",program,re.I):continue
                    rows_focal.append((r,program))
            nonblank=valid=0;ids=set();status_counts=Counter();date_nonblank=0
            historical_adverse=set();surrendered=set();id_status={}
            future_adverse_seen=0
            for r,program in rows_focal:
                raw=r[oi] if oi is not None and oi<len(r) else None
                if str(raw or "").strip():nonblank+=1
                cid=norm_id(raw)
                if not cid:continue
                valid+=1;ids.add(cid)
                st=str(r[si] if si is not None and si<len(r) else "").strip()
                dt=parse_date(r[di] if di is not None and di<len(r) else None)
                if st:status_counts[st]+=1
                if dt:date_nonblank+=1
                id_status.setdefault(cid,st)
                if st in ("Suspended","Revoked") and dt:
                    if dt<=CUTOFF: historical_adverse.add(cid)
                    else: future_adverse_seen+=1
                if st=="Surrendered":surrendered.add(cid)
            syntax=valid/nonblank if nonblank else 0
            ev["gates"].append({"gate":6,"pass":syntax>=0.999,"observed":{"valid":valid,"nonblank":nonblank,"rate":syntax,"threshold":0.999}})
            ev["gates"].append({"gate":7,"pass":len(ids)>=40000,"observed":{"distinct_ids":len(ids),"threshold":40000}})
            certified={cid for cid,st in id_status.items() if st=="Certified"}
            ev["gates"].append({"gate":8,"pass":len(certified)>=30000,"observed":{"certified_ids":len(certified),"threshold":30000}})
            recognized=sum(v for k,v in status_counts.items() if k in STATUS_ALLOWED);total_status=sum(status_counts.values())
            sr=recognized/total_status if total_status else 0
            ev["gates"].append({"gate":9,"pass":sr>=0.999,"observed":{"status_counts":dict(status_counts),"recognized_rate":sr,"unknown":[k for k in status_counts if k not in STATUS_ALLOWED]}})
            dr=date_nonblank/valid if valid else 0
            ev["gates"].append({"gate":10,"pass":dr>=0.99,"observed":{"date_rows":date_nonblank,"qualified_rows":valid,"rate":dr,"threshold":0.99}})
            ev["gates"].append({"gate":11,"pass":len(historical_adverse)>=1000,"observed":{"historical_suspended_revoked_ids":len(historical_adverse),"threshold":1000}})
            ev["gates"].append({"gate":12,"pass":len(surrendered)>=100 and "Surrendered" in status_counts and ("Suspended" in status_counts or "Revoked" in status_counts),
                                "observed":{"surrendered_ids":len(surrendered),"threshold":100,"statuses":dict(status_counts)}})

            dtext=pdf_text(td/"dictionary.pdf") if (td/"dictionary.pdf").exists() else ""
            faqtext=pdf_text(td/"faq.pdf") if (td/"faq.pdf").exists() else ""
            etext=(td/"enforcement.html").read_text("utf-8",errors="replace") if (td/"enforcement.html").exists() else ""
            dectext=(td/"decisions.html").read_text("utf-8",errors="replace") if (td/"decisions.html").exists() else ""
            semantic_blob=" ".join((dtext,faqtext,re.sub(r"<[^>]+>"," ",etext),re.sub(r"<[^>]+>"," ",dectext))).lower()
            g13=("suspension" in semantic_blob and "revocation" in semantic_blob and "appeal" in semantic_blob and "final" in semantic_blob)
            ev["gates"].append({"gate":13,"pass":g13,"observed":{"suspension":("suspension" in semantic_blob),"revocation":("revocation" in semantic_blob),"appeal":("appeal" in semantic_blob),"final":("final" in semantic_blob)}})

            sample=sorted(ids)[:100]
            prof=[]
            with ThreadPoolExecutor(max_workers=10) as ex:
                fs={ex.submit(profile_one,cid,id_status.get(cid,"")):cid for cid in sample}
                for z in as_completed(fs):prof.append(z.result())
            available=[x for x in prof if x.get("available")]
            concord=[x for x in available if x.get("id_ok") and x.get("status_ok")]
            pr=len(concord)/len(available) if available else 0
            ev["gates"].append({"gate":14,"pass":bool(available) and pr>=0.95,
                                "observed":{"sample_rule":"lexicographically first 100 qualified IDs","requested":len(sample),"available":len(available),"concordant":len(concord),"rate":pr,"threshold":0.95,"results":sorted(prof,key=lambda x:x["id"])}})

            lineage=("merged into the list of operations" in faqtext.lower() and "suspended" in faqtext.lower() and "revoked" in faqtext.lower()
                     and "effective date of operation status" in dtext.lower() and len(historical_adverse)>=1000)
            ev["gates"].append({"gate":15,"pass":lineage,"observed":{"faq_merge_support":("merged into the list of operations" in faqtext.lower()),"effective_date_semantics":("effective date of operation status" in dtext.lower()),"historical_adverse_ids":len(historical_adverse)}})

            # Any post-cutoff adverse row in the baseline would open prohibited future membership.
            if future_adverse_seen:
                ev["future_suspended_revoked_membership_opened"]=True
                ev["future_entity_rows_consumed_for_membership"]=future_adverse_seen
            g16=(not ev["future_suspended_revoked_membership_opened"] and ev["future_entity_rows_consumed_for_membership"]==0)
            ev["gates"].append({"gate":16,"pass":g16,"observed":{"future_membership_opened":ev["future_suspended_revoked_membership_opened"],"future_rows":ev["future_entity_rows_consumed_for_membership"]}})
            g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],ev["identity_repair_used"],ev["prohibited_precursor_exposure_computed"]])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,"ranking":False,"causal":False,"identity_repair":False,"prohibited_precursor":False}})
            g18=(re.fullmatch(r"[0-9a-f]{64}",ev["export_sha256"]) is not None and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":g18,"observed":{"export_sha256":ev["export_sha256"],"runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[x["gate"] for x in ev["gates"] if not x["pass"]]
        ev["attempt_valid"]=True
        ev["pass_count"]=18-len(failed)
        ev["failed_gates"]=failed
        ev["disposition"]="PASS_US_USDA_ORG_F01_EXACT_OPERATION_FUTURE_SUSPENSION_REVOCATION_DESIGN_READY" if not failed else "HOLD_US_USDA_ORG_F01_EXACT_OPERATION_FUTURE_SUSPENSION_REVOCATION_DESIGN_NOT_READY"
    except RuntimeError as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_USDA_ORG_F01_ATTEMPT_01"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for x in ev["gates"] if x.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_USDA_ORG_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-USDA-ORG-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future Suspended/Revoked membership opened: **{ev['future_suspended_revoked_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1000:o=o[:997]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No future adverse-status source was intentionally queried. Current baseline rows were evaluated only under the frozen cutoff/firewall rule.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":main()
