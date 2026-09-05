---
id: US-AIR-F01-SOURCE-PREFLIGHT
type: source-preflight
created: 2026-09-05
issue: 88
state: CONTINUE
interim_gate: CONTINUE_US_AIR_F01_BYTE_AND_MAPPING_CARDINALITY
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Source Preflight
# US-AIR-F01 Source 사전검증

## Interim gate / 중간 판정

**`CONTINUE_US_AIR_F01_BYTE_AND_MAPPING_CARDINALITY`**

The official source surface is materially stronger than a metadata-only concept, but the frozen 50-airport / 40-NOAA-station PASS cardinality has **not** yet been established.

No weather values, delay magnitudes or weather–delay relationship were analyzed.

## 1. BTS 2025 On-Time source / BTS 2025 정시운항 source

Official TranStats table:

**Marketing Carrier On-Time Performance (Beginning January 2018)**

Current table profile reports:
- first year: 2018;
- last year: 2026;
- latest available: June 2026;
- 119 fields;
- 60,707,559 records across the current table;
- individual-flight data available through Download.

Primary source:
https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGK

Table profile:
https://transtats.bts.gov/TableInfo.asp?QO_fu146_anzr=b0-gvzr&V0s1_b0yB=D&gnoyr_VQ=FGK

### 2025 monthly PREZIP directory

The official public `/PREZIP/` directory currently exposes all twelve 2025 monthly Marketing Carrier files.

| Month | Filename | Directory size (bytes) |
|---:|---|---:|
| 1 | `On_Time_Marketing_Carrier_On_Time_Performance_Beginning_January_2018_2025_1.zip` | 31,599,374 |
| 2 | `..._2025_2.zip` | 29,442,140 |
| 3 | `..._2025_3.zip` | 35,460,382 |
| 4 | `..._2025_4.zip` | 34,062,432 |
| 5 | `..._2025_5.zip` | 35,708,775 |
| 6 | `..._2025_6.zip` | 36,074,147 |
| 7 | `..._2025_7.zip` | 37,234,575 |
| 8 | `..._2025_8.zip` | 35,785,563 |
| 9 | `..._2025_9.zip` | 32,624,136 |
| 10 | `..._2025_10.zip` | 35,550,100 |
| 11 | `..._2025_11.zip` | 33,429,487 |
| 12 | `..._2025_12.zip` | 35,337,872 |

Directory-listed compressed bytes across the 12 files:
**412,308,983 bytes**.

Directory:
https://transtats.bts.gov/PREZIP/

Direct January and December URLs resolve as ZIP content on the official host. The current conversational web reader rejects ZIP payload materialization because the content type is binary, so **no local SHA-256 is claimed yet**.

This is an execution-environment limitation, not evidence that the BTS file is absent.

## 2. BTS outcome/identity semantics / BTS outcome·식별자 의미

The current official field surface explicitly provides:
- `FlightDate`;
- `OriginAirportID`, `OriginAirportSeqID`;
- `DestAirportID`, `DestAirportSeqID`;
- `CRSDepTime`, `DepTime`;
- `DepDelay`, `DepDelayMinutes`, `DepDel15`;
- `Cancelled`, `CancellationCode`, `Diverted`, `Duplicate`;
- carrier, flight and route identities.

BTS defines:
- `AirportID` as the DOT airport identity appropriate for analysis across years;
- `AirportSeqID` as the time-specific airport identity whose attributes may change;
- `DepDelayMinutes` as scheduled-to-actual departure delay with early departures set to zero.

No delay magnitude was opened to perform this semantic qualification.

## 3. 2025 reporting semantics / 2025 보고 의미

BTS Technical Reporting Directive #39:
- effective 2025-01-01;
- identifies the reporting carriers for calendar-year 2025 data;
- requires on-time reporting for scheduled domestic passenger operations serving reportable airports under the directive;
- defines reportable airports as large, medium, small and non-hub airports under the cited federal definition;
- defines actual gate-departure reporting in **local time**;
- defines departure delay as actual gate departure minus CRS scheduled departure.

Primary:
https://www.bts.gov/explore-topics-and-geography/modes/aviation/number-39-technical-directive-reporting-time

This confirms the local-time interpretation is source-level, but it does not by itself resolve DST conversion to NOAA timestamps.

## 4. BTS Master Coordinate / BTS 공항 좌표

Official Aviation Support Tables — Master Coordinate currently exposes:
- `AirportSeqID`;
- `AirportID`;
- airport code/name;
- `Latitude`, `Longitude`;
- `UTCLocalTimeVariation`;
- `AirportStartDate`, `AirportEndDate`;
- `AirportIsClosed`, `AirportIsLatest`.

Primary:
https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL

Current BTS release information reports the Master Coordinate support table as updated in August 2026.

The current web reader verified field semantics but did not materialize the complete table rows, so no airport→coordinate cardinality is yet claimed.

## 5. NOAA LCDv2 / NOAA LCDv2

Current NOAA/NCEI Local Climatological Data Version 2:
- is the replacement for deprecated LCDv1;
- contains hourly, daily and monthly station measurements;
- derives from U.S. observing systems including ASOS/AWOS;
- provides bulk CSV plain-text access;
- provides an official station list;
- includes common weather families such as temperature, precipitation, humidity, wind, sky conditions, weather type and pressure.

Primary:
https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data

Current station list:
https://www.ncei.noaa.gov/oa/local-climatological-data/v2/doc/lcdv2-station-list.txt

The current station-list retrieval contains **24,072 lines** and directly exposes station ID, latitude, longitude, elevation and station name fields.

Examples visibly present in the official list include distinct U.S. airport stations such as:
- `USW00013874` — Atlanta Hartsfield-Jackson Intl;
- `USW00094846` — Chicago O'Hare Intl;
- `USW00023174` — Los Angeles Intl;
- numerous additional airport/ASOS-type station identities.

These examples establish that airport-coincident station support exists, but they are **not** substituted for the frozen >=40-station intersection test.

## 6. What is already closed / 이미 닫힌 불확실성

Source-level uncertainty reduced:
- 2025 BTS On-Time has all 12 monthly public PREZIP files;
- direct delay outcome semantics are official;
- stable and time-specific airport identities are official;
- BTS has an official coordinate/time-zone support table;
- NOAA LCDv2 has a live official station list and bulk CSV route;
- both source families are zero-cost/public.

## 7. What remains open / 남은 불확실성

Do **not** declare PASS yet.

Still required:
1. materialize a bounded official BTS monthly ZIP and record SHA-256/header without analyzing delay magnitudes;
2. reproduce the complete BTS Master Coordinate row route;
3. construct the actual 2025 origin AirportID/SeqID support set;
4. freeze time-valid airport-coordinate rows for 2025;
5. construct the prospective airport→LCDv2 station map;
6. verify >=50 qualified airports and >=40 unique NOAA stations;
7. verify 2025 LCDv2 station-time support;
8. freeze DST/time-zone conversion and station-day/hour exposure keys.

## 8. Branch discipline / branch 규율

Do not:
- infer support from millions of flight rows;
- count multiple flights under one station-time key as independent weather observations;
- use airport-name matching as the final spatial join;
- optimize station distance by weather–delay result;
- parse `WeatherDelay` as the primary outcome;
- switch to a commercial source to bypass public-source friction.

## Exact next action / 정확한 다음 행동

Use one bounded zero-cost source-execution step to retrieve:
- a BTS 2025 monthly PREZIP payload;
- the BTS Master Coordinate payload;
- NOAA LCDv2 station metadata;

then emit only hashes, headers, identity/coordinate/time-support counts and prospective mapping cardinality.

No effect analysis is authorized.

Incremental monetary cost remains **0 USD**.
