---
id: KR-PORT-F01-RESULT
type: feasibility-result
state: COMPLETED_PARTIAL
created: 2026-09-03
parent: KR-PORT-F01
issue: 65
mission_anchor: MEM-054
portfolio_decision: DEC-094
incremental_monetary_cost_usd: 0
---

# KR-PORT-F01 Result — Port-Call Identity & Turnaround-Target Feasibility
# KR-PORT-F01 결과 — Port-Call 식별자 및 Turnaround Target 실행가능성

## Final Gate / 최종 게이트

**`PARTIAL_KR_PORT_METADATA_SCHEMA_READY__SAMPLE_ACCESS_PENDING`**

The official-source metadata/schema layer is sufficiently coherent to preserve the candidate, but the current execution context cannot complete record-level duplicate/correction/duration diagnostics without a reproducible sample/API access path. No predictive experiment is authorized.

공식 source의 metadata/schema 계층은 후보를 유지할 만큼 충분히 정합적이나, 현재 실행환경에서는 재현 가능한 sample/API record 접근 없이 중복·정정·duration 진단을 완료할 수 없다. 예측실험은 아직 승인되지 않는다.

## 1. Authoritative source identity / 공식 source 확인

### A. Vessel entry/exit / 선박입출항
Official Public Data Portal / Ministry of Oceans and Fisheries surfaces verified:
- `15006353 해양수산부_선박운항정보`: port, query period, call sign and operational vessel information including entry/exit time semantics and arrival count;
- `15083024 해양수산부_선박입출항현황`: official XLSX metadata explicitly lists port name, call sign, vessel name, arrival count, domestic/foreign classification, gross tonnage, arrival timestamp and departure timestamp.

`15083024` currently states:
- 100 rows;
- XLSX;
- free;
- unrestricted-use license;
- institution-hosted download via PORT-MIS information page;
- updated 2025-12-09.

### B1. Port facility use / 항만시설사용
Official `3056955 해양수산부_항만시설사용정보` verified:
- free, unrestricted-use REST/XML;
- real-time;
- automatic development/production approval;
- documented exact query keys: `prtAgCd`, `etryptYear`, `etryptCo`, `clsgn`;
- response repeats the same four fields and provides use type, mooring-place code/subcode/name, `etryndDt`, report time, fees and correction-sequence field `unityFrghtUpdtOdr`.

The official documentation sample reports `totalCount=9` for one frozen query identity, establishing that multiple facility-use rows may exist under one port-call key. Facility rows therefore cannot be counted as independent vessel calls.

### B2. Current facility authorization / 현행 시설사용허가현황
Outcome-blind `AMENDMENT-01` added official Public Data Portal ID `15160015 해양수산부_시설사용허가현황`, registered/modified 2026-06-22.

Its official metadata states that queries may use port, search dates, arrival year, arrival count, call sign and barge call sign, while responses contain vessel information, requested facility/period, designated facility/period, reporting company and authorization status.

This source is semantically promising for future waiting/berth-context construction, but its API detail is credential-gated in the current execution context.

### C. Weather / 기상
Official KMA sources verified:
- `15057210 ASOS 시간자료`: hourly standardized weather observations;
- `15139439 지상기상관측 지점정보`: station number plus observation-period and latitude/longitude history.

An official port-location layer is also available (`15121268 항만가이드라인 위치`) with port names and latitude/longitude coordinates. This provides a defensible future route for freezing a port→weather-station spatial mapping rather than joining by place-name guess alone.

## 2. Candidate port-call identity / 후보 port-call 식별자

Preserve:

`port_call_id = (port/port-authority identifier, arrival year, arrival count, call sign)`

Evidence:
- the facility-use API requires exactly these four dimensions for lookup;
- the vessel-entry/exit surface contains corresponding port/call-sign/arrival-count/timestamp semantics;
- the same key can attach multiple facility rows.

Status: **SUPPORTED AT METADATA/SCHEMA LEVEL; RECORD-LEVEL UNIQUENESS NOT YET VALIDATED.**

Do not drop any key component merely to improve match rate.

## 3. Target construct / Target 구성

Preserve primary target candidate:

`port_stay_hours = departure_timestamp - arrival_timestamp`

The official vessel-entry/exit description explicitly places arrival and departure timestamps in the same vessel entry/exit record family, supporting a same-call operational stay/turnaround proxy.

Claim boundary remains strict:
- this is **port stay / vessel turnaround proxy** only;
- it is not berth waiting time;
- it is not anchorage waiting time;
- it is not cargo handling time;
- it is not causal congestion delay.

Status: **SEMANTICALLY SUPPORTED; RECORD-LEVEL VALIDITY/TIMEZONE DIAGNOSTICS PENDING.**

## 4. Duplicate/correction semantics / 중복·정정 의미

Observed at schema level:
- one port-call key may map to multiple facility-use rows (`totalCount` sample >1);
- `unityFrghtUpdtOdr` explicitly represents a correction/update sequence in B1;
- B2 exposes authorization-status and requested/designated-period semantics.

Not yet established authoritatively at record level:
- whether duplicate rows represent multiple distinct facility uses, correction history, billing lines, or combinations;
- the exact deterministic latest/current-record selection rule for correction sequences;
- whether call-sign/arrival-count records ever require an additional stable key;
- distribution of missing, zero or negative arrival→departure durations.

No duplicate row is silently removed and no correction rule is invented.

## 5. Nested facility-use rule / 시설사용 nested 규칙

**PASS at schema semantics level.**

Independent unit remains one qualified `port_call_id`. Facility-use/authorization rows are nested/contextual records under the port call. Multiple rows may represent different facility/use/charge/authorization records and must be aggregated or encoded only under a prospectively frozen rule.

## 6. Weather-join route / 기상 join 경로

**READY AT SOURCE-SEMANTIC LEVEL.**

Defensible route:
1. freeze a port-level location from an official Ministry of Oceans and Fisheries location layer;
2. use KMA station-history metadata to identify an eligible ASOS station by explicit coordinates and observation validity dates;
3. join hourly weather only over the port-call time window under a frozen timezone/time-binning rule.

Do not use weather measured after departure as a predictor in a prospective turnaround model.

Remaining item: exact PORT-MIS timestamp timezone semantics must be frozen before a controlled experiment.

## 7. Bounded sample-access feasibility / 제한 sample 접근

Official access terms are zero-cost:
- B1/B2 APIs: free, automatic approval, development traffic 10,000;
- vessel XLSX metadata: free and unrestricted-use;
- KMA APIs: public official data services.

However, in the current execution context:
- no Public Data Portal service credential is available or invented;
- B2 documentation explicitly requires an API service key;
- the 100-row vessel XLSX is institution-hosted through a dynamic PORT-MIS page rather than directly retrievable through the current reproducible tool path.

Therefore actual sample rows needed to validate uniqueness, correction behavior, missingness and duration signs were not accessed.

## 8. Gate evaluation / 게이트 평가

| Requirement | Result |
|---|---|
| authoritative source identity / 공식 source | PASS |
| deterministic candidate identity / 후보 식별자 | PASS_METADATA_SCHEMA_ONLY |
| duplicate/correction handling / 중복·정정 처리 | PARTIAL — fields exist, deterministic rule not yet validated |
| same-call arrival/departure target / 입출항 target | PASS_SEMANTICS_ONLY |
| nonnegative-duration empirical validation | PENDING_SAMPLE |
| nested facility-use semantics | PASS |
| weather join route | PASS_SOURCE_ROUTE / timezone freeze pending |
| bounded reproducible free sample | PENDING_CURRENT_EXECUTION_CONTEXT |

Final:
**`PARTIAL_KR_PORT_METADATA_SCHEMA_READY__SAMPLE_ACCESS_PENDING`**

## 9. Mission-ROI disposition / 목적-ROI 처리

Do **not** create a credential-acquisition or scraping descendant merely to finish F01.

The scientific candidate remains promising, but PASS requires a future execution context that already has a legitimately authorized zero-cost Public Data Portal credential or a directly reproducible official sample-download route.

Under `MEM-054 / DEC-093`, this PARTIAL result does not justify infrastructure recursion. Return to Stage 0 portfolio review unless the user explicitly prioritizes completing this branch or an authorized free sample-access context becomes available naturally.

## 10. Cost / 비용

Incremental monetary cost: **0 USD**.
No paid access, proxy, scraping service, storage or compute was used.
