---
id: MEM-051-AMBENCH-F28
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
research: AMBENCH-F28
---

# MEM-051 — AMBENCH-F28 / F28

## Final / 최종
`PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`

## What was verified / 검증된 내용
- NIST `mds2-4103` current version `1.0.0`.
- T72/T82/T92/T102/T112/T122 each have one unique P1 `*_pixel_points.csv` component.
- All six P1 components locally match NERDm size/SHA-256 and expose the same 7-field pixel-coordinate schema with 45 rows.
- NIST README defines the pixel-point measurement semantics and geometry calculation relationships; cross-sectional TIFFs have physical micrometer-per-pixel scaling.
- `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv` is exact-path unique, size 1653 bytes, SHA-256 `98c898fd78be88c5f0a318575ad6468dc03a3cdeaa31dc19d03605a2df9f7c22`, and locally integrity-matched.
- Surface-reference schema: `Image Name`, `Y reference pixel number`, `Step over direction`.
- Each of the six target plates has exactly one P1 surface-reference row.

## Boundary / 경계
No raw coordinate/reference values were emitted. No geometry endpoint, condition comparison, permutation test, rank statistic, or model was computed.

Permanent inherited disclosure:
`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Next / 다음
Per `DEC-059`, separately preregister `AMBENCH-E29` before numerical inspection. Freeze endpoint, missingness/coverage, plate aggregation, exact 3-vs-3 inference, effect-size/gates, and nested-track dependence limits first.

## Capability / Portfolio
Reusable NERDm/source-integrity/provenance workflow remains `SHARED-INTERNAL-CANDIDATE`; no duplicate Skill/MCP/Plugin. Shared resource availability must not be assumed without canonical ledger evidence.

Incremental monetary cost: `0 USD`.
