---
id: US-AIR-E01-STAGE-B-IMPLEMENTATION-CONTRACT
type: preregistered-implementation-contract
created: 2026-09-10
issue: 90
state: FROZEN_BEFORE_DELAY_MAGNITUDES
parent_decisions:
  - DEC-124
  - DEC-125
primary_result_opened: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 Stage B Implementation Contract
# US-AIR-E01 Stage B 구현 계약

## Purpose / 목적

Freeze the remaining numerical implementation choices **before any BTS `DepDelayMinutes` magnitude is parsed**. This file implements DEC-124 without changing its scientific question, predictor, outcome, denominator, panel thresholds or PASS gate. / BTS 지연값을 열기 전에 남은 수치 구현 선택을 고정한다.

## 1. Source-integrity barrier / source 무결성 장벽

Stage B shall first download all twelve official BTS 2025 Marketing Carrier On-Time PREZIP archives to transient storage.

Before opening any CSV member or parsing any outcome magnitude:

1. recover the twelve expected SHA-256 values from `research/US-AIR-F01/FULL_YEAR_DATE_SUPPORT.md`;
2. compute SHA-256 for all twelve newly downloaded ZIP byte streams;
3. require **12/12 exact hash equality**.

If any hash differs:
- do not open the ZIP CSV members;
- persist the observed/expected hash manifest;
- resolve to `HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT` with reason `BTS_SOURCE_SNAPSHOT_DRIFT`;
- return to Stage 0 without source substitution.

Raw ZIP/CSV bytes remain transient under RAW-001.

## 2. Frozen Stage-A cohort / 고정 Stage-A cohort

Use only rows from `STAGE_A_AIRPORT_DATE_WEATHER.csv` satisfying:

- `stage_a_airport_qualified == True`;
- `usable_primary == True`;
- one deterministic `AirportID × FlightDate` key.

No weather or outcome criterion may otherwise add/remove an airport-day.

Primary trace rule remains `T = 0.0 mm`; the 0.1 mm trace encoding is sensitivity only.

## 3. BTS parsing after 12/12 hash PASS / hash PASS 후 BTS parsing

Read only these BTS fields:

- `FlightDate`;
- `OriginAirportID`;
- `Duplicate`;
- `Cancelled`;
- `Diverted`;
- `DepDelayMinutes`.

Do not read `WeatherDelay`, arrival-delay fields, carrier performance fields, or other weather-attribution outcomes.

### Scheduled-volume denominator

For each Stage-A airport-date:

`N_sched_ad` = count of BTS rows with `Duplicate != Y/true/1`, regardless of cancellation/diversion status.

### Primary delay outcome

A row is eligible for `Y_ad` only when:
- not Duplicate;
- `Cancelled != 1`;
- `DepDelayMinutes` is nonblank and finite.

Non-cancelled Diverted rows remain eligible.

If any eligible `DepDelayMinutes < 0`, stop with `HOLD_INFERENCE_OR_SOURCE_SEMANTICS` rather than silently truncating.

`Y_ad` = arithmetic mean of eligible `DepDelayMinutes`.

No winsorization, weighting, imputation or outcome transform.

## 4. Realized panel gate / 실현 panel gate

Keep a Stage-B airport-day only if:
- it belongs to the frozen Stage-A usable cohort;
- `N_sched_ad > 0`;
- at least one primary-outcome-eligible departure exists.

Before fitting or interpreting `beta`, require:
- **>=100 unique AirportIDs**;
- **>=30,000 airport-date rows**.

Otherwise resolve to `HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT`.

## 5. Fixed-effects implementation / 고정효과 구현

Let:
- `y = Y_ad`;
- `v = log1p(N_sched_ad)`;
- `x = log1p(DailyPrecipitation_mm_ad)`.

Absorb AirportID and FlightDate fixed effects by iterative alternating projection:

1. subtract within-AirportID means;
2. subtract within-FlightDate means;
3. repeat in that order until the maximum absolute change across all residualized columns is **< 1e-12**;
4. maximum iterations = **1,000**.

Residualize `y`, `v`, and `x` jointly with the same group structure. Failure to converge is `HOLD_INFERENCE_DEGENERATE`.

After absorption, fit by ordinary least squares with **no intercept**:

Baseline:
`y_tilde = gamma * v_tilde + error`

Weather model:
`y_tilde = gamma * v_tilde + beta * x_tilde + error`

Require full column rank:
- baseline rank = 1;
- weather-model rank = 2.

Rank deficiency or a non-finite coefficient is `HOLD_INFERENCE_DEGENERATE`.

## 6. Primary two-way CR1 covariance / primary two-way CR1 공분산

For the weather model only, define:

`B = (X'X)^(-1)`.

For any clustering partition `g`, cluster score:
`s_g = X_g' u_g`.

Cluster meat:
`M_g = sum_g s_g s_g'`.

CR1 correction:
`c_g = [G/(G-1)] * [(N-1)/(N-K)]`.

Primary model full-parameter count:
`K = A + D + 1`,
where:
- `A` = number of AirportID levels;
- `D` = number of FlightDate levels;
- +1 reflects two slopes plus intercept-equivalent FE parameterization: `1 + (A-1) + (D-1) + 2 = A + D + 1`.

Compute:
- `V_airport = B * c_airport M_airport * B`;
- `V_date = B * c_date M_date * B`;
- `V_intersection = B * c_intersection M_intersection * B`, where intersection clusters are AirportID×FlightDate and therefore one realized airport-day each;
- **`V_primary = V_airport + V_date - V_intersection`**.

Do not project or clip the covariance matrix to positive semidefinite form.

If the precipitation-slope variance is <=0 or non-finite, resolve to `HOLD_INFERENCE_DEGENERATE`.

Primary t degrees of freedom:
**`df = min(G_airport - 1, G_date - 1)`**.

Primary 95% CI:
`beta ± t_(0.975, df) * SE_beta`.

Primary two-sided p-value uses the same t distribution.

## 7. Primary gate / primary 판정

Compute before any sensitivity:

`delta_10mm = beta * ln(11)`.

Adjudicate exactly:

1. if source/panel/inference integrity fails → `HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT` (or the more specific HOLD reason in diagnostics);
2. else if `beta > 0`, 95% CI lower > 0, and `delta_10mm >= 1.0 minute` → `PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION`;
3. else if `beta > 0` and 95% CI lower > 0 but `delta_10mm < 1.0 minute` → `DETECTABLE_BUT_SUBMATERIAL_US_AIR_E01`;
4. else → `NO_PREREGISTERED_POSITIVE_US_AIR_E01_RELATIONSHIP`.

Baseline and weather-model in-sample RMSE may be reported descriptively. RMSE improvement is **not a gate**.

## 8. Prespecified non-gate sensitivities / 사전 sensitivity

Run only after the primary gate has been computed and stored in memory:

### S1 — trace encoding
Refit the exact primary model after changing only Stage-A trace rows from `0.0` to `0.1 mm`.

### S2 — diverted exclusion
Rebuild `Y_ad` using the same rows/rules but additionally exclude `Diverted = 1`; retain the same frozen Stage-A weather cohort. Report realized row-count changes.

### S3 — dependence stress test
Use the **primary coefficients and residuals** but replace primary covariance clusters with:
- AirportID;
- ISO calendar week `YYYY-Www`;
- intersection AirportID×ISO-week.

Use the same cluster-meat and CR1 formula. Full parameter count remains `K=A+D+1` because the fitted FE model is unchanged. Degrees of freedom = `min(G_airport-1, G_week-1)`.

Sensitivity results cannot alter or rescue the primary gate.

## 9. Reproducibility outputs / 재현 산출물

Persist:
- 12-month BTS source-integrity hash manifest;
- realized Stage-B airport-day panel;
- one-row primary result CSV;
- sensitivity result CSV;
- human-readable Stage-B result;
- executable runner and runtime package versions.

Do not persist raw BTS archives.

## 10. Interpretation boundary / 해석 경계

Even a primary PASS is only a preregistered contemporaneous association. It does not establish:
- advance prediction;
- causality;
- delay propagation;
- airport/carrier ranking;
- a precipitation threshold;
- novelty;
- operational/commercial utility;
- investment or policy superiority.

Incremental monetary cost remains **0 USD**.
