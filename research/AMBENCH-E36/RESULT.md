---
id: AMBENCH-E36-RESULT
type: confirmatory-reproduction-result
state: COMPLETED_NUMERICAL_EXECUTION
created: 2026-08-23
source_of_truth: github-actions
publication_level_outcomes_preexposed: true
raw_analysis_rows_committed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E36 Result — RHF External Part-Level Variability Reproduction
# AMBENCH-E36 결과 — RHF 외부 Part-Level 변동성 재현

## Execution integrity / 실행 무결성
- dataset: `mds2-2507`
- NERDm version: `1.0.1`
- archive_size: `1637430`
- SHA-256 expected/NERDm/local: `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`
- checksum_match: `True`
- physical_parts: `55`
- rows_per_part: `1498`
- baseline_parts: `[1, 12, 23, 34, 45]`
- RHF_parts: `50`
- No raw analysis rows are committed; only preregistered physical-part aggregates/statistics are persisted.

## Frozen primary — melt-pool-area variability / 고정 1차 — melt-pool area 변동성
- baseline_part_sd_median_px: `0.00502139929961`
- RHF_part_sd_median_px: `0.00436718302021`
- Delta_med_baseline_minus_RHF_px: `0.000654216279402`
- permutation_n: `100000`
- permutation_seed: `20260823`
- extreme_count: `1247`
- add_one_one_sided_p: `0.0124798752012`
- block_sign_counts: `positive=5; negative=0; zero=0`
- **primary_gate: `PASS_E36_EXTERNAL_RHF_VARIABILITY_REDUCTION`**

### Physical-part area SD aggregates / Physical-part area SD 집계
| Part | Group | SD area (px) | Rows |
|---:|---|---:|---:|
| P01 | BASELINE_CONSTANT_POWER | 0.00441478319906 | 1498 |
| P02 | RHF_VARIABLE_POWER | 0.00379813934204 | 1498 |
| P03 | RHF_VARIABLE_POWER | 0.00381218590275 | 1498 |
| P04 | RHF_VARIABLE_POWER | 0.00410304511276 | 1498 |
| P05 | RHF_VARIABLE_POWER | 0.00424417986138 | 1498 |
| P06 | RHF_VARIABLE_POWER | 0.00431135243536 | 1498 |
| P07 | RHF_VARIABLE_POWER | 0.0043138015808 | 1498 |
| P08 | RHF_VARIABLE_POWER | 0.00450069941734 | 1498 |
| P09 | RHF_VARIABLE_POWER | 0.00467736358537 | 1498 |
| P10 | RHF_VARIABLE_POWER | 0.00497519315786 | 1498 |
| P11 | RHF_VARIABLE_POWER | 0.00503151773468 | 1498 |
| P12 | BASELINE_CONSTANT_POWER | 0.00505577490106 | 1498 |
| P13 | RHF_VARIABLE_POWER | 0.0043825293186 | 1498 |
| P14 | RHF_VARIABLE_POWER | 0.00416694274472 | 1498 |
| P15 | RHF_VARIABLE_POWER | 0.00430922188112 | 1498 |
| P16 | RHF_VARIABLE_POWER | 0.00428386445681 | 1498 |
| P17 | RHF_VARIABLE_POWER | 0.00448350339329 | 1498 |
| P18 | RHF_VARIABLE_POWER | 0.00457771809674 | 1498 |
| P19 | RHF_VARIABLE_POWER | 0.00470995853883 | 1498 |
| P20 | RHF_VARIABLE_POWER | 0.00496419170168 | 1498 |
| P21 | RHF_VARIABLE_POWER | 0.0050552336092 | 1498 |
| P22 | RHF_VARIABLE_POWER | 0.00532207572366 | 1498 |
| P23 | BASELINE_CONSTANT_POWER | 0.00502139929961 | 1498 |
| P24 | RHF_VARIABLE_POWER | 0.00435183672183 | 1498 |
| P25 | RHF_VARIABLE_POWER | 0.00421604962938 | 1498 |
| P26 | RHF_VARIABLE_POWER | 0.0041929969909 | 1498 |
| P27 | RHF_VARIABLE_POWER | 0.00447816450091 | 1498 |
| P28 | RHF_VARIABLE_POWER | 0.00439687062324 | 1498 |
| P29 | RHF_VARIABLE_POWER | 0.00452111842618 | 1498 |
| P30 | RHF_VARIABLE_POWER | 0.00468151404854 | 1498 |
| P31 | RHF_VARIABLE_POWER | 0.00488192862997 | 1498 |
| P32 | RHF_VARIABLE_POWER | 0.00524691872603 | 1498 |
| P33 | RHF_VARIABLE_POWER | 0.00530941029039 | 1498 |
| P34 | BASELINE_CONSTANT_POWER | 0.00508529858414 | 1498 |
| P35 | RHF_VARIABLE_POWER | 0.00426235545557 | 1498 |
| P36 | RHF_VARIABLE_POWER | 0.00393137455199 | 1498 |
| P37 | RHF_VARIABLE_POWER | 0.00387303242206 | 1498 |
| P38 | RHF_VARIABLE_POWER | 0.00407618990817 | 1498 |
| P39 | RHF_VARIABLE_POWER | 0.00411244614177 | 1498 |
| P40 | RHF_VARIABLE_POWER | 0.00406073264472 | 1498 |
| P41 | RHF_VARIABLE_POWER | 0.00424358714861 | 1498 |
| P42 | RHF_VARIABLE_POWER | 0.00452343296056 | 1498 |
| P43 | RHF_VARIABLE_POWER | 0.00485396319946 | 1498 |
| P44 | RHF_VARIABLE_POWER | 0.00506481608015 | 1498 |
| P45 | BASELINE_CONSTANT_POWER | 0.0049840116285 | 1498 |
| P46 | RHF_VARIABLE_POWER | 0.00427804509675 | 1498 |
| P47 | RHF_VARIABLE_POWER | 0.00407601787029 | 1498 |
| P48 | RHF_VARIABLE_POWER | 0.00428946696711 | 1498 |
| P49 | RHF_VARIABLE_POWER | 0.00418142785414 | 1498 |
| P50 | RHF_VARIABLE_POWER | 0.00423708970102 | 1498 |
| P51 | RHF_VARIABLE_POWER | 0.00429216486151 | 1498 |
| P52 | RHF_VARIABLE_POWER | 0.00444688975835 | 1498 |
| P53 | RHF_VARIABLE_POWER | 0.00459090833746 | 1498 |
| P54 | RHF_VARIABLE_POWER | 0.00483999745694 | 1498 |
| P55 | RHF_VARIABLE_POWER | 0.00484345923632 | 1498 |

### Frozen block stability / 고정 block 안정성
| Block | Baseline | RHF parts | Baseline SD - RHF median SD (px) | Sign |
|---:|---:|---|---:|---|
| B1 | P01 | P02–P11 | 0.00010220619098 | positive |
| B2 | P12 | P13–P22 | 0.000525164156049 | positive |
| B3 | P23 | P24–P33 | 0.000521757836068 | positive |
| B4 | P34 | P35–P44 | 0.000907281938951 | positive |
| B5 | P45 | P46–P55 | 0.00069319571419 | positive |

## Publication-form descriptive reproduction / 논문형 기술 재현
- mean_baseline_part_area_SD_px: `0.00491225352247`
- median_baseline_part_area_SD_px: `0.00502139929961`
- minimum_RHF_part: `P02`
- minimum_RHF_part_area_SD_px: `0.00379813934204`
- descriptive_reduction_vs_mean_baseline_pct: `22.6803070187`
- This optimum/minimum section is descriptive only and has no independent PASS authority because the candidate optimum is selected across 50 RHF conditions and publication-level optimum information was already known.

## Secondary sensitivity / 2차 sensitivity
Length and width use the same part-level sample-SD construction but cannot rescue the primary area gate.
- length: baseline_median_SD=`0.0630170384771`; RHF_median_SD=`0.0564441052286`; Delta=`0.00657293324849`; block_signs=`[1, 1, 1, 1, 1]`
- width: baseline_median_SD=`0.0205792836338`; RHF_median_SD=`0.0192732628143`; Delta=`0.00130602081953`; block_signs=`[-1, 1, 1, 1, 1]`

## Final / 최종
- **`PASS_E36_EXTERNAL_RHF_VARIABILITY_REDUCTION`**
- Claim scope: independent NIST IN625 bare-plate RHF parameter-sweep experiment; physical-part-level non-selective association between RHF variable-power conditions and melt-pool-area variability.
- Not randomized causal proof, not universal superiority of every RHF setting, not same-construct replication of E33, and not pristine outcome-blind discovery.
- No post-hoc filtering, row/frame pseudo-replication, parameter-subset search, endpoint switch, model escalation, or paid computation was used.

