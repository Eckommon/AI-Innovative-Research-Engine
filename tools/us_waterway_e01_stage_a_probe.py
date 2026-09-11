#!/usr/bin/env python3
"""Outcome-blind Stage-A structural probe for Corps Locks Annual Usage.

Reads only page/form/table structure and identity/year cells. It never converts or
persists delay, processing, traffic, or hydrology magnitudes.
"""
from __future__ import annotations
import hashlib, json, re, time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
import urllib.request, http.cookiejar

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-E01"
HOME = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/home"
ANNUAL = "https://ndc.ops.usace.army.mil/ords/r/lpms/corps-locks/annual-usage-report"
UA = "AI-Innovative-Research-Engine/US-WATERWAY-E01-stage-a-probe"
YEARS = {str(y) for y in range(2016, 2026)}


def fetch(opener, url, attempts=4):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
            with opener.open(req, timeout=120) as r:
                return r.read(), getattr(r, "status", 200), r.geturl()
        except Exception as e:
            last = e
            if i + 1 < attempts:
                time.sleep(2 * (i + 1))
    raise last


class Probe(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.inputs = []
        self.selects = []
        self.tables = []
        self._select = None
        self._option = None
        self._table = None
        self._cell = None
        self._row = None
        self._in_script = False
        self._script_parts = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "input":
            name = str(a.get("name") or "")
            iid = str(a.get("id") or "")
            value = str(a.get("value") or "")
            keep = ("YEAR" in name.upper() or "YEAR" in iid.upper() or value in YEARS or
                    any(k in name.upper() for k in ["LOCK", "RIVER"]) or any(k in iid.upper() for k in ["LOCK", "RIVER"]))
            if keep:
                self.inputs.append({"name": name, "id": iid, "type": a.get("type"), "value": value if value in YEARS else ""})
        elif tag == "select":
            self._select = {"name": str(a.get("name") or ""), "id": str(a.get("id") or ""), "options": []}
        elif tag == "option" and self._select is not None:
            self._option = {"value": str(a.get("value") or ""), "text": ""}
        elif tag == "table":
            self._table = {"id": str(a.get("id") or ""), "class": str(a.get("class") or ""), "rows": []}
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in {"th", "td"} and self._row is not None:
            self._cell = {"tag": tag, "text": ""}
        elif tag == "script":
            self._in_script = True
            self._script_parts = []

    def handle_endtag(self, tag):
        if tag == "option" and self._option is not None and self._select is not None:
            self._option["text"] = self._option["text"].strip()
            if self._option["value"] in YEARS or self._option["text"] in YEARS:
                self._select["options"].append(self._option)
            self._option = None
        elif tag == "select" and self._select is not None:
            if ("YEAR" in self._select["name"].upper() or "YEAR" in self._select["id"].upper() or self._select["options"]):
                self.selects.append(self._select)
            self._select = None
        elif tag in {"th", "td"} and self._cell is not None and self._row is not None:
            self._cell["text"] = self._cell["text"].strip()
            self._row.append(self._cell)
            self._cell = None
        elif tag == "tr" and self._row is not None and self._table is not None:
            self._table["rows"].append(self._row)
            self._row = None
        elif tag == "table" and self._table is not None:
            self.tables.append(self._table)
            self._table = None
        elif tag == "script":
            self._in_script = False

    def handle_data(self, data):
        if self._option is not None:
            self._option["text"] += data
        if self._cell is not None:
            self._cell["text"] += data
        if self._in_script:
            self._script_parts.append(data)


def safe_table_summary(t):
    rows = t["rows"]
    header = []
    header_idx = None
    for i, row in enumerate(rows):
        if any(c["tag"] == "th" for c in row):
            header = [c["text"] for c in row]
            header_idx = i
            break
    wanted = []
    for i, h in enumerate(header):
        u = re.sub(r"\s+", " ", h.upper()).strip()
        if any(k in u for k in ["LOCK", "RIVER", "WATERWAY", "YEAR"]):
            wanted.append(i)
    samples = []
    years = set()
    identity_rows = 0
    if header_idx is not None and wanted:
        for row in rows[header_idx + 1:]:
            vals = []
            for i in wanted:
                if i < len(row):
                    text = row[i]["text"].strip()
                    vals.append({"header": header[i], "text": text})
                    if text in YEARS:
                        years.add(text)
            if any(v["text"] for v in vals):
                identity_rows += 1
                if len(samples) < 40:
                    samples.append(vals)
    return {
        "id": t["id"], "class": t["class"], "header": header,
        "identity_column_indexes": wanted,
        "identity_row_count": identity_rows,
        "year_labels_in_identity_cells": sorted(years),
        "identity_samples": samples,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    home_b, home_status, home_final = fetch(opener, HOME)
    annual_b, annual_status, annual_final = fetch(opener, ANNUAL)
    text = annual_b.decode("utf-8", "replace")
    p = Probe(); p.feed(text)
    summaries = [safe_table_summary(t) for t in p.tables]
    script_text = text
    item_tokens = sorted(set(re.findall(r"\bP\d+_[A-Z0-9_]*YEAR[A-Z0-9_]*\b", script_text, re.I)))
    worksheet_ids = sorted(set(re.findall(r"p_worksheet_id(?:\\u0026|=)(\d+)", script_text, re.I)))
    region_ids = sorted(set(re.findall(r"(?:regionId|region_id)[\"']?\s*[:=]\s*[\"']?(\d+)", script_text, re.I)))
    year_labels = sorted(set(re.findall(r"\b(?:2016|2017|2018|2019|2020|2021|2022|2023|2024|2025)\b", text)))
    out = {
        "boundary": {
            "delay_magnitudes_parsed": False,
            "processing_magnitudes_parsed": False,
            "traffic_magnitudes_parsed": False,
            "hydrology_values_parsed": False,
            "relationship_computed": False,
        },
        "home": {"status": home_status, "final_url": home_final, "bytes": len(home_b), "sha256": hashlib.sha256(home_b).hexdigest()},
        "annual": {"status": annual_status, "final_url": annual_final, "bytes": len(annual_b), "sha256": hashlib.sha256(annual_b).hexdigest()},
        "year_labels_anywhere": year_labels,
        "year_item_tokens": item_tokens,
        "year_inputs": p.inputs,
        "year_selects": p.selects,
        "worksheet_ids": worksheet_ids,
        "region_ids": region_ids,
        "tables": summaries,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "STAGE_A_ANNUAL_USAGE_SCHEMA_PROBE.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# US-WATERWAY-E01 Stage A Annual Usage Schema Probe", "",
        "Outcome-blind structural probe: numerical delay/processing/traffic/hydrology magnitudes were not parsed.", "",
        f"- Annual Usage HTTP: **{annual_status}**",
        f"- Annual Usage bytes: **{len(annual_b)}**",
        f"- page year labels: **{', '.join(year_labels)}**",
        f"- year item tokens: `{item_tokens}`",
        f"- worksheet IDs: `{worksheet_ids}`",
        f"- tables found: **{len(summaries)}**",
    ]
    for i, s in enumerate(summaries):
        lines += ["", f"## Table {i+1}", f"- id: `{s['id']}`", f"- headers: `{s['header']}`", f"- identity rows: **{s['identity_row_count']}**", f"- year labels in identity cells: `{s['year_labels_in_identity_cells']}`"]
        for sample in s["identity_samples"][:10]:
            lines.append("- identity: " + " | ".join(f"{x['header']}={x['text']}" for x in sample))
    lines += ["", "Incremental monetary cost: **0 USD**."]
    (OUT / "STAGE_A_ANNUAL_USAGE_SCHEMA_PROBE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
