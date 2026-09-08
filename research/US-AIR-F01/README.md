---
id: US-AIR-F01
type: source-semantic-join-feasibility
created: 2026-09-05
issue: 88
state: COMPLETED
parent: PORTFOLIO-R08
decision: DEC-122
claim_basis: CLM-135
mission_anchor: MEM-054
final_gate: PASS_US_AIR_AIRPORT_WEATHER_JOIN_READY
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 — BTS On-Time Airport/Flight Identity × NOAA LCDv2 Weather-Station Join Feasibility
# US-AIR-F01 — BTS 정시운항 공항/항공편 식별자 × NOAA LCDv2 기상관측소 조인 가능성

## Purpose / 목적

Before any weather–delay statistic, determine whether official zero-cost U.S. public sources can support a deterministic, time-valid and anti-pseudoreplicated bridge:

`flight / origin airport × local time → DepDelayMinutes outcome → BTS airport identity/coordinates → NOAA LCDv2 station identity`.

## Frozen period / 고정 기간

Primary support period:
**2025-01-01 through 2025-12-31**.

No period may be changed because a later weather–delay relationship is more favorable.

## Frozen primary outcome family / 고정 primary outcome

**BTS `DepDelayMinutes`**.

Do not use BTS `WeatherDelay` as the primary outcome.

Cancellation/diversion/duplicate fields are structural eligibility/status fields only unless a separately authorized future gate defines otherwise before exposure.

## Official source surfaces / 공식 source

### BTS On-Time

https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGK

Required source-semantic fields include:
- `FlightDate`;
- origin/destination AirportID and AirportSeqID;
- scheduled/actual local times;
- departure-delay fields;
- cancellation/diversion/duplicate flags;
- route/carrier/flight identity.

### BTS Master Coordinate

https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL

Required identity fields include:
- AirportSeqID / AirportID;
- airport code/name;
- latitude / longitude;
- UTCLocalTimeVariation;
- AirportStartDate / AirportEndDate;
- latest/closed flags.

### NOAA NCEI LCDv2

https://www.ncei.noaa.gov/products/land-based-station/local-climatological-data

Qualify:
- station list and stable station identity;
- station coordinates;
- observation-period support;
- hourly/daily source mechanics;
- bulk CSV route;
- missing/quality/time semantics.

LCDv1 is deprecated and is not a fallback.

## Anti-pseudoreplication structure / 의사반복 방지 구조

Flights are nested observations.

Before any weather or delay magnitude is analyzed, F01 must report:
- unique origin AirportIDs;
- unique eligible NOAA station IDs;
- airport→station multiplicity;
- station×local-date support keys;
- station×local-hour support keys if defensible;
- number of flights nested under exposure keys.

Minimum PASS support:
- >=50 origin airports;
- >=40 unique NOAA stations;
- all 12 months of 2025 supported.

Shared weather stations are shared exposure clusters, not independent airport weather units.

## Spatial rule / 공간 규칙

Outcome-blind order:
1. BTS time-valid AirportID/SeqID;
2. BTS Master Coordinate latitude/longitude;
3. NOAA LCDv2 station metadata;
4. exact documented airport/station identity or co-location if available;
5. otherwise one prospectively frozen nearest-station cap;
6. ambiguous/tied/out-of-cap airports excluded.

No commercial geocoder and no result-based manual repair.

## Temporal rule / 시간 규칙

Freeze before effect analysis:
- BTS local-time semantics;
- NOAA observation timestamp/time-zone semantics;
- daylight-saving treatment;
- airport local-date/hour conversion;
- whether future weather exposure grain is station-day or station-hour.

## Allowed F01 diagnostics / 허용 진단

Allowed:
- source and schema metadata;
- bytes/hashes/download identity;
- row/key counts;
- null/duplicate/status counts;
- IDs/coordinates/time support;
- bounded samples needed to validate source mechanics.

Not allowed:
- weather–delay correlation/regression;
- descriptive delay by weather;
- weather-value ranking;
- airport/carrier sensitivity;
- threshold selection;
- network propagation estimate;
- causal or policy/investment claims.

## Gate / 게이트

- PASS: `PASS_US_AIR_AIRPORT_WEATHER_JOIN_READY`
- PARTIAL: `PARTIAL_US_AIR_JOIN_OR_TIME_SEMANTICS`
- HOLD: `HOLD_US_AIR_PUBLIC_WEATHER_OR_DOWNLOAD_ROUTE`
- REJECT: `REJECT_US_AIR_INDEPENDENT_EXPOSURE_SUPPORT`

## Stop rule / 중단 규칙

Fail closed and return to Stage 0 if:
- reproducible official BTS 2025 download cannot be established;
- airport→station mapping needs subjective repair;
- support is below 50 airports / 40 stations;
- temporal alignment cannot be frozen;
- a source/outcome substitution is proposed after failure;
- paid data or paid compute becomes necessary.

## Cost / 비용

Incremental monetary cost must remain **0 USD**. Any potentially billable action requires explicit prior approval.


## Final disposition / 최종 처분

Issue #88 completed under `DEC-122` with **`PASS_US_AIR_AIRPORT_WEATHER_JOIN_READY`**. / Issue #88은 `DEC-122`에 따라 JOIN_READY PASS로 완료됐다.

Final outcome-blind support is **263 origin airports, 263 unique NOAA stations, and 95,995 station × calendar-date source keys** after full-year identity, frozen 10 km mapping and 365-DATE support. / 연중 식별·고정 10km·365 DATE 기준 후 최종 지원도는 263개 공항·263개 관측소·95,995개 station-date key다.

See `RESULT.md` and `TEMPORAL_SEMANTIC_ADJUDICATION.md`. E01 is not automatically authorized. / E01은 자동 승인되지 않는다.
