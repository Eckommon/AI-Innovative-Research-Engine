#!/usr/bin/env python3
from pathlib import Path
import hashlib, io, json, re, urllib.request, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/US-IRS-EO-N01/schema-application-pending-map.json'
URL='https://www.irs.gov/pub/irs-tege/990x-schema-2019v5.1.zip'
UA='Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)'
req=urllib.request.Request(URL,headers={'User-Agent':UA,'Accept':'*/*'})
with urllib.request.urlopen(req,timeout=90) as r: raw=r.read()
zf=zipfile.ZipFile(io.BytesIO(raw))
hits=[]
for n in zf.namelist():
    if not n.lower().endswith('.xsd'): continue
    txt=zf.read(n).decode('utf-8',errors='replace')
    for tag in ('ApplicationPending','ApplicationPendingInd'):
        for m in re.finditer(r'<(?:xs|xsd):element\b[^>]*(?:name|ref)=["\'][^"\']*'+tag+r'["\'][^>]*>',txt):
            hits.append({'tag':tag,'file':n,'declaration':re.sub(r'\s+',' ',m.group(0))[:800]})
e={'research':'US-IRS-EO-N01','contract_sha':'70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8',
   'schema_sha256':hashlib.sha256(raw).hexdigest(),'hits':hits,
   'historical_return_rows_opened':0,'future_outcome_rows_opened':0,
   'scientific_contract_changed':False,'incremental_monetary_cost_usd':0}
OUT.write_text(json.dumps(e,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(hits,sort_keys=True))
