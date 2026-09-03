---
id: KR-PORT-F01
type: cross-dataset-feasibility-gate
state: PREREGISTERED
created: 2026-09-03
parent_candidate: C-KR-003
portfolio_decision: DEC-094
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# KR-PORT-F01 — Port-Call Identity & Turnaround-Target Feasibility Gate
# KR-PORT-F01 — Port-Call 식별자 및 Turnaround Target 실행가능성 게이트

## 1. Purpose / 목적

Before extracting a long history or training any model, determine whether official Korean port datasets support a deterministic **port-call-level identity** and a defensible **arrival-to-departure operational turnaround/stay target** that can be joined to port-facility use and later weather/cargo context.

장기 이력 추출이나 모델학습 전에 한국 공식 항만데이터에서 결정론적 **port-call 단위 식별자**와 방어 가능한 **입항→출항 turnaround/stay target**을 만들고 항만시설사용 및 후속 기상·화물 context와 결합할 수 있는지 검증한다.

This is a source/schema/semantic feasibility gate, not a predictive experiment. / 본 단계는 source·schema·의미론 실행가능성 검증이며 예측실험이 아니다.

## 2. Mission-ROI / 목적-ROI

- Scientific uncertainty: event identity + operational target semantics.
- Not a transport/runtime workaround.
- High cross-dataset value with low immediate compute burden.
- If this gate HOLD/REJECTs, return to Stage 0 portfolio selection; do not open an automatic rescue chain.

## 3. Frozen official source candidates / 고정 공식 source 후보

### A. Vessel operation / entry-exit / 선박운항·입출항
Public Data Portal family `15006353`; current metadata describes port, call sign, arrival count, vessel attributes, origin/next port and arrival/departure time semantics.

Official references:
- `https://www.data.go.kr/data/15006353/openapi.do`
- `https://www.data.go.kr/data/15083024/fileData.do`

### B. Port facility use / 항만시설사용
Public Data Portal `3056955`, Ministry of Oceans and Fisheries.

Current documented query identity:
- `prtAgCd` — port authority code;
- `etryptYear` — arrival year;
- `etryptCo` — arrival count;
- `clsgn` — call sign.

Current documented response includes the same identity fields plus:
- `laidupPlaceCd` / `laidupPlaceSubCd` / `laidupFcltyNm`;
- `useSe` / `useSeNm`;
- `etryndDt`;
- facility/charge-related fields.

Official reference:
- `https://www.data.go.kr/data/3056955/openapi.do`

### C. Weather context / 기상 context
KMA ASOS hourly API `15057210`.

Current documented fields include station/time plus temperature, precipitation, wind, humidity, pressure and related observations.

Official reference:
- `https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057210`

### D. Cargo/container context / 화물·컨테이너 context
Retain only as downstream context until exact call-level join semantics are qualified. Do not assume monthly/statistical container APIs are event-level joins.

## 4. Frozen candidate event identity / 고정 후보 event identity

The primary identity candidate to test is:

`port_call_id = (port/port-authority identifier, arrival year, arrival count, call sign)`

No component may be dropped after observing duplicates merely to increase apparent match rate.

The gate must determine:
- whether the vessel-entry/operation source exposes corresponding fields with stable semantics;
- whether facility-use rows can be many-to-one/nested under one port call rather than being miscounted as independent vessel calls;
- how corrections/updates/duplicate declarations are represented;
- whether vessel call sign reuse or port-code ambiguity requires additional frozen identity fields.

## 5. Frozen target candidate / 고정 target 후보

Primary candidate only if authoritative source semantics support same-call arrival and departure timestamps:

`port_stay_hours = departure_timestamp - arrival_timestamp`

Requirements before promotion:
- both timestamps belong to the same qualified `port_call_id`;
- duration is computed only after timestamp/timezone semantics are verified;
- negative/zero/missing durations are diagnosed, not silently dropped;
- no facility-use or weather field that occurs after departure is permitted as a predictor in a future prospective-delay model;
- distinguish **port stay / vessel turnaround proxy** from berth waiting, anchorage waiting, cargo handling time, and causal congestion unless separate timestamps establish those constructs.

The project must not label `port_stay_hours` as berth-delay or congestion-delay merely because it is long.

## 6. Outcome-blind / anti-leakage boundary / 결과 비사용·누수 방지

KR-PORT-F01 may inspect:
- metadata;
- schema/field names/types;
- a bounded sample sufficient to test identity/duplicate/timestamp validity if available through a verified free route;
- counts/missingness/duplicate structure needed for feasibility.

It must not:
- fit predictive models;
- optimize thresholds based on turnaround values;
- define congestion classes from observed quantiles;
- select ports/weather variables because they correlate with the target;
- treat facility-use rows as independent port calls.

## 7. Access / cost boundary / 접근·비용 경계

Public Data Portal APIs are documented as free but require a service key for API calls. KR-PORT-F01 must not invent or expose a credential.

Allowed:
- official public metadata/documentation without authentication;
- official public file/sample access if directly available;
- an already-authorized free Public Data Portal service key if available through an approved project execution context.

If exact sample/API access requires a service key not available to the execution context, record `PARTIAL_METADATA_SCHEMA_READY__SAMPLE_ACCESS_PENDING`; do not replace it with scraped/unverified data and do not request paid access.

## 8. Frozen gates / 고정 gate

### `PASS_KR_PORT_CALL_TARGET_READY`
All of the following are established:
1. authoritative source identity and terms;
2. deterministic call-level identity across vessel and facility-use surfaces;
3. documented duplicate/correction handling;
4. same-call arrival/departure semantics support a nonnegative turnaround/stay target under a frozen validity rule;
5. facility-use attaches as nested/contextual information without redefining independent units;
6. weather join route is semantically defensible;
7. bounded free sample access is reproducible.

### `PARTIAL_KR_PORT_METADATA_SCHEMA_READY__SAMPLE_ACCESS_PENDING`
Metadata/schema/identity candidate and target semantics are supported, but authenticated sample bytes/records needed for duplicate and duration validation are unavailable in the current zero-cost execution context.

### `HOLD_KR_PORT_IDENTITY_OR_TARGET_GAP`
Official sources exist but exact call identity, arrival/departure pairing, correction semantics, or target construct remains too ambiguous for a controlled experiment.

### `REJECT_KR_PORT_TURNAROUND_ROUTE`
The intended port-call turnaround construct cannot be represented defensibly from the selected official sources, or join semantics require speculative linkage.

## 9. PASS downstream boundary / PASS 후속 경계

A PASS authorizes at most one separately preregistered low-DOF controlled experiment. Before that experiment, freeze:
- one target construct;
- one baseline;
- one time split/design;
- a small, source-justified predictor set;
- leakage exclusions;
- materiality and rejection criteria.

After that experiment, mandatory Stage 0 Mission-ROI portfolio return applies.

## 10. Cost / 비용

Incremental monetary cost remains `0 USD`. Any potentially billable action requires explicit prior user approval.
