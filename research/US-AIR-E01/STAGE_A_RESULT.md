---
id: US-AIR-E01-STAGE-A-RESULT
type: outcome-blind-weather-quality-result
created: 2026-09-10
issue: 90
gate: PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY
delay_magnitudes_parsed: false
weather_delay_relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 Stage A — DailyPrecipitation Quality
# US-AIR-E01 Stage A — DailyPrecipitation 품질

## Exposure boundary / 노출 경계

- Primary variable was frozen before this execution: NOAA LCDv2 DailyPrecipitation.
- This stage parsed the frozen weather variable and quality syntax only.
- No BTS DepDelayMinutes magnitude was loaded or summarized.
- No weather-delay relationship, airport ranking, threshold or lag was computed.

## Source cohort / source cohort

- F01 final airports entering Stage A: **263**
- deterministic station identities required by 2025 assignment: **263**
- source fetch errors: **0**
- station files missing DailyPrecipitation column: **0**
- current station-year files whose SHA-256 differs from the F01 DATE-support snapshot: **0/263**

A changed hash is disclosed as source revision/snapshot drift; it is not selected by weather or delay results.

## Deterministic airport-date assignment / 결정론적 공항-일 배정

- PASS assignments: **95,995**
- unassigned airport-dates: **0**
- ambiguous-station airport-dates: **0**

## Frozen quality gate / 고정 품질 gate

Per-airport requirement: >= 330 usable assigned days and >= 20 usable days in every month.

- qualified origin airports: **255**
- unique NOAA stations represented by qualified usable airport-days: **255**
- qualified usable airport-date weather keys: **92,818**
- >= 120 airport threshold: **True**
- >= 120 station threshold: **True**

## Gate / 판정

**PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY**

If PASS, Stage B may be separately executed under the already frozen outcome/model contract. If HOLD, do not substitute another weather variable inside E01; return to Stage 0.

## Durable derived artifacts / 영속 파생 산출물

- research/US-AIR-E01/STAGE_A_STATION_MANIFEST.csv
- research/US-AIR-E01/STAGE_A_AIRPORT_QUALITY.csv
- research/US-AIR-E01/STAGE_A_AIRPORT_DATE_WEATHER.csv

Raw NOAA station-year CSV files are transient and are not persisted.

Incremental monetary cost remains **0 USD**.
