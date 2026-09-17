#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-223'
CONTRACT='6550f4cfbde9df2702c793b902d7676f05700d61'
REVALIDATION='c1a36a8fb522a2aa51a724ac4b78c05421a73d73'
SCORECARD='3a62ddae3e6fce7684d0d71da6de2d5e9045f9f5'
SELECTION='SELECT_US_EIA_GEN_001_GENERATOR_COMMISSIONING_SLIPPAGE_F01'

score=(ROOT/'research/PORTFOLIO-R36/SCORECARD.md').read_text(encoding='utf-8')
assert SELECTION in score
assert '`US-EIA-GEN-001` | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **39**' in score
assert '`US-CMS-HOSP-001` | 3 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 1 | **36**' in score
assert '`US-FDIC-BANK-001` | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 0 | **35**' in score
assert '`US-EDU-FIN-001` | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 4 | 0 | **34**' in score

result=f'''---
id: PORTFOLIO-R36-RESULT
type: stage0-portfolio-selection
created: 2026-09-17
issue: 155
state: COMPLETED_SELECTED
selection: {SELECTION}
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R36 Result / 결과

**`{SELECTION}`**

R36 executed the candidate pool and rubric frozen before Issue binding at `{CONTRACT}`, source/internal-history/overlap revalidation at `{REVALIDATION}`, and the one-time immutable scorecard at `{SCORECARD}`.

## Immutable ranking

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-EIA-GEN-001` | **39** | **SELECT_F01** |
| `US-CMS-HOSP-001` | **36** | HOLD_AGENCY_FRAMEWORK_OVERLAP |
| `US-FDIC-BANK-001` | **35** | HOLD_MATURE_FAILURE_PREDICTION_OVERLAP |
| `US-EDU-FIN-001` | **34** | HOLD_NEAR_IDENTICAL_CLOSURE_PREDICTION_OVERLAP |

No tie-break was required.

## Why EIA advances

The EIA branch combines a source-native plant-code + generator-ID identity prospect, large independent-unit support, direct prospective commissioning timing/status and strong practical infrastructure-delivery value. It is selected despite — not because of ignoring — existing EIA delay analyses. Generic generator/solar delay is therefore not a novelty claim; the next F01 must first establish whether longitudinal generator snapshots can support a deterministic preregistered trajectory design without outcome leakage.

## What is authorized

Exactly one separate outcome-blind `US-EIA-GEN-F01` may be designed next. F01 may inspect source access, schemas, snapshot lineage, generator identifiers, schedule/status field availability, longitudinal uniqueness and cardinality only.

F01 may **not** open or calculate generator-specific commissioning slippage, technology delay rates, developer/project rankings, cancellation relationships, predictive metrics or causal effects. If generator identity/snapshot continuity is ambiguous, the branch must HOLD without name/geospatial/manual repair.

## Non-claims

R36 establishes no commissioning-delay relationship, project/developer risk, technology comparison, closure/failure/readmission relationship, causal effect or novelty claim. Candidate outcome rows remained unopened.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/PORTFOLIO-R36/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 155
research: PORTFOLIO-R36
status: terminal
---

# {DEC} — Select US-EIA-GEN-001 for separate outcome-blind F01

Finalize R36 with `{SELECTION}` from immutable scorecard `{SCORECARD}`.

Authorize only a separate `US-EIA-GEN-F01` structural/source/snapshot/identity gate. Generic EIA delay existence is not novel and candidate outcome values remain unopened. CMS, FDIC and education candidates remain portfolio HOLDs because of stronger agency/literature overlap. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Select `US-EIA-GEN-001` at 39/45 and authorize only separate outcome-blind `US-EIA-GEN-F01`. / 39/45의 `US-EIA-GEN-001`을 선택하고 별도 outcome-blind F01만 허가. | Source-native generator identity and commissioning bottleneck value lead; agency delay precedent is explicitly penalized and no novelty is claimed. / source-native generator identity·commissioning bottleneck 가치가 우세하되 기관 delay 선례를 감점하고 신규성은 주장하지 않음. | Issue #155; `{SCORECARD}`; `research/PORTFOLIO-R36/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260917-PORTFOLIO-R36-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':155,'last_completed_research':'PORTFOLIO-R36','last_decision':DEC,'updated':'2026-09-17'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-PORTFOLIO-R36-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 155
last_completed_research: PORTFOLIO-R36
last_decision: DEC-223
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+f'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R36_SELECTED_US_EIA_GEN_001__F01_AUTHORIZATION_REQUIRED`\n\nR36 selected `US-EIA-GEN-001` at 39/45. Candidate outcome rows remain unopened.\n\n## Exact next action / 정확한 다음 행동\n\nDesign and freeze a separate outcome-blind `US-EIA-GEN-F01` contract before opening its Issue. F01 must test official EIA source access, snapshot lineage, exact plant-code + generator-ID continuity, schedule/status schema and cardinality without calculating commissioning slippage.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R36_SELECTED_US_EIA_GEN_001__F01_AUTHORIZATION_REQUIRED`\n\n- Issue #155 should be completed.\n- Contract: `{CONTRACT}`.\n- Revalidation: `{REVALIDATION}`.\n- Scorecard: `{SCORECARD}`.\n- Ranking: EIA 39, CMS 36, FDIC 35, EDU 34.\n- Selected: `{SELECTION}`.\n- Candidate outcomes unopened; no novelty/causal/ranking claim.\n- Next: pre-Issue `US-EIA-GEN-F01` contract.\n- Cost: 0 USD.\n''',encoding='utf-8')
print(SELECTION)
