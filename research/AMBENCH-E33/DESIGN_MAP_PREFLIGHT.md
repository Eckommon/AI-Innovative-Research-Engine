---
id: AMBENCH-E33-DESIGN-MAP-PREFLIGHT
type: process-input-preflight
created: 2026-08-23
numerical_outcome_values_emitted: false
process_input_values_only: true
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Equivalent Programmed-Length Reverse Map / 동등 programmed-length 역매칭 검증

## Boundary / 경계
- Process-input scan strategy only. `Measurements.xlsx` numerical outcomes were not opened.
- Gate metric and tolerance are frozen in `AMENDMENT-02.md`.

## Source integrity / source 무결성
- dataset: `mds2-3662`
- version: `1.0.1`
- archive_size: `28583`
- sha256_nerdm: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- sha256_local: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- checksum_match: `True`

## Frozen process-input resolution / 고정 공정입력 해상도
- nominal_scan_speed_um_s: `960000.0`
- expected_sampling_interval_s: `1e-05`
- observed_median_dt_s: `1e-05`
- sampling_interval_match: `True`
- frozen_pair_tolerance_um: `10.0`

## Laser-on segmentation / laser-on track 분할
- C_segment_count: `18`
- D_segment_count: `18`

### C segments
- C1: n=126; duration_s=0.00125; programmed_length_um=1200.000000; polyline_um=1200.851306
- C2: n=125; duration_s=0.00124; programmed_length_um=1190.400000; polyline_um=1187.311192
- C3: n=124; duration_s=0.00123; programmed_length_um=1180.800000; polyline_um=1177.300173
- C4: n=124; duration_s=0.00123; programmed_length_um=1180.800000; polyline_um=1181.404702
- C5: n=123; duration_s=0.00122; programmed_length_um=1171.200000; polyline_um=1166.130852
- C6: n=122; duration_s=0.00121; programmed_length_um=1161.600000; polyline_um=1161.856816
- C7: n=121; duration_s=0.0012; programmed_length_um=1152.000000; polyline_um=1152.240633
- C8: n=120; duration_s=0.00119; programmed_length_um=1142.400000; polyline_um=1142.322211
- C9: n=119; duration_s=0.00118; programmed_length_um=1132.800000; polyline_um=1130.676476
- C10: n=118; duration_s=0.00117; programmed_length_um=1123.200000; polyline_um=1123.365588
- C11: n=117; duration_s=0.00116; programmed_length_um=1113.600000; polyline_um=1112.196267
- C12: n=116; duration_s=0.00115; programmed_length_um=1104.000000; polyline_um=1103.415413
- C13: n=115; duration_s=0.00114; programmed_length_um=1094.400000; polyline_um=1091.791766
- C14: n=114; duration_s=0.00113; programmed_length_um=1084.800000; polyline_um=1089.141025
- C15: n=113; duration_s=0.00112; programmed_length_um=1075.200000; polyline_um=1073.234392
- C16: n=112; duration_s=0.00111; programmed_length_um=1065.600000; polyline_um=1063.325016
- C17: n=111; duration_s=0.0011; programmed_length_um=1056.000000; polyline_um=1052.736381
- C18: n=110; duration_s=0.00109; programmed_length_um=1046.400000; polyline_um=1049.371097

### D segments
- D1: n=109; duration_s=0.00108; programmed_length_um=1036.800000; polyline_um=1043.709809
- D2: n=110; duration_s=0.00109; programmed_length_um=1046.400000; polyline_um=1057.520772
- D3: n=111; duration_s=0.0011; programmed_length_um=1056.000000; polyline_um=1057.075093
- D4: n=112; duration_s=0.00111; programmed_length_um=1065.600000; polyline_um=1068.370723
- D5: n=113; duration_s=0.00112; programmed_length_um=1075.200000; polyline_um=1081.490613
- D6: n=114; duration_s=0.00113; programmed_length_um=1084.800000; polyline_um=1092.720828
- D7: n=115; duration_s=0.00114; programmed_length_um=1094.400000; polyline_um=1096.545998
- D8: n=116; duration_s=0.00115; programmed_length_um=1104.000000; polyline_um=1105.534979
- D9: n=117; duration_s=0.00116; programmed_length_um=1113.600000; polyline_um=1123.742422
- D10: n=118; duration_s=0.00117; programmed_length_um=1123.200000; polyline_um=1130.545998
- D11: n=119; duration_s=0.00118; programmed_length_um=1132.800000; polyline_um=1146.453715
- D12: n=120; duration_s=0.00119; programmed_length_um=1142.400000; polyline_um=1145.836118
- D13: n=121; duration_s=0.0012; programmed_length_um=1152.000000; polyline_um=1154.534979
- D14: n=122; duration_s=0.00121; programmed_length_um=1161.600000; polyline_um=1165.720828
- D15: n=123; duration_s=0.00122; programmed_length_um=1171.200000; polyline_um=1178.578562
- D16: n=124; duration_s=0.00123; programmed_length_um=1180.800000; polyline_um=1183.579294
- D17: n=125; duration_s=0.00124; programmed_length_um=1190.400000; polyline_um=1189.776213
- D18: n=126; duration_s=0.00125; programmed_length_um=1200.000000; polyline_um=1202.595873

## Reverse-pair programmed-length equivalence / 역매칭 programmed-length 동등성
- Pair: `C(t) ↔ D(19−t)`; length = laser-on duration × 960,000 µm/s.
- all_18_reverse_pairs_within_10um: `True`
- MAE_reverse_um: `8.000000`
- MAE_same_index_um: `84.800000`
- reverse_globally_better_than_same_index: `True`
- pairs:
  - C1 ↔ D18: C_len_um=1200.000000; D_len_um=1200.000000; abs_diff_um=0.000000
  - C2 ↔ D17: C_len_um=1190.400000; D_len_um=1190.400000; abs_diff_um=0.000000
  - C3 ↔ D16: C_len_um=1180.800000; D_len_um=1180.800000; abs_diff_um=0.000000
  - C4 ↔ D15: C_len_um=1180.800000; D_len_um=1171.200000; abs_diff_um=9.600000
  - C5 ↔ D14: C_len_um=1171.200000; D_len_um=1161.600000; abs_diff_um=9.600000
  - C6 ↔ D13: C_len_um=1161.600000; D_len_um=1152.000000; abs_diff_um=9.600000
  - C7 ↔ D12: C_len_um=1152.000000; D_len_um=1142.400000; abs_diff_um=9.600000
  - C8 ↔ D11: C_len_um=1142.400000; D_len_um=1132.800000; abs_diff_um=9.600000
  - C9 ↔ D10: C_len_um=1132.800000; D_len_um=1123.200000; abs_diff_um=9.600000
  - C10 ↔ D9: C_len_um=1123.200000; D_len_um=1113.600000; abs_diff_um=9.600000
  - C11 ↔ D8: C_len_um=1113.600000; D_len_um=1104.000000; abs_diff_um=9.600000
  - C12 ↔ D7: C_len_um=1104.000000; D_len_um=1094.400000; abs_diff_um=9.600000
  - C13 ↔ D6: C_len_um=1094.400000; D_len_um=1084.800000; abs_diff_um=9.600000
  - C14 ↔ D5: C_len_um=1084.800000; D_len_um=1075.200000; abs_diff_um=9.600000
  - C15 ↔ D4: C_len_um=1075.200000; D_len_um=1065.600000; abs_diff_um=9.600000
  - C16 ↔ D3: C_len_um=1065.600000; D_len_um=1056.000000; abs_diff_um=9.600000
  - C17 ↔ D2: C_len_um=1056.000000; D_len_um=1046.400000; abs_diff_um=9.600000
  - C18 ↔ D1: C_len_um=1046.400000; D_len_um=1036.800000; abs_diff_um=9.600000

## Frozen gate application / 고정 gate 적용
- checksum_identity: `True`
- exact_18x18_laser_on_segments: `True`
- sampling_resolution_match: `True`
- reverse_pair_tolerance: `True`
- reverse_global_superiority: `True`

## Pre-outcome design conclusion / outcome 전 설계 결론
**PASS_E33_EQUIVALENT_LENGTH_REVERSE_MAP** — checksum-frozen process inputs verify `C(t) ↔ D(19−t)` as the deterministic equivalent programmed-length map under opposite scan-history order. It is not a same-XY-location map.
- Per Amendment-01, publication-level outcomes were already exposed after preregistration; raw `Measurements.xlsx` values remain unopened at this gate.

