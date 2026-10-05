#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, json, os, re

import requests
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="fed9f05c7271c712881fc9b7936ca1a5f7912347"
ISSUE=194
OUTDIR=ROOT/"research/US-CMS-NH-F01/evidence"
JSON_OUT=OUTDIR/"attempt-02.json"
MD_OUT=OUTDIR/"attempt-02.md"
ARCHIVE="https://data.cms.gov/provider-data/archived-data/nursing-homes"
PROVIDER="https://data.cms.gov/provider-data/dataset/4pq5-n9py"
DEFICIENCY="https://data.cms.gov/provider-data/dataset/r5ix-sfxw"
DICTIONARY="https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/nursing_home/NH_Data_Dictionary.pdf"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
REQUIRED=[(2025,m) for m in range(9,13)]+[(2026,m) for m in range(1,9)]

def fetch_meta(url):
    r=requests.get(url,headers={"User-Agent":UA},timeout=120,allow_redirects=True)
    r.raise_for_status()
    return {"status":r.status_code,"requested_url":url,"final_url":r.url,
            "content_type":r.headers.get("content-type"),"last_modified":r.headers.get("last-modified"),
            "etag":r.headers.get("etag"),"bytes":len(r.content),
            "sha256":hashlib.sha256(r.content).hexdigest()}

def extract_dates(text):
    out=set()
    for m,d,y in re.findall(r"\b(0?[1-9]|1[0-2])\s*/\s*(0?[1-9]|[12][0-9]|3[01])\s*/\s*(20[0-9]{2})\b",text):
        out.add((int(y),int(m),int(d)))
    for y,m,d in re.findall(r"\b(20[0-9]{2})-(0[1-9]|1[0-2])-([0-3][0-9])\b",text):
        out.add((int(y),int(m),int(d)))
    return out

def discover_archive_network():
    obs={"dom_text":"","responses":[],"response_dates":[],"performance_urls":[],"console":[]}
    date_hits=set()
    with sync_playwright() as pw:
        b=pw.chromium.launch(headless=True)
        ctx=b.new_context(user_agent=UA)
        p=ctx.new_page()
        p.on("console",lambda msg: obs["console"].append({"type":msg.type,"text":msg.text[:2000]}))
        def on_resp(resp):
            try:
                u=resp.url
                if "data.cms.gov" not in u: return
                ct=(resp.headers.get("content-type") or "").lower()
                rec={"url":u,"status":resp.status,"content_type":ct}
                if any(x in ct for x in ("json","text","javascript")):
                    try:
                        body=resp.body()
                        if len(body)<=8_000_000:
                            txt=body.decode("utf-8","replace")
                            ds=extract_dates(txt)
                            if ds:
                                rec["dates"]=sorted([f"{y:04d}-{m:02d}-{d:02d}" for y,m,d in ds])
                                date_hits.update(ds)
                            if "nursing-homes" in txt.lower() or "archive" in txt.lower():
                                rec["body_excerpt"]=txt[:6000]
                    except Exception as e:
                        rec["body_error"]=f"{type(e).__name__}:{e}"
                obs["responses"].append(rec)
            except Exception: pass
        p.on("response",on_resp)
        p.goto(ARCHIVE,wait_until="domcontentloaded",timeout=90000)
        p.wait_for_timeout(30000)
        try:
            obs["dom_text"]=p.locator("body").inner_text(timeout=15000)[:60000]
            date_hits.update(extract_dates(obs["dom_text"]))
        except Exception: pass
        try:
            urls=p.evaluate("performance.getEntriesByType('resource').map(x=>x.name)")
            obs["performance_urls"]=[x for x in urls if "data.cms.gov" in x][:500]
        except Exception: pass
        b.close()
    obs["response_dates"]=sorted([{"year":y,"month":m,"day":d} for y,m,d in date_hits],key=lambda x:(x["year"],x["month"],x["day"]))
    return obs

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-02 evidence exists")
    ev={"research":"US-CMS-NH-F01","attempt":2,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "sep2026_or_later_row_bodies_opened":0,"future_standard_survey_membership_opened":False,
        "future_serious_deficiency_membership_opened":False,"relationship_computed":False,
        "prediction_computed":False,"ranking_computed":False,"causal_claim_made":False,
        "prohibited_outcome_exposure_computed":False,"identity_repair_used":False,"gates":[]}
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        a1=json.loads((OUTDIR/"attempt-01.json").read_text())
        assert a1["archive_ui"]["text"]=="" and a1["archive_ui"]["dates"]==[]
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261006-US-CMS-NH-F01-ACTIVE"
            and cp.get("active_issue")==194 and cp.get("active_research")=="US-CMS-NH-F01"
            and cp.get("last_decision")=="DEC-300")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("CMS_NH_F01_BOUND")=="1" and os.environ.get("CMS_NH_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":194,"contract_sha":os.environ.get("CMS_NH_F01_CONTRACT_SHA")}})
        docs={}
        for k,u in {"archive":ARCHIVE,"provider":PROVIDER,"deficiency":DEFICIENCY,"dictionary":DICTIONARY}.items():
            try: docs[k]=fetch_meta(u)
            except Exception as e: docs[k]={"error":f"{type(e).__name__}:{e}","url":u}
        ev["gates"].append({"gate":3,"pass":all(docs.get(k,{}).get("status")==200 for k in docs),"observed":docs})
        obs=discover_archive_network();ev["archive_discovery"]=obs
        dates={(x["year"],x["month"],x["day"]) for x in obs["response_dates"]}
        if not dates:
            ev["attempt_valid"]=False
            ev["implementation_error"]={"type":"ArchiveDiscoveryUnresolved","message":"CMS_OFFICIAL_ARCHIVE_NETWORK_AND_DOM_EXPOSED_NO_DATES"}
            ev["pass_count"]=sum(1 for g in ev["gates"] if g["pass"]);ev["failed_gates"]=[]
            ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NH_F01_ATTEMPT_02"
        else:
            by={}
            for y,m,d in dates:by.setdefault((y,m),[]).append(d)
            resolved={f"{y}-{m:02d}":sorted(by.get((y,m),[])) for y,m in REQUIRED}
            missing=[k for k,v in resolved.items() if not v]
            g4=not missing
            ev["gates"].append({"gate":4,"pass":g4,"observed":{"required_months":[f"{y}-{m:02d}" for y,m in REQUIRED],
                "official_archive_release_days_by_month":resolved,"missing_months":missing,
                "source_native_dates_seen":obs["response_dates"]}})
            if not g4:
                for g in range(5,19):ev["gates"].append({"gate":g,"pass":False,"observed":{"not_evaluated_after_decisive_gate4":True,"reason":"FROZEN_MONTHLY_ARCHIVE_LINEAGE_MISSING"}})
                ev["attempt_valid"]=True;ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
                ev["failed_gates"]=[g["gate"] for g in ev["gates"] if not g["pass"]]
                ev["pass_count"]=sum(1 for g in ev["gates"] if g["pass"])
                ev["disposition"]="HOLD_US_CMS_NH_F01_EXACT_CCN_FUTURE_STANDARD_SURVEY_SERIOUS_DEFICIENCY_DESIGN_NOT_READY"
            else:
                ev["attempt_valid"]=False
                ev["implementation_error"]={"type":"ImplementationContinuationRequired","message":"ALL_FROZEN_ARCHIVE_MONTHS_PRESENT_BODY_RESOLVER_REQUIRED"}
                ev["pass_count"]=sum(1 for g in ev["gates"] if g["pass"]);ev["failed_gates"]=[]
                ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NH_F01_ATTEMPT_02"
    except Exception as e:
        ev["attempt_valid"]=False;ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"));ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_CMS_NH_F01_ATTEMPT_02"
    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-CMS-NH-F01 — Attempt 02","",f"**Disposition:** `{ev['disposition']}`","",
      f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
      f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future serious membership opened: **{ev['future_serious_deficiency_membership_opened']}**",
      f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1800:o=o[:1797]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","Attempt 01 remains immutable and non-adjudicative because its official archive DOM was empty. No future outcome body was opened.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__":main()
