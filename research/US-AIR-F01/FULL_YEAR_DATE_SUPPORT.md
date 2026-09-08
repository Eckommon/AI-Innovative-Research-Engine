---
id: US-AIR-F01-FULL-YEAR-DATE-SUPPORT
type: outcome-blind-full-year-support
created: 2026-09-08
issue: 88
frozen_distance_cap_km: 10.0
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Full-Year Identity x NOAA DATE Support
# US-AIR-F01 연중 식별자 x NOAA DATE 지원도

## Exposure boundary / 노출 경계

- BTS delay magnitudes were not parsed or summarized.
- DepDelayMinutes was inspected only as blank/nonblank structure under the frozen eligibility contract.
- NOAA station-year payloads were inspected only for the STATION and DATE prefixes; weather measurement columns were not interpreted.
- Raw BTS and NOAA payloads were temporary and were not persisted.

## A. BTS 2025 identity source

| Month | ZIP bytes | SHA-256 | rows | Origin AirportID | Origin AirportSeqID |
|---:|---:|---|---:|---:|---:|
| 1 | 31599374 | 0feaabdbc9e4bd851ef717f342678cdcc5ea0822dd706359aab030bb1a5d1c24 | 599013 | 352 | 352 |
| 2 | 29442140 | 080ad48e2826a6b4c3f39690f75a08dea9ad4e0831ff82958656cdb61693dd15 | 559577 | 353 | 353 |
| 3 | 35460382 | ad3f46a598bd529588bfcc004731b893b27999a681804a07a3841b2904d66d48 | 664932 | 353 | 353 |
| 4 | 34062432 | 88b88ae1a9b49a03cb82c835481ac8dcf86ff2d378614655638889866767608f | 644084 | 353 | 353 |
| 5 | 35708775 | 261fb75b956abedca34a27db3ae7221437e1a2ce349b5ee9a49ec267d7555b29 | 667586 | 357 | 357 |
| 6 | 36074147 | 0cb4038a49962ab92cba33f9840a8eec9671ef19a5afeedfa27998984476b609 | 674179 | 360 | 360 |
| 7 | 37234575 | 4aa0c2b27f4f2cbd2d4ec9e2b6eddd323f6bc9148939200ed3526760e48355dd | 696049 | 360 | 360 |
| 8 | 35785563 | ecbf30c1fd69d43db430915daa90a109d8be981461fd13efcc43db0209ea108e | 666242 | 363 | 363 |
| 9 | 32624136 | 852dee3ba0dc7ab124440eac58056e27744f79a73ed2c92b3f59dae3eef12d2e | 621601 | 360 | 360 |
| 10 | 35550100 | 60e14dd57856474a351b77935f9e004f05d43aaa37e2c0411f05a6a303c8f3ec | 668332 | 361 | 361 |
| 11 | 33429487 | 858ba018a0f4bea73b140a4052586b492c3790300f5726851593ab3161d26eba | 630188 | 357 | 357 |
| 12 | 35337872 | 5597d2d99bc2c2ca92bad7837effe853cac07126e9447498db7bbfb25b834522 | 644987 | 359 | 359 |

- total identity rows: **7,736,770**
- union Origin AirportIDs: **364**
- AirportIDs present in all 12 months: **349**
- unique AirportID/SeqID pairs: **528**
- unique Origin AirportSeqIDs: **528**
- monthly header consistency: **True**
- FlightDate parse errors: **0**

### Structural status vocabulary

- Cancelled: {'0.00': 7618602, '1.00': 118168}
- Diverted: {'0.00': 7715664, '1.00': 21106}
- Duplicate: {'N': 7736770}
- Frozen eligibility: exclude Duplicate; exclude Cancelled for continuous DepDelayMinutes; retain non-cancelled Diverted rows when DepDelayMinutes is nonblank.

## B. Master Coordinate full-year identity

- materialized ZIP bytes: **325,900**
- SHA-256: f12537d5865c4fd4334a6695a35b65d73887f02b5944d0811918447f3add8fef
- CSV member: T_MASTER_CORD.csv
- CSV rows: **20,283**
- distinct AirportSeqIDs: **20,283**
- conflicting duplicate AirportSeqIDs: **0**

## C. Frozen 10 km full-year mapping

- derived AirportID/SeqID mapping rows: **528**
- all-12-month airports: **349**
- spatial-qualified airports requiring every observed SeqID to pass: **337**
- unique NOAA stations used by spatial-qualified airports: **340**
- mapping status counts: {'PASS': 513, 'AMBIGUOUS_TIE': 5, 'OVER_10KM': 10}
- >=50 airport spatial threshold: **True**
- >=40 station spatial threshold: **True**

## D. NOAA 2025 DATE-only support

- station-year files requested: **340**
- stations with complete 365 DATE labels: **265**
- fetch errors: **18**
- stations with missing 2025 DATE labels: **75**
- final date-supported airports: **263**
- final unique NOAA stations: **263**
- source-supported station x calendar-date keys: **95,995**
- >=50 airport DATE-support threshold: **True**
- >=40 station DATE-support threshold: **True**

DATE presence is source support only. It does not prove usable weather-variable completeness, quality, statistical independence, or an effect.

## E. Reusable derived manifests

- research/US-AIR-F01/DERIVED_AIRPORT_SEQ_STATION_MAP.csv
- research/US-AIR-F01/DERIVED_AIRPORT_SUPPORT.csv
- research/US-AIR-F01/DERIVED_NOAA_DATE_SUPPORT.csv
- research/US-AIR-F01/FINAL_SUPPORT_AIRPORTS.csv

No raw BTS ZIP/CSV or NOAA station-year CSV is persisted.

## Structural/date gate

**PASS_US_AIR_F01_FULL_YEAR_IDENTITY_DATE_SUPPORT**

This is not the final F01 research gate. Final adjudication must separately resolve NOAA LST DATE-window versus BTS local civil-date semantics.

Incremental monetary cost remains **0 USD**.
