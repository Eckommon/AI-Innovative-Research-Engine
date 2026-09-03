---
id: UK-GRID-F01-SOURCE-PREFLIGHT
type: schema-date-alignment-preflight
created: 2026-09-03
gate: PARTIAL_UK_GRID_SCHEMA_READY__DATE_ALIGNMENT_PENDING
incremental_monetary_cost_usd: 0
---

# UK-GRID-F01 Source/Alignment Preflight / Source·정렬 사전검증

**Gate / 게이트:** `PARTIAL_UK_GRID_SCHEMA_READY__DATE_ALIGNMENT_PENDING`

## Outcome-blind execution boundary / 결과 비사용 실행경계

- FY2026-27 constraint API: schema metadata + `Date` only.
- Historic Demand 2026 API: schema metadata + `SETTLEMENT_DATE` + `SETTLEMENT_PERIOD` only.
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

## Diagnostics / 진단

- `constraint_schema_http_status`: `200`
- `constraint_schema_sha256`: `3d51e94996407527b2e91cc464a43a4a3c98946ccc38e688aa5c15fe6b718ef2`
- `demand_schema_http_status`: `200`
- `demand_schema_sha256`: `5c6e921301d60834c594999d0fb7a9983058cc0b3568b05ec546b1ef5e945012`
- `exception_message`: `HTTP Error 409: Conflict`
- `exception_type`: `HTTPError`

## Correction/version boundary / 수정·버전 경계

NESO documents that Constraint Breakdown may be refreshed when post-event action tags change. Historic Demand is populated 21 days in arrears and may receive retrospective solar/demand corrections. A later experiment must therefore freeze extraction UTC timestamp, exact resource IDs, raw/query response hashes, an evaluation window and a maturity rule before numerical outcome access.

## Claim boundary / 주장 경계

A PASS establishes daily source/time alignment feasibility only. It does not establish that system-state variables explain or predict constraint costs, nor does it establish causal transmission bottleneck drivers.

Incremental monetary cost remained **0 USD**.
