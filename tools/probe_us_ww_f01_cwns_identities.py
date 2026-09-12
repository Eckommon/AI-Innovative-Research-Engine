#!/usr/bin/env python3
from __future__ import annotations

import csv, io, json, os, time, zipfile
from collections import Counter, defaultdict
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
DL=Path(os.environ.get('RUNNER_TEMP','/tmp'))/'cwns-id-download'; DL.mkdir(parents=True,exist_ok=True)
URL='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'

def decode(b):
 for enc in ('utf-8-sig','utf-8','cp1252','latin-1'):
  try:return b.decode(enc)
  except UnicodeDecodeError:pass
 raise RuntimeError('decode')

def rows(z,name): return csv.DictReader(io.StringIO(decode(z.read(name))))

opts=webdriver.ChromeOptions(); opts.add_argument('--headless=new'); opts.add_argument('--no-sandbox'); opts.add_argument('--disable-dev-shm-usage'); opts.add_argument('--window-size=1440,1200')
opts.add_experimental_option('prefs',{'download.default_directory':str(DL),'download.prompt_for_download':False,'download.directory_upgrade':True,'safebrowsing.enabled':True})
driver=webdriver.Chrome(options=opts)
try:
 driver.get(URL); wait=WebDriverWait(driver,30)
 btn=wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if 'p3_type=NA_CSV' in (x.get_attribute('onclick') or '')),None)); btn.click()
 wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,'iframe'))>0)
 found=False
 for fr in driver.find_elements(By.CSS_SELECTOR,'iframe'):
  driver.switch_to.default_content(); driver.switch_to.frame(fr)
  if driver.find_elements(By.ID,'P3_QUESTION'): found=True; break
 if not found: raise RuntimeError('dialog not found')
 Select(wait.until(EC.presence_of_element_located((By.ID,'P3_QUESTION')))).select_by_visible_text('Researcher')
 wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if (x.text or '').strip()=='Download'),None)).click()
 deadline=time.time()+90; chosen=None
 while time.time()<deadline:
  zips=[p for p in DL.iterdir() if p.is_file() and p.suffix.lower()=='.zip' and not p.name.endswith('.crdownload')]
  if zips: chosen=max(zips,key=lambda p:p.stat().st_mtime); break
  time.sleep(1)
 if chosen is None: raise RuntimeError('zip not downloaded')
 data=chosen.read_bytes()
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  names=set(z.namelist()); required={'FACILITIES.csv','FACILITY_TYPES.csv','FACILITY_PERMIT.csv','REF_FACILITY_TYPES.csv','REF_NEEDS_CATEGORIES.csv','NEEDS_COST_BY_CATEGORY.csv'}
  missing=required-names
  if missing: raise RuntimeError(f'missing tables: {sorted(missing)}')
  facilities={}; infra_counts=Counter()
  for r in rows(z,'FACILITIES.csv'):
   cid=(r.get('CWNS_ID') or '').strip(); st=(r.get('STATE_CODE') or '').strip(); infra=(r.get('INFRASTRUCTURE_TYPE') or '').strip()
   if cid: facilities[cid]={'state':st,'infrastructure_type':infra}; infra_counts[infra]+=1
  type_catalog=Counter(); facility_types=defaultdict(set)
  for r in rows(z,'FACILITY_TYPES.csv'):
   cid=(r.get('CWNS_ID') or '').strip(); typ=(r.get('FACILITY_TYPE') or '').strip()
   if cid and typ: facility_types[cid].add(typ); type_catalog[typ]+=1
  ref_types=[{'facility_type':(r.get('FACILITY_TYPE') or '').strip(),'infrastructure_type':(r.get('INFRASTRUCTURE_TYPE') or '').strip()} for r in rows(z,'REF_FACILITY_TYPES.csv')]
  permit_source_counts=Counter(); permit_type_counts=Counter(); npdes_linked=defaultdict(set); all_linked=defaultdict(set)
  for r in rows(z,'FACILITY_PERMIT.csv'):
   cid=(r.get('CWNS_ID') or '').strip(); permit=(r.get('PERMIT_NUMBER') or '').strip(); source=(r.get('PERMIT_SOURCE') or '').strip(); ptype=(r.get('PERMIT_TYPE') or '').strip()
   if source: permit_source_counts[source]+=1
   if ptype: permit_type_counts[ptype]+=1
   if cid and permit:
    all_linked[cid].add(permit)
    if source.casefold()=='npdes': npdes_linked[cid].add(permit)
  wastewater={cid for cid,v in facilities.items() if v['infrastructure_type'].casefold()=='wastewater'}
  npdes_wastewater={cid for cid in wastewater if npdes_linked.get(cid)}
  states=Counter(facilities[cid]['state'] for cid in npdes_wastewater if facilities[cid]['state'])
  linked_npdes_ids=sorted({p for cid in npdes_wastewater for p in npdes_linked[cid]})
  categories=[{'needs_category':(r.get('NEEDS_CATEGORY') or '').strip(),'category_name':(r.get('CATEGORY_NAME') or '').strip(),'valid_for_sso_flag':(r.get('VALID_FOR_SSO_FLAG') or '').strip()} for r in rows(z,'REF_NEEDS_CATEGORIES.csv')]
  used_categories=Counter()
  for r in rows(z,'NEEDS_COST_BY_CATEGORY.csv'):
   cat=(r.get('NEEDS_CATEGORY') or '').strip()
   if cat: used_categories[cat]+=1
 manifest={
  'id':'US-WW-F01-CWNS-IDENTITY-CARDINALITY','issue':114,'probe_revision':2,
  'technical_correction':'official NPDES linkage cardinality now requires PERMIT_SOURCE == NPDES',
  'relationship_computed':False,'need_dollar_magnitudes_read':False,'candidate_outcome_magnitudes_opened':False,
  'facility_count':len(facilities),'infrastructure_type_counts':dict(sorted(infra_counts.items())),'facility_type_catalog':dict(sorted(type_catalog.items())),'reference_facility_types':ref_types,
  'permit_source_counts':dict(sorted(permit_source_counts.items())),'permit_type_counts':dict(sorted(permit_type_counts.items())),
  'wastewater_facility_identities':len(wastewater),'wastewater_with_any_permit_linkage':sum(1 for cid in wastewater if all_linked.get(cid)),
  'wastewater_with_official_npdes_linkage':len(npdes_wastewater),'npdes_linked_state_count':len(states),'npdes_linked_states':dict(sorted(states.items())),'distinct_official_npdes_ids':len(linked_npdes_ids),
  'official_npdes_ids_sha256_only':__import__('hashlib').sha256('\n'.join(linked_npdes_ids).encode()).hexdigest(),
  'need_category_catalog':categories,'need_category_structural_usage_counts':dict(sorted(used_categories.items())),
  'pass_threshold_3000_facilities':len(npdes_wastewater)>=3000,'pass_threshold_30_states':len(states)>=30,
  'raw_source_bytes_persisted':False,'incremental_monetary_cost_usd':0,
 }
 (OUT/'CWNS_IDENTITY_MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps({'wastewater':len(wastewater),'npdes_linked':len(npdes_wastewater),'states':len(states),'npdes_ids':len(linked_npdes_ids),'permit_sources':dict(permit_source_counts)}))
finally:
 driver.quit()
 for p in DL.iterdir():
  try:p.unlink()
  except Exception:pass
