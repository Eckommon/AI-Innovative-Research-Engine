---
id: AMBENCH-D25
type: preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-E24
  - DEC-051
---

# AMBENCH-D25 — Registered X4 Fixed-Effect Dominance / Variance-Structure Diagnostic
# AMBENCH-D25 — Registered X4 고정효과 지배 / 분산구조 진단

## Purpose / 목적

**KO:** E24의 `NO_MATERIAL_E24_ASSOCIATION`을 feature 추가나 model-capacity 증가로 구제하지 않는다. E24와 정확히 동일한 predictor/outcome/aggregation만 재현하여 XCT와 melt-pool aggregate variation이 `part`, `25-layer block`, 잔차 중 어디에 주로 위치하는지 분해하고, part별 음의 관계와 part+block-adjusted 약한 양의 slope가 공존한 구조적 이유를 진단한다.

**EN:** Do not rescue E24's `NO_MATERIAL_E24_ASSOCIATION` by adding features or model capacity. Reproduce exactly the same E24 predictor, outcome and aggregation, decompose variation across `part`, fixed 25-layer `block`, and residual structure, and diagnose why negative part-wise relationships coexist with the weak positive part+block-adjusted slope.

## Frozen data contract / 고정 데이터 contract
- dataset: NIST `mds2-3761` registered X4;
- predictor only: F23 col16 `melt_pool_area_t100_mm2`;
- outcome only: F23 col40 `xct_voxel_mean5`;
- exact F22/F23 SHA-256 identities must pass before parsing;
- no t80/t120, LWI, power/speed, alternative XCT field, learned feature or new endpoint is allowed;
- inherited exposure disclosure: `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`.

## Frozen aggregation / 고정 집계
Reproduce E24 exactly:
1. finite paired t100-area/XCT-mean5 rows only;
2. part-layer eligible at >=30 paired rows;
3. part-layer median predictor and median outcome;
4. fixed blocks 1–25, 26–50, ..., 226–250;
5. part-block median across eligible layer medians;
6. part-block eligible at >=20 eligible layers;
7. blocks with <3 eligible parts excluded;
8. no raw-row/layer value table may be persisted.

### Reproduction integrity check / 재현 무결성 확인
Before D25 interpretation, recomputation must reproduce E24 to rounding tolerance:
- eligible primary units = `36`;
- included blocks = `9`;
- excluded block set = `[1]`;
- `beta_part_block_adjusted` must equal E24 `0.015305` within absolute tolerance `5e-7` when rounded from the same standardized ddof=0 procedure;
- E24 primary partial R² must reproduce `0.019321` within absolute tolerance `5e-7`.
Failure => `HOLD_D25_REPRODUCTION_INTEGRITY`.

## Frozen variance decomposition / 고정 분산 분해
All analyses use the reproduced eligible part-block units. Predictor and outcome are globally standardized with population SD (`ddof=0`) for slope comparisons.

### Outcome models / Outcome model
Fit ordinary least squares:
- `Y0`: `y ~ 1`;
- `YP`: `y ~ C(part)`;
- `YB`: `y ~ C(block)`;
- `YPB`: `y ~ C(part) + C(block)`;
- `YPBX`: `y ~ x + C(part) + C(block)`.

Report:
- `R2_y_part_only`;
- `R2_y_block_only`;
- `R2_y_part_block`;
- `partial_R2_y_block_given_part = (SSE_YP - SSE_YPB) / SSE_YP`;
- `partial_R2_y_part_given_block = (SSE_YB - SSE_YPB) / SSE_YB`;
- `residual_fraction_y_after_part_block = SSE_YPB / SST_Y`;
- reproduce E24 predictor partial R² from `YPB -> YPBX`.

These partial R² values are not added together; the design is unbalanced after frozen eligibility filtering.

### Predictor structure / Predictor 구조
Treat x as the diagnostic response and fit:
- `XP`: `x ~ C(part)`;
- `XB`: `x ~ C(block)`;
- `XPB`: `x ~ C(part) + C(block)`.

Report:
- `R2_x_part_only`;
- `R2_x_block_only`;
- `R2_x_part_block`;
- `partial_R2_x_block_given_part`;
- `partial_R2_x_part_given_block`;
- `residual_fraction_x_after_part_block`.

## Frozen sign-decomposition / 고정 부호 분해
Using the same standardized eligible units, report predictor slope from:
1. `beta_pooled`: `y ~ x`;
2. `beta_part_adjusted`: `y ~ x + C(part)`;
3. `beta_block_adjusted`: `y ~ x + C(block)`;
4. `beta_part_block_adjusted`: `y ~ x + C(part) + C(block)` (must reproduce E24).

Also report, without p-values:
- the four E24-equivalent part-specific Spearman `rho(x,y)` values;
- for each part, Spearman `rho(block_index,x)` and `rho(block_index,y)` over eligible blocks.

`STRUCTURAL_SIGN_REVERSAL = YES` is frozen as:
- `beta_part_adjusted` and `beta_part_block_adjusted` have opposite signs;
- both absolute coefficients are >= `0.01`;
- at least 3 of 4 part-specific `rho(x,y)` values have the same sign as `beta_part_adjusted`.
Otherwise `NO`.

`BLOCK_REMOVAL_EXPLAINS_REVERSAL = YES` requires `STRUCTURAL_SIGN_REVERSAL = YES` and the sign of `beta_block_adjusted` equals the sign of `beta_part_block_adjusted`. This is descriptive, not causal.

## Frozen dominance gates / 고정 지배 판정
Outcome structure determines the primary diagnostic gate:

### `D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`
Requires all:
- `R2_y_part_block >= 0.90`;
- `partial_R2_y_block_given_part >= 0.80`;
- `partial_R2_y_block_given_part - partial_R2_y_part_given_block >= 0.10`.

### `D25_PART_DOMINANT_HIERARCHICAL_STRUCTURE`
Requires all:
- `R2_y_part_block >= 0.90`;
- `partial_R2_y_part_given_block >= 0.80`;
- `partial_R2_y_part_given_block - partial_R2_y_block_given_part >= 0.10`.

### `D25_MIXED_FIXED_EFFECT_STRUCTURE`
Use when `R2_y_part_block >= 0.90` but neither dominance gate passes.

### `D25_RESIDUAL_DOMINANT_STRUCTURE`
Use when `R2_y_part_block < 0.90` and no integrity HOLD applies.

### Holds
- `HOLD_D25_REPRODUCTION_INTEGRITY`;
- `HOLD_D25_SOURCE_OR_SCHEMA_INTEGRITY`.
HOLD supersedes diagnostic gates.

## Decision rule after D25 / D25 이후 의사결정
Do **not** start another same-dataset feature search merely because a fixed-effect component is strong.

If D25 shows block- or part-dominant structure and E24's predictor partial R² remains <0.05, the default next decision is to stop escalating the same registered-X4 representation and seek an **independent-condition or independently varied dataset/experiment** before testing a new mechanistic hypothesis.

Only if D25 shows substantial residual structure not explained by part/block may a separately preregistered diagnostic justify further same-dataset work. No automatic high-capacity ML is authorized.

## Output boundary / 출력 경계
Allowed durable outputs:
- source-integrity and coverage counts;
- R² / partial R² / residual fractions above;
- four specified slopes;
- prespecified Spearman diagnostics;
- frozen diagnostic gate.

Prohibited:
- raw row values;
- layer-level or 36-unit numeric tables;
- new feature rankings;
- endpoint switching;
- post-hoc threshold changes;
- raw ZIP/CSV commit, artifact or cache.

## Cost / 비용
Only zero-incremental-cost official NIST routes and standard public GitHub-hosted runners are authorized. Any potentially billable action requires explicit prior user approval.