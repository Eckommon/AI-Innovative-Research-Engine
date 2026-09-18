#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import hashlib, json, re, urllib.request, zipfile, io

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/US-IRS-EO-N01/schema-preflight.json'
MD=ROOT/'research/US-IRS-EO-N01/SCHEMA_PREFLIGHT.md'
SCHEMA_URL='https://www.irs.gov/pub/irs-tege/990x-schema-2019v5.1.zip'
INDEX_URL='https://apps.irs.gov/pub/epostcard/990/xml/2019/index_2019.csv'
ZIP_URLS=[
'https://apps.irs.gov/pub/epostcard/990/xml/2019/2019_TEOS_XML_CT1.zip',
*[f'https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_{i}.zip' for i in range(1,9)]
]
AUTO='https://apps.irs.gov/pub/epostcard/data-download-revocation.zip'
UA='Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)'

CANDIDATES=[
'EIN','TaxPeriodEndDt','TaxPeriodBeginDt','ReturnTypeCd','StateAbbreviationCd',
'Organization501c3Ind','InitialReturnInd','FinalReturnInd','AmendedReturnInd',
'ApplicationPendingInd','GroupReturnForAffiliatesInd',
'VotingMembersGoverningBodyCnt','VotingMembersIndependentCnt',
'CYTotalRevenueAmt','CYTotalExpensesAmt','TotalAssetsEOYAmt','NetAssetsOrFundBalancesEOYAmt'
]
KEYWORDS=('VotingMembers','Revenue','Expenses','Assets','501c3','InitialReturn','FinalReturn',
          'AmendedReturn','ApplicationPending','GroupReturn','StateAbbreviation','TaxPeriod','EIN')

def request(url, method='GET'):
    return urllib.request.urlopen(urllib.request.Request(url,method=method,headers={'User-Agent':UA,'Accept':'*/*'}),timeout=90)

def head(url):
    with request(url,'HEAD') as r:
        return {'url':url,'status':getattr(r,'status',None),'content_type':r.headers.get('Content-Type'),
                'content_length':r.headers.get('Content-Length'),'etag':r.headers.get('ETag'),
                'last_modified':r.headers.get('Last-Modified'),'entity_body_bytes_consumed':0}

if OUT.exists() or MD.exists():
    raise SystemExit('immutable schema preflight already exists')

with request(SCHEMA_URL,'GET') as r:
    raw=r.read()
schema_sha=hashlib.sha256(raw).hexdigest()
zf=zipfile.ZipFile(io.BytesIO(raw))
names=zf.namelist()
all_text=''
for n in names:
    if n.lower().endswith(('.xsd','.xml','.txt')):
        try:
            all_text += '\n' + zf.read(n).decode('utf-8',errors='replace')
        except Exception:
            pass

element_names=set(re.findall(r'<(?:xs|xsd):element\b[^>]*\bname=["\']([^"\']+)["\']',all_text))
present={x:(x in element_names) for x in CANDIDATES}
keyword_hits=sorted(x for x in element_names if any(k.lower() in x.lower() for k in KEYWORDS))

meta={
 'research':'US-IRS-EO-N01','type':'schema_source_preflight',
 'contract_sha':'70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8','issue':164,
 'schema_url':SCHEMA_URL,'schema_sha256':schema_sha,'schema_bytes':len(raw),
 'schema_files':names,'candidate_element_presence':present,'keyword_element_hits':keyword_hits,
 'index_head':head(INDEX_URL),'historical_xml_zip_heads':[head(u) for u in ZIP_URLS],
 'automatic_revocation_head':head(AUTO),
 'historical_index_rows_opened':0,'historical_xml_return_rows_opened':0,
 'future_outcome_rows_opened':0,'automatic_revocation_entity_body_bytes_consumed':0,
 'incremental_monetary_cost_usd':0
}
OUT.write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n',encoding='utf-8')
MD.write_text(
 '# US-IRS-EO-N01 Schema/Source Preflight\n\n'
 f'- 2019 redacted Form 990X schema SHA-256: `{schema_sha}`\n'
 f'- Candidate exact element presence: `{json.dumps(present,sort_keys=True)}`\n'
 f'- Keyword-matched schema elements: **{len(keyword_hits)}**\n'
 f'- Historical XML ZIP endpoints HEAD-success: **{sum(1 for x in meta["historical_xml_zip_heads"] if x["status"]==200)}/{len(ZIP_URLS)}**\n'
 '- Historical organization-return rows opened: **0**\n'
 '- Automatic Revocation rows opened: **0**; entity-body bytes consumed: **0**\n'
 '- Incremental monetary cost: **0 USD**\n\n'
 'This preflight is schema/source metadata only. It does not alter the frozen N01 scientific contract.\n',
 encoding='utf-8')
print(json.dumps(present,sort_keys=True))
