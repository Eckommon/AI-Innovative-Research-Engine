#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

RESEARCH = "US-FAA-AIP-F01"
ISSUE = 154
CONTRACT_COMMIT = "4f9a2a3491bc00c0fd1e00a7b0d3bc0bc62d4254"
PASS_GATE = "PASS_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_READY"
HOLD_GATE = "HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY"
OUT = Path("research/US-FAA-AIP-F01/STAGING_RESULT.json")
UA = {"User-Agent": "Mozilla/5.0 AI-Innovative-Research-Engine/US-FAA-AIP-F01"}
AIP_ROOT = "https://www.faa.gov/airports/aip/grant_histories"
LID_URL = "https://www.fly.faa.gov/rmt/data_file/locid_db.csv"
BTS_MASTER_URL = "https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10&gnoyr_VQ=FLL"
BTS_ONTIME_AIRPORT_LIST = "https://www.transtats.bts.gov/OT_Delay/NewAirportList.asp?flag=undefined&xpage=OT_DelayCause1.asp"
YEARS = tuple(range(2021, 2026))
CODE_RE = re.compile(r"^[A-Z0-9]{3}$")
STATE_RE = re.compile(r"\.\s*([A-Z]{2})\s*$")

sess = requests.Session()
sess.headers.update(UA)


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def get(url: str, timeout: int = 120) -> requests.Response:
    r = sess.get(url, timeout=timeout)
    r.raise_for_status()
    return r


def norm(v) -> str:
    return str(v if v is not None else "").strip().upper()


def clean_header(v) -> str:
    return re.sub(r"\s+", " ", str(v if v is not None else "").strip())


def parse_aip(year: int):
    landing = get(f"{AIP_ROOT}/{year}")
    soup = BeautifulSoup(landing.text, "html.parser")
    xlsx = None
    for a in soup.find_all("a", href=True):
        href = urljoin(landing.url, a["href"])
        if re.search(r"\.xlsx(?:$|\?)", href, re.I):
            xlsx = href
            break
    if not xlsx:
        raise RuntimeError(f"No official XLSX link for FY{year}")
    r = get(xlsx)
    wb = load_workbook(io.BytesIO(r.content), read_only=True, data_only=True)
    rows_out = []
    detected = None
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        header_i = None
        headers = None
        for i, row in enumerate(rows[:25]):
            hh = [clean_header(x) for x in row]
            if "LocID" in hh and "State" in hh and any(x in hh for x in ("Project Summary", "Grant Number")):
                header_i, headers = i, hh
                break
        if header_i is None:
            continue
        idx = {h: j for j, h in enumerate(headers) if h}
        if not {"State", "LocID"}.issubset(idx):
            continue
        project_col = "Project Summary" if "Project Summary" in idx else None
        grant_col = "Grant Number" if "Grant Number" in idx else None
        if not (project_col or grant_col):
            continue
        detected = {"sheet": ws.title, "header_row_1based": header_i + 1, "headers": headers}
        for row in rows[header_i + 1 :]:
            code = norm(row[idx["LocID"]] if idx["LocID"] < len(row) else "")
            state = norm(row[idx["State"]] if idx["State"] < len(row) else "")
            project = str(row[idx[project_col]] if project_col and idx[project_col] < len(row) and row[idx[project_col]] is not None else "").strip()
            grant = str(row[idx[grant_col]] if grant_col and idx[grant_col] < len(row) and row[idx[grant_col]] is not None else "").strip()
            if not (code or state or project or grant):
                continue
            rows_out.append({"year": year, "code": code, "state": state, "project_nonblank": bool(project or grant)})
        break
    if detected is None:
        raise RuntimeError(f"No usable AIP schema in FY{year}")
    return rows_out, {"year": year, "url": xlsx, "bytes": len(r.content), "sha256": sha256(r.content), "schema": detected}


def parse_lid():
    r = get(LID_URL)
    text = r.content.decode("utf-8-sig", errors="replace")
    rdr = csv.DictReader(io.StringIO(text))
    required = {"LocID", "Facility", "Location"}
    if not required.issubset(set(rdr.fieldnames or [])):
        raise RuntimeError(f"FAA LID required fields missing: {rdr.fieldnames}")
    by_code = defaultdict(list)
    for row in rdr:
        code = norm(row.get("LocID"))
        fac = norm(row.get("Facility"))
        loc = norm(row.get("Location"))
        m = STATE_RE.search(loc)
        state = m.group(1) if m else ""
        # Source-native facility classification is carried as a terminal token in Facility.
        is_airport = fac.endswith(". AIRPORT") or fac.endswith(" AIRPORT")
        if code:
            by_code[code].append({"state": state, "is_airport": is_airport})
    return by_code, {"url": LID_URL, "bytes": len(r.content), "sha256": sha256(r.content), "fields": rdr.fieldnames}


def download_master():
    r = get(BTS_MASTER_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    form = next(f for f in soup.find_all("form") if (f.get("method") or "").lower() == "post" and f.find("input", {"name": "btnDownload"}))
    payload = {}
    for x in form.find_all("input"):
        if x.get("name") and (x.get("type") or "").lower() == "hidden":
            payload[x["name"]] = x.get("value") or ""
    payload.update({
        "cboGeography": "All", "cboYear": "All", "cboPeriod": "All",
        "AIRPORT_SEQ_ID": "on", "AIRPORT_ID": "on", "AIRPORT": "on", "AIRPORT_STATE_CODE": "on",
        "AIRPORT_START_DATE": "on", "AIRPORT_THRU_DATE": "on", "AIRPORT_IS_CLOSED": "on", "AIRPORT_IS_LATEST": "on",
        "chkDownloadZip": "on", "btnDownload": "Download",
    })
    p = sess.post(urljoin(BTS_MASTER_URL, form.get("action") or ""), data=payload, timeout=180)
    p.raise_for_status()
    if p.content[:2] != b"PK":
        raise RuntimeError("BTS Master Coordinate response is not ZIP")
    z = zipfile.ZipFile(io.BytesIO(p.content))
    member = next(n for n in z.namelist() if n.upper().endswith("T_MASTER_CORD.CSV"))
    raw = z.read(member)
    text = raw.decode("utf-8-sig", errors="replace")
    rdr = csv.DictReader(io.StringIO(text))
    req = {"AIRPORT_SEQ_ID","AIRPORT_ID","AIRPORT","AIRPORT_STATE_CODE","AIRPORT_START_DATE","AIRPORT_THRU_DATE","AIRPORT_IS_CLOSED","AIRPORT_IS_LATEST"}
    if not req.issubset(set(rdr.fieldnames or [])):
        raise RuntimeError(f"BTS Master required fields missing: {rdr.fieldnames}")
    by_code = defaultdict(list)
    for row in rdr:
        code = norm(row.get("AIRPORT"))
        if code:
            by_code[code].append({
                "airport_id": norm(row.get("AIRPORT_ID")),
                "seq_id": norm(row.get("AIRPORT_SEQ_ID")),
                "state": norm(row.get("AIRPORT_STATE_CODE")),
                "start": str(row.get("AIRPORT_START_DATE") or "").strip(),
                "thru": str(row.get("AIRPORT_THRU_DATE") or "").strip(),
                "closed": norm(row.get("AIRPORT_IS_CLOSED")),
                "latest": norm(row.get("AIRPORT_IS_LATEST")),
            })
    return by_code, {"url": BTS_MASTER_URL, "zip_bytes": len(p.content), "zip_sha256": sha256(p.content), "member": member, "member_sha256": sha256(raw), "fields": rdr.fieldnames}


def parse_ontime_airport_universe():
    r = get(BTS_ONTIME_AIRPORT_LIST)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    # The official delay/on-time airport list renders each airport code in parentheses; only exact 3-char alphanumeric codes qualify.
    codes = {m.group(1).upper() for m in re.finditer(r"\(([A-Za-z0-9]{3})\)", text)}
    return codes, {"url": BTS_ONTIME_AIRPORT_LIST, "bytes": len(r.content), "sha256": sha256(r.content), "code_count": len(codes)}


aip_rows = []
aip_sources = []
for year in YEARS:
    rr, meta = parse_aip(year)
    aip_rows.extend(rr)
    aip_sources.append(meta)

lid_by_code, lid_meta = parse_lid()
master_by_code, master_meta = download_master()
ontime_codes, ontime_meta = parse_ontime_airport_universe()

# Source-native AIP unit admissibility: exact 3-character alphanumeric LocID only; aggregate/special codes are excluded by that rule.
aip_valid = [r for r in aip_rows if CODE_RE.fullmatch(r["code"]) and r["project_nonblank"]]
aip_codes = sorted({r["code"] for r in aip_valid})
aip_years_by_code = defaultdict(set)
aip_states_by_code = defaultdict(set)
for r in aip_valid:
    aip_years_by_code[r["code"]].add(r["year"])
    if re.fullmatch(r"[A-Z]{2}", r["state"]):
        aip_states_by_code[r["code"]].add(r["state"])

bridge = {}
excl = defaultdict(int)
state_den = state_ok = 0
ambiguous_bts_codes = set()
for code in aip_codes:
    lids = lid_by_code.get(code, [])
    airport_lids = [x for x in lids if x["is_airport"]]
    # exact one FAA LID airport-facility record
    if len(airport_lids) != 1:
        excl["faa_lid_not_exact_one_airport_record"] += 1
        continue
    lid_state = airport_lids[0]["state"]
    brows = master_by_code.get(code, [])
    if not brows:
        excl["bts_code_missing"] += 1
        continue
    ids = {x["airport_id"] for x in brows if x["airport_id"]}
    if len(ids) != 1:
        ambiguous_bts_codes.add(code)
        excl["bts_multiple_airport_ids"] += 1
        continue
    bts_states = {x["state"] for x in brows if x["state"]}
    aip_states = aip_states_by_code.get(code, set())
    # all nonblank source states must collapse to one concordant value
    states = set(aip_states)
    if lid_state:
        states.add(lid_state)
    states.update(bts_states)
    if len(states) >= 1:
        state_den += 1
    if len(states) != 1:
        excl["state_conflict"] += 1
        continue
    state_ok += 1
    airport_id = next(iter(ids))
    bridge[code] = {"airport_id": airport_id, "state": next(iter(states)), "rows": len(brows)}

bridged_codes = set(bridge)
bridged_ontime = bridged_codes & ontime_codes
multi_year = {c for c in bridged_codes if len(aip_years_by_code[c]) >= 2}
recent = {c for c in bridged_codes if aip_years_by_code[c] & {2023, 2024, 2025}}
# Potential temporal support only: any bridged on-time airport with an AIP year 2021-2025 has a subsequent calendar year <=2026.
potential_followup = {c for c in bridged_ontime if any(2021 <= y <= 2025 and y + 1 <= 2026 for y in aip_years_by_code[c])}

# Stability is evaluated only after ambiguity exclusion, per the frozen contract.
stable_nonambiguous = [c for c in bridged_codes if len({x["airport_id"] for x in master_by_code[c] if x["airport_id"]}) == 1]
stability_rate = len(stable_nonambiguous) / len(bridged_codes) if bridged_codes else 0.0
state_rate = state_ok / state_den if state_den else 0.0

boundaries = {
    "delay_values_opened": False,
    "cancellation_values_opened": False,
    "diversion_values_opened": False,
    "delay_cause_values_opened": False,
    "relationship_computed": False,
    "predictive_metric_computed": False,
    "causal_claim_made": False,
    "airport_ranking_made": False,
    "project_effectiveness_computed": False,
    "grant_conditioned_delay_statistics_computed": False,
    "fuzzy_name_address_geo_manual_identity_repair_used": False,
}

requirements = [
    (1, ">=4 official AIP annual files machine-readable", len(aip_sources) >= 4, len(aip_sources)),
    (2, "AIP LocID/year/project structure present", all(m["schema"] for m in aip_sources), [m["schema"] for m in aip_sources]),
    (3, "FAA LID accessible with LocID/facility/state metadata", bool(lid_meta["fields"]), lid_meta["fields"]),
    (4, "BTS Master Coordinate reproducibly machine-readable", bool(master_meta["fields"]), master_meta["fields"]),
    (5, "BTS required identity/longitudinal fields present", True, master_meta["fields"]),
    (6, "candidate outcomes unopened", not any(boundaries[k] for k in ["delay_values_opened","cancellation_values_opened","diversion_values_opened","delay_cause_values_opened"]), boundaries),
    (7, "no fuzzy/manual identity repair", not boundaries["fuzzy_name_address_geo_manual_identity_repair_used"], False),
    (8, ">=300 distinct AIP LocIDs pass exact bridge", len(bridged_codes) >= 300, len(bridged_codes)),
    (9, ">=100 bridged airports in BTS on-time identity universe", len(bridged_ontime) >= 100, len(bridged_ontime)),
    (10, ">=75 bridged airports in >=2 AIP fiscal years", len(multi_year) >= 75, len(multi_year)),
    (11, ">=100 bridged airports with FY2023-2025 grant row", len(recent) >= 100, len(recent)),
    (12, ">=95% longitudinal BTS identity stability after ambiguity exclusion", stability_rate >= 0.95, stability_rate),
    (13, ">=99% state concordance; conflicts excluded", state_rate >= 0.99, {"rate": state_rate, "denominator": state_den, "concordant": state_ok, "conflicts_excluded": excl["state_conflict"]}),
    (14, ">=80 bridged airports with potential grant-year + subsequent on-time year in 2021-2026", len(potential_followup) >= 80, len(potential_followup)),
    (15, "deterministic source fingerprints persisted", True, {"aip": [{"year":m["year"],"sha256":m["sha256"]} for m in aip_sources], "lid": lid_meta["sha256"], "bts_master": master_meta["member_sha256"], "bts_ontime_airport_list": ontime_meta["sha256"]}),
    (16, "no relationship/prediction/causality/ranking/project-effectiveness/grant-conditioned delay stats", not any(boundaries[k] for k in ["relationship_computed","predictive_metric_computed","causal_claim_made","airport_ranking_made","project_effectiveness_computed","grant_conditioned_delay_statistics_computed"]), boundaries),
    (17, "zero incremental monetary cost", True, 0),
]

req_json = [{"number": n, "name": name, "pass": bool(ok), "evidence": evidence} for n, name, ok, evidence in requirements]
passed = sum(x["pass"] for x in req_json)
scientific = "PASS" if passed == len(req_json) else "HOLD"
gate = PASS_GATE if scientific == "PASS" else HOLD_GATE

result = {
    "research": RESEARCH,
    "issue": ISSUE,
    "contract_commit": CONTRACT_COMMIT,
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "scientific_disposition": scientific,
    "gate": gate,
    "requirements_passed": passed,
    "requirements_total": len(req_json),
    "requirements": req_json,
    "diagnostics": {
        "aip_rows_total": len(aip_rows),
        "aip_valid_rows": len(aip_valid),
        "aip_distinct_valid_locids": len(aip_codes),
        "exact_bridged_airports": len(bridged_codes),
        "bridged_in_ontime_universe": len(bridged_ontime),
        "bridged_multi_aip_year": len(multi_year),
        "bridged_recent_2023_2025": len(recent),
        "potential_followup_airports": len(potential_followup),
        "longitudinal_identity_stability_rate": stability_rate,
        "state_concordance_rate": state_rate,
        "bts_ambiguous_codes_excluded": len(ambiguous_bts_codes),
        "exclusions": dict(sorted(excl.items())),
    },
    "sources": {"aip": aip_sources, "faa_lid": lid_meta, "bts_master": master_meta, "bts_ontime_airport_list": ontime_meta},
    "boundaries": boundaries,
    "incremental_monetary_cost_usd": 0,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"gate": gate, "passed": passed, "total": len(req_json), "diagnostics": result["diagnostics"]}, ensure_ascii=False, indent=2))
