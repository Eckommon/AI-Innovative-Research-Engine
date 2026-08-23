---
id: AMBENCH-F42-RESULT
type: source-grounded-path-order-transfer-feasibility-result
created: 2026-08-24
custom_simulator_performance_executed: false
physical_outcome_values_inspected: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F42 Result — P01 Source-Grounded Path-Order Transfer Feasibility
# AMBENCH-F42 결과 — P01 Source-Grounded Path-Order Transfer 타당성

## Boundary / 경계
- Only checksum-frozen P01 process-input commands and pinned 3DThesis input syntax are used.
- No custom 3DThesis performance simulation is executed.
- No MPM/encoder/analysis/microscopy outcome value is used.

## Source integrity / source 무결성
- NERDm_version: `1.0.1`
- archive_size_match: `True`
- archive_sha256_local: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`
- archive_sha256_match: `True`
- P01_member: `RHF_Command/RHF_P01_layer0001.csv`
- parsed_rows: `25051`
- positive_rows: `7408`
- source_native_runs: `39`

## Source timing partition / source timing 분할
- leading_off_rows: `200`
- inter_run_gap_count: `38`
- inter_run_gap_rows: `[614, 614, 614, 1067, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 397, 423, 423, 423, 423, 423, 423, 402, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423, 423]`
- trailing_off_rows: `199`
- laser_on_time_s: `0.07408`
- laser_off_time_s: `0.17643`
- total_modeled_time_s: `0.25051`
- benchmark_energy_proxy_J_at_600W: `44.448`

## Geometry/domain transfer / geometry-domain transfer
- source_positive_bbox_x_mm: `[-26.5, -23.5]`
- source_positive_bbox_y_mm: `[7, 9]`
- translated_width_mm: `3`
- translated_height_mm: `2`
- frozen_xy_buffer_mm: `1.0`
- grid_shape_xyz: `[101, 81, 41]`
- derived_grid_points: `335421`
- grid_cap: `1000000`

## Matched generated inputs / 동일 생성 입력
- nominal_order: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]`
- risk_order: `[5, 39, 6, 18, 24, 22, 20, 21, 23, 25, 27, 17, 16, 28, 29, 15, 14, 13, 30, 26, 31, 7, 32, 19, 12, 11, 33, 34, 10, 8, 9, 38, 35, 36, 37, 1, 3, 2, 4]`
- nominal_path_sha256: `7b2860908b2c96b167e1f383af5fa150b92184ad433e1ca9b3320dba68eeb475`
- risk_order_path_sha256: `778adef0041061f2413b35539798c3c5836b3290c1054e4c71b39f5dc689cd9b`
- path_hashes_distinct: `True`
- per_run_geometry_preserved: `True`
- positive_count_and_total_time_invariants: `True`

## Frozen F42 gate / 고정 F42 판정
**`PASS_F42_SOURCE_GROUNDED_PATH_TRANSFER_READY`**

Nominal and F41 risk-order P01 transfers are distinct while preserving exact source-native positive-run geometry, positive command count, source-derived timing budget, common benchmark energy proxy and one deterministic bounded domain. A separately preregistered path-order-only performance experiment may now be designed; F42 itself authorizes no performance result.
