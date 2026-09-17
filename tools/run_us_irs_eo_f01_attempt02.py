#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re

import run_us_irs_eo_f01 as base

ROOT = Path(__file__).resolve().parents[1]
CORRECTION_COMMIT = 'd3026031bb7e5b90e63709589e226cd99babc590'
BASE_RUNNER_COMMIT = '14b671a6f0209cc6afba2099fa42e6bc209e63f9'
OUTDIR = ROOT / 'research/US-IRS-EO-F01/evidence'
JSON_OUT = OUTDIR / 'attempt-02.json'
MD_OUT = OUTDIR / 'attempt-02.md'
PRECISION = Counter()

original_parse_date = base.parse_date


def parse_date_attempt02(v: str):
    s = (v or '').strip()
    if re.fullmatch(r'\d{4}', s):
        year = int(s)
        if 1900 <= year <= 2100:
            PRECISION['YYYY_year_precision'] += 1
            # Internal ordering sentinel only. Month/day are not observed source values.
            return datetime(year, 1, 1)
    d = original_parse_date(v)
    if d is not None:
        PRECISION['existing_full_or_timestamp_precision'] += 1
        return d
    if s:
        PRECISION['unparsed_nonblank'] += 1
    else:
        PRECISION['blank'] += 1
    return None


def main() -> int:
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError('immutable attempt-02 evidence already exists')

    attempt1 = OUTDIR / 'attempt-01.json'
    if not attempt1.exists():
        raise RuntimeError('attempt-01 evidence missing')
    a1 = json.loads(attempt1.read_text(encoding='utf-8'))
    assert a1.get('attempt_valid') is True
    assert a1.get('failed_gates') == [11]
    assert a1.get('pass_count') == 17
    assert a1.get('future_outcome_rows_opened') == 0
    assert a1.get('future_form990_2025_2026_rows_opened') == 0
    assert a1.get('automatic_revocation_entity_body_bytes_consumed') == 0

    base.JSON_OUT = JSON_OUT
    base.MD_OUT = MD_OUT
    base.parse_date = parse_date_attempt02

    rc = base.main()

    evidence = json.loads(JSON_OUT.read_text(encoding='utf-8'))
    evidence['attempt'] = 2
    evidence['implementation_correction_commit'] = CORRECTION_COMMIT
    evidence['base_runner_commit'] = BASE_RUNNER_COMMIT
    evidence['attempt02_wrapper_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    evidence['submission_date_precision_counts'] = dict(sorted(PRECISION.items()))
    evidence['year_precision_semantics'] = (
        'Exact YYYY source values are accepted only as year-precision Submission Date representations. '
        'The internal YYYY-01-01 datetime is an ordering sentinel and does not assert an observed month or day.'
    )
    evidence['scientific_threshold_changed'] = False
    evidence['source_years_changed'] = False
    evidence['identity_rule_changed'] = False
    evidence['outcome_firewall_changed'] = False

    gate11 = next(g for g in evidence['gates'] if g['gate'] == 11)
    gate11['observed']['source_precision_counts'] = evidence['submission_date_precision_counts']
    gate11['observed']['min_max_semantics'] = 'year-precision values use Jan-01 internal ordering sentinel only; month/day are not observed'

    JSON_OUT.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n', encoding='utf-8')

    md = MD_OUT.read_text(encoding='utf-8')
    md = md.replace('# US-IRS-EO-F01 — Attempt 01', '# US-IRS-EO-F01 — Attempt 02', 1)
    md += '\n## Attempt 02 implementation-only correction\n\n'
    md += f'- Correction commit: `{CORRECTION_COMMIT}`\n'
    md += f'- Base runner commit: `{BASE_RUNNER_COMMIT}`\n'
    md += f"- Submission-date source precision counts: `{json.dumps(evidence['submission_date_precision_counts'], sort_keys=True)}`\n"
    md += '- Exact `YYYY` is treated as source **year precision** only. `YYYY-01-01` is an internal ordering sentinel, not an observed month/day.\n'
    md += '- Scientific thresholds changed: **false**\n'
    md += '- Source years changed: **false**\n'
    md += '- Identity rule changed: **false**\n'
    md += '- Outcome firewall changed: **false**\n'
    MD_OUT.write_text(md, encoding='utf-8')

    print(evidence['disposition'])
    print(json.dumps(evidence['submission_date_precision_counts'], sort_keys=True))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
