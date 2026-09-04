---
id: JP-PORT-F01
type: source-semantic-spatial-temporal-join-feasibility
created: 2026-09-04
issue: 79
state: PREREGISTERED_ACTIVE
mission_anchor: MEM-054
portfolio_decision: DEC-110
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 — MLIT Port-Month × JMA Weather-Station Deterministic Join Feasibility
# JP-PORT-F01 — MLIT 항만-월 × JMA 기상관측소 결정론적 조인 실행가능성

## 1. Objective / 목적

Establish only whether official Japanese public sources support a deterministic research bridge:

`port identity × calendar month → official port location → JMA station identity → daily weather observations → later monthly exposure aggregation`

while freezing one direct port-throughput outcome family before any weather-throughput relationship statistic is calculated.

F01 is **not** the numerical port-weather experiment.

## 2. Frozen source families / 고정 소스

### A. MLIT Port Survey / 港湾調査
Official root:
`https://www.mlit.go.jp/k-toukei/kouwan.html`

F01 shall qualify:
- exact current e-Stat/MLIT data-product identifiers and access route;
- port-level monthly grain;
- stable port identifier/name;
- year/month;
- vessel-arrival, maritime-cargo and container fields/units;
- preliminary vs final/revision semantics;
- exact source snapshot/hash where downloadable.

### B. JMA historical weather / 過去の気象データ
Official root:
`https://www.data.jma.go.jp/risk/obsdl/`

F01 shall qualify:
- station ID/name and coordinates/location metadata;
- daily observation elements relevant to port operations;
- date/time basis;
- missing, quality and homogeneity indicators;
- reproducible zero-cost access route.

## 3. Outcome-free future throughput selection rule / 결과 비사용 향후 throughput 규칙

Before any JMA weather relationship is computed, F01 must freeze exactly one future primary throughput outcome family from source semantics.

Prospective priority:
1. monthly **total maritime cargo throughput** at port level, if one consistent total field and unit exists;
2. otherwise monthly total vessel arrivals, if cargo total semantics cannot be made uniform;
3. container/TEU may be secondary only if its port coverage and unit semantics are independently qualified.

No outcome may be chosen because it later produces a stronger weather relation.

## 4. Port-location and station identity / 항만 위치·관측소 식별

F01 must use an official location source.

A future mapping may use a nearest-station rule only after:
- port coordinate semantics are frozen;
- JMA station coordinates are frozen;
- one maximum-distance rule is declared before throughput-weather outcomes;
- ties/multiple stations are resolved by a deterministic source rule;
- stations with relocation/homogeneity breaks are handled prospectively.

No manual visual map matching or post-outcome station substitution is allowed.

## 5. Time qualification / 기간 검증

Use only a bounded period for which:
- MLIT monthly data are mature/final or have a documented revision state;
- JMA daily observations and required quality metadata are available;
- station identity is sufficiently stable for monthly aggregation.

F01 may count structural coverage but shall not calculate weather-throughput associations.

## 6. Integrity rules to freeze before PASS / PASS 전 고정 규칙

- source URL/table/file identity and hash/snapshot;
- port identifier uniqueness;
- duplicate port-month handling;
- preliminary/final revision policy;
- missing/zero distinction;
- unit semantics;
- JMA station missing/quality/homogeneity rules;
- spatial mapping rule and maximum distance;
- support-qualified port subset rule;
- exact common period.

## 7. Gate / 게이트

### PASS
**`PASS_JP_PORT_WEATHER_JOIN_READY`**

if exact source snapshots, deterministic port/station mapping, mature common period, direct future throughput outcome, and fail-closed integrity rules are all established.

### PARTIAL
`PARTIAL_JP_PORT_JOIN_SEMANTICS`

### HOLD
`HOLD_JP_PORT_PUBLIC_OR_SPATIAL_ROUTE`

### REJECT
`REJECT_JP_PORT_STATION_UNIT_NOT_IDENTIFIABLE`

## 8. Exposure boundary / 노출 경계

F01 shall not calculate:
- monthly weather exposure vs throughput relationships;
- threshold optimization;
- port sensitivity/ranking;
- causal effects;
- policy/investment ranking.

## 9. Cost / 비용

Incremental monetary cost must remain **0 USD**. Any potentially billable action requires explicit prior user approval.
