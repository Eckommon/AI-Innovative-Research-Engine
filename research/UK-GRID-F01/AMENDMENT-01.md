---
id: UK-GRID-F01-AMENDMENT-01
type: outcome-blind-query-harness-amendment
state: ACTIVE
created: 2026-09-03
parent: UK-GRID-F01
incremental_monetary_cost_usd: 0
---

# UK-GRID-F01 AMENDMENT-01 — SQL Projection Harness Correction
# UK-GRID-F01 수정-01 — SQL Projection 실행 하네스 보정

## Trigger / 발동 사유

The first frozen F01 preflight completed all schema checks successfully but received `HTTP 409 Conflict` when attempting the `datastore_search` requests that used a `fields=` projection. No FY2026-27 constraint numerical cost/volume values and no demand/wind/solar/interconnector numerical values were requested or emitted.

최초 F01 사전검증은 모든 schema 검증을 통과했으나 `fields=` projection을 사용한 `datastore_search` 요청에서 `HTTP 409 Conflict`가 발생했다. FY2026-27 constraint 비용/물량 수치와 demand/wind/solar/interconnector 수치는 요청·출력되지 않았다.

## Official API basis / 공식 API 근거

NESO's current public CKAN pages document both:
- `datastore_search`; and
- `datastore_search_sql` with explicit `SELECT ... FROM "<resource_id>"` syntax.

Therefore the projection mechanism may be corrected without changing the scientific contract.

## Frozen correction / 고정 보정

Keep the existing `datastore_search?limit=0` calls for schema metadata.

Replace only projected record retrieval:

1. Constraint dates:
   `SELECT "Date" FROM "4136a8e2-07c5-4784-8096-28999447a16e"`

2. Demand date/settlement periods:
   `SELECT "SETTLEMENT_DATE", "SETTLEMENT_PERIOD" FROM "8a4a771c-3929-4e56-93ad-cdf13219dea5"`

Use the official `datastore_search_sql` action endpoint.

No cost/volume or system-state numerical column may be selected.

## Date normalization / 날짜 정규화

Normalize both selected date fields only to ISO calendar date `YYYY-MM-DD` before uniqueness/overlap checks. Accept source strings that begin with a valid ISO date and discard only a time suffix for the purpose of the preregistered **daily** independent unit.

This is a source-semantic normalization, not an outcome transformation. It does not alter settlement-period cardinality or any numerical scientific variable.

## Unchanged contract / 변경 없음

Unchanged:
- resource IDs;
- daily independent unit;
- schema requirements;
- allowed settlement counts `{46,48,50}`;
- overlap lower bound `2026-04-01`;
- correction/version boundary;
- frozen scientific gates;
- numerical exposure boundary;
- zero-cost rule.

`NEW_UK_GRID_FY2627_CONSTRAINT_NUMERICAL_OUTCOME_BLIND` remains `YES` because this amendment selects only dates and settlement-period identifiers.

## Cost / 비용

Incremental monetary cost remains **0 USD**.
