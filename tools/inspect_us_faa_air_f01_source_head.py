#!/usr/bin/env python3
"""FAA F01 outcome-blind official-source HEAD transport preflight.

Do not GET any ZIP, open a row, request future event identity or test F01 science.
Metadata-only HEAD is not a gate PASS and cannot imply source date or identity.
"""
from __future__ import annotations
import datetime as dt
import json
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/US-FAA-AIR-F01/evidence/source-access-preflight-01.json'
MD = OUT.with_suffix('.md')
ISSUE = 220
CONTRACT = 'a4c775127eeafce152595759897590f553e237c5'
SOURCES = {
    'official_landing': 'https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download',
    'official_dictionary': 'https://registry.faa.gov/database/ardata.pdf',
    'current_aircraft_zip': 'https://registry.faa.gov/database/ReleasableAircraft.zip',
    'historical_2020_zip': 'https://registry.faa.gov/database/yearly/ReleasableAircraft.2020.zip',
    'historical_2021_zip': 'https://registry.faa.gov/database/yearly/ReleasableAircraft.2021.zip',
}

class BlockRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def probe_head(url, opener=None):
    if url not in SOURCES.values():
        raise ValueError('Not an exact pre-registered first-party source URL')
    opener = opener or urllib.request.build_opener(BlockRedirect())
    request = urllib.request.Request(url, method='HEAD', headers={
        'User-Agent': 'AI-Innovative-Research-Engine/1.0 (FAA-official-HEAD-only-science-sealed)',
        'Accept': '*/*',
    })
    try:
        with opener.open(request, timeout=18) as response:
            status = response.status
            headers = response.headers
            final = response.geturl()
            if final != url:
                raise RuntimeError('HTTP HEAD unexpectedly followed redirect')
    except urllib.error.HTTPError as error:
        status = error.code
        headers = error.headers
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return {
            'url': url, 'method': 'HEAD', 'http_status': None,
            'content_type': None, 'content_length_header': None, 'last_modified_header': None,
            'redirect_location': None, 'result': 'INCONCLUSIVE_HEAD_TRANSPORT',
            'error_type': type(error).__name__, 'body_read_bytes': 0,
        }
    return {
        'url': url, 'method': 'HEAD', 'http_status': status,
        'content_type': headers.get('Content-Type'),
        'content_length_header': headers.get('Content-Length'),
        'last_modified_header': headers.get('Last-Modified'),
        'redirect_location': headers.get('Location'),
        'result': 'HEAD_METADATA_ACCESSIBLE_NOT_BODY_PROVEN' if status == 200 else 'HEAD_NOT_VERIFIED_NO_FINAL_ABSENCE_INFERENCE',
        'error_type': None, 'body_read_bytes': 0,
    }

def classify(reports):
    all200 = all(v.get('http_status') == 200 for v in reports.values())
    return 'CONTINUE_FAA_F01_BODY_ACCESS_NOT_YET_PROVEN' if all200 else 'HOLD_FAA_F01_SOURCE_TRANSPORT_OR_LINEAGE_NOT_VERIFIED'

def run():
    if OUT.exists():
        raise RuntimeError('immutable preflight evidence exists; refusing overwrite')
    observed = dt.datetime.now(dt.timezone.utc).isoformat()
    report = {name: probe_head(url) for name, url in SOURCES.items()}
    record = {
        'research': 'US-FAA-AIR-F01', 'issue': ISSUE,
        'source_contract_commit': CONTRACT,
        'checked_at_utc': observed,
        'purpose': 'SOURCE_HEAD_METADATA_ONLY_NO_F01_SCIENTIFIC_GATES_EXECUTED',
        'source_urls': SOURCES,
        'source_reports': report,
        'disposition': classify(report),
        'historical_archives_body_validated': False,
        'current_baseline_zip_opened': False,
        'historical_zip_bodies_opened': False,
        'deregistered_file_rows_opened': False,
        'future_deregistration_membership_opened': False,
        'personal_owner_data_opened': False,
        'f01_18_gate_result': None,
        'incremental_monetary_cost_usd': 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# FAA F01 — official HEAD-only source preflight / FAA 원천 HEAD 접근성 실측', '',
        f'- Observed UTC / 관측시각: `{observed}`',
        f'- Disposition / 판정: `{record["disposition"]}`',
        '- No ZIP bodies, archived rows, deregistration events, owner fields or 18 science gates opened. / 미래 결과·소유자 정보 미열람.',
        '', '| Source | HEAD status | Redirect |', '|---|---|---|'
    ]
    for name, r in report.items():
        lines.append(f'| `{name}` | `{r["http_status"]}` | `{r["redirect_location"]}` |')
    lines += ['', 'An HTTP HEAD success/failure is a transport hint only. Even 200 is not proof of valid historical ZIP content. / 헤더 결과는 ZIP 존재·유효성·식별 성립을 보증하지 않음.', '', 'Incremental cost: **0 USD**.', '']
    MD.write_text('\n'.join(lines), encoding='utf-8')
    print('FAA_SOURCE_HEAD_PREFLIGHT', record['disposition'])
    print('source_statuses', {k:v['http_status'] for k,v in report.items()})

if __name__ == '__main__':
    run()
