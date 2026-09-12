#!/usr/bin/env python3
from __future__ import annotations

import csv
import io
import json
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "CA-GRAIN-E02"
GSW_URLS = {
    "2023-24": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2023-24/gsw-shg-en.csv",
    "2024-25": "https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/2024-25/gsw-shg-en.csv",
}
GRAINS = {"Amber Durum","Barley","Beans","Canaryseed","Canola","Chick Peas","Corn","Flaxseed","Lentils","Mustard Seed","Oats","Peas","Rye","Soybeans","Wheat"}
REGIONS = {"Alberta","British Columbia","Manitoba","Saskatchewan"}
START = date(2023,8,1); END = date(2025,7,31)
UA = "AI-Innovative-Research-Engine/CA-GRAIN-E02 duplicate-key audit"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def decode(b):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try: return b.decode(enc)
        except UnicodeDecodeError: pass
    raise RuntimeError("decode")


def hnorm(s): return re.sub(r"[_\-\s]+"," ",(s or "").strip()).casefold()
def exact(headers, name):
    m={hnorm(h):h for h in headers}; return m.get(hnorm(name))
def norm(s): return re.sub(r"\s+"," ",(s or "").strip()).casefold()

def parse_iso_or_unambiguous(raw):
    s=(raw or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s): return datetime.strptime(s,"%Y-%m-%d").date(), "YMD"
    if re.fullmatch(r"\d{4}/\d{2}/\d{2}", s): return datetime.strptime(s,"%Y/%m/%d").date(), "YMD_SLASH"
    # For ambiguous slash formats, do not silently choose: report both viable parses.
    return None, "AMBIGUOUS_OR_OTHER"

def monday(d): return d-timedelta(days=d.weekday())

records=[]
raw_format_counts=Counter()
for crop,url in GSW_URLS.items():
    reader=csv.DictReader(io.StringIO(decode(fetch(url))))
    headers=reader.fieldnames or []
    hd=exact(headers,"week_ending_date") or exact(headers,"Week Ending Date")
    hw=exact(headers,"worksheet"); hm=exact(headers,"metric"); hp=exact(headers,"period")
    hg=exact(headers,"grain"); hgrade=exact(headers,"grade"); hr=exact(headers,"region") or exact(headers,"Region")
    if not all((hd,hw,hm,hp,hg,hgrade,hr)): raise RuntimeError((crop,headers))
    for row in reader:
        if norm(row.get(hw))!=norm("Primary") or norm(row.get(hm))!=norm("Deliveries") or norm(row.get(hp))!=norm("Current Week"): continue
        if (row.get(hgrade) or "").strip()!="": continue
        grain=(row.get(hg) or "").strip(); region=(row.get(hr) or "").strip()
        if grain not in GRAINS or region not in REGIONS: continue
        raw=(row.get(hd) or "").strip()
        d,fmt=parse_iso_or_unambiguous(raw); raw_format_counts[fmt]+=1
        if d is None:
            records.append({"crop":crop,"raw_date":raw,"parsed_date":None,"week":None,"grain":grain,"region":region})
            continue
        if not (START<=d<=END): continue
        records.append({"crop":crop,"raw_date":raw,"parsed_date":d.isoformat(),"week":monday(d).isoformat(),"grain":grain,"region":region})

# Key audit uses only rows with unambiguous parsed dates.
by_key=defaultdict(list)
for rec in records:
    if rec["week"] is not None:
        by_key[(rec["week"],rec["grain"],rec["region"])].append((rec["crop"],rec["raw_date"],rec["parsed_date"]))

dup_weeks=defaultdict(lambda:{"duplicate_key_count":0,"raw_dates":Counter(),"crops":Counter(),"examples":[]})
for (wk,g,r), items in by_key.items():
    if len(items)>1:
        x=dup_weeks[wk]; x["duplicate_key_count"]+=1
        for crop,raw,pd in items:
            x["raw_dates"][raw]+=1; x["crops"][crop]+=1
        if len(x["examples"])<5:
            x["examples"].append({"grain":g,"region":r,"occurrences":[{"crop":c,"raw_date":raw,"parsed_date":pd} for c,raw,pd in items]})

out={
    "id":"CA-GRAIN-E02-DUPLICATE-KEY-AUDIT",
    "issue":110,
    "values_read":False,
    "relationship_computed":False,
    "raw_date_format_counts":dict(raw_format_counts),
    "ambiguous_or_other_date_samples":sorted({r["raw_date"] for r in records if r["parsed_date"] is None})[:30],
    "duplicate_normalized_weeks":{
        wk:{
            "duplicate_key_count":v["duplicate_key_count"],
            "raw_dates":dict(v["raw_dates"]),
            "crops":dict(v["crops"]),
            "examples":v["examples"],
        } for wk,v in sorted(dup_weeks.items())
    },
    "interpretation_rule":"Audit only. Does not alter Issue #110 preregistration or authorize deduplication.",
    "incremental_monetary_cost_usd":0,
}
(OUT/"DUPLICATE_KEY_AUDIT.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"date_formats":dict(raw_format_counts),"duplicate_weeks":len(dup_weeks),"values_read":False}))
