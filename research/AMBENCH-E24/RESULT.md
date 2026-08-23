---
id: AMBENCH-E24-RESULT
type: experiment-result
state: COMPLETED_NO_MATERIAL_E24_ASSOCIATION
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-E24/README.md
  - research/AMBENCH-E24/EXECUTION_RESULT.md
  - Issue #42
---

# AMBENCH-E24 Result — Registered Melt-Pool ↔ XCT Controlled Experiment
# AMBENCH-E24 결과 — 등록 Melt-Pool ↔ XCT 통제 실험

**Frozen final gate / 고정 최종 판정:** **`NO_MATERIAL_E24_ASSOCIATION`**

## 1. Executive result / 핵심 결과

**KO:** F23 이후 처음으로 `mds2-3761` checksum-verified registered X4 dataset에서 사전등록된 numerical process↔XCT 실험을 실행했다. Primary predictor는 col 16 `melt_pool_area_t100_mm2`, outcome은 col 40 `xct_voxel_mean5`였고, raw rows를 독립 표본으로 사용하지 않고 part×layer median → 25-layer part×block median으로 집계한 뒤 part/block fixed effects를 통제했다. Primary standardized beta는 `0.015305`, full-model R²는 `0.999432`, predictor partial R²는 `0.019321`, block-preserving permutation p는 `0.007900`이었다. 사전등록 materiality 기준 `partial_R2 >= 0.05`를 충족하지 못했으므로 최종 gate는 `NO_MATERIAL_E24_ASSOCIATION`이다.

**EN:** E24 is the first preregistered numerical process↔XCT experiment on the checksum-verified `mds2-3761` registered X4 dataset after F23. The primary predictor was col 16 `melt_pool_area_t100_mm2` and the outcome was col 40 `xct_voxel_mean5`. Raw rows were not treated as independent observations; data were aggregated from part×layer medians to fixed 25-layer part×block medians and analyzed with part/block fixed effects. The primary standardized beta was `0.015305`, full-model R² `0.999432`, predictor partial R² `0.019321`, and block-preserving permutation p `0.007900`. Because the preregistered materiality threshold `partial_R2 >= 0.05` was not met, the frozen final gate is `NO_MATERIAL_E24_ASSOCIATION`.

## 2. Source integrity and coverage / source 무결성 및 coverage
All four registered archives exactly matched their F22/F23 NIST NERDm SHA-256 and expected sizes before parsing.

Primary t100 coverage:
- Part 1: 232 / 250 eligible layers;
- Part 2: 231 / 250;
- Part 3: 230 / 250;
- Part 4: 230 / 250;
- eligible part×block units after frozen block filtering: 36 / 40;
- included 25-layer blocks: 9 / 10;
- Block 1 was excluded under the preregistered `<3 eligible parts` rule.

Coverage therefore passed the frozen HOLD threshold.

## 3. Primary controlled association / 1차 통제 연관
Frozen model:
`standardized XCT_mean5_block ~ standardized melt_pool_area_t100_block + C(part) + C(block)`.

Observed:
- `beta_primary = 0.015305`;
- `full_model_R2 = 0.999432`;
- `partial_R2_predictor = 0.019321`;
- `permutation_p = 0.007900` from 20,000 fixed-seed block-preserving permutations.

Interpretation:
- the association is statistically detectable under the frozen permutation scheme;
- its additional explanatory contribution after part/block effects is small by the prospectively fixed materiality criterion;
- statistical detectability is therefore **not** promoted to a material process↔XCT relationship.

The extremely high full-model R² together with low predictor partial R² indicates that the frozen part/block structure dominates the aggregated XCT variation; E24 does not attribute that dominance causally.

## 4. Threshold sensitivity / threshold 민감도
Prespecified area-threshold sensitivity remained directionally consistent:
- t80 beta `0.016772`, partial R² `0.025308`;
- t120 beta `0.017831`, partial R² `0.021048`;
- material sign disagreement: NO.

Thus the NO_MATERIAL result is not caused by an arbitrary sign reversal at the neighboring NIST melt-pool thresholds.

## 5. Registration negative control / registration 음성대조
Frozen +25-layer shift control:
- units: 32;
- `beta_shift25 = 0.011634`;
- `partial_R2_shift25 = 0.009379`;
- locality criterion `|beta_primary| > |beta_shift25|`: PASS.

The correctly registered association is somewhat stronger than the deliberately shifted control, but both are small. This supports limited local-registration specificity while remaining insufficient for the preregistered material-effect gate.

## 6. Part-specific rank diagnostics / part별 rank 진단
Part-specific block-level Spearman diagnostics were:
- Part 1: `-0.460255`;
- Part 2: `-0.268917`;
- Part 3: `-0.483333`;
- Part 4: `-0.694567`.

These diagnostics estimate a different structure from the two-way fixed-effect slope: they follow across-block trajectories within each part, whereas the primary beta asks for predictor association after controlling common block and part effects. The sign reversal therefore warns against pooled or naive interpretation and strengthens the requirement to keep geometry/layer structure explicit.

## 7. Uncertainty / 불확실성
NIST AMS 100-69 documents:
- melt-pool feature sensitivity to pixelation, camera noise/digitization, blur and threshold choice;
- XCT uncertainty from original imaging/reconstruction plus downscaling and registration;
- approximately 1.2-voxel positional uncertainty for reported XCT locations;
- reduced voxelwise uncertainty when using mean-filtered XCT values.

E24 used t80/t100/t120 sensitivity and the 5×5×5 XCT field prospectively, but these choices do not remove measurement/registration uncertainty. No causal interpretation is authorized.

## 8. Exposure boundary / 사전노출 경계
Inherited disclosure remains:
**`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`**.

No association/model result was inspected before the E24 design freeze. E24 performed no post-hoc feature selection, endpoint switching, nonlinear modeling, or raw-row/layer-level result publication.

## 9. Frozen gate application / 고정 gate 적용
- source/schema integrity: PASS;
- aggregated coverage: PASS;
- `partial_R2 >= 0.05`: **NO**;
- permutation p <= 0.05: YES;
- locality criterion: YES;
- no material threshold sign disagreement: YES.

Under the preregistration, `partial_R2 < 0.05` maps to:
**`NO_MATERIAL_E24_ASSOCIATION`**.

## 10. Scientific consequence / 과학적 후속
Do **not** respond by trying additional predictors, endpoints, nonlinear models or feature searches on the same data. That would convert a controlled negative result into post-hoc feature fishing.

The next highest-leverage work is a narrow diagnostic gate quantifying why part/block structure dominates the XCT outcome and separating:
1. between-block/layer-geometry variation;
2. persistent between-part/location variation;
3. remaining within-block between-part variation;
4. the small registered melt-pool contribution.

Only after this variance-structure diagnostic should the project decide whether a differently defined independent experiment is scientifically justified.

## 11. Cost / 비용
Incremental monetary cost: `0 USD`. Public standard GitHub-hosted runner and official NIST sources only; no raw artifact/cache retained.