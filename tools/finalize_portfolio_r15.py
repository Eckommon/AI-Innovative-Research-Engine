#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R15 = ROOT / 'research' / 'PORTFOLIO-R15'
E02 = ROOT / 'research' / 'US-WATERWAY-E02'
REG = ROOT / 'registry'
R15.mkdir(parents=True, exist_ok=True)
E02.mkdir(parents=True, exist_ok=True)

result = '''---
id: PORTFOLIO-R15-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-11
issue: 101
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-006-SIGNED-FLOW-REDESIGN
selected_gate: US-WATERWAY-E02
next_issue: 102
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R15 Result — Post-E01 HOLD Reselection
# PORTFOLIO-R15 결과 — E01 HOLD 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_US_006_SIGNED_FLOW_REDESIGN_E02`**

Selected next gate: **Issue #102 `US-WATERWAY-E02` — preregistered signed-flow extreme burden × annual lock-delay relationship test.**

This is not an E01 rescue. E01 remains terminal HOLD. E02 is a new prospective contract fixed before any relationship coefficient or USACE delay outcome magnitude is opened.

## New source-semantics evidence / 신규 source 의미 근거

The R15 outcome-blind probe checked the 13 frozen USGS gages over 2016–2025 and found **28 negative Daily `00060/00003` observations across 2 gages**. Every negative record was published as **Approved**, with no additional qualifier, and legacy `/dv` reproduced the same signed values. Official USGS documentation also states that negative streamflow can occur from backwater, flow reversal and other phenomena, and that daily statistics do not automatically remove negative observations.

Therefore the E01 nonnegative-only rule was a valid fail-closed boundary but is not a generally valid USGS source-semantic rule. E02 prospectively accepts finite signed published discharge exactly as distributed; no deletion, truncation, absolute-value transform or imputation is allowed.

No USACE delay magnitude was opened and no cross-source relationship was computed during R15.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; total /45. Portfolio-control judgment only.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit / falsifiability | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WATERWAY signed-flow E02 redesign** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | **42** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_OPERABILITY |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| C-CA-002 Grain Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 1 | **35** | NO_AUTO_CONTINUATION |
| US-AIR descendant | 3 | 4 | 4 | 5 | 3 | 5 | 5 | 2 | 0 | **31** | NO_AUTO_CONTINUATION |

## Why E02 wins now / 현재 E02 우선 이유

The previous blocker is now characterized as a bounded source-semantic issue rather than an unknown data defect. The relationship itself remains completely untested, the 13-gage/23-lock deterministic cohort remains available, and the new signed-flow rule is fixed without outcome feedback. This gives E02 unusually high immediate information gain at zero incremental cost while preserving falsifiability.

US-UTIL remains technically ready but has higher external overlap risk; C-EU-001 remains scientifically attractive but current operability friction is materially higher.

Incremental monetary cost remains **0 USD**.
'''
(R15 / 'RESULT.md').write_text(result, encoding='utf-8')

claim = '''---
id: CLM-144
type: claim
created: 2026-09-11
issue: 101
status: active
---

# CLM-144 — Negative USGS daily discharge is published source data, not a missing-value sentinel

Across the 13 frozen US-WATERWAY gages for 2016–2025, the R15 source-semantics probe found **28 negative Daily `00060/00003` records across 2 gages**. All 28 were returned by the modern USGS Daily API as **Approved** with no additional qualifier, and the legacy `/dv` route reproduced the same signed values on the same dates.

This establishes that the E01 `Q >= 0` restriction was not a defensible universal source-semantic rule. It does **not** establish why each negative value occurred, nor any relationship with lock delay.

Source: `research/PORTFOLIO-R15/USGS_NEGATIVE_DISCHARGE_SEMANTICS.*`; Run `34577013281`. Incremental monetary cost: **0 USD**.
'''
(REG / 'CLM-144.md').write_text(claim, encoding='utf-8')

dec140 = '''---
id: DEC-140
type: decision
created: 2026-09-11
issue: 101
status: accepted
---

# DEC-140 — Select a prospective signed-flow US-WATERWAY redesign after E01 HOLD

PORTFOLIO-R15 selects `US-WATERWAY-E02` at **42/45** over C-EU-001 (39), US-UTIL descendant (38), C-CA-002 (37) and other retained alternatives.

Selection is justified because R15 independently resolved the E01 blocker as a source-semantics assumption problem: negative `00060/00003` values are approved published USGS observations. E01 remains terminal HOLD; no result is rewritten or rescued.

E02 may proceed only under a new preregistered contract that preserves signed finite discharge exactly as published and is fixed before relationship estimation or delay-outcome inspection.
'''
(REG / 'DEC-140.md').write_text(dec140, encoding='utf-8')

dec141 = '''---
id: DEC-141
type: decision
created: 2026-09-11
issue: 102
status: accepted
---

# DEC-141 — Preregister US-WATERWAY-E02 signed-flow relationship test

Authorize Issue #102 under `research/US-WATERWAY-E02/README.md`.

Frozen cohort: the exact E01 Stage-A-qualified 13 USGS gages and 23 deterministic locks over 2016–2025. Daily `00060/00003` values may be negative, zero or positive if finite numeric and officially published; sign must be preserved. Null/blank/non-numeric observations alone are missing. Each gage-year requires at least 330 usable daily observations.

Exposure, outcome, FE model, two-way CR1 inference, +10 percentage-point / +5-minute materiality floor, sensitivity order, and no-rescue rules are fixed before Stage B execution. Causality, prediction, novelty and decision utility remain unclaimed.
'''
(REG / 'DEC-141.md').write_text(dec141, encoding='utf-8')

e02 = '''---
id: US-WATERWAY-E02
issue: 102
state: ACTIVE_PREREGISTERED
mission_anchor: MEM-054
portfolio_decision: DEC-140
preregistration_decision: DEC-141
parent: US-WATERWAY-E01
relationship_computed: false
delay_magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E02 — Signed-Flow Extreme Burden × Annual Lock Delay
# US-WATERWAY-E02 — 부호 보존 수문 극단일 부담 × 연간 Lock 지연

## Scientific boundary / 과학적 경계

E02 is a new prospective descendant, not a modification of E01. E01 remains `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`.

## Frozen cohort
- exactly the 13 USGS gages / 23 locks in `research/US-WATERWAY-E01/STAGE_A_GAGE_LOCK_MAP.csv`;
- calendar years 2016–2025;
- shared gages contribute one gage-year outcome unit;
- no new manual/fuzzy identity repair.

## Frozen exposure `E_gy`
- USGS Daily discharge `00060`, statistic `00003`;
- accept every finite numeric published value **with sign preserved**, including negative and zero;
- never delete negatives, clamp to zero, take absolute values, or impute;
- null/blank/non-numeric = missing;
- require >=330 usable days in every included gage-year;
- compute q10_g and q90_g from all usable signed observations over fixed 2016–2025;
- `E_gy = share(Q < q10_g or Q > q90_g)` within year.

## Frozen outcome `Y_gy`
- USACE Annual Usage `Average Delay (minutes)` for every prospectively mapped lock-year;
- each nonblank value must be finite and >=0;
- gage-year outcome = unweighted arithmetic mean across mapped qualified locks;
- no imputation or alternate outcome.

## Frozen primary model
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`

- unweighted gage-year OLS;
- two-way CR1 by gage and calendar year;
- Student-t df = `min(G_gage-1, G_year-1)`;
- primary hypothesis: `beta > 0`;
- materiality: `0.10 * beta >= 5 minutes`.

Primary PASS requires beta > 0, two-sided 95% CI lower > 0, and materiality >=5 minutes per +10pp extreme-day share.

Terminal gates:
- `PASS_US_WATERWAY_E02_POSITIVE_MATERIAL_SIGNED_EXTREME_FLOW_DELAY_ASSOCIATION`
- `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E02`
- `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP`
- `HOLD_US_WATERWAY_E02_SOURCE_PANEL_OR_INFERENCE_SUPPORT`

## Non-gate sensitivities — only after primary gate fixed
1. high-flow-only share;
2. low-flow-only share, preserving signed Q;
3. leave-one-gage-out beta range.

Sensitivities cannot rescue or reverse primary.

## Prohibited
No abs(Q), negative-value deletion, zero coercion, alternate predictor, percentile tuning, lag/lead search, river cherry-picking, outcome substitution, causal/prediction/novelty/utility claim.

Incremental monetary cost: **0 USD**.
'''
(E02 / 'README.md').write_text(e02, encoding='utf-8')

# Append ledgers idempotently.
claim_ledger = REG / 'CLAIM_LEDGER.md'
cl = claim_ledger.read_text(encoding='utf-8')
line = '| `CLM-144` | R15 found 28 approved negative USGS Daily `00060/00003` records across 2/13 frozen gages; legacy `/dv` reproduced them, so negative values are not a missing-value sentinel. / 음수 discharge는 결측 sentinel이 아닌 승인 배포값이다. | `OBSERVED/DERIVED` | `V3_REPRODUCED` | Run `34577013281`; `research/PORTFOLIO-R15/USGS_NEGATIVE_DISCHARGE_SEMANTICS.*` | 2026-09-11 | active |'
if '`CLM-144`' not in cl:
    claim_ledger.write_text(cl.rstrip() + '\n' + line + '\n', encoding='utf-8')

dlog = REG / 'DECISION_LOG.md'
dl = dlog.read_text(encoding='utf-8')
for line in [
    '| `DEC-140` | 2026-09-11 | R15 selects prospective signed-flow `US-WATERWAY-E02` after source-semantics probe; E01 remains terminal HOLD. / source 의미 확인 후 별도 E02 선정. | Relationship remains untested; signed negative USGS discharge is approved source data. | Issue #101; `CLM-144`; `research/PORTFOLIO-R15/RESULT.md` | active |',
    '| `DEC-141` | 2026-09-11 | Preregister E02 with signed finite Daily `00060/00003`, frozen 13-gage/23-lock cohort, >=330 days/year and unchanged primary inferential gate. / signed-flow E02 사전등록. | Prospectively resolves E01 source assumption without outcome feedback. | Issue #102; `research/US-WATERWAY-E02/README.md` | active |'
]:
    if line.split('`')[1] not in dl:
        dl = dl.rstrip() + '\n' + line + '\n'
dlog.write_text(dl, encoding='utf-8')

status = '''---
checkpoint_id: CHK-20260911-US-WATERWAY-E02-ACTIVE
active_issue: 102
active_research: US-WATERWAY-E02
last_completed_issue: 101
last_completed_research: PORTFOLIO-R15
last_decision: DEC-141
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R15_SELECTED_US_WATERWAY_E02__PREREGISTERED_ACTIVE`

R15 selected a new signed-flow US-WATERWAY descendant after an outcome-blind source-semantics probe established that negative Daily USGS discharge values are approved published observations. E01 remains terminal HOLD and is not rewritten.

## Exact next action / 정확한 다음 행동

Execute only the frozen `US-WATERWAY-E02` contract in `research/US-WATERWAY-E02/README.md`. Preserve signed finite discharge, require >=330 usable daily values per gage-year, fit the primary model only if source/panel checks pass, fix the primary gate before sensitivities, and make no causal/novelty/utility claim.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / 'STATUS.md').write_text(status, encoding='utf-8')

handoff = '''---
checkpoint_id: CHK-20260911-US-WATERWAY-E02-ACTIVE
active_issue: 102
active_research: US-WATERWAY-E02
last_completed_issue: 101
last_completed_research: PORTFOLIO-R15
last_decision: DEC-141
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

Issue #101 PORTFOLIO-R15 selected Issue #102 `US-WATERWAY-E02` after R15 Run `34577013281` showed 28 approved negative Daily `00060/00003` records across 2/13 frozen gages. Negative values are preserved as signed source observations in E02; E01 remains terminal HOLD.

Execute the E02 frozen relationship test only. Use the exact 13-gage/23-lock cohort, 2016–2025, >=330 usable days per gage-year, signed q10/q90 extreme-day share, USACE Average Delay outcome, gage+year FE, two-way CR1, and the preregistered directional/materiality gate. Primary gate must be fixed before sensitivities. Cost = 0 USD.
'''
(ROOT / 'context' / 'SESSION_HANDOFF.md').write_text(handoff, encoding='utf-8')

checkpoint = {
  'checkpoint_id': 'CHK-20260911-US-WATERWAY-E02-ACTIVE',
  'active_issue': 102,
  'active_research': 'US-WATERWAY-E02',
  'last_completed_issue': 101,
  'last_completed_research': 'PORTFOLIO-R15',
  'last_decision': 'DEC-141',
  'updated': '2026-09-11'
}
(ROOT / 'context' / 'checkpoint.json').write_text(json.dumps(checkpoint, indent=2) + '\n', encoding='utf-8')
