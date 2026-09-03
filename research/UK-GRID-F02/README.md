---
id: UK-GRID-F02
type: boundary-identity-alignment-feasibility-gate
state: PREREGISTERED
created: 2026-09-03
parent_candidate: C-UK-001
parent: UK-GRID-F01
issue: 69
decision: DEC-099
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# UK-GRID-F02 — Boundary Headroom × Thermal-Cost Identity/Alignment Qualification
# UK-GRID-F02 — Boundary Headroom × Thermal-Cost 식별자·정렬 검증

## 1. Purpose / 목적

Determine, before any numerical flow/limit/cost observation is opened, whether two current official NESO resources share exact non-speculative constraint-boundary identity and temporal semantics sufficient for one future low-DOF `boundary headroom → realized thermal cost` experiment.

실제 flow/limit/cost 수치를 열기 전에, 두 현행 공식 NESO resource가 향후 단 하나의 저차원 `boundary headroom → realized thermal cost` 실험에 필요한 동일한 constraint-boundary identity와 시간 의미를 추정 없이 공유하는지 검증한다.

## 2. Frozen official resources / 고정 공식 resource

### A. Day-ahead boundary state / Day-ahead 경계 상태
NESO `Day Ahead Constraint Flows and Limits`:
- resource ID: `38a18ec1-9e40-465d-93fb-301e80fd1352`;
- expected fields: `Constraint Group`, `Date (GMT/BST)`, `Limit (MW)`, `Flow (MW)`;
- source semantics: half-hourly day-ahead boundary flow forecast after Day Ahead energy scheduling and a maximum boundary flow limit;
- source note: from `2024-04-22`, flows no longer include expected constraint mitigation/optimisation actions. The intended 2026 route lies wholly after this methodology boundary.

### B. Realized thermal-cost outcome surface / 실현 thermal-cost outcome
NESO `Thermal Constraint Costs Data 26-27`:
- resource ID: `c730b788-4328-43dc-9f84-27fd3adeda59`;
- expected fields: `Settlement Date`, `Constraint Group`, `Daily Cost (GBP)`;
- source semantics: daily outturn thermal-constraint spend by named constraint group.

## 3. Why F02 rather than immediate E01 / 즉시 E01 대신 F02인 이유

`UK-GRID-F01` established a valid daily join between GB-wide Historic Demand and Constraint Breakdown. It did not establish that generic national demand/embedded-renewables aggregates are the best physical bottleneck predictors.

The F02 pair is more direct:

`named boundary half-hourly flow + limit → named boundary daily thermal cost`.

This is a scientific/source-semantic uncertainty reduction, not a tooling rescue. It therefore satisfies `MEM-054` Mission-ROI logic.

## 4. Frozen outcome-blind boundary / 고정 결과 비사용 경계

F02 may retrieve and persist only:
- CKAN schema metadata;
- exact distinct `Constraint Group` strings;
- row/group counts;
- source-level or group-level minimum/maximum date/datetime coverage;
- hashes of those non-numerical query responses.

F02 must **not** retrieve or emit observation-level numerical values from:
- `Limit (MW)`;
- `Flow (MW)`;
- `Daily Cost (GBP)`.

No relationship, correlation, threshold, ranking or model may be computed.

## 5. Frozen future unit / 고정 향후 단위

Candidate future independent unit:

**`Constraint Group × Settlement Date` / constraint-group × 일**.

Half-hourly day-ahead rows are nested within group-day and are not independent outcomes.

## 6. Frozen identity rule / 고정 identity 규칙

Use **exact source string equality only** for F02.

- normalize leading/trailing whitespace only;
- do not infer B-number ↔ named-boundary translation;
- do not use fuzzy matching, manually guessed aliases, maps or post-hoc semantic remapping to create a match.

If exact code overlap is absent, the default gate is HOLD/REJECT rather than a mapping workaround chain.

## 7. Frozen temporal qualification / 고정 시간 검증

F02 must verify:
1. both resources are publicly queryable;
2. all expected schema fields exist and numerical fields are typed as numeric/integer where documented;
3. both `Constraint Group` fields are strings;
4. both sources expose at least one non-null group identifier;
5. exact normalized group-string intersection is non-empty;
6. day-ahead datetime and thermal settlement-date ranges are parseable;
7. at least one exact common group has overlapping source coverage on/after `2026-04-01`;
8. the intended overlap is post-`2024-04-22` methodology change;
9. no numerical observation from the three frozen numerical fields is requested/emitted.

## 8. Frozen gates / 고정 게이트

### `PASS_UK_GRID_BOUNDARY_IDENTITY_READY`
Exact constraint-group identity and sufficient 2026 temporal overlap are reproducibly established without numerical observation access.

### `PARTIAL_UK_GRID_BOUNDARY_SCHEMA_READY__IDENTITY_PENDING`
Schemas qualify but exact group identity/coverage cannot be reproduced from bounded public queries.

### `HOLD_UK_GRID_BOUNDARY_MAPPING_GAP`
The resources are individually valid but require a non-trivial or speculative group translation not frozen in official source identity.

### `REJECT_UK_GRID_BOUNDARY_ROUTE`
The resources cannot support a defensible same-boundary group-day route.

## 9. PASS downstream boundary / PASS 후속 경계

A PASS does not authorize exploratory analysis. It only permits consideration of the **single remaining numerical experiment allowance** under `DEC-098 / DEC-099`.

Before opening any `Limit`, `Flow` or `Daily Cost` values, that experiment must prospectively freeze:
- one boundary scope or an explicit all-common-group rule;
- one headroom/stress definition;
- one primary daily-cost outcome;
- nested half-hour aggregation;
- repeated-group handling;
- evaluation/maturity/correction window;
- missingness and nonpositive-limit handling;
- one primary statistic and materiality/falsification gate.

After that single experiment, return to Stage 0 Mission-ROI review.

## 10. Cost / 비용

Incremental monetary cost remains **0 USD**.
