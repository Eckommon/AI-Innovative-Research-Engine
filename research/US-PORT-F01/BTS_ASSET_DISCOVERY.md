---
id: US-PORT-F01-BTS-ASSET-DISCOVERY
type: metadata-only-source-discovery
created: 2026-09-04
raw_rows_opened: false
outcome_values_emitted: false
weather_data_opened: false
incremental_monetary_cost_usd: 0
---

# US-PORT-F01 BTS Metadata-only Asset Discovery / BTS metadata 전용 자산 탐색

- source: official Socrata public catalog for `data.transportation.gov`
- dataset row values queried: NO
- dashboard scraping/reverse engineering: NO
- weather→dwell effect analysis: NO

## Catalog query integrity / 카탈로그 query 무결성
- `vessel dwell`: HTTP 200; SHA256 `37c369bfc2acb143f1604c828bd91d64867bbff9007e86edeb1ac6c4211ea520`
- `vessel berthing`: HTTP 200; SHA256 `f09fa28db84db7b3a7d66785afb9d328370a6ab43d57015822708d78ceedbd09`
- `container vessel dwell`: HTTP 200; SHA256 `8cb6fb44946b5959dd1ae1cc3754044d22cb2f9ab88d09a5bac0175c86bed500`
- `tanker vessel dwell`: HTTP 200; SHA256 `01c55fc334e52cd1258c06b43248ffc1141dfa77629c35943398c9b2cf4b8783`
- `port dwell time`: HTTP 200; SHA256 `2cc2df91afe2e4ff75a4099bf18ec60edc6dc9fde917d21fd94bba0e97bb00d9`

## Dataset-type assets discovered / 발견된 dataset 자산
- unique_dataset_count: 3

### `abu9-jbyq` — Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023
- permalink: `https://data.bts.gov/d/abu9-jbyq`
- view_metadata_status: 200
- view_metadata_SHA256: `53ccd2a7420e869af079b01af7542dfaa61a9250045230d68b829500d312c7a9`
- column_count: 6
- explicit_port_field_detected: NO
- dwell_or_berth_metric_field_detected: YES
- explicit_time_field_detected: YES
- call_or_support_field_detected: NO

| display_name | api_field | type | description |
|---|---|---|---|
| `Month` | `month` | `text` |  |
| `Year` | `year` | `text` |  |
| `Hours` | `hours` | `number` |  |
| `Quarter` | `quarter` | `text` |  |
| `Q-Year` | `q_year` | `text` |  |
| `Month-Year` | `month_year` | `calendar_date` |  |

### `nfsh-p62e` — Monthly Average Container Vessel Dwell Times at the Top 25 U.S. Container Ports January 2019 to June 2023
- permalink: `https://data.bts.gov/d/nfsh-p62e`
- view_metadata_status: 200
- view_metadata_SHA256: `faaff48770e3ef5a0d7a2db4dad6d57fb195a090f9c17a40ee243b17c13df947`
- column_count: 6
- explicit_port_field_detected: NO
- dwell_or_berth_metric_field_detected: YES
- explicit_time_field_detected: YES
- call_or_support_field_detected: NO

| display_name | api_field | type | description |
|---|---|---|---|
| `Month` | `month` | `text` |  |
| `Year` | `year` | `text` |  |
| `Hours` | `hours` | `number` |  |
| `Quarter` | `quarter` | `text` |  |
| `Q-Year` | `q_year` | `text` |  |
| `Month-Year` | `month_year` | `calendar_date` |  |

### `uxyn-8v2z` — Cruise Ship Counts and Passengers by Arrival at Ports Top 25 Ports 2019 thru 2023
- permalink: `https://data.bts.gov/d/uxyn-8v2z`
- view_metadata_status: 200
- view_metadata_SHA256: `7cc115a2a1ed2b195d8d90572ff39449bdefc288dae7165fab47df2eba9f0356`
- column_count: 3
- explicit_port_field_detected: NO
- dwell_or_berth_metric_field_detected: NO
- explicit_time_field_detected: YES
- call_or_support_field_detected: YES

| display_name | api_field | type | description |
|---|---|---|---|
| `Year` | `year` | `text` |  |
| `Total Number of Arrivals` | `total_calls` | `number` |  |
| `Total Number of Passengers` | `total_number_of_passengers` | `number` |  |

## Discovery gate / 탐색 판정
- inspected_semantically_relevant_dataset_count: 3
- machine_readable_port_time_dwell_dataset_ids: `[]`

**`HOLD_NO_MACHINE_READABLE_PORT_TIME_DWELL_DATASET_DISCOVERED`**

This discovery result is source-semantic only and does not evaluate weather effects.
본 탐색은 source semantics만 검증하며 기상 효과를 평가하지 않는다.

- outcome values emitted: NO
- incremental monetary cost: 0 USD
