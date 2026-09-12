#!/usr/bin/env python3
from __future__ import annotations

import html, json, re, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'
OUT.mkdir(parents=True, exist_ok=True)
UA='AI-Innovative-Research-Engine/US-WW-F01 outcome-blind route probe'
URLS={
 'cwns_download':'https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download',
 'echo_downloads':'https://echo.epa.gov/tools/data-downloads',
 'echo_npdes_summary':'https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary',
 'echo_dmr_summary':'https://echo.epa.gov/tools/data-downloads/icis-npdes-dmr-summary',
}

def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'text/html,*/*'})
 with urllib.request.urlopen(req,timeout=120) as r:
  b=r.read(); return b.decode('utf-8','replace'), {'requested_url':url,'final_url':r.geturl(),'status':getattr(r,'status',200),'bytes':len(b),'content_type':r.headers.get('Content-Type')}

def links(text,base):
 out=[]
 for m in re.finditer(r'''(?:href|action)\s*=\s*["']([^"']+)["']''',text,re.I):
  u=html.unescape(m.group(1)); full=urllib.parse.urljoin(base,u)
  if any(k in full.casefold() for k in ('download','cwns','npdes','icis','xlsx','zip','csv')):
   out.append(full)
 return sorted(set(out))

def inputs(text):
 items=[]
 for tag in re.findall(r'<input\b[^>]*>',text,re.I):
  attrs={k.casefold():html.unescape(v) for k,v in re.findall(r'''([\w:-]+)\s*=\s*["']([^"']*)["']''',tag)}
  if attrs.get('name') or attrs.get('id'):
   items.append({k:attrs.get(k) for k in ('type','name','id','value') if attrs.get(k) is not None})
 return items[:200]

manifest={'id':'US-WW-F01-SOURCE-ROUTE-PROBE','issue':114,'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,'incremental_monetary_cost_usd':0,'pages':{}}
for key,url in URLS.items():
 text,meta=get(url)
 manifest['pages'][key]={'fetch':meta,'candidate_links':links(text,meta['final_url']),'form_inputs':inputs(text) if key=='cwns_download' else []}

# Explicitly record known schema facts from page text only, not outcome values.
summary_text=get(URLS['echo_npdes_summary'])[0]
manifest['echo_schema_text_support']={
 'npdes_id_present': bool(re.search(r'\bNPDES_ID\b',summary_text,re.I)),
 'registry_id_present': bool(re.search(r'\bREGISTRY_ID\b',summary_text,re.I)),
 'violation_id_present': bool(re.search(r'\bNPDES_VIOLATION_ID\b',summary_text,re.I)),
 'violation_date_like_present': bool(re.search(r'VIOLATION|SCHEDULE_DATE|DETECTION_DATE|REPORT_RECEIVED_DATE',summary_text,re.I)),
}
(OUT/'SOURCE_ROUTE_PROBE.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'cwns_links':len(manifest['pages']['cwns_download']['candidate_links']),'echo_links':len(manifest['pages']['echo_downloads']['candidate_links']),'schema':manifest['echo_schema_text_support']}))
