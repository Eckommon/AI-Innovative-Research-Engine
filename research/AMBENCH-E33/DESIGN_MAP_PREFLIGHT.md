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
- parsed_rows: `2980`
- skipped_rows: `0`
- header: `['x (�m)', 'y (�m)', 'laser power (W)', 'time (seconds)']`
- laser_power_values: `[0.0, 285.0]`
- positive_dt_median_s: `9.999999999999593e-06`
- nonpositive_dt_count: `0`
- dt_gt_50us_count: `0`

## `Scan Strategy Data/scanStrategyDiverging.csv`
- parsed_rows: `2965`
- skipped_rows: `0`
- header: `['x (�m)', 'y (�m)', 'laser power (W)', 'time (seconds)']`
- laser_power_values: `[0.0, 285.0]`
- positive_dt_median_s: `9.999999999999593e-06`
- nonpositive_dt_count: `0`
- dt_gt_50us_count: `0`

## Segmentation / track 분할
- C_segment_count: `1`
- D_segment_count: `1`
- C_base_dt: `9.999999999999593e-06`
- D_base_dt: `9.999999999999593e-06`
- threshold_s: `5e-05`

### C process-input segments
- C1: n=2980; start=(2435.0, 675.0); end=(570.0, 734.0); segment_time_s=0.02979

### D process-input segments
- D1: n=2965; start=(2432.0, 738.0); end=(568.0, 649.0); segment_time_s=0.02964

## Geometry-location matching / geometry 위치 매칭
- one_to_one_18x18: `False`
- exact_Ct_to_D19minusT: `False`
- matches:
  - C1 -> D1: endpoint_error_sum_um=148.095; next_best_error_sum_um=NA

## Pre-outcome design conclusion / outcome 전 설계 결론
**HOLD_GEOMETRY_REVERSE_MAPPING_NOT_VERIFIED** — do not open measurement outcomes.

