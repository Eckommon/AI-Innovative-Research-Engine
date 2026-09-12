#!/usr/bin/env python3
from __future__ import annotations

import csv, io, json, os, re, shutil, time, urllib.request, zipfile
from collections import Counter, defaultdict
from datetime import datetime, date
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-N01'; OUT.mkdir(parents=True,exist_ok=True)
TMP=Path(os.environ.get('RUNNER_TEMP','/tmp'))/'us-ww-n01'; TMP.mkdir(parents=True,exist_ok=True)
CWNS_URL='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'
ECHO_URL='https://echo.epa.gov/files/echodownloads/npdes_downloads.zip'
UA='AI-Innovative-Research-Engine/US-WW-N01 outcome-blind leakage-control probe'
EXPOSURE_CODES={'III-A','III-B','V'}
BASE_START=date(2019,1,1); BASE_END=date(2021,12,31)

def decode(b):
 for enc in ('utf-8-sig','utf-8','cp1252','latin-1'):
  try:return b.decode(enc)
  except UnicodeDecodeError:pass
 raise RuntimeError('decode')
def rows(b): return csv.DictReader(io.StringIO(decode(b)))
def normid(s): return re.sub(r'\s+','',(s or '').strip()).upper()
def member(names,target):
 hits=[n for n in names if n.rsplit('/',1)[-1].casefold()==target.casefold()]
 if len(hits)!=1: raise RuntimeError(f'{target}: {hits}')
 return hits[0]
def parse_date(s):
 s=(s or '').strip()
 if not s:return None
 for fmt in ('%m/%d/%Y','%Y-%m-%d','%m/%d/%Y %H:%M:%S'):
  try:return datetime.strptime(s[:19] if 'H' in fmt else s[:10],fmt).date()
  except ValueError:pass
 return None

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
   if driver.find_elements(By.ID,'P3_QUESTION'):found=True;break
  if not found:raise RuntimeError('CWNS dialog not found')
  Select(wait.until(EC.presence_of_element_located((By.ID,'P3_QUESTION')))).select_by_visible_text('Researcher')
  wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if (x.text or '').strip()=='Download'),None)).click()
  deadline=time.time()+90
  while time.time()<deadline:
   z=[p for p in dl.iterdir() if p.suffix.lower()=='.zip' and not p.name.endswith('.crdownload')]
   if z:return max(z,key=lambda p:p.stat().st_mtime)
   time.sleep(1)
  raise RuntimeError('CWNS ZIP not downloaded')
 finally: driver.quit()

def download(url,path):
 req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'})
 with urllib.request.urlopen(req,timeout=300) as r, open(path,'wb') as f:shutil.copyfileobj(r,f,1024*1024)
 return path.stat().st_size

cwns_path=download_cwns(); echo_path=TMP/'npdes_downloads.zip'; echo_bytes=download(ECHO_URL,echo_path)

# CWNS identity-only extraction. Never access BASE_AMOUNT/OFFICIAL_AMOUNT.
facilities={}; permits=defaultdict(set); categories=defaultdict(set); reasons=defaultdict(set); reason_counts=Counter()
with zipfile.ZipFile(cwns_path) as z:
 names=z.namelist()
 for r in rows(z.read(member(names,'FACILITIES.csv'))):
  cid=(r.get('CWNS_ID') or '').strip(); infra=(r.get('INFRASTRUCTURE_TYPE') or '').strip(); st=(r.get('STATE_CODE') or '').strip()
  if cid and infra.casefold()=='wastewater':facilities[cid]={'state':st}
 for r in rows(z.read(member(names,'FACILITY_PERMIT.csv'))):
  cid=(r.get('CWNS_ID') or '').strip(); src=(r.get('PERMIT_SOURCE') or '').strip(); pid=normid(r.get('PERMIT_NUMBER'))
  if cid in facilities and src.casefold()=='npdes' and pid:permits[cid].add(pid)
 for r in rows(z.read(member(names,'NEEDS_COST_BY_CATEGORY.csv'))):
  cid=(r.get('CWNS_ID') or '').strip(); cat=(r.get('NEEDS_CATEGORY') or '').strip()
  if cid in facilities and cat:categories[cid].add(cat)
 for r in rows(z.read(member(names,'REASON_FOR_NEEDS.csv'))):
  cid=(r.get('CWNS_ID') or '').strip(); reason=(r.get('NEED_REASON') or '').strip()
  if cid in facilities and reason:
   reasons[cid].add(reason); reason_counts[reason]+=1

with zipfile.ZipFile(echo_path) as z:
 names=z.namelist()
 icis_ids=set()
 for r in rows(z.read(member(names,'ICIS_PERMITS.csv'))):
  pid=normid(r.get('EXTERNAL_PERMIT_NMBR'))
  if pid:icis_ids.add(pid)

 # All linked permits must travel together; require every official linked permit to exist in ICIS_PERMITS.
 exact_facilities={cid for cid,ps in permits.items() if ps and ps.issubset(icis_ids)}
 documented_need={cid for cid in exact_facilities if categories.get(cid)}
 exposed={cid for cid in documented_need if categories[cid] & EXPOSURE_CODES}
 comparator={cid for cid in documented_need if not (categories[cid] & EXPOSURE_CODES)}

 # Baseline only: 2019-2021. Future 2023-2025 rows are never counted or persisted.
 baseline_violation_permits=set(); baseline_schema=[]
 for target in ('NPDES_PS_VIOLATIONS.csv','NPDES_CS_VIOLATIONS.csv','NPDES_SE_VIOLATIONS.csv'):
  raw=z.read(member(names,target)); reader=rows(raw); headers=reader.fieldnames or []
  date_cols=[h for h in headers if 'DATE' in h.upper()]
  type_cols=[h for h in headers if 'VIOLATION' in h.upper() and ('TYPE' in h.upper() or 'CODE' in h.upper() or 'DESC' in h.upper())]
  baseline_date_identity_observed=False
  for r in reader:
   pid=normid(r.get('NPDES_ID'))
   if pid not in icis_ids:continue
   in_base=False
   for c in date_cols:
    d=parse_date(r.get(c))
    if d and BASE_START<=d<=BASE_END:
     in_base=True;baseline_date_identity_observed=True;break
   if in_base:baseline_violation_permits.add(pid)
  baseline_schema.append({'table':target,'date_identity_columns':date_cols,'violation_type_identity_columns':type_cols,'baseline_2019_2021_date_identity_observed':baseline_date_identity_observed})

baseline_clean={cid for cid in exact_facilities if all(pid not in baseline_violation_permits for pid in permits[cid])}
# This is baseline identity support/cardinality only; no future outcomes are inspected.
exposed_clean=exposed & baseline_clean; comparator_clean=comparator & baseline_clean
reason_catalog=sorted(reason_counts)
# Outcome-blind semantic marker candidates only; terminal leakage policy is adjudicated after inspecting exact labels.
compliance_like=[r for r in reason_catalog if re.search(r'permit|compliance|regulat|enforcement|violation|consent|order|standard',r,re.I)]

manifest={
 'id':'US-WW-N01-DESIGN-MANIFEST','issue':116,
 'boundary':{'future_2023_2025_outcome_counts_read_or_persisted':False,'future_outcome_rates_computed':False,'relationship_computed':False,'need_dollar_magnitudes_read':False},
 'frozen_windows':{'baseline':['2019-01-01','2021-12-31'],'future_identity_only':['2023-01-01','2025-12-31']},
 'population':{
  'wastewater_facilities':len(facilities),'official_npdes_linked_facilities':len(permits),'all_linked_permits_exact_in_icis_facilities':len(exact_facilities),
  'exact_link_support_fraction_of_linked':len(exact_facilities)/len(permits) if permits else 0.0,
 },
 'exposure':{
  'codes':sorted(EXPOSURE_CODES),'documented_need_exact_linked_facilities':len(documented_need),'exposed_facilities':len(exposed),'comparator_facilities':len(comparator),
  'pass_500_each':len(exposed)>=500 and len(comparator)>=500,
 },
 'reason_for_needs':{'labels':reason_catalog,'structural_row_counts_by_label':dict(sorted(reason_counts.items())),'compliance_like_label_candidates':compliance_like},
 'baseline_identity':{
  'violation_tables':baseline_schema,'baseline_violation_permit_identity_count':len(baseline_violation_permits),
  'baseline_clean_exact_linked_facilities':len(baseline_clean),'baseline_clean_exposed_facilities':len(exposed_clean),'baseline_clean_comparator_facilities':len(comparator_clean),
  'pass_80pct_identity_route':len(exact_facilities)/len(permits)>=0.80 if permits else False,
 },
 'future_window':{'identity_schema_available_from_F01':True,'outcome_counts_intentionally_not_computed':True},
 'raw_source_bytes_persisted':False,'echo_core_bytes_transient':echo_bytes,'incremental_monetary_cost_usd':0,
}
(OUT/'DESIGN_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'exact_facilities':len(exact_facilities),'exposed':len(exposed),'comparator':len(comparator),'baseline_clean':len(baseline_clean),'clean_exposed':len(exposed_clean),'clean_comparator':len(comparator_clean),'reason_labels':reason_catalog,'compliance_like':compliance_like,'future_outcomes_opened':False}))
shutil.rmtree(TMP,ignore_errors=True)
