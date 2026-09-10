---
id: US-AIR-E01
type: preregistered-primary-relationship-experiment
created: 2026-09-10
issue: 90
state: COMPLETED_PASS
parent: US-AIR-F01
portfolio_decision: DEC-123
preregistration_decision: DEC-124
mission_anchor: MEM-054
primary_weather_variable: DailyPrecipitation
final_gate: PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION
relationship_outcome_computed: true
delay_magnitudes_parsed: true
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 — Daily Precipitation × Departure Delay Airport-Day Relationship
# US-AIR-E01 — 일별 강수량 × 출발지연 공항-일 관계검증

## Scientific question / 과학 질문

Among prospectively qualified U.S. airport-days in calendar year 2025, is higher same-calendar-date precipitation associated with higher mean departure delay after airport, calendar-date and scheduled-volume controls? / 사전 자격을 통과한 2025 미국 공항-일에서 동일 달력일 강수량 증가가 공항·날짜·예정운항량 통제 후 평균 출발지연 증가와 연관되는가?

This is a **contemporaneous relationship test**. It is not advance prediction and not causal inference. / 당일 관계검증이며 사전예측·인과추론이 아니다.

## Frozen source cohort / 고정 source cohort

Start only from the final F01 deterministic mapping assets:
- `research/US-AIR-F01/DERIVED_AIRPORT_SEQ_STATION_MAP.csv`;
- `research/US-AIR-F01/FINAL_SUPPORT_AIRPORTS.csv`.

F01 produced 263 final airport IDs / 263 unique NOAA station IDs with complete 2025 DATE labels. E01 may reduce this cohort only through the prospectively frozen weather-quality rules below, never by delay relationship.

## Frozen primary exposure / 고정 primary exposure

NOAA LCDv2 **`DailyPrecipitation`** from SI/metric station-year CSV.

Primary numeric predictor:

**`X_ad = log1p(DailyPrecipitation_mm_ad)`**

No alternate weather variable, threshold, lag/lead, station remap, airport subset or carrier subset may replace it after weather quality or delay effects are viewed.

## Frozen precipitation parsing / 강수 parsing 고정

Official LCDv2 precipitation indicators are applied prospectively:

- numeric value >= 0 → usable;
- `0` → measured zero precipitation;
- `T` trace → primary numeric value **0.0 mm**, with a trace flag retained;
- suspect value marked `s` → primary unusable;
- erroneous `*` → unusable;
- blank → missing/unreported; never coerce to zero;
- multiple distinct daily values for one station/date → ambiguous and unusable;
- no imputation.

A prespecified **non-gate** sensitivity may encode `T` as 0.1 mm after the primary result. It cannot rescue the primary gate.

## Stage A — outcome-blind weather-quality gate / 결과 비사용 기상 품질 gate

Before any `DepDelayMinutes` magnitude is parsed:

1. assign each airport-date to the time-valid F01 AirportSeqID→NOAA station;
2. parse only station/date and the frozen `DailyPrecipitation` field plus its quality indicator syntax;
3. preserve a derived weather panel and quality manifest;
4. compute coverage/support only;
5. do not load or summarize delay magnitudes.

An airport qualifies for Stage B only if:
- deterministic station assignment exists for the airport-date;
- **>=330 usable assigned precipitation days** in 2025;
- **every calendar month has >=20 usable assigned days**;
- no manual station repair is used.

Stage-A PASS requires:
- **>=120 qualified origin AirportIDs**;
- **>=120 unique NOAA station identities represented**;
- zero delay-magnitude exposure.

Otherwise:

**`HOLD_US_AIR_E01_PRECIPITATION_SOURCE_QUALITY → Stage 0`**

No alternate weather variable may be substituted inside E01.

## Frozen primary outcome / 고정 primary outcome

Unit: **airport × FlightDate**.

Primary outcome:

**arithmetic mean `DepDelayMinutes` over eligible departures for airport-day**.

Eligible flight rows:
- Duplicate excluded;
- Cancelled = 1 excluded;
- `DepDelayMinutes` nonblank required;
- non-cancelled Diverted rows retained.

No winsorization.

Do not substitute `WeatherDelay`, `ArrDelay`, cancellation rate, another delay measure, or a carrier-specific outcome.

## Frozen operational baseline / 고정 baseline

For airport `a`, date `d`:

- `Y_ad` = mean eligible `DepDelayMinutes`;
- `N_sched_ad` = count of non-duplicate scheduled departure rows, including cancelled/diverted scheduled operations;
- `X_ad` = `log1p(DailyPrecipitation_mm)`.

Baseline model:

`Y_ad = airport FE + calendar-date FE + gamma*log1p(N_sched_ad) + error`

Weather model:

`Y_ad = airport FE + calendar-date FE + gamma*log1p(N_sched_ad) + beta*X_ad + error`

Primary estimation:
**unweighted airport-day OLS**.

Primary uncertainty:
**two-way CR1 clustering by AirportID and FlightDate**.

## Realized panel support gate / 실현 panel 지원 gate

Before interpreting `beta`, Stage B must retain:
- **>=100 origin AirportIDs**;
- **>=30,000 airport-date observations**.

No realized airport/day can be kept or removed because of the sign or magnitude of its weather-delay relationship.

## Primary hypothesis and materiality / 주가설·실질성

Directional hypothesis:

**`beta > 0`**

Primary scientific PASS requires all three:
1. `beta > 0`;
2. two-sided 95% CI lower bound > 0;
3. model-implied 0 mm → 10 mm difference:
   **`beta * ln(11) >= 1.0 minute`**.

The one-minute threshold is a preregistered **screening materiality floor**, not a business-utility claim. / 1분은 연구 선별 실질성 하한이며 사업 효익 주장이 아니다.

Primary gates:
- `PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION`;
- `DETECTABLE_BUT_SUBMATERIAL_US_AIR_E01`;
- `NO_PREREGISTERED_POSITIVE_US_AIR_E01_RELATIONSHIP`;
- `HOLD_US_AIR_E01_SOURCE_OR_PANEL_SUPPORT`.

## Prespecified non-gate sensitivities / 사전 sensitivity

Only after the primary result:
1. trace `T = 0.1 mm` instead of 0.0 mm;
2. exclude Diverted rows from the outcome denominator;
3. dependence stress test clustering by airport and calendar week.

These cannot change or rescue the primary gate.

## Interpretation boundary / 해석 경계

Even a PASS would establish only a preregistered contemporaneous association under this panel design.

It would not establish:
- advance prediction;
- causality;
- network propagation;
- airport/carrier ranking;
- a weather threshold;
- novelty;
- operational or commercial utility;
- investment/policy superiority.

## Exact next action / 정확한 다음 행동

**Execute Stage A only.**

Do not parse `DepDelayMinutes` magnitudes until Stage A is durably recorded as PASS.

## Stop rule / 중단 규칙

Return to Stage 0 without rescue if:
- Stage-A precipitation support fails;
- realized Stage-B panel support fails;
- station identity requires manual repair;
- another weather variable or outcome is proposed after failure;
- paid data or paid compute is required.

Incremental monetary cost must remain **0 USD**.


## Stage A disposition / Stage A 처분

Run 34429102100 resolves Stage A as:

**PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY**

- qualified airports: **255**
- represented NOAA stations: **255**
- usable airport-date weather keys: **92,818**
- assignment gaps / ambiguous station assignments: **0 / 0**
- source fetch failures: **0**
- F01 snapshot hash drift: **0/263**

Eight airports are prospectively excluded by the frozen quality gate: AGS, ATW, BRD, EAR, HIB, LBL, MYR, PQI.

Under DEC-125, Stage B may now execute the previously frozen outcome/model contract. No change to the predictor, thresholds, outcome or model is permitted.


## Final disposition / 최종 처분

Run `34429684361` resolves the preregistered E01 as **`PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION`**.

Primary result: 91,687 airport-days / 255 airports; beta=4.892129968812, 95% CI [4.318542282873, 5.465717654751], 0→10 mm model-implied contrast=11.730815 minutes.

Under DEC-126 this branch is `RELATIONSHIP_TESTED` only. Close #90 and return to Stage 0; no automatic tuning or generalization claim.
