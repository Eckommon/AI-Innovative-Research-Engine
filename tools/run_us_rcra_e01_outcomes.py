#!/usr/bin/env python3
"""US-RCRA-E01 Pass 2: open only frozen selected-pair FOUND_VIOLATION values."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import os
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-RCRA-E01"
PAIR_P = OUT / "PAIR_MANIFEST.json"
TMP = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "us-rcra-e01"
TMP.mkdir(parents=True, exist_ok=True)
RCRA_URL = "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip"
UA = "AI-Innovative-Research-Engine/US-RCRA-E01 preregistered paired outcome test"

pair_manifest = json.loads(PAIR_P.read_text(encoding="utf-8"))
assert pair_manifest["issue"] == 125
assert pair_manifest["outcomes_opened"] is False
assert pair_manifest["found_violation_values_accessed_or_persisted"] is False
assert pair_manifest["pair_count"] == 297
assert pair_manifest["state_territory_fips_count"] == 43
pairs = pair_manifest["pairs"]
canonical = json.dumps(pairs, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
fp = hashlib.sha256(canonical).hexdigest()
assert fp == pair_manifest["pair_identity_sha256"], (fp, pair_manifest["pair_identity_sha256"])

# Exact selected row keys only. Date is part of validation, not pair selection.
selected: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
for p in pairs:
    rid = p["id_number"]
    selected[(rid, p["pre_evaluation_identifier"])].append(("pre", p["pre_cei_date"]))
    selected[(rid, p["post_evaluation_identifier"])].append(("post", p["post_cei_date"]))

zip_path = TMP / "rcra_downloads.zip"
req = urllib.request.Request(RCRA_URL, headers={"User-Agent": UA, "Accept": "*/*"})
h = hashlib.sha256(); total = 0
with urllib.request.urlopen(req, timeout=300) as r, open(zip_path, "wb") as f:
    while True:
        chunk = r.read(1024 * 1024)
        if not chunk: break
        f.write(chunk); h.update(chunk); total += len(chunk)
if not zipfile.is_zipfile(zip_path):
    raise RuntimeError("RCRA source is not a ZIP")

rows_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
with zipfile.ZipFile(zip_path) as z:
    hits = [n for n in z.namelist() if n.rsplit("/",1)[-1].casefold() == "rcra_evaluations.csv"]
    if len(hits) != 1: raise RuntimeError(f"expected one RCRA_EVALUATIONS.csv: {hits}")
    raw = z.open(hits[0]); text = io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")
    reader = csv.DictReader(text)
    fields = set(reader.fieldnames or [])
    required = {"ID_NUMBER","EVALUATION_IDENTIFIER","EVALUATION_TYPE","EVALUATION_START_DATE","EVALUATION_AGENCY","FOUND_VIOLATION"}
    miss = sorted(required - fields)
    if miss: raise RuntimeError(f"missing evaluation headers: {miss}")
    for r in reader:
        key = ((r.get("ID_NUMBER") or "").strip().upper(), (r.get("EVALUATION_IDENTIFIER") or "").strip())
        if key in selected:
            rows_by_key[key].append({k:(r.get(k) or "").strip() for k in required})

# Raw bytes are transient.
try: zip_path.unlink()
except FileNotFoundError: pass

resolved: dict[tuple[str,str], dict[str,str]] = {}
for key, expected_uses in selected.items():
    rows = rows_by_key.get(key, [])
    # Exact identifier must resolve one CEI row; no post-value fuzzy repair.
    cei_rows = [r for r in rows if r["EVALUATION_TYPE"].upper() == "CEI"]
    if len(cei_rows) != 1:
        raise RuntimeError(f"selected evaluation identity does not resolve uniquely: {key} count={len(cei_rows)}")
    row = cei_rows[0]
    expected_dates = {d for _, d in expected_uses}
    # Identifier reuse across role would still need the one exact frozen date.
    if len(expected_dates) != 1 or row["EVALUATION_START_DATE"] not in expected_dates:
        # tolerate source MM/DD/YYYY versus frozen ISO only by deterministic parse conversion
        from datetime import datetime
        try:
            iso = datetime.strptime(row["EVALUATION_START_DATE"][:10], "%m/%d/%Y").date().isoformat()
        except ValueError:
            try: iso = datetime.strptime(row["EVALUATION_START_DATE"][:10], "%Y-%m-%d").date().isoformat()
            except ValueError: iso = ""
        if len(expected_dates) != 1 or iso not in expected_dates:
            raise RuntimeError(f"selected evaluation date drift: {key} got={row['EVALUATION_START_DATE']} expected={expected_dates}")
    resolved[key] = row

if len(resolved) != len(selected):
    raise RuntimeError(f"selected identity coverage drift: {len(resolved)}/{len(selected)}")

value_counts_pre = Counter(); value_counts_post = Counter()
contingency = Counter()
records = []
agency_changes = 0
pre_distances=[]; post_distances=[]
hazard_diag: dict[str, Counter] = defaultdict(Counter)
same_agency_pairs=[]

def outcome_class(v: str) -> str:
    u = (v or "").strip().upper()
    if u in {"Y","N","U"}: return u
    return "BLANK_OTHER"

for p in pairs:
    pre = resolved[(p["id_number"], p["pre_evaluation_identifier"])]
    post = resolved[(p["id_number"], p["post_evaluation_identifier"])]
    a = outcome_class(pre["FOUND_VIOLATION"]); b = outcome_class(post["FOUND_VIOLATION"])
    value_counts_pre[a]+=1; value_counts_post[b]+=1
    same_agency = pre["EVALUATION_AGENCY"] == post["EVALUATION_AGENCY"]
    if not same_agency: agency_changes += 1
    index_d = date.fromisoformat(p["index_date"])
    pre_d = date.fromisoformat(p["pre_cei_date"]); post_d = date.fromisoformat(p["post_cei_date"])
    pre_distances.append((index_d-pre_d).days); post_distances.append((post_d-index_d).days)
    analyzable = a in {"Y","N"} and b in {"Y","N"}
    if analyzable:
        contingency[a+b]+=1
        hazard_diag[p["index_incident_type"]][a+b]+=1
        if same_agency: same_agency_pairs.append((a,b))
    records.append((a,b,same_agency,p["index_incident_type"]))

n_nn=contingency["NN"]; n_ny=contingency["NY"]; n_yn=contingency["YN"]; n_yy=contingency["YY"]
n = n_nn+n_ny+n_yn+n_yy
discordant = n_ny+n_yn

def exact_mcnemar_p(ny:int, yn:int) -> float | None:
    m=ny+yn
    if m==0: return None
    lo=min(ny,yn)
    tail=sum(math.comb(m,k) for k in range(lo+1))/(2**m)
    return min(1.0, 2.0*tail)

p_exact = exact_mcnemar_p(n_ny,n_yn)
if n < 100 or discordant < 20:
    gate="HOLD_US_RCRA_E01_INSUFFICIENT_OUTCOME_SUPPORT"
    rd = None if n==0 else (n_ny-n_yn)/n
else:
    rd=(n_ny-n_yn)/n
    assert p_exact is not None
    if rd >= 0.05 and p_exact < 0.05:
        gate="PASS_POSITIVE_MATERIAL_US_RCRA_E01_RELATIONSHIP"
    elif 0 < rd < 0.05 and p_exact < 0.05:
        gate="POSITIVE_BELOW_MATERIALITY_US_RCRA_E01_RELATIONSHIP"
    else:
        gate="NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP"

pre_risk = None if n==0 else (n_yy+n_yn)/n
post_risk = None if n==0 else (n_yy+n_ny)/n
same_ct=Counter(a+b for a,b in same_agency_pairs)
same_n=sum(same_ct.values()); same_disc=same_ct["NY"]+same_ct["YN"]
same_diag={"analyzable_pairs":same_n,"discordant_pairs":same_disc}
if same_n>=50 and same_disc>=10:
    same_diag.update({
        "n_NN":same_ct["NN"],"n_NY":same_ct["NY"],"n_YN":same_ct["YN"],"n_YY":same_ct["YY"],
        "risk_difference":(same_ct["NY"]-same_ct["YN"])/same_n,
        "p_exact_two_sided":exact_mcnemar_p(same_ct["NY"],same_ct["YN"]),
    })

manifest={
    "id":"US-RCRA-E01-EXECUTION-RESULT","issue":125,"gate":gate,
    "pair_identity_sha256":fp,"pair_count_frozen":297,"state_territory_fips_count_frozen":43,
    "pair_identity_drift":False,"selected_outcomes_opened":True,"relationship_computed": n>=100 and discordant>=20,
    "source":{"rcra_url":RCRA_URL,"bytes_transient":total,"sha256":h.hexdigest(),"raw_source_bytes_persisted":False},
    "outcome_coding":{"Y":1,"N":0,"U":"missing","blank_or_other":"missing"},
    "value_counts":{"pre":dict(value_counts_pre),"post":dict(value_counts_post)},
    "primary_support":{"analyzable_pairs":n,"discordant_pairs":discordant,"minimum_analyzable":100,"minimum_discordant":20},
    "primary":{"n_NN":n_nn,"n_NY":n_ny,"n_YN":n_yn,"n_YY":n_yy,"pre_risk":pre_risk,"post_risk":post_risk,"risk_difference":rd,"p_exact_two_sided_mcnemar":p_exact,"materiality_floor":0.05},
    "diagnostics_non_rescuing":{
        "agency_change_pairs":agency_changes,"agency_change_fraction":agency_changes/297,
        "same_agency_subset":same_diag,
        "pre_cei_distance_days":{"min":min(pre_distances),"max":max(pre_distances),"mean":sum(pre_distances)/len(pre_distances)},
        "post_cei_distance_days":{"min":min(post_distances),"max":max(post_distances),"mean":sum(post_distances)/len(post_distances)},
        "hazard_contingencies":{k:dict(v) for k,v in sorted(hazard_diag.items())},
    },
    "claim_boundary":"non-causal monitoring/compliance association; FOUND_VIOLATION is an inspection-result field",
    "incremental_monetary_cost_usd":0,
}
(OUT/"EXECUTION_RESULT.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"gate":gate,"n":n,"discordant":discordant,"RD":rd,"p":p_exact},indent=2))
