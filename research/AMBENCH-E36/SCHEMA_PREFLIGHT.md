---
id: AMBENCH-E36-SCHEMA-PREFLIGHT
type: schema-missingness-preflight
created: 2026-08-23
raw_analysis_numerical_values_emitted: false
raw_analysis_statistics_computed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E36 RHF Analysis Schema Preflight / RHF 분석 Schema 사전점검

## Boundary / 경계
- Checksum-frozen `RHF_Analysis_Results.zip` only.
- Numerical data cells are **not emitted** and no min/max/mean/median/std/correlation/group comparison is computed from result values.
- Only member identity, CSV header/order, row count, missing/non-empty counts and lexical type counts are used.

## Source integrity / source 무결성
- dataset: `mds2-2507`
- NERDm version: `1.0.1`
- archive_size_nerdm: `1637430`
- archive_size_local: `1637430`
- size_match: `True`
- sha256_nerdm: `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`
- sha256_preregistered: `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`
- sha256_local: `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`
- checksum_match_all: `True`

## Member identity / member identity
- matching_analysis_csv_count: `55`
- part_ids: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]`
- exact_P01_to_P55: `True`
- members:
  - `P01` | path=`DAQ_RHF_P01_layer0001_T80_XYPVALWI.csv` | size=`95019` | data_rows=`1497` | ragged_rows=`0`
  - `P02` | path=`DAQ_RHF_P02_layer0001_T80_XYPVALWI.csv` | size=`94969` | data_rows=`1497` | ragged_rows=`0`
  - `P03` | path=`DAQ_RHF_P03_layer0001_T80_XYPVALWI.csv` | size=`94895` | data_rows=`1497` | ragged_rows=`0`
  - `P04` | path=`DAQ_RHF_P04_layer0001_T80_XYPVALWI.csv` | size=`95031` | data_rows=`1497` | ragged_rows=`0`
  - `P05` | path=`DAQ_RHF_P05_layer0001_T80_XYPVALWI.csv` | size=`95123` | data_rows=`1497` | ragged_rows=`0`
  - `P06` | path=`DAQ_RHF_P06_layer0001_T80_XYPVALWI.csv` | size=`95465` | data_rows=`1497` | ragged_rows=`0`
  - `P07` | path=`DAQ_RHF_P07_layer0001_T80_XYPVALWI.csv` | size=`93603` | data_rows=`1497` | ragged_rows=`0`
  - `P08` | path=`DAQ_RHF_P08_layer0001_T80_XYPVALWI.csv` | size=`93543` | data_rows=`1497` | ragged_rows=`0`
  - `P09` | path=`DAQ_RHF_P09_layer0001_T80_XYPVALWI.csv` | size=`93475` | data_rows=`1497` | ragged_rows=`0`
  - `P10` | path=`DAQ_RHF_P10_layer0001_T80_XYPVALWI.csv` | size=`93446` | data_rows=`1497` | ragged_rows=`0`
  - `P11` | path=`DAQ_RHF_P11_layer0001_T80_XYPVALWI.csv` | size=`93534` | data_rows=`1497` | ragged_rows=`0`
  - `P12` | path=`DAQ_RHF_P12_layer0001_T80_XYPVALWI.csv` | size=`94868` | data_rows=`1497` | ragged_rows=`0`
  - `P13` | path=`DAQ_RHF_P13_layer0001_T80_XYPVALWI.csv` | size=`94916` | data_rows=`1497` | ragged_rows=`0`
  - `P14` | path=`DAQ_RHF_P14_layer0001_T80_XYPVALWI.csv` | size=`94860` | data_rows=`1497` | ragged_rows=`0`
  - `P15` | path=`DAQ_RHF_P15_layer0001_T80_XYPVALWI.csv` | size=`95048` | data_rows=`1497` | ragged_rows=`0`
  - `P16` | path=`DAQ_RHF_P16_layer0001_T80_XYPVALWI.csv` | size=`95233` | data_rows=`1497` | ragged_rows=`0`
  - `P17` | path=`DAQ_RHF_P17_layer0001_T80_XYPVALWI.csv` | size=`95423` | data_rows=`1497` | ragged_rows=`0`
  - `P18` | path=`DAQ_RHF_P18_layer0001_T80_XYPVALWI.csv` | size=`93654` | data_rows=`1497` | ragged_rows=`0`
  - `P19` | path=`DAQ_RHF_P19_layer0001_T80_XYPVALWI.csv` | size=`93539` | data_rows=`1497` | ragged_rows=`0`
  - `P20` | path=`DAQ_RHF_P20_layer0001_T80_XYPVALWI.csv` | size=`93420` | data_rows=`1497` | ragged_rows=`0`
  - `P21` | path=`DAQ_RHF_P21_layer0001_T80_XYPVALWI.csv` | size=`93325` | data_rows=`1497` | ragged_rows=`0`
  - `P22` | path=`DAQ_RHF_P22_layer0001_T80_XYPVALWI.csv` | size=`93447` | data_rows=`1497` | ragged_rows=`0`
  - `P23` | path=`DAQ_RHF_P23_layer0001_T80_XYPVALWI.csv` | size=`97207` | data_rows=`1497` | ragged_rows=`0`
  - `P24` | path=`DAQ_RHF_P24_layer0001_T80_XYPVALWI.csv` | size=`97303` | data_rows=`1497` | ragged_rows=`0`
  - `P25` | path=`DAQ_RHF_P25_layer0001_T80_XYPVALWI.csv` | size=`97245` | data_rows=`1497` | ragged_rows=`0`
  - `P26` | path=`DAQ_RHF_P26_layer0001_T80_XYPVALWI.csv` | size=`97310` | data_rows=`1497` | ragged_rows=`0`
  - `P27` | path=`DAQ_RHF_P27_layer0001_T80_XYPVALWI.csv` | size=`97433` | data_rows=`1497` | ragged_rows=`0`
  - `P28` | path=`DAQ_RHF_P28_layer0001_T80_XYPVALWI.csv` | size=`97700` | data_rows=`1497` | ragged_rows=`0`
  - `P29` | path=`DAQ_RHF_P29_layer0001_T80_XYPVALWI.csv` | size=`95905` | data_rows=`1497` | ragged_rows=`0`
  - `P30` | path=`DAQ_RHF_P30_layer0001_T80_XYPVALWI.csv` | size=`95746` | data_rows=`1497` | ragged_rows=`0`
  - `P31` | path=`DAQ_RHF_P31_layer0001_T80_XYPVALWI.csv` | size=`95743` | data_rows=`1497` | ragged_rows=`0`
  - `P32` | path=`DAQ_RHF_P32_layer0001_T80_XYPVALWI.csv` | size=`95712` | data_rows=`1497` | ragged_rows=`0`
  - `P33` | path=`DAQ_RHF_P33_layer0001_T80_XYPVALWI.csv` | size=`95743` | data_rows=`1497` | ragged_rows=`0`
  - `P34` | path=`DAQ_RHF_P34_layer0001_T80_XYPVALWI.csv` | size=`96402` | data_rows=`1497` | ragged_rows=`0`
  - `P35` | path=`DAQ_RHF_P35_layer0001_T80_XYPVALWI.csv` | size=`96534` | data_rows=`1497` | ragged_rows=`0`
  - `P36` | path=`DAQ_RHF_P36_layer0001_T80_XYPVALWI.csv` | size=`96359` | data_rows=`1497` | ragged_rows=`0`
  - `P37` | path=`DAQ_RHF_P37_layer0001_T80_XYPVALWI.csv` | size=`96452` | data_rows=`1497` | ragged_rows=`0`
  - `P38` | path=`DAQ_RHF_P38_layer0001_T80_XYPVALWI.csv` | size=`96685` | data_rows=`1497` | ragged_rows=`0`
  - `P39` | path=`DAQ_RHF_P39_layer0001_T80_XYPVALWI.csv` | size=`97049` | data_rows=`1497` | ragged_rows=`0`
  - `P40` | path=`DAQ_RHF_P40_layer0001_T80_XYPVALWI.csv` | size=`95188` | data_rows=`1497` | ragged_rows=`0`
  - `P41` | path=`DAQ_RHF_P41_layer0001_T80_XYPVALWI.csv` | size=`95149` | data_rows=`1497` | ragged_rows=`0`
  - `P42` | path=`DAQ_RHF_P42_layer0001_T80_XYPVALWI.csv` | size=`94936` | data_rows=`1497` | ragged_rows=`0`
  - `P43` | path=`DAQ_RHF_P43_layer0001_T80_XYPVALWI.csv` | size=`94942` | data_rows=`1497` | ragged_rows=`0`
  - `P44` | path=`DAQ_RHF_P44_layer0001_T80_XYPVALWI.csv` | size=`94933` | data_rows=`1497` | ragged_rows=`0`
  - `P45` | path=`DAQ_RHF_P45_layer0001_T80_XYPVALWI.csv` | size=`96378` | data_rows=`1497` | ragged_rows=`0`
  - `P46` | path=`DAQ_RHF_P46_layer0001_T80_XYPVALWI.csv` | size=`96486` | data_rows=`1497` | ragged_rows=`0`
  - `P47` | path=`DAQ_RHF_P47_layer0001_T80_XYPVALWI.csv` | size=`96485` | data_rows=`1497` | ragged_rows=`0`
  - `P48` | path=`DAQ_RHF_P48_layer0001_T80_XYPVALWI.csv` | size=`96651` | data_rows=`1497` | ragged_rows=`0`
  - `P49` | path=`DAQ_RHF_P49_layer0001_T80_XYPVALWI.csv` | size=`96820` | data_rows=`1497` | ragged_rows=`0`
  - `P50` | path=`DAQ_RHF_P50_layer0001_T80_XYPVALWI.csv` | size=`97001` | data_rows=`1497` | ragged_rows=`0`
  - `P51` | path=`DAQ_RHF_P51_layer0001_T80_XYPVALWI.csv` | size=`95080` | data_rows=`1497` | ragged_rows=`0`
  - `P52` | path=`DAQ_RHF_P52_layer0001_T80_XYPVALWI.csv` | size=`95187` | data_rows=`1497` | ragged_rows=`0`
  - `P53` | path=`DAQ_RHF_P53_layer0001_T80_XYPVALWI.csv` | size=`95000` | data_rows=`1497` | ragged_rows=`0`
  - `P54` | path=`DAQ_RHF_P54_layer0001_T80_XYPVALWI.csv` | size=`95080` | data_rows=`1497` | ragged_rows=`0`
  - `P55` | path=`DAQ_RHF_P55_layer0001_T80_XYPVALWI.csv` | size=`95133` | data_rows=`1497` | ragged_rows=`0`

## Header/schema consistency / header·schema 일관성
- header_consistent_all_55: `False`
- header_column_count: `10`
- canonical_header: `['-26.504', '9.0043', '29.631', '740', '0', '0', '0', '0.010764', '0', '0']`
- area_column_hits_1based: `[]`
- length_column_hits_1based: `[]`
- width_column_hits_1based: `[]`
- required_columns_unique: `False`
- total_ragged_rows: `0`

## Required physical-outcome column occupancy / 필수 물리 outcome 열 점유
### `area`
- required_column: `NOT_UNIQUELY_IDENTIFIED`

### `length`
- required_column: `NOT_UNIQUELY_IDENTIFIED`

### `width`
- required_column: `NOT_UNIQUELY_IDENTIFIED`

## Per-part lexical occupancy / part별 lexical 점유
- The following records contain counts only; no numerical result value is emitted.


## Frozen schema gate / 고정 schema gate
- source_integrity: `True`
- exact_part_coverage: `True`
- header_consistency: `False`
- required_area_length_width_unique: `False`
- required_column_occupancy: `False`
- no_ragged_rows: `True`

**HOLD_E36_SCHEMA_OR_IDENTITY_GAP**
- Numerical result access remains prohibited.

