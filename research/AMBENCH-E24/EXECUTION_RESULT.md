---
id: AMBENCH-E24-EXECUTION-RESULT
type: controlled-experiment-result
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
---

# AMBENCH-E24 Execution Result / E24 실행 결과

- route: public standard GitHub-hosted ubuntu-latest
- incremental monetary cost: 0 USD
- raw ZIP/CSV artifacts/cache: NONE
- inherited exposure state: NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED

## Source integrity / source 무결성
- part1.zip: PASS; size=87041995; SHA256=0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3
- part02.zip: PASS; size=85261726; SHA256=bf72d9e160d94094f9268fcf3f76a532c8a29fb64aff1afbec20256acaee178e
- part03.zip: PASS; size=83521608; SHA256=89e9e1afadca22b9c34177d82972272a4e73789b19388f0c83d62a9ebd53d878
- part04.zip: PASS; size=81225258; SHA256=6c3f655a1482001119c54d1f1e404a34eb401f386fffc06147628b36c7c8d7c5
- all_source_integrity_pass: YES

## Frozen coverage / 고정 coverage
- part1_eligible_t100_layers: 232 / 250
- part2_eligible_t100_layers: 231 / 250
- part3_eligible_t100_layers: 230 / 250
- part4_eligible_t100_layers: 230 / 250
- primary_eligible_part_block_units_after_block_filter: 36 / 40
- primary_included_blocks: 9 / 10
- excluded_blocks_lt3_parts: [1]

## Primary preregistered result / 1차 사전등록 결과
- beta_primary_standardized: 0.015305
- full_model_R2: 0.999432
- partial_R2_predictor: 0.019321
- block_preserving_permutation_draws: 20000
- permutation_p_two_sided: 0.007900

## Threshold sensitivity / threshold 민감도
- beta_t80: 0.016772
- partial_R2_t80: 0.025308
- eligible_units_t80: 36
- beta_t120: 0.017831
- partial_R2_t120: 0.021048
- eligible_units_t120: 36
- material_sign_disagreement: NO

## +25-layer registration negative control / +25-layer registration 음성대조
- shift_control_units: 32
- beta_shift25: 0.011634
- partial_R2_shift25: 0.009379
- locality_criterion_abs_primary_gt_abs_shift25: YES

## Part-specific Spearman diagnostics / part별 Spearman 진단
- part1_rho: -0.460255
- part2_rho: -0.268917
- part3_rho: -0.483333
- part4_rho: -0.694567

## Frozen gate application / 고정 판정 적용
- partial_R2_ge_0_05: NO
- permutation_p_le_0_05: YES
- locality_criterion: YES
- no_material_sign_disagreement: YES

## Final gate / 최종 판정
**NO_MATERIAL_E24_ASSOCIATION**

- causal claim authorized: NO
- raw numerical row/layer table persisted: NO
- feature selection or endpoint switching performed: NO
- raw transient teardown: SUCCESS
