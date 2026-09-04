---
id: CA-RAIL-E01
type: preregistered-panel-association-experiment
state: PREREGISTERED_OUTCOME_BLIND
created: 2026-09-04
issue: 84
parent_candidate: C-CA-001
parent_feasibility: CA-RAIL-F01
decision: DEC-116
mission_anchor: MEM-054
weather_values_opened: false
rail_dwell_relationship_computed: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-E01 — Weekly Extreme-Cold × Intermodal Terminal-Dwell Experiment
# CA-RAIL-E01 — 주간 극한저온 × 인터모달 터미널 체류시간 실험

## 1. Research question / 연구 질문

Across the frozen 2024–2025 CN/CPKC intermodal terminal panel, are colder weekly extreme minimum temperatures associated with longer weekly intermodal terminal dwell?

This is an association experiment, not a causal design.

## 2. Why minimum temperature was selected before outcomes / 결과 이전 변수 선정 이유

The primary weather exposure is frozen as **ECCC daily Minimum Temperature (Min Temp, °C)**.

This choice is made before opening selected weather values because:
- Canadian railway safety/operations rules explicitly recognize temperature-dependent winter operating restrictions;
- current Canadian rail research identifies extreme cold as an operational constraint on braking, train length, speed and service capacity;
- ECCC provides daily minimum temperature as a standard historical-climate field;
- choosing raw minimum temperature avoids inventing a post-hoc cold threshold.

No snowfall, precipitation, wind, gust, mean temperature, maximum temperature or composite weather index may replace the primary variable after outcomes.

## 3. Frozen universe / 고정 universe

Parent support manifest:
`research/CA-RAIL-F01/FINAL_SUPPORT_KEYS.csv`

SHA-256:
`454bce3a77510cedbe4ff0f81cdc561500ec40462396e63f6f36ef8ebaf361e7`

Universe:
- 19 carrier-terminal series;
- CN and CPKC only;
- 105 Monday reporting weeks;
- maximum 1,995 carrier-terminal-week keys;
- 2024-01-01 through 2025-12-31;
- CPKC Thunder Bay remains prospectively excluded.

No support key can be added after Stage A begins.

## 4. Frozen rail outcome / 고정 rail outcome

Transport Canada source-defined measure:

**Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**

Frozen source dimensions:
- Carrier = CN or CPKC;
- Commodity = Intermodal containers;
- Car_Type = Not Applicable;
- Dwell_Time_Range = Not Applicable;
- Fleet_Status = Not Applicable;
- Employee_Type = Not Applicable;
- Segment_Distance_km = 0.0;
- Unit_of_Measure = Hours;
- Status_of_Value = 0 - Available.

Primary outcome:

`Y_i,t = log1p(DwellHours_i,t)`

A numeric zero remains valid. Blank/non-numeric dwell is missing and is never imputed.

## 5. Frozen weather exposure / 고정 weather exposure

For frozen ECCC station `s` and reporting week `t`:

`W_s,t = min(DailyMinTemp_s,d)`

over the seven days Monday through Sunday.

A daily minimum temperature is valid only if:
- `Min Temp (°C)` is numeric; and
- it is not an official missing/unknown-temperature observation such as M, N or Y.

Official estimated numeric observations such as E-coded values remain admissible; flags must be preserved in diagnostics.

A station-week is primary-qualified only when **7/7 daily minimum temperatures are valid**.

No threshold such as -25 °C is used in the primary predictor. The experiment tests the continuous weekly extreme minimum temperature.

## 6. Stage A — weather source integrity before relationship exposure

Stage A must run before Transport Canada dwell magnitudes are parsed for the association.

It must:
1. resolve each frozen ECCC Climate ID to the official historical-data download identity using the frozen station inventory;
2. retrieve only official ECCC daily data needed for 2024–2025;
3. record exact request/URL identity, access timestamp, bytes and SHA-256;
4. verify station/date/schema identity;
5. parse only the selected Min Temp field plus its flag for weather completeness;
6. construct the Monday–Sunday station-week qualification manifest;
7. persist source/hash/completeness diagnostics.

Stage A PASS requires:
- all 14 frozen ECCC station identities resolve deterministically;
- at least **90% of 14 × 105 station-weeks** satisfy 7/7 valid Min Temp;
- every frozen station has at least **90 qualified weeks**.

If not:

**`HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY`**

Stage B must not run.

No station, terminal, variable or completeness rule can be changed to rescue Stage A.

## 7. Stage B — one frozen primary model

For realized qualified carrier-terminal-week rows:

`log1p(Dwell_i,t) = beta * WeeklyMinTemp_s(i),t + alpha_i + gamma_t + epsilon_i,t`

where:
- `i` = frozen carrier-terminal series;
- `t` = frozen Monday reporting week;
- `s(i)` = frozen ECCC station;
- `alpha_i` = carrier-terminal fixed effects;
- `gamma_t` = reporting-week fixed effects.

No lag, lead, seasonal subset, nonlinear threshold, interaction, carrier trend or alternate weather variable is permitted.

## 8. Frozen inference / 고정 추론

Cluster on:
**ECCC Climate ID**.

Use one-way CR1 covariance:

`V_CR1 = V_CR0 * [G/(G-1)] * [(N-1)/(N-K)]`

where:
- `G` = realized ECCC station clusters;
- `N` = realized panel rows;
- `K` = fitted design rank/column count.

Primary 95% CI:

`beta ± t_(0.975,G-1) * SE_CR1`

Primary two-sided p-value uses `G-1` degrees of freedom.

Stage-B integrity requires:
- at least **90% of the 1,995 frozen carrier-terminal-week keys** remain after source completeness and rail numeric parsing;
- at least **12 ECCC station clusters** remain;
- the design matrix is full rank;
- outcome and predictor values are finite.

## 9. Frozen hypothesis and gate / 고정 가설·게이트

Because the predictor is temperature in °C:

**H1: beta < 0**

A negative beta means a warmer weekly extreme minimum is associated with lower dwell; equivalently, colder weekly extremes are associated with higher dwell.

### PASS

**`PASS_CA_RAIL_E01_EXTREME_COLD_DWELL_ASSOCIATION`**

only if:
- Stage A/B integrity passes;
- `beta < 0`; and
- the upper endpoint of the frozen two-sided 95% station-clustered CI is below zero.

### NO

**`NO_CA_RAIL_E01_EXTREME_COLD_DWELL_ASSOCIATION`**

if integrity passes but the PASS condition is not met.

### HOLD

**`HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY`**

if the frozen experiment cannot be executed without prohibited alteration.

## 10. Source revision / reproducibility contract

Transport Canada:
- use the F01-frozen ZIP only if its SHA-256 remains exactly
  `e29cd33ea9e65601b4945b7d196cef0fbd539831377a7666ce0ea65886dfd088`;
- otherwise fail closed and version the source rather than silently replacing it.

ECCC:
- Stage A must pin exact daily-data request/response hashes;
- historical climate values may be retrospectively revised under quality control;
- all Stage-B weather values must come from one Stage-A manifest version;
- no silent source replacement.

## 11. Interpretation boundary / 해석 경계

A PASS would support only:

**a preregistered negative association between weekly extreme minimum temperature and intermodal terminal dwell in the frozen official-source panel.**

It would not establish:
- causality;
- a -25 °C threshold effect;
- snow/wind/precipitation effects;
- terminal-specific vulnerability rankings;
- carrier superiority;
- exact yard-level weather exposure;
- policy or investment superiority.

A NO would not prove that weather is irrelevant to rail operations; it would mean this one preregistered minimum-temperature/dwell construct did not meet its gate.

## 12. Cost / 비용

Incremental monetary cost remains **0 USD**.
