#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import json
import math
import os
import re
import shutil
import time
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, date
from pathlib import Path

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WW-E01"
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "us-ww-e01"
TMP.mkdir(parents=True, exist_ok=True)

CWNS_URL = "https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download"
ECHO_URL = "https://echo.epa.gov/files/echodownloads/npdes_downloads.zip"
UA = "AI-Innovative-Research-Engine/US-WW-E01 preregistered experiment"

EXPOSURE_CODES = {"III-A", "III-B", "V"}
LEAKAGE_LABELS = {
    "The project(s) is necessary to obtain compliance with a new permit requirement.",
    "The project(s) is required to maintain compliance with a NPDES permit.",
    "The project(s) is to achieve or maintain compliance with a TMDL.",
    "The project(s) is to increase capacity or improve treatment in advance of anticipated new permit requirements.",
}
BASE_START, BASE_END = date(2019, 1, 1), date(2021, 12, 31)
FUTURE_START, FUTURE_END = date(2023, 1, 1), date(2025, 12, 31)
MATERIALITY = 0.03
MIN_GROUP = 500
MIN_STATES = 30
Z95 = 1.959963984540054

VIOLATION_START = {
    "NPDES_PS_VIOLATIONS.csv": "SCHEDULE_DATE",
    "NPDES_CS_VIOLATIONS.csv": "SCHEDULE_DATE",
    "NPDES_SE_VIOLATIONS.csv": "SINGLE_EVENT_VIOLATION_DATE",
}


def decode(b: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    raise RuntimeError("cannot decode source bytes")


def rows(b: bytes):
    return csv.DictReader(io.StringIO(decode(b)))


def normid(s: str | None) -> str:
    return re.sub(r"\s+", "", (s or "").strip()).upper()


def member(names: list[str], target: str) -> str:
    hits = [n for n in names if n.rsplit("/", 1)[-1].casefold() == target.casefold()]
    if len(hits) != 1:
        raise RuntimeError(f"expected one {target}, got {hits}")
    return hits[0]


def parse_date(s: str | None) -> date | None:
    s = (s or "").strip()
    if not s:
        return None
    for fmt, n in (("%m/%d/%Y", 10), ("%Y-%m-%d", 10), ("%m/%d/%Y %H:%M:%S", 19)):
        try:
            return datetime.strptime(s[:n], fmt).date()
        except ValueError:
            pass
    return None


def download(url: str, path: Path) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
        shutil.copyfileobj(r, f, 1024 * 1024)
    return path.stat().st_size


def download_cwns() -> Path:
    dl = TMP / "cwns"
    dl.mkdir(exist_ok=True)
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1440,1200")
    opts.add_experimental_option("prefs", {
        "download.default_directory": str(dl),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(CWNS_URL)
        wait = WebDriverWait(driver, 30)
        btn = wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME, "button") if "p3_type=NA_CSV" in (x.get_attribute("onclick") or "")), None))
        btn.click()
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "iframe")) > 0)
        found = False
        for fr in driver.find_elements(By.CSS_SELECTOR, "iframe"):
            driver.switch_to.default_content()
            driver.switch_to.frame(fr)
            if driver.find_elements(By.ID, "P3_QUESTION"):
                found = True
                break
        if not found:
            raise RuntimeError("CWNS download dialog not found")
        Select(wait.until(EC.presence_of_element_located((By.ID, "P3_QUESTION")))).select_by_visible_text("Researcher")
        wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME, "button") if (x.text or "").strip() == "Download"), None)).click()
        deadline = time.time() + 90
        while time.time() < deadline:
            zips = [p for p in dl.iterdir() if p.suffix.lower() == ".zip" and not p.name.endswith(".crdownload")]
            if zips:
                return max(zips, key=lambda p: p.stat().st_mtime)
            time.sleep(1)
        raise RuntimeError("CWNS ZIP not downloaded")
    finally:
        driver.quit()


def ols_hc1(y: np.ndarray, x: np.ndarray, beta_col: int) -> dict:
    n, k = x.shape
    rank = int(np.linalg.matrix_rank(x))
    if rank != k or n <= k:
        raise RuntimeError(f"design rank failure n={n} k={k} rank={rank}")
    xtx_inv = np.linalg.inv(x.T @ x)
    b = xtx_inv @ x.T @ y
    resid = y - x @ b
    meat = x.T @ ((resid ** 2)[:, None] * x)
    cov = (n / (n - k)) * (xtx_inv @ meat @ xtx_inv)
    se = float(math.sqrt(max(float(cov[beta_col, beta_col]), 0.0)))
    beta = float(b[beta_col])
    if se == 0.0:
        z = math.inf if beta != 0 else 0.0
        p = 0.0 if beta != 0 else 1.0
    else:
        z = beta / se
        p = math.erfc(abs(z) / math.sqrt(2.0))
    return {
        "n": n,
        "k": k,
        "rank": rank,
        "beta": beta,
        "se_hc1": se,
        "z": z,
        "p_two_sided_normal": p,
        "ci95_lower": beta - Z95 * se,
        "ci95_upper": beta + Z95 * se,
    }


def design_matrix(records: list[dict], include_leakage: bool = True) -> tuple[np.ndarray, list[str], list[str]]:
    states = sorted({r["state"] for r in records})
    if not states:
        raise RuntimeError("no states")
    ref = states[0]
    cols = ["intercept", "exposed"]
    if include_leakage:
        cols.append("leakage")
    cols.extend(f"state:{s}" for s in states[1:])
    xrows = []
    for r in records:
        row = [1.0, float(r["x"])]
        if include_leakage:
            row.append(float(r["l"]))
        row.extend(1.0 if r["state"] == s else 0.0 for s in states[1:])
        xrows.append(row)
    return np.asarray(xrows, dtype=float), cols, [ref] + states[1:]


def both_group_states(records: list[dict]) -> list[str]:
    groups = defaultdict(set)
    for r in records:
        groups[r["state"]].add(r["x"])
    return sorted(s for s, g in groups.items() if g == {0, 1})


cwns_path = download_cwns()
echo_path = TMP / "npdes_downloads.zip"
echo_bytes = download(ECHO_URL, echo_path)

# CWNS identities only. Never read need-dollar fields.
facilities: dict[str, str] = {}
permits: dict[str, set[str]] = defaultdict(set)
categories: dict[str, set[str]] = defaultdict(set)
reasons: dict[str, set[str]] = defaultdict(set)
with zipfile.ZipFile(cwns_path) as z:
    names = z.namelist()
    for r in rows(z.read(member(names, "FACILITIES.csv"))):
        cid = (r.get("CWNS_ID") or "").strip()
        if cid and (r.get("INFRASTRUCTURE_TYPE") or "").strip().casefold() == "wastewater":
            facilities[cid] = (r.get("STATE_CODE") or "").strip()
    for r in rows(z.read(member(names, "FACILITY_PERMIT.csv"))):
        cid = (r.get("CWNS_ID") or "").strip()
        pid = normid(r.get("PERMIT_NUMBER"))
        if cid in facilities and (r.get("PERMIT_SOURCE") or "").strip().casefold() == "npdes" and pid:
            permits[cid].add(pid)
    for r in rows(z.read(member(names, "NEEDS_COST_BY_CATEGORY.csv"))):
        cid = (r.get("CWNS_ID") or "").strip()
        cat = (r.get("NEEDS_CATEGORY") or "").strip()
        if cid in facilities and cat:
            categories[cid].add(cat)
    for r in rows(z.read(member(names, "REASON_FOR_NEEDS.csv"))):
        cid = (r.get("CWNS_ID") or "").strip()
        reason = (r.get("NEED_REASON") or "").strip()
        if cid in facilities and reason:
            reasons[cid].add(reason)

with zipfile.ZipFile(echo_path) as z:
    names = z.namelist()
    permit_member = member(names, "ICIS_PERMITS.csv")
    permit_reader = rows(z.read(permit_member))
    permit_headers = permit_reader.fieldnames or []
    required_permit_headers = {"EXTERNAL_PERMIT_NMBR", "EFFECTIVE_DATE", "TERMINATION_DATE"}
    missing = sorted(required_permit_headers - set(permit_headers))
    if missing:
        raise RuntimeError(f"missing frozen ICIS_PERMITS headers: {missing}")

    icis_ids: set[str] = set()
    lifecycle: dict[str, list[tuple[date | None, date | None]]] = defaultdict(list)
    for r in permit_reader:
        pid = normid(r.get("EXTERNAL_PERMIT_NMBR"))
        if not pid:
            continue
        icis_ids.add(pid)
        lifecycle[pid].append((parse_date(r.get("EFFECTIVE_DATE")), parse_date(r.get("TERMINATION_DATE"))))

    exact_facilities = {cid for cid, ps in permits.items() if ps and ps.issubset(icis_ids)}
    documented_need = {cid for cid in exact_facilities if categories.get(cid)}
    exposed = {cid for cid in documented_need if categories[cid] & EXPOSURE_CODES}
    comparator = documented_need - exposed
    leakage = {cid for cid in documented_need if reasons.get(cid, set()) & LEAKAGE_LABELS}

    def permit_at_risk(pid: str) -> bool:
        for eff, term in lifecycle.get(pid, []):
            if eff is not None and eff <= FUTURE_END and (term is None or term >= FUTURE_START):
                return True
        return False

    at_risk = {cid for cid in documented_need if any(permit_at_risk(pid) for pid in permits[cid])}

    # PASS 1: baseline only. Rows outside baseline are ignored immediately and never accumulated.
    baseline_violation_permits: set[str] = set()
    baseline_schema = []
    for target, start_col in VIOLATION_START.items():
        reader = rows(z.read(member(names, target)))
        headers = reader.fieldnames or []
        if "NPDES_ID" not in headers or start_col not in headers:
            raise RuntimeError(f"missing frozen violation headers in {target}: NPDES_ID/{start_col}")
        baseline_seen = False
        for r in reader:
            d = parse_date(r.get(start_col))
            if d is None or not (BASE_START <= d <= BASE_END):
                continue
            pid = normid(r.get("NPDES_ID"))
            if pid:
                baseline_violation_permits.add(pid)
                baseline_seen = True
        baseline_schema.append({"table": target, "start_column": start_col, "baseline_date_observed": baseline_seen})

    baseline_clean = {cid for cid in documented_need if all(pid not in baseline_violation_permits for pid in permits[cid])}
    eligible = baseline_clean & at_risk
    pre_model_records = []
    for cid in sorted(eligible):
        x = 1 if cid in exposed else 0
        if cid not in exposed and cid not in comparator:
            continue
        st = facilities[cid]
        if not st:
            continue
        pre_model_records.append({"cid": cid, "state": st, "x": x, "l": 1 if cid in leakage else 0})

    states_both = both_group_states(pre_model_records)
    states_both_set = set(states_both)
    model_records = [r for r in pre_model_records if r["state"] in states_both_set]
    model_exposed = sum(r["x"] == 1 for r in model_records)
    model_comparator = sum(r["x"] == 0 for r in model_records)
    x_pre, x_cols, ordered_states = design_matrix(model_records, include_leakage=True) if model_records else (np.empty((0,0)), [], [])
    rank = int(np.linalg.matrix_rank(x_pre)) if x_pre.size else 0
    full_rank = bool(x_pre.size and rank == x_pre.shape[1])

    shared_permit_counts = Counter(pid for cid in exact_facilities for pid in permits[cid])
    shared_permits = sum(1 for _, n in shared_permit_counts.items() if n > 1)

    structural = {
        "all_linked_permits_exact_facilities": len(exact_facilities),
        "documented_need_facilities": len(documented_need),
        "baseline_clean_documented_need_facilities": len(baseline_clean),
        "future_at_risk_documented_need_facilities": len(at_risk),
        "eligible_before_state_overlap": len(pre_model_records),
        "both_group_states": states_both,
        "both_group_state_count": len(states_both),
        "model_exposed": model_exposed,
        "model_comparator": model_comparator,
        "design_columns": x_cols,
        "design_rank": rank,
        "design_k": int(x_pre.shape[1]) if x_pre.size else 0,
        "design_full_rank": full_rank,
        "shared_official_npdes_permits_across_cwns_facilities": shared_permits,
        "pass_group_threshold": model_exposed >= MIN_GROUP and model_comparator >= MIN_GROUP,
        "pass_state_threshold": len(states_both) >= MIN_STATES,
        "pass_rank": full_rank,
    }
    structural_pass = structural["pass_group_threshold"] and structural["pass_state_threshold"] and structural["pass_rank"]

    base_result = {
        "id": "US-WW-E01-EXECUTION-RESULT",
        "issue": 119,
        "preregistration": {
            "exposure_codes": sorted(EXPOSURE_CODES),
            "baseline_window": [BASE_START.isoformat(), BASE_END.isoformat()],
            "future_window": [FUTURE_START.isoformat(), FUTURE_END.isoformat()],
            "canonical_start_columns": VIOLATION_START,
            "materiality_absolute_probability": MATERIALITY,
            "minimum_group": MIN_GROUP,
            "minimum_both_group_states": MIN_STATES,
            "model": "OLS LPM: Y ~ intercept + exposed + leakage + state FE; HC1",
        },
        "source_schema": {
            "permit_member": permit_member,
            "permit_lifecycle_fields": ["EFFECTIVE_DATE", "TERMINATION_DATE"],
            "baseline_violation_tables": baseline_schema,
        },
        "structural_gate": structural,
        "future_outcomes_opened_before_structural_gate": False,
        "need_dollar_magnitudes_read": False,
        "raw_source_bytes_persisted": False,
        "echo_core_bytes_transient": echo_bytes,
        "incremental_monetary_cost_usd": 0,
    }

    if not structural_pass:
        base_result.update({
            "gate": "HOLD_US_WW_E01_INSUFFICIENT_STRUCTURAL_SUPPORT",
            "future_outcomes_opened": False,
            "relationship_computed": False,
        })
        (OUT / "EXECUTION_RESULT.json").write_text(json.dumps(base_result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"gate": base_result["gate"], "structural": structural, "future_outcomes_opened": False}))
        shutil.rmtree(TMP, ignore_errors=True)
        raise SystemExit(0)

    # PASS 2: only now derive frozen future binary incident outcomes.
    permit_to_cids: dict[str, set[str]] = defaultdict(set)
    model_cids = {r["cid"] for r in model_records}
    for cid in model_cids:
        for pid in permits[cid]:
            permit_to_cids[pid].add(cid)

    future_positive: set[str] = set()
    table_positive: dict[str, set[str]] = {t: set() for t in VIOLATION_START}
    for target, start_col in VIOLATION_START.items():
        reader = rows(z.read(member(names, target)))
        for r in reader:
            d = parse_date(r.get(start_col))
            if d is None or not (FUTURE_START <= d <= FUTURE_END):
                continue
            pid = normid(r.get("NPDES_ID"))
            cids = permit_to_cids.get(pid)
            if not cids:
                continue
            future_positive.update(cids)
            table_positive[target].update(cids)

# Model outside ZIP scope.
for r in model_records:
    r["y"] = 1 if r["cid"] in future_positive else 0

y = np.asarray([r["y"] for r in model_records], dtype=float)
x, cols, states_ordered = design_matrix(model_records, include_leakage=True)
primary = ols_hc1(y, x, beta_col=1)
primary["columns"] = cols
primary["reference_state"] = states_ordered[0]

exp_y = [r["y"] for r in model_records if r["x"] == 1]
cmp_y = [r["y"] for r in model_records if r["x"] == 0]
exp_risk = float(sum(exp_y) / len(exp_y))
cmp_risk = float(sum(cmp_y) / len(cmp_y))
rd = exp_risk - cmp_risk
rr = None if cmp_risk == 0 else exp_risk / cmp_risk

strata = {}
for lv in (0, 1):
    subset = [r for r in model_records if r["l"] == lv]
    e = [r["y"] for r in subset if r["x"] == 1]
    c = [r["y"] for r in subset if r["x"] == 0]
    er = (sum(e) / len(e)) if e else None
    cr = (sum(c) / len(c)) if c else None
    strata[str(lv)] = {
        "n_exposed": len(e), "n_comparator": len(c),
        "risk_exposed": er, "risk_comparator": cr,
        "risk_difference": (er - cr) if er is not None and cr is not None else None,
        "risk_ratio": (er / cr) if er is not None and cr not in (None, 0) else None,
    }

sensitivity = None
l0 = [r for r in model_records if r["l"] == 0]
if sum(r["x"] == 1 for r in l0) >= MIN_GROUP and sum(r["x"] == 0 for r in l0) >= MIN_GROUP:
    l0_states = set(both_group_states(l0))
    l0m = [r for r in l0 if r["state"] in l0_states]
    if sum(r["x"] == 1 for r in l0m) >= MIN_GROUP and sum(r["x"] == 0 for r in l0m) >= MIN_GROUP:
        sx, scols, sstates = design_matrix(l0m, include_leakage=False)
        sy = np.asarray([r["y"] for r in l0m], dtype=float)
        if np.linalg.matrix_rank(sx) == sx.shape[1]:
            sensitivity = ols_hc1(sy, sx, beta_col=1)
            sensitivity["columns"] = scols
            sensitivity["reference_state"] = sstates[0]

beta = primary["beta"]
lo = primary["ci95_lower"]
if beta >= MATERIALITY and lo > 0:
    gate = "PASS_POSITIVE_MATERIAL_US_WW_E01_RELATIONSHIP"
elif 0 < beta < MATERIALITY and lo > 0:
    gate = "POSITIVE_BELOW_MATERIALITY_US_WW_E01_RELATIONSHIP"
else:
    gate = "NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP"

base_result.update({
    "gate": gate,
    "future_outcomes_opened": True,
    "relationship_computed": True,
    "primary": primary,
    "raw_risk": {
        "n_exposed": len(exp_y), "n_comparator": len(cmp_y),
        "events_exposed": int(sum(exp_y)), "events_comparator": int(sum(cmp_y)),
        "risk_exposed": exp_risk, "risk_comparator": cmp_risk,
        "risk_difference": rd, "risk_ratio": rr,
    },
    "leakage_strata_diagnostic": strata,
    "l0_sensitivity_non_rescuing": sensitivity,
    "table_contribution_facility_counts_nonexclusive": {t: len(v) for t, v in table_positive.items()},
})
(OUT / "EXECUTION_RESULT.json").write_text(json.dumps(base_result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
print(json.dumps({"gate": gate, "beta": primary["beta"], "ci": [primary["ci95_lower"], primary["ci95_upper"]], "p": primary["p_two_sided_normal"], "raw_risk": base_result["raw_risk"]}))
shutil.rmtree(TMP, ignore_errors=True)
