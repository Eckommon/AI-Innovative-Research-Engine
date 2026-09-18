#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, io, json, re, urllib.request, zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/US-IRS-EO-N01/schema-preflight-02.json'
MD=ROOT/'research/US-IRS-EO-N01/SCHEMA_PREFLIGHT_02.md'
URL='https://www.irs.gov/pub/irs-tege/990x-schema-2019v5.1.zip'
UA='Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)'
CANDIDATES=[
'EIN','TaxPeriodEndDt','TaxPeriodBeginDt','ReturnTypeCd','StateAbbreviationCd',
'Organization501c3Ind','InitialReturnInd','FinalReturnInd','AmendedReturnInd','ApplicationPendingInd',
'GroupReturnForAffiliatesInd','VotingMembersGoverningBodyCnt','VotingMembersIndependentCnt',
'CYTotalRevenueAmt','CYTotalExpensesAmt','TotalAssetsEOYAmt','NetAssetsOrFundBalancesEOYAmt'
]
if OUT.exists() or MD.exists(): raise SystemExit('immutable schema preflight 02 exists')
req=urllib.request.Request(URL,headers={'User-Agent':UA,'Accept':'*/*'})
with urllib.request.urlopen(req,timeout=90) as r: raw=r.read()
zf=zipfile.ZipFile(io.BytesIO(raw))
decl={x:[] for x in CANDIDATES}
for n in zf.namelist():
    if not n.lower().endswith('.xsd'): continue
    txt=zf.read(n).decode('utf-8',errors='replace')
    for x in CANDIDATES:
        if re.search(r'\bname=["\']'+re.escape(x)+r'["\']',txt):
            decl[x].append({'file':n,'mode':'name'})
        if re.search(r'\bref=["\'][^"\']*:?'+re.escape(x)+r'["\']',txt):
            decl[x].append({'file':n,'mode':'ref'})
e={
'research':'US-IRS-EO-N01','type':'schema_mapping_preflight_02',
'contract_sha':'70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8','issue':164,
'schema_url':URL,'schema_sha256':hashlib.sha256(raw).hexdigest(),
'candidate_declarations':decl,
'candidate_resolved':{k:bool(v) for k,v in decl.items()},
'historical_index_rows_opened':0,'historical_xml_return_rows_opened':0,
'future_outcome_rows_opened':0,'automatic_revocation_entity_body_bytes_consumed':0,
'scientific_contract_changed':False,'incremental_monetary_cost_usd':0
}
OUT.write_text(json.dumps(e,indent=2,sort_keys=True)+'\n',encoding='utf-8')
MD.write_text('# US-IRS-EO-N01 Schema Mapping Preflight 02\n\n'
              f'- Exact name/ref resolution: `{json.dumps(e["candidate_resolved"],sort_keys=True)}`\n'
              '- Historical return rows opened: **0**\n- Automatic Revocation rows opened: **0**\n'
              '- Scientific contract changed: **false**\n- Cost: **0 USD**\n',
              encoding='utf-8')
print(json.dumps(e['candidate_resolved'],sort_keys=True))
