---
id: AU-NEM-F01
type: source-semantic-spatial-temporal-feasibility
state: PREREGISTERED_ACTIVE
created: 2026-09-05
issue: 86
candidate: C-AU-001
decision: DEC-118
mission_anchor: MEM-054
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# AU-NEM-F01 — AEMO Dispatch Constraint/Interconnector × BOM Gridded-Weather Region Feasibility
# AU-NEM-F01 — AEMO dispatch 제약/인터커넥터 × BOM gridded-weather 지역 실행가능성

## 1. Objective / 목적

Qualify one deterministic official-source route from NEM operating identity to a direct congestion outcome and a zero-cost regional weather exposure, before any relationship statistic.

## 2. AEMO source families / AEMO 소스

- Dispatch information page;
- NEMWeb current and archive DispatchIS report directories;
- AEMO constraint FAQ/documentation;
- official NEM region definitions/boundaries.

Primary tables to inspect:
- DISPATCHCONSTRAINT;
- DISPATCHINTERCONNECTORRES;
- DISPATCHREGIONSUM.

## 3. Outcome priority / 결과 우선순위

Priority is frozen before weather values:
1. source-defined binding-constraint burden if generic constraint → region/region-pair identity is deterministic;
2. otherwise source-defined interconnector congestion/transfer-stress;
3. otherwise HOLD.

Non-zero DISPATCHCONSTRAINT MarginalValue is source-defined evidence of a binding constraint. This does not by itself establish a regional outcome until the constraint identity can be assigned without subjective text interpretation.

## 4. NEM geographic identity / NEM 지리 식별

Current AEMO semantics define five interconnected price regions:
- QLD;
- NSW including ACT;
- SA;
- VIC;
- TAS.

If machine geometry is required, F01 may introduce one official government boundary source prospectively. No hand-drawn polygon or post-outcome region repair.

## 5. Weather source boundary / 기상 소스 경계

Candidate BOM routes:
- Climate Data Online;
- Australian Water Outlook product downloads;
- Australian Water Data Service;
- official NCI collection linked by BOM/AWO.

F01 must demonstrate a zero-cost reproducible daily route. Paid data extraction is prohibited.

Potential climate variables are not selected in F01. F01 may inspect only source availability/schema for temperature, rainfall, wind or other documented gridded inputs.

## 6. Time / version contract / 시간·버전

F01 must record:
- dispatch timestamp/time-zone semantics;
- archive/current file naming;
- current schema/data-model version evidence;
- weather time standard;
- source revision/update behavior.

## 7. Exposure boundary / 노출 경계

No weather-congestion relationship, effect size, threshold, lag/lead or region ranking is authorized.

## 8. Gate / 게이트

PASS:
**PASS_AU_NEM_WEATHER_CONGESTION_JOIN_READY**

PARTIAL:
`PARTIAL_AU_NEM_JOIN_SEMANTICS`

HOLD:
`HOLD_AU_NEM_ZERO_COST_WEATHER_OR_OUTCOME_ROUTE`

REJECT:
`REJECT_AU_NEM_CONGESTION_UNIT_NOT_IDENTIFIABLE`

## 9. Cost / 비용

Incremental monetary cost remains **0 USD**.
