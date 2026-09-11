#!/usr/bin/env python3
"""Frozen US-WATERWAY-E01 Stage B relationship test.

Implements DEC-138 and STAGE_B_IMPLEMENTATION_CONTRACT.md exactly. Raw external
USGS/USACE responses remain transient. The primary gate is persisted before any
prespecified sensitivity is calculated.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

import numpy as np
from scipy import stats
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-E01"
MAP = OUT / "STAGE_A_GAGE_LOCK_MAP.csv"
USGS_DAILY = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/items"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
REGION_ID = "R356617877054373260"
DATA_TABLE_ID = "356617961145373261_orig"
START = "2016-01-01"
END = "2025-12-31"
YEARS = list(range(2016, 2026))
UA = "AI-Innovative-Research-Engine/US-WATERWAY-E01-stage-b"


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch_json(url: str, attempts: int = 5):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/geo+json, application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                b = r.read()
                return json.loads(b.decode("utf-8", "replace")), {
                    "url": url,
                    "final_url": r.geturl(),
                    "status": getattr(r, "status", 200),
                    "bytes": len(b),
                    "sha256": sha256(b),
                }
        except Exception as e:
            last = e
            if i + 1 < attempts:
                time.sleep(2 * (i + 1))
    raise last


def read_cohort():
    with MAP.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        raise RuntimeError("empty Stage-A cohort")
    by_gage = defaultdict(list)
    for r in rows:
        if str(r.get("annual_usage_all_2016_2025_nonblank", "")).lower() != "true":
            raise RuntimeError("Stage-A cohort contains nonqualified annual-support row")
        by_gage[r["usgs_id"]].append(r)
    return rows, dict(by_gage)


def fetch_usgs_daily(gages):
    params = {
        "f": "json",
        "monitoring_location_id": ",".join(sorted(gages)),
        "parameter_code": "00060",
        "statistic_id": "00003",
        "datetime": f"{START}/{END}",
        "limit": "10000",
        "api_key": "DEMO_KEY",
        "properties": "monitoring_location_id,parameter_code,statistic_id,time,value,unit_of_measure,approval_status,qualifier",
    }
    url = USGS_DAILY + "?" + urllib.parse.urlencode(params, safe=",")
    values = defaultdict(dict)
    conflicts = []
    manifest = []
    seen_urls = set()
    page = 0
    while url:
        if url in seen_urls:
            raise RuntimeError("USGS pagination loop")
        seen_urls.add(url)
        obj, meta = fetch_json(url)
        page += 1
        meta["page"] = page
        meta["numberReturned"] = obj.get("numberReturned")
        manifest.append(meta)
        for feat in obj.get("features", []):
            p = feat.get("properties") or {}
            gid = str(p.get("monitoring_location_id") or "")
            if gid not in gages:
                continue
            if str(p.get("parameter_code")) != "00060" or str(p.get("statistic_id")) != "00003":
                continue
            day = str(p.get("time") or "")[:10]
            if not (START <= day <= END):
                continue
            try:
                val = float(p.get("value"))
            except Exception:
                continue
            if not math.isfinite(val) or val < 0:
                raise RuntimeError(f"invalid USGS discharge value {gid} {day}: {p.get('value')!r}")
            prior = values[gid].get(day)
            if prior is not None and not math.isclose(prior, val, rel_tol=0.0, abs_tol=0.0):
                conflicts.append({"gage": gid, "date": day, "a": prior, "b": val})
            else:
                values[gid][day] = val
        next_url = None
        for link in obj.get("links", []):
            if link.get("rel") == "next" and link.get("href"):
                next_url = str(link["href"])
                break
        url = next_url
    if conflicts:
        raise RuntimeError(f"conflicting USGS duplicate gage/date values: {conflicts[:5]}")
    return values, manifest


class AnnualTableParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_target = False
        self.depth = 0
        self.in_cell = False
        self.cell_tag = ""
        self.cell_text = ""
        self.row = None
        self.rows = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table" and a.get("id") == DATA_TABLE_ID and not self.in_target:
            self.in_target = True
            self.depth = 1
            return
        if not self.in_target:
            return
        if tag == "table":
            self.depth += 1
        elif tag == "tr" and self.depth == 1:
            self.row = []
        elif tag in {"th", "td"} and self.row is not None and self.depth == 1:
            self.in_cell = True
            self.cell_tag = tag
            self.cell_text = ""

    def handle_data(self, data):
        if self.in_target and self.in_cell:
            self.cell_text += data

    def handle_endtag(self, tag):
        if not self.in_target:
            return
        if tag in {"th", "td"} and self.in_cell and self.row is not None and self.depth == 1:
            self.row.append((self.cell_tag, re.sub(r"\s+", " ", self.cell_text).strip()))
            self.in_cell = False
        elif tag == "tr" and self.row is not None and self.depth == 1:
            self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.depth -= 1
            if self.depth == 0:
                self.in_target = False


def code_part(text):
    return str(text or "").split(" - ", 1)[0].strip().upper()


def lockcode(s):
    s = re.sub(r"[^A-Z0-9]", "", str(s or "").upper())
    m = re.fullmatch(r"0*(\d+)([A-Z]?)", s)
    if m:
        return str(int(m.group(1))) + m.group(2)
    return s


def header_index(headers, label):
    target = re.sub(r"\s+", " ", label.upper()).strip()
    hs = [re.sub(r"\s+", " ", h.upper()).strip() for h in headers]
    for i, h in enumerate(hs):
        if h == target or h.startswith(target + " ") or h.startswith(target + "SORT"):
            return i
    raise RuntimeError(f"header {label!r} not found")


def year_index(headers, year):
    hs = [re.sub(r"\s+", " ", h.upper()).strip() for h in headers]
    pat = re.compile(rf"^CY[_ ]?{year}(?:\b|SORT)")
    for i, h in enumerate(hs):
        if pat.search(h):
            return i
    raise RuntimeError(f"year header {year} not found")


def parse_annual_snapshot(html):
    p = AnnualTableParser(); p.feed(html)
    header = None; pos = None
    for i, row in enumerate(p.rows):
        if row and any(tag == "th" for tag, _ in row):
            header = [txt for _, txt in row]; pos = i; break
    if header is None:
        raise RuntimeError("Annual Usage data-table header absent")
    idx = {k: header_index(header, k) for k in ["RIVER", "LOCK", "USAGE TYPE"]}
    yi = {y: year_index(header, y) for y in YEARS}
    records = []
    first_sig = None
    for row in p.rows[pos+1:]:
        vals = [txt for _, txt in row]
        if len(vals) < len(header):
            continue
        river, lock, usage = vals[idx["RIVER"]], vals[idx["LOCK"]], vals[idx["USAGE TYPE"]]
        if first_sig is None:
            first_sig = (river, lock, usage)
        if usage.upper() != "AVERAGE DELAY (MINUTES)":
            continue
        key = (code_part(river), lockcode(code_part(lock)))
        yearly = {}
        for y in YEARS:
            raw = vals[yi[y]].strip().replace(",", "")
            if raw == "":
                yearly[y] = None
                continue
            try:
                v = float(raw)
            except Exception as e:
                raise RuntimeError(f"non-numeric Annual Usage delay {key} {y}: {raw!r}") from e
            if not math.isfinite(v) or v < 0:
                raise RuntimeError(f"invalid Annual Usage delay {key} {y}: {raw!r}")
            yearly[y] = v
        records.append((key, yearly))
    return records, first_sig


def annual_sig(driver):
    try:
        _, sig = parse_annual_snapshot(driver.page_source)
        return sig
    except Exception:
        return None


def fetch_annual_delays(needed_keys):
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument(f"--user-agent={UA}")
    driver = webdriver.Chrome(options=opts)
    found = {}
    pages = 0
    page_hashes = []
    try:
        wait = WebDriverWait(driver, 30)
        driver.get(HOME); wait.until(lambda d: "corps-locks" in d.current_url)
        driver.get(ANNUAL)
        wait.until(lambda d: len(d.find_elements(By.ID, DATA_TABLE_ID)) >= 1)
        wait.until(lambda d: annual_sig(d) is not None)
        while True:
            html = driver.page_source
            pages += 1
            page_hashes.append({"page": pages, "html_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest()})
            records, sig = parse_annual_snapshot(html)
            for key, yearly in records:
                if key in needed_keys:
                    found[key] = yearly
            region = driver.find_element(By.ID, REGION_ID)
            btns = region.find_elements(By.CSS_SELECTOR, "button.a-IRR-button--pagination[title='Next']")
            if not btns:
                break
            if btns[0].get_attribute("disabled") is not None or btns[0].get_attribute("aria-disabled") == "true":
                break
            before = sig
            region = driver.find_element(By.ID, REGION_ID)
            btn = region.find_element(By.CSS_SELECTOR, "button.a-IRR-button--pagination[title='Next']")
            driver.execute_script("arguments[0].click();", btn)
            wait.until(lambda d: annual_sig(d) is not None and annual_sig(d) != before)
            if pages > 200:
                raise RuntimeError("Annual Usage pagination safety limit exceeded")
            time.sleep(0.1)
    finally:
        driver.quit()
    missing = sorted(needed_keys - set(found))
    if missing:
        raise RuntimeError(f"mapped Annual Usage locks not found: {missing}")
    return found, {"url": ANNUAL, "pages": pages, "page_html_sha256": page_hashes}


def residualize(arrays, gages, years, tol=1e-12, max_iter=1000):
    z = [np.asarray(a, dtype=float).copy() for a in arrays]
    gages = np.asarray(gages); years = np.asarray(years)
    ug = np.unique(gages); uy = np.unique(years)
    for iteration in range(1, max_iter+1):
        before = [a.copy() for a in z]
        for g in ug:
            mask = gages == g
            for a in z: a[mask] -= a[mask].mean()
        for y in uy:
            mask = years == y
            for a in z: a[mask] -= a[mask].mean()
        delta = max(float(np.max(np.abs(a-b))) for a,b in zip(z,before))
        if delta < tol:
            return z, iteration, delta
    raise RuntimeError("fixed-effect residualization did not converge")


def cluster_var(x, u, labels, K):
    n = len(x)
    unique = np.unique(labels)
    C = len(unique)
    if C <= 1 or n <= K:
        raise RuntimeError("insufficient clusters/df for CR1")
    xx = float(np.dot(x, x))
    if not math.isfinite(xx) or xx <= 0:
        raise RuntimeError("degenerate residualized exposure")
    meat = 0.0
    for c in unique:
        m = labels == c
        s = float(np.dot(x[m], u[m]))
        meat += s*s
    correction = (C/(C-1.0))*((n-1.0)/(n-K))
    return (meat/(xx*xx))*correction


def fit_primary(panel, exposure_key="extreme_share"):
    y = np.array([r["delay_mean"] for r in panel], dtype=float)
    x = np.array([r[exposure_key] for r in panel], dtype=float)
    g = np.array([r["usgs_id"] for r in panel], dtype=object)
    t = np.array([int(r["year"]) for r in panel], dtype=int)
    (yr, xr), iters, delta = residualize([y, x], g, t)
    if len(np.unique(np.round(xr, 15))) < 2:
        raise RuntimeError("fewer than two distinct residualized exposure values")
    xx = float(np.dot(xr, xr))
    if xx <= 0 or not math.isfinite(xx):
        raise RuntimeError("rank-deficient exposure")
    beta = float(np.dot(xr, yr)/xx)
    u = yr - beta*xr
    G = len(np.unique(g)); T = len(np.unique(t)); N = len(panel); K = G + T
    vg = cluster_var(xr, u, g, K)
    vt = cluster_var(xr, u, t, K)
    inter = np.array([f"{a}|{b}" for a,b in zip(g,t)], dtype=object)
    vi = cluster_var(xr, u, inter, K)
    variance = vg + vt - vi
    if not math.isfinite(variance) or variance <= 0:
        raise RuntimeError(f"nonpositive/nonfinite two-way CR1 variance: {variance}")
    se = math.sqrt(variance)
    df = min(G-1, T-1)
    crit = float(stats.t.ppf(0.975, df))
    lo = beta - crit*se; hi = beta + crit*se
    tstat = beta/se
    p = float(2*stats.t.sf(abs(tstat), df))
    material_10pp = 0.10*beta
    if beta > 0 and lo > 0 and material_10pp >= 5:
        gate = "PASS_US_WATERWAY_E01_POSITIVE_MATERIAL_EXTREME_FLOW_DELAY_ASSOCIATION"
    elif beta > 0 and lo > 0 and material_10pp < 5:
        gate = "DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01"
    else:
        gate = "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP"
    return {
        "gate": gate, "N": N, "G_gage": G, "G_year": T, "K": K,
        "beta_minutes_per_share_1_0": beta, "se_two_way_cr1": se,
        "df": df, "ci95_lower": lo, "ci95_upper": hi, "t_stat": tstat,
        "p_two_sided": p, "delta_minutes_per_plus_10pp": material_10pp,
        "fe_iterations": iters, "fe_final_delta": delta,
        "var_gage": vg, "var_year": vt, "var_intersection": vi,
    }


def build_panel(by_gage, daily, delays):
    panel = []
    gage_summary = []
    for gid, locks in sorted(by_gage.items()):
        obs = daily.get(gid, {})
        year_obs = {y: [] for y in YEARS}
        for day, val in obs.items():
            y = int(day[:4])
            if y in year_obs: year_obs[y].append((day,val))
        counts = {y: len(year_obs[y]) for y in YEARS}
        total = sum(counts.values())
        eligible = total >= 3300 and all(counts[y] >= 330 for y in YEARS)
        if not eligible:
            gage_summary.append({"usgs_id":gid,"eligible":False,"total_days":total,"min_year_days":min(counts.values()),"q10":"","q90":""})
            continue
        vals = np.array([v for y in YEARS for _,v in year_obs[y]], dtype=float)
        q10 = float(np.quantile(vals, 0.10, method="linear")); q90 = float(np.quantile(vals, 0.90, method="linear"))
        gage_summary.append({"usgs_id":gid,"eligible":True,"total_days":total,"min_year_days":min(counts.values()),"q10":q10,"q90":q90})
        keys = [(str(r["river_code"]).upper(), lockcode(r["lock_code"])) for r in locks]
        for y in YEARS:
            arr = np.array([v for _,v in year_obs[y]], dtype=float)
            n = len(arr)
            extreme = float(np.count_nonzero((arr < q10)|(arr > q90))/n)
            high = float(np.count_nonzero(arr > q90)/n)
            low = float(np.count_nonzero(arr < q10)/n)
            ds = []
            for k in keys:
                v = delays[k].get(y)
                if v is None or not math.isfinite(float(v)) or float(v) < 0:
                    ds = []; break
                ds.append(float(v))
            if len(ds) != len(keys):
                continue
            panel.append({
                "usgs_id": gid, "year": y, "usable_days": n,
                "q10": q10, "q90": q90,
                "extreme_share": extreme, "high_share": high, "low_share": low,
                "mapped_lock_count": len(keys), "delay_mean": float(np.mean(ds)),
            })
    return panel, gage_summary


def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader()
        for r in rows: w.writerow({k:r.get(k,"") for k in fields})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cohort, by_gage = read_cohort()
    gages = set(by_gage)
    needed_keys = {(str(r["river_code"]).upper(), lockcode(r["lock_code"])) for r in cohort}

    source_manifest={"boundary":{"raw_external_bytes_persisted":False},"period":[START,END],"incremental_monetary_cost_usd":0}
    try:
        daily, usgs_manifest = fetch_usgs_daily(gages)
        source_manifest["usgs_daily"]={"endpoint":USGS_DAILY,"pages":usgs_manifest,"gage_count_requested":len(gages)}
        delays, annual_manifest = fetch_annual_delays(needed_keys)
        source_manifest["usace_annual_usage"]=annual_manifest
        panel, gage_summary = build_panel(by_gage,daily,delays)
        eligible_gages = sorted({r["usgs_id"] for r in panel})
        if len(eligible_gages) < 12 or len(panel) < 120:
            raise RuntimeError(f"realized panel below frozen support: gages={len(eligible_gages)} rows={len(panel)}")
        primary = fit_primary(panel,"extreme_share")
        primary["status"]="PRIMARY_GATE_FIXED_BEFORE_SENSITIVITIES"
        primary["incremental_monetary_cost_usd"]=0
    except Exception as e:
        source_manifest["error"]=f"{type(e).__name__}: {e}"
        (OUT/"STAGE_B_SOURCE_MANIFEST.json").write_text(json.dumps(source_manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        hold={"gate":"HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT","reason":source_manifest["error"],"primary_gate_fixed_before_sensitivities":True,"incremental_monetary_cost_usd":0}
        (OUT/"STAGE_B_PRIMARY_RESULT.json").write_text(json.dumps(hold,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        (OUT/"STAGE_B_SENSITIVITY_RESULT.json").write_text(json.dumps({"not_run":True,"reason":"primary HOLD; sensitivities cannot rescue"},indent=2)+"\n",encoding="utf-8")
        (OUT/"STAGE_B_RESULT.md").write_text(f"# US-WATERWAY-E01 Stage B Result\n\n**`{hold['gate']}`**\n\nReason: `{hold['reason']}`\n\nNo alternate predictor/outcome/source was substituted. Sensitivities were not used to rescue the primary gate.\n\nIncremental monetary cost: **0 USD**.\n",encoding="utf-8")
        print(json.dumps(hold)); return

    # Persist the primary gate before calculating any sensitivity.
    (OUT/"STAGE_B_SOURCE_MANIFEST.json").write_text(json.dumps(source_manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (OUT/"STAGE_B_PRIMARY_RESULT.json").write_text(json.dumps(primary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    write_csv(OUT/"STAGE_B_GAGE_YEAR_PANEL.csv",panel,["usgs_id","year","usable_days","q10","q90","extreme_share","high_share","low_share","mapped_lock_count","delay_mean"])
    write_csv(OUT/"STAGE_B_GAGE_QUALITY.csv",gage_summary,["usgs_id","eligible","total_days","min_year_days","q10","q90"])

    sensitivity={}
    for key,name in [("high_share","high_flow_only"),("low_share","low_flow_only")]:
        try: sensitivity[name]=fit_primary(panel,key)
        except Exception as e: sensitivity[name]={"error":f"{type(e).__name__}: {e}"}
    loo=[]
    for gid in sorted({r["usgs_id"] for r in panel}):
        sub=[r for r in panel if r["usgs_id"]!=gid]
        try:
            fit=fit_primary(sub,"extreme_share")
            loo.append({"left_out_gage":gid,"beta":fit["beta_minutes_per_share_1_0"],"gate_if_treated_as_primary":fit["gate"]})
        except Exception as e:
            loo.append({"left_out_gage":gid,"error":f"{type(e).__name__}: {e}"})
    betas=[x["beta"] for x in loo if "beta" in x]
    sensitivity["leave_one_gage_out"]={"rows":loo,"beta_min":min(betas) if betas else None,"beta_max":max(betas) if betas else None}
    sensitivity["cannot_rescue_primary"]=True
    (OUT/"STAGE_B_SENSITIVITY_RESULT.json").write_text(json.dumps(sensitivity,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    md=[
        "# US-WATERWAY-E01 Stage B Result","",f"**`{primary['gate']}`**","",
        "Primary gate was fixed and persisted before prespecified sensitivities.","",
        f"- realized gage-year N: **{primary['N']}**",
        f"- unique gages: **{primary['G_gage']}**",
        f"- calendar years: **{primary['G_year']}**",
        f"- beta: **{primary['beta_minutes_per_share_1_0']:.10g} minutes per 1.0 extreme-share**",
        f"- two-way CR1 SE: **{primary['se_two_way_cr1']:.10g}**",
        f"- df: **{primary['df']}**",
        f"- 95% CI: **[{primary['ci95_lower']:.10g}, {primary['ci95_upper']:.10g}]**",
        f"- two-sided p: **{primary['p_two_sided']:.10g}**",
        f"- model-implied +10pp extreme-share difference: **{primary['delta_minutes_per_plus_10pp']:.10g} minutes**","",
        "## Interpretation boundary","",
        "This is the preregistered observational annual association only. It does not establish causality, advance prediction, propagation, novelty, lock ranking, decision utility, or an optimal threshold. Sensitivities cannot rescue or alter the primary classification.","",
        "Incremental monetary cost: **0 USD**.",
    ]
    (OUT/"STAGE_B_RESULT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"gate":primary["gate"],"N":primary["N"],"gages":primary["G_gage"],"beta":primary["beta_minutes_per_share_1_0"],"ci_lower":primary["ci95_lower"],"delta10":primary["delta_minutes_per_plus_10pp"]}))

if __name__=="__main__": main()
