---
id: US-AIR-E01-STAGE-B-RESULT
type: preregistered-primary-relationship-result
created: 2026-09-10
issue: 90
gate: PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION
relationship_outcome_computed: true
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 Stage B Result
# US-AIR-E01 Stage B 결과

## Source-integrity barrier / source 무결성 장벽

- BTS 2025 PREZIP exact hash matches: **12/12**
- All twelve hashes were verified before any ZIP CSV member was opened.
- parsed BTS identity/outcome source rows after hash PASS: **7,736,770**
- rows belonging to the frozen Stage-A weather cohort: **6,726,149**
- negative eligible DepDelayMinutes rows: **0**
- non-finite/unparsed nonblank delay rows: **0**
- monthly header consistency: **True**

## Realized frozen panel / 실현 고정 panel

- airport-date observations: **91,687**
- unique airports: **255**
- unique FlightDate levels: **365**
- full parameter count used for CR1 correction K: **621**
- FE alternating-projection iterations: **8**
- final FE max absolute change: **9.104e-15**

Frozen support minimums >=100 airports and >=30,000 airport-days are satisfied.

## Primary preregistered result / 주결과

Model: airport FE + FlightDate FE + log1p(scheduled departures) + log1p(DailyPrecipitation_mm).

- beta on log1p precipitation: **4.892129968812 minutes**
- two-way CR1 SE (AirportID, FlightDate): **0.291257725833**
- t: **16.796567**
- df: **254**
- two-sided p: **4.30645849183e-43**
- 95% CI: **[4.318542282873, 5.465717654751]**
- model-implied 0 mm to 10 mm difference beta*ln(11): **11.730815 minutes**
- scheduled-volume coefficient gamma: **5.326426281902**

### Descriptive baseline comparison / 기술적 baseline 비교

- baseline within-RMSE: **36.906107 minutes**
- weather-model within-RMSE: **36.666737 minutes**

RMSE is descriptive and is not a PASS gate.

## Primary gate / 주 판정

**PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION**

The gate was adjudicated before the prespecified sensitivities were run.

## Prespecified non-gate sensitivities / 사전 sensitivity

- **S1_TRACE_0_1MM**: status=OK, beta=4.948700792523204, SE=0.2931940308122592, 95% CI=[4.371299849136134, 5.526101735910274], delta_10mm=11.866466236884941
- **S2_EXCLUDE_DIVERTED**: status=OK, beta=4.870090114802776, SE=0.28765092093551625, 95% CI=[4.3036054812166356, 5.436574748388917], delta_10mm=11.677966064387652
- **S3_CLUSTER_AIRPORT_ISO_WEEK**: status=OK, beta=4.892129968812057, SE=0.29214568791272755, 95% CI=[4.305896757549434, 5.47836318007468], delta_10mm=11.730815326129672

Sensitivity results do not alter or rescue the primary gate.

## Interpretation boundary / 해석 경계

This is a preregistered contemporaneous association test. It is not advance prediction, causal inference, network propagation, airport/carrier ranking, novelty validation, operational utility validation, investment advice or policy superiority.

## Durable outputs / 영속 산출물

- research/US-AIR-E01/STAGE_B_BTS_SOURCE_MANIFEST.csv
- research/US-AIR-E01/STAGE_B_AIRPORT_DAY_PANEL.csv
- research/US-AIR-E01/STAGE_B_PRIMARY_RESULT.csv
- research/US-AIR-E01/STAGE_B_SENSITIVITY_RESULT.csv
- research/US-AIR-E01/STAGE_B_RESULT.md

- Python/numpy/scipy: 2.5.3 / scipy-module

Raw BTS ZIP/CSV bytes were transient and are not persisted.

Incremental monetary cost remains **0 USD**.
