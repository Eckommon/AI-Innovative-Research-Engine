#!/usr/bin/env python3
from __future__ import annotations
import html, http.cookiejar, json, re, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
START='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'
UA='AI-Innovative-Research-Engine/US-WW-F01 CWNS national popup route probe'
JAR=http.cookiejar.CookieJar()
OPENER=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(JAR))

def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'text/html,*/*'})
 with OPENER.open(req,timeout=120) as r:
  b=r.read(); return b.decode('utf-8','replace'),r.geturl(),getattr(r,'status',200),len(b)

def decode_js_url(s):
 return s.replace('\\u002F','/').replace('\\u0026','&').replace('\\u003F','?').replace('\\/','/')

main,final,status,nbytes=get(START)
m=re.search(r"apex\.theme42\.dialog\('([^']*p2_location_id=NA[^']*p3_type=NA_CSV[^']*)'",main,re.I)
if not m: raise RuntimeError('NA_CSV popup route not found')
popup_rel=html.unescape(decode_js_url(m.group(1)))
popup=urllib.parse.urljoin(final,popup_rel)
text,pfinal,pstatus,pbytes=get(popup)

links=[]
for mm in re.finditer(r'''(?:href|action)\s*=\s*["']([^"']+)["']''',text,re.I):
 u=html.unescape(decode_js_url(mm.group(1))); full=urllib.parse.urljoin(pfinal,u)
 if re.search(r'download|zip|csv|state-zip|location_id|NA_CSV|wwv_flow',full,re.I): links.append(full)
controls=[]
for tag in re.findall(r'<(?:a|button|input|form)\b[^>]*>',text,re.I):
 dec=html.unescape(decode_js_url(tag))
 if re.search(r'download|zip|csv|p_request|apex\.submit|wwv_flow|location_id',dec,re.I):
  controls.append(re.sub(r'\s+',' ',dec)[:3000])
snips=[]
for pat in ('Download','NA_CSV','download-state-zip','p2_location_id','apex.submit','p_request'):
 for mm in re.finditer(re.escape(pat),text,re.I):
  s=html.unescape(decode_js_url(text[max(0,mm.start()-700):min(len(text),mm.end()+1200)])); s=re.sub(r'\s+',' ',s)
  if s not in snips: snips.append(s)
out={'id':'US-WW-F01-CWNS-NATIONAL-CSV-POPUP-ROUTE','issue':114,'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,'main_fetch':{'url':final,'status':status,'bytes':nbytes},'popup_url':popup,'popup_fetch':{'url':pfinal,'status':pstatus,'bytes':pbytes},'session_cookie_names':sorted({c.name for c in JAR}),'candidate_links':sorted(set(links)),'controls':controls[:100],'snippets':snips[:50],'incremental_monetary_cost_usd':0}
(OUT/'CWNS_NATIONAL_POPUP_ROUTE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'popup_status':pstatus,'links':len(out['candidate_links']),'controls':len(out['controls']),'cookies':out['session_cookie_names']}))
