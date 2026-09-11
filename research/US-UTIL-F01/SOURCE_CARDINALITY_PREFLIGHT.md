---
id: US-UTIL-F01-SOURCE-CARDINALITY-PREFLIGHT
type: outcome-blind-source-identity-result
created: 2026-09-11
issue: 94
gate: HOLD_US_UTIL_F01_SOURCE_IDENTITY_CARDINALITY
reliability_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 Source / Identity / Cardinality Preflight
# US-UTIL-F01 Source / Identity / Cardinality 사전검증

## Outcome-blind boundary / 결과 비사용 경계

The reliability workbook was parsed only through the Utility Number identity column. No SAIDI/SAIFI or other reliability magnitude was read into the analysis. No AMI or storm effect was estimated. / Reliability는 Utility Number identity만 읽었고 SAIDI/SAIFI 값 및 관계효과는 열지 않았다.

## Source materialization / source materialization

- EIA-861 2024 final ZIP: HTTP **200**, bytes **4,568,208**, SHA-256 `77ce49c60ac5a6bad50c442fc401aad5404a21da875dc5cbaba353af5ede54de`
- EIA reliability member: `Reliability_2024.xlsx`
- EIA Advanced Metering member: `Advanced_Meters_2024.xlsx`
- EIA Service Territory member: `Service_Territory_2024.xlsx`
- NOAA details: `StormEvents_details-ftp_v1.0_d2024_c20260728.csv.gz`, bytes **12,693,243**, SHA-256 `2070b83eccab041b36360ab73645b9a249c3eefc5b92b5b3fc0cbba4d9fcc09c`
- NOAA locations: `StormEvents_locations-ftp_v1.0_d2024_c20260728.csv.gz`, rows **41,574**, bytes **983,723**, SHA-256 `8847a6336e1af94000f7ecfb4a80c06bf0d5c1ac122fe39da5b2e379dc62c1b4`

## EIA identity cardinality / EIA identity cardinality

- Reliability unique Utility Numbers: **3**
- Advanced Metering unique Utility Numbers: **8**
- Service Territory unique Utility Numbers: **5**
- Reliability ∩ Service Territory utility IDs: **3**
- Reliability ∩ Service Territory ∩ Advanced Metering utility IDs: **3**
- unique Service Territory utility×state×county keys for Reliability utilities: **84**
- same keys restricted to triple-intersection utilities: **84**

## NOAA county route / NOAA county route

- Storm Events details total rows: **69,801**
- county-type (`CZ_TYPE=C`) rows: **39,718**
- unique county FIPS keys: **3,063**
- unique deterministic USPS-state × normalized-county-name keys: **2,984**
- EIA Service Territory unique normalized state×county keys: **90**
- exact normalized EIA↔NOAA county-name keys: **0** (0.00% of EIA unique county keys)

The normalized-name comparison is diagnostic only. It is deterministic, not fuzzy, and is not yet a customer-allocation weight. Unmatched keys are retained for a later explicit county-key adjudication if needed. / 정규화 name 비교는 진단용이며 fuzzy matching이 아니다.

## Frozen structural thresholds / 고정 구조 기준

- >=300 Reliability utilities joined to Service Territory: **False** (3)
- >=250 of those with Advanced Metering support: **False** (3)
- >=1,000 qualified utility×county mappings: **False** (84)
- reproducible NOAA 2024 county-key route: **True**

## Gate / 판정

**`HOLD_US_UTIL_F01_SOURCE_IDENTITY_CARDINALITY`**

A structural PASS authorizes only the next outcome-blind county-key/join qualification step. It does not authorize reading reliability magnitudes or estimating an AMI/storm effect. / 구조 PASS는 다음 join qualification만 허용한다.

## Durable derived artifacts / 영속 파생 산출물

- `research/US-UTIL-F01/SOURCE_MANIFEST.csv`
- `research/US-UTIL-F01/EIA_MEMBER_MANIFEST.csv`
- `research/US-UTIL-F01/SCHEMA_MANIFEST.csv`
- `research/US-UTIL-F01/COUNTY_KEY_DIAGNOSTIC.csv`

Raw ZIP/XLSX/GZ/CSV bytes were transient and are not persisted.

Incremental monetary cost remained **0 USD**.
