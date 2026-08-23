---
id: AMBENCH-D25-EXECUTION-RESULT
type: diagnostic-result
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
---

# AMBENCH-D25 Execution Result / D25 실행 결과

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

## Frozen coverage reproduction / 고정 coverage 재현
- part1_eligible_t100_layers: 232 / 250
- part2_eligible_t100_layers: 231 / 250
- part3_eligible_t100_layers: 230 / 250
- part4_eligible_t100_layers: 230 / 250
- eligible_part_block_units: 36 / 40
- included_blocks: 9 / 10
- excluded_blocks_lt3_parts: [1]
- reproduced_beta_part_block_adjusted: 0.015305236
- reproduced_partial_R2_predictor: 0.019321313
- E24_reproduction_integrity: PASS

## Outcome variance structure / Outcome 분산구조
- R2_y_part_only: 0.000602
- R2_y_block_only: 0.998820
- R2_y_part_block: 0.999421
- partial_R2_y_block_given_part: 0.999421
- partial_R2_y_part_given_block: 0.509735
- residual_fraction_y_after_part_block: 0.000579
- E24_partial_R2_x_given_part_block: 0.019321

## Predictor variance structure / Predictor 분산구조
- R2_x_part_only: 0.747172
- R2_x_block_only: 0.205094
- R2_x_part_block: 0.952265
- partial_R2_x_block_given_part: 0.811197
- partial_R2_x_part_given_block: 0.939949
- residual_fraction_x_after_part_block: 0.047735

## Frozen sign decomposition / 고정 부호 분해
- beta_pooled: -0.278047
- beta_part_adjusted: -1.026589
- beta_block_adjusted: -0.022349
- beta_part_block_adjusted: 0.015305
- STRUCTURAL_SIGN_REVERSAL: YES
- BLOCK_REMOVAL_EXPLAINS_REVERSAL: NO

## Prespecified Spearman diagnostics / 사전고정 Spearman 진단
- part1: rho_x_y=-0.460255; rho_block_x=-0.686198; rho_block_y=0.166667
- part2: rho_x_y=-0.268917; rho_block_x=-0.840366; rho_block_y=0.166667
- part3: rho_x_y=-0.483333; rho_block_x=-0.800000; rho_block_y=0.166667
- part4: rho_x_y=-0.694567; rho_block_x=-0.644357; rho_block_y=0.166667

## Final gate / 최종 판정
**D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE**

- causal claim authorized: NO
- new feature/endpoint selection performed: NO
- raw numerical row/layer/unit table persisted: NO
- raw transient teardown: SUCCESS
