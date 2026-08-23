---
id: AMBENCH-E30
stage: EXPERIMENT
status: PREREGISTERED
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-E30 — Six-Plate P2/P3 Spatial Robustness Falsification / 6-plate P2/P3 공간 강건성 반증

## Purpose / 목적

**KO:** E29의 P1 strong directional signal이 동일한 여섯 physical plates의 아직 E29에서 사용하지 않은 P2/P3 공간 단면에서도 같은 방향으로 유지되는지 반증 중심으로 검정한다. P2/P3는 추가 독립표본이 아니라 plate 내부의 nested spatial repeated measurements이다.

**EN:** Test, with a falsification-first design, whether the E29 P1 strong directional signal persists at the previously unused P2/P3 spatial cross-sections of the same six physical plates. P2/P3 are nested spatial repeated measurements within plates, not additional independent samples.

## Preregistration timing / 사전등록 시점

This document is committed before any E30 plate-specific P2/P3 coordinate, surface-reference, reconstructed geometry, plate-position endpoint, combined endpoint, group effect, permutation statistic, or robustness result is numerically inspected or computed.

Permanent exposure disclosure:
`NEW_E30_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

E30 does not claim fresh outcome blindness. It is a separately preregistered robustness/falsification cycle after E29.

## Experimental units / 실험 단위

Independent replicate = **physical plate**.

Groups remain fixed:
- 0.75 ms: T72, T82, T92
- 5.0 ms: T102, T112, T122

Spatial positions = **P2 and P3 only**.

P2/P3 are nested within the same physical plate. Track rows are further nested within each plate-position. Neither cross-section positions nor tracks may be counted as independent replicates.

## Frozen source/reconstruction contract / 고정 source·재구성 contract

Authority = current NIST `mds2-4103`, using the same F28/E29 authoritative contract:
- exact root `4103_ReadMe.txt`;
- `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`;
- exact plate-specific `*_P2s_pixel_points.csv` and `*_P3s_pixel_points.csv` components.

Every component must locally match current NERDm size/SHA-256 before numerical use. Raw authoritative bytes remain transient.

For plate `i`, position `k∈{P2,P3}`, track `j`:

`overlap_depth_px[i,k,j] = overlap_depth_y[i,k,j] - surface_y_reference[i,k]`

`overlap_depth_um[i,k,j] = overlap_depth_px[i,k,j] * pixel_scale_um_per_px`

The physical scale must be uniquely parsed from the exact root README. No alternate scale, sign flip, offset correction, or source substitution is allowed.

Any finite reconstructed overlap depth `<0` => `HOLD_E30_INTEGRITY_OR_COVERAGE`.

## Missingness and coverage / 결측·coverage

README-defined unavailable values such as `#N/A` are missing and are never imputed.

Each plate-position is expected to contain 45 track rows. A plate-position is valid only if at least **41/45 (>=90%)** reconstructed overlap-depth tracks are finite and valid.

If any of the 12 plate-position cells fails the >=41/45 rule, E30 => `HOLD_E30_INTEGRITY_OR_COVERAGE`.

## Frozen position endpoints / 고정 위치 endpoint

For each plate and each position:

`position_mean[i,k] = arithmetic mean of all valid reconstructed overlap depths at that plate-position`

Define position-level group contrasts:

`Delta_P2 = mean(P2 means of 0.75 ms plates) - mean(P2 means of 5.0 ms plates)`

`Delta_P3 = mean(P3 means of 0.75 ms plates) - mean(P3 means of 5.0 ms plates)`

These are spatial-consistency diagnostics, not separate primary hypothesis tests.

## Primary robustness endpoint / 1차 강건성 endpoint

For each physical plate, equal-weight the two spatial positions:

`plate_robustness_mean[i] = (position_mean[i,P2] + position_mean[i,P3]) / 2`

This equal weighting is frozen to prevent differential valid-track counts from implicitly weighting one spatial position more heavily.

Primary combined group effect:

`Delta_combined = mean(plate_robustness_mean for 0.75 ms) - mean(plate_robustness_mean for 5.0 ms)`

Frozen direction remains:
`0.75 ms > 5.0 ms`.

## Exact primary inference / 정확 1차 검정

Use a **one-sided exact label permutation** over all `C(6,3)=20` allocations of the six physical-plate robustness endpoints into groups of three.

Statistic = combined group mean difference.

`p_exact_combined = count(permuted Delta >= observed Delta_combined) / 20`

Ties use `>=`; minimum attainable p-value = 0.05.

Primary plate-level rank-biserial effect uses the 3x3 cross-group comparisons of the six combined plate endpoints:

`r_rb_combined = (wins_0.75 - losses_0.75) / 9`

Strong threshold remains `>=7/9`.

## Common-track spatial sensitivity / 공통 track 공간 sensitivity

Define a single **global common-valid track set** as track IDs valid across all 12 plate-position cells (six plates × P2/P3).

If global common-valid count >= **36/45 (80%)**:
- recompute each P2 and P3 position mean using only that identical common track set;
- equal-weight P2/P3 into one sensitivity endpoint per plate;
- compute `Delta_common_combined`.

If common-valid count <36, record `NOT_COMPUTED_LOW_COMMON_COVERAGE`; strong robustness PASS is not allowed.

## Frozen gates / 고정 gate

### `PASS_E30_SPATIALLY_ROBUST_DIRECTIONAL_EFFECT`
All must hold:
1. all source/hash/binding/reconstruction/coverage gates pass;
2. `Delta_P2 > 0`;
3. `Delta_P3 > 0`;
4. `Delta_combined > 0`;
5. `p_exact_combined <= 0.05`;
6. `r_rb_combined >= 7/9`;
7. global common-valid count >=36 and `Delta_common_combined > 0`.

### `MIXED_E30_SPATIAL_ROBUSTNESS`
Integrity/coverage pass and `Delta_combined > 0`, but one or more strong-robustness requirements fail, including a nonpositive P2 or P3 position contrast, p/rank threshold failure, or unavailable/nonpositive common-track sensitivity.

This means the E29 direction retains some combined support but is not uniformly spatially robust.

### `FALSIFIED_E30_SPATIAL_GENERALITY`
Integrity/coverage pass and `Delta_combined <= 0`.

This directly falsifies extension of the E29 P1 direction to the predeclared equal-weight P2/P3 robustness endpoint. A reverse effect may be described but not converted into a new post-hoc hypothesis inside E30.

### `HOLD_E30_INTEGRITY_OR_COVERAGE`
Any required immutable source identity, unique P2/P3 surface-reference binding, unique scale, 45-row schema, nonnegative reconstruction, or >=41/45 plate-position coverage requirement fails.

## Forbidden adaptations / 금지

E30 must not:
- treat P2/P3 as additional independent plates;
- pool all track rows across plates for inferential n;
- use P1 to rescue P2/P3 robustness;
- drop either P2 or P3 after seeing results;
- change equal weighting after seeing valid counts or effects;
- impute unavailable tracks;
- switch sign/scale/source;
- search alternative geometry endpoints;
- perform high-capacity modeling or feature selection;
- reinterpret a MIXED/FALSIFIED result as PASS.

## Reporting / 보고

Durable sanitized output may include source-integrity status, physical scale, valid-track counts for 12 plate-position cells, 12 position means, six equal-weight plate robustness means, `Delta_P2`, `Delta_P3`, `Delta_combined`, exact combined p-value, combined rank-biserial, global common-track count, `Delta_common_combined`, and frozen final gate.

Raw coordinate/reference rows remain transient and are not committed.

## Capability / Portfolio / 비용

The execution pattern remains `SHARED-INTERNAL-CANDIDATE`; no Skill/MCP/Plugin promotion is justified by E30 alone. Shared paid resource availability is never assumed without canonical ledger evidence.

Execution is authorized only at `0 USD` incremental monetary cost. Potentially billable work => `HOLD_COST_APPROVAL` pending explicit user approval.
