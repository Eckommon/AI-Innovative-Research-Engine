# US-WATERWAY-E01 Stage B Implementation Contract

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
