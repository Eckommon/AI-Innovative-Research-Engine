#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
STAGING='3cc19e706fa341c7bf27b919f8abd9e07855292d'
DEC='DEC-225'
GATE='HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY'

x=json.loads((ROOT/'research/US-EIA-GEN-F01/STAGING_RESULT.json').read_text(encoding='utf-8'))
assert x['gate']==GATE and x['scientific_disposition']=='HOLD'
assert x['requirements_total']==18 and x['requirements_passed']==17
failed=[r for r in x['requirements'] if not r['pass']]
assert len(failed)==1 and failed[0]['number']==8 and failed[0]['evidence']==664
assert x['diagnostics']['colocated_solar_generators']==95
assert x['diagnostics']['standalone_solar_generators']==569
assert x['diagnostics']['colocated_plant_ids']==92
assert len(x['diagnostics']['states_with_both_classes'])==15
assert all(v is False for v in x['boundaries'].values())
assert x['incremental_monetary_cost_usd']==0

result=f'''---
id: US-EIA-GEN-F01-RESULT
type: structural-feasibility-result
created: 2026-09-17
issue: 156
research: US-EIA-GEN-F01
disposition: HOLD
staging_commit: {STAGING}
contract_commit: {x['contract_commit']}
gate: {GATE}
---

# US-EIA-GEN-F01 Result / 결과

## Terminal disposition / 최종 판정

**`{GATE}`**

The immutable outcome-blind run passed **17 of 18** frozen requirements. The only failed requirement was gate 8: the January-2024 Planned snapshot contained **664** eligible 2024–2025 planned solar generator keys, below the prospectively frozen minimum of **1,000**.

고정된 18개 요구조건 중 **17개가 PASS**했고, 유일한 실패는 gate 8입니다. 2024-01 Planned snapshot의 2024–2025 계획 태양광 generator key는 **664개**로 사전고정한 최소 **1,000개**에 미달했습니다.

## Strong structural support that does not override HOLD

- COLOCATED focal solar generators: **95**
- STANDALONE focal solar generators: **569**
- distinct COLOCATED Plant IDs: **92**
- states containing both exposure classes: **15**
- focal exact-key ambiguity rate: **0%** / unambiguous rate **100%**
- valid planned month/year: **100%**
- positive finite nameplate capacity: **100%**
- plant-state consistency: **100%**
- manifest SHA-256: `{x['diagnostics']['manifest_sha256']}`

These facts show a clean and potentially useful cohort, but they cannot retroactively reduce the frozen 1,000-unit requirement.

## Future-outcome firewall

The December-2025 official workbook was fingerprinted and inspected only for workbook/sheet/header structure. No future data row, generator membership, status value, actual-operation date, schedule change, commissioning-slippage metric, relationship, prediction, causal estimate, plant/developer ranking or novelty claim was opened/computed.

## Consequence / 후속 조치

`US-EIA-GEN-N01` is **not authorized** under this branch. The 1,000-unit gate must not be lowered after observing the 664-unit cohort, and the exposure window may not be broadened post hoc to rescue this F01. Return to independent portfolio reselection or a separately preregistered new candidate/branch whose design is not conditioned on this outcome.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/US-EIA-GEN-F01/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 156
research: US-EIA-GEN-F01
status: terminal
---

# {DEC} — Terminate US-EIA-GEN-F01 at frozen cohort-size HOLD

Finalize `US-EIA-GEN-F01` as `{GATE}` from immutable staging commit `{STAGING}`.

The branch passed 17/18 gates, but only **664** focal planned solar generator keys were available against the frozen **>=1,000** requirement. Preserve the strong 95 COLOCATED / 569 STANDALONE support as evidence only; do not lower the threshold or broaden the exposure period after observing support. N01 is not authorized. Future generator outcomes remained unopened. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Finalize `US-EIA-GEN-F01` as frozen cohort-size HOLD; do not authorize N01 or lower/broaden the observed support gate. / `US-EIA-GEN-F01`을 고정 cohort-size HOLD로 종결하고 N01·threshold/window 사후구제를 금지. | 17/18 PASS; focal solar cohort 664 < frozen 1,000 despite 95 COLOCATED and 569 STANDALONE units. / 17/18 PASS이나 focal solar 664개로 고정 1,000개 미달. | Issue #156; `{STAGING}`; `research/US-EIA-GEN-F01/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260917-US-EIA-GEN-F01-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':156,'last_completed_research':'US-EIA-GEN-F01','last_decision':DEC,'updated':'2026-09-17'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-US-EIA-GEN-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 156
last_completed_research: US-EIA-GEN-F01
last_decision: DEC-225
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_EIA_GEN_F01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`\n\nUS-EIA-GEN-F01 is terminal HOLD: 17/18 frozen gates passed, but the focal planned-solar cohort was 664, below the frozen 1,000-unit minimum. Future commissioning outcomes remained unopened. N01 is not authorized.\n\n## Exact next action / 정확한 다음 행동\n\nReturn to an independent portfolio reselection. Do not lower the 1,000-unit threshold or broaden the January-2024/2024–2025 exposure definition after observing support.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_EIA_GEN_F01_HOLD__PORTFOLIO_RESELECTION_REQUIRED`\n\n- Issue #156 completed.\n- Contract: `{x['contract_commit']}`.\n- Immutable staging: `{STAGING}`.\n- 17/18 PASS; focal planned solar 664 < frozen 1,000.\n- COLOCATED 95; STANDALONE 569; COLOCATED Plant IDs 92; both-class states 15.\n- Identity/date/capacity/state gates all 100%.\n- December-2025 row-level outcomes remained unopened.\n- `US-EIA-GEN-N01` not authorized.\n- Next: independent portfolio reselection.\n- Cost: 0 USD.\n''',encoding='utf-8')
print(GATE)
