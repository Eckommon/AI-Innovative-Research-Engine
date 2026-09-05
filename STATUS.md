---
checkpoint_id: CHK-20260905-US-AIR-F01-ACTIVE
active_issue: 88
active_research: US-AIR-F01
last_completed_issue: 87
last_completed_research: PORTFOLIO-R08
last_decision: DEC-120
updated: 2026-09-05
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__PORTFOLIO_R08_US_AIR_SELECTED__US_AIR_F01_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #88 `US-AIR-F01 — BTS On-Time airport/flight identity × NOAA LCDv2 weather-station join feasibility`.

## Fixed Mission / 고정 목적

Discover and validate **new, falsifiable, reproducible and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**. `MEM-054` remains mandatory.

## Last completed research / 마지막 완료 연구

`PORTFOLIO-R08` completed as:

**`SELECT_C_US_004_AVIATION_WEATHER_DELAY_PROPAGATION`**

Selected branch:

**C-US-004 — U.S. Aviation Weather–Delay Propagation Intelligence**.

Why:
- BTS exposes direct operational departure-delay fields and stable/time-specific airport IDs;
- BTS Master Coordinate exposes official airport coordinates and time-zone attributes;
- NOAA LCDv2 is the current official station-weather product with bulk CSV access;
- the branch can test true independent weather-exposure cardinality before any relationship estimate;
- it diversifies away from immediate AU-NEM / Canada-rail / Japan-port / U.S.-grid tuning or rescue.

No weather value or delay magnitude was used to select the branch.

## Preserved AU-NEM boundary / 보존된 AU-NEM 경계

`AU-NEM-F01` remains:

**`PASS_AU_NEM_WEATHER_CONGESTION_JOIN_READY`**.

Do not automatically launch broad-region AU-NEM E01:
- six interconnectors collapse to four broad region-pair weather exposures;
- parallel interconnectors are not independent weather units;
- the join asset remains reusable under `DEC-119`.

## Active US-AIR-F01 boundary / 활성 US-AIR-F01 경계

Frozen candidate period:
**calendar year 2025**.

Primary future outcome family to qualify:
**BTS `DepDelayMinutes`**.

Do not use `WeatherDelay` as the primary outcome.

F01 must explicitly count:
- qualified BTS origin AirportIDs;
- unique NOAA LCDv2 station identities;
- station × local-date support;
- station × local-hour support if time semantics qualify;
- nested flight multiplicity;
- airports sharing one station.

Minimum structural PASS support:
- >=50 qualified origin AirportIDs;
- >=40 unique NOAA station identities;
- complete 12-month 2025 common support;
- deterministic spatial/time alignment.

Flight rows sharing the same weather exposure must not be treated as independent environmental replications.

## Exact next action / 정확한 다음 행동

Execute Issue #88 `US-AIR-F01` outcome-blind:

1. reproduce the official BTS 2025 On-Time download/snapshot route without opaque scraping;
2. qualify BTS airport identity, coordinate and time-zone support;
3. qualify NOAA LCDv2 station metadata and zero-cost bulk route;
4. freeze a prospective airport→station spatial rule;
5. freeze BTS-local ↔ NOAA observation-time alignment including DST handling;
6. report independent exposure-unit cardinality before weather values or delay magnitudes;
7. return PASS / PARTIAL / HOLD / REJECT under the frozen gate.

Incremental monetary cost remains **0 USD**. Any potentially billable action requires explicit prior approval.
