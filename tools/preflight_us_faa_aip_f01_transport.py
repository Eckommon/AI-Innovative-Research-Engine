#!/usr/bin/env python3
from __future__ import annotations
import json, re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

UA={'User-Agent':'Mozilla/5.0 research-preflight/1.0'}
OUT={'outcomes_opened':False,'support_counts_computed':False}

def get(url):
    r=requests.get(url,headers=UA,timeout=60)
    r.raise_for_status(); return r

# FAA grant-history link transport only.
faa='https://www.faa.gov/airports/aip/grant_histories'
r=get(faa); s=BeautifulSoup(r.text,'html.parser')
links=[]
for tr in s.find_all('tr'):
    txt=' '.join(tr.stripped_strings)
    m=re.search(r'\b(2021|2022|2023|2024|2025)\b',txt)
    if not m: continue
    for a in tr.find_all('a',href=True):
        links.append({'year':int(m.group(1)),'text':' '.join(a.stripped_strings)[:120],'href':urljoin(faa,a['href'])})
OUT['faa_links']=links

# FAA LID header only.
lid='https://www.fly.faa.gov/rmt/data_file/locid_db.csv'
r=get(lid)
first=r.text.splitlines()[0] if r.text else ''
OUT['lid']={'url':lid,'status':r.status_code,'bytes':len(r.content),'header':first[:1000]}

# BTS Master Coordinate ASP.NET form transport only.
bts='https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10&gnoyr_VQ=FLL'
r=get(bts); s=BeautifulSoup(r.text,'html.parser')
forms=[]
for f in s.find_all('form'):
    item={'action':urljoin(bts,f.get('action') or ''),'method':(f.get('method') or 'get').lower(),'inputs':[],'selects':[]}
    for x in f.find_all('input'):
        name=x.get('name'); typ=(x.get('type') or '').lower(); val=x.get('value')
        if name and (typ in {'submit','button','checkbox','radio','hidden'} or re.search(r'download|prezip|zip|field|select',name,re.I)):
            item['inputs'].append({'name':name,'type':typ,'value':(val[:300] if isinstance(val,str) else val),'id':x.get('id')})
    for x in f.find_all('select'):
        item['selects'].append({'name':x.get('name'),'id':x.get('id'),'options':[{'value':o.get('value'),'text':' '.join(o.stripped_strings)[:100]} for o in x.find_all('option')[:20]]})
    forms.append(item)
OUT['bts_master']={'url':bts,'status':r.status_code,'bytes':len(r.content),'forms':forms}

# Extract script snippets relevant to download/prezip without submitting anything.
snips=[]
for sc in s.find_all('script'):
    t=sc.string or sc.get_text(' ',strip=True)
    if t and re.search(r'prezip|download|zip',t,re.I):
        snips.append(re.sub(r'\s+',' ',t)[:1500])
OUT['bts_script_snippets']=snips[:20]
print(json.dumps(OUT,indent=2,ensure_ascii=False))
