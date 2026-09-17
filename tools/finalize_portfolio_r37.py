#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-227'
CONTRACT='7ad2e9bf392d3e8fdf41982d7e1a800eca377f5a'
REVALIDATION='5c79e690f5ea4745a9ca6be18829e8e6178a1509'
SCORECARD='3c2e70376ddbfd8d34d72f68fbedaae2183df5f3'
SELECTION='SELECT_US_FSIS_SAMPLE_001_ESTABLISHMENT_SAMPLING_TO_RECALL_F01'

score=(ROOT/'research/PORTFOLIO-R37/SCORECARD.md').read_text(encoding='utf-8')
assert SELECTION in score
assert '`US-FSIS-SAMPLE-001` | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41**' in score
assert '`US-EPA-SDWIS-001` | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **38**' in score
assert '`US-CMS-NH-001` | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 1 | **37**' in score
assert '`US-USASPEND-VENDOR-001` | 4 | 2 | 2 | 5 | 4 | 5 | 5 | 4 | 3 | **34**' in score

result=f'''---
id: PORTFOLIO-R37-RESULT
type: stage0-portfolio-selection
created: 2026-09-17
issue: 157
state: COMPLETED_SELECTED
selection: {SELECTION}
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R37 Result / 결과

**`{SELECTION}`**

R37 executed the candidate pool and rubric frozen before Issue binding at `{CONTRACT}`, bounded source/internal-history/literature revalidation at `{REVALIDATION}`, and the one-time immutable scorecard at `{SCORECARD}`.

## Immutable ranking

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-FSIS-SAMPLE-001` | **41** | **SELECT_F01** |
| `US-EPA-SDWIS-001` | **38** | HOLD_SAME_REGULATORY_FRAMEWORK_OVERLAP |
| `US-CMS-NH-001` | **37** | HOLD_MATURE_TURNOVER_QUALITY_OVERLAP |
| `US-USASPEND-VENDOR-001` | **34** | HOLD_AMBIGUOUS_AWARD_INTERRUPTION_OUTCOME |

No tie-break was required.

## Why FSIS advances

FSIS offers the best remaining combination of cross-dataset information gain, direct future event quality, practical food-safety-process value, and an outcome-blind next gate that can cheaply falsify the hardest assumption: whether establishment-specific sampling records and later recall/public-health-alert records can be linked using only documented USDA establishment-number semantics.

The identity score is intentionally 4/5 rather than 5/5 because prefixes/format variants and recall identifier coverage still require explicit structural proof. No name/address/fuzzy/manual repair is authorized.

## What is authorized

Exactly one separate outcome-blind `US-FSIS-SAMPLE-F01` may be designed next. F01 may inspect official sampling/source schemas, establishment-directory identity semantics, archive/version coverage, establishment-number normalization rules, cardinality, and recall-source identifier/schema availability while keeping future recall membership sealed.

F01 may **not** open later recall membership, calculate pathogen-to-recall relationships, rank establishments, estimate recall probability, infer causality, or claim novelty.

## Non-claims

R37 establishes no food-safety relationship, vendor interruption relationship, drinking-water relationship, nursing-home relationship, prediction, ranking, causal effect, or novelty claim. Candidate future outcome rows remained unopened.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/PORTFOLIO-R37/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 157
research: PORTFOLIO-R37
status: terminal
---

# {DEC} — Select US-FSIS-SAMPLE-001 for separate outcome-blind F01

Finalize R37 with `{SELECTION}` from immutable scorecard `{SCORECARD}`.

Authorize only a separate `US-FSIS-SAMPLE-F01` structural/source/identity/cardinality gate. Sampling→regulatory attention already has FSIS precedent, so no novelty is claimed. Later recall membership remains unopened. SDWIS/CMS/USAspending remain portfolio HOLDs. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Select `US-FSIS-SAMPLE-001` at 41/45 and authorize only separate outcome-blind `US-FSIS-SAMPLE-F01`. / 41/45의 `US-FSIS-SAMPLE-001`을 선택하고 별도 outcome-blind F01만 허가. | Distinct official sampling→recall source families and practical process-control value lead, while identity normalization remains the structural falsification target. / distinct official sampling→recall 소스와 공정통제 가치가 우세하되 identity normalization은 구조적 검증 대상으로 유지. | Issue #157; `{SCORECARD}`; `research/PORTFOLIO-R37/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260917-PORTFOLIO-R37-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':157,'last_completed_research':'PORTFOLIO-R37','last_decision':DEC,'updated':'2026-09-17'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-PORTFOLIO-R37-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 157
last_completed_research: PORTFOLIO-R37
last_decision: DEC-227
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R37_SELECTED_US_FSIS_SAMPLE_001__F01_AUTHORIZATION_REQUIRED`\n\nR37 selected `US-FSIS-SAMPLE-001` at 41/45. Candidate future outcome rows remain unopened.\n\n## Exact next action / 정확한 다음 행동\n\nDesign and freeze a separate outcome-blind `US-FSIS-SAMPLE-F01` contract before opening its Issue. F01 must prove official FSIS sampling-source access, historical/version coverage, establishment-number semantics/normalization, independent-establishment cardinality, and recall-source identifier/schema availability without opening later recall membership.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R37_SELECTED_US_FSIS_SAMPLE_001__F01_AUTHORIZATION_REQUIRED`\n\n- Issue #157 should be completed.\n- Contract: `{CONTRACT}`.\n- Revalidation: `{REVALIDATION}`.\n- Scorecard: `{SCORECARD}`.\n- Ranking: FSIS 41, SDWIS 38, CMS 37, USAspending 34.\n- Selected: `{SELECTION}`.\n- Future outcome rows unopened; no novelty/causal/ranking claim.\n- Next: pre-Issue `US-FSIS-SAMPLE-F01` contract.\n- Cost: 0 USD.\n''',encoding='utf-8')
print(SELECTION)
