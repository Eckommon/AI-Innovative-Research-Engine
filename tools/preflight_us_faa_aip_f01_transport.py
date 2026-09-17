#!/usr/bin/env python3
from __future__ import annotations
import csv, io, json, re, zipfile
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

UA={'User-Agent':'Mozilla/5.0 research-preflight/1.0'}
OUT={'outcomes_opened':False,'support_counts_computed':False,'download_payload_rows_inspected':False}
sess=requests.Session(); sess.headers.update(UA)

def get(url):
    r=sess.get(url,timeout=60); r.raise_for_status(); return r

faa='https://www.faa.gov/airports/aip/grant_histories'
landing=[]; xlsx_urls={}
for y in range(2021,2026):
    url=f'{faa}/{y}'
    rr=get(url); ss=BeautifulSoup(rr.text,'html.parser')
    anchors=[]
    for a in ss.find_all('a',href=True):
        href=urljoin(url,a['href']); txt=' '.join(a.stripped_strings)
        if re.search(r'\.xlsx(?:$|\?)',href,re.I): xlsx_urls[y]=href
        if re.search(r'grant|summary|excel|xls|xlsx|csv|download',txt+' '+href,re.I): anchors.append({'text':txt[:160],'href':href})
    landing.append({'year':y,'url':url,'status':rr.status_code,'anchors':anchors[:40]})
OUT['faa_landing']=landing
schemas={}
for y,u in sorted(xlsx_urls.items()):
    rr=get(u); wb=load_workbook(io.BytesIO(rr.content),read_only=True,data_only=True)
    items=[]
    for ws in wb.worksheets[:5]:
        rows=[]
        for row in ws.iter_rows(min_row=1,max_row=15,values_only=True): rows.append([str(v)[:120] if v is not None else '' for v in row[:25]])
        items.append({'sheet':ws.title,'first_rows':rows})
    schemas[str(y)]={'url':u,'bytes':len(rr.content),'sheets':items}
OUT['faa_xlsx_schema_samples']=schemas

lid='https://www.fly.faa.gov/rmt/data_file/locid_db.csv'
r=get(lid); text=r.content.decode('utf-8-sig',errors='replace'); rdr=csv.DictReader(io.StringIO(text)); sample=[]
for i,row in enumerate(rdr):
    if i>=30: break
    sample.append({k:(v[:160] if isinstance(v,str) else v) for k,v in row.items()})
OUT['lid']={'url':lid,'status':r.status_code,'bytes':len(r.content),'fieldnames':rdr.fieldnames,'sample_rows':sample}

bts='https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10&gnoyr_VQ=FLL'
r=get(bts); s=BeautifulSoup(r.text,'html.parser'); form=next(f for f in s.find_all('form') if (f.get('method') or '').lower()=='post' and f.find('input',{'name':'btnDownload'}))
payload={}
for x in form.find_all('input'):
    name=x.get('name'); typ=(x.get('type') or '').lower()
    if name and typ=='hidden': payload[name]=x.get('value') or ''
payload.update({'cboGeography':'All','cboYear':'All','cboPeriod':'All','AIRPORT_SEQ_ID':'on','AIRPORT_ID':'on','AIRPORT':'on','AIRPORT_STATE_CODE':'on','AIRPORT_START_DATE':'on','AIRPORT_THRU_DATE':'on','AIRPORT_IS_CLOSED':'on','AIRPORT_IS_LATEST':'on','chkDownloadZip':'on','btnDownload':'Download'})
post=sess.post(urljoin(bts,form.get('action') or ''),data=payload,timeout=120,allow_redirects=True)
info={'status':post.status_code,'content_type':post.headers.get('content-type'),'bytes':len(post.content),'zip_magic':post.content[:2]==b'PK'}
if post.content[:2]==b'PK':
    z=zipfile.ZipFile(io.BytesIO(post.content)); info['members']=z.namelist()
    if z.namelist():
        raw=z.read(z.namelist()[0]); txt=raw.decode('utf-8-sig',errors='replace'); cr=csv.reader(io.StringIO(txt)); info['csv_header']=next(cr,[]); info['sample_rows']=[next(cr,[]) for _ in range(10)]
OUT['bts_master_schema_sample']=info
print(json.dumps(OUT,indent=2,ensure_ascii=False))
