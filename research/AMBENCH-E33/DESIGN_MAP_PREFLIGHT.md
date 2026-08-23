---
id: AMBENCH-E33-DESIGN-MAP-PREFLIGHT
type: process-input-preflight
created: 2026-08-23
numerical_outcome_values_emitted: false
process_input_values_only: true
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Scan-Strategy Design Map Preflight / Scan-Strategy 설계 map 사전점검

## Boundary / 경계
- Process-input scan strategy only. `Measurements.xlsx` numerical outcomes were not opened.

## Source integrity / source 무결성
- dataset: `mds2-3662`
- version: `1.0.1`
- archive_size: `28583`
- sha256_nerdm: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- sha256_local: `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`
- checksum_match: `True`

## `Scan Strategy Data/scanStrategyConverging.csv`
- header: `['x (�m)', 'y (�m)', 'laser power (W)', 'time (seconds)']`
- rows: `2980`
- laser_on_rows: `2130`
- laser_off_rows: `850`

## `Scan Strategy Data/scanStrategyDiverging.csv`
- header: `['x (�m)', 'y (�m)', 'laser power (W)', 'time (seconds)']`
- rows: `2965`
- laser_on_rows: `2115`
- laser_off_rows: `850`

## Laser-on segmentation / laser-on track 분할
- C_segment_count: `18`
- D_segment_count: `18`

### C track segments
- C1: n=126; start=(2435.0, 675.0); end=(2435.0, 1872.0); duration_s=0.00125; chord_um=1197
- C2: n=125; start=(2326.0, 1841.0); end=(2326.0, 658.0); duration_s=0.00124; chord_um=1183
- C3: n=124; start=(2216.0, 690.0); end=(2216.0, 1863.0); duration_s=0.00123; chord_um=1173
- C4: n=124; start=(2106.0, 1836.0); end=(2107.0, 659.0); duration_s=0.00123; chord_um=1177
- C5: n=123; start=(1996.0, 695.0); end=(1991.0, 1858.0); duration_s=0.00122; chord_um=1163.01
- C6: n=122; start=(1887.0, 1827.0); end=(1887.0, 669.0); duration_s=0.00121; chord_um=1158
- C7: n=121; start=(1777.0, 700.0); end=(1772.0, 1849.0); duration_s=0.0012; chord_um=1149.01
- C8: n=120; start=(1668.0, 1817.0); end=(1668.0, 679.0); duration_s=0.00119; chord_um=1138
- C9: n=119; start=(1563.0, 711.0); end=(1558.0, 1839.0); duration_s=0.00118; chord_um=1128.01
- C10: n=118; start=(1454.0, 1808.0); end=(1453.0, 689.0); duration_s=0.00117; chord_um=1119
- C11: n=117; start=(1343.0, 721.0); end=(1339.0, 1830.0); duration_s=0.00116; chord_um=1109.01
- C12: n=116; start=(1234.0, 1798.0); end=(1234.0, 699.0); duration_s=0.00115; chord_um=1099
- C13: n=115; start=(1124.0, 736.0); end=(1119.0, 1825.0); duration_s=0.00114; chord_um=1089.01
- C14: n=114; start=(1010.0, 1798.0); end=(1009.0, 714.0); duration_s=0.00113; chord_um=1084
- C15: n=113; start=(904.0, 746.0); end=(900.0, 1816.0); duration_s=0.00112; chord_um=1070.01
- C16: n=112; start=(791.0, 1789.0); end=(790.0, 729.0); duration_s=0.00111; chord_um=1060
- C17: n=111; start=(685.0, 756.0); end=(681.0, 1806.0); duration_s=0.0011; chord_um=1050.01
- C18: n=110; start=(571.0, 1779.0); end=(570.0, 734.0); duration_s=0.00109; chord_um=1045

### D track segments
- D1: n=109; start=(2432.0, 738.0); end=(2435.0, 1779.0); duration_s=0.00108; chord_um=1041
- D2: n=110; start=(2326.0, 1778.0); end=(2328.0, 722.0); duration_s=0.00109; chord_um=1056
- D3: n=111; start=(2214.0, 730.0); end=(2212.0, 1786.0); duration_s=0.0011; chord_um=1056
- D4: n=112; start=(2103.0, 1780.0); end=(2100.0, 714.0); duration_s=0.00111; chord_um=1066
- D5: n=113; start=(1995.0, 718.0); end=(1994.0, 1798.0); duration_s=0.00112; chord_um=1080
- D6: n=114; start=(1885.0, 1792.0); end=(1882.0, 702.0); duration_s=0.00113; chord_um=1090
- D7: n=115; start=(1777.0, 711.0); end=(1775.0, 1806.0); duration_s=0.00114; chord_um=1095
- D8: n=116; start=(1661.0, 1799.0); end=(1663.0, 695.0); duration_s=0.00115; chord_um=1104
- D9: n=117; start=(1554.0, 699.0); end=(1557.0, 1818.0); duration_s=0.00116; chord_um=1119
- D10: n=118; start=(1443.0, 1812.0); end=(1445.0, 683.0); duration_s=0.00117; chord_um=1129
- D11: n=119; start=(1336.0, 687.0); end=(1339.0, 1825.0); duration_s=0.00118; chord_um=1138
- D12: n=120; start=(1225.0, 1819.0); end=(1222.0, 676.0); duration_s=0.00119; chord_um=1143
- D13: n=121; start=(1118.0, 679.0); end=(1116.0, 1832.0); duration_s=0.0012; chord_um=1153
- D14: n=122; start=(1007.0, 1831.0); end=(1004.0, 668.0); duration_s=0.00121; chord_um=1163
- D15: n=123; start=(900.0, 667.0); end=(898.0, 1844.0); duration_s=0.00122; chord_um=1177
- D16: n=124; start=(783.0, 1838.0); end=(786.0, 656.0); duration_s=0.00123; chord_um=1182
- D17: n=125; start=(677.0, 660.0); end=(679.0, 1847.0); duration_s=0.00124; chord_um=1187
- D18: n=126; start=(565.0, 1850.0); end=(568.0, 649.0); duration_s=0.00125; chord_um=1201

## Geometry-location matching / geometry 위치 매칭
- Method: minimum unordered start/end endpoint distance from process-input coordinates.
- one_to_one_18x18: `True`
- exact_Ct_to_D19minusT: `False`
- max_best_endpoint_error_sum_um: `156.277`
- min_next_best_margin_um: `101.444`
- predeclared_recording_tolerance_ok: `False`
- matches:
  - C1 -> D1: best_error_sum_um=156.071; next_best_margin_um=104.73007081365597
  - C2 -> D2: best_error_sum_um=127.031; next_best_margin_um=131.16872207378827
  - C3 -> D3: best_error_sum_um=117.154; next_best_margin_um=138.34235107926023
  - C4 -> D4: best_error_sum_um=111.524; next_best_margin_um=133.33679987374552
  - C5 -> D5: best_error_sum_um=83.0967; next_best_margin_um=155.98595826623162
  - C6 -> D6: best_error_sum_um=68.4337; next_best_margin_um=161.0224903062554
  - C7 -> D7: best_error_sum_um=54.1045; next_best_margin_um=177.4767594212302
  - C8 -> D8: best_error_sum_um=36.0763; next_best_margin_um=185.0878480023323
  - C9 -> D9: best_error_sum_um=36.0238; next_best_margin_um=175.74245891438574
  - C10 -> D10: best_error_sum_um=21.7047; next_best_margin_um=183.2734405929017
  - C11 -> D11: best_error_sum_um=39.7131; next_best_margin_um=174.68160709375275
  - C12 -> D12: best_error_sum_um=48.7896; next_best_margin_um=162.32975974956065
  - C13 -> D13: best_error_sum_um=64.9307; next_best_margin_um=156.14764226818946
  - C14 -> D14: best_error_sum_um=79.407; next_best_margin_um=146.39377568771656
  - C15 -> D15: best_error_sum_um=107.173; next_best_margin_um=127.69645858004937
  - C16 -> D16: best_error_sum_um=122.758; next_best_margin_um=123.81921791156026
  - C17 -> D17: best_error_sum_um=137.382; next_best_margin_um=111.65053796496042
  - C18 -> D18: best_error_sum_um=156.277; next_best_margin_um=101.44397111563325

## Pre-outcome design conclusion / outcome 전 설계 결론
**HOLD_GEOMETRY_REVERSE_MAPPING_NOT_VERIFIED** — no measurement outcome access authorized.

