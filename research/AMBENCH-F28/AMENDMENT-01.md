# AMBENCH-F28 Amendment 01 — Coordinate fields are not direct physical metrics / Coordinate field는 direct physical metric이 아님

## Trigger / 발생
The automated source/schema workflow marked `direct_geometry_metric_field_present=YES` because the P1 headers contain strings such as `depth` and `overlap_depth`.

## Scientific correction / 과학적 보정
The actual bounded headers explicitly carry units `(px)` and are coordinate/annotation fields:
- `depth_x (px)` / `depth_y (px)`;
- `width_x (px)`;
- `bead_height_y (px)`;
- `overlap_depth_x (px)` / `overlap_depth_y (px)`.

Therefore the automated `PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY` is **provisional and not accepted as the scientific final gate**. Presence of metric names inside pixel-coordinate labels does not itself establish an analysis-ready physical geometry measurand.

## Required final verification / 최종 검증 필요
Before final F28 classification, verify from the authoritative NIST README/documentation whether a deterministic reconstruction contract is specified for converting the plate-specific pixel annotations into physical depth/overlap-depth geometry without outcome-driven tuning.

If such a contract is not explicitly verified, final F28 must be:
`PARTIAL_F28_PLATE_SPECIFIC_ANNOTATION_READY`.

No coordinate values, geometry outcomes, condition comparisons, or endpoint selection may be performed during this documentation check.

## Invariants / 불변사항
- six component identity/hash findings remain valid;
- plate/P1 bindings remain valid;
- no source or endpoint switch;
- inherited exposure state remains `NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`;
- cost remains 0 USD.