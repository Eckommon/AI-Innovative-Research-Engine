#!/usr/bin/env python3
from __future__ import annotations
import html, http.cookiejar, json, re, traceback, urllib.error, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
START='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'
UA='AI-Innovative-Research-Engine/US-WW-F01 CWNS national popup route probe'
JAR=http.cookiejar.CookieJar(); OPENER=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(JAR))

def get(url, referer=None):
 headers={'User-Agent':UA,'Accept':'text/html,*/*'}
 if referer: headers['Referer']=referer
 req=urllib.request.Request(url,headers=headers)
 try:
  with OPENER.open(req,timeout=120) as r:
   b=r.read(); return b.decode('utf-8','replace'),r.geturl(),getattr(r,'status',200),len(b),None
 except urllib.error.HTTPError as e:
  b=e.read(); return b.decode('utf-8','replace'),e.geturl(),e.code,len(b),{'type':'HTTPError','reason':str(e.reason),'headers':dict(e.headers.items())}
 except Exception as e:
  return '',url,None,0,{'type':type(e).__name__,'reason':str(e)}

def decode_js_url(s): return s.replace('\\u002F','/').replace('\\u0026','&').replace('\\u003F','?').replace('\\/','/')

out={'id':'US-WW-F01-CWNS-NATIONAL-CSV-POPUP-ROUTE','issue':114,'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,'incremental_monetary_cost_usd':0}
try:
 main,final,status,nbytes,main_error=get(START)
 out['main_fetch']={'url':final,'status':status,'bytes':nbytes,'error':main_error}
 main_dec=html.unescape(main)
 m=re.search(r"apex\.theme42\.dialog\('([^']*p2_location_id=NA[^']*p3_type=NA_CSV[^']*)'",main_dec,re.I)
 if not m:
  out['stage_error']={'stage':'extract_popup','reason':'NA_CSV popup route not found','sample_matches':re.findall(r'p2_location_id=NA.{0,300}',main_dec,re.I|re.S)[:5]}
 else:
  popup_rel=decode_js_url(m.group(1)); popup=urllib.parse.urljoin(final,popup_rel); out['popup_url']=popup
  text,pfinal,pstatus,pbytes,popup_error=get(popup,referer=final)
  out['popup_fetch']={'url':pfinal,'status':pstatus,'bytes':pbytes,'error':popup_error}
  out['session_cookie_names']=sorted({c.name for c in JAR})
  text_dec=html.unescape(text)
  links=[]
  for mm in re.finditer(r'''(?:href|action)\s*=\s*["']([^"']+)["']''',text_dec,re.I):
   u=decode_js_url(mm.group(1)); full=urllib.parse.urljoin(pfinal,u)
   if re.search(r'download|zip|csv|state-zip|location_id|NA_CSV|wwv_flow',full,re.I): links.append(full)
  controls=[]
  for tag in re.findall(r'<(?:a|button|input|form)\b[^>]*>',text_dec,re.I):
   dec=decode_js_url(tag)
   if re.search(r'download|zip|csv|p_request|apex\.submit|wwv_flow|location_id',dec,re.I): controls.append(re.sub(r'\s+',' ',dec)[:3000])
  snips=[]
  for pat in ('Download','NA_CSV','download-state-zip','p2_location_id','apex.submit','p_request','error','checksum','session'):
   for mm in re.finditer(re.escape(pat),text_dec,re.I):
    s=decode_js_url(text_dec[max(0,mm.start()-700):min(len(text_dec),mm.end()+1200)]); s=re.sub(r'\s+',' ',s)
    if s not in snips: snips.append(s)
  out['candidate_links']=sorted(set(links)); out['controls']=controls[:100]; out['snippets']=snips[:50]
except Exception as e:
 out['stage_error']={'stage':'unexpected','type':type(e).__name__,'reason':str(e),'traceback':traceback.format_exc()[-4000:]}

(OUT/'CWNS_NATIONAL_POPUP_ROUTE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'stage_error':out.get('stage_error'),'popup_fetch':out.get('popup_fetch'),'links':len(out.get('candidate_links',[]))}))
