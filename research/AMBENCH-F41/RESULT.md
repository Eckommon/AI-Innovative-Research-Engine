---
id: AMBENCH-F41-RESULT
type: nondegenerate-path-order-source-gate-result
created: 2026-08-24
raw_measurement_outcomes_inspected: false
simulator_performance_executed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F41 Result — NIST RHF P01 Source-Native Path/Order Gate
# AMBENCH-F41 결과 — NIST RHF P01 Source-Native Path/Order Gate

## Boundary / 경계
- Only checksum-frozen P01 `X,Y,Power,Trigger` process-input rows are inspected.
- No MPM, encoder outcome, analysis-result, microscopy, or simulator-performance value is used.
- Scan runs are maximal contiguous `Power>0` source runs; no geometry-based split/merge.

## Source integrity / source 무결성
- dataset: `mds2-2507`
- NERDm_version: `1.0.1`
- expected_version_match: `True`
- archive_size_local: `18079576`
- archive_size_match: `True`
- archive_sha256_local: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`
- archive_sha256_match: `True`
- P01_member: `RHF_Command/RHF_P01_layer0001.csv`
- parsed_command_rows: `25051`
- positive_power_rows: `7408`

## Source-native scan runs / source-native scan run
- maximal_positive_run_count_all: `39`
- eligible_run_count_min2rows: `39`
- eligible_run_lengths: `[251, 376, 251, 376, 21, 40, 60, 79, 99, 119, 138, 158, 177, 197, 217, 236, 256, 275, 284, 284, 284, 284, 284, 284, 284, 277, 257, 238, 218, 199, 179, 159, 140, 120, 101, 81, 61, 42, 22]`

## Unchanged RHF run-risk gate / 변경 없는 RHF run-risk gate
- R: `0.29 mm`
- T: `6 ms`
- timing: original command-row index x `10 us`
- positive prior command L_k: `1`
- normalization: `H_N=min(H/(mean(H)+population_SD(H)),1)`
- run_risks: `[0.964399013606817, 0.976234447913061, 0.964399013606817, 0.976234447913061, 0.525857355240114, 0.769589471861311, 0.840068470146306, 0.856387735989238, 0.858879496315618, 0.853939339156543, 0.845100672483816, 0.842638402267424, 0.836854033700968, 0.835670102917281, 0.834972916654933, 0.831085487655538, 0.830740575497594, 0.827731676684206, 0.841311617354158, 0.828798956249636, 0.82928084648798, 0.828753445031162, 0.829300481555412, 0.828730090981891, 0.829326553515201, 0.839302527222874, 0.829647148945383, 0.833088603021482, 0.83366593629808, 0.838191782759587, 0.839423942373706, 0.840938685301042, 0.848196396478048, 0.851849992410463, 0.8638476805678, 0.87273424946079, 0.874198062324499, 0.862098036583657, 0.751036639425473]`
- run_risk_range: `0.450377092672948`
- numerical_tie_guard_64ULP: `7.105427357601e-15`
- stable_risk_order: `[5, 39, 6, 18, 24, 22, 20, 21, 23, 25, 27, 17, 16, 28, 29, 15, 14, 13, 30, 26, 31, 7, 32, 19, 12, 11, 33, 34, 10, 8, 9, 38, 35, 36, 37, 1, 3, 2, 4]`
- nominal_run_order: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]`

## Frozen F41 gate / 고정 F41 판정
**`PASS_F41_NONDEGENERATE_PATH_ORDER_SOURCE_READY`**

P01 contains source-native reorderable runs with materially distinct unchanged-RHF risks and a stable non-nominal risk ordering. A separately preregistered descendant performance design may be considered; this result itself authorizes no performance run.
