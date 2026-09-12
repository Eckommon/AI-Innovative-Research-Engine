#!/usr/bin/env python3
from __future__ import annotations
import html, json, re, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
URL='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'
UA='AI-Innovative-Research-Engine/US-WW-F01 CWNS APEX route inspection'
req=urllib.request.Request(URL,headers={'User-Agent':UA,'Accept':'text/html,*/*'})
with urllib.request.urlopen(req,timeout=120) as r:
    raw=r.read().decode('utf-8','replace'); final=r.geturl()

# Preserve only structural snippets around download controls; no survey values are touched.
patterns=['Download CSVs','Download Access Database','download-state-zip','download-national','apex.submit','p_request','NATIONAL','ZIP']
snips=[]
for pat in patterns:
    for m in re.finditer(re.escape(pat),raw,re.I):
        a=max(0,m.start()-500); b=min(len(raw),m.end()+900)
        s=html.unescape(raw[a:b])
        s=re.sub(r'\s+',' ',s)
        if s not in snips: snips.append(s)

# Capture onclick/button/form structural attributes containing download/request semantics.
controls=[]
for tag in re.findall(r'<(?:a|button|input|form)\b[^>]*>',raw,re.I):
    dec=html.unescape(tag)
    if re.search(r'download|p_request|apex\.submit|wwv_flow',dec,re.I):
        attrs={k.lower():v for k,v in re.findall(r'''([\w:-]+)\s*=\s*["']([^"']*)["']''',dec)}
        controls.append({k:attrs[k] for k in ('tag','id','name','type','value','href','action','onclick','data-url','data-request') if k in attrs})
        if 'raw' not in attrs:
            controls[-1]['raw']=re.sub(r'\s+',' ',dec)[:2000]

urls=sorted(set(re.findall(r'https?://[^\s"\'<>]+',html.unescape(raw))))
urls=[u for u in urls if re.search(r'download|zip|xlsx|csv|cwns',u,re.I)]

out={'id':'US-WW-F01-CWNS-APEX-ROUTE-INSPECTION','issue':114,'source_url':URL,'final_url':final,'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,'controls':controls,'candidate_absolute_urls':urls,'snippets':snips[:50],'incremental_monetary_cost_usd':0}
(OUT/'CWNS_APEX_ROUTE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'controls':len(controls),'urls':len(urls),'snippets':len(out['snippets'])}))
