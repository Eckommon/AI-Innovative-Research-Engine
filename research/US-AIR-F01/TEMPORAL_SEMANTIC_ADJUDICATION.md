---
id: US-AIR-F01-TEMPORAL-SEMANTIC-ADJUDICATION
type: temporal-semantic-adjudication
created: 2026-09-09
issue: 88
state: FINAL
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Temporal Semantic Adjudication
# US-AIR-F01 시간 의미 판정

## Decision / 판정

For the first eligible daily-grain downstream design, the deterministic temporal key is:

**BTS `FlightDate` calendar label ↔ NOAA LCDv2 `DATE` YYYY-MM-DD calendar prefix**

This closes the F01 join-feasibility requirement at **calendar-date label grain** only. / 이는 F01의 결합 가능성을 **달력 날짜 라벨 단위**에서만 닫는다.

## Source semantics / source 의미

- BTS calendar-year 2025 on-time reporting records scheduled/actual flight-operation times in local time and provides `FlightDate` as the operational calendar-date key. / BTS 2025 정시운항 보고는 운항 시각을 local time으로 보고하며 `FlightDate`를 운항 달력일 key로 제공한다.
- NOAA LCDv2 documentation defines hourly observation time as Local Standard Time and states that Daylight Saving Time adjustment is not applied. / NOAA LCDv2는 hourly observation time을 Local Standard Time으로 정의하며 DST 보정을 적용하지 않는다.
- The previously frozen primary exposure grain is `NOAA station × local calendar date`; hourly alignment was explicitly excluded from F01. / 기존 계약은 `station × local calendar date`를 primary grain으로 고정했고 hourly alignment는 F01에서 제외했다.

## Frozen interpretation / 고정 해석

The same YYYY-MM-DD label is a reproducible **date-label join**, but it is **not** evidence that BTS civil-local day and NOAA LST day represent the same physical 24-hour interval during DST periods. / 동일 YYYY-MM-DD는 재현 가능한 날짜-label 결합이지만 DST 기간의 BTS civil-local day와 NOAA LST day가 동일한 물리적 24시간 구간이라는 뜻은 아니다.

Therefore:

1. F01 permits only the date-label join for future daily-grain work. / F01은 향후 daily-grain 작업에서 날짜-label 결합만 허용한다.
2. F01 does not authorize station-hour, near-departure-hour, lead/lag-hour, or sub-daily weather alignment. / station-hour·출발 인접시간·lead/lag·sub-daily 결합은 미승인이다.
3. Any future hourly design requires a new prospectively frozen DST/time-zone conversion contract before weather or delay effects are opened. / 향후 hourly 설계는 결과 노출 전에 별도 DST/time-zone 계약을 사전고정해야 한다.
4. DATE presence proves source support, not weather-variable completeness, quality, or equal physical exposure windows. / DATE 존재는 source 지원도만 증명하며 기상변수 완전성·품질·동일 물리 노출창을 증명하지 않는다.

## Outcome structural eligibility / outcome 구조 자격

The separately frozen outcome contract remains coherent with the 2025 source structure:
- `Duplicate` observed vocabulary is only `N` across 7,736,770 identity rows;
- `Cancelled` and `Diverted` are source-defined structural flags;
- future continuous `DepDelayMinutes` work excludes Duplicate and Cancelled rows, retains non-cancelled Diverted rows only when `DepDelayMinutes` is nonblank, and never promotes `WeatherDelay` to the primary outcome.

F01 inspected `DepDelayMinutes` only as blank/nonblank structure; no delay magnitude was parsed or summarized. / F01은 지연값 자체가 아니라 blank/nonblank 구조만 확인했다.

## Boundary / 경계

This adjudication establishes deterministic **join semantics**, not statistical independence, weather measurement quality, association, prediction, causality, propagation, novelty or utility. / 본 판정은 결정론적 **결합 의미**만 확정하며 통계적 독립성·기상 측정품질·연관성·예측·인과·전파·신규성·실용성을 확정하지 않는다.

Incremental monetary cost remains **0 USD**.
