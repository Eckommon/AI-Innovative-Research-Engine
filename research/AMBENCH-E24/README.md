---
id: AMBENCH-E24
type: preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-F22
  - AMBENCH-F23
  - DEC-050
---

# AMBENCH-E24 — Registered Melt-Pool ↔ XCT Controlled Experiment
# AMBENCH-E24 — 등록 Melt-Pool ↔ XCT 통제 실험

## Purpose / 목적
**KO:** NIST `mds2-3761`의 checksum-verified, headerless 40-column registered X4 dataset에서 결과 확인 전 고정한 저자유도 설계로 in-situ melt-pool variation과 registered ex-situ XCT voxel variation의 관계를 검증한다. Raw measured-point rows를 독립 replicate로 취급하지 않고 `row ⊂ layer ⊂ part` 계층을 보존한다.

**EN:** Test the relationship between in-situ melt-pool variation and registered ex-situ XCT voxel variation in checksum-verified `mds2-3761` using a low-degree-of-freedom design frozen before association results are inspected. Raw measured-point rows are not treated as independent replicates; hierarchy `row ⊂ layer ⊂ part` is preserved.

## Disclosure / 사전노출 공시
Inherited unchanged from F22/F23:
`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`.
The limited F22 first-row exposure is disclosed. No association, rank, aggregation result, model, or feature-selection result was seen before this E24 design freeze.

## Authoritative variables / 권위 변수
F23 positional contract (NIST AMS 100-69):
- primary predictor: column 16 `melt_pool_area_t100_mm2`;
- sensitivity predictors only: column 13 `melt_pool_area_t80_mm2`, column 19 `melt_pool_area_t120_mm2`;
- primary outcome: column 40 `xct_voxel_mean5` (5×5×5 mean-filtered XCT voxel value).

Rationale frozen prospectively:
- threshold 100 is the central one of NIST's reported 80/100/120 melt-pool thresholds;
- area is used rather than selecting among length/width/area after results;
- the 5×5×5 XCT value is chosen because NIST reports mean-filtered volumes as reducing voxelwise uncertainty relative to raw values.

No LWI features, power/speed features, alternative XCT columns, or learned features are eligible in E24.

## Analysis unit and aggregation / 분석 단위 및 집계
1. Verify each ZIP against the exact F22/F23 NIST SHA-256 before parsing.
2. For each part × layer CSV, retain rows where predictor and outcome are both finite.
3. A part-layer is eligible if paired finite-row count >= 30. No imputation.
4. For each eligible part-layer, compute the median predictor and median outcome. These medians are analysis intermediates; raw row values are never emitted.
5. Partition layers into ten fixed contiguous 25-layer blocks: 1–25, 26–50, ..., 226–250.
6. For each part × block, compute the median of eligible layer medians. A block unit is eligible if >= 20 of 25 layers are eligible.
7. Expected maximum analysis units: 4 parts × 10 blocks = 40. No raw-row or layer-level p-value is permitted.

## Primary estimand / 1차 estimand
Fit a two-way fixed-effect linear model on eligible part×block units:
`XCT_mean5_block ~ melt_pool_area_t100_block + C(part) + C(block)`.

Before fitting, predictor and outcome are standardized globally across eligible part×block units (mean 0, population SD with `ddof=0`). The primary estimand is the standardized coefficient `beta_primary` on melt-pool area. Reference-category choice for the fixed-effect dummies does not alter this predictor slope.

Inference is descriptive/controlled, not causal. Report:
- `beta_primary`;
- ordinary R² of the full fixed-effect model;
- partial R² attributable to the predictor relative to the part+block-only baseline.

No automated variable selection, polynomial term, interaction, nonlinear learner, or hyperparameter search is allowed.

## Block-preserving permutation / block 보존 permutation
Primary null calibration uses a fixed-seed (`20260823`) Monte Carlo permutation with 20,000 draws:
- within each 25-layer block, permute the four part labels of the predictor among eligible parts;
- preserve the outcome, part labels, block labels and marginal predictor distribution;
- refit the identical fixed-effect model;
- two-sided permutation p-value = `(1 + count(|beta_perm| >= |beta_primary|)) / (1 + 20000)`.

If a block has fewer than 3 eligible part units, exclude that block from both observed and permutation analyses and report the exclusion.

## Prespecified sensitivity / 사전고정 sensitivity
Repeat the identical pipeline separately for:
- col 13, `melt_pool_area_t80_mm2`;
- col 19, `melt_pool_area_t120_mm2`.
These are threshold-sensitivity checks only. They cannot replace the primary result.

`material sign disagreement` is frozen before numerical execution as follows: at least one sensitivity beta has the opposite sign to `beta_primary` **and** has `|beta_sensitivity| >= 0.10`, while `|beta_primary| >= 0.10`. Smaller opposite-sign coefficients are recorded but are not treated as material sign disagreement.

## Registration negative control / registration 음성 대조
Construct one frozen misregistration control using the primary predictor and the primary outcome shifted forward by exactly 25 layers (one block) within the same part, dropping the terminal block rather than wrapping.
Apply the same aggregation/fixed-effect model to the resulting aligned block pairs.
Report `beta_shift25` and `partial_R2_shift25`.

Interpret registered locality as more credible only if `|beta_primary| > |beta_shift25|`; failure does not prove no relationship but weakens a local-registration interpretation.

## Robustness / 강건성
Report part-specific simple Spearman rho across the ten block units for the primary predictor/outcome only, with no p-values. These four rhos are consistency diagnostics, not independent confirmatory tests.

## Missingness / 결측
- finite paired rows only;
- no imputation;
- layer eligibility >=30 paired rows;
- block eligibility >=20 eligible layers;
- report counts only before effect estimates.
If fewer than 24 total part×block units or fewer than 6 blocks remain, final gate must be `HOLD_E24_INSUFFICIENT_AGGREGATED_COVERAGE` and no effect interpretation is permitted.

## Uncertainty / 불확실성
Carry NIST AMS 100-69 uncertainty into interpretation:
- melt-pool dimensions depend on camera pixelation, digitization/noise and threshold choice; t80/t100/t120 sensitivity is therefore prespecified;
- XCT is downscaled/registered, with positional uncertainty on the order documented by NIST; 5×5×5 mean-filtered values are used to reduce voxelwise uncertainty, not eliminate it;
- no causal claim is authorized.

## Frozen gates / 고정 판정
- `PASS_E24_CONTROLLED_ASSOCIATION_COMPLETED`
- `MIXED_E24_REGISTERED_ASSOCIATION`
- `NO_MATERIAL_E24_ASSOCIATION`
- `HOLD_E24_INSUFFICIENT_AGGREGATED_COVERAGE`
- `HOLD_E24_SOURCE_OR_SCHEMA_INTEGRITY`

Gate semantics:
- PASS: primary association is nontrivial (`partial_R2 >= 0.05`), permutation p <= 0.05, locality criterion `|beta_primary| > |beta_shift25|` holds, and there is no material threshold-sensitivity sign disagreement;
- MIXED: some but not all PASS criteria hold, or material threshold-sensitivity sign disagreement occurs;
- NO_MATERIAL: `partial_R2 < 0.05` and no other integrity HOLD applies;
- HOLD gates supersede effect gates when triggered.

## Output boundary / 출력 경계
Allowed durable outputs:
- source hashes and structural/coverage counts;
- part×block aggregate counts, but not a table of the 40 numeric units;
- model coefficients, R²/partial R², permutation p-value;
- threshold-sensitivity coefficients;
- negative-control coefficient/R²;
- four part-specific Spearman diagnostics.

Prohibited:
- raw row values;
- row-level predictions/residuals;
- layer-level value tables;
- feature fishing or post-hoc endpoint switching;
- raw ZIP/CSV artifacts/cache/commits.

## Cost / 비용
Zero-incremental-cost official NIST routes and standard public GitHub-hosted runners only. Any potentially billable route requires explicit prior user approval.