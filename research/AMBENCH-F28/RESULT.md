---
id: AMBENCH-F28-RESULT
type: research-result
state: COMPLETED
created: 2026-08-23
source_of_truth: github
final_gate: PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY
incremental_monetary_cost_usd: 0
---

# AMBENCH-F28 Result / F28 결과

## Final gate / 최종 판정

**`PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`**

**KO:** NIST `mds2-4103`의 여섯 plate-specific P1 `*_pixel_points.csv`와 권위 있는 README reconstruction semantics, 그리고 `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`를 결합하면 T72/T82/T92/T102/T112/T122 각각에 대해 P1 cross-section의 geometry를 결정론적으로 재구성할 수 있는 source/provenance contract가 성립한다.

**EN:** The six plate-specific P1 `*_pixel_points.csv` components in NIST `mds2-4103`, together with the authoritative README reconstruction semantics and `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`, establish a deterministic source/provenance contract for reconstructing P1 cross-section geometry for T72/T82/T92/T102/T112/T122.

## Evidence / 근거

### 1. Six immutable plate-specific P1 components / 여섯 immutable plate-specific P1 component

All six P1 files were uniquely bound by filepath to one physical plate, downloaded transiently, and locally matched to current NIST NERDm size and SHA-256. Their common bounded schema is:

- `Row`
- `depth_x (px)`
- `depth_y (px)`
- `width_x (px)`
- `bead_height_y (px)`
- `overlap_depth_x (px)`
- `overlap_depth_y (px)`

Each inspected component exposes 45 data rows. No coordinate values were emitted by F28.

### 2. Authoritative reconstruction semantics / 권위 reconstruction semantics

The current NIST README was immutable-source verified and states that the `*_pixel_points.csv` files contain pixel locations used for measurements/calculations. It defines the coordinate meanings and formulas for width, bead height, and overlap depth. It also states that cross-sectional TIFF micrographs have a physical micrometer-per-pixel scale.

For overlap depth, the documented semantic contract is the difference between the overlap-depth Y coordinate and the substrate-surface Y coordinate, followed by the documented image pixel scaling when physical units are required.

### 3. Deterministic surface-reference binding / 결정론적 surface-reference binding

Current NERDm exposes exactly one component at:

`Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`

Verified immutable identity:
- size: `1653` bytes
- SHA-256: `98c898fd78be88c5f0a318575ad6468dc03a3cdeaa31dc19d03605a2df9f7c22`
- local size match: YES
- local SHA-256 match: YES

Bounded schema:
- `Image Name`
- `Y reference pixel number`
- `Step over direction`

All six target plates are present, all six have a P1 reference, and there is exactly one P1 reference row for each target plate.

## What PASS means / PASS의 의미

**KO:** F28 PASS는 source/schema/provenance 수준에서 plate-specific physical-geometry reconstruction route가 검증되었다는 뜻이다. 이는 turnaround-time 효과가 존재한다거나 어떤 condition이 우월하다는 numerical result가 아니다.

**EN:** F28 PASS means the plate-specific physical-geometry reconstruction route is verified at the source/schema/provenance level. It is not a numerical finding that turnaround time has an effect or that one condition is superior.

## Boundaries / 경계

F28 did **not**:
- emit raw pixel-coordinate or surface-reference values;
- compute any plate geometry endpoint;
- compare 0.75 ms vs 5.0 ms conditions;
- run a permutation test, rank statistic, model, or feature selection;
- reinterpret the E27 malformed schema-preflight emission as valid evidence.

Permanent inherited disclosure remains:
`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Capability delta / Capability 변화

The repeated NERDm immutable-component + bounded-schema + provenance verification pattern remains **`SHARED-INTERNAL-CANDIDATE`**. F28 does not justify extraction into a new Skill/MCP/Plugin yet; central capability overlap remains nonblocking and must be reconciled before any extraction.

## Next eligible mission work / 다음 가능한 mission work

A separate preregistered numerical experiment may now use the verified plate-specific reconstruction contract. The preferred next step is **AMBENCH-E29 — six-plate P1 reconstructed overlap-depth turnaround-time controlled experiment**, with the endpoint, missingness rule, plate aggregation, directional hypothesis, exact permutation statistic, and gates frozen before any coordinate/reference values are inspected numerically.

Incremental monetary cost: **0 USD**.
