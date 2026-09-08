---
id: US-AIR-F01-RESULT
type: feasibility-result
created: 2026-09-09
issue: 88
state: COMPLETED
gate: PASS_US_AIR_AIRPORT_WEATHER_JOIN_READY
decision: DEC-122
claim: CLM-135
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Result
# US-AIR-F01 결과

## Final gate / 최종 판정

**`PASS_US_AIR_AIRPORT_WEATHER_JOIN_READY`**

Current official zero-cost BTS and NOAA public sources support a deterministic, time-valid, outcome-blind airport-to-weather-station join for a later bounded daily-grain experiment. / 현행 무료 BTS·NOAA 공식 공개 source는 향후 제한된 daily-grain 실험을 위한 결정론적·time-valid·결과 비사용 공항→기상관측소 결합을 지원한다.

**JOIN_READY does not mean EXPERIMENT_READY. / JOIN_READY는 EXPERIMENT_READY를 의미하지 않는다.**

## Frozen gate review / 고정 gate 검토

| Requirement / 요건 | Evidence / 증거 | Result / 판정 |
|---|---|---|
| Reproducible BTS 2025 route / BTS 2025 재현 경로 | 12 monthly official PREZIP files; 7,736,770 identity rows; hashes recorded | PASS |
| Direct outcome semantics / 직접 outcome 의미 | `DepDelayMinutes` frozen; `WeatherDelay` excluded; structural status eligibility frozen | PASS |
| Deterministic airport identity / 공항 식별 | 528 annual AirportID/SeqID pairs; Master Coordinate exact identity/time-valid checks | PASS |
| Frozen spatial rule / 고정 공간 규칙 | 10.0 km nearest eligible NOAA station; tie/out-of-cap fail closed | PASS |
| >=50 origin airports / 공항 최소수 | 337 all-12-month spatial-qualified; 263 remain with full DATE support | PASS |
| >=40 NOAA stations / 관측소 최소수 | 340 spatial station identities; 263 remain with full DATE support | PASS |
| Complete 2025 source-date support / 연중 source-date 지원 | 265 station-year files have all 365 DATE labels; final 263-airport/263-station subset | PASS |
| Exposure-key cardinality / 노출 key 수 | 263 × 365 = **95,995 station × calendar-date keys** | PASS |
| Temporal contract / 시간 계약 | BTS `FlightDate` ↔ NOAA DATE prefix at date-label grain; DST physical-window limitation explicit | PASS at daily date-label grain |
| No outcome exposure / 결과 비노출 | no weather values, delay magnitudes, association or effect opened | PASS |

## Full-year evidence / 연중 증거

Successful zero-cost GitHub Actions Run:

**`34218434530`**

The reusable runner `tools/us_air_f01_support.py` reproduced:
- 364 union 2025 origin AirportIDs;
- 349 AirportIDs present in all 12 months;
- 528 AirportID/SeqID pairs;
- 513 SeqID mappings passing the frozen spatial rule;
- 5 ambiguous ties excluded;
- 10 over-10-km mappings excluded;
- 337 all-12-month airports whose every observed SeqID passes;
- 340 unique NOAA stations used by those spatial-qualified airports;
- 265 station-year files with all 365 2025 DATE labels;
- final **263 airports / 263 unique NOAA stations / 95,995 station-date source keys**.

Reusable derived manifests:
- `DERIVED_AIRPORT_SEQ_STATION_MAP.csv`
- `DERIVED_AIRPORT_SUPPORT.csv`
- `DERIVED_NOAA_DATE_SUPPORT.csv`
- `FINAL_SUPPORT_AIRPORTS.csv`
- `FULL_YEAR_DATE_SUPPORT.md`

Raw BTS/NOAA payloads remain transient under RAW-001. / 원천 bytes는 RAW-001에 따라 영속 저장하지 않는다.

## Temporal qualification / 시간 자격

The admissible F01 time alignment is **same YYYY-MM-DD label at daily grain**, not physical 24-hour equivalence. NOAA hourly timestamps are LST without DST adjustment, so an hourly or near-departure design remains prohibited until separately preregistered. / 허용 결합은 daily 동일 날짜 label이며 물리적 24시간 동일성 주장이 아니다. hourly/near-departure 설계는 별도 사전등록 전 금지한다.

See `TEMPORAL_SEMANTIC_ADJUDICATION.md`.

## What this PASS does not establish / 이 PASS가 입증하지 않는 것

It does **not** establish:
- usable completeness or quality of any selected weather measurement variable;
- statistical independence of distinct stations or station-days;
- weather–delay association or effect;
- advance prediction;
- causal effects;
- network delay propagation;
- airport or carrier ranking;
- novelty, operational benefit or commercial utility.

Distinct stations can experience the same storm system, and adjacent station-days can be dependent. / 관측소 ID가 다르다고 기상 충격이 독립인 것은 아니다.

## Next-state rule / 다음 상태 규칙

Issue #88 may close as completed feasibility. / #88은 완료 feasibility로 종결 가능하다.

Do **not** automatically open or execute E01. Return to Stage 0 portfolio control first. / E01 자동 개시·실행 금지, Stage 0 포트폴리오 통제로 복귀한다.

Any future US-AIR E01 requires a new preregistration that freezes, before weather/delay effects:
- one primary scientific question;
- weather predictor and quality/missingness semantics;
- aggregation denominator and cancellation/diversion handling;
- operational/calendar baseline;
- untouched evaluation split;
- dependence-aware uncertainty;
- falsification/sensitivity rule;
- minimum useful improvement;
- novelty and named decision utility assessment plan.

## Cost / 비용

Incremental monetary cost: **0 USD**. Any potentially billable action still requires explicit prior approval.
