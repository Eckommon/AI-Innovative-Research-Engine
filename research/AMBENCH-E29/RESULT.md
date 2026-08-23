---
id: AMBENCH-E29-RESULT
type: controlled-experiment-result
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
inherited_exposure: NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION
---

# AMBENCH-E29 Result / E29 결과

- incremental monetary cost: 0 USD
- raw P1 coordinate rows committed/emitted: NO
- raw surface-reference rows committed/emitted: NO
- amendments: AMENDMENT-01 symbolic hold diagnostics; AMENDMENT-02 exact root README selector

## Source identity / source identity
- NERDm_version: 1.0.0
- component_count: 552

- README_exact_root_path: `4103_ReadMe.txt`
- README_integrity_pass: YES
- authoritative_pixel_scale_parse: PASS
- pixel_scale_um_per_px: 0.174

- surface_reference_integrity_pass: YES
- exactly_one_P1_surface_reference_per_plate: YES

## Plate reconstruction / plate 재구성
- six_P1_component_integrity_pass: YES
- valid_track_counts: {'T72': 44, 'T82': 44, 'T92': 44, 'T102': 44, 'T112': 44, 'T122': 44}
- all_plates_valid_track_count_gte_41: YES
- T72_plate_mean_overlap_depth_um: 112.674229909
- T82_plate_mean_overlap_depth_um: 115.201840909
- T92_plate_mean_overlap_depth_um: 114.859120227
- T102_plate_mean_overlap_depth_um: 87.679513500
- T112_plate_mean_overlap_depth_um: 84.165251318
- T122_plate_mean_overlap_depth_um: 83.641278000

## Frozen statistical result / 고정 통계 결과
- Delta_primary_um: 29.083049409
- exact_one_sided_permutation_p: 0.050000000
- plate_rank_biserial: 1.000000000
- rank_pair_wins_losses_ties: 9/0/0
- common_valid_track_count: 44
- Delta_common_um: 29.083049409

## Frozen E29 gate / 고정 E29 판정
**PASS_E29_STRONG_DIRECTIONAL_EFFECT**

## Interpretation boundary / 해석 경계
- independent replicate: physical plate (n=3 vs n=3)
- 45 tracks are nested within-plate measurements, not independent replicates
- no P2/P3 rescue, imputation, sign flip, endpoint switch, feature search, or model escalation performed
- inherited exposure disclosure remains active
