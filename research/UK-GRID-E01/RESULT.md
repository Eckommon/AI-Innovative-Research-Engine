---
id: UK-GRID-E01-RESULT
type: controlled-cross-dataset-experiment-result
created: 2026-09-03
gate: HOLD_E01_SOURCE_CARDINALITY
issue: 70
incremental_monetary_cost_usd: 0
---

# UK-GRID-E01 Result — SCOTEX Stress × Thermal Cost
# UK-GRID-E01 결과 — SCOTEX Stress × Thermal Cost

**Final gate / 최종 게이트:** `HOLD_E01_SOURCE_CARDINALITY`

## Frozen contract / 고정 계약

- Boundary: `SCOTEX` (selected outcome-blind).
- Window: `2026-04-01` → `2026-07-31`, exactly 122 calendar days.
- Predictor: daily maximum of signed `Flow / Limit` across exactly 48 half-hours.
- Outcome: explicit same-day SCOTEX `Daily Cost (GBP)`.
- Primary statistic: Spearman rho plus all-122 circular-shift one-sided temporal-alignment p-value.
- PASS threshold: `rho >= 0.30` and `p_circ <= 0.05`.

## Stage A — structural gate / 구조 gate

- Stage A pass: `False`
- exact 122 day-ahead dates: `PASS`
- exact 5,856 day-ahead structural rows: `FAIL`
- exactly 48 day-ahead rows per date: `FAIL`
- 48 unique day-ahead timestamps per date: `FAIL`
- no duplicate day-ahead datetime: `PASS`
- exact 122 thermal-cost dates: `PASS`
- exact 122 thermal-cost structural rows: `PASS`
- one explicit thermal-cost record per date: `PASS`

### Stage A diagnostics / Stage A 진단

- `dayahead_identifier_http_status`: `200`
- `dayahead_identifier_response_sha256`: `6c381c7e37f74095b6bff0605ac00d827e932257dd11935263ca644e2e7bea0b`
- `dayahead_per_day_row_count_set`: `[38, 48]`
- `dayahead_per_day_unique_timestamp_count_set`: `[38, 48]`
- `dayahead_structural_row_count`: `5846`
- `dayahead_unique_date_count`: `122`
- `expected_cost_rows`: `122`
- `expected_date_count`: `122`
- `expected_dayahead_rows`: `5856`
- `expected_halfhours_per_date`: `48`
- `numerical_flow_limit_cost_requested`: `False`
- `stage`: `A`
- `thermalcost_identifier_http_status`: `200`
- `thermalcost_identifier_response_sha256`: `73156604f7fcf7f3de506051845ef679a4964f0cfab431e5a2071879749e53d5`
- `thermalcost_per_date_count_set`: `[1]`
- `thermalcost_structural_row_count`: `122`
- `thermalcost_unique_date_count`: `122`

## Primary and secondary aggregate results / 1차·2차 집계 결과

- Numerical aggregate metrics: `NOT_AVAILABLE_UNDER_FINAL_GATE`

### Stage B diagnostics / Stage B 진단

- `numerical_query_executed`: `False`

## Interpretation boundary / 해석 경계

This experiment tests a bounded temporal operational association between source-defined day-ahead SCOTEX boundary stress and same-day realized SCOTEX thermal-constraint cost. It does not establish causality, isolate Scottish wind as a sole driver, equate every operational Limit with one immutable circuit rating, or generalize to other boundaries/years/systems.

Raw half-hour/day observations are not persisted in this public result. Exact numerical-query response hashes and extraction timestamp are retained when Stage B executes.

## Portfolio rule / 포트폴리오 규칙

Under `MEM-054` and `DEC-093`, E01 closes after this single frozen execution regardless of PASS/PARTIAL/NO/HOLD. The next step is Stage 0 Mission-ROI portfolio review, not automatic same-branch retuning.

Incremental monetary cost remained **0 USD**.
