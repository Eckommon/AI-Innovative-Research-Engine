---
id: UK-GRID-F01-SOURCE-PREFLIGHT
type: schema-date-alignment-preflight
created: 2026-09-03
gate: PASS_UK_GRID_DAILY_ALIGNMENT_READY
incremental_monetary_cost_usd: 0
---

# UK-GRID-F01 Source/Alignment Preflight / Source·정렬 사전검증

**Gate / 게이트:** `PASS_UK_GRID_DAILY_ALIGNMENT_READY`

## Outcome-blind execution boundary / 결과 비사용 실행경계

- FY2026-27 constraint API: schema metadata + `Date` only.
- Historic Demand 2026 API: schema metadata + `SETTLEMENT_DATE` + `SETTLEMENT_PERIOD` only.
- Projected rows use official NESO `datastore_search_sql` after `AMENDMENT-01` corrected a `fields=` query-harness incompatibility.
- No FY2026-27 constraint cost/volume values were requested or emitted.
- No demand/wind/solar/interconnector numerical values were requested or emitted.

## Checks / 검증

| Check / 검증 | Result |
|---|---|
| Constraint CKAN public schema access | PASS |
| Demand CKAN public schema access | PASS |
| Constraint schema field Date | PASS |
| Constraint schema field Reducing largest loss cost | PASS |
| Constraint schema field Increasing system inertia cost | PASS |
| Constraint schema field Voltage constraints cost | PASS |
| Constraint schema field Thermal constraints cost | PASS |
| Constraint schema field Reducing largest loss volume | PASS |
| Constraint schema field Increasing system inertia volume | PASS |
| Constraint schema field Voltage constraints volume | PASS |
| Constraint schema field Thermal constraints volume | PASS |
| FY2026-27 Thermal constraints cost typed numeric | PASS |
| Demand schema field SETTLEMENT_DATE | PASS |
| Demand schema field SETTLEMENT_PERIOD | PASS |
| Demand schema field ND | PASS |
| Demand schema field TSD | PASS |
| Demand schema field EMBEDDED_WIND_GENERATION | PASS |
| Demand schema field EMBEDDED_SOLAR_GENERATION | PASS |
| Demand schema field IFA_FLOW | PASS |
| Demand schema field IFA2_FLOW | PASS |
| Demand schema field BRITNED_FLOW | PASS |
| Demand schema field MOYLE_FLOW | PASS |
| Demand schema field EAST_WEST_FLOW | PASS |
| Demand schema field NEMO_FLOW | PASS |
| Demand schema field NSL_FLOW | PASS |
| Demand schema field ELECLINK_FLOW | PASS |
| Demand schema field VIKING_FLOW | PASS |
| Demand schema field GREENLINK_FLOW | PASS |
| Constraint date-only SQL request returned rows | PASS |
| Constraint Date unique at daily unit | PASS |
| Demand date/settlement-period SQL request returned rows | PASS |
| Demand (date, settlement period) pairs unique | PASS |
| Daily settlement-period counts compatible with 46/48/50 | PASS |
| Non-empty daily overlap from 2026-04-01 onward | PASS |
| Every overlap date has one constraint record | PASS |
| Every overlap date has allowed settlement-period count | PASS |

## Diagnostics / 진단

- `constraint_date_count`: `140`
- `constraint_date_http_status`: `200`
- `constraint_date_response_sha256`: `c62c0b554cb1a2cb479cf7937e312d9cd41e84f7d645ecbcc9f18546c9c376ca`
- `constraint_max_date`: `2026-08-18`
- `constraint_min_date`: `2026-04-01`
- `constraint_numerical_outcomes_requested`: `False`
- `constraint_projection_method`: `datastore_search_sql__Date_only`
- `constraint_schema_http_status`: `200`
- `constraint_schema_sha256`: `3d51e94996407527b2e91cc464a43a4a3c98946ccc38e688aa5c15fe6b718ef2`
- `constraint_unique_date_count`: `140`
- `date_normalization`: `ISO_calendar_date_first_10_chars_validated`
- `demand_date_period_http_status`: `200`
- `demand_date_period_response_sha256`: `62ab3673ab2ffba51814a95e9866e0c23b270173d436530c3d26e9a7bee4a47c`
- `demand_date_period_row_count`: `10798`
- `demand_max_date`: `2026-08-13`
- `demand_min_date`: `2026-01-01`
- `demand_numerical_system_state_requested`: `False`
- `demand_period_count_set`: `46,48`
- `demand_projection_method`: `datastore_search_sql__date_period_only`
- `demand_schema_http_status`: `200`
- `demand_schema_sha256`: `5c6e921301d60834c594999d0fb7a9983058cc0b3568b05ec546b1ef5e945012`
- `demand_unique_date_count`: `225`
- `overlap_date_count`: `135`
- `overlap_max_date`: `2026-08-13`
- `overlap_min_date`: `2026-04-01`

## Correction/version boundary / 수정·버전 경계

NESO documents that Constraint Breakdown may be refreshed when post-event action tags change. Historic Demand is populated 21 days in arrears and may receive retrospective solar/demand corrections. A later experiment must therefore freeze extraction UTC timestamp, exact resource IDs, raw/query response hashes, an evaluation window and a maturity rule before numerical outcome access.

## Claim boundary / 주장 경계

A PASS establishes daily source/time alignment feasibility only. It does not establish that system-state variables explain or predict constraint costs, nor does it establish causal transmission bottleneck drivers.

Incremental monetary cost remained **0 USD**.
