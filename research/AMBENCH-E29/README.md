---
id: AMBENCH-E29
stage: EXPERIMENT
status: PREREGISTERED
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-E29 — Six-Plate P1 Reconstructed Overlap-Depth Turnaround-Time Controlled Experiment / 6-plate P1 재구성 overlap-depth turnaround-time 통제 실험

## Purpose / 목적

**KO:** F28에서 검증된 plate-specific P1 pixel annotation + surface-reference + physical-scale contract를 사용하여, 0.75 ms turnaround와 5.0 ms turnaround 사이의 P1 overlap depth 차이를 physical plate를 독립 반복단위로 하여 검정한다.

**EN:** Use the plate-specific P1 pixel-annotation + surface-reference + physical-scale contract verified in F28 to test the P1 overlap-depth difference between 0.75 ms and 5.0 ms turnaround conditions, treating the physical plate as the independent replicate.

## Preregistration timing / 사전등록 시점

This document is committed **before any E29 numerical pixel-coordinate, surface-reference, reconstructed-geometry, plate-endpoint, group-effect, permutation, or model result is inspected or computed**.

Permanent inherited disclosure:

`NEW_E29_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`

E27 temporarily exposed malformed pseudo-header content containing numerical cells. The current experiment therefore does **not** claim fresh outcome blindness. However, the endpoint, P1 location, six-plate grouping, direction `0.75 ms > 5.0 ms`, exact 3-vs-3 permutation framework, and strong-effect rank criterion were frozen in E27 **before** that incident. E29 inherits them and does not re-select them.

## Frozen experimental units / 고정 실험 단위

Independent replicate = **physical plate**, not track.

### 0.75 ms group
- T72
- T82
- T92

### 5.0 ms group
- T102
- T112
- T122

Cross-section = **P1 only**.

The 45 track rows within one P1 file are nested repeated measurements used only to construct one plate endpoint. They are never treated as 45 independent replicates.

## Frozen source contract / 고정 source contract

Authority: current NIST `mds2-4103` source identities qualified by F28.

Required components:
1. six exact P1 `*_pixel_points.csv` components bound to the six physical plates (`CLM-095`);
2. authoritative NIST README reconstruction semantics and physical micrometer-per-pixel scale (`CLM-096`);
3. exact `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv` surface-reference component (`CLM-097`).

Every downloaded component must locally match current NERDm size/SHA-256 before numerical use. Any identity/hash mismatch => `HOLD_E29_INTEGRITY_OR_COVERAGE`; do not substitute a different source.

Raw authoritative external bytes are transient only and must not be committed or uploaded as Actions artifacts/cache.

## Frozen reconstruction / 고정 재구성

For plate `i` and track `j`:

`overlap_depth_px[i,j] = overlap_depth_y[i,j] - surface_y_reference[i]`

`overlap_depth_um[i,j] = overlap_depth_px[i,j] * pixel_scale_um_per_px`

where:
- `overlap_depth_y` comes from that plate's P1 `*_pixel_points.csv`;
- `surface_y_reference` comes from the unique P1 row for the same plate in `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`;
- `pixel_scale_um_per_px` is parsed from the authoritative NIST README statement defining cross-sectional TIFF pixel scaling.

No sign flip, offset tuning, alternative scale, source substitution, P2/P3 substitution, or outcome-informed reconstruction adjustment is allowed.

If the documented formula yields any finite reconstructed overlap depth `< 0`, treat this as a semantic/integrity failure and HOLD rather than changing the sign convention.

## Missingness and coverage / 결측 및 coverage

README-defined unavailable entries such as `#N/A` are treated as missing, never imputed.

A track is valid for the primary endpoint only when its `overlap_depth_y`, the plate's unique surface reference, and the authoritative pixel scale are all finite and usable.

Frozen plate coverage requirement:
- total expected track rows = 45;
- each plate must have **at least 41 valid overlap-depth tracks (>=90%)**;
- if any plate has <41 valid tracks => `HOLD_E29_INTEGRITY_OR_COVERAGE`.

Rationale: allow at most four unavailable track measurements explicitly permitted by the source documentation while preventing a plate endpoint from being dominated by differential missingness.

No missing coordinate is imputed or replaced by a condition average.

## Primary plate endpoint / 1차 plate endpoint

For each plate:

`plate_mean_overlap_depth_um = arithmetic mean of all valid reconstructed P1 track overlap depths for that plate`

Primary group effect:

`Delta_primary = mean(three 0.75 ms plate endpoints) - mean(three 5.0 ms plate endpoints)`

Frozen direction:

`H1: Delta_primary > 0`

This direction is inherited from the E27 preregistration and is not re-selected in E29.

## Exact inference / 정확 검정

Primary test = **one-sided exact label permutation** over all `C(6,3)=20` allocations of six plate endpoints into groups of three.

Statistic = group mean difference in the frozen direction.

`p_exact = count(permuted Delta >= observed Delta) / 20`

Ties are included with `>=`. Because the complete permutation space contains only 20 allocations, the minimum attainable one-sided p-value is 0.05.

No asymptotic t-test or pseudo-replicated track-level p-value is primary.

## Effect size / 효과크기

Primary nonparametric effect size = plate-level rank-biserial effect from all 3x3 cross-group plate comparisons:

`r_rb = (wins_0.75ms - losses_0.75ms) / 9`

Ties contribute zero to wins/losses.

Frozen strong-effect threshold:

`r_rb >= 7/9 = 0.777777...`

This threshold is inherited from E27 and is not outcome-selected in E29.

## Missingness sensitivity / 결측 sensitivity

Define the **common-valid track set** as track indices valid in all six plates.

If the common-valid set contains at least **36 of 45 tracks (>=80%)**, compute one sensitivity endpoint per plate as the arithmetic mean over that identical common-valid track set and report:

`Delta_common = mean(0.75 ms common-track plate endpoints) - mean(5.0 ms common-track plate endpoints)`

No additional p-value is required for this sensitivity.

If common-valid coverage is <36, sensitivity is `NOT_COMPUTED_LOW_COMMON_COVERAGE`; the primary may still be evaluable if every plate satisfies the >=41/45 primary coverage rule, but a strong PASS is not allowed without an available positive-direction common-track sensitivity.

## Frozen gates / 고정 gate

### `PASS_E29_STRONG_DIRECTIONAL_EFFECT`
All must hold:
1. all source/hash/reconstruction/coverage gates pass;
2. `Delta_primary > 0`;
3. `p_exact <= 0.05`;
4. `r_rb >= 7/9`;
5. common-valid sensitivity is available and `Delta_common > 0`.

### `MIXED_E29_DIRECTIONAL_SIGNAL`
Source/integrity/primary coverage pass and `Delta_primary > 0`, but one or more strong-PASS criteria fail, including exact p-value, rank criterion, or sensitivity support.

### `NO_MATERIAL_GAIN_E29`
Source/integrity/primary coverage pass and `Delta_primary <= 0` under the frozen direction. A reverse-direction observation may be reported descriptively but must not be reframed as a post-hoc new hypothesis inside E29.

### `HOLD_E29_INTEGRITY_OR_COVERAGE`
Any required source/hash identity, unique plate/reference binding, scale parse, documented reconstruction contract, nonnegative reconstruction, or >=41/45 per-plate coverage requirement fails.

## Forbidden adaptations / 금지된 적응

E29 must not:
- switch primary endpoint after reading results;
- use P2/P3 to rescue a failed P1 result;
- use summary tables as a substitute for plate-specific reconstruction;
- impute missing track coordinates;
- change the sign convention or scale after seeing outcomes;
- treat 45 tracks as independent samples;
- fit high-capacity ML or search multiple feature/endpoint variants;
- select a two-sided/one-sided test after observing the effect;
- erase or minimize the inherited E27 exposure disclosure.

## Reporting / 보고

Sanitized durable output may include:
- source-integrity status;
- parsed physical pixel scale;
- valid-track counts per plate;
- six aggregated plate endpoints in µm;
- `Delta_primary`;
- exact one-sided p-value;
- plate-level `r_rb`;
- common-valid track count and `Delta_common` if available;
- frozen final gate.

Raw P1 coordinate rows and raw surface-reference rows remain transient and are not committed.

## Capability / Portfolio / 비용

The execution pattern remains `SHARED-INTERNAL-CANDIDATE`; no new Skill/MCP/Plugin is created for E29. Existing Central Capability Repository overlap remains nonblocking. Shared paid quota/budget is not assumed.

Execution is authorized only at **0 USD incremental monetary cost**. Any potentially billable action => `HOLD_COST_APPROVAL` pending explicit user approval.
