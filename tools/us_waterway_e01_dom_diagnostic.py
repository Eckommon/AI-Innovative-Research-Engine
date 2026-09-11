#!/usr/bin/env python3
"""Outcome-blind DOM identity diagnostic for US-WATERWAY-E01 Stage A.

Records only element identity/tag/class/counts and TH texts. It never reads TD
text, annual metric values, delay magnitudes, or hydrology observations.
"""
from __future__ import annotations

import json, time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-E01"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
TID = "356617961145373261"
RID = "R356617877054373260"
UA = "AI-Innovative-Research-Engine/US-WATERWAY-E01-dom-diagnostic"


def attrs(el):
    return {
        "tag": el.tag_name,
        "id": el.get_attribute("id") or "",
        "class": el.get_attribute("class") or "",
        "role": el.get_attribute("role") or "",
        "aria_label": el.get_attribute("aria-label") or "",
        "th_count": len(el.find_elements(By.TAG_NAME, "th")),
        "tr_count": len(el.find_elements(By.TAG_NAME, "tr")),
        "table_count": len(el.find_elements(By.TAG_NAME, "table")),
        "thead_count": len(el.find_elements(By.TAG_NAME, "thead")),
        "tbody_count": len(el.find_elements(By.TAG_NAME, "tbody")),
        "th_texts": [(x.get_attribute("textContent") or "").strip() for x in el.find_elements(By.TAG_NAME, "th")],
    }


def main():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument(f"--user-agent={UA}")
    d = webdriver.Chrome(options=opts)
    try:
        d.get(HOME)
        WebDriverWait(d, 30).until(lambda x: "corps-locks" in x.current_url)
        d.get(ANNUAL)
        WebDriverWait(d, 30).until(lambda x: len(x.find_elements(By.ID, RID)) >= 1)
        snapshots=[]
        for delay in (0, 2, 5, 10):
            if delay: time.sleep(delay)
            tids=d.find_elements(By.ID,TID)
            rids=d.find_elements(By.ID,RID)
            all_tables=d.find_elements(By.TAG_NAME,"table")
            snapshots.append({
                "after_seconds":delay,
                "target_id_elements":[attrs(e) for e in tids],
                "region_id_elements":[attrs(e) for e in rids],
                "all_table_summaries":[attrs(e) for e in all_tables],
            })
        out={
            "boundary":{"td_text_read":False,"delay_magnitudes_parsed":False,"hydrology_values_parsed":False,"relationship_computed":False},
            "current_url":d.current_url,
            "snapshots":snapshots,
            "incremental_monetary_cost_usd":0,
        }
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/"STAGE_A_DOM_DIAGNOSTIC.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        lines=["# US-WATERWAY-E01 Stage A DOM Diagnostic","","Outcome-blind: only element structure and TH text inspected; no TD values read.",""]
        for s in snapshots:
            lines += [f"## Snapshot +{s['after_seconds']}s",f"- target-id elements: **{len(s['target_id_elements'])}**",f"- region-id elements: **{len(s['region_id_elements'])}**",f"- all tables: **{len(s['all_table_summaries'])}**"]
            for i,e in enumerate(s['target_id_elements']): lines.append(f"- target[{i}]: `{e}`")
            for i,e in enumerate(s['all_table_summaries']): lines.append(f"- table[{i}]: tag={e['tag']} id=`{e['id']}` class=`{e['class']}` th={e['th_count']} tr={e['tr_count']} thead={e['thead_count']} tbody={e['tbody_count']} headers=`{e['th_texts']}`")
            lines.append("")
        lines += ["Incremental monetary cost: **0 USD**."]
        (OUT/"STAGE_A_DOM_DIAGNOSTIC.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    finally:
        d.quit()

if __name__=="__main__": main()
