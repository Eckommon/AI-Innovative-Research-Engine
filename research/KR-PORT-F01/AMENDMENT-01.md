---
id: KR-PORT-F01-AMENDMENT-01
type: outcome-blind-source-semantic-amendment
state: ACTIVE
created: 2026-09-03
parent: KR-PORT-F01
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# KR-PORT-F01 AMENDMENT-01 — Current Facility-Authorization Source Augmentation
# KR-PORT-F01 수정-01 — 현행 시설사용허가 Source 보강

## Trigger / 발동 사유

During outcome-blind source/schema qualification, a newer official Ministry of Oceans and Fisheries Public Data Portal API was identified:

- `해양수산부_시설사용허가현황`
- Public Data Portal ID `15160015`
- registered/modified `2026-06-22`
- REST/XML
- free / unrestricted-use metadata
- development and production approval: automatic
- development traffic: 10,000 requests

No numerical port-call turnaround outcome, predictive association, threshold, model result, or port ranking was inspected before this amendment.

결과를 보기 전 source/schema 검증 과정에서 2026-06-22 등록·수정된 해양수산부 공식 `시설사용허가현황` API를 발견하였다. 본 수정 전 port-call turnaround 수치, 예측 연관성, threshold, 모델 결과 또는 항만 순위는 확인하지 않았다.

## Frozen augmentation / 고정 보강

Add this API as **Source B2** while preserving the original B source (`3056955 항만시설사용정보`) as B1.

B2 official metadata states that it accepts port, search start/end dates, arrival year, arrival count, call sign and barge call sign, and returns vessel information, requested-facility information, requested period, reporting-company information, designated-facility information, designated period and permit/authorization status.

Use B2 only for source/schema/semantic qualification inside F01. It does not change the frozen independent unit or primary target candidate.

## Why this is allowed / 허용 근거

This is a prospective source-semantic improvement discovered before sample outcome analysis. It may improve the construct validity of future waiting/berth-related context because requested/designated facility periods and authorization status are closer to operational facility-use semantics than billing-oriented fields alone.

It does **not** authorize calling `port_stay_hours` berth delay, anchorage delay, congestion delay or cargo-handling time. Such constructs require explicit timestamp/usage semantics and separate preregistration.

## Unchanged frozen elements / 변경 없음

Unchanged:
- primary port-call identity candidate: `(port/port-authority identifier, arrival year, arrival count, call sign)`;
- primary target candidate: `departure_timestamp - arrival_timestamp` only after same-call/time semantics pass;
- no model fitting;
- no outcome-driven thresholding;
- facility-use rows remain nested/contextual, not independent calls;
- cost boundary remains `0 USD`;
- PASS/PARTIAL/HOLD/REJECT gates remain unchanged.

## Access boundary / 접근 경계

The B2 Public Data Portal page explicitly requires an API service key and exposes `SERVICE_KEY_IS_NULL` / access-denied error semantics. No credential is available or invented in the current execution context. Therefore metadata may be qualified, but record-level duplicate/timestamp validation remains contingent on reproducible free sample access.
