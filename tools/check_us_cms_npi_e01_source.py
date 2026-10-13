#!/usr/bin/env python3
from __future__ import annotations
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
import hashlib, json, re, requests

ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"research/US-CMS-NPI-E01/evidence"
JSON_OUT=OUTDIR/"source-preflight-01.json"
MD_OUT=OUTDIR/"source-preflight-01.md"
URL="https://download.cms.gov/nppes/NPI_Files.html"
CONTRACT_SHA="48843c9979336dcd10fdff984f458277062d6f20"
ANCHOR="100526_101126"
MIN_START=date(2026,10,12)
UA="Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; metadata-only-source-check)"

def parse_range(token:str):
    m=re.fullmatch(r"(\d{6})_(\d{6})",token)
    if not m:return None
    try:
        s=datetime.strptime(m.group(1),"%m%d%y").date()
        e=datetime.strptime(m.group(2),"%m%d%y").date()
        return s,e
    except ValueError:
        return None

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable source-preflight-01 already exists")
    r=requests.get(URL,headers={"User-Agent":UA},timeout=90,allow_redirects=True)
    r.raise_for_status()
    html=r.text
    page_sha=hashlib.sha256(r.content).hexdigest()

    # Extract only listing metadata/hrefs. Do not request any ZIP href.
    link_re=re.compile(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',re.I|re.S)
    weekly=[]
    seen=set()
    for href,label_html in link_re.findall(html):
        label=re.sub(r"<[^>]+>"," ",label_html)
        label=" ".join(label.split())
        hay=f"{label} {href}"
        if "weekly" not in hay.lower() and "weekly" not in label.lower():
            # Some links contain only date token; surrounding text is handled below.
            continue
        m=re.search(r"(\d{6}_\d{6})",hay)
        if not m:continue
        token=m.group(1)
        rng=parse_range(token)
        if not rng:continue
        key=(token,urljoin(r.url,href))
        if key in seen:continue
        seen.add(key)
        weekly.append({
            "token":token,
            "start":rng[0].isoformat(),
            "end":rng[1].isoformat(),
            "label":label,
            "href":urljoin(r.url,href),
        })

    # Fallback: find weekly tokens from page text and pair href where possible.
    text=re.sub(r"<[^>]+>"," ",html)
    text=" ".join(text.split())
    for token in re.findall(r"\b\d{6}_\d{6}\b",text):
        rng=parse_range(token)
        if not rng:continue
        if any(x["token"]==token for x in weekly):continue
        href_m=re.search(r'href=["\']([^"\']*'+re.escape(token)+r'[^"\']*)["\']',html,re.I)
        weekly.append({
            "token":token,
            "start":rng[0].isoformat(),
            "end":rng[1].isoformat(),
            "label":None,
            "href":urljoin(r.url,href_m.group(1)) if href_m else None,
        })

    weekly.sort(key=lambda x:(x["start"],x["end"],x["token"]))
    qualifying=[x for x in weekly if date.fromisoformat(x["start"])>=MIN_START and date.fromisoformat(x["end"])>MIN_START]
    earliest=qualifying[0] if qualifying else None
    anchor_present=any(x["token"]==ANCHOR for x in weekly) or ANCHOR in html

    ev={
        "research":"US-CMS-NPI-E01",
        "preflight":1,
        "contract_sha":CONTRACT_SHA,
        "checked_at_utc":datetime.now(timezone.utc).isoformat(),
        "source_page":{
            "requested_url":URL,
            "final_url":r.url,
            "status":r.status_code,
            "content_type":r.headers.get("content-type"),
            "last_modified":r.headers.get("last-modified"),
            "etag":r.headers.get("etag"),
            "bytes":len(r.content),
            "sha256":page_sha,
        },
        "metadata_only":True,
        "zip_body_opened":False,
        "future_membership_opened":False,
        "anchor_token":ANCHOR,
        "anchor_present":anchor_present,
        "weekly_listings":weekly,
        "qualifying_rule":{
            "min_start":"2026-10-12",
            "end_must_be_after":"2026-10-12",
        },
        "qualifying_count":len(qualifying),
        "earliest_qualifying":earliest,
        "disposition":"SOURCE_READY_US_CMS_NPI_E01" if earliest else "WAIT_SOURCE_US_CMS_NPI_E01",
        "incremental_monetary_cost_usd":0,
    }
    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

    lines=[
        "# US-CMS-NPI-E01 — Source Preflight 01","",
        f"**Disposition:** `{ev['disposition']}`","",
        f"- CMS page status: **{r.status_code}**",
        f"- Metadata-only: **True**",
        f"- ZIP body opened: **False**",
        f"- Future membership opened: **False**",
        f"- Pre-baseline anchor `{ANCHOR}` present: **{anchor_present}**",
        f"- Qualifying weekly listings: **{len(qualifying)}**","",
        "## Weekly listings observed","",
        "| Token | Start | End | Href recorded |",
        "|---|---|---|:---:|",
    ]
    for x in weekly:
        lines.append(f"| `{x['token']}` | {x['start']} | {x['end']} | {'yes' if x.get('href') else 'no'} |")
    lines += ["","## Earliest qualifying weekly","",
              f"`{earliest['token']}`" if earliest else "**None. Remain WAIT_SOURCE.**","",
              "No weekly ZIP href was requested. This preflight consumed listing metadata only.","",
              "Incremental monetary cost: **0 USD**.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"],len(weekly),len(qualifying))

if __name__=="__main__":
    main()
