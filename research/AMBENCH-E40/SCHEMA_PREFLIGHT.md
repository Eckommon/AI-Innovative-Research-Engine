---
id: AMBENCH-E40-SCHEMA-PREFLIGHT
type: pinned-mpstats-output-schema-preflight
created: 2026-08-24
bundled_numerical_values_persisted: false
bundled_numerical_statistics_computed: false
custom_controller_performance_executed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E40 MP_Stats Schema Preflight / MP_Stats Schema 사전점검

## Boundary / 경계
- Exact pinned upstream build + bundled `solidification_mpstats` execution only.
- Only output filename, header/schema and row count are persisted.
- No bundled numerical data cell, numerical statistic, ranking or C0–C4 custom-controller performance is persisted or computed.

## Runtime identity / 실행환경 identity
- repository: `ORNL-MDF/3DThesis`
- pinned_commit: `2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`
- runner: standard GitHub-hosted Ubuntu
- cmake_configure/build/install: `PASS`
- bundled_example_execution: `PASS`
- generated_csv_name: `solidification_mpstats.Solidification.Final.csv`

## Output schema / 출력 schema
- header_column_count: `6`
- header: `['x', 'y', 'z', 'MP_width', 'MP_length', 'MP_depth']`
- data_row_count: `12453`
- MP_width_hits_1based: `[4]`
- MP_length_hits_1based: `[5]`
- MP_depth_hits_1based: `[6]`
- deterministic_MP_width_field: `True`

## Frozen Stage A gate / 고정 Stage A 판정
**PASS_E40_MPSTATS_SCHEMA_READY**
- The frozen primary endpoint maps deterministically to the exact `MP_width` output field.
- Stage B C0–C4 performance execution is now authorized under the unchanged F39 design contract.
