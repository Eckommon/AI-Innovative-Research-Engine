---
id: PORTFOLIO-R08-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-05
issue: 87
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-004
selected_gate: US-AIR-F01
next_issue: 88
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R08 Result — Post-AU-NEM Join-PASS Mission-ROI Reselection
# PORTFOLIO-R08 결과 — AU-NEM 조인 PASS 이후 목적-ROI 재선정

## Final selection / 최종 선정

**`SELECT_C_US_004_AVIATION_WEATHER_DELAY_PROPAGATION`**

Selected candidate:

**C-US-004 — U.S. Aviation Weather–Delay Propagation Intelligence**  
**C-US-004 — 미국 항공 기상–지연 전파 병목 지능화**

Exact next bounded gate:

**US-AIR-F01 — BTS On-Time Airport/Flight Identity × NOAA LCDv2 Weather-Station Join Feasibility**  
Issue #88.

No weather value, delay magnitude, weather–delay association, airport ranking or network-propagation coefficient was computed in R08.

## Why a new candidate is promoted / 신규 후보 승격 이유

AU-NEM-F01 proved a technically strong public join but also exposed a portfolio-level lesson:

**large row count is not equivalent to large independent exposure support.**

Six AEMO interconnectors collapse to four broad region-pair weather exposures, so an immediate broad-region regression would risk pseudoreplication.

R08 therefore prioritizes candidates whose next gate can establish:
- a direct source-defined operational outcome;
- many prospectively independent spatial/environmental units;
- deterministic official identity and coordinates;
- a zero-cost machine-readable route;
- a source-semantic gate that can reject the design before effect estimation.

The U.S. aviation candidate is the strongest current fit.

## Current official-source refresh / 현행 공식 source 갱신

### U.S. DOT / BTS — On-Time Performance

Official TranStats currently exposes **Marketing Carrier On-Time Performance (Beginning January 2018)** with latest available data through June 2026.

Current source schema includes:
- `FlightDate`;
- stable `OriginAirportID` / `DestAirportID`;
- time-specific `OriginAirportSeqID` / `DestAirportSeqID`;
- scheduled and actual local departure/arrival times;
- `DepDelayMinutes`, `ArrDelayMinutes`;
- cancellation, diversion and duplicate flags;
- carrier, flight and route identities.

BTS explicitly describes `AirportID` as the airport identifier to use across years and `AirportSeqID` as the time-specific airport identity.

Official:
https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGK

### U.S. DOT / BTS — Master Coordinate support table

The official Aviation Support Tables **Master Coordinate** surface provides:
- `AirportSeqID`, `AirportID`;
- airport code/name;
- latitude/longitude;
- `UTCLocalTimeVariation`;
- attribute start/end dates;
- closed/latest status.

This provides a source-defined airport geometry/time-identity layer without commercial geocoding.

Official:
https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL

### NOAA / NCEI — LCDv2

Current NOAA Local Climatological Data Version 2:
- reports hourly, daily and monthly station measurements;
- uses U.S. observing systems including ASOS/AWOS;
- provides station-list/search mechanics;
- provides bulk CSV plain-text access;
- includes temperature, precipitation, humidity, wind, sky condition, weather type and pressure families.

NOAA states LCDv1 is deprecated and LCDv2 is the current replacement.

Official:
https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data

### ENTSO-E / C-EU-001

The European grid candidate remains scientifically high value, but the official Transparency Platform Web API still requires registration/security-token provisioning. This remains a minimum-operability penalty relative to a keyless source-semantic U.S. aviation F01.

## Mission-ROI scoring / 목적-ROI 점수

0–5 per dimension; total /45. Scores are portfolio decision aids, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Current access | Join defensibility | Next-gate info gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-US-004 Aviation Weather–Delay Propagation** | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | **43** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 5 | **39** | HOLD_HIGH_VALUE_CREDENTIAL |
| C-CA-002 Grain-Flow Pressure × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 4 | 2 | **37** | HOLD_REDESIGN_GEOGRAPHY |
| AU-NEM continuation | 5 | 5 | 5 | 2 | 5 | 5 | 4 | 3 | 2 | **36** | PRESERVE_JOIN__NO_AUTO_E01 |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 4 | **36** | PRESERVE_JOIN_ASSET |
| C-SG-001 Maritime Activity × Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_UNIT_DIVERSITY |

## Why C-US-004 wins / 왜 C-US-004인가

The candidate combines three properties that the last branches repeatedly lacked in one place:

1. **direct operational outcome** — source-defined flight departure-delay fields rather than an invented stress score;
2. **prospective independent-unit scale** — many airport identities can potentially map to distinct weather stations, but F01 must prove this cardinality rather than assume it from flight-row volume;
3. **official identity chain** — BTS itself provides stable/time-specific airport IDs, coordinates and time-zone attributes, while NOAA provides current official station metadata and bulk weather distribution.

It also diversifies away from immediate tuning/rescue of:
- AU-NEM;
- Canada rail;
- Japan port;
- U.S. grid;
- U.S. critical minerals.

## Outcome-boundary decision / outcome 경계 결정

R08 prospectively prioritizes **BTS `DepDelayMinutes`** for F01 outcome qualification.

Do **not** use `WeatherDelay` as the primary future outcome. It is already a source-attributed weather-cause label and would create avoidable label leakage/tail-chasing when related back to observed weather.

Cancellation/diversion remain structural status fields and cannot become substitute outcomes after viewing effects.

## Anti-pseudoreplication requirement / 의사반복 방지 요구사항

The next gate must not claim that millions of flight rows imply millions of independent weather observations.

US-AIR-F01 must count prospectively:
- qualified origin AirportIDs;
- unique NOAA station identities;
- station × local-date support;
- station × local-hour support if time semantics qualify;
- flights nested inside each weather-exposure key;
- airports sharing one weather station.

Frozen minimum PASS support:
- >=50 qualified origin airports;
- >=40 unique NOAA stations;
- complete 2025 common support;
- deterministic source-defined/time-valid spatial and temporal mapping.

## Exact next gate / 정확한 다음 gate

Open exactly:

### US-AIR-F01 — BTS On-Time Airport/Flight Identity × NOAA LCDv2 Weather-Station Join Feasibility

F01 is source-semantic / spatial-temporal / independent-unit feasibility only.

It may inspect:
- metadata/schema;
- source download mechanics and hashes;
- airport/station identities and coordinates;
- date/time/time-zone semantics;
- source-support cardinality;
- null/duplicate/cancel/divert status structure.

It shall not calculate:
- weather–delay effects;
- airport sensitivity;
- weather thresholds;
- network propagation;
- carrier rankings;
- causal effects;
- policy/investment rankings.

## Stop rule / 중단 규칙

Return to Stage 0 if:
- BTS 2025 download is not reproducible without opaque scraping;
- airport→NOAA station mapping requires subjective repair;
- support falls below 50 airports / 40 unique NOAA stations;
- 2025 temporal alignment cannot be frozen;
- a different source/outcome is proposed only to rescue a failed primary route;
- paid access is required.

Incremental monetary cost remained **0 USD**. Any potentially billable action requires explicit prior approval.
