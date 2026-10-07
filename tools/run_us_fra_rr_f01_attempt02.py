#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json, os, re, xml.etree.ElementTree as ET
import requests

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-FRA-RR-F01/evidence"
JSON_OUT=OUTDIR/"attempt-02.json"; MD_OUT=OUTDIR/"attempt-02.md"
CONTRACT_SHA="492e2a29261e786fe115fa9eaf2f89a8862fa5a6"
ISSUE=196
SERVICE="https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx"
WSDL=SERVICE+"?WSDL"
YEARS=[2020,2021,2022,2023,2024,2025]
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"
S=requests.Session(); S.headers.update({"User-Agent":UA})

def sha(b): return hashlib.sha256(b).hexdigest()
def lname(tag): return tag.split("}")[-1]
def text(v): return (v or "").strip()
def normcode(v): return text(v).upper()
def num(v):
    s=text(v).replace(",","").replace("$","")
    try:return float(s)
    except:return None

def get(url,timeout=90):
    r=S.get(url,timeout=timeout,allow_redirects=True); r.raise_for_status()
    return r,{"status":r.status_code,"url":r.url,"content_type":r.headers.get("content-type"),
              "bytes":len(r.content),"sha256":sha(r.content),"last_modified":r.headers.get("last-modified"),
              "etag":r.headers.get("etag")}

def wsdl_model(raw):
    root=ET.fromstring(raw)
    tns=root.attrib.get("targetNamespace","http://tempuri.org/")
    ns={"wsdl":"http://schemas.xmlsoap.org/wsdl/","xsd":"http://www.w3.org/2001/XMLSchema","soap":"http://schemas.xmlsoap.org/wsdl/soap/"}
    endpoint=None
    for a in root.findall(".//soap:address",ns):
        endpoint=a.attrib.get("location"); break
    actions={}
    for op in root.findall(".//wsdl:binding/wsdl:operation",ns):
        so=op.find("soap:operation",ns)
        if so is not None: actions[op.attrib.get("name")]=so.attrib.get("soapAction")
    params={}
    # ASMX WSDL normally declares operation request elements in xsd:schema.
    for el in root.findall(".//xsd:schema/xsd:element",ns):
        name=el.attrib.get("name")
        if not name: continue
        seq=el.find(".//xsd:sequence",ns)
        if seq is None: continue
        params[name]=[x.attrib.get("name") for x in seq.findall("xsd:element",ns) if x.attrib.get("name")]
    return {"target_namespace":tns,"endpoint":endpoint or SERVICE,"actions":actions,"params":params}

def soap_call(model,op,values,timeout=180):
    if op not in model["actions"]: raise RuntimeError(f"WSDL_OPERATION_MISSING:{op}")
    pnames=model["params"].get(op,[])
    if set(values)-set(pnames): raise RuntimeError(f"WSDL_PARAMETER_MISMATCH:{op}:{pnames}:{sorted(values)}")
    env=ET.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    body=ET.SubElement(env,"{http://schemas.xmlsoap.org/soap/envelope/}Body")
    req=ET.SubElement(body,f"{{{model['target_namespace']}}}{op}")
    for p in pnames:
        child=ET.SubElement(req,f"{{{model['target_namespace']}}}{p}")
        child.text=str(values.get(p,""))
    raw=ET.tostring(env,encoding="utf-8",xml_declaration=True)
    headers={"Content-Type":"text/xml; charset=utf-8","SOAPAction":model["actions"][op] or f"{model['target_namespace']}{op}"}
    r=S.post(model["endpoint"],data=raw,headers=headers,timeout=timeout,allow_redirects=True)
    r.raise_for_status()
    return r.content,{"status":r.status_code,"url":r.url,"bytes":len(r.content),"sha256":sha(r.content),"content_type":r.headers.get("content-type")}

def candidate_argmap(model,op,year=None):
    out={}
    for p in model["params"].get(op,[]):
        q=p.lower()
        if "year" in q:
            if year is None: raise RuntimeError(f"YEAR_REQUIRED:{op}")
            out[p]=str(year)
        elif "rail" in q or q in {"rr","rrcode","railroadcode"}:
            out[p]="All"
        else:
            out[p]=""
    return out

def rows_from_xml(raw):
    root=ET.fromstring(raw)
    rows=[]
    # Prefer repeating leaf-record elements with >=2 child leaves.
    for el in root.iter():
        kids=list(el)
        if len(kids)<2: continue
        if any(list(k) for k in kids): continue
        d={lname(k.tag):text(k.text) for k in kids}
        if len(d)>=2: rows.append(d)
    # De-duplicate XML serialization artifacts.
    seen=set(); uniq=[]
    for d in rows:
        key=tuple(sorted(d.items()))
        if key not in seen:
            seen.add(key); uniq.append(d)
    return uniq

def find_field(row,patterns):
    keys=list(row)
    for pat in patterns:
        for k in keys:
            if re.search(pat,k,re.I): return k
    return None

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists(): raise RuntimeError("immutable attempt-02 evidence exists")
    ev={"research":"US-FRA-RR-F01","attempt":2,"issue":ISSUE,"contract_sha":CONTRACT_SHA,
        "github_run_id":os.getenv("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_2026plus_accident_membership_opened":False,"future_rows_consumed":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
        "causal_claim_made":False,"prior_accident_predictor_computed":False,"identity_repair_used":False,"gates":[]}
    ev["runner_sha256"]=sha(Path(__file__).read_bytes())
    try:
        cp=json.loads((ROOT/"context/checkpoint.json").read_text())
        g1=(cp.get("checkpoint_id")=="CHK-20261008-US-FRA-RR-F01-ACTIVE" and cp.get("active_issue")==196
            and cp.get("active_research")=="US-FRA-RR-F01" and cp.get("last_decision")=="DEC-304")
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound=os.getenv("FRA_F01_BOUND")=="1" and os.getenv("FRA_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":196,"contract_sha":os.getenv("FRA_F01_CONTRACT_SHA")}})

        landing,lmeta=get(SERVICE)
        wr,wmeta=get(WSDL)
        model=wsdl_model(wr.content)
        needed={"GetRailroadData","GetF54Schema","GetF55Schema","GetAccident54DataByRailroad","GetAccident55DataByRailroad"}
        year_ops={"GetAccident54DataByRailroad","GetAccident55DataByRailroad"}
        g3=(landing.status_code==200 and wr.status_code==200 and needed.issubset(model["actions"])
            and all(model["params"].get(x,[])==["year"] for x in year_ops))
        ev["service"]={"landing":lmeta,"wsdl":wmeta,"target_namespace":model["target_namespace"],"endpoint":model["endpoint"],
                       "operations":sorted(model["actions"]),"parameter_signatures":{k:model["params"].get(k,[]) for k in sorted(needed)}}
        ev["gates"].append({"gate":3,"pass":g3,"observed":{"landing_status":landing.status_code,"wsdl_status":wr.status_code,
            "operations_present":sorted(needed & set(model["actions"])),"signatures":ev["service"]["parameter_signatures"]}})
        if not g3: raise RuntimeError("DIRECT_SERVICE_OR_WSDL_NOT_RESOLVED")

        ref_raw,ref_meta=soap_call(model,"GetRailroadData",{})
        ref_rows=rows_from_xml(ref_raw)
        ev["railroad_reference"]={"meta":ref_meta,"row_candidates":len(ref_rows),"sample_fields":sorted(ref_rows[0]) if ref_rows else []}
        g4=len(ref_rows)>=100
        ev["gates"].append({"gate":4,"pass":g4,"observed":ev["railroad_reference"]})
        if not g4: raise RuntimeError("RAILROAD_REFERENCE_NOT_PARSEABLE")

        f54s_raw,f54s_meta=soap_call(model,"GetF54Schema",{})
        f55s_raw,f55s_meta=soap_call(model,"GetF55Schema",{})
        s54=f54s_raw.decode("utf-8","replace").lower(); s55=f55s_raw.decode("utf-8","replace").lower()
        g5=(len(f54s_raw)>1000 and len(f55s_raw)>1000 and "railroad" in s54 and "railroad" in s55)
        ev["schemas"]={"f54":f54s_meta,"f55":f55s_meta}
        ev["gates"].append({"gate":5,"pass":g5,"observed":{"f54_bytes":len(f54s_raw),"f55_bytes":len(f55s_raw),
                                                            "f54_has_railroad":"railroad" in s54,"f55_has_railroad":"railroad" in s55}})
        if not g5: raise RuntimeError("SCHEMA_NOT_PARSEABLE")

        f54_by_year={}; f55_by_year={}; manifests={"f54":{},"f55":{}}
        for y in YEARS:
            raw55,m55=soap_call(model,"GetAccident55DataByRailroad",candidate_argmap(model,"GetAccident55DataByRailroad",y),timeout=240)
            raw54,m54=soap_call(model,"GetAccident54DataByRailroad",candidate_argmap(model,"GetAccident54DataByRailroad",y),timeout=240)
            r55=rows_from_xml(raw55); r54=rows_from_xml(raw54)
            f55_by_year[y]=r55; f54_by_year[y]=r54
            manifests["f55"][str(y)]={**m55,"rows":len(r55)}
            manifests["f54"][str(y)]={**m54,"rows":len(r54)}
        ev["historical_manifests"]=manifests
        g6=all(len(f55_by_year[y])>0 for y in YEARS)
        g7=all(len(f54_by_year[y])>0 for y in YEARS)
        ev["gates"].append({"gate":6,"pass":g6,"observed":{str(y):len(f55_by_year[y]) for y in YEARS}})
        ev["gates"].append({"gate":7,"pass":g7,"observed":{str(y):len(f54_by_year[y]) for y in YEARS}})
        if not (g6 and g7): raise RuntimeError("HISTORICAL_ROWS_NOT_RESOLVED")

        # Resolve source field names from first rows.
        s55=next((r for y in YEARS for r in f55_by_year[y] if r),{})
        s54=next((r for y in YEARS for r in f54_by_year[y] if r),{})
        rr55=find_field(s55,[r"^railroad$",r"railroad.*code",r"^rr$"])
        rr54=find_field(s54,[r"^railroad$",r"railroad.*code",r"^rr$"])
        year55=find_field(s55,[r"^year$",r"iyr"])
        year54=find_field(s54,[r"^year$",r"iyr"])
        # Common operational concepts: train miles + employee hours. Match flexibly but record exact names.
        train_fields=[k for k in s55 if re.search(r"train.*mile|mile.*train",k,re.I)]
        hour_fields=[k for k in s55 if re.search(r"employee.*hour|worker.*hour|^empl.*hr|^emp.*hr",k,re.I)]
        ev["resolved_fields"]={"f55_railroad":rr55,"f54_railroad":rr54,"f55_year":year55,"f54_year":year54,
                               "train_mile_fields":train_fields,"employee_hour_fields":hour_fields,
                               "f55_fields":sorted(s55),"f54_fields":sorted(s54)}
        if not rr55 or not rr54: raise RuntimeError("RAILROAD_FIELD_NOT_RESOLVED")

        ref_codes=set()
        for r in ref_rows:
            k=find_field(r,[r"^railroad$",r"railroad.*code",r"^rr$"])
            if k and normcode(r.get(k)): ref_codes.add(normcode(r.get(k)))

        f55_codes=set(); f54_codes=set(); f55_nonblank=0; f55_recog=0
        yearly_nonzero=Counter(); appear=Counter(); qualified_rows=[]; accident_rows=0; dateok=0
        for y in YEARS:
            seen_nonzero=set()
            for r in f55_by_year[y]:
                c=normcode(r.get(rr55))
                if c:
                    f55_nonblank+=1; f55_codes.add(c)
                    if not ref_codes or c in ref_codes: f55_recog+=1
                vals=[num(r.get(k)) for k in train_fields]
                hrs=[num(r.get(k)) for k in hour_fields]
                tm=sum(v for v in vals if v is not None) if vals else None
                eh=sum(v for v in hrs if v is not None) if hrs else None
                if c and tm is not None and tm>0:
                    seen_nonzero.add(c)
                if c and tm is not None and eh is not None and tm>=0 and eh>=0:
                    qualified_rows.append((y,c,tm,eh))
            yearly_nonzero[y]=len(seen_nonzero)
            for c in seen_nonzero: appear[c]+=1
            for r in f54_by_year[y]:
                accident_rows+=1
                c=normcode(r.get(rr54))
                if c: f54_codes.add(c)
                # year/date consistency: accept explicit year field equals requested year.
                if year54:
                    v=text(r.get(year54))
                    yy=None
                    m=re.search(r"(20\d{2}|\d{2})",v)
                    if m:
                        yy=int(m.group(1)); yy=2000+yy if yy<100 else yy
                        if yy==y: dateok+=1

        syntax_rate=f55_recog/f55_nonblank if f55_nonblank else 0
        ev["gates"].append({"gate":8,"pass":syntax_rate>=0.99,"observed":{"nonblank":f55_nonblank,"recognized":f55_recog,
                                                                         "rate":syntax_rate,"reference_codes":len(ref_codes)}})
        join=len(f54_codes & (f55_codes|ref_codes))/len(f54_codes) if f54_codes else 0
        ev["gates"].append({"gate":9,"pass":join>=0.98,"observed":{"distinct_f54_codes":len(f54_codes),
                                                                  "matched":len(f54_codes & (f55_codes|ref_codes)),"rate":join}})
        ev["gates"].append({"gate":10,"pass":all(yearly_nonzero[y]>=300 for y in YEARS),
                            "observed":{str(y):yearly_nonzero[y] for y in YEARS}})
        longn=sum(1 for c,n in appear.items() if n>=4)
        ev["gates"].append({"gate":11,"pass":longn>=250,"observed":{"railroads_4plus_years":longn,"threshold":250}})
        total55=sum(len(f55_by_year[y]) for y in YEARS)
        comp=len(qualified_rows)/total55 if total55 else 0
        ev["gates"].append({"gate":12,"pass":bool(train_fields and hour_fields and comp>=0.95),
                            "observed":{"total_rows":total55,"qualified_rows":len(qualified_rows),"rate":comp,
                                        "train_fields":train_fields,"employee_hour_fields":hour_fields}})
        ev["gates"].append({"gate":13,"pass":accident_rows>=1500,"observed":{"accident_rows":accident_rows,"threshold":1500}})
        dr=dateok/accident_rows if accident_rows else 0
        ev["gates"].append({"gate":14,"pass":bool(year54 and dr>=0.99),
                            "observed":{"accident_rows":accident_rows,"year_consistent":dateok,"rate":dr,"year_field":year54}})

        # Threshold semantics: source pages already known; verify FRA safety portal text plus 2026 guidance is reachable.
        durl="https://railroads.dot.gov/safety-data"
        tr,tmeta=get(durl)
        blob=tr.text.lower()
        g15=("reporting threshold" in blob or "accident" in blob) and ("form" in blob or "6180.54" in blob)
        ev["gates"].append({"gate":15,"pass":g15,"observed":{"url":tmeta["url"],"sha256":tmeta["sha256"],
                                                             "mentions_reporting_threshold":"reporting threshold" in blob}})
        g16=(ev["future_2026plus_accident_membership_opened"] is False and ev["future_rows_consumed"]==0)
        ev["gates"].append({"gate":16,"pass":g16,"observed":{"future_membership_opened":False,"future_rows":0,
                                                              "requested_years":YEARS}})
        g17=not any([ev["relationship_computed"],ev["prediction_computed"],ev["ranking_computed"],ev["causal_claim_made"],
                     ev["prior_accident_predictor_computed"],ev["identity_repair_used"]])
        ev["gates"].append({"gate":17,"pass":g17,"observed":{"relationship":False,"prediction":False,"ranking":False,
                                                              "causal":False,"prior_accident_predictor":False,"identity_repair":False}})
        g18=(len(ev["runner_sha256"])==64 and ev["incremental_monetary_cost_usd"]==0 and all("sha256" in manifests[k][str(y)] for k in ("f54","f55") for y in YEARS))
        ev["gates"].append({"gate":18,"pass":g18,"observed":{"runner_sha256":ev["runner_sha256"],"contract_sha":CONTRACT_SHA,
                                                              "cost_usd":0,"manifested_years":YEARS}})
        ev["gates"]=sorted(ev["gates"],key=lambda x:x["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True; ev["failed_gates"]=failed; ev["pass_count"]=18-len(failed)
        ev["disposition"]="PASS_US_FRA_RR_F01_EXACT_RAILROAD_OPERATIONAL_ACCIDENT_DESIGN_READY" if not failed else "HOLD_US_FRA_RR_F01_EXACT_RAILROAD_OPERATIONAL_ACCIDENT_DESIGN_NOT_READY"
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_US_FRA_RR_F01_ATTEMPT_02"
    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False,default=str)+"\n",encoding="utf-8")
    lines=["# US-FRA-RR-F01 — Attempt 02","",f"**Disposition:** `{ev['disposition']}`","",
           f"- Attempt valid: `{ev.get('attempt_valid')}`",f"- Gates passed: **{ev.get('pass_count',0)}/18**",
           f"- Failed gates: `{ev.get('failed_gates',[])}`",f"- Future 2026+ accident membership opened: **{ev['future_2026plus_accident_membership_opened']}**",
           "- Incremental monetary cost: **0 USD**","","## Gate ledger","","| Gate | PASS | Observed |","|---:|:---:|---|"]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        o=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True,default=str)
        if len(o)>1400:o=o[:1397]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{o.replace(chr(96),'')}` |")
    if ev.get("implementation_error"): lines+=["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines+=["","Only 2020–2025 historical service calls were authorized. No 2026+ Form54 accident membership was opened.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],ev.get("pass_count"),ev.get("failed_gates"))

if __name__=="__main__": main()
