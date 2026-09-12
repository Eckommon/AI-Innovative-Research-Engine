#!/usr/bin/env python3
"""Audit frozen selected CEI duplicate identities using NON-OUTCOME columns only."""
from __future__ import annotations
import csv, io, json, os, urllib.request, zipfile
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"research"/"US-RCRA-E01"
TMP=Path(os.environ.get("RUNNER_TEMP","/tmp"))/"us-rcra-e01-dup-audit"; TMP.mkdir(parents=True,exist_ok=True)
URL="https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"; UA="AI-Innovative-Research-Engine/US-RCRA-E01 duplicate identity audit"

def iso(s):
    s=(s or "").strip()
    for fmt,n in (("%m/%d/%Y",10),("%Y-%m-%d",10),("%Y-%m-%dT%H:%M:%S",19)):
        try:return datetime.strptime(s[:n],fmt).date().isoformat()
        except ValueError:pass
    return ""
pm=json.loads((OUT/"PAIR_MANIFEST.json").read_text())
selected=set()
for p in pm["pairs"]:
    selected.add((p["id_number"],p["pre_cei_date"],p["pre_evaluation_identifier"]))
    selected.add((p["id_number"],p["post_cei_date"],p["post_evaluation_identifier"]))

zp=TMP/"r.zip"; req=urllib.request.Request(URL,headers={"User-Agent":UA})
with urllib.request.urlopen(req,timeout=300) as r,open(zp,"wb") as f:
    while True:
        b=r.read(1024*1024)
        if not b:break
        f.write(b)

groups=defaultdict(list); non_outcome_headers=[]
with zipfile.ZipFile(zp) as z:
    name=[n for n in z.namelist() if n.rsplit('/',1)[-1].casefold()=="rcra_evaluations.csv"][0]
    reader=csv.DictReader(io.TextIOWrapper(z.open(name),encoding="utf-8-sig",errors="replace",newline=""))
    headers=reader.fieldnames or []
    assert "FOUND_VIOLATION" in headers
    non_outcome_headers=[h for h in headers if h!="FOUND_VIOLATION"]
    for r in reader:
        key=((r.get("ID_NUMBER") or "").strip().upper(),iso(r.get("EVALUATION_START_DATE")),(r.get("EVALUATION_IDENTIFIER") or "").strip())
        if key in selected and (r.get("EVALUATION_TYPE") or "").strip().upper()=="CEI":
            groups[key].append(tuple((r.get(h) or "").strip() for h in non_outcome_headers))
try:zp.unlink()
except:pass

duplicates={k:v for k,v in groups.items() if len(v)>1}
summary=[]; diff_columns=Counter(); exact_nonoutcome_dupe=0
for key,rows in sorted(duplicates.items()):
    uniq=set(rows)
    differing=[]
    if len(uniq)==1:exact_nonoutcome_dupe+=1
    else:
        for i,h in enumerate(non_outcome_headers):
            if len({r[i] for r in rows})>1:
                differing.append(h); diff_columns[h]+=1
    summary.append({"id_number":key[0],"cei_date":key[1],"evaluation_identifier":key[2],"source_row_count":len(rows),"unique_nonoutcome_signatures":len(uniq),"differing_nonoutcome_columns":differing})

out={"id":"US-RCRA-E01-DUPLICATE-IDENTITY-AUDIT","issue":125,"outcome_field_read":False,"outcome_field_persisted":False,"selected_identity_count":len(selected),"resolved_identity_count":len(groups),"duplicate_identity_count":len(duplicates),"exact_duplicate_on_all_nonoutcome_columns":exact_nonoutcome_dupe,"nonoutcome_differing_column_counts":dict(diff_columns),"duplicates":summary,"incremental_monetary_cost_usd":0}
(OUT/"DUPLICATE_IDENTITY_AUDIT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({k:out[k] for k in ["selected_identity_count","resolved_identity_count","duplicate_identity_count","exact_duplicate_on_all_nonoutcome_columns","nonoutcome_differing_column_counts"]},indent=2))
