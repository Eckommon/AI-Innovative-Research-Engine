---
id: UK-GRID-F01-RESULT
type: cross-dataset-alignment-feasibility-result
state: COMPLETED_PASS
created: 2026-09-03
parent: UK-GRID-F01
issue: 68
gate: PASS_UK_GRID_DAILY_ALIGNMENT_READY
incremental_monetary_cost_usd: 0
---

# UK-GRID-F01 Result — NESO Constraint × Demand/Renewables Daily Alignment
# UK-GRID-F01 결과 — NESO 계통제약 × 수요·재생에너지 일별 정렬

## Final gate / 최종 게이트

**`PASS_UK_GRID_DAILY_ALIGNMENT_READY`**

## What was demonstrated / 검증된 내용

The outcome-blind preflight established that the selected current NESO resources can be deterministically aligned to a daily independent unit without opening the selected FY2026-27 numerical constraint outcomes.

선정된 현행 NESO resource는 FY2026-27의 실제 수치형 제약 outcome을 열지 않은 상태에서 결정론적으로 일별 독립단위에 정렬할 수 있음이 검증되었다.

### Frozen resources / 고정 resource
- Constraint Breakdown 2026-2027: `4136a8e2-07c5-4784-8096-28999447a16e`
- Historic Demand Data 2026: `8a4a771c-3929-4e56-93ad-cdf13219dea5`

### Passed checks / 통과 검증
- both public CKAN schemas accessible;
- all frozen constraint cost/volume fields present;
- `Thermal constraints cost` typed numeric;
- all frozen historic-demand state fields present;
- constraint `Date` unique at daily unit;
- demand `(SETTLEMENT_DATE, SETTLEMENT_PERIOD)` pairs unique;
- daily settlement-period counts compatible with `{46,48,50}`;
- exact date overlap exists on/after `2026-04-01`;
- every overlap date has one constraint record and an allowed settlement-period count.

## Structural diagnostics / 구조 진단

- constraint date records: `140`
- constraint unique dates: `140`
- constraint coverage: `2026-04-01` → `2026-08-18`
- demand date/period rows: `10798`
- demand unique dates: `225`
- demand coverage: `2026-01-01` → `2026-08-13`
- observed daily period-count set: `{46,48}`
- qualified overlap: `135` days
- overlap window: `2026-04-01` → `2026-08-13`

## Outcome-blind integrity / 결과 비사용 무결성

No selected FY2026-27 constraint cost/volume observations were requested or emitted during F01.

No demand/wind/solar/interconnector numerical system-state observations were requested or emitted during F01.

The first harness attempt returned `HTTP 409 Conflict` when using `fields=` projection. `AMENDMENT-01` corrected only the query mechanism to official NESO `datastore_search_sql`; the scientific contract and numerical non-exposure boundary were unchanged.

## Version/correction boundary / 버전·정정 경계

NESO states that Constraint Breakdown may be refreshed when post-event action tags change. Historic Demand is populated 21 days in arrears and may receive retrospective solar and demand corrections.

Therefore any future numerical experiment must freeze:
- UTC extraction timestamp;
- exact resource IDs;
- exact response/download hashes;
- final evaluation window;
- maturity/correction rule before numerical analysis.

## Claim boundary / 주장 경계

F01 validates **source/schema/time alignment feasibility only**.

It does **not** establish that national demand, renewable generation, interconnector flows or any other system-state variable explains, predicts or causes transmission-constraint costs.

## Mission-ROI implication / 미션-ROI 함의

A direct daily join is now a validated reusable asset. However, forcing a national-demand association merely because the join is available would be scientifically weak. Before consuming the one authorized low-DOF experiment, the project should prefer a more direct source-defined bottleneck construct if available.

Current official NESO data provides a higher-value candidate: `Day Ahead Constraint Flows and Limits`, which measures boundary-specific flow and limit at half-hourly resolution and can potentially be joined to boundary-specific daily thermal-constraint cost. This route is separately qualified under `UK-GRID-F02`; F01 itself remains closed PASS.

## Cost / 비용

Incremental monetary cost remained **0 USD**.
