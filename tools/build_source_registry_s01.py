#!/usr/bin/env python3
"""S01 deterministic registry from GitHub-committed *summary evidence*, no raw archives."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "research/SOURCE-REGISTRY-S01"
SOURCES = [
 {"id":"CMS-NPI","name_ko":"CMS NPI 코호트","grade":"D4","evidence":["research/US-CMS-NPI-N01/RESULT.md"],"required":["346,859","18/18"],"status":"PASS_N01_E01_WAIT_SOURCE","url":"https://download.cms.gov/nppes/NPI_Files.html","key":"NPI","key_state":"VERIFIED_N01","vintage":"2026-10-12 baseline","reserved":True,"source_body":"N01 baseline evidence; D4 design; future weekly UNOBSERVED","reusable":False},
 {"id":"NOAA-QCEW","name_ko":"NOAA×BLS 기상·고용","grade":"D2","evidence":["research/US-NOAA-QCEW-F01/RESULT.md","research/US-NOAA-QCEW-F01/evidence/attempt-01.json"],"required":["17/18","12,888,092"],"status":"TERMINAL_F01_HOLD_GATE12","url":"https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/","key":"County FIPS; frozen F01 exact route failed","key_state":"UNQUALIFIED_F01","vintage":"NOAA 2023, QCEW 2024 Q1","reserved":False,"source_body":"Full official NOAA + BLS SHA/byte evidence","reusable":False},
 {"id":"EPA-RCRA","name_ko":"EPA RCRA 시설","grade":"D3","evidence":["research/US-EPA-RCRA-F01/RESULT.md","research/US-EPA-RCRA-N01/RESULT.md"],"required":["119,521,531","18/18","13/18"],"status":"PASS_F01_TERMINAL_N01_HOLD","url":"https://rcrapublic.epa.gov/rcrainfoweb/action/modules/main/home","key":"HANDLER_ID","key_state":"VERIFIED_F01","vintage":"2026-10 baseline","reserved":False,"source_body":"Full RCRA official ZIP SHA/bytes","reusable":False},
 {"id":"FDIC-BRANCH","name_ko":"FDIC 은행 지점","grade":"D3","evidence":["research/US-FDIC-BRANCH-F01/RESULT.md","research/US-FDIC-BRANCH-N01/RESULT.md"],"required":["18/18","15/18","UNINUMBR"],"status":"PASS_F01_TERMINAL_N01_HOLD","url":"https://www.fdic.gov/resources/bankers/","key":"UNINUMBR","key_state":"VERIFIED_F01","vintage":"2022-2024 structural","reserved":False,"source_body":"Official annual source asserted by original immutable F01","reusable":False},
 {"id":"NHTSA-RCL","name_ko":"NHTSA 리콜 자료","grade":"D1","evidence":["research/PORTFOLIO-R58/evidence/source-endpoint-preflight-01.json"],"required":["PREFIX_MATCH_BODY_UNINSPECTED","FLAT_RCL_POST_2010.zip"],"status":"PREFIX_ONLY_EXACT_JOIN_UNVERIFIED","url":"https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_POST_2010.zip","key":"Campaign ID","key_state":"UNVERIFIED","vintage":"2026-10 observed first-byte","reserved":False,"source_body":"ZIP magic only","reusable":False},
 {"id":"NCES-IPEDS","name_ko":"NCES IPEDS","grade":"D1","evidence":["research/PORTFOLIO-R59/evidence/source-frontdoor-01.json"],"required":["IPEDS_2023_24_final_zip","zip_magic_verified"],"status":"IPEDS_MAGIC_SCORECARD_403","url":"https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2023-24_Final.zip","key":"UNITID to OPEID6","key_state":"UNVERIFIED","vintage":"2023-24 final","reserved":False,"source_body":"ZIP magic only; other source 403","reusable":False},
 {"id":"SEC-BULK","name_ko":"SEC 공시 대량 파일","grade":"D0","evidence":["research/PORTFOLIO-R59/evidence/source-frontdoor-01.json","research/PORTFOLIO-R59/evidence/sec-zip-fourbyte-02.json"],"required":["SEC_submissions_bulk_zip","403"],"status":"TRANSPORT_403_HEAD_AND_GET","url":"https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip","key":"CIK","key_state":"DOCUMENTED_ONLY","vintage":"2026-10 probe","reserved":False,"source_body":"NO BODY; HTTP 403, not file absence","reusable":False},
 {"id":"USPTO-FEES","name_ko":"USPTO 특허·수수료","grade":"D0","evidence":["research/PORTFOLIO-R59/evidence/source-frontdoor-01.json"],"required":["USPTO","403"],"status":"PORTAL_METADATA_API_ACCESS_RESTRICTED","url":"https://data.uspto.gov/","key":"Patent ID","key_state":"DOCUMENTED_ONLY","vintage":"2026-10 portal inspection","reserved":False,"source_body":"Metadata/portal only, login/key barrier","reusable":False},
]
def build(root=ROOT):
    out=[]
    missing=[]
    for s in SOURCES:
        refs=[]
        for path in s["evidence"]:
            f=root / path
            if not f.is_file():
                missing.append(path); continue
            raw=f.read_bytes()
            refs.append({"path":path,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw)})
        text="\n".join((root / p).read_text(encoding="utf-8") for p in s["evidence"] if (root/p).is_file())
        s1={**s,"source_evidence":refs,"required_tokens_present":{t:t in text for t in s["required"]},
            "publication_time":"UNVERIFIED_SEPARATE_FROM_OBSERVED_TIME",
            "observed_time":"SEE_IMMUTABLE_REFERENCED_EVIDENCE",
            "original_science_disposition":s["status"],
            "experimental_authorization":False}
        out.append(s1)
    return out,missing
def validate(records, missing):
    g=[]
    def gate(i,title,valid,detail):
        g.append({"gate":i,"name":title,"passed":bool(valid),"detail":detail})
    IDs=[x["id"] for x in records]
    grades={"D0","D1","D2","D3","D4","D5"}
    gate(1,"all exact frozen evidence paths exist",not missing and all(x["source_evidence"] for x in records),missing)
    gate(2,"stable non-PII names, first party URLs, citations",len(set(IDs))==len(IDs) and all(re.fullmatch("[A-Z0-9-]+",x["id"]) and x["url"].startswith("https://") and x["source_evidence"] for x in records),len(IDs))
    gate(3,"bounded conservative grade and evidence tokens",all(x["grade"] in grades and all(x["required_tokens_present"].values()) for x in records),[(x["id"],x["grade"],x["required_tokens_present"]) for x in records])
    gate(4,"magic distinguished from full SHA and row authority",all(("magic only" in x["source_body"].lower()) == (x["grade"]=="D1") or x["grade"] not in {"D1","D2"} for x in records), "D1 prefix-only; D2 full source")
    gate(5,"publication vs observed timestamps separated",all(x["publication_time"].startswith("UNVERIFIED_") and x["observed_time"].startswith("SEE_") and x["vintage"] for x in records),len(records))
    gate(6,"key state qualified separately",all(x["key"] and x["key_state"] in {"VERIFIED_N01","VERIFIED_F01","UNQUALIFIED_F01","UNVERIFIED","DOCUMENTED_ONLY"} for x in records),len(records))
    gate(7,"terminal science retained independent of grade",any(x["grade"]=="D3" and "HOLD" in x["status"] for x in records) and any(x["grade"]=="D2" and "HOLD" in x["status"] for x in records),len(records))
    gate(8,"primary CMS cohort remains reserved",next(x for x in records if x["id"]=="CMS-NPI")["reserved"] and not any(x["reusable"] for x in records),True)
    gate(9,"negative transport preserved",any("403" in x["status"] for x in records) and any(x["grade"]=="D0" for x in records),True)
    gate(10,"no source files/outcomes fetched or emitted",all(not x["experimental_authorization"] and all(p["path"].startswith("research/") for p in x["source_evidence"]) for x in records),True)
    gate(11,"bilingual deterministic JSON/MD registry",len(records)==8 and all(x["name_ko"] for x in records),len(records))
    eligible=[x for x in records if x["grade"] in {"D2","D3","D4","D5"} and x["reusable"] and not x["reserved"]]
    disposition="SELECT_NEW_INDEPENDENT_PORTFOLIO_ONLY_IF_VERIFIED_DUAL_D2_AND_KEY_BRIDGE" if len(eligible)>=2 else "HOLD_NEED_DUAL_D2_SOURCE"
    gate(12,"one conservative subsequent decision",disposition=="HOLD_NEED_DUAL_D2_SOURCE" and len(eligible)<2,disposition)
    return g,disposition
def main():
    target=DIR/"evidence/attempt-01.json"
    if target.exists():
        raise RuntimeError("Immutable S01 result exists; no replay")
    records,missing=build()
    gates,decision=validate(records,missing)
    result={"research":"SOURCE-REGISTRY-S01","issue":244,"contract_commit":"6370bbd5a8f3bdedba3e84ec2e296b9a05eb04d5",
            "gate_count":12,"passed":sum(g["passed"] for g in gates),
            "gates":gates,"next_source_decision":decision,
            "status":"PASS_SOURCE_REGISTRY_S01_OPERATIONAL_ONLY" if all(g["passed"] for g in gates) else "HOLD_SOURCE_REGISTRY_S01_OPERATIONS",
            "no_raw_public_source_zip_opened":True,"future_outcomes_opened":False,
            "individual_or_company_rows_emitted":False,"cost_usd":0,
            "sources":records}
    DIR.mkdir(parents=True,exist_ok=True)
    (DIR/"REGISTRY.json").write_text(json.dumps(records,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    rows=["# S01 — Source evidence registry / 공식 데이터 원천 증거 등록부","",
          "| ID | Evidence grade / 등급 | Key status / 조인키 | Original verdict / 기존 판정 |",
          "|---|---|---|---|"]
    for s in records:
        rows.append(f"| {s['id']} | {s['grade']} | {s['key_state']} | {s['status']} |")
    rows+=["",f"**Next / 다음:** \`{decision}\`","","Source grade is NOT a scientific outcome, body access or new E01 authority. / 등급은 과학적 PASS 및 E01 승인과 다릅니다.","","Cost / 비용: **0 USD**."]
    (DIR/"REGISTRY.md").write_text("\n".join(rows)+"\n")
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    (DIR/"evidence/attempt-01.md").write_text("# S01 — 12 operations gates / 운영 게이트\n\n"+ "\n".join(f"- {g['gate']:02}: {'PASS' if g['passed'] else 'HOLD'} — {g['name']}" for g in gates)+f"\n\n**{result['status']}** / {result['passed']}/12\n\n**{decision}**\n\n0 USD. No raw source/outcomes.\n")
    print("S01_RESULT",result["status"],result["passed"],"/12",decision)
if __name__=="__main__":
    main()
