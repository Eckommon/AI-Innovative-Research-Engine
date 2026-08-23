---
id: AMBENCH-F35-COMMAND-DESIGN-PREFLIGHT
type: process-input-design-preflight
created: 2026-08-23
candidate_outcomes_inspected: false
process_inputs_only: true
incremental_monetary_cost_usd: 0
---

# AMBENCH-F35 RHF Command Design Preflight / RHF Command 설계 사전점검

## Boundary / 경계
- `RHF_Command.zip` process-input CSVs only. No encoder, MPM, analysis-result, microscopy or synchronized-movie data opened.
- Persisted classification uses only whether commanded laser power is constant or variable within each PXX command file; no candidate outcome values are used.

## Source integrity / source 무결성
- dataset: `mds2-2507`
- version: `1.0.1`
- archive_size_nerdm: `18079576`
- archive_size_local: `18079576`
- sha256_nerdm: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`
- sha256_local: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`
- checksum_match: `True`

## Physical-part command inventory / physical-part command inventory
- command_csv_count: `55`
- part_ids: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]`
- exact_P01_to_P55: `True`
- constant_power_part_count: `0`
- variable_power_part_count: `55`
- expected_5_baseline_50_RHF_split: `False`
- constant_power_part_ids: `[]`
- variable_power_part_ids: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]`

## Per-part process-input classification / part별 공정입력 분류
| Part | Command path | Rows | Power field | Unique commanded power count | Class |
|---:|---|---:|---|---:|---|
| P01 | `RHF_Command/RHF_P01_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P02 | `RHF_Command/RHF_P02_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P03 | `RHF_Command/RHF_P03_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P04 | `RHF_Command/RHF_P04_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P05 | `RHF_Command/RHF_P05_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P06 | `RHF_Command/RHF_P06_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P07 | `RHF_Command/RHF_P07_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P08 | `RHF_Command/RHF_P08_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P09 | `RHF_Command/RHF_P09_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P10 | `RHF_Command/RHF_P10_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P11 | `RHF_Command/RHF_P11_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P12 | `RHF_Command/RHF_P12_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P13 | `RHF_Command/RHF_P13_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P14 | `RHF_Command/RHF_P14_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P15 | `RHF_Command/RHF_P15_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P16 | `RHF_Command/RHF_P16_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P17 | `RHF_Command/RHF_P17_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P18 | `RHF_Command/RHF_P18_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P19 | `RHF_Command/RHF_P19_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P20 | `RHF_Command/RHF_P20_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P21 | `RHF_Command/RHF_P21_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P22 | `RHF_Command/RHF_P22_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P23 | `RHF_Command/RHF_P23_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P24 | `RHF_Command/RHF_P24_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P25 | `RHF_Command/RHF_P25_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P26 | `RHF_Command/RHF_P26_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P27 | `RHF_Command/RHF_P27_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P28 | `RHF_Command/RHF_P28_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P29 | `RHF_Command/RHF_P29_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P30 | `RHF_Command/RHF_P30_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P31 | `RHF_Command/RHF_P31_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P32 | `RHF_Command/RHF_P32_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P33 | `RHF_Command/RHF_P33_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P34 | `RHF_Command/RHF_P34_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P35 | `RHF_Command/RHF_P35_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P36 | `RHF_Command/RHF_P36_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P37 | `RHF_Command/RHF_P37_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P38 | `RHF_Command/RHF_P38_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P39 | `RHF_Command/RHF_P39_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P40 | `RHF_Command/RHF_P40_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P41 | `RHF_Command/RHF_P41_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P42 | `RHF_Command/RHF_P42_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P43 | `RHF_Command/RHF_P43_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P44 | `RHF_Command/RHF_P44_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P45 | `RHF_Command/RHF_P45_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P46 | `RHF_Command/RHF_P46_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P47 | `RHF_Command/RHF_P47_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P48 | `RHF_Command/RHF_P48_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P49 | `RHF_Command/RHF_P49_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P50 | `RHF_Command/RHF_P50_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P51 | `RHF_Command/RHF_P51_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P52 | `RHF_Command/RHF_P52_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P53 | `RHF_Command/RHF_P53_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P54 | `RHF_Command/RHF_P54_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |
| P55 | `RHF_Command/RHF_P55_layer0001.csv` | 25050 | `0` | 2 | RHF_VARIABLE_POWER |

## Pre-outcome design conclusion / outcome 전 설계 결론
**HOLD_F35_COMMAND_INTERVENTION_STRUCTURE** — command structure does not reproduce the preregistered 55-part / 5+50 design. Do not open outcomes.

