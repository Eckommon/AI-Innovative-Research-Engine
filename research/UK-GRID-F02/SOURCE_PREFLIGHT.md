---
id: UK-GRID-F02-SOURCE-PREFLIGHT
type: boundary-identity-alignment-preflight
created: 2026-09-03
gate: PASS_UK_GRID_BOUNDARY_IDENTITY_READY
incremental_monetary_cost_usd: 0
---

# UK-GRID-F02 Source/Boundary Preflight / Source·Boundary 사전검증

**Gate / 게이트:** `PASS_UK_GRID_BOUNDARY_IDENTITY_READY`

## Outcome-blind execution boundary / 결과 비사용 실행경계

- Day-ahead source: schema plus `Constraint Group` and group-level min/max datetime/cardinality only.
- Thermal-cost source: schema plus `Constraint Group` and group-level min/max settlement-date/cardinality only.
- No observation-level `Limit (MW)`, `Flow (MW)`, or `Daily Cost (GBP)` values were requested or emitted.
- Identity matching used trim-whitespace-only exact source string equality; no fuzzy/manual boundary translation.

## Checks / 검증

| Check / 검증 | Result |
|---|---|
| Day-ahead CKAN public schema access | PASS |
| Thermal-cost CKAN public schema access | PASS |
| Day-ahead schema field Constraint Group | PASS |
| Day-ahead schema field Date (GMT/BST) | PASS |
| Day-ahead schema field Limit (MW) | PASS |
| Day-ahead schema field Flow (MW) | PASS |
| Thermal-cost schema field Settlement Date | PASS |
| Thermal-cost schema field Constraint Group | PASS |
| Thermal-cost schema field Daily Cost (GBP) | PASS |
| Day-ahead Constraint Group typed string | PASS |
| Thermal-cost Constraint Group typed string | PASS |
| Day-ahead Limit typed numeric | PASS |
| Day-ahead Flow typed numeric | PASS |
| Thermal Daily Cost typed numeric | PASS |
| Day-ahead non-null constraint groups returned | PASS |
| Thermal-cost non-null constraint groups returned | PASS |
| Exact normalized Constraint Group intersection non-empty | PASS |
| At least one exact common group overlaps on/after 2026-04-01 | PASS |
| Intended 2026 overlap is post-2024-04-22 methodology boundary | PASS |

## Diagnostics / 진단

- `dayahead_group_count`: `31`
- `dayahead_group_range_http_status`: `200`
- `dayahead_group_range_sha256`: `b50abce3b2005c57212b1f4358308b12d4273c08fa46ad91784cc5e07f042630`
- `dayahead_groups`: `BOLSELEX,BOLSELEX1,CANDUNEX,CANSELEX,DRESHEX1,DUNSELEX,ERROEX,ESTEX,ESTEX3,ESTEX4,FLOWSTH,GALLEX,GETEX,GM+SNOW5A,HARSPNBLY,NINSELEX,NKILGRMO,SCOTEX,SEIMP,SEIMPPR21,SEIMPPR23,SEIMPPR33,SHARN,SSE+GRMO,SSE-SP,SSE-SP2,SSEN-S,SSHARN,SSHARN3,SSHARN7,SWALEX`
- `dayahead_schema_http_status`: `200`
- `dayahead_schema_sha256`: `e4c6d627bc5cf0b22fdf911d6c27743badf0d33f91ed9e9928a18ee7eacd0e86`
- `exact_common_group_count`: `6`
- `exact_common_groups`: `ESTEX,SCOTEX,SEIMP,SSE-SP,SSHARN,SWALEX`
- `identity_normalization`: `trim_whitespace_only__exact_string_equality`
- `numerical_limit_flow_cost_observations_requested`: `False`
- `overlapping_common_group_count`: `2`
- `overlapping_common_groups`: `ESTEX:2026-04-01..2026-08-18;SCOTEX:2026-04-01..2026-08-18`
- `thermalcost_group_count`: `6`
- `thermalcost_group_range_http_status`: `200`
- `thermalcost_group_range_sha256`: `cf1b3e55300247efcc393d2aca9c013bb5a456e19423653baff9197e9cb32494`
- `thermalcost_groups`: `ESTEX,SCOTEX,SEIMP,SSE-SP,SSHARN,SWALEX`
- `thermalcost_schema_http_status`: `200`
- `thermalcost_schema_sha256`: `13da142be41e9cc62cb4cd006d8ca554629e65174d1bfd36960c6b2fcf30bf59`

## Source-method boundary / Source 방법론 경계

NESO documents that, from `2024-04-22`, Day Ahead Constraint Flows no longer consider expected constraint mitigation or optimisation actions. Any qualified 2026 overlap is therefore evaluated wholly within the post-change methodology regime.

## Claim boundary / 주장 경계

A PASS establishes exact source identity and time-join feasibility only. It does not establish that day-ahead headroom predicts, explains or causes realized thermal-constraint cost. No numerical relationship is evaluated here.

Incremental monetary cost remained **0 USD**.
