#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-231'
CONTRACT='81216245922df756667295a4ffeb89fb41bd274f'
REVAL='51c51480bd1adff6e37676266d15b42a54ca29fd'
SCORE='293ee57618f94b934312ffcdc776277e24d76691'
ISSUE=159

cp=json.loads((ROOT/'context/checkpoint.json').read_text())
assert str(cp['active_issue']) in {'159','#159'} and cp['active_research']=='PORTFOLIO-R38' and cp['last_decision']=='DEC-230'
score=(ROOT/'research/PORTFOLIO-R38/SCORECARD.md').read_text()
assert '`US-FDIC-BRANCH-001` | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 2 | **39** | **SELECT_F01**' in score
assert 'candidate_outcomes_opened: false' in score

result=f'''---
id: PORTFOLIO-R38-RESULT
type: stage0-portfolio-selection
created: 2026-09-18
issue: {ISSUE}
state: COMPLETED_SELECTED
selection: SELECT_US_FDIC_BRANCH_001_DEPOSIT_NETWORK_TO_BRANCH_CLOSURE_F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R38 Result / 결과

**`SELECT_US_FDIC_BRANCH_001_DEPOSIT_NETWORK_TO_BRANCH_CLOSURE_F01`**

R38 executed the candidate pool/rubric frozen before Issue binding at `{CONTRACT}`, bounded source/internal-history/literature revalidation at `{REVAL}`, and the one-time immutable scorecard at `{SCORE}`.

## Immutable ranking

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-FDIC-BRANCH-001` | **39** | **SELECT_F01** |
| `US-CMS-DIALYSIS-001` | **36** | HOLD_MATURE_QUALITY_FRAMEWORK |
| `US-FRA-XING-001` | **35** | HOLD_DIRECT_PREDICTION_OVERLAP |
| `US-FCC-BDC-001` | **34** | HOLD_IDENTITY_AND_OUTCOME_AMBIGUITY |

No tie-break was required.

## What is authorized

Exactly one separate outcome-blind `US-FDIC-BRANCH-F01` may be designed next. Before any future closure membership is opened, F01 must prove or reject:

1. reproducible official SOD historical source access and branch-level schema;
2. exact source-native `UNINUMBR` / documented branch identity semantics across SOD and BankFind structure data;
3. whether acquisition, sale/lease, merger and identifier transition can be distinguished structurally from genuine branch closure/non-continuation without name/address repair;
4. sufficient independent branch/year cardinality and temporal support;
5. deterministic fingerprints/version lineage at zero incremental cost.

A future branch must not claim generic low-deposit→closure novelty: FDIC already publishes branch closure analyses and has documented lower-deposit closure patterns.

## Non-claims

R38 establishes no branch-closure relationship, crossing collision relationship, broadband withdrawal relationship, dialysis discontinuation relationship, prediction, ranking, causal effect or novelty claim. Candidate future event rows remained unopened.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/PORTFOLIO-R38/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: PORTFOLIO-R38
status: terminal
---

# {DEC} — Select FDIC branch identity/history for the next outcome-blind F01

Finalize `PORTFOLIO-R38` as `SELECT_US_FDIC_BRANCH_001_DEPOSIT_NETWORK_TO_BRANCH_CLOSURE_F01` from immutable scorecard `{SCORE}`.

Authorize only a separate pre-Issue `US-FDIC-BRANCH-F01` structural contract. Candidate branch-closure membership remains unopened. Generic deposit-to-closure association is not a novelty claim. FRA remains held for direct GXAPS/literature overlap; CMS for mature quality-framework overlap; FCC for provider-identity/outcome ambiguity. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Finalize `PORTFOLIO-R38` with `US-FDIC-BRANCH-001` selected 39/45 for one separate outcome-blind F01. / R38을 종결하고 `US-FDIC-BRANCH-001` 39/45를 별도 outcome-blind F01로 선정. | Exact FDIC branch IDs, long SOD history and high next-gate information value survive conservative overlap penalties; future closure membership stays sealed. / FDIC exact branch ID·장기 SOD·높은 next-gate 정보가치가 보수적 중복 감점 후에도 우위, 미래 closure membership 미개봉. | Issue #159; `{SCORE}`; `research/PORTFOLIO-R38/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-PORTFOLIO-R38-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':159,'last_completed_research':'PORTFOLIO-R38','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n')
front='''---
checkpoint_id: CHK-20260918-PORTFOLIO-R38-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 159
last_completed_research: PORTFOLIO-R38
last_decision: DEC-231
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R38_SELECTED_US_FDIC_BRANCH_001__F01_AUTHORIZATION_REQUIRED`\n\nR38 selected `US-FDIC-BRANCH-001` at 39/45. Candidate future branch-closure membership remains unopened.\n\n## Exact next action / 정확한 다음 행동\n\nDesign and freeze a separate outcome-blind `US-FDIC-BRANCH-F01` contract before opening its Issue. F01 must test SOD/BankFind source access, exact branch identity/history semantics, acquisition/sale/merger/ID-transition handling, cardinality and version lineage without opening future closure membership.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R38_SELECTED_US_FDIC_BRANCH_001__F01_AUTHORIZATION_REQUIRED`\n\n- Issue #159 completed.\n- Contract: `{CONTRACT}`.\n- Revalidation: `{REVAL}`.\n- Scorecard: `{SCORE}`.\n- Selected: FDIC branch 39/45.\n- CMS 36 HOLD; FRA 35 HOLD; FCC 34 HOLD.\n- Candidate future event membership unopened.\n- Next: pre-Issue `US-FDIC-BRANCH-F01` structural contract.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('SELECT_US_FDIC_BRANCH_001_DEPOSIT_NETWORK_TO_BRANCH_CLOSURE_F01')
