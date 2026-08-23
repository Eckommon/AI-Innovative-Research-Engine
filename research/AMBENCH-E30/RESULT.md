---
id: AMBENCH-E30-RESULT
type: spatial-robustness-result
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
inherited_exposure: NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION
---

# AMBENCH-E30 Result / E30 결과

- incremental monetary cost: 0 USD
- raw P2/P3 coordinate rows committed/emitted: NO
- raw surface-reference rows committed/emitted: NO

## Source identity / source identity
- NERDm_version: 1.0.0
- component_count: 552

- README_filepath: `4103_ReadMe.txt`
- README_size: 23849
- README_SHA256: 857ed848396ebce7e88ccfe95c1b6ac9dd75ba8337fd570e78a797bad5a45d94
- README_local_integrity_match: YES
- pixel_scale_um_per_px: 0.174

- surface_filepath: `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`
- surface_size: 1653
- surface_SHA256: 98c898fd78be88c5f0a318575ad6468dc03a3cdeaa31dc19d03605a2df9f7c22
- surface_local_integrity_match: YES
- exactly_one_P2_P3_surface_reference_per_plate_position: YES

## Immutable P2/P3 components / immutable P2/P3 component
- T72_P2: `Cross_Sections/Tracks_Results/20241010_AMB_T72_P2s_pixel_points.csv` | size=2046 | SHA256=ee138b31f952908d881afae45d943a1ea849fb3ca19a780c11e4f0c886054832 | local_match=YES
- T72_P3: `Cross_Sections/Tracks_Results/20241010_AMB_T72_P3s_pixel_points.csv` | size=2031 | SHA256=ae3e0ebd3fa5e10eeadc77e2634caf4c4b750fda5ec945ab2a57836635426b57 | local_match=YES
- T82_P2: `Cross_Sections/Tracks_Results/20241015_AMB_T82_P2s_pixel_points.csv` | size=2064 | SHA256=a0f44a9fd922f0c7d554c8efebff04d93f4c3f96f7b1043398d80656defc69b4 | local_match=YES
- T82_P3: `Cross_Sections/Tracks_Results/20241015_AMB_T82_P3s_pixel_points.csv` | size=1976 | SHA256=19dbfea207911a04a070a08cf4ee6567576a3143d1484fcd844b0e283275b946 | local_match=YES
- T92_P2: `Cross_Sections/Tracks_Results/20241015_AMB_T92_P2s_pixel_points.csv` | size=2076 | SHA256=bfd4122cdca96691b11df91946f792b221ebc5457f8781986b0b410567cf8849 | local_match=YES
- T92_P3: `Cross_Sections/Tracks_Results/20241015_AMB_T92_P3s_pixel_points.csv` | size=2040 | SHA256=3ad9df3268df8e5a32fdc88da25d12170afe49b51b1308f349bb45d0d5cc3f3f | local_match=YES
- T102_P2: `Cross_Sections/Tracks_Results/20241010_AMB_T102_P2s_pixel_points.csv` | size=2067 | SHA256=ca88f56c90441d92669b25403f458711d5ec4408cdbf558279bdfd3a1f776a1e | local_match=YES
- T102_P3: `Cross_Sections/Tracks_Results/20241010_AMB_T102_P3s_pixel_points.csv` | size=2046 | SHA256=0f7368c61a4f63de255d94aa77bfae4ac07f16729ccc2792e681951a788549f2 | local_match=YES
- T112_P2: `Cross_Sections/Tracks_Results/20241015_AMB_T112_P2s_pixel_points.csv` | size=2025 | SHA256=edc85602aa595af6947e3a839adc2a22f5f026160478b6fd0cbf7b04dbd4844d | local_match=YES
- T112_P3: `Cross_Sections/Tracks_Results/20241015_AMB_T112_P3s_pixel_points.csv` | size=2033 | SHA256=a4a3bea42a22aeee163115eb562ce95d14e95e126351e8489f47456977d5b3dc | local_match=YES
- T122_P2: `Cross_Sections/Tracks_Results/20241015_AMB_T122_P2s_pixel_points.csv` | size=2002 | SHA256=d8c514f0deb255a54bfb2c8d8f2d4e192b9713c415854ec1a508651c7d13902b | local_match=YES
- T122_P3: `Cross_Sections/Tracks_Results/20241015_AMB_T122_P3s_pixel_points.csv` | size=2047 | SHA256=08a95f03484ffe0b88e0facbb4b9e1a1e11f95bff8b209b1756d61e7f4b5446c | local_match=YES

## Position reconstruction / 위치 재구성
- all_12_component_integrity_pass: YES
- valid_track_counts: {'T72_P2': 44, 'T72_P3': 44, 'T82_P2': 44, 'T82_P3': 44, 'T92_P2': 44, 'T92_P3': 44, 'T102_P2': 44, 'T102_P3': 44, 'T112_P2': 44, 'T112_P3': 44, 'T122_P2': 44, 'T122_P3': 44}
- all_12_plate_position_coverage_gte_41: YES
- T72_P2_mean_overlap_depth_um: 119.014018773
- T72_P3_mean_overlap_depth_um: 133.372320818
- T82_P2_mean_overlap_depth_um: 121.352475955
- T82_P3_mean_overlap_depth_um: 132.278892955
- T92_P2_mean_overlap_depth_um: 122.505894273
- T92_P3_mean_overlap_depth_um: 135.392437091
- T102_P2_mean_overlap_depth_um: 95.800180500
- T102_P3_mean_overlap_depth_um: 98.630962773
- T112_P2_mean_overlap_depth_um: 97.151974636
- T112_P3_mean_overlap_depth_um: 97.034663045
- T122_P2_mean_overlap_depth_um: 97.057065545
- T122_P3_mean_overlap_depth_um: 97.655514818

## Combined plate robustness endpoints / 결합 plate 강건성 endpoint
- T72_P2P3_equal_weight_mean_um: 126.193169795
- T82_P2P3_equal_weight_mean_um: 126.815684455
- T92_P2P3_equal_weight_mean_um: 128.949165682
- T102_P2P3_equal_weight_mean_um: 97.215571636
- T112_P2P3_equal_weight_mean_um: 97.093318841
- T122_P2P3_equal_weight_mean_um: 97.356290182

## Frozen robustness statistics / 고정 강건성 통계
- Delta_P2_um: 24.287722773
- Delta_P3_um: 35.907503409
- Delta_combined_um: 30.097613091
- exact_one_sided_combined_permutation_p: 0.050000000
- combined_plate_rank_biserial: 1.000000000
- combined_rank_wins_losses_ties: 9/0/0
- global_common_valid_track_count: 44
- Delta_common_combined_um: 30.097613091

## Frozen E30 gate / 고정 E30 판정
**PASS_E30_SPATIALLY_ROBUST_DIRECTIONAL_EFFECT**

## Interpretation boundary / 해석 경계
- independent replicate remains physical plate (n=3 vs n=3)
- P2/P3 are nested spatial repeats; tracks are nested within plate-position
- P1 was not used to rescue or weight E30
- no position dropping, imputation, endpoint search, sign/scale/source adaptation, or model escalation
- inherited exposure disclosure remains active
