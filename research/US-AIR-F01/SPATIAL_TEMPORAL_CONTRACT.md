---
id: US-AIR-F01-SPATIAL-TEMPORAL-CONTRACT
type: prospective-join-contract
created: 2026-09-05
issue: 88
state: FROZEN_BEFORE_MAPPING_COUNTS
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Spatial–Temporal Contract
# US-AIR-F01 공간–시간 결합 계약

## Purpose / 목적

Freeze the airport→NOAA spatial rule and future weather-exposure time grain before the airport→station mapping cardinality is observed.

No weather value, delay magnitude, association, airport sensitivity or distance-threshold optimization has been computed.

## Spatial contract / 공간 계약

Primary identity chain:

1. BTS 2025 On-Time OriginAirportID + OriginAirportSeqID;
2. exact AirportSeqID row in the official BTS Aviation Support Tables Master Coordinate;
3. BTS decimal Latitude / Longitude;
4. current NOAA/NCEI LCDv2 station-list GHCN station identity and coordinates;
5. great-circle nearest eligible LCDv2 station.

Frozen maximum nearest-station distance:

**10.0 km**

Rules:
- distance is Haversine great-circle distance on decimal coordinates;
- only NOAA station-list identities beginning with US are eligible in this U.S. gate;
- no airport-name similarity is used as the final join key;
- if no eligible station is within 10.0 km, exclude the airport;
- if two stations are tied to numerical precision within 0.001 km, exclude as ambiguous rather than manually choose;
- do not widen 10.0 km after seeing mapping or later weather–delay results;
- if multiple airports map to one NOAA station, that station remains one environmental exposure cluster.

The 10 km cap is a prospective local-airport-weather measurement boundary, selected to avoid turning this gate into broad regional interpolation.

## Temporal contract / 시간 계약

Primary future environmental exposure grain:

**NOAA station × local calendar date**

Primary BTS date key:

**FlightDate**

Reason for selecting day grain prospectively:
- BTS on-time operational reporting is in local time;
- NOAA LCDv2 documents hourly observations in Local Standard Time and states that DST adjustment is not applied to those hourly observation times;
- an hourly gate would therefore require an additional DST/time-zone conversion contract before effect analysis;
- the day-grain route preserves a source-defensible local-calendar join while avoiding an unnecessary hidden hourly conversion in the first controlled experiment.

Therefore:
- station × local-hour is not the primary E01 exposure unit;
- no lag/lead hour is eligible for selection in F01;
- F01 must verify 2025 station-year date support before PASS;
- later hourly work requires a separately frozen temporal conversion contract before any weather–delay relationship is opened.

## Anti-pseudoreplication / 의사반복 방지

A flight is not an independent weather exposure.

The future primary observational cluster is:

**NOAA station × local calendar date**

Flights nested under the same station-day must be aggregated or clustered under a future preregistered E01 design.

Airport count, flight count and station-day count must be reported separately.

## Frozen structural PASS boundary / 고정 구조 PASS 경계

F01 still requires:
- >=50 qualified 2025 BTS origin AirportIDs;
- >=40 unique NOAA LCDv2 station identities after the 10.0 km rule;
- complete 2025 common station-date support for the eventual qualified subset;
- deterministic BTS AirportSeqID→Master Coordinate row identity.

No threshold can be relaxed after seeing effect values.

## Official source semantics / 공식 source 의미

BTS:
- Marketing Carrier On-Time Performance;
- Aviation Support Tables — Master Coordinate.

NOAA:
- LCDv2 product page;
- LCDv2 station list;
- LCDv2 documentation.

NOAA LCDv2 documentation states that hourly observation time is Local Standard Time and no adjustment is made for Daylight Saving Time.

## Cost / 비용

Incremental monetary cost remains **0 USD**. Any potentially billable action requires explicit prior approval.
