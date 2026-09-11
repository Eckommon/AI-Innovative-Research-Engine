# US-WATERWAY-E02 Stage B Implementation Contract

Frozen **before E02 opens any USACE delay magnitude or computes any relationship**. This operationalizes DEC-141 without changing the preregistration. E01 remains terminal HOLD.

## 1. Frozen cohort and interval

- Reuse exactly `research/US-WATERWAY-E01/STAGE_A_GAGE_LOCK_MAP.csv`.
- 13 qualified USGS gages / 23 deterministic locks; no new fuzzy/manual identity repair.
- Calendar interval: **2016-01-01 through 2025-12-31**.
- Primary unit: **USGS monitoring-location × calendar-year**; shared-gage locks are not independent exposure units.
- Hydrology: USGS Daily `00060`, statistic `00003` only.
- Outcome: USACE Annual Usage `Average Delay (minutes)` only.

## 2. Source integrity / RAW-001

- Re-fetch official USGS Daily values and official Corps Locks Annual Usage at zero incremental monetary cost.
- Raw external bytes/HTML remain transient. Persist URLs, response/page hashes, derived panels/results and code only.
- No alternate source if an official route fails; unresolved source failure is HOLD.

## 3. Signed hydrology parsing and completeness

For each frozen gage:
- accept every **finite numeric** Daily `00060/00003` value in the interval, whether negative, zero or positive;
- preserve sign exactly as published;
- never drop a value because it is negative, clamp it to zero, take `abs(Q)`, or impute;
- `null`, blank or non-numeric observations alone are missing;
- conflicting duplicate values for one gage/date trigger source-semantics HOLD if not deterministically resolvable;
- a gage-year is usable only with **>=330** usable daily observations;
- a gage is primary-eligible only if every one of the ten years has >=330 usable days and the full interval has >=3300 usable days.

Compute `q10_g` and `q90_g` once from all usable **signed** 2016–2025 observations using NumPy linear quantiles (`method='linear'`).

Primary exposure:
`E_gy = count(Q < q10_g or Q > q90_g) / usable_days_gy`.
Strict inequalities apply.

## 4. Delay parsing and outcome

For every frozen mapped lock-year:
- parse only `Average Delay (minutes)`;
- require finite numeric value >=0;
- no transformation, winsorization, imputation or partial lock-set substitution.

For each gage-year:
`Y_gy = unweighted arithmetic mean of all mapped qualified lock Average Delay values`.

## 5. Realized panel gate

Before model fitting require:
- >= **12 unique primary-eligible gages**;
- >= **120 usable gage-year observations**;
- at least 2 distinct residualized `E_gy` values;
- no invalid delay value.

Failure: `HOLD_US_WATERWAY_E02_SOURCE_PANEL_OR_INFERENCE_SUPPORT`.

## 6. Fixed effects

Model:
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`.

Residualize `Y` and `E` by alternating projections:
1. subtract gage means;
2. subtract year means;
3. repeat in that order until max absolute change < `1e-12`;
4. maximum 1000 iterations; non-convergence = HOLD.

Fit no-intercept OLS `Y_tilde ~ E_tilde`; require rank 1 and finite coefficient/residuals.

## 7. Two-way CR1

For each cluster family use cluster score `s_c = X_c' u_c` and meat `sum_c s_c s_c'`.

Full parameter count: `K = G + T`.
For C clusters: `c_C = [C/(C-1)] * [(N-1)/(N-K)]`.

Primary covariance:
`V = V_gage + V_year - V_intersection`.
No PSD clipping/projection.

Require finite positive slope variance. `df = min(G-1, T-1)`. Use Student-t two-sided 95% CI and p-value.

## 8. Primary gate

- directional hypothesis: `beta > 0`;
- materiality: `0.10 * beta >= 5 minutes`.

PASS only if beta >0, CI lower >0, and +10pp model-implied difference >=5 minutes.

Classification:
- PASS -> `PASS_US_WATERWAY_E02_POSITIVE_MATERIAL_SIGNED_EXTREME_FLOW_DELAY_ASSOCIATION`
- positive detectable but submaterial -> `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E02`
- otherwise -> `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP`
- source/panel/inference failure -> `HOLD_US_WATERWAY_E02_SOURCE_PANEL_OR_INFERENCE_SUPPORT`.

**Persist the primary gate before calculating any sensitivity.**

## 9. Non-gate sensitivities

Only after primary fixation:
1. high-flow-only `Q > q90_g`;
2. low-flow-only `Q < q10_g`, preserving signed Q;
3. leave-one-gage-out beta range.

Sensitivities cannot rescue or alter primary.

## 10. Interpretation boundary

Observational contemporaneous annual association only. No causal, advance-prediction, propagation, novelty, ranking, operational-utility or optimal-threshold claim.

Incremental monetary cost: **0 USD**.
