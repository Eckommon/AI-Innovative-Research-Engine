---
checkpoint_id: CHK-20260910-US-AIR-E01-STAGE-A-ACTIVE
active_issue: 90
active_research: US-AIR-E01
last_completed_issue: 89
last_completed_research: PORTFOLIO-R09
last_decision: DEC-124
updated: 2026-09-10
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

PORTFOLIO-R09 is complete and selects US-AIR-E01. / R09 완료, US-AIR-E01 선정.

Issue #90 is active under `DEC-124`.

Do not redo F01 or R09 by default.

## Frozen E01 question / 고정 질문

Does same-calendar-date NOAA LCDv2 `DailyPrecipitation` have a positive, materially nontrivial association with airport-day mean BTS `DepDelayMinutes` after airport/date/scheduled-volume controls? / 동일 날짜 강수량이 통제 후 평균 출발지연과 양의 실질적 연관성을 갖는가?

This is not advance prediction or causality.

## Exact next bounded execution / 다음 제한 실행

**Stage A only, before any delay magnitude.**

Use:
- `research/US-AIR-F01/DERIVED_AIRPORT_SEQ_STATION_MAP.csv`;
- `research/US-AIR-F01/FINAL_SUPPORT_AIRPORTS.csv`;
- NOAA 2025 LCDv2 station-year CSV.

Parse only station/date/`DailyPrecipitation` needed for quality qualification.

Frozen per-airport Stage-A support:
- >=330 usable assigned days;
- >=20 usable days in every month.

PASS requires:
- >=120 qualified airports;
- >=120 represented NOAA stations.

No alternate predictor or station repair after failure.

## After Stage A / Stage A 이후

Only if Stage A passes may Stage B read `DepDelayMinutes` and execute the exact frozen model. Otherwise HOLD and return Stage 0.

No weather-delay effect has been computed at this checkpoint.

Cost remains **0 USD**.
