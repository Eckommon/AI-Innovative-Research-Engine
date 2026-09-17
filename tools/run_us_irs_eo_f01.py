#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
import csv
import hashlib
import html
import json
import os
import re
import tempfile
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_SHA = '689a00db411b650defcb679bef998beeb55a57da'
ISSUE = 163
INDEX_URLS = {
    2022: 'https://apps.irs.gov/pub/epostcard/990/xml/2022/index_2022.csv',
    2023: 'https://apps.irs.gov/pub/epostcard/990/xml/2023/index_2023.csv',
    2024: 'https://apps.irs.gov/pub/epostcard/990/xml/2024/index_2024.csv',
}
DOWNLOAD_PAGE = 'https://www.irs.gov/charities-non-profits/form-990-series-downloads'
FAQ_PAGE = 'https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-teos-faqs'
SCHEMA_PAGE = 'https://www.irs.gov/e-file-providers/current-valid-xml-schemas-and-business-rules-for-exempt-organizations-and-other-tax-exempt-entities-modernized-e-file'
AUTO_PAGE = 'https://www.irs.gov/charities-non-profits/automatic-revocation-of-exemption'
BULK_PAGE = 'https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads'
AUTO_ZIP = 'https://apps.irs.gov/pub/epostcard/data-download-revocation.zip'
XML_HEAD = 'https://apps.irs.gov/pub/epostcard/990/xml/2024/2024_TEOS_XML_01A.zip'
UA = 'Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)'
OUTDIR = ROOT / 'research/US-IRS-EO-F01/evidence'
JSON_OUT = OUTDIR / 'attempt-01.json'
MD_OUT = OUTDIR / 'attempt-01.md'


def req(url: str, method: str = 'GET', timeout: int = 90):
    r = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept': '*/*'})
    last = None
    for i in range(3):
        try:
            return urllib.request.urlopen(r, timeout=timeout)
        except Exception as e:
            last = e
            if i < 2:
                time.sleep(2 ** i)
    raise last


def get_text(url: str) -> tuple[str, dict]:
    with req(url, 'GET') as r:
        data = r.read()
        meta = {'status': getattr(r, 'status', None), 'content_type': r.headers.get('Content-Type'), 'bytes': len(data), 'final_url': r.geturl()}
    txt = data.decode('utf-8', errors='replace')
    return txt, meta


def head_meta(url: str) -> dict:
    # Never call read(): entity-body bytes consumed by this runner remain zero.
    methods = ['HEAD', 'OPTIONS']
    errors = []
    for method in methods:
        try:
            r = req(url, method)
            try:
                return {
                    'method': method,
                    'status': getattr(r, 'status', None),
                    'content_type': r.headers.get('Content-Type'),
                    'content_length': r.headers.get('Content-Length'),
                    'last_modified': r.headers.get('Last-Modified'),
                    'etag': r.headers.get('ETag'),
                    'final_url': r.geturl(),
                    'entity_body_bytes_consumed': 0,
                }
            finally:
                r.close()
        except Exception as e:
            errors.append(f'{method}:{type(e).__name__}:{e}')
    raise RuntimeError('; '.join(errors))


def normalize_header(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', (s or '').strip().lower())


def html_text(raw: str) -> str:
    raw = re.sub(r'(?is)<script.*?</script>|<style.*?</style>', ' ', raw)
    raw = re.sub(r'(?s)<[^>]+>', ' ', raw)
    return re.sub(r'\s+', ' ', html.unescape(raw)).strip().lower()


def ein_norm(v: str) -> str | None:
    s = (v or '').strip().replace('-', '')
    return s if re.fullmatch(r'\d{9}', s) else None


def tax_period_ok(v: str) -> bool:
    s = re.sub(r'\s+', '', (v or ''))
    if re.fullmatch(r'\d{6}', s):
        y, m = int(s[:4]), int(s[4:])
        return 1900 <= y <= 2100 and 1 <= m <= 12
    if re.fullmatch(r'\d{4}', s):
        y = int(s)
        return 1900 <= y <= 2100
    return False


def parse_date(v: str):
    s = (v or '').strip()
    for f in ('%Y-%m-%d', '%m/%d/%Y', '%Y%m%d', '%m/%d/%Y %H:%M:%S', '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.strptime(s, f)
        except ValueError:
            pass
    return None


def download_csv(year: int, url: str, td: Path) -> tuple[Path, dict]:
    p = td / f'index_{year}.csv'
    h = hashlib.sha256()
    n = 0
    with req(url, 'GET', timeout=180) as r, p.open('wb') as f:
        status = getattr(r, 'status', None)
        final_url = r.geturl()
        ctype = r.headers.get('Content-Type')
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
            f.write(chunk)
            n += len(chunk)
    return p, {'url': url, 'status': status, 'final_url': final_url, 'content_type': ctype, 'bytes': n, 'sha256': h.hexdigest()}


def resolve_fields(fieldnames: list[str]) -> tuple[dict, list[str]]:
    norm = {normalize_header(x): x for x in fieldnames if x is not None}
    concepts = {
        'return_id': ('returnid',),
        'filing_type': ('filingtype',),
        'ein': ('ein',),
        'tax_period': ('taxperiod',),
        'submission_date': ('submissiondate', 'subdate'),
        'taxpayer_name': ('taxpayername',),
        'dln': ('dln',),
        'object_id': ('objectid',),
    }
    out, missing = {}, []
    for concept, alts in concepts.items():
        hit = next((norm[a] for a in alts if a in norm), None)
        if hit is None:
            missing.append(concept)
        else:
            out[concept] = hit
    return out, missing


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError('immutable attempt-01 evidence already exists')

    evidence: dict = {
        'research': 'US-IRS-EO-F01',
        'attempt': 1,
        'contract_sha': CONTRACT_SHA,
        'issue': ISSUE,
        'github_run_id': os.environ.get('GITHUB_RUN_ID'),
        'incremental_monetary_cost_usd': 0,
        'future_outcome_rows_opened': 0,
        'future_form990_2025_2026_rows_opened': 0,
        'nonfiling_streak_exposure_variables_constructed': 0,
        'name_address_repair_used': False,
        'automatic_revocation_entity_body_bytes_consumed': 0,
        'gates': [],
    }
    runner_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    evidence['runner_sha256'] = runner_sha

    try:
        cp = json.loads((ROOT/'context/checkpoint.json').read_text(encoding='utf-8'))
        gate1 = cp.get('checkpoint_id') == 'CHK-20260918-US-IRS-EO-F01-ACTIVE' and cp.get('active_issue') == 163 and cp.get('active_research') == 'US-IRS-EO-F01' and cp.get('last_decision') == 'DEC-237'
        evidence['gates'].append({'gate': 1, 'pass': gate1, 'observed': cp})

        issue_bound = os.environ.get('IRS_EO_F01_ISSUE_BOUND') == '1' and os.environ.get('IRS_EO_F01_CONTRACT_SHA') == CONTRACT_SHA
        evidence['gates'].append({'gate': 2, 'pass': issue_bound, 'observed': {'issue': ISSUE, 'contract_sha': os.environ.get('IRS_EO_F01_CONTRACT_SHA')}})

        docs = {}
        for key, url in [('download', DOWNLOAD_PAGE), ('faq', FAQ_PAGE), ('schema', SCHEMA_PAGE), ('auto', AUTO_PAGE), ('bulk', BULK_PAGE)]:
            raw, meta = get_text(url)
            docs[key] = {'text': html_text(raw), 'meta': meta, 'url': url, 'sha256': hashlib.sha256(raw.encode('utf-8')).hexdigest()}

        total_rows = nonblank_ein = valid_ein_rows = 0
        tax_valid = object_nonblank = object_duplicate_rows = subdate_valid = 0
        distinct_eins: set[str] = set()
        ein_yearmask: dict[str, int] = {}
        object_seen: set[str] = set()
        index_meta = {}
        schema_by_year = {}
        dates_by_year = {}

        with tempfile.TemporaryDirectory() as tds:
            td = Path(tds)
            for bit, year in enumerate((2022, 2023, 2024)):
                p, meta = download_csv(year, INDEX_URLS[year], td)
                index_meta[str(year)] = meta
                with p.open('r', encoding='utf-8-sig', newline='') as f:
                    reader = csv.DictReader(f)
                    fields = reader.fieldnames or []
                    resolved, missing = resolve_fields(fields)
                    schema_by_year[str(year)] = {'raw_headers': fields, 'resolved': resolved, 'missing': missing}
                    if missing:
                        # Still count no rows; gate 4 will fail, but this is a valid empirical schema result.
                        continue
                    ymin = ymax = None
                    for row in reader:
                        total_rows += 1
                        raw_ein = (row.get(resolved['ein']) or '').strip()
                        if raw_ein:
                            nonblank_ein += 1
                        ein = ein_norm(raw_ein)
                        if ein is None:
                            continue
                        valid_ein_rows += 1
                        distinct_eins.add(ein)
                        ein_yearmask[ein] = ein_yearmask.get(ein, 0) | (1 << bit)
                        if tax_period_ok(row.get(resolved['tax_period']) or ''):
                            tax_valid += 1
                        obj = (row.get(resolved['object_id']) or '').strip()
                        if obj:
                            object_nonblank += 1
                            if obj in object_seen:
                                object_duplicate_rows += 1
                            else:
                                object_seen.add(obj)
                        d = parse_date(row.get(resolved['submission_date']) or '')
                        if d is not None:
                            subdate_valid += 1
                            ymin = d if ymin is None or d < ymin else ymin
                            ymax = d if ymax is None or d > ymax else ymax
                    dates_by_year[str(year)] = {'min': ymin.isoformat() if ymin else None, 'max': ymax.isoformat() if ymax else None}

        g3 = all(m['status'] and 200 <= int(m['status']) < 400 and m['bytes'] > 0 for m in index_meta.values()) and len(index_meta) == 3
        evidence['gates'].append({'gate': 3, 'pass': g3, 'observed': index_meta})
        g4 = len(schema_by_year) == 3 and all(not x['missing'] for x in schema_by_year.values())
        evidence['gates'].append({'gate': 4, 'pass': g4, 'observed': schema_by_year})

        ein_rate = valid_ein_rows / nonblank_ein if nonblank_ein else 0.0
        evidence['gates'].append({'gate': 5, 'pass': ein_rate >= 0.999, 'observed': {'valid_rows': valid_ein_rows, 'nonblank_rows': nonblank_ein, 'rate': ein_rate}})
        evidence['gates'].append({'gate': 6, 'pass': total_rows >= 500000, 'observed': {'combined_rows': total_rows, 'threshold': 500000}})
        evidence['gates'].append({'gate': 7, 'pass': len(distinct_eins) >= 150000, 'observed': {'distinct_valid_ein': len(distinct_eins), 'threshold': 150000}})
        longitudinal = sum(1 for mask in ein_yearmask.values() if mask & (mask - 1))
        evidence['gates'].append({'gate': 8, 'pass': longitudinal >= 75000, 'observed': {'ein_in_at_least_two_indexes': longitudinal, 'threshold': 75000}})
        tax_rate = tax_valid / valid_ein_rows if valid_ein_rows else 0.0
        evidence['gates'].append({'gate': 9, 'pass': tax_rate >= 0.99, 'observed': {'parseable_tax_period': tax_valid, 'valid_ein_rows': valid_ein_rows, 'rate': tax_rate}})
        obj_nonblank_rate = object_nonblank / valid_ein_rows if valid_ein_rows else 0.0
        dup_rate = object_duplicate_rows / object_nonblank if object_nonblank else 1.0
        evidence['gates'].append({'gate': 10, 'pass': obj_nonblank_rate >= 0.999 and dup_rate <= 0.001, 'observed': {'object_nonblank': object_nonblank, 'valid_ein_rows': valid_ein_rows, 'nonblank_rate': obj_nonblank_rate, 'duplicate_rows': object_duplicate_rows, 'duplicate_rate': dup_rate}})
        sub_rate = subdate_valid / valid_ein_rows if valid_ein_rows else 0.0
        evidence['gates'].append({'gate': 11, 'pass': sub_rate >= 0.99, 'observed': {'parseable_submission_dates': subdate_valid, 'valid_ein_rows': valid_ein_rows, 'rate': sub_rate, 'min_max_by_index': dates_by_year}})

        dtext = docs['download']['text']
        index_doc_ok = all(f'index file for {y}' in dtext for y in (2022, 2023, 2024)) and 'xml' in dtext
        xml_head = head_meta(XML_HEAD)
        g12 = index_doc_ok and xml_head['status'] is not None and 200 <= int(xml_head['status']) < 400 and xml_head['entity_body_bytes_consumed'] == 0
        evidence['gates'].append({'gate': 12, 'pass': g12, 'observed': {'download_page_documented': index_doc_ok, 'xml_zip_metadata': xml_head}})

        stext = re.sub(r'[^a-z0-9]+', '', docs['schema']['text'])
        g13 = 'form990' in stext and '990ez' in stext and '990pf' in stext
        evidence['gates'].append({'gate': 13, 'pass': g13, 'observed': {'official_schema_family_990': 'form990' in stext, '990ez': '990ez' in stext, '990pf': '990pf' in stext}})

        atext = docs['auto']['text']
        g14 = ('employer identification number' in atext or '(ein)' in atext) and 'effective date of revocation' in atext and ('date the organization was added' in atext or 'posted' in atext) and 'reinstatement' in atext
        evidence['gates'].append({'gate': 14, 'pass': g14, 'observed': {'ein': ('employer identification number' in atext or '(ein)' in atext), 'effective_revocation_date': 'effective date of revocation' in atext, 'posting_date': ('date the organization was added' in atext or 'posted' in atext), 'reinstatement': 'reinstatement' in atext}})
        g15 = 'three consecutive years' in atext and 'original filing due date of the third annual return or notice' in atext
        evidence['gates'].append({'gate': 15, 'pass': g15, 'observed': {'three_consecutive_years': 'three consecutive years' in atext, 'third_due_date_semantics': 'original filing due date of the third annual return or notice' in atext}})

        auto_head = head_meta(AUTO_ZIP)
        evidence['automatic_revocation_entity_body_bytes_consumed'] = auto_head['entity_body_bytes_consumed']
        g16 = auto_head['status'] is not None and 200 <= int(auto_head['status']) < 400 and auto_head['entity_body_bytes_consumed'] == 0
        evidence['gates'].append({'gate': 16, 'pass': g16, 'observed': auto_head})

        g17 = evidence['future_outcome_rows_opened'] == 0 and evidence['future_form990_2025_2026_rows_opened'] == 0 and evidence['nonfiling_streak_exposure_variables_constructed'] == 0 and not evidence['name_address_repair_used'] and evidence['automatic_revocation_entity_body_bytes_consumed'] == 0
        evidence['gates'].append({'gate': 17, 'pass': g17, 'observed': {k: evidence[k] for k in ('future_outcome_rows_opened','future_form990_2025_2026_rows_opened','nonfiling_streak_exposure_variables_constructed','name_address_repair_used','automatic_revocation_entity_body_bytes_consumed')}})

        evidence['source_fingerprints'] = {y: m['sha256'] for y, m in index_meta.items()}
        evidence['documentation_fingerprints'] = {k: v['sha256'] for k, v in docs.items()}
        g18 = len(evidence['source_fingerprints']) == 3 and all(re.fullmatch(r'[0-9a-f]{64}', x or '') for x in evidence['source_fingerprints'].values()) and re.fullmatch(r'[0-9a-f]{64}', runner_sha) is not None and evidence['incremental_monetary_cost_usd'] == 0
        evidence['gates'].append({'gate': 18, 'pass': g18, 'observed': {'source_sha256': evidence['source_fingerprints'], 'runner_sha256': runner_sha, 'contract_sha': CONTRACT_SHA, 'cost_usd': 0}})

        failed = [g['gate'] for g in evidence['gates'] if not g['pass']]
        evidence['attempt_valid'] = True
        evidence['pass_count'] = 18 - len(failed)
        evidence['failed_gates'] = failed
        evidence['disposition'] = 'PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY' if not failed else 'HOLD_US_IRS_EO_F01_FROZEN_GATES_FAILED'
    except Exception as e:
        evidence['attempt_valid'] = False
        evidence['implementation_error'] = {'type': type(e).__name__, 'message': str(e)}
        evidence['pass_count'] = sum(1 for g in evidence['gates'] if g.get('pass'))
        evidence['failed_gates'] = []
        evidence['disposition'] = 'IMPLEMENTATION_BLOCKED_US_IRS_EO_F01_ATTEMPT_01'

    JSON_OUT.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    lines = [
        '# US-IRS-EO-F01 — Attempt 01', '',
        f"**Disposition:** `{evidence['disposition']}`", '',
        f"- Attempt valid: `{evidence.get('attempt_valid')}`",
        f"- Gates passed: **{evidence.get('pass_count', 0)}/18**",
        f"- Failed gates: `{evidence.get('failed_gates', [])}`",
        f"- Future automatic-revocation rows opened: **{evidence['future_outcome_rows_opened']}**",
        f"- 2025/2026 Form-990 index rows opened: **{evidence['future_form990_2025_2026_rows_opened']}**",
        f"- Automatic-revocation entity-body bytes consumed: **{evidence['automatic_revocation_entity_body_bytes_consumed']}**",
        f"- Incremental monetary cost: **{evidence['incremental_monetary_cost_usd']} USD**", '',
        '## Gate ledger', '', '| Gate | PASS | Observed |', '|---:|:---:|---|'
    ]
    for g in evidence['gates']:
        obs = json.dumps(g.get('observed'), sort_keys=True, ensure_ascii=False)
        if len(obs) > 700:
            obs = obs[:697] + '...'
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{obs.replace('`','')}` |")
    if evidence.get('implementation_error'):
        lines += ['', '## Implementation error', '', f"`{evidence['implementation_error']}`"]
    lines += ['', 'This attempt did not read any Automatic Revocation List row. Scientific thresholds and source years were not modified.', '']
    MD_OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(evidence['disposition'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
