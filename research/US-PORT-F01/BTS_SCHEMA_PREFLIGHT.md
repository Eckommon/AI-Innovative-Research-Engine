---
id: US-PORT-F01-BTS-SCHEMA-PREFLIGHT
type: bounded-source-schema-preflight
created: 2026-09-03
source_of_truth: github-actions
raw_rows_committed: false
weather_effect_analysis_performed: false
incremental_monetary_cost_usd: 0
---

# US-PORT-F01 BTS Schema Preflight / BTS schema 사전검증

- purpose: source identity / schema / access only
- outcome values emitted: NO
- weather data opened: NO
- dashboard scraping/reverse engineering: NO

## Frozen BTS dataset / 고정 BTS 데이터셋
- columns_endpoint: FAIL (HTTPError)

- source_row_count: 54

## Bounded first-50 identity inspection / 최초 50행 identity 제한 검증
- sample_endpoint_status: 200
- sample_payload_SHA256: `058c244fa6c1259ccbf5339839190b8a71115db064e65436c5dc16fed64aa259`
- sample_row_count: 50
- all_api_keys: `['hours', 'month', 'month_year', 'q_year', 'quarter', 'year']`
- permitted_identity_keys: `['month', 'month_year', 'q_year', 'year']`
- identity_values[month]: `['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']`
- identity_values[month_year]: `['2019-01-01T00:00:00.000', '2019-02-01T00:00:00.000', '2019-03-01T00:00:00.000', '2019-04-01T00:00:00.000', '2019-05-01T00:00:00.000', '2019-06-01T00:00:00.000', '2019-07-01T00:00:00.000', '2019-08-01T00:00:00.000', '2019-09-01T00:00:00.000', '2019-10-01T00:00:00.000', '2019-11-01T00:00:00.000', '2019-12-01T00:00:00.000', '2020-01-01T00:00:00.000', '2020-02-01T00:00:00.000', '2020-03-01T00:00:00.000', '2020-04-01T00:00:00.000', '2020-05-01T00:00:00.000', '2020-06-01T00:00:00.000', '2020-07-01T00:00:00.000', '2020-08-01T00:00:00.000']`
- identity_values[q_year]: `['2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', '2023-Q1']`
- identity_values[year]: `['2019', '2020', '2021', '2022', '2023']`

- numerical dwell/berth/call-support values emitted: NO

## Semantic role check / semantic role 검증
- explicit_port_field_detected: NO
- explicit_week_field_detected: NO
- explicit_month_field_detected: NO
- explicit_year_field_detected: NO
- dwell_or_berth_metric_field_detected: NO
- call_or_support_field_detected: NO

## Current weekly-berthing asset discovery / 현재 weekly berthing asset 탐색
- Socrata_catalog_status: 200
- Socrata_catalog_SHA256: `dff7949ddc1e910bef00bb581f5843a848b27e1f497e42be7e1f88551f30fc1b`
- result_count: 20
- discovery_scope: metadata only; no dashboard content queried
- result: id=`4kd6-2t87` type=`story` name=`Vessel Berthing Times` permalink=`https://data.bts.gov/stories/s/4kd6-2t87`
- result: id=`abu9-jbyq` type=`dataset` name=`Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023` permalink=`https://data.bts.gov/d/abu9-jbyq`
- result: id=`nfsh-p62e` type=`dataset` name=`Monthly Average Container Vessel Dwell Times at the Top 25 U.S. Container Ports January 2019 to June 2023` permalink=`https://data.bts.gov/d/nfsh-p62e`
- result: id=`xqz2-92fw` type=`story` name=`Introduction` permalink=`https://data.bts.gov/stories/s/xqz2-92fw`
- result: id=`ht8q-b5eg` type=`story` name=`Economic Impact of U.S. Ports` permalink=`https://data.bts.gov/stories/s/ht8q-b5eg`
- result: id=`prsc-k6eu` type=`story` name=`Air Draft & Channel Depths` permalink=`https://data.bts.gov/stories/s/prsc-k6eu`
- result: id=`ari2-ub6a` type=`story` name=`Tanker Vessel Dwell Times` permalink=`https://data.bts.gov/stories/s/ari2-ub6a`
- result: id=`ngjm-b5rq` type=`dataset` name=`Containerized Imports' Value and Weight by Port in 2023` permalink=`https://data.bts.gov/d/ngjm-b5rq`
- result: id=`vc8a-zq94` type=`dataset` name=`Containerized Exports' Value and Weight by Port in 2023` permalink=`https://data.bts.gov/d/vc8a-zq94`
- result: id=`5tut-fj6e` type=`story` name=`Supply-Chain Challenges` permalink=`https://data.bts.gov/stories/s/5tut-fj6e`
- result: id=`j4yu-qgj6` type=`story` name=`Rail & Road Connections` permalink=`https://data.bts.gov/stories/s/j4yu-qgj6`
- result: id=`uxyn-8v2z` type=`dataset` name=`Cruise Ship Counts and Passengers by Arrival at Ports Top 25 Ports 2019 thru 2023` permalink=`https://data.bts.gov/d/uxyn-8v2z`
- result: id=`ryjr-58ty` type=`story` name=`Record Low Water on the Mississippi and Ohio Rivers` permalink=`https://data.bts.gov/stories/s/ryjr-58ty`
- result: id=`rjzd-p9xx` type=`dataset` name=`2020 PM` permalink=`https://data.bts.gov/d/rjzd-p9xx`
- result: id=`y5ut-ibwt` type=`dataset` name=`Supply Chain and Freight Indicators` permalink=`https://data.bts.gov/d/y5ut-ibwt`
- result: id=`mjx8-bw4c` type=`dataset` name=`Value of Containerized Exports by Coast in 2023` permalink=`https://data.bts.gov/d/mjx8-bw4c`
- result: id=`ub6a-sqr5` type=`dataset` name=`Value of Containerized Imports by Coast in 2023` permalink=`https://data.bts.gov/d/ub6a-sqr5`
- result: id=`7mzw-a8si` type=`dataset` name=`U.S. Imports and Exports Value by Year and Mode 2003 thru 2023` permalink=`https://data.bts.gov/d/7mzw-a8si`
- result: id=`iahn-a7j4` type=`dataset` name=`20-Foot Equivalent Units (TEU) Handled by Select U.S. Container Ports January 2020 to August 2023` permalink=`https://data.bts.gov/d/iahn-a7j4`
- result: id=`iiy2-kmkn` type=`dataset` name=`Weekly Number of Container Ships Awaiting to Dock at All U.S. Ports: July 2021 to September 2023` permalink=`https://data.bts.gov/d/iiy2-kmkn`

## BTS-only preflight gate / BTS 단독 사전검증 판정
**`HOLD_BTS_SOURCE_ACCESS_OR_SCHEMA_UNRESOLVED`**

This is not the final US-PORT-F01 gate. NOAA/geography are not evaluated here.
본 결과는 최종 US-PORT-F01 판정이 아니다. NOAA/지리 조인은 아직 평가하지 않았다.

- weather→dwell association computed: NO
- incremental monetary cost: 0 USD
