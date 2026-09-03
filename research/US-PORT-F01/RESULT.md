---
id: US-PORT-F01-RESULT
type: source-semantic-join-feasibility-result
created: 2026-09-04
issue: 72
state: COMPLETED_HOLD
final_gate: HOLD_US_PORT_PUBLIC_JOIN_ROUTE
weather_effect_analysis_performed: false
incremental_monetary_cost_usd: 0
---

# US-PORT-F01 Result — BTS Berthing × NOAA Weather Join Feasibility
# US-PORT-F01 결과 — BTS 선박 접안시간 × NOAA 기상 join 가능성

## Final gate / 최종 판정

**`HOLD_US_PORT_PUBLIC_JOIN_ROUTE`**

## Korean summary / 한국어 요약

공식 미국 공공데이터만으로 `port-time vessel dwell/berthing × weather-event` 관계를 재현 가능하게 구성할 수 있는지 source-semantic/join feasibility만 검증했다.

NOAA Storm Events와 USACE/BTS port geography 쪽은 재현 가능한 공식 경로가 확인되었으나, BTS의 공개 machine-readable dwell/berthing outcome 자산에서는 **port identity가 확인되지 않았다**. 따라서 현재 zero-cost, no-scraping 경로에서는 deterministic `port × time` outcome table을 만들 수 없으며 F01은 HOLD로 종료한다.

기상→dwell 효과값, 상관계수, 회귀계수, 유의성 또는 방향성은 계산하지 않았다.

## English summary

F01 evaluated only whether official U.S. public data can support a reproducible `port-time vessel dwell/berthing × weather-event` relationship.

The NOAA Storm Events and USACE/BTS geography sides have reproducible official source paths, but the public BTS machine-readable dwell/berthing outcome assets inspected do **not expose a port identity field**. Therefore a deterministic `port × time` dwell table cannot be established on the current zero-cost, no-scraping route, and F01 resolves to HOLD.

No weather→dwell effect, correlation, regression, significance test, or directional claim was computed.

## 1. BTS machine-readable outcome qualification / BTS 기계판독 outcome 검증

Two bounded GitHub Actions preflights were executed with raw outcome values excluded from durable output.

### Initial schema preflight

`research/US-PORT-F01/BTS_SCHEMA_PREFLIGHT.md`

- official Socrata dataset `abu9-jbyq` responded through the public resource API;
- source row count: `54`, matching the title interval January 2019 through June 2023 at monthly grain;
- bounded first-50 sample exposed time identity keys only: `month`, `month_year`, `q_year`, `year`;
- no port identity appeared in the sampled API keys;
- the first attempt at the dedicated columns endpoint returned HTTP error, so no final conclusion was taken from that failure alone.

BTS-only interim gate:
`HOLD_BTS_SOURCE_ACCESS_OR_SCHEMA_UNRESOLVED`.

### Metadata-only catalog discovery

`research/US-PORT-F01/BTS_ASSET_DISCOVERY.md`

Five official Socrata catalog searches were frozen to source semantics only:
- `vessel dwell`;
- `vessel berthing`;
- `container vessel dwell`;
- `tanker vessel dwell`;
- `port dwell time`.

The official catalog returned three dataset-type assets within the bounded semantic search. Exact view metadata was then inspected without opening dataset row values.

Relevant dwell datasets:

1. `abu9-jbyq` — Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023
   - columns: `Month`, `Year`, `Hours`, `Quarter`, `Q-Year`, `Month-Year`;
   - explicit port field: **NO**;
   - dwell/berth metric field: **YES**;
   - explicit time field: **YES**;
   - call/support field: **NO**.

2. `nfsh-p62e` — Monthly Average Container Vessel Dwell Times at the Top 25 U.S. Container Ports January 2019 to June 2023
   - same six-column schema;
   - explicit port field: **NO**;
   - dwell/berth metric field: **YES**;
   - explicit time field: **YES**;
   - call/support field: **NO**.

Metadata-only discovery gate:
**`HOLD_NO_MACHINE_READABLE_PORT_TIME_DWELL_DATASET_DISCOVERED`**.

BTS technical documentation confirms that underlying dwell calculations are performed within defined port/terminal geofences and that summary statistics can be calculated for each port area. BTS documentation and the Port Performance site also state that individual-port dwell values are shown in interactive Port Profiles. However, F01 did not identify a stable public machine-readable `port × time × dwell` table corresponding to those profile values.

The preregistered branch-stop rule prohibits opaque dashboard scraping or reverse engineering merely to recover such values.

## 2. Port geography / 항만 지리

This component is **source-ready**.

Official BTS/USACE evidence establishes nationally consistent port definitions and machine-readable geospatial assets:

- BTS states that the Port Performance program follows USACE statistical port definitions for national consistency.
- BTS/NTAD distributes `Port Areas` and `Port Statistical Areas` in common geospatial/download formats, including GeoJSON/CSV/WFS routes.
- Data.gov identifies the `Port Statistical Areas` dataset as USACE-published and part of BTS NTAD.

This provides a defensible official geographic anchor without manually inventing port boundaries.

Primary official references:
- https://www.bts.gov/PPFS-Tech-Docs
- https://www.bts.gov/newsroom/bts-updates-datasets-national-transportation-atlas-database-summer-2025
- https://catalog.data.gov/dataset/port-statistical-areas

## 3. NOAA Storm Events semantics / NOAA Storm Events semantics

This component is **source-ready** for a later preregistered mapping if an outcome table becomes available.

The official NOAA/NCEI Storm Events bulk distribution provides yearly `details`, `locations`, and `fatalities` files linked by `event_id`. The official bulk format documents, among others:

- `begin_yearmonth`, `begin_day`, `begin_time`;
- `end_yearmonth`, `end_day`, `end_time`;
- `begin_date_time`, `end_date_time`, `cz_timezone`;
- `cz_type` identifying County / Forecast Zone / Marine;
- `cz_fips`, `cz_name`, `state`;
- `begin_lat`, `begin_lon`, `end_lat`, `end_lon` where applicable;
- `event_id` as the cross-file key.

The live bulk directory currently exposes annual files and creation dates, which supports snapshot/version pinning.

Primary official references:
- https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/
- https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Bulk-csv-Format.pdf

## 4. Overlap / 공통 기간

A temporal overlap exists in principle: the inspected BTS dwell assets cover January 2019 through June 2023 and NOAA Storm Events publishes annual data covering that interval.

However, F01 does **not** treat temporal overlap alone as a valid common analytical panel. Because the machine-readable BTS dwell assets lack port identity, a deterministic `port × time` overlap cannot be constructed under the frozen route.

## 5. Integrity / 무결성

Reproducibility assets preserved:

- `BTS_SCHEMA_PREFLIGHT.md` records sanitized API/schema diagnostics and sample payload SHA-256;
- `BTS_ASSET_DISCOVERY.md` records five catalog-response SHA-256 values and exact Socrata view-metadata SHA-256 values;
- NOAA bulk files encode both data year and creation date in filenames;
- official port-geography datasets have version/update metadata through BTS/USACE/Data.gov.

No paid source, paid runner, credential-heavy API, dashboard scraping, or commercial weather source was used.

## 6. Gate application / 게이트 적용

The preregistered PASS requires all of:

- stable official machine-readable BTS dwell/berthing table;
- exact time/port/dwell/support semantics;
- deterministic official port geography;
- compatible NOAA temporal/geographic fields;
- bounded common period;
- reproducible revision/snapshot/hash plan.

The BTS outcome layer fails the required **port identity** condition. Therefore PASS and PARTIAL are not justified.

**Final: `HOLD_US_PORT_PUBLIC_JOIN_ROUTE`.**

## 7. Branch stop / branch 중단

Do not create a dashboard-scraping, reverse-engineering, or ad-hoc manual port-mapping descendant to rescue this exact F01 route.

Return to mandatory Stage 0 Mission-ROI portfolio selection. `C-US-002` may be reconsidered only if a new stable official machine-readable port-level dwell/berthing source appears or if a separately selected outcome changes the research framing before exposure.

Incremental monetary cost remained **0 USD**.
