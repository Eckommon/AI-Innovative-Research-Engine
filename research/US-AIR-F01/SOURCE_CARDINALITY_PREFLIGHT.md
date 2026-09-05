---
id: US-AIR-F01-SOURCE-CARDINALITY-PREFLIGHT
type: source-cardinality-preflight
created: 2026-09-05
issue: 88
relationship_outcome_computed: false
weather_values_parsed: false
delay_magnitudes_parsed: false
incremental_monetary_cost_usd: 0
---

# US-AIR-F01 Source Cardinality Preflight
# US-AIR-F01 Source 독립단위 Cardinality 사전검증

## Exposure boundary / 노출 경계

- Parsed only BTS date/origin-airport identity fields needed for source-support cardinality.
- Did not index or parse departure/arrival delay magnitudes, WeatherDelay, or any NOAA weather measurement value.
- NOAA station-list latitude/longitude/name metadata were parsed; no LCDv2 observation values were downloaded.

## A. BTS 2025 monthly source bytes / BTS 2025 월별 source bytes

| Month | ZIP bytes | SHA-256 | CSV rows | Origin AirportID | Origin AirportSeqID |
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

- total parsed 2025 flight records for identity support only: 7,736,770
- union unique Origin AirportID: 364
- Origin AirportID present in all 12 months: 349
- union unique Origin AirportSeqID: 528
- Origin AirportSeqID present in all 12 months: 190
- monthly CSV headers identical across all 12 files: True
- AirportID with more than one observed 2025 origin code: 0
- AirportID with more than one 2025 OriginAirportSeqID: 164

### Frozen threshold structural check / 고정 threshold 구조 확인

- at least 50 origin AirportIDs available across 2025 source: True
- at least 50 origin AirportIDs present in every 2025 month: True
- This does not yet establish at least 40 unique NOAA stations because the deterministic coordinate join is still pending.

## B. NOAA LCDv2 station metadata / NOAA LCDv2 station metadata

- HTTP: 200
- bytes: 2,070,192
- SHA-256: 708c24f51a0eb72be8cb3d078e657723172da0f14fa167e67a97dbd596e46e1c
- parsed station rows: 24,072
- station IDs beginning US: 6,115
- U.S.-prefix station names with airport/airfield lexical markers, diagnostic only: 957
- The lexical name count is not the final airport-to-station mapping and cannot satisfy the 40-station gate by itself.

## C. BTS Master Coordinate download mechanics / BTS Master Coordinate download mechanics

- source page HTTP: 200
- source page bytes: 132,839
- source page SHA-256: 7402f14531fe9e702a1ee642b5cb5193f6a9808d5b29051a51ad11180bae7dc7
- detected forms: [('GET', 'https://search.usa.gov/search'), ('post', './DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&amp;gnoyr_VQ=FLL'), ('POST', 'Search.asp')]
- public input names (46): ['AIRPORT', 'AIRPORT_COUNTRY_CODE_ISO', 'AIRPORT_COUNTRY_NAME', 'AIRPORT_ID', 'AIRPORT_IS_CLOSED', 'AIRPORT_IS_LATEST', 'AIRPORT_SEQ_ID', 'AIRPORT_START_DATE', 'AIRPORT_STATE_CODE', 'AIRPORT_STATE_FIPS', 'AIRPORT_STATE_NAME', 'AIRPORT_THRU_DATE', 'AIRPORT_WAC', 'AIRPORT_WAC_SEQ_ID2', 'CITY_MARKET_ID', 'CITY_MARKET_SEQ_ID', 'CITY_MARKET_WAC', 'CITY_MARKET_WAC_SEQ_ID2', 'DISPLAY_AIRPORT_CITY_NAME_FULL', 'DISPLAY_AIRPORT_NAME', 'DISPLAY_CITY_MARKET_NAME_FULL', 'LATITUDE', 'LAT_DEGREES', 'LAT_HEMISPHERE', 'LAT_MINUTES', 'LAT_SECONDS', 'LONGITUDE', 'LON_DEGREES', 'LON_HEMISPHERE', 'LON_MINUTES', 'LON_SECONDS', 'UTC_LOCAL_TIME_VARIATION', '__EVENTVALIDATION', '__VIEWSTATE', '__VIEWSTATEGENERATOR', 'affiliate', 'btnDownload', 'chkAllGroups', 'chkAllVars', 'chkDocument', 'chkDownloadZip', 'chkMergeSub', 'chkTermDef', 'chkshowNull', 'query', 'txtSearch']
- public select names (3): ['cboGeography', 'cboPeriod', 'cboYear']
- PREZIP filenames matching coordinate/airport/master/support heuristic: []

### Public endpoint-hint text / 공개 endpoint 단서

- Download page
- {&quot;path&quot;:{&quot;baseUrl&quot;:&quot;\/&quot;,&quot;pathPrefix&quot;:&quot;&quot;,&quot;currentPath&quot;:&quot;standalone_template\/head&quot;,&quot;currentPathIsAdmin&quot;:false,&quot;isFront&quot;:false,&quot;currentLanguage&quot;:&quot;en&quot;},&quot;pluralDelimiter&quot;:&quot;\u0003&quot;,&quot;suppressDeprecationErrors&quot;:true,&quot;google_analytics&quot;:{&quot;account&quot;:&quot;UA-18660041-1&quot;,&quot;trackOutbound&quot;:true,&quot;trackMailto&quot;:true,&quot;trackDownload&quot;:true,&quot;trackDownloadExtensions&quot;:&quot;7z|aac|arc|arj|asf|asx|avi|bin|csv|doc(x|m)?|dot(x|m)?|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|ppt(x|m)?|pot(x|m)?|p
- Airline Information for Download
- Download Instructions
- Prezipped File&amp;nbsp;&amp;nbsp;
- AirportWac World Area Code for the Physical Location of the Airport Get Lookup Table
- CityMarketSeqID An identification number assigned by US DOT to identify a city market at a given point of time. City Market attributes may change over time. For example the country associated with the city market can change over time due to geopolitical changes. Get Lookup Table
- CityMarketID An identification number assigned by US DOT to identify a city market. Use this field to consolidate airports serving the same city market. Get Lookup Table
- CityMarketWac World Area Code for the City Market Get Lookup Table
- AirportIsClosed Indicates if the airport is closed (1 = Yes). If yes, the airport is closed is on the AirportEndDate. Get Lookup Table
- AirportIsLatest Indicates if this row contains the latest attributes for the Airport (1 = Yes) Get Lookup Table

## Interim gate / 중간 판정

CONTINUE_US_AIR_F01_MASTER_COORDINATE_MATERIALIZATION

The frozen at-least-50-airport source-side condition can now be evaluated from actual 2025 BTS identity rows, but the at-least-40 unique NOAA-station condition remains unresolved until the official BTS Master Coordinate payload is materialized and a prospective spatial rule is applied.

No weather-delay effect is authorized or computed.

## Exact next action / 정확한 다음 행동

Materialize the official BTS Master Coordinate table through the source download mechanics identified above, freeze time-valid 2025 airport coordinates, then apply one prospective airport-to-LCDv2 station distance/identity rule and report only mapping/support cardinality.

Incremental monetary cost remains 0 USD.
