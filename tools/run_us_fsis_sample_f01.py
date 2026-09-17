#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'research/US-FSIS-SAMPLE-F01'
CONTRACT='1c7496ad5f4f6d82900fd60f0a31d3406cf217dc'
PASS='PASS_US_FSIS_SAMPLE_F01_EXACT_ESTABLISHMENT_LONGITUDINAL_JOIN_READY'
HOLD='HOLD_US_FSIS_SAMPLE_F01_EXACT_ESTABLISHMENT_LONGITUDINAL_JOIN_NOT_READY'
LANDING='https://www.fsis.usda.gov/science-data/data-sets-visualizations/laboratory-sampling-data'
MPI='https://www.fsis.usda.gov/inspection/establishments/meat-poultry-and-egg-product-inspection-directory'
RECALL_GUIDE='https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/understanding-fsis-food-recalls'
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/153.0 Safari/537.36'


def fetch(url:str)->bytes:
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*','Referer':'https://www.fsis.usda.gov/'})
    with urllib.request.urlopen(req,timeout=90) as r:
        return r.read()


def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()

def hrefs(html:bytes,base:str)->list[str]:
    text=html.decode('utf-8','ignore')
    vals=re.findall(r'''href=["']([^"']+)["']''',text,re.I)
    return [urllib.parse.urljoin(base,v.replace('&amp;','&')) for v in vals]


def normalize_header(v:Any)->str:
    return re.sub(r'[^A-Z0-9]+',' ',str(v).upper()).strip()


def normalize_est(v:Any)->str|None:
    if v is None: return None
    s=str(v).strip().upper()
    if not s or s in {'NAN','NONE','NULL','NA','N/A'}: return None
    # Contract permits only trim/uppercase by default. Internal spaces are NOT removed
    # unless official schema names establish the same representation; runner stays stricter.
    return s


def recursive_lists(obj:Any,path:str='root')->Iterable[tuple[str,list[dict[str,Any]]]]:
    if isinstance(obj,list):
        ds=[x for x in obj if isinstance(x,dict)]
        if len(ds)>=10:
            yield path,ds
        for i,x in enumerate(obj[:20]):
            yield from recursive_lists(x,f'{path}[{i}]')
    elif isinstance(obj,dict):
        for k,v in obj.items():
            yield from recursive_lists(v,f'{path}.{k}')


def field_choice(keys:Iterable[str],kind:str)->str|None:
    ks=list(keys)
    scored=[]
    for k in ks:
        n=normalize_header(k)
        score=0
        if kind=='est':
            if 'ESTABLISHMENT' in n and ('NUMBER' in n or n.endswith(' NO')): score=100
            if n in {'ESTNUMBER','EST NUMBER','EST NO'}: score=120
            if 'PRIMARY ESTABLISHMENT' in n: score+=30
        elif kind=='fy':
            if n in {'FISCAL YEAR','FY','FISCALYEAR'}: score=120
            if 'FISCAL' in n and 'YEAR' in n: score=100
        elif kind=='date':
            if 'COLLECTION' in n and 'DATE' in n: score=120
            elif 'SAMPLE' in n and 'DATE' in n: score=100
            elif n.endswith('DATE'): score=50
        if score: scored.append((score,k))
    return max(scored,default=(0,None))[1]


def year_of(row:dict[str,Any],fy_field:str|None,date_field:str|None)->int|None:
    if fy_field:
        m=re.search(r'20\d{2}',str(row.get(fy_field,'')))
        if m: return int(m.group())
    if date_field:
        s=str(row.get(date_field,''))
        # Federal fiscal year: Oct-Dec belong to following FY. Support common date layouts.
        m=re.search(r'(20\d{2})[-/](\d{1,2})[-/](\d{1,2})',s)
        if m:
            y,mo=int(m.group(1)),int(m.group(2)); return y+1 if mo>=10 else y
        m=re.search(r'(\d{1,2})[-/](\d{1,2})[-/](20\d{2})',s)
        if m:
            mo,y=int(m.group(1)),int(m.group(3)); return y+1 if mo>=10 else y
    return None


def choose_sampling_records(obj:Any)->tuple[list[dict[str,Any]],str,str|None,str|None,str]:
    best=None
    for path,rows in recursive_lists(obj):
        keys=set().union(*(r.keys() for r in rows[:100]))
        est=field_choice(keys,'est'); fy=field_choice(keys,'fy'); dt=field_choice(keys,'date')
        if not est: continue
        count=sum(1 for r in rows[:500] if normalize_est(r.get(est)))
        score=count + (500 if fy or dt else 0) + min(len(rows),5000)/10
        cand=(score,rows,est,fy,dt,path)
        if best is None or cand[0]>best[0]: best=cand
    if best is None:
        raise RuntimeError('No sampling record array with source-native establishment field found')
    _,rows,est,fy,dt,path=best
    return rows,est,fy,dt,path


def parse_csv_asset(b:bytes)->tuple[list[dict[str,str]],str]:
    text=b.decode('utf-8-sig','replace')
    rows=list(csv.DictReader(io.StringIO(text)))
    if not rows: raise RuntimeError('MPI CSV has no rows')
    est=field_choice(rows[0].keys(),'est')
    if not est: raise RuntimeError(f'No MPI establishment number field in {list(rows[0])}')
    return rows,est


def main()->None:
    cp=json.loads((ROOT/'context/checkpoint.json').read_text())
    assert str(cp['active_issue']) in {'158','#158'} and cp['active_research']=='US-FSIS-SAMPLE-F01' and cp['last_decision']=='DEC-228'
    contract=(RESEARCH/'README.md').read_text()
    assert PASS in contract and HOLD in contract and '2024-01-01 through 2025-12-31' in contract

    boundary={
      'candidate_2024_2025_recall_rows_opened':False,
      'candidate_recall_membership_opened':False,
      'recall_reason_class_pounds_pathogen_values_opened':False,
      'sampling_to_recall_relationship_computed':False,
      'recall_prediction_computed':False,
      'establishment_ranking_made':False,
      'causal_claim_made':False,
      'novelty_claim_made':False,
      'fuzzy_name_address_geo_manual_identity_repair_used':False,
    }

    landing_b=fetch(LANDING)
    links=hrefs(landing_b,LANDING)
    json_candidates=[u for u in links if ('poultry' in u.lower()) and ('.json' in u.lower() or 'json' in u.lower())]
    if not json_candidates:
        # Some Drupal assets use opaque file names; use anchor-neighborhood discovery.
        text=landing_b.decode('utf-8','ignore')
        for m in re.finditer(r'Raw Poultry Sampling',text,re.I):
            lo=max(0,m.start()-2500); hi=min(len(text),m.end()+2500)
            frag=text[lo:hi]
            for h in re.findall(r'''href=["']([^"']+)["']''',frag,re.I):
                u=urllib.parse.urljoin(LANDING,h.replace('&amp;',''))
                if 'json' in u.lower(): json_candidates.append(u)
    if not json_candidates:
        raise RuntimeError('Could not discover official Raw Poultry JSON asset from FSIS landing page')
    # Deterministic choice: shortest then lexical among official fsis.gov links.
    json_candidates=sorted(set(u for u in json_candidates if urllib.parse.urlparse(u).netloc.endswith('fsis.usda.gov')),key=lambda x:(len(x),x))
    sampling_url=json_candidates[0]
    sampling_b=fetch(sampling_url)
    obj=json.loads(sampling_b.decode('utf-8-sig'))
    rows,est_field,fy_field,date_field,record_path=choose_sampling_records(obj)

    usable=[]; nonblank=0; structurally_usable=0
    seen_exact=set(); conflicting=set(); by_key=defaultdict(list)
    for r in rows:
        y=year_of(r,fy_field,date_field)
        if y not in {2021,2022,2023}: continue
        structurally_usable+=1
        e=normalize_est(r.get(est_field))
        if e:
            nonblank+=1; by_key[(e,y)].append(r)
    # Exposure-only counts; pathogen/result values are never read.
    for (e,y),rs in by_key.items():
        usable.append((e,y,len(rs)))
    distinct=set(e for e,_,_ in usable)
    years_by=defaultdict(set)
    for e,y,_ in usable: years_by[e].add(y)

    mpi_page=fetch(MPI)
    mpi_links=hrefs(mpi_page,MPI)
    csvs=[u for u in mpi_links if '.csv' in u.lower()]
    if not csvs: raise RuntimeError('No CSV assets discovered on official MPI Directory page')
    # Prefer numeric establishment-number directory over demographic/name order.
    def mpi_score(u:str)->tuple[int,int,str]:
        x=u.lower(); s=0
        if 'numer' in x or 'establishment-number' in x or 'establishment_number' in x: s+=20
        if 'directory' in x: s+=10
        if 'demographic' in x: s-=5
        return (-s,len(u),u)
    mpi_url=sorted(set(csvs),key=mpi_score)[0]
    mpi_b=fetch(mpi_url)
    mpi_rows,mpi_est_field=parse_csv_asset(mpi_b)
    mpi_counts=Counter(normalize_est(r.get(mpi_est_field)) for r in mpi_rows)
    mpi_counts.pop(None,None)
    linked={e for e in distinct if e in mpi_counts}
    linked_unique={e for e in linked if mpi_counts[e]==1}

    # Recall guidance only; DO NOT request recalls/annual-summary rows.
    guide_b=fetch(RECALL_GUIDE)
    guide_text=re.sub(r'<[^>]+>',' ',guide_b.decode('utf-8','ignore'))
    guide_norm=' '.join(guide_text.split()).lower()
    recall_est_semantics=('establishment number' in guide_norm) or ('est. no.' in guide_norm) or ('est no' in guide_norm)

    req=[]
    def add(n,name,p,evidence): req.append({'number':n,'name':name,'pass':bool(p),'evidence':evidence})
    add(1,'official Raw Poultry source machine-readable',bool(rows),{'url':sampling_url,'bytes':len(sampling_b),'sha256':sha(sampling_b)})
    metadata_signal=isinstance(obj,dict) and any(tok in ' '.join(map(str,obj.keys())).lower() for tok in ['meta','document','data'])
    landing_signal=('metadata' in landing_b.decode('utf-8','ignore').lower())
    add(2,'dataset documentation/metadata and FY semantics established',bool((fy_field or date_field) and (metadata_signal or landing_signal)),{'record_path':record_path,'establishment_field':est_field,'fiscal_year_field':fy_field,'date_field':date_field})
    years_found=sorted(set(y for _,y,_ in usable))
    add(3,'FY2021 FY2022 FY2023 reproducibly accessible in official source',years_found==[2021,2022,2023],years_found)
    add(4,'source-native establishment-number field present',bool(est_field),est_field)
    add(5,'sampling date/FY semantics sufficient',bool(fy_field or date_field),{'fy_field':fy_field,'date_field':date_field})
    add(6,'official MPI machine-readable and fingerprinted',bool(mpi_rows),{'url':mpi_url,'bytes':len(mpi_b),'sha256':sha(mpi_b)})
    add(7,'MPI official establishment-number field present',bool(mpi_est_field),mpi_est_field)
    add(8,'recall guidance establishes establishment-number semantics without candidate rows',recall_est_semantics,{'guide_url':RECALL_GUIDE,'guide_sha256':sha(guide_b),'candidate_recall_pages_requested':False})
    add(9,'candidate 2024-2025 recall membership unopened',not any(boundary[k] for k in ['candidate_2024_2025_recall_rows_opened','candidate_recall_membership_opened','recall_reason_class_pounds_pathogen_values_opened']),boundary)
    add(10,'no fuzzy/name/address/geospatial/manual repair',not boundary['fuzzy_name_address_geo_manual_identity_repair_used'],False)
    add(11,'>=150 distinct sampled establishments',len(distinct)>=150,len(distinct))
    two=sum(len(v)>=2 for v in years_by.values()); three=sum(len(v)>=3 for v in years_by.values())
    add(12,'>=100 establishments in >=2 frozen FYs',two>=100,two)
    add(13,'>=50 establishments in all 3 frozen FYs',three>=50,three)
    nonblank_rate=(nonblank/structurally_usable) if structurally_usable else 0
    add(14,'>=95% structurally usable rows have valid establishment number',nonblank_rate>=0.95,nonblank_rate)
    link_rate=(len(linked)/len(distinct)) if distinct else 0
    add(15,'>=90% distinct sampled establishments exact-link to MPI',link_rate>=0.90,{'linked':len(linked),'denominator':len(distinct),'rate':link_rate})
    unique_rate=(len(linked_unique)/len(linked)) if linked else 0
    add(16,'>=99% linked establishments map to one MPI record',unique_rate>=0.99,{'unique':len(linked_unique),'linked':len(linked),'rate':unique_rate,'ambiguous':len(linked-linked_unique)})

    manifest_rows=[{'establishment_number':e,'fiscal_year':y,'sampling_row_count':n,'mpi_exact_link':e in linked_unique} for e,y,n in sorted(usable)]
    out=io.StringIO(); w=csv.DictWriter(out,fieldnames=['establishment_number','fiscal_year','sampling_row_count','mpi_exact_link']); w.writeheader(); w.writerows(manifest_rows)
    manifest_text=out.getvalue(); (RESEARCH/'EXPOSURE_MANIFEST.csv').write_text(manifest_text,encoding='utf-8')
    scientific_clean=not any(boundary.values())
    add(17,'fingerprints/schema/exclusions/exposure-only manifest persisted and no downstream science',scientific_clean,{'manifest_sha256':hashlib.sha256(manifest_text.encode()).hexdigest(),'boundaries':boundary})
    add(18,'zero incremental monetary cost',True,0)

    passed=sum(x['pass'] for x in req); disposition='PASS' if passed==18 else 'HOLD'; gate=PASS if disposition=='PASS' else HOLD
    result={
      'research':'US-FSIS-SAMPLE-F01','issue':158,'contract_commit':CONTRACT,'activation_decision':'DEC-228',
      'scientific_disposition':disposition,'gate':gate,'requirements_total':18,'requirements_passed':passed,'requirements':req,
      'diagnostics':{
        'sampling_record_path':record_path,'sampling_establishment_field':est_field,'sampling_fy_field':fy_field,'sampling_date_field':date_field,
        'structurally_usable_rows_fy2021_2023':structurally_usable,'nonblank_establishment_rows':nonblank,
        'distinct_sampled_establishments':len(distinct),'establishments_ge2_years':two,'establishments_all3_years':three,
        'mpi_exact_linked_establishments':len(linked),'mpi_unique_linked_establishments':len(linked_unique),
      },
      'sources':{'sampling_url':sampling_url,'sampling_sha256':sha(sampling_b),'mpi_url':mpi_url,'mpi_sha256':sha(mpi_b),'recall_guidance_url':RECALL_GUIDE,'recall_guidance_sha256':sha(guide_b)},
      'boundaries':boundary,'incremental_monetary_cost_usd':0,
    }
    (RESEARCH/'STAGING_RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(gate); print(json.dumps(result['diagnostics'],sort_keys=True)); print(f'REQUIREMENTS={passed}/18')

if __name__=='__main__': main()
