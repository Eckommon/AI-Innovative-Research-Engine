#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DEC = 'DEC-236'
ISSUE = 162
CONTRACT = '9d6a16975bc02638aae938f20b6591ffe02d1fa9'
REVAL = 'a835ed4eb46cb6634f7c55408029651819a74748'
SCORE = '776cf5702778cfd4e994a0c668b38f1dd6cd2019'
RESULT = '1fc531a3537e70863989002b99f858380b63f229'

cp = json.loads((ROOT / 'context/checkpoint.json').read_text(encoding='utf-8'))
assert cp['checkpoint_id'] == 'CHK-20260918-US-FDIC-BRANCH-N01-TERMINAL'
assert str(cp['active_issue']).lower() in {'none', 'null'}
assert cp['active_research'] == 'NONE'
assert cp['last_completed_issue'] == 161
assert cp['last_completed_research'] == 'US-FDIC-BRANCH-N01'
assert cp['last_decision'] == 'DEC-235'

score = (ROOT / 'research/PORTFOLIO-R39/SCORECARD.md').read_text(encoding='utf-8')
result = (ROOT / 'research/PORTFOLIO-R39/RESULT.md').read_text(encoding='utf-8')
canon = (ROOT / 'research/PORTFOLIO-R39/CANONICALIZATION.md').read_text(encoding='utf-8')
assert '`US-IRS-EO-001` | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 2 | **41** | **SELECT_F01**' in score
assert 'candidate_outcomes_opened: false' in score
assert 'SELECT_US_IRS_EO_001_FILED_STRUCTURE_TO_AUTOMATIC_REVOCATION_F01' in result
assert 'scientific_selection_changed: false' in canon
assert 'candidate_outcomes_opened: false' in canon

dec = f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: PORTFOLIO-R39
status: terminal
---

# {DEC} — Canonicalize R39 selection of IRS exempt-organization structural F01

Record the already-frozen `PORTFOLIO-R39` terminal selection without rescoring or reopening Issue #{ISSUE}.

Evidence chain: contract `{CONTRACT}`, revalidation `{REVAL}`, immutable scorecard `{SCORE}`, result `{RESULT}`. `US-IRS-EO-001` remains selected at 41/45 for one separate outcome-blind structural F01. The other three R39 candidates remain HOLD. Future automatic-revocation membership remains unopened, and prior nonfiling/missed-filing streaks remain prohibited as exposure. Incremental monetary cost remains 0 USD.
'''
(ROOT / f'registry/{DEC}.md').write_text(dec, encoding='utf-8')

logp = ROOT / 'registry/DECISION_LOG.md'
log = logp.read_text(encoding='utf-8')
if DEC not in log:
    row = f'''\n| `{DEC}` | 2026-09-18 | Canonicalize completed `PORTFOLIO-R39`: select `US-IRS-EO-001` 41/45 for one separate outcome-blind F01; no rescoring. / 완료된 R39 상태를 정규화하고 `US-IRS-EO-001` 41/45를 별도 outcome-blind F01로 선정, 재평가 없음. | Exact EIN identity, separate public filed-return and legal-status source families, direct revocation event and high next-gate information value survive conservative overlap penalty. / exact EIN, 분리된 공개 filing·법적상태 소스, 직접 revocation event와 높은 next-gate 정보가치가 보수적 중복 감점 후에도 우위. | Issue #162; `{SCORE}`; `research/PORTFOLIO-R39/RESULT.md`; `research/PORTFOLIO-R39/CANONICALIZATION.md` | active |\n'''
    logp.write_text(log.rstrip() + row, encoding='utf-8')

cp2 = {
    'checkpoint_id': 'CHK-20260918-PORTFOLIO-R39-TERMINAL',
    'active_issue': 'none',
    'active_research': 'NONE',
    'last_completed_issue': 162,
    'last_completed_research': 'PORTFOLIO-R39',
    'last_decision': DEC,
    'updated': '2026-09-18',
}
(ROOT / 'context/checkpoint.json').write_text(json.dumps(cp2, indent=2) + '\n', encoding='utf-8')

front = '''---
checkpoint_id: CHK-20260918-PORTFOLIO-R39-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 162
last_completed_research: PORTFOLIO-R39
last_decision: DEC-236
updated: 2026-09-18
---
'''
status = front + '''
# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R39_SELECTED_US_IRS_EO_001__F01_CONTRACT_REQUIRED`

PORTFOLIO-R39 is terminal. `US-IRS-EO-001` was selected at 41/45 from the immutable scorecard. Candidate future automatic-revocation membership remained unopened. The scientific selection was not changed by terminal canonicalization.

## Exact next action / 정확한 다음 행동

Design and freeze a separate outcome-blind `US-IRS-EO-F01` structural contract **before creating its Issue**. F01 may test historical Form-990 XML/index access, exact EIN semantics/coverage, historical filed-organization longitudinal support, documented automatic-revocation schema/date semantics and a future-membership firewall. It may not use prior nonfiling/missed-filing streaks as exposure or open future revocation membership.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / 'STATUS.md').write_text(status, encoding='utf-8')

handoff = front + f'''
# Session Handoff / 세션 인계

`PORTFOLIO_R39_SELECTED_US_IRS_EO_001__F01_CONTRACT_REQUIRED`

- Issue #162 completed.
- Contract: `{CONTRACT}`.
- Revalidation: `{REVAL}`.
- Scorecard: `{SCORE}`.
- Result: `{RESULT}`.
- Selected: `US-IRS-EO-001` 41/45.
- DOL 38 HOLD; FEMA-BPS 37 HOLD; BLS-CBP 36 HOLD.
- Candidate future outcome memberships unopened.
- No retroactive R39 activation decision was invented; `DEC-236` only canonicalizes the completed evidence chain.
- Next: freeze pre-Issue `US-IRS-EO-F01` structural contract.
- Prior nonfiling/missed-filing streak exposure prohibited.
- Cost: 0 USD.
'''
(ROOT / 'context/SESSION_HANDOFF.md').write_text(handoff, encoding='utf-8')

print('PORTFOLIO_R39_SELECTED_US_IRS_EO_001__F01_CONTRACT_REQUIRED')
