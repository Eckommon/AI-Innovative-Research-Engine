---
id: US-WATERWAY-F01-RESULT
type: outcome-blind-join-feasibility-result
created: 2026-09-11
issue: 98
state: COMPLETED_PASS
final_gate: PASS_US_WATERWAY_F01_JOIN_READY
decision: DEC-135
claim: CLM-141
delay_magnitudes_parsed: false
hydrology_values_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-F01 Result / 결과

## Final gate / 최종 판정

**`PASS_US_WATERWAY_F01_JOIN_READY`**

The frozen source/identity/date-support gate passes without parsing any lock-delay magnitude or hydrologic observation value. / lock 지연값·수문 관측값을 열지 않고 source·identity·기간지원 gate를 통과했다.

## Verified structure / 검증 구조

- Official Corps Locks Annual Usage public route is HTTP 200, describes usage metrics **for each lock**, exposes annual labels **2016–2025**, and includes `Average Delay` plus processing-time schema labels.
- The official historical Public Lock Usage XLSX (`2959.xlsx`) is reproducibly downloadable, SHA-256 `0db8e4ae602bb60fea029a17a3c39929fe58cef6cc46b6f05bd1f45c4088f90f`, and its TOC contains **193** unique lock identities with `Waterway` and `Lock` columns.
- The public USACE lock feature layer exposes **234** lock features with stable machine-readable identity/location fields.
- Existing USGS metadata qualification provides **25** lock↔monitoring-location matches with Daily `00060` and/or `00065` metadata covering **2018-01-01–2020-12-31**.
- Historical Usage identity ↔ qualified USGS lock crosswalk resolves **25/25**, with no fuzzy matching; three named aliases are admitted only because the official USACE TOC directly documents the historical names.

The same prospective three-year interval **2018–2020** is supported by the Annual Usage route and the USGS metadata route. / 동일 3개년 2018–2020이 양쪽 source route에서 지원된다.

## Evidence boundary / 증거 경계

This PASS means **JOIN_READY only**. It does not establish:
- the magnitude or distribution of lock delay;
- any streamflow/gage-height magnitude;
- a hydrology → delay relationship;
- causality, prediction, propagation, novelty, or decision utility.

Any effect experiment must return through Stage 0 and separately preregister one outcome, one hydrology exposure, temporal aggregation/alignment, lock dependence, seasonality/navigation controls, falsification, materiality, and novelty/utility assessment. / 효과실험은 별도 사전등록 전 자동 승인되지 않는다.

## Durable evidence / 영속 근거

- `ANNUAL_USAGE_SESSION_DIAGNOSTIC.md`
- `USAGE_ARCHIVE_PREFLIGHT.md`
- `USAGE_TOC_PREFLIGHT.md`
- `NAMED_LOCK_ALIAS_DIAGNOSTIC.md`
- `HISTORICAL_HYDROLOGY_CROSSWALK.md`
- `HYDROLOGY_METADATA_PREFLIGHT_V2.md`
- `SOURCE_ROUTE_DIAGNOSTIC.md`

Incremental monetary cost remained **0 USD**.
