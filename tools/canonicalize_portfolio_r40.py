#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-241'
ISSUE=165
CONTRACT='22ff4cc6045bb895e5e4fe45dccca42bfc25867f'
REVAL='1700a3877e540b68ebec1e85f8624fbe0a02727d'
SCORE='4c2977bc5b2b386d09193010244629dfec63969f'
RESULT='f3a4e615b640e668a56759305fe4a783591a3cfb'

cp=json.loads((ROOT/'context/checkpoint.json').read_text(encoding='utf-8'))
assert cp['checkpoint_id']=='CHK-20260918-US-IRS-EO-N01-TERMINAL'
assert str(cp['active_issue']).lower() in {'none','null'}
assert cp['active_research']=='NONE'
assert cp['last_completed_issue']==164
assert cp['last_completed_research']=='US-IRS-EO-N01'
assert cp['last_decision']=='DEC-240'

score=(ROOT/'research/PORTFOLIO-R40/SCORECARD.md').read_text(encoding='utf-8')
result=(ROOT/'research/PORTFOLIO-R40/RESULT.md').read_text(encoding='utf-8')
assert '`US-FCC-ULS-001` | 4 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | **39** | **SELECT_F01**' in score
assert 'candidate_future_event_membership_used_for_scoring: false' in score
assert 'SELECT_US_FCC_ULS_001_LICENSE_STRUCTURE_TO_CANCELLATION_TERMINATION_F01' in result

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: PORTFOLIO-R40
status: terminal
---

# {DEC} — Canonicalize R40 selection of FCC ULS structural F01

Record the frozen `PORTFOLIO-R40` terminal selection without rescoring.

Evidence chain: contract `{CONTRACT}`, revalidation `{REVAL}`, immutable scorecard `{SCORE}`, result `{RESULT}`. `US-FCC-ULS-001` remains selected at 39/45 for one separate outcome-blind structural F01. `US-FMCSA-CARRIER-001` remains HOLD at 38/45; SEC and NCES candidates remain HOLD at 36/45.

The next stage may test only ULS structural/source/identity feasibility before any future cancelled/terminated event cohort is opened. No scientific score or candidate boundary is changed by canonicalization. Incremental monetary cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Canonicalize completed `PORTFOLIO-R40`: select `US-FCC-ULS-001` 39/45 for one separate outcome-blind F01; no rescoring. / 완료된 R40에서 FCC ULS 후보 39/45를 별도 outcome-blind F01로 선정, 재평가 없음. | FCC unique 9-digit system ID, complete/daily public files, direct cancelled/terminated states and high next-gate information value survive same-system penalty. / 고유 9-digit ID·complete/daily 공개파일·직접 상태·높은 next-gate 가치가 same-system 감점 후 우위. | Issue #165; `{SCORE}`; `research/PORTFOLIO-R40/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp2={
 'checkpoint_id':'CHK-20260918-PORTFOLIO-R40-TERMINAL',
 'active_issue':'none','active_research':'NONE',
 'last_completed_issue':165,'last_completed_research':'PORTFOLIO-R40',
 'last_decision':DEC,'updated':'2026-09-18'
}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp2,indent=2)+'\n',encoding='utf-8')

front='''---
checkpoint_id: CHK-20260918-PORTFOLIO-R40-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 165
last_completed_research: PORTFOLIO-R40
last_decision: DEC-241
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''
# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R40_SELECTED_US_FCC_ULS_001__F01_CONTRACT_REQUIRED`

PORTFOLIO-R40 is terminal. `US-FCC-ULS-001` was selected at 39/45 from the immutable scorecard. The selection was not changed by canonicalization.

## Exact next action / 정확한 다음 행동

Design and freeze a separate outcome-blind `US-FCC-ULS-F01` structural contract **before creating its Issue and before opening a future cancelled/terminated event cohort**. F01 must prospectively freeze one radio-service family and source windows, then test official file access, exact 9-digit system-ID semantics/coverage, action/status/date semantics, historical transaction lineage, support/cardinality, deterministic fingerprints and an outcome firewall.

Incremental monetary cost remains **0 USD**.
''',encoding='utf-8')

(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''
# Session Handoff / 세션 인계

`PORTFOLIO_R40_SELECTED_US_FCC_ULS_001__F01_CONTRACT_REQUIRED`

- Issue #165 completed.
- Contract: `{CONTRACT}`.
- Revalidation: `{REVAL}`.
- Scorecard: `{SCORE}`.
- Result: `{RESULT}`.
- Selected: `US-FCC-ULS-001` 39/45.
- FMCSA 38 HOLD; SEC 36 HOLD; NCES 36 HOLD.
- No candidate-specific future-event membership was used in scoring.
- Next: freeze pre-Issue `US-FCC-ULS-F01` structural contract.
- F01 must choose one radio-service family prospectively before empirical event membership.
- Cost: 0 USD.
''',encoding='utf-8')
print('PORTFOLIO_R40_SELECTED_US_FCC_ULS_001__F01_CONTRACT_REQUIRED')
