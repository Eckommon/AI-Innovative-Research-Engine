#!/usr/bin/env python3
from __future__ import annotations
import json, re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

UA={'User-Agent':'Mozilla/5.0 research-preflight/1.0'}
OUT={'outcomes_opened':False,'support_counts_computed':False,'download_payload_rows_inspected':False}
sess=requests.Session(); sess.headers.update(UA)

def get(url):
    r=sess.get(url,timeout=60); r.raise_for_status(); return r

faa='https://www.faa.gov/airports/aip/grant_histories'
landing=[]
for y in range(2021,2026):
    url=f'{faa}/{y}'
    rr=get(url); ss=BeautifulSoup(rr.text,'html.parser')
    anchors=[]
    for a in ss.find_all('a',href=True):
        href=urljoin(url,a['href']); txt=' '.join(a.stripped_strings)
        if re.search(r'grant|summary|excel|xls|xlsx|csv|download',txt+' '+href,re.I):
            anchors.append({'text':txt[:160],'href':href})
    landing.append({'year':y,'url':url,'status':rr.status_code,'anchors':anchors[:40]})
OUT['faa_landing']=landing

lid='https://www.fly.faa.gov/rmt/data_file/locid_db.csv'
r=get(lid)
OUT['lid']={'url':lid,'status':r.status_code,'bytes':len(r.content),'header':(r.text.splitlines()[0] if r.text else '')[:1000]}

bts='https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10&gnoyr_VQ=FLL'
r=get(bts); s=BeautifulSoup(r.text,'html.parser')
form=next(f for f in s.find_all('form') if (f.get('method') or '').lower()=='post' and f.find('input',{'name':'btnDownload'}))
payload={}
for x in form.find_all('input'):
    name=x.get('name'); typ=(x.get('type') or '').lower()
    if name and typ=='hidden': payload[name]=x.get('value') or ''
payload.update({'cboGeography':'All','cboYear':'All','cboPeriod':'All','AIRPORT_SEQ_ID':'on','AIRPORT_ID':'on','AIRPORT':'on','AIRPORT_STATE_CODE':'on','AIRPORT_START_DATE':'on','AIRPORT_THRU_DATE':'on','AIRPORT_IS_CLOSED':'on','AIRPORT_IS_LATEST':'on','chkDownloadZip':'on','btnDownload':'Download'})
post=sess.post(urljoin(bts,form.get('action') or ''),data=payload,timeout=120,allow_redirects=True)
info={'status':post.status_code,'final_url':post.url,'content_type':post.headers.get('content-type'),'bytes':len(post.content),'zip_magic':post.content[:2]==b'PK'}
if 'text/html' in (post.headers.get('content-type') or '').lower():
    ps=BeautifulSoup(post.text,'html.parser'); cand=[]
    for a in ps.find_all('a',href=True):
        h=urljoin(post.url,a['href']); t=' '.join(a.stripped_strings)
        if re.search(r'\.zip|\.csv|download|prezip',h+' '+t,re.I): cand.append({'text':t[:120],'href':h})
    info['candidate_links']=cand[:30]
OUT['bts_master_post']=info
print(json.dumps(OUT,indent=2,ensure_ascii=False))
