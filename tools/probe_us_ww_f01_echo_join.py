#!/usr/bin/env python3
from __future__ import annotations

import csv, io, json, os, re, shutil, tempfile, time, urllib.request, zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
TMP=Path(os.environ.get('RUNNER_TEMP','/tmp'))/'us-ww-f01-echo'; TMP.mkdir(parents=True,exist_ok=True)
CWNS_URL='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'
ECHO_URL='https://echo.epa.gov/files/echodownloads/npdes_downloads.zip'
UA='AI-Innovative-Research-Engine/US-WW-F01 exact join probe'

def decode(b):
 for enc in ('utf-8-sig','utf-8','cp1252','latin-1'):
  try:return b.decode(enc)
  except UnicodeDecodeError:pass
 raise RuntimeError('decode')

def normid(s): return re.sub(r'\s+','',(s or '').strip()).upper()
def rows_from_bytes(b): return csv.DictReader(io.StringIO(decode(b)))

def download_cwns():
 dl=TMP/'cwns'; dl.mkdir(exist_ok=True)
 opts=webdriver.ChromeOptions(); opts.add_argument('--headless=new'); opts.add_argument('--no-sandbox'); opts.add_argument('--disable-dev-shm-usage'); opts.add_argument('--window-size=1440,1200')
 opts.add_experimental_option('prefs',{'download.default_directory':str(dl),'download.prompt_for_download':False,'download.directory_upgrade':True,'safebrowsing.enabled':True})
 driver=webdriver.Chrome(options=opts)
 try:
  driver.get(CWNS_URL); wait=WebDriverWait(driver,30)
  btn=wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if 'p3_type=NA_CSV' in (x.get_attribute('onclick') or '')),None)); btn.click()
  wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,'iframe'))>0)
  found=False
  for fr in driver.find_elements(By.CSS_SELECTOR,'iframe'):
   driver.switch_to.default_content(); driver.switch_to.frame(fr)
   if driver.find_elements(By.ID,'P3_QUESTION'): found=True; break
  if not found: raise RuntimeError('CWNS dialog not found')
  Select(wait.until(EC.presence_of_element_located((By.ID,'P3_QUESTION')))).select_by_visible_text('Researcher')
  wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if (x.text or '').strip()=='Download'),None)).click()
  deadline=time.time()+90
  while time.time()<deadline:
   z=[p for p in dl.iterdir() if p.suffix.lower()=='.zip' and not p.name.endswith('.crdownload')]
   if z: return max(z,key=lambda p:p.stat().st_mtime)
   time.sleep(1)
  raise RuntimeError('CWNS zip not downloaded')
 finally: driver.quit()

def download_file(url,path):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'})
 with urllib.request.urlopen(req,timeout=300) as r, open(path,'wb') as f:
  shutil.copyfileobj(r,f,1024*1024)
 return {'status':getattr(r,'status',200) if 'r' in locals() else 200,'bytes':path.stat().st_size}

def find_member(names,target):
 hits=[n for n in names if n.rsplit('/',1)[-1].casefold()==target.casefold()]
 if len(hits)!=1: raise RuntimeError(f'{target}: expected one member, got {hits}')
 return hits[0]

cwns_path=download_cwns()
linked=set(); wastewater=set(); states={}
with zipfile.ZipFile(cwns_path) as z:
 fac=find_member(z.namelist(),'FACILITIES.csv'); permit=find_member(z.namelist(),'FACILITY_PERMIT.csv')
 for r in rows_from_bytes(z.read(fac)):
  cid=(r.get('CWNS_ID') or '').strip(); infra=(r.get('INFRASTRUCTURE_TYPE') or '').strip(); st=(r.get('STATE_CODE') or '').strip()
  if cid and infra.casefold()=='wastewater': wastewater.add(cid); states[cid]=st
 for r in rows_from_bytes(z.read(permit)):
  cid=(r.get('CWNS_ID') or '').strip(); source=(r.get('PERMIT_SOURCE') or '').strip(); pid=normid(r.get('PERMIT_NUMBER'))
  if cid in wastewater and source.casefold()=='npdes' and pid: linked.add(pid)

# Download ICIS-NPDES national identity/violation package transiently.
echo_path=TMP/'npdes_downloads.zip'; meta=download_file(ECHO_URL,echo_path)
with zipfile.ZipFile(echo_path) as z:
 names=z.namelist()
 permit_member=find_member(names,'ICIS_PERMITS.csv')
 facility_member=find_member(names,'ICIS_FACILITIES.csv')
 permit_ids=set(); facility_ids=set()
 for r in rows_from_bytes(z.read(permit_member)):
  pid=normid(r.get('EXTERNAL_PERMIT_NMBR'))
  if pid: permit_ids.add(pid)
 for r in rows_from_bytes(z.read(facility_member)):
  pid=normid(r.get('NPDES_ID'))
  if pid: facility_ids.add(pid)
 matched_permits=linked & permit_ids; matched_facilities=linked & facility_ids; matched_union=linked & (permit_ids|facility_ids)

 # Compliance identity probe: headers + boolean evidence of post-2022 date identities only.
 vio_targets=['NPDES_PS_VIOLATIONS.csv','NPDES_CS_VIOLATIONS.csv','NPDES_SE_VIOLATIONS.csv']
 violation_schema=[]
 post2022_identity_available=False
 for target in vio_targets:
  member=find_member(names,target); raw=z.read(member); reader=rows_from_bytes(raw); headers=reader.fieldnames or []
  date_cols=[h for h in headers if 'DATE' in h.upper()]
  type_cols=[h for h in headers if 'VIOLATION' in h.upper() and ('TYPE' in h.upper() or 'CODE' in h.upper() or 'DESC' in h.upper())]
  any_post=False
  # Date identity only; do not inspect violation magnitudes or aggregate outcome counts.
  for i,r in enumerate(reader):
   for c in date_cols:
    s=(r.get(c) or '').strip()
    if not s: continue
    for fmt in ('%m/%d/%Y','%Y-%m-%d'):
     try:
      d=datetime.strptime(s[:10],fmt).date()
      if d.year>=2023: any_post=True; break
     except ValueError: pass
    if any_post: break
   if any_post or i>=250000: break
  post2022_identity_available |= bool(any_post and type_cols)
  violation_schema.append({'member':target,'headers':headers,'date_identity_columns':date_cols,'violation_type_identity_columns':type_cols,'post_2022_date_identity_observed':any_post})

coverage=lambda n: (n/len(linked)) if linked else 0.0
manifest={
 'id':'US-WW-F01-ECHO-EXACT-JOIN','issue':114,'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,
 'cwns_official_npdes_ids':len(linked),'echo_download':{'url':ECHO_URL,'bytes':meta['bytes'],'zip_valid':True},
 'echo_identity_route':{'permit_member':'ICIS_PERMITS.csv','permit_ids':len(permit_ids),'facility_member':'ICIS_FACILITIES.csv','facility_ids':len(facility_ids)},
 'exact_match':{
  'permit_route_matches':len(matched_permits),'permit_route_coverage':coverage(len(matched_permits)),
  'facility_route_matches':len(matched_facilities),'facility_route_coverage':coverage(len(matched_facilities)),
  'union_matches':len(matched_union),'union_coverage':coverage(len(matched_union)),
  'pass_80pct_on_permit_route':coverage(len(matched_permits))>=0.80,
 },
 'compliance_identity':{'violation_tables':violation_schema,'post_2022_date_and_type_identity_available':post2022_identity_available},
 'no_fuzzy_matching':True,'raw_source_bytes_persisted':False,'incremental_monetary_cost_usd':0,
}
(OUT/'ECHO_JOIN_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'linked':len(linked),'permit_coverage':manifest['exact_match']['permit_route_coverage'],'facility_coverage':manifest['exact_match']['facility_route_coverage'],'post2022':post2022_identity_available,'echo_bytes':meta['bytes']}))

shutil.rmtree(TMP,ignore_errors=True)
