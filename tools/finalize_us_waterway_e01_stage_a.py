#!/usr/bin/env python3
"""Adjudicate US-WATERWAY-E01 Stage A PASS and freeze Stage B implementation.

Uses only committed Stage-A structural evidence. No delay magnitude or hydrology
observation value is opened by this finalizer.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research'/'US-WATERWAY-E01'
REG=ROOT/'registry'

support=json.loads((R/'STAGE_A_SUPPORT.json').read_text(encoding='utf-8'))
assert support['stage_a_gate']=='PASS_US_WATERWAY_E01_STAGE_A_PANEL_SUPPORT'
assert support['qualified_unique_usgs_gages']>=12
assert support['qualified_all_year_locks']>=20
assert support['prospective_gage_year_cells']>=120
assert support['boundary']['delay_magnitudes_parsed'] is False
assert support['boundary']['hydrology_values_parsed'] is False
assert support['incremental_monetary_cost_usd']==0

claim='''---
id: CLM-142
type: claim
created: 2026-09-11
issue: 100
status: active
---

# CLM-142 — US-WATERWAY-E01 Stage A panel support passes

The preregistered outcome-blind Stage A passes: the official Annual Usage surface was traversed across **58 pages**, yielding **179** Average Delay identity rows; **23** prospectively qualified locks have nonblank 2016–2025 Annual Usage support and full-period Daily USGS `00060/00003` metadata, spanning **13 unique USGS gages** and **130 prospective gage-year cells**.

Evidence class: `OBSERVED/DERIVED/VALIDATED`  
Verification: `V3_PREREGISTERED_SOURCE_PANEL_REPRODUCED`  
Source: `research/US-WATERWAY-E01/STAGE_A_RESULT.md`; GitHub Actions Run `34575280258`.

No delay magnitude or hydrology observation value was parsed or persisted in Stage A. Shared-gage locks remain one exposure cluster. Incremental monetary cost: **0 USD**.
'''
(REG/'CLM-142.md').write_text(claim,encoding='utf-8')

decision='''---
id: DEC-138
type: decision
created: 2026-09-11
issue: 100
status: accepted
---

# DEC-138 — Accept US-WATERWAY-E01 Stage A PASS and authorize frozen Stage B

Accept `PASS_US_WATERWAY_E01_STAGE_A_PANEL_SUPPORT` under DEC-137. Stage B may open only the preregistered USACE Annual Usage `Average Delay (minutes)` and USGS Daily `00060/00003` values for the prospectively frozen Stage-A gage↔lock set and 2016–2025 interval.

Stage B must follow `research/US-WATERWAY-E01/STAGE_B_IMPLEMENTATION_CONTRACT.md`. No alternate hydrology parameter, percentile threshold, time window, lock subset, outcome, covariance estimator, lag/lead, river filter, novelty claim, utility claim, causal claim or prediction claim may rescue the primary gate. Sensitivities run only after the primary gate is fixed. Incremental monetary cost remains **0 USD**.
'''
(REG/'DEC-138.md').write_text(decision,encoding='utf-8')

contract='''# US-WATERWAY-E01 Stage B Implementation Contract

Frozen **before any delay magnitude or hydrology observation value is opened**. This document operationalizes, but does not change, DEC-137 / the E01 preregistration.

## 1. Frozen cohort and interval

- Use only rows in `STAGE_A_GAGE_LOCK_MAP.csv`.
- Calendar interval: **2016-01-01 through 2025-12-31**.
- Exposure unit: **USGS monitoring-location × calendar-year**. Multiple locks sharing one gage are not independent exposure units.
- Primary hydrology: USGS Daily streamflow `00060`, daily-mean statistic `00003` only.
- Primary outcome: USACE Annual Usage `Average Delay (minutes)` only.

## 2. Source integrity and raw-byte policy

- Re-fetch official public USGS daily values and the official Corps Locks Annual Usage surface at zero incremental monetary cost.
- Raw external bytes/HTML are transient under RAW-001. Persist source URLs, retrieval metadata/hashes where available, derived panel/results and code only.
- No source substitution if an official route is unavailable; resolve source support as HOLD.

## 3. Hydrology parsing and completeness

For each Stage-A qualified gage:
- accept only finite, nonnegative Daily `00060/00003` observations dated in the frozen interval;
- duplicate conflicting values for the same gage/date are unusable and trigger source-semantics HOLD if unresolved deterministically;
- no imputation;
- a gage-year is usable only with **>=330** usable daily observations;
- a gage is primary-eligible only if it has >=330 usable days in **every one of the ten years** and >=3300 usable days over the full interval.

Compute `q10_g` and `q90_g` once from all usable 2016–2025 daily observations of that gage using NumPy's default linear quantile interpolation (`method='linear'`). Freeze these thresholds before annual exposure aggregation.

Primary annual exposure:
`E_gy = count(Q < q10_g or Q > q90_g) / usable_days_gy`.
Strict inequalities are used; values equal to q10/q90 are not extreme.

## 4. Delay parsing and gage-year outcome

For every prospectively mapped lock-year:
- parse only the Annual Usage `Average Delay (minutes)` cell;
- require a finite numeric value >=0;
- no winsorization, transformation, imputation or partial lock-set substitution.

For a gage-year, all Stage-A mapped qualified locks for that gage must have valid delay values. Then:
`Y_gy = unweighted arithmetic mean of mapped lock Average Delay values`.

## 5. Realized panel support gate

Before fitting the relationship model, require:
- >= **12 unique primary-eligible gages**;
- >= **120 usable gage-year observations**;
- at least 2 distinct values of `E_gy` after fixed-effect residualization;
- no invalid negative/nonfinite delay value.

Failure resolves `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT` without predictor/outcome substitution.

## 6. Fixed-effects implementation

Primary model:
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`.

Residualize `Y` and `E` against gage and calendar-year fixed effects by alternating projections:
1. subtract gage means;
2. subtract calendar-year means;
3. repeat in that order until the maximum absolute change across residualized variables is < `1e-12`;
4. maximum 1000 iterations; non-convergence is inference HOLD.

Fit no-intercept OLS `Y_tilde ~ E_tilde`. Require rank 1 and finite coefficient/residuals.

## 7. Primary two-way CR1 inference

Let `X` be the single residualized exposure column and `u` the primary residual.
For each cluster family, cluster score is `s_c = X_c' u_c`; meat is `sum_c s_c s_c'`.

Full parameter count for finite-sample correction:
`K = G + T`, where G = number of realized gages and T = number of realized calendar years (intercept + G-1 gage FE + T-1 year FE + one exposure slope).

For a cluster family with C clusters:
`c_C = [C/(C-1)] * [(N-1)/(N-K)]`.

Primary covariance:
`V = V_gage + V_year - V_intersection`, where intersection clusters are individual gage-year observations. No PSD clipping/projection.

Require finite positive slope variance. Reference degrees of freedom:
`df = min(G-1, T-1)`.
Use Student-t two-sided 95% CI and two-sided p-value.

## 8. Frozen primary gate

Directional hypothesis: `beta > 0`.
Materiality: `0.10 * beta >= 5 minutes`.

Primary PASS only if all hold:
1. `beta > 0`;
2. two-sided 95% CI lower bound > 0;
3. `0.10 * beta >= 5` minutes.

Otherwise classify exactly as preregistered:
- statistically detectable positive but submaterial -> `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01`;
- otherwise -> `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP`;
- source/panel/inference failure -> `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`.

The primary gate is stored before any sensitivity result is calculated.

## 9. Prespecified non-gate sensitivities

Only after primary gate fixation:
1. high-flow-only share `Q > q90_g`;
2. low-flow-only share `Q < q10_g`;
3. leave-one-gage-out coefficient range.

Sensitivities cannot rescue or alter the primary classification.

## 10. Interpretation boundary

E01 is an observational contemporaneous annual relationship test. It does **not** establish causality, advance prediction, propagation, novelty, lock ranking, operational utility, or an optimal hydrologic threshold.

Incremental monetary cost: **0 USD**.
'''
(R/'STAGE_B_IMPLEMENTATION_CONTRACT.md').write_text(contract,encoding='utf-8')

readme=(R/'README.md').read_text(encoding='utf-8')
readme=readme.replace('state: ACTIVE_STAGE_A_PANEL_SUPPORT','state: ACTIVE_STAGE_B_AUTHORIZED')
(R/'README.md').write_text(readme,encoding='utf-8')

# Append compact durable index rows without rewriting prior history.
ledger=REG/'CLAIM_LEDGER.md'
with ledger.open('a',encoding='utf-8') as f:
    f.write('\n| `CLM-142` | US-WATERWAY-E01 Stage A passes: 23 all-year locks, 13 unique gages, 130 prospective gage-years; no magnitudes opened. / E01 Stage A 구조 PASS. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_SOURCE_PANEL_REPRODUCED` | Run `34575280258`; `research/US-WATERWAY-E01/STAGE_A_RESULT.md` | 2026-09-11 | active |\n')
log=REG/'DECISION_LOG.md'
with log.open('a',encoding='utf-8') as f:
    f.write('\n- [DEC-138](DEC-138.md): accept US-WATERWAY-E01 Stage A PASS and authorize only the frozen Stage B implementation contract; no values opened by adjudication. / Stage A PASS 수용 및 고정 Stage B만 승인.\n')

status='''---
checkpoint_id: CHK-20260911-US-WATERWAY-E01-STAGE-B-AUTHORIZED
active_issue: 100
active_research: US-WATERWAY-E01
last_completed_issue: 99
last_completed_research: PORTFOLIO-R14
last_decision: DEC-138
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WATERWAY_E01_STAGE_A_PASS__STAGE_B_AUTHORIZED`

US-WATERWAY-E01 Stage A passed prospectively with **23** all-year matched locks, **13** unique USGS gages and **130** prospective gage-year cells. No delay magnitude or hydrology observation value was opened during Stage A.

## Exact next action / 정확한 다음 행동

Execute only the frozen Stage B in `research/US-WATERWAY-E01/STAGE_B_IMPLEMENTATION_CONTRACT.md`. Open the preregistered Annual Usage `Average Delay (minutes)` and USGS Daily `00060/00003` values only for the frozen Stage-A cohort and 2016–2025 interval. Fix the primary gate before sensitivities. No tuning/substitution/rescue.

Incremental monetary cost remains **0 USD**.
'''
(ROOT/'STATUS.md').write_text(status,encoding='utf-8')

handoff='''---
checkpoint_id: CHK-20260911-US-WATERWAY-E01-STAGE-B-AUTHORIZED
active_issue: 100
active_research: US-WATERWAY-E01
last_completed_issue: 99
last_completed_research: PORTFOLIO-R14
last_decision: DEC-138
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

Issue #100 `US-WATERWAY-E01` remains the sole active research gate. Stage A is durably **PASS** (`CLM-142`, `DEC-138`).

Exact next action: execute the frozen Stage B implementation contract. The primary panel is gage×calendar-year over 2016–2025; exposure is within-gage q10/q90 extreme-day share from Daily streamflow `00060/00003`; outcome is the unweighted mean Annual Usage `Average Delay (minutes)` across the prospectively mapped locks for each gage-year. Two-way CR1 is by gage and calendar year. Store the primary gate before sensitivities.

Do not substitute predictors/outcomes, tune percentiles, search lags/leads, cherry-pick rivers, rank locks, or claim causality/prediction/novelty/utility. Cost remains 0 USD.
'''
(ROOT/'context'/'SESSION_HANDOFF.md').write_text(handoff,encoding='utf-8')

checkpoint={
  'checkpoint_id':'CHK-20260911-US-WATERWAY-E01-STAGE-B-AUTHORIZED',
  'active_issue':100,
  'active_research':'US-WATERWAY-E01',
  'last_completed_issue':99,
  'last_completed_research':'PORTFOLIO-R14',
  'last_decision':'DEC-138',
  'updated':'2026-09-11'
}
(ROOT/'context'/'checkpoint.json').write_text(json.dumps(checkpoint,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'gate':support['stage_a_gate'],'claim':'CLM-142','decision':'DEC-138','state':'STAGE_B_AUTHORIZED'}))
