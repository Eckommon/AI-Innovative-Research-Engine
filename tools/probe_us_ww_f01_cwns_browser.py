#!/usr/bin/env python3
from __future__ import annotations

import csv, hashlib, io, json, os, time, zipfile
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'/'US-WW-F01'; OUT.mkdir(parents=True,exist_ok=True)
DL=Path(os.environ.get('RUNNER_TEMP','/tmp'))/'cwns-download'; DL.mkdir(parents=True,exist_ok=True)
URL='https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download'

opts=webdriver.ChromeOptions()
opts.add_argument('--headless=new'); opts.add_argument('--no-sandbox'); opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--window-size=1440,1200')
opts.add_experimental_option('prefs',{'download.default_directory':str(DL),'download.prompt_for_download':False,'download.directory_upgrade':True,'safebrowsing.enabled':True})

driver=webdriver.Chrome(options=opts)
try:
    driver.get(URL)
    wait=WebDriverWait(driver,30)
    btn=wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if 'p3_type=NA_CSV' in (x.get_attribute('onclick') or '')),None))
    btn.click()
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR,'iframe'))>0)
    frames=driver.find_elements(By.CSS_SELECTOR,'iframe')
    target=None
    for fr in frames:
        try:
            driver.switch_to.default_content(); driver.switch_to.frame(fr)
            if driver.find_elements(By.ID,'P3_QUESTION'):
                target=fr; break
        except Exception:
            continue
    if target is None:
        raise RuntimeError('CWNS download dialog iframe with P3_QUESTION not found')
    select=Select(wait.until(EC.presence_of_element_located((By.ID,'P3_QUESTION'))))
    # This is a usage-purpose category, not personal identity; current use is research.
    select.select_by_visible_text('Researcher')
    download=wait.until(lambda d: next((x for x in d.find_elements(By.TAG_NAME,'button') if (x.text or '').strip()=='Download'),None))
    download.click()
    deadline=time.time()+90
    chosen=None
    while time.time()<deadline:
        files=[p for p in DL.iterdir() if p.is_file() and not p.name.endswith(('.crdownload','.tmp'))]
        zips=[p for p in files if p.suffix.lower()=='.zip']
        if zips:
            chosen=max(zips,key=lambda p:p.stat().st_mtime); break
        time.sleep(1)
    if chosen is None:
        raise RuntimeError('No completed ZIP download observed')
    data=chosen.read_bytes()
    members=[]
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for name in z.namelist():
            if name.endswith('/'):
                continue
            info=z.getinfo(name)
            rec={'name':name,'uncompressed_bytes':info.file_size}
            if name.lower().endswith('.csv'):
                raw=z.read(name)
                text=None
                for enc in ('utf-8-sig','utf-8','cp1252','latin-1'):
                    try: text=raw.decode(enc); break
                    except UnicodeDecodeError: pass
                if text is not None:
                    reader=csv.reader(io.StringIO(text))
                    try: rec['headers']=next(reader)
                    except StopIteration: rec['headers']=[]
                    rec['row_count']=sum(1 for _ in reader)
            members.append(rec)
    manifest={
      'id':'US-WW-F01-CWNS-NATIONAL-BROWSER-PROBE','issue':114,
      'relationship_computed':False,'candidate_outcome_magnitudes_opened':False,
      'source_url':URL,'usage_category_submitted':'Researcher',
      'download':{'filename':chosen.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'zip_valid':True},
      'members':members,'member_count':len(members),
      'raw_source_bytes_persisted':False,'incremental_monetary_cost_usd':0,
    }
    (OUT/'CWNS_NATIONAL_STRUCTURE.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'zip':chosen.name,'bytes':len(data),'members':len(members)}))
finally:
    driver.quit()
    for p in DL.iterdir():
        try: p.unlink()
        except Exception: pass
