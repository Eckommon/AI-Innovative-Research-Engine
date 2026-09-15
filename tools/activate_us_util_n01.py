#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE = 137
status_p = ROOT / 'STATUS.md'
handoff_p = ROOT / 'context' / 'SESSION_HANDOFF.md'
checkpoint_p = ROOT / 'context' / 'checkpoint.json'
dec_log_p = ROOT / 'registry' / 'DECISION_LOG.md'
readme_p = ROOT / 'research' / 'US-UTIL-N01' / 'README.md'
dec_p = ROOT / 'registry' / 'DEC-188.md'

c = json.loads(checkpoint_p.read_text(encoding='utf-8'))
assert c['active_issue'] == 'none'
assert c['active_research'] == 'NONE'
assert c['last_completed_issue'] == 136
assert c['last_completed_research'] == 'PORTFOLIO-R28'
assert c['last_decision'] == 'DEC-187'
assert 'PORTFOLIO_R28_SELECTED_US_UTIL_N01__AUTHORIZATION_REQUIRED' in status_p.read_text(encoding='utf-8')

r = readme_p.read_text(encoding='utf-8')
assert 'state: AUTHORIZED_OUTCOME_BLIND_DESIGN' in r
assert 'reliability_magnitudes_opened: false' in r
assert 'AMI_SHARE_y' in r
assert 'IEEE_SAIDI_WITH_MED' in r
assert dec_p.exists()

dec_log = dec_log_p.read_text(encoding='utf-8')
if '`DEC-188`' not in dec_log:
    dec_log += "\n| `DEC-188` | 2026-09-16 | Authorize Issue #137 / US-UTIL-N01 and freeze utility-state AMI-penetration-ramp × future IEEE SAIDI With MED design before Reliability magnitude access. / #137 결과 비개봉 AMI ramp × 미래 SAIDI 설계 승인. | F02 already established panel/schema comparability; N01 may open AMI meter counts but Reliability magnitudes remain closed. | Issue #137; `research/US-UTIL-N01/README.md`; `registry/DEC-188.md` | active |\n"
dec_log_p.write_text(dec_log, encoding='utf-8')

checkpoint_id = 'CHK-20260916-US-UTIL-N01-ACTIVE'
front = f'''---
checkpoint_id: {checkpoint_id}
active_issue: 137
active_research: US-UTIL-N01
last_completed_issue: 136
last_completed_research: PORTFOLIO-R28
last_decision: DEC-188
updated: 2026-09-16
---
'''
next_action = (
    'Execute US-UTIL-N01 exactly as preregistered. Verify all 2019-2024 EIA-861 ZIP hashes against F02 first; '
    'then parse only Advanced Metering counts plus Reliability blank/nonblank IEEE-SAIDI-with-MED support, freeze deterministic pairs and fingerprint, '
    'and apply the frozen PASS/PARTIAL/HOLD gate without opening Reliability magnitudes or using NOAA storm magnitudes.'
)
status_p.write_text(front + f'''
# Project Status / 프로젝트 상태

**State / 상태:** `US_UTIL_N01_ACTIVE__OUTCOME_BLIND_AMI_RAMP_DESIGN`

Issue #137 / US-UTIL-N01 is active under DEC-188. The only authorized exposure is annual utility-state AMI penetration change using official AMI + AMR + Standard meter totals. Future outcome basis is IEEE SAIDI With MED, but its magnitudes remain closed.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')
handoff_p.write_text(front + f'''
# Session Handoff / 세션 인수인계

Issue #137 / US-UTIL-N01 is active and outcome-blind under DEC-188. Unit, denominator, exposure quantiles, future SAIDI basis, materiality, calipers, global utility single-use rule, storm boundary and PASS/PARTIAL/HOLD thresholds are frozen in `research/US-UTIL-N01/README.md`.

Reliability magnitude access remains forbidden.

Exact restart: {next_action}

Cost: **0 USD**.
''', encoding='utf-8')
checkpoint_p.write_text(json.dumps({
    'checkpoint_id': checkpoint_id,
    'active_issue': ISSUE,
    'active_research': 'US-UTIL-N01',
    'last_completed_issue': 136,
    'last_completed_research': 'PORTFOLIO-R28',
    'last_decision': 'DEC-188',
    'updated': '2026-09-16'
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

print(json.dumps({
    'state': 'US_UTIL_N01_ACTIVE__OUTCOME_BLIND_AMI_RAMP_DESIGN',
    'issue': ISSUE,
    'last_decision': 'DEC-188',
    'reliability_magnitudes_opened': False,
    'incremental_monetary_cost_usd': 0,
}, ensure_ascii=False))
