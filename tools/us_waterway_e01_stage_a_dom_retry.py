#!/usr/bin/env python3
"""Execution-only dynamic-DOM adapter for US-WATERWAY-E01 Stage A.

Preserves the frozen Stage A scientific contract. Oracle APEX renders a fixed-
header clone plus a row-bearing ``_orig`` table and may replace that data table
while scripts settle or pagination advances. This adapter avoids retaining stale
row WebElements: each page is snapshotted as HTML, only the target table is
parsed, Average Delay annual cells are immediately reduced to nonblank booleans,
and then pagination advances. No scientific variable, support threshold,
identity rule, annual-cell semantics, or outcome boundary changes.
"""
from __future__ import annotations

import re
import time
from html.parser import HTMLParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import us_waterway_e01_stage_a as stage_a

TARGET_ID = stage_a.INDIVIDUAL_TABLE_ID + "_orig"


class TargetTableParser(HTMLParser):
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
        if tag == "table" and a.get("id") == TARGET_ID and not self.in_target:
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
            self.cell_tag = ""
            self.cell_text = ""
        elif tag == "tr" and self.row is not None and self.depth == 1:
            self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.depth -= 1
            if self.depth == 0:
                self.in_target = False


def parse_snapshot(html):
    p = TargetTableParser()
    p.feed(html)
    rows = p.rows
    header = None
    header_pos = None
    for i, row in enumerate(rows):
        if row and any(tag == "th" for tag, _ in row):
            header = [txt for _, txt in row]
            header_pos = i
            break
    if header is None:
        raise RuntimeError("target APEX data table header not present in snapshot")
    idx = {name: stage_a.header_index(header, name) for name in ["DISTRICT", "RIVER", "LOCK", "USAGE TYPE"]}
    yidx = {y: stage_a.year_header_index(header, y) for y in stage_a.YEARS}
    records = []
    first_sig = None
    for row in rows[header_pos + 1:]:
        vals = [txt for _, txt in row]
        if len(vals) < len(header):
            continue
        district = vals[idx["DISTRICT"]]
        river = vals[idx["RIVER"]]
        lock = vals[idx["LOCK"]]
        usage = vals[idx["USAGE TYPE"]]
        if first_sig is None:
            first_sig = (river, lock, usage)
        if usage.upper() != "AVERAGE DELAY (MINUTES)":
            continue
        present = {y: bool(vals[yidx[y]]) for y in stage_a.YEARS}
        key = (stage_a.code_part(river), stage_a.lockcode(stage_a.code_part(lock)))
        records.append((key, {
            "district": district,
            "river": river,
            "lock": lock,
            "year_nonblank": present,
            "all_years_nonblank": all(present.values()),
        }))
    return records, first_sig


def snapshot_sig(driver):
    try:
        _, sig = parse_snapshot(driver.page_source)
        return sig
    except Exception:
        return None


def scrape_annual_support_snapshot():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument(f"--user-agent={stage_a.UA}")
    driver = webdriver.Chrome(options=opts)
    all_delay = {}
    page_count = 0
    try:
        wait = WebDriverWait(driver, 30)
        driver.get(stage_a.HOME)
        wait.until(lambda d: "corps-locks" in d.current_url)
        driver.get(stage_a.ANNUAL)
        wait.until(lambda d: len(d.find_elements(By.ID, TARGET_ID)) >= 1)
        wait.until(lambda d: snapshot_sig(d) is not None)
        while True:
            # APEX may replace the table asynchronously. Parse one immutable page snapshot.
            records, first_sig = parse_snapshot(driver.page_source)
            for key, rec in records:
                all_delay[key] = rec
            page_count += 1

            region = driver.find_element(By.ID, stage_a.INDIVIDUAL_REGION_ID)
            buttons = region.find_elements(By.CSS_SELECTOR, "button.a-IRR-button--pagination[title='Next']")
            if not buttons:
                break
            disabled = buttons[0].get_attribute("disabled") is not None or buttons[0].get_attribute("aria-disabled") == "true"
            if disabled:
                break
            before = first_sig
            # Reacquire immediately before click to avoid keeping a stale element.
            region = driver.find_element(By.ID, stage_a.INDIVIDUAL_REGION_ID)
            btn = region.find_element(By.CSS_SELECTOR, "button.a-IRR-button--pagination[title='Next']")
            driver.execute_script("arguments[0].click();", btn)
            wait.until(lambda d: (snapshot_sig(d) is not None and snapshot_sig(d) != before))
            if page_count > 200:
                raise RuntimeError("pagination safety limit exceeded")
            time.sleep(0.1)
        return all_delay, page_count
    finally:
        driver.quit()


stage_a.scrape_annual_support = scrape_annual_support_snapshot

if __name__ == "__main__":
    stage_a.main()
