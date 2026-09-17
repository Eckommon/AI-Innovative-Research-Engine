#!/usr/bin/env python3
from __future__ import annotations
import csv, io, json, zipfile
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

OUT={'outcomes_opened':False,'support_counts_computed':False}
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 research-preflight/1.0'})
url='https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10&gnoyr_VQ=FLL'
r=s.get(url,timeout=60); r.raise_for_status(); soup=BeautifulSoup(r.text,'html.parser')
form=next(f for f in soup.find_all('form') if (f.get('method') or '').lower()=='post' and f.find('input',{'name':'btnDownload'}))
payload={}
for x in form.find_all('input'):
    if x.get('name') and (x.get('type') or '').lower()=='hidden': payload[x['name']]=x.get('value') or ''
payload.update({'cboGeography':'All','cboYear':'All','cboPeriod':'All','AIRPORT_SEQ_ID':'on','AIRPORT_ID':'on','AIRPORT':'on','AIRPORT_STATE_CODE':'on','AIRPORT_START_DATE':'on','AIRPORT_THRU_DATE':'on','AIRPORT_IS_CLOSED':'on','AIRPORT_IS_LATEST':'on','chkDownloadZip':'on','btnDownload':'Download'})
p=s.post(urljoin(url,form.get('action') or ''),data=payload,timeout=120); p.raise_for_status()
z=zipfile.ZipFile(io.BytesIO(p.content)); name=next(n for n in z.namelist() if n.upper().endswith('T_MASTER_CORD.CSV'))
text=z.read(name).decode('utf-8-sig',errors='replace'); cr=csv.reader(io.StringIO(text)); header=next(cr,[]); samples=[]
for i,row in enumerate(cr):
    if i>=15: break
    samples.append(row)
OUT['zip_bytes']=len(p.content); OUT['member']=name; OUT['header']=header; OUT['sample_rows']=samples
print(json.dumps(OUT,indent=2,ensure_ascii=False))
