---
id: US-AIR-F01-MASTER-COORDINATE-MAPPING-PREFLIGHT
type: outcome-blind-spatial-mapping-preflight
created: 2026-09-05
issue: 88
frozen_distance_cap_km: 10.0
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Master Coordinate × NOAA Mapping Preflight
# US-AIR-F01 BTS 공항좌표 × NOAA 관측소 Mapping 사전검증

## Exposure boundary / 노출 경계

- The 10.0 km nearest-station cap was frozen in SPATIAL_TEMPORAL_CONTRACT.md before this mapping count was observed.
- Read only airport identities/coordinates and NOAA station metadata.
- Did not parse any BTS delay magnitude or NOAA weather observation value.

## A. BTS January identity support / BTS 1월 identity support

- January ZIP bytes: 31,599,374
- January ZIP SHA-256: 0feaabdbc9e4bd851ef717f342678cdcc5ea0822dd706359aab030bb1a5d1c24
- January unique Origin AirportID: 352
- previously verified Origin AirportID present in all 12 months: 349
- maximum January airports that can be outside the 12-month intersection: 3

## B. BTS Master Coordinate materialization / BTS Master Coordinate materialization

- source-page HTTP: 200
- POST/materialized HTTP: 200
- final materialized URL: https://transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL
- materialized ZIP bytes: 419,318
- materialized ZIP SHA-256: 8852220bbe66bf3929c6de8596e8f5d9641b0a2aa6d46cabdc9d5f22d5cd2156
- CSV member: T_MASTER_CORD.csv
- CSV rows: 20,283
- exact distinct AirportSeqID rows parsed: 20,283
- conflicting duplicate AirportSeqID records: 0
- January exact AirportSeqID matches: 352/352
- January exact matches with usable decimal coordinates: 352/352

## C. Frozen 10 km nearest-LCDv2 mapping / 고정 10 km mapping

- eligible NOAA US-prefix station metadata rows: 6,115
- January airports mapped within 10.0 km: 340
- January airports excluded for no station within cap: 8
- January airports excluded as <=0.001 km nearest-distance tie: 4
- January airports with no exact Master Coordinate SeqID: 0
- January airports with unusable coordinates: 0
- unique NOAA stations after frozen mapping: 340
- NOAA stations shared by more than one mapped airport: 0
- mathematically conservative lower bound on unique stations among the 349 all-12-month airports: 337
- frozen >=40 unique-station threshold proven by lower bound: True

### Mapping-distance diagnostics / mapping 거리 진단

- median km: 0.738
- p90 km: 1.559
- maximum accepted km: 2.968

## D. NOAA 2025 station-year file existence / NOAA 2025 station-year 파일 존재성

- Probe used HEAD, with one-byte Range GET fallback only when needed; no weather observation values were parsed.
- mapped unique stations with a directly reachable 2025 LCDv2 station-year file: 322/340
- conservative lower bound after allowing for up to 3 January-only airports: 319
- frozen >=40 station-year-file threshold proven by lower bound: True

## Interim gate / 중간 판정

**CONTINUE_US_AIR_F01_2025_DATE_SUPPORT_VERIFICATION**

The spatial cardinality gate is evaluated without weather/delay values. A full F01 PASS still requires 2025 station-date support semantics under the frozen station × local-calendar-date grain.

## Exact next action / 정확한 다음 행동

For a deterministic qualified subset, verify only DATE/support coverage in the 2025 LCDv2 station-year files and report station-day cardinality/missing-date structure. Do not parse weather measurements or delay magnitudes.

Incremental monetary cost remains **0 USD**.
