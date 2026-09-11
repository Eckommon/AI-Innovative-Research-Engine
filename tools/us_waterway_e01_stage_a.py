#!/usr/bin/env python3
"""US-WATERWAY-E01 Stage A: outcome-blind 2016-2025 panel qualification.

No lock-delay magnitude or hydrology observation value is converted, summarized,
or persisted. Annual metric cells are reduced immediately to nonblank booleans.
USGS support comes from previously persisted time-series metadata only.
"""
from __future__ import annotations
import csv, json, re, urllib.request
from collections import defaultdict
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parents[1]
F01 = ROOT / "research" / "US-WATERWAY-F01"
OUT = ROOT / "research" / "US-WATERWAY-E01"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
LOCK_QUERY = "https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services/Locks/FeatureServer/0/query?where=1%3D1&outFields=ID,NDCCODE,RIVERCD,LOCKCD,PMSDATA,PMSNAME,RIVER,STATE,DISTRICT&returnGeometry=false&f=json"
INDIVIDUAL_TABLE_ID = "356617961145373261"
INDIVIDUAL_REGION_ID = "R356617877054373260"
START = "2016-01-01"
END = "2025-12-31"
YEARS = [str(y) for y in range(2016, 2026)]
UA = "AI-Innovative-Research-Engine/US-WATERWAY-E01-stage-a"
ALIASES = {
    "MEL PRICE": "MELVIN PRICE",
    "CAPT ANT MELDAHL": "CAPTAIN ANTHONY MELDAHL",
    "JOHN T MYERSLOCK": "JOHN T MYERS",
}


def norm(s):
    s = str(s or "").upper().replace("&", " AND ")
    s = re.sub(r"\bL\s*/\s*D\b", " LOCK AND DAM ", s)
    s = re.sub(r"[^A-Z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def stripped_name(name):
    toks = [t for t in norm(name).split() if t not in {"LOCK", "LOCKS", "DAM", "AND", "RES"}]
    return " ".join(toks)


def historical_keys(name, river):
    n = norm(name); r = norm(river)
    out = {n, stripped_name(name)}
    nums = re.findall(r"\b(\d+[A-Z]?)\b", n)
    if nums:
        out.add(f"{nums[-1]} {r}")
    stripped = stripped_name(name)
    if stripped in ALIASES:
        out.add(ALIASES[stripped])
    return {x for x in out if x}


def code_part(text):
    return str(text or "").split(" - ", 1)[0].strip().upper()


def lockcode(s):
    s = re.sub(r"[^A-Z0-9]", "", str(s or "").upper())
    m = re.fullmatch(r"0*(\d+)([A-Z]?)", s)
    if m:
        return str(int(m.group(1))) + m.group(2)
    return s


def json_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def metadata_qualifies(match):
    for s in match.get("daily_metadata_support", []):
        if str(s.get("parameter_code")) != "00060":
            continue
        if str(s.get("statistic_id")) != "00003":
            continue
        a = str(s.get("start") or "")[:10]
        b = str(s.get("end") or "")[:10]
        if a and b and a <= START and b >= END:
            return True, a, b
    return False, "", ""


def text_content(element):
    return (element.get_attribute("textContent") or "").strip()


def table_headers(table):
    return [text_content(x) for x in table.find_elements(By.CSS_SELECTOR, "thead th")]


def header_index(headers, label):
    target = re.sub(r"\s+", " ", label.upper()).strip()
    normalized = [re.sub(r"\s+", " ", h.upper()).strip() for h in headers]
    for i, h in enumerate(normalized):
        if h == target or h.startswith(target + " ") or h.startswith(target + "SORT"):
            return i
    raise ValueError(f"header {label!r} not found in {headers!r}")


def year_header_index(headers, year):
    normalized = [re.sub(r"\s+", " ", h.upper()).strip() for h in headers]
    pat = re.compile(rf"^CY[_ ]?{re.escape(year)}(?:\b|SORT)")
    for i, h in enumerate(normalized):
        if pat.search(h):
            return i
    raise ValueError(f"year header {year} not found in {headers!r}")


def find_individual_table(driver):
    return driver.find_element(By.ID, INDIVIDUAL_TABLE_ID)


def scrape_annual_support():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument(f"--user-agent={UA}")
    driver = webdriver.Chrome(options=opts)
    all_delay = {}
    page_count = 0
    try:
        wait = WebDriverWait(driver, 30)
        driver.get(HOME)
        wait.until(lambda d: "corps-locks" in d.current_url)
        driver.get(ANNUAL)
        wait.until(lambda d: len(d.find_elements(By.ID, INDIVIDUAL_TABLE_ID)) == 1)
        while True:
            table = find_individual_table(driver)
            headers = table_headers(table)
            idx = {name: header_index(headers, name) for name in ["DISTRICT", "RIVER", "LOCK", "USAGE TYPE"]}
            year_idx = {y: year_header_index(headers, y) for y in YEARS}
            rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
            page_count += 1
            first_sig = None
            for tr in rows:
                cells = tr.find_elements(By.TAG_NAME, "td")
                if len(cells) < len(headers):
                    continue
                district = text_content(cells[idx["DISTRICT"]])
                river = text_content(cells[idx["RIVER"]])
                lock = text_content(cells[idx["LOCK"]])
                usage = text_content(cells[idx["USAGE TYPE"]])
                if first_sig is None:
                    first_sig = (river, lock, usage)
                if usage.upper() != "AVERAGE DELAY (MINUTES)":
                    continue
                present = {y: bool(text_content(cells[year_idx[y]])) for y in YEARS}
                key = (code_part(river), lockcode(code_part(lock)))
                all_delay[key] = {
                    "district": district,
                    "river": river,
                    "lock": lock,
                    "year_nonblank": present,
                    "all_years_nonblank": all(present.values()),
                }
            region = driver.find_element(By.ID, INDIVIDUAL_REGION_ID)
            buttons = region.find_elements(By.CSS_SELECTOR, "button.a-IRR-button--pagination[title='Next']")
            if not buttons:
                break
            btn = buttons[0]
            disabled = btn.get_attribute("disabled") is not None or btn.get_attribute("aria-disabled") == "true"
            if disabled:
                break
            before = first_sig
            driver.execute_script("arguments[0].click();", btn)
            def changed(d):
                try:
                    nt = find_individual_table(d)
                    rs = nt.find_elements(By.CSS_SELECTOR, "tbody tr")
                    if not rs:
                        return False
                    cs = rs[0].find_elements(By.TAG_NAME, "td")
                    nh = table_headers(nt)
                    ri = header_index(nh, "RIVER")
                    li = header_index(nh, "LOCK")
                    ui = header_index(nh, "USAGE TYPE")
                    sig = (text_content(cs[ri]), text_content(cs[li]), text_content(cs[ui]))
                    return sig != before
                except Exception:
                    return False
            wait.until(changed)
            if page_count > 200:
                raise RuntimeError("pagination safety limit exceeded")
        return all_delay, page_count
    finally:
        driver.quit()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    hyd = json.loads((F01 / "HYDROLOGY_METADATA_PREFLIGHT_V3.json").read_text(encoding="utf-8"))
    toc = json.loads((F01 / "USAGE_TOC_PREFLIGHT.json").read_text(encoding="utf-8"))
    toc_names = toc["lock_identity_unique"]
    toc_norm = {norm(x): x for x in toc_names}

    lock_obj = json_get(LOCK_QUERY)
    feat = {}
    for f in lock_obj.get("features", []):
        a = f.get("attributes") or {}
        feat[int(a["ID"])] = a

    candidates = []
    for m in hyd.get("matches", []):
        ok, meta_start, meta_end = metadata_qualifies(m)
        if not ok:
            continue
        lid = int(m["lock_id"])
        a = feat.get(lid)
        if not a:
            continue
        keys = historical_keys(m.get("lock_name"), m.get("river"))
        hits = [k for k in keys if k in toc_norm]
        if not hits:
            continue
        candidates.append({
            "lock_id": lid,
            "lock_name": m.get("lock_name"),
            "river": m.get("river"),
            "river_code": str(a.get("RIVERCD") or "").upper().strip(),
            "lock_code": lockcode(a.get("LOCKCD")),
            "usgs_id": m.get("usgs_id"),
            "usgs_name": m.get("usgs_name"),
            "metadata_start": meta_start,
            "metadata_end": meta_end,
            "historical_toc_lock": toc_norm[hits[0]],
        })

    annual, pages = scrape_annual_support()
    qualified = []
    excluded = []
    for c in candidates:
        key = (c["river_code"], c["lock_code"])
        ar = annual.get(key)
        row = dict(c)
        row["annual_usage_match"] = bool(ar)
        row["annual_usage_all_2016_2025_nonblank"] = bool(ar and ar["all_years_nonblank"])
        row["annual_usage_display_lock"] = ar["lock"] if ar else ""
        if ar and ar["all_years_nonblank"]:
            qualified.append(row)
        else:
            excluded.append(row)

    gage_locks = defaultdict(list)
    for q in qualified:
        gage_locks[str(q["usgs_id"])].append(q)
    gages = sorted(gage_locks)
    lock_count = len(qualified)
    gage_year_cells = len(gages) * len(YEARS)
    stage_a_pass = len(gages) >= 12 and lock_count >= 20 and gage_year_cells >= 120
    gate = "PASS_US_WATERWAY_E01_STAGE_A_PANEL_SUPPORT" if stage_a_pass else "HOLD_US_WATERWAY_E01_PANEL_SUPPORT"

    fields = ["usgs_id", "usgs_name", "lock_id", "river", "river_code", "lock_code", "lock_name", "historical_toc_lock", "metadata_start", "metadata_end", "annual_usage_match", "annual_usage_all_2016_2025_nonblank", "annual_usage_display_lock"]
    with (OUT / "STAGE_A_GAGE_LOCK_MAP.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader()
        for r in sorted(qualified, key=lambda x: (str(x["usgs_id"]), x["river_code"], x["lock_code"])):
            w.writerow({k: r.get(k, "") for k in fields})
    with (OUT / "STAGE_A_EXCLUSIONS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader()
        for r in excluded:
            w.writerow({k: r.get(k, "") for k in fields})
    support = {
        "boundary": {
            "delay_magnitudes_parsed": False,
            "hydrology_values_requested": False,
            "hydrology_values_parsed": False,
            "relationship_computed": False,
            "annual_metric_cells_reduced_to_nonblank_boolean_only": True,
        },
        "period": [START, END],
        "annual_usage_pages_traversed": pages,
        "annual_usage_average_delay_identity_rows": len(annual),
        "v3_hydrology_matches_entering": len(hyd.get("matches", [])),
        "candidates_after_00060_00003_full_period_and_historical_identity": len(candidates),
        "qualified_all_year_locks": lock_count,
        "qualified_unique_usgs_gages": len(gages),
        "prospective_gage_year_cells": gage_year_cells,
        "excluded_candidate_locks": len(excluded),
        "stage_a_gate": gate,
        "gage_lock_counts": {g: len(gage_locks[g]) for g in gages},
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "STAGE_A_SUPPORT.json").write_text(json.dumps(support, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# US-WATERWAY-E01 Stage A Panel Support Result", "",
        f"**`{gate}`**", "",
        "Outcome-blind Stage A: no lock-delay magnitude and no hydrology observation value was parsed or persisted.", "",
        f"- Annual Usage pages traversed: **{pages}**",
        f"- Annual Usage Average Delay identity rows discovered: **{len(annual)}**",
        f"- v3 USGS-qualified lock candidates entering: **{len(hyd.get('matches', []))}**",
        f"- candidates with full 2016–2025 Daily `00060/00003` metadata + deterministic historical identity: **{len(candidates)}**",
        f"- qualified matched locks with nonblank Annual Usage Average Delay support in every 2016–2025 column: **{lock_count}**",
        f"- unique qualified USGS gages: **{len(gages)}**",
        f"- prospective gage-year cells: **{gage_year_cells}**",
        f"- exclusions after candidate construction: **{len(excluded)}**", "",
        "## Frozen thresholds", "",
        f"- unique gages >=12: **{'PASS' if len(gages)>=12 else 'FAIL'}**",
        f"- all-year matched locks >=20: **{'PASS' if lock_count>=20 else 'FAIL'}**",
        f"- prospective gage-years >=120: **{'PASS' if gage_year_cells>=120 else 'FAIL'}**", "",
        "Shared-gage locks remain collapsed to one exposure unit for Stage B. This PASS/HOLD establishes support only and contains no relationship information.", "",
        "Incremental monetary cost: **0 USD**.",
    ]
    (OUT / "STAGE_A_RESULT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"gate": gate, "gages": len(gages), "locks": lock_count, "gage_years": gage_year_cells, "pages": pages}))

if __name__ == "__main__":
    main()
