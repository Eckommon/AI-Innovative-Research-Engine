#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from urllib.parse import urljoin
import hashlib, json, os, re
import requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
CONTRACT_SHA="2734008b75116779d410ffec1e3ca44343e3e1f9"
ISSUE=187
OUTDIR=ROOT/"research/US-SEC-IA-F01/evidence"
JSON_OUT=OUTDIR/"attempt-01.json"
MD_OUT=OUTDIR/"attempt-01.md"

REPORT_PAGE="https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers"
ADV_PAGE="https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data"
IAPD_ADV="https://adviserinfo.sec.gov/adv"
ADVW_FORM="https://www.sec.gov/files/formadv-w.pdf"
FAQ="https://www.sec.gov/about/divisions-offices/division-investment-management/electronic-filing-investment-advisers-iard/frequently-asked-questions-form-adv-iard"
HIST_ADVW="https://www.sec.gov/files/advw-20001019-20241231.zip"
UA="AI-Innovative-Research-Engine/1.0 research contact public-data"

MONTHS=[
("2025-09","September 2025"),("2025-10","October 2025"),("2025-11","November 2025"),
("2025-12","December 2025"),("2026-01","January 2026"),("2026-02","February 2026"),
("2026-03","March 2026"),("2026-04","April 2026"),("2026-05","May 2026"),
("2026-06","June 2026"),("2026-07","July 2026"),("2026-08","August 2026")
]

def get(url, timeout=90):
    r=requests.get(url,headers={"User-Agent":UA},timeout=timeout,allow_redirects=True)
    r.raise_for_status()
    return r

def meta(r, include_sha=True):
    d={"status":r.status_code,"final_url":r.url,"content_type":r.headers.get("content-type"),
       "content_length_header":r.headers.get("content-length"),"last_modified":r.headers.get("last-modified"),
       "etag":r.headers.get("etag"),"bytes":len(r.content)}
    if include_sha:d["sha256"]=hashlib.sha256(r.content).hexdigest()
    return d

def classify_link(href, row_text):
    h=(href or "").lower()
    t=(row_text or "").upper()
    if ".ZIP" in t or h.endswith(".zip"): return "ZIP"
    if ".XLSX" in t or h.endswith(".xlsx"): return "XLSX"
    if ".PDF" in t or h.endswith(".pdf"): return "PDF"
    return "OTHER"

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-01 evidence exists")
    ev={
      "research":"US-SEC-IA-F01","attempt":1,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
      "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
      "post_cutoff_advw_body_opened":False,"future_advw_membership_opened":False,
      "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
      "causal_claim_made":False,"prohibited_withdrawal_exposure_computed":False,
      "identity_repair_used":False,"gates":[]
    }
    ev["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20260930-US-SEC-IA-F01-ACTIVE" and
            cp.get("active_issue")==187 and cp.get("active_research")=="US-SEC-IA-F01" and
            cp.get("last_decision")=="DEC-285")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.environ.get("SEC_IA_F01_BOUND")=="1" and os.environ.get("SEC_IA_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":187,"contract_sha":os.environ.get("SEC_IA_F01_CONTRACT_SHA")}})

        docs={}
        bodies={}
        for k,u in {"reports":REPORT_PAGE,"historical_adv":ADV_PAGE,"iapd_adv":IAPD_ADV,"advw_form":ADVW_FORM,"faq":FAQ}.items():
            try:
                r=get(u,90); docs[k]=meta(r); bodies[k]=r.content
            except Exception as e:
                docs[k]={"error":f"{type(e).__name__}:{e}","url":u}
        g3=all(docs.get(k,{}).get("status")==200 for k in docs)
        ev["gates"].append({"gate":3,"pass":g3,"observed":docs})

        # Resolve exactly the 12 Registered Investment Adviser monthly links from the official SEC page.
        html=bodies.get("reports",b"").decode("utf-8","replace")
        soup=BeautifulSoup(html,"html.parser")
        resolved={}
        for ym,label in MONTHS:
            target=re.compile(rf"Registered Investment Advisers,?\s*{re.escape(label)}",re.I)
            found=None
            for a in soup.find_all("a",href=True):
                text=" ".join(a.get_text(" ",strip=True).split())
                if target.search(text):
                    parent=a.find_parent(["tr","li","p","div"])
                    rowtext=" ".join((parent.get_text(" ",strip=True) if parent else text).split())
                    href=urljoin(REPORT_PAGE,a.get("href"))
                    found={"anchor_text":text,"url":href,"row_text":rowtext,"declared_format":classify_link(href,rowtext)}
                    break
            resolved[ym]=found
        ev["monthly_resolution"]=resolved

        exactly12=all(resolved.get(ym) is not None for ym,_ in MONTHS)
        all_zip=exactly12 and all(resolved[ym]["declared_format"]=="ZIP" for ym,_ in MONTHS)
        g4=bool(exactly12 and all_zip)
        ev["gates"].append({"gate":4,"pass":g4,"observed":{
            "expected_months":[x[0] for x in MONTHS],
            "resolved_count":sum(1 for x in resolved.values() if x),
            "all_external_zip":all_zip,
            "formats":{k:(v or {}).get("declared_format") for k,v in resolved.items()},
            "urls":{k:(v or {}).get("url") for k,v in resolved.items()}
        }})

        # Gate 4 is a prospectively decisive source-lineage requirement. Do not consume
        # historical ADV-W row bodies if it fails; preserve future/outcome firewall.
        if not g4:
            for g in range(5,17):
                ev["gates"].append({"gate":g,"pass":False,"observed":{"not_evaluated_after_decisive_gate4_failure":True}})
            g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],
                         ev["causal_claim_made"],ev["prohibited_withdrawal_exposure_computed"],ev["identity_repair_used"]]) and not ev["future_advw_membership_opened"] and not ev["post_cutoff_advw_body_opened"]
            ev["gates"].append({"gate":17,"pass":g17,"observed":{
              "relationship":False,"prediction":False,"ranking":False,"causal":False,
              "prohibited_exposure":False,"identity_repair":False,
              "post_cutoff_advw_body_opened":False,"future_membership_opened":False
            }})
            g18=(re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":bool(g18),"observed":{"contract_sha":CONTRACT_SHA,"runner_sha256":ev["runner_sha256"],"cost_usd":0,"historical_advw_body_opened":False}})
            ev["attempt_valid"]=True
            ev["failed_gates"]=[g["gate"] for g in ev["gates"] if not g["pass"]]
            ev["pass_count"]=sum(1 for g in ev["gates"] if g["pass"])
            ev["disposition"]="HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY"
        else:
            # This runner intentionally fails closed rather than silently implementing a
            # different empirical path. If all 12 become ZIPs in a future source revision,
            # a separately documented implementation continuation would be required.
            raise RuntimeError("UNEXPECTED_ALL_12_ZIP_NEEDS_FULL_EMPIRICAL_IMPLEMENTATION")
    except RuntimeError as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_SEC_IA_F01_ATTEMPT_01"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_SEC_IA_F01_ATTEMPT_01"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-SEC-IA-F01 — Attempt 01","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",
           f"- Post-cutoff ADV-W body opened: **{ev['post_cutoff_advw_body_opened']}**",
           f"- Future ADV-W membership opened: **{ev['future_advw_membership_opened']}**",
           f"- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1600:o=o[:1597]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","No historical or post-cutoff ADV-W row body was opened after a decisive Gate 4 source-lineage failure. No relationship or predictive metric was computed.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__": main()
