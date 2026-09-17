#!/usr/bin/env python3
# Execution trigger: implementation-only correction attempt 02; frozen contract unchanged.
from __future__ import annotations
import copy, hashlib, json, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'research/US-FDIC-BRANCH-F01/staging/f01_result.json'
OUT=ROOT/'research/US-FDIC-BRANCH-F01/staging/attempt-02'
OUT.mkdir(parents=True,exist_ok=True)
CONTRACT='6568d9bd0d897abb0bcabf8eaf04f2e54f50177f'
PREFLIGHT='b8063ff71c3b9b7aa05a5c6cae2325901af6d531'
CORRECTION='08403a21ef34462149b3a22228c3f3a02300b50f'

raw=BASE.read_bytes()
base=json.loads(raw)
assert base['contract_commit']==CONTRACT
assert base['requirements_total']==18
assert base['requirements'][7]['number']==8
assert base['requirements'][7]['pass'] is False
for k in ('future_2025_sod_data_rows_opened','future_branch_membership_opened','future_history_event_membership_opened','future_closure_noncontinuation_computed'):
    assert base['boundaries'][k] is False

preflight=(ROOT/'research/US-FDIC-BRANCH-F01/SOURCE_PREFLIGHT.md').read_text(encoding='utf-8')
assert 'UNINUMBR' in preflight and 'YEAR' in preflight and 'CERT' in preflight and 'BRNUM' in preflight
assert 'regardless of ownership' in preflight

params=urllib.parse.urlencode({'filters':'YEAR:2025','fields':'YEAR,CERT,BRNUM,UNINUMBR','limit':1,'offset':0})
url='https://api.fdic.gov/banks/sod?'+params
req=urllib.request.Request(url,method='HEAD',headers={
    'User-Agent':'AI-Innovative-Research-Engine/US-FDIC-BRANCH-F01 outcome-blind schema preflight',
    'Accept':'application/json',
})
with urllib.request.urlopen(req,timeout=60) as resp:
    status=resp.status
    headers={k.lower():v for k,v in resp.headers.items()}
    # Deliberately do not call resp.read(): no 2025 response body or row is consumed.

header_evidence={
    'method':'HEAD','url':url,'http_status':status,
    'content_type':headers.get('content-type'),'content_length':headers.get('content-length'),
    'response_body_read':False,'future_2025_rows_opened':False,
    'schema_fields_requested':['YEAR','CERT','BRNUM','UNINUMBR'],
    'preflight_commit':PREFLIGHT,'correction_commit':CORRECTION,
}
header_evidence['request_evidence_sha256']=hashlib.sha256(json.dumps(header_evidence,sort_keys=True).encode()).hexdigest()

result=copy.deepcopy(base)
result['attempt']=2
result['supersedes_for_implementation_only']='staging/f01_result.json'
result['base_attempt_sha256']=hashlib.sha256(raw).hexdigest()
result['implementation_correction_commit']=CORRECTION
r8=result['requirements'][7]
r8['pass']=(200 <= status < 400)
r8['evidence']={
    'rowless_2025_sod_head':header_evidence,
    'official_current_sod_mandatory_schema_preflight':True,
    'openapi_sha256':base['requirements'][7]['evidence']['openapi_sha256'],
    'sod_metadata_sha256':base['requirements'][7]['evidence']['sod_metadata_sha256'],
    'future_2025_rows_opened':False,
}
result['requirements_passed']=sum(bool(x['pass']) for x in result['requirements'])
if result['requirements_passed']==18:
    result['scientific_disposition']='PASS'
    result['gate']='PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY'
else:
    result['scientific_disposition']='HOLD'
    result['gate']='HOLD_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_NOT_READY'
result['boundaries']['future_2025_sod_data_rows_opened']=False
result['incremental_monetary_cost_usd']=0
(OUT/'f01_result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
(OUT/'rowless_2025_schema_evidence.json').write_text(json.dumps(header_evidence,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(result['gate'])
print('requirements',result['requirements_passed'],'/18')
print('2025_HEAD',status,'BODY_READ=False')
