---
id: UK-GRID-F01
type: cross-dataset-alignment-feasibility-gate
state: PREREGISTERED
created: 2026-09-03
parent_candidate: C-UK-001
portfolio_decision: DEC-098
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# UK-GRID-F01 — NESO Constraint × Demand/Renewables Alignment Feasibility
# UK-GRID-F01 — NESO 계통제약 × 수요·재생에너지 정렬 실행가능성

## 1. Purpose / 목적

Before any association, prediction, thresholding or ranking, determine whether current public NESO resources support a deterministic **daily GB system-state × daily transmission-constraint outcome** join.

연관분석·예측·threshold·순위화 전에 현행 공개 NESO 자료가 결정론적 **일별 GB 계통상태 × 일별 송전제약 outcome** 조인을 지원하는지 검증한다.

This is a source/schema/time-alignment gate only. / 본 단계는 source·schema·시간정렬 검증만 수행한다.

## 2. Frozen official resources / 고정 공식 resource

### A. Constraint outcome / 제약 outcome
NESO `Constraint Breakdown 2026-2027`:
- CKAN resource ID: `4136a8e2-07c5-4784-8096-28999447a16e`;
- frequency: daily records / dataset updated weekly;
- official categories: reducing largest loss, increasing system inertia, voltage, thermal;
- costs in GBP and volumes in MWh;
- source-defined thermal constraint: actions taken when natural energy flow between regions exceeds connecting-circuit capacity.

F01 may read only schema metadata and `Date` values. It must not retrieve or emit current FY2026-27 numerical constraint cost/volume records.

### B. System-state input / 계통상태 input
NESO `Historic Demand Data 2026`:
- CKAN resource ID: `8a4a771c-3929-4e56-93ad-cdf13219dea5`;
- `SETTLEMENT_DATE`;
- `SETTLEMENT_PERIOD` — half-hourly period; period 1 = 00:00–00:30 and clock changes are represented in settlement-period structure;
- system-state fields include `ND`, `TSD`, embedded wind/solar generation and capacity, pump storage, Scottish transfer and multiple interconnector flows.

F01 may read schema metadata and only `SETTLEMENT_DATE` + `SETTLEMENT_PERIOD` records needed to validate cardinality and overlap. It must not emit input numerical values.

## 3. Exposure disclosure / 노출 고지

Before this preregistration, source qualification opened:
- first five numerical records of **Constraint Breakdown 2025-2026**;
- first five numerical records of **Historic Demand Data 2026**.

Those records are permanently exposed.

As of this preregistration, no actual numerical cost/volume records from the selected **2026-2027 constraint resource** have been opened. Documentation examples are treated as schema examples, not as selected current-resource observations.

`NEW_UK_GRID_FY2627_CONSTRAINT_NUMERICAL_OUTCOME_BLIND = YES_AT_PREREGISTRATION`

Any later experiment must separately disclose demand-record exposure and freeze an evaluation window that does not pretend the exposed records are unseen.

## 4. Frozen future independent unit / 고정 향후 독립단위

Candidate independent unit for a later controlled experiment:

**one calendar/settlement date / 1일**.

Constraint data must contribute at most one record per date. Half-hourly demand/system-state rows are nested within that date and may only be prospectively aggregated; they are not independent daily outcomes.

## 5. Frozen alignment checks / 고정 정렬 검증

F01 must verify without numerical outcome access:

1. both CKAN resource IDs are publicly accessible;
2. constraint schema contains `Date` and all eight documented cost/volume fields;
3. current FY2026-27 `Thermal constraints cost` is typed numeric in the live schema;
4. demand schema contains `SETTLEMENT_DATE`, `SETTLEMENT_PERIOD`, `ND`, `TSD`, embedded wind/solar and interconnector-flow fields;
5. constraint `Date` values are unique;
6. demand `(SETTLEMENT_DATE, SETTLEMENT_PERIOD)` pairs are unique;
7. per-day demand settlement-period count is compatible with GB half-hourly settlement days: allowed set `{46, 48, 50}`;
8. there is a non-empty date overlap on/after `2026-04-01` between FY2026-27 constraints and 2026 demand;
9. no date exists in the qualified overlap with a duplicate daily constraint record;
10. source correction/update semantics are explicitly preserved.

## 6. Frozen correction/version rule / 고정 수정·버전 규칙

NESO documents that:
- Constraint Breakdown action tags can change post-event and the dataset is refreshed;
- Historic Demand is populated 21 days in arrears and may receive retrospective solar/demand corrections.

Therefore any later experiment must freeze:
- extraction timestamp in UTC;
- exact resource IDs;
- raw/query-response SHA-256 or exact downloaded-file SHA-256;
- the final evaluation date window before numerical outcome analysis;
- a maturity rule that excludes dates not yet sufficiently settled under published update lags.

F01 does not choose a numerical maturity cutoff beyond documenting these requirements.

## 7. Future aggregation boundary / 향후 집계 경계

F01 only establishes that aggregation is mechanically possible. It does not select predictors from observed association.

A later experiment may prospectively define a small set of daily aggregates from half-hourly system-state data, but must account for 46/48/50-period clock-change days rather than assuming exactly 48 rows every day.

`SCOTTISH_TRANSFER` is not automatically eligible because the current 2026 NESO page explicitly notes a missing Scottish-transfer data issue. Its use would require separate completeness qualification.

## 8. Frozen gates / 고정 게이트

### `PASS_UK_GRID_DAILY_ALIGNMENT_READY`
All required source/schema/date/cardinality/overlap checks pass and the correction/version rule is sufficient for a separately preregistered experiment.

### `PARTIAL_UK_GRID_SCHEMA_READY__DATE_ALIGNMENT_PENDING`
Schemas qualify but bounded date/cardinality access cannot be reproduced.

### `HOLD_UK_GRID_TIME_OR_VERSION_SEMANTICS_GAP`
Date, settlement-period, correction/version or overlap semantics remain too ambiguous for a defensible daily join.

### `REJECT_UK_GRID_ALIGNMENT_ROUTE`
The selected resources cannot be aligned to one daily independent unit without speculative or non-reproducible transformations.

## 9. PASS downstream boundary / PASS 후속 경계

PASS authorizes at most one separately preregistered low-DOF controlled experiment. Before any numerical FY2026-27 constraint values are opened, that experiment must freeze:
- one primary constraint outcome;
- one baseline;
- small source-justified daily input aggregates;
- evaluation window and maturity rule;
- missingness/correction handling;
- primary metric/materiality/rejection criteria.

After that experiment, mandatory Stage 0 Mission-ROI portfolio return applies.

## 10. Cost / 비용

Incremental monetary cost remains **0 USD**.
