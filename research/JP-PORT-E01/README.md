---
id: JP-PORT-E01
type: preregistered-controlled-panel-experiment
created: 2026-09-04
issue: 80
state: PREREGISTERED_OUTCOME_BLIND
parent: JP-PORT-F01
decision: DEC-111
weather_relationship_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 — Monthly Extreme Wind × Port Cargo Panel Experiment
# JP-PORT-E01 — 월별 극대풍속 × 항만 화물 패널 실험

## 1. Primary question / 주 질문

Across the prospectively frozen Japanese port universe, is stronger monthly extreme wind at the matched JMA station associated with lower monthly total maritime cargo at the port, after controlling for fixed port differences and common year-month conditions?

This is an association experiment, not a causal attribution study.

## 2. Frozen source universe / 고정 source universe

### MLIT / e-Stat
Use only the six hashed mature annual Port Survey workbooks:
2019 through 2024.

Use exactly the source identities and hashes frozen in:
`research/JP-PORT-F01/FINAL_SUPPORT_PREFLIGHT.md`.

### JMA
Historical observation source:
`https://www.data.jma.go.jp/risk/obsdl/`

Use only the F01-frozen 149 port→station mappings.

No mapping may be changed after JMA values are opened.

## 3. Frozen panel / 고정 패널

Potential calendar support:
**2019-01 through 2024-12 = 72 months**.

Potential port universe:
**149 ports**.

The realized eligible panel is determined only by the preregistered Stage A quality/completeness rules.

The same JMA station can serve multiple ports:
- 149 port mappings;
- 131 unique station IDs;
- 16 station IDs shared by 34 port mappings.

These are not 149 independent weather series.

## 4. Primary predictor / primary 설명변수

Daily JMA element:
**日最大風速 / daily maximum wind speed, m/s**.

For station s and calendar month t:

`W_s,t = max(valid daily maximum wind speed)`

where valid means:
- JMA quality code = 8;
- same accepted homogeneity regime under Stage A;
- date belongs to calendar month t.

No gust-speed, rainfall, temperature, direction, exceedance-day count or thresholded wind variable is co-primary.

## 5. Weather completeness / 기상 완전성

For each station-month:
- required valid quality-8 days:
  **ceil(0.90 × number of calendar days in that month)**.
- if below the threshold, predictor is missing;
- no interpolation/imputation;
- no substitution from a neighboring station.

If Stage A reveals multiple homogeneity numbers for the selected wind element within 2019–2024 for a station, all descendant rows using that station are excluded before Stage B.

## 6. Primary outcome / primary 결과

For port p and month t:

`Y_p,t = log(1 + Cargo_p,t)`

where `Cargo_p,t` is:
- MLIT sheet `海上出入貨物`;
- port row `種別=計`;
- monthly `合計` column;
- source `トン数` unit.

Blank/non-numeric cells are missing.
Numeric zero is a valid zero.

The source freight-ton convention is preserved; the result is not labeled pure physical mass.

## 7. Primary model / 주 모델

`Y_p,t = beta W_s(p),t + alpha_p + gamma_t + epsilon_p,t`

where:
- `alpha_p` = port fixed effect;
- `gamma_t` = year-month fixed effect for each calendar month in 2019–2024;
- `s(p)` = frozen JMA station assigned to port p.

Primary standard errors:
**cluster-robust by JMA station ID**.

No cargo-volume weights.

Primary directional hypothesis:
`beta < 0`.

## 8. Primary gate / 주 판정

### PASS
**`PASS_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION`**

if:
1. Stage A integrity PASS;
2. model is estimable under the frozen panel;
3. `beta < 0`;
4. two-sided 95% station-clustered confidence interval is entirely below zero.

### NO
**`NO_E01_NEGATIVE_EXTREME_WIND_CARGO_ASSOCIATION`**

if Stage A/model integrity pass but the PASS condition is not met.

### HOLD
**`HOLD_E01_SOURCE_OR_PANEL_INTEGRITY`**

if source, identity, homogeneity, completeness, duplicate or estimability rules fail.

No alternate weather variable may rescue NO/HOLD inside E01.

## 9. Effect-size interpretation / 효과크기

Report:
- beta in log1p cargo units per +1 m/s monthly extreme wind;
- the model-implied cargo change for a fixed **+5 m/s** contrast as a descriptive effect-size translation.

The +5 m/s translation is descriptive only and is **not an additional PASS threshold**.

Statistical significance does not establish operational materiality or causality.

## 10. Stage A / source integrity

Stage A must occur before any weather-throughput relationship statistic.

It must:
1. retrieve only JMA daily maximum-wind data for the frozen station universe/date window;
2. batch requests conservatively within JMA request limits;
3. retain value, date, quality and homogeneity metadata;
4. pin every raw CSV SHA-256;
5. verify station IDs and date coverage;
6. apply quality=8 and 90% month completeness;
7. exclude homogeneity-broken stations without remapping;
8. re-verify all six frozen MLIT source hashes;
9. verify one unique port-total row per qualified port/source year;
10. persist an eligible panel-key manifest before Stage B.

Stage A may read weather values only for the frozen variable because the preregistration is already committed. It must not calculate the primary relationship.

## 11. Stage B / numerical experiment

Only after Stage A PASS:
1. aggregate daily maximum wind to monthly maximum;
2. extract monthly total maritime cargo;
3. calculate log1p outcome;
4. fit exactly the frozen fixed-effects model;
5. compute station-clustered 95% confidence interval;
6. apply the frozen gate;
7. persist result and return to mandatory Stage 0 after completion.

## 12. Bounded diagnostics / 제한 진단

Allowed after the primary result, without changing the gate:
- number of eligible port-months;
- port/station/month coverage counts;
- residual/model numerical-integrity diagnostics;
- descriptive +5 m/s effect translation.

Not preregistered as alternative hypothesis tests:
- precipitation;
- temperature;
- gust speed;
- wind direction;
- lag/lead variants;
- port-specific sensitivity coefficients;
- alternate distance caps;
- alternate completeness thresholds.

## 13. Scientific boundary / 과학적 경계

A PASS would establish a reproducible **association** between monthly station-level extreme wind and port-level monthly cargo in the frozen panel.

It would not establish:
- causal weather disruption;
- exact terminal-level exposure;
- physical tonnage loss;
- port resilience rankings;
- investment or policy superiority.

## 14. Cost / 비용

Incremental monetary cost remains **0 USD**. Any potentially billable work requires explicit prior approval.
