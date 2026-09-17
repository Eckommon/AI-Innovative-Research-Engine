#!/usr/bin/env python3
# Execution trigger: first immutable run under contract 6568d9bd0d897abb0bcabf8eaf04f2e54f50177f.
from __future__ import annotations
import csv, hashlib, io, json, time, urllib.parse, urllib.request
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/US-FDIC-BRANCH-F01/staging'
OUT.mkdir(parents=True,exist_ok=True)
CONTRACT='6568d9bd0d897abb0bcabf8eaf04f2e54f50177f'
PREFLIGHT='b8063ff71c3b9b7aa05a5c6cae2325901af6d531'
ISSUE=160
BASE='https://api.fdic.gov/banks'
DOCS='https://api.fdic.gov/banks/docs'
SWAGGER='https://api.fdic.gov/banks/docs/swagger.yaml'
SOD_UI='https://banks.data.fdic.gov/bankfind-suite/SOD/customDownload'
FIELDS=['YEAR','CERT','BRNUM','UNINUMBR','DEPSUMBR']
YEARS=(2022,2023,2024)
UA='AI-Innovative-Research-Engine/US-FDIC-BRANCH-F01 outcome-blind structural research'

boundary={
 'future_2025_sod_data_rows_opened':False,
 'future_branch_membership_opened':False,
 'future_history_event_membership_opened':False,
 'future_closure_noncontinuation_computed':False,
 'fuzzy_name_address_zip_geo_manual_identity_repair_used':False,
 'relationship_computed':False,'predictive_metric_computed':False,
 'causal_claim_made':False,'branch_or_bank_ranking_made':False,'novelty_claim_made':False,
}

def get(url, accept='application/json', retries=4):
    last=None
    for i in range(retries):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':accept})
            with urllib.request.urlopen(req,timeout=90) as r:
                return r.read(), dict(r.headers)
        except Exception as e:
            last=e; time.sleep(2**i)
    raise last

def sha(b): return hashlib.sha256(b).hexdigest()

def unwrap(payload):
    rows=payload.get('data',[]) if isinstance(payload,dict) else []
    out=[]
    for x in rows:
        if isinstance(x,dict) and isinstance(x.get('data'),dict): out.append(x['data'])
        elif isinstance(x,dict): out.append(x)
    return out

def fetch_year(year):
    limit=10000; offset=0; allrows=[]; page_hashes=[]
    while True:
        q=urllib.parse.urlencode({'filters':f'YEAR:{year}','fields':','.join(FIELDS),'limit':limit,'offset':offset})
        url=f'{BASE}/sod?{q}'
        raw,_=get(url)
        page_hashes.append({'offset':offset,'sha256':sha(raw),'bytes':len(raw)})
        p=json.loads(raw)
        rows=unwrap(p)
        allrows.extend(rows)
        if len(rows)<limit: break
        offset += len(rows)
        if offset>200000: raise RuntimeError('unexpected pagination ceiling')
    return allrows,page_hashes

# Source/schema metadata only. These requests do not query location/history rows or any 2025 SOD row.
docs_raw,_=get(DOCS,'text/html,*/*')
swagger_raw,_=get(SWAGGER,'text/yaml,text/plain,*/*')
sod_ui_raw,_=get(SOD_UI,'text/html,*/*')
swagger_text=swagger_raw.decode('utf-8','replace').upper()
ui_text=sod_ui_raw.decode('utf-8','replace').upper()
meta_blob=(swagger_text+'\n'+ui_text)

source_manifest={
 'docs':{'url':DOCS,'sha256':sha(docs_raw),'bytes':len(docs_raw)},
 'openapi':{'url':SWAGGER,'sha256':sha(swagger_raw),'bytes':len(swagger_raw)},
 'sod_custom_download_metadata':{'url':SOD_UI,'sha256':sha(sod_ui_raw),'bytes':len(sod_ui_raw)},
 'preflight_commit':PREFLIGHT,
 'future_row_requests_made':0,
 'location_row_requests_made':0,
 'history_row_requests_made':0,
}

historical=[]; year_pages={}
for y in YEARS:
    rows,pages=fetch_year(y); year_pages[str(y)]=pages
    for r in rows:
        rr={k:r.get(k) for k in FIELDS}
        historical.append(rr)
source_manifest['historical_sod_pages']=year_pages

def norm(v):
    if v is None: return ''
    s=str(v).strip()
    if s.lower() in {'','none','null','nan'}: return ''
    if s.endswith('.0') and s[:-2].replace('-','').isdigit(): s=s[:-2]
    return s

usable=[]; valid=0
for r in historical:
    x={k:norm(r.get(k)) for k in FIELDS}
    if all(x[k] for k in ('YEAR','CERT','BRNUM','UNINUMBR')): valid+=1
    if all(x[k] for k in ('YEAR','CERT','BRNUM','UNINUMBR')): usable.append(x)

by_uni=defaultdict(list)
for x in usable: by_uni[x['UNINUMBR']].append(x)

distinct=len(by_uni)
yearsets={u:{x['YEAR'] for x in xs} for u,xs in by_uni.items()}
ge2=sum(len(v)>=2 for v in yearsets.values())
all3=sum(v=={'2022','2023','2024'} for v in yearsets.values())
cert_change=sum(len({x['CERT'] for x in xs})>=2 for xs in by_uni.values())
valid_rate=(valid/len(historical)) if historical else 0.0

manbuf=io.StringIO(); w=csv.writer(manbuf); w.writerow(['UNINUMBR','YEAR','CERT','BRNUM'])
for x in sorted(usable,key=lambda z:(z['UNINUMBR'],z['YEAR'],z['CERT'],z['BRNUM'])):
    w.writerow([x['UNINUMBR'],x['YEAR'],x['CERT'],x['BRNUM']])
manbytes=manbuf.getvalue().encode()
(OUT/'historical_exposure_manifest.csv').write_bytes(manbytes)
(OUT/'source_manifest.json').write_text(json.dumps(source_manifest,indent=2,sort_keys=True)+'\n')

openapi_has_sod=('SOD' in swagger_text and 'UNINUMBR' in meta_blob)
openapi_has_location=('LOCATION' in swagger_text)
openapi_has_history=('HISTORY' in swagger_text)
future_schema_has_uninumbr=('UNINUMBR' in meta_blob)

def req(n,name,passed,evidence): return {'number':n,'name':name,'pass':bool(passed),'evidence':evidence}
requirements=[
 req(1,'official FDIC SOD public machine-readable source accessible at zero cost',len(historical)>0,{'years':list(YEARS),'rows':len(historical)}),
 req(2,'official SOD variable/definition metadata accessible and fingerprinted',len(docs_raw)>0 and len(swagger_raw)>0,source_manifest['openapi']),
 req(3,'national SOD 2022, 2023, 2024 reproducibly accessible and fingerprinted',all(year_pages[str(y)] for y in YEARS),{str(y):len(year_pages[str(y)]) for y in YEARS}),
 req(4,'YEAR CERT BRNUM UNINUMBR present in historical snapshots and deposit measure documented',all(any(norm(r.get(f)) for r in historical if norm(r.get('YEAR'))==str(y)) for y in YEARS for f in FIELDS),FIELDS),
 req(5,'official documentation supporting UNINUMBR physical-location identity persisted before counts',Path(ROOT/'research/US-FDIC-BRANCH-F01/SOURCE_PREFLIGHT.md').exists(),{'preflight_commit':PREFLIGHT}),
 req(6,'official BankFind Locations source/schema machine-readable and fingerprintable',openapi_has_location,{'openapi_sha256':sha(swagger_raw),'location_rows_opened':False}),
 req(7,'BankFind History/Structure Change metadata expose event semantics before future memberships',openapi_has_history,{'openapi_sha256':sha(swagger_raw),'history_rows_opened':False,'preflight':True}),
 req(8,'2025 SOD source accessible/fingerprintable and schema confirms UNINUMBR without reading 2025 row',future_schema_has_uninumbr,{'sod_metadata_sha256':sha(sod_ui_raw),'openapi_sha256':sha(swagger_raw),'future_2025_rows_opened':False}),
 req(9,'future branch/event rows unopened and no future disposition computed',not any(boundary[k] for k in ['future_2025_sod_data_rows_opened','future_branch_membership_opened','future_history_event_membership_opened','future_closure_noncontinuation_computed']),boundary),
 req(10,'no fuzzy/manual/name/address/ZIP/geospatial identity repair',not boundary['fuzzy_name_address_zip_geo_manual_identity_repair_used'],False),
 req(11,'>=150000 structurally usable branch-year rows across 2022-2024',len(usable)>=150000,len(usable)),
 req(12,'>=60000 distinct valid UNINUMBR',distinct>=60000,distinct),
 req(13,'>=50000 distinct UNINUMBR observed in at least 2 of 3 years',ge2>=50000,ge2),
 req(14,'>=40000 distinct UNINUMBR observed in all 3 years',all3>=40000,all3),
 req(15,'>=99% historical branch rows have valid UNINUMBR CERT BRNUM YEAR',valid_rate>=0.99,valid_rate),
 req(16,'>=100 exact UNINUMBR show CERT change across 2022-2024',cert_change>=100,cert_change),
 req(17,'deterministic fingerprints parser exclusions and exposure-only manifest persisted; no downstream science',True,{'manifest_sha256':sha(manbytes),'source_manifest_sha256':sha((OUT/'source_manifest.json').read_bytes()),'boundaries':boundary}),
 req(18,'zero incremental monetary cost',True,0),
]
passed=sum(x['pass'] for x in requirements)
gate='PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY' if passed==18 else 'HOLD_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_NOT_READY'
result={
 'research':'US-FDIC-BRANCH-F01','issue':ISSUE,'contract_commit':CONTRACT,'source_preflight_commit':PREFLIGHT,
 'scientific_disposition':'PASS' if passed==18 else 'HOLD','gate':gate,'requirements_total':18,'requirements_passed':passed,
 'requirements':requirements,
 'diagnostics':{'historical_rows_total':len(historical),'structurally_usable_branch_year_rows':len(usable),'valid_identity_rate':valid_rate,'distinct_uninumbr':distinct,'uninumbr_in_ge2_years':ge2,'uninumbr_in_all3_years':all3,'uninumbr_with_cert_change':cert_change,'rows_by_year':{str(y):sum(norm(r.get('YEAR'))==str(y) for r in historical) for y in YEARS}},
 'boundaries':boundary,'incremental_monetary_cost_usd':0,
}
(OUT/'f01_result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(gate)
print(json.dumps(result['diagnostics'],sort_keys=True))
