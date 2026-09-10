---
checkpoint_id: CHK-20260910-US-AIR-E01-STAGE-A-ACTIVE
active_issue: 90
active_research: US-AIR-E01
last_completed_issue: 89
last_completed_research: PORTFOLIO-R09
last_decision: DEC-124
updated: 2026-09-10
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_AIR_E01_PREREGISTERED__STAGE_A_WEATHER_QUALITY_ACTIVE`

## Mission / 목적

MEM-054 remains controlling: maximize falsifiable, reproducible, practically relevant cross-data innovation/bottleneck information, not branch throughput. / branch 처리량이 아니라 반증·재현 가능한 관계 정보가 우선이다.

## Stage 0 result / Stage 0 결과

PORTFOLIO-R09 selected:

**`SELECT_C_US_004_FIRST_RELATIONSHIP_TEST`**

Issue #90 `US-AIR-E01` is the sole active research issue.

Selection basis:
- US-AIR-F01 final support = 263 airports / 263 NOAA stations / 95,995 station-date source keys;
- no weather/delay relationship has yet been opened;
- stronger unit diversity and immediate zero-cost operability than current preserved alternatives;
- no automatic tuning of already-tested JP-PORT or rescue of CA-RAIL/AU-NEM structural limits.

## Frozen E01 / 고정 E01

Primary exposure:
**NOAA LCDv2 `DailyPrecipitation` → `log1p(mm)`**.

Primary future outcome:
**airport-day mean eligible BTS `DepDelayMinutes`**.

The relationship model, outcome denominator, baseline, inference, materiality rule and prohibited searches are frozen in `research/US-AIR-E01/README.md` and `DEC-124`.

## Exact next action / 정확한 다음 행동

**Run Stage A weather-quality support only.**

Before any delay magnitude:
- map each airport-date through the F01 time-valid station assignment;
- parse only `DailyPrecipitation` and its quality syntax;
- require >=330 usable assigned days and >=20 usable days each month per airport;
- Stage-A PASS requires >=120 airports and >=120 NOAA stations;
- persist derived weather/quality manifests.

Do not calculate a weather-delay relationship or load delay magnitudes until Stage A PASS is durably adjudicated.

Incremental monetary cost remains **0 USD**.
