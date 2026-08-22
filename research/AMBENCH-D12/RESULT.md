---
id: AMBENCH-D12-RESULT
type: diagnostic-result
state: COMPLETED_ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION
evidence_class: OBSERVED_DERIVED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D12/README.md
  - Issue #29
  - Run 32555864796
---

# AMBENCH-D12 Result — Repeat-Sensitive Coupling Descriptor Provenance/Stability Diagnostic
# AMBENCH-D12 결과 — repeat-sensitive coupling descriptor 출처·안정성 진단

**Issue:** #29  
**Run:** `32555864796`  
**Job:** `96989749627`  
**Run conclusion:** `success`  
**Frozen final gate:** **`ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`**  
**Cost:** verified zero-incremental-cost standard public-repository runner only; `COST-001` + `DEC-028` satisfied.  
**Raw data:** `RAW_DATA_TRANSIENT_ONLY`; no Actions artifact; `RAW_TEARDOWN=SUCCESS`.

## 1. Executive Result / 핵심 결과

**KO:** D11에서 `REPEAT_INFORMATIVE`로 분류된 5개 descriptor 모두 D12의 deterministic sampling-phase perturbation보다 repeat 간 차이가 크게 나타나 `ROBUST_TO_SAMPLING_PHASE`를 통과했다. 동시에 5/5 모두 balanced case+repeat-index decomposition에서 `repeat_index_share <= 0.25`로 `CASE_SPECIFIC_RESIDUAL_DOMINANT`였다. 즉 D11의 repeat-sensitive 변동은 factor-2/4 sample-phase 선택만으로 설명되지 않지만, repeat 1/2/3이라는 공통 번호 효과로도 설명되지 않는다. frozen gate는 **`ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`**이다.

**EN:** All five D11 `REPEAT_INFORMATIVE` descriptors showed repeat differences materially larger than the deterministic D12 sampling-phase perturbations and therefore passed `ROBUST_TO_SAMPLING_PHASE`. At the same time, all `5/5` were `CASE_SPECIFIC_RESIDUAL_DOMINANT` in the balanced case+repeat-index decomposition with `repeat_index_share <= 0.25`. Thus, D11 repeat-sensitive variation is not explained by factor-2/4 sample-phase choice alone, but it is also not explained by a common repeat-1/2/3 effect across cases. The frozen gate is **`ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`**.

This does **not** prove physical instability and does not rule out sensor/process noise, local heterogeneity, or other unobserved mechanisms. / 이는 물리적 불안정성을 증명하지 않으며 sensor/process noise·국부 이질성·미관측 메커니즘을 배제하지 않는다.

## 2. Source & Reproduction Integrity / 원천·재현 무결성

- NIST PDR `mds2-3842`, exact version `1.0.3`;
- manifest SHA-256 matched: `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb`;
- coupling ZIP `93,566 B`, SHA-256 matched: `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`;
- exact `21 = 7 cases × 3 repeats` track structure;
- D11 eight within-fractions reproduced with maximum absolute delta `< 3.2e-15`, far inside frozen `1e-9` tolerance;
- workflow completed successfully;
- Actions artifact count `0`;
- `RAW_TEARDOWN=SUCCESS`.

No integrity HOLD was triggered. / 무결성 HOLD 없음.

## 3. Primary Five Descriptor Results / 1차 5개 descriptor 결과

| Descriptor | D11 within fraction | repeat_index_share | Repeat structure | R_sampling | Sampling label |
|---|---:|---:|---|---:|---|
| `iqr_mid` | `0.5706644395` | `0.1996594728` | `CASE_SPECIFIC_RESIDUAL_DOMINANT` | `6.0948047` | `ROBUST_TO_SAMPLING_PHASE` |
| `early_contrast` | `0.2235847868` | `0.2240955606` | `CASE_SPECIFIC_RESIDUAL_DOMINANT` | `9.3127387` | `ROBUST_TO_SAMPLING_PHASE` |
| `late_contrast` | `0.3750992986` | `0.0437382268` | `CASE_SPECIFIC_RESIDUAL_DOMINANT` | `6.8407607` | `ROBUST_TO_SAMPLING_PHASE` |
| `early_shape_slope` | `0.6611836993` | `0.2096893630` | `CASE_SPECIFIC_RESIDUAL_DOMINANT` | `41.1114383` | `ROBUST_TO_SAMPLING_PHASE` |
| `late_shape_slope` | `0.7350150566` | `0.1064794815` | `CASE_SPECIFIC_RESIDUAL_DOMINANT` | `12.1920546` | `ROBUST_TO_SAMPLING_PHASE` |

Frozen primary counts:
- `representation_sensitive = 0/5`;
- `sampling_robust = 5/5`;
- `cross_case_repeat_index = 0/5`;
- `condition_specific_residual = 5/5`.

## 4. Meaning of the Sampling Test / sampling test 의미

D12 used six deterministic decimation variants per track:
- factor 2 phases `0,1`;
- factor 4 phases `0,1,2,3`;
- original full-track normalized `tau` retained.

For each descriptor:
`R_sampling = S_repeat / max(S_phase, eps)`.

All five primary descriptors had `R_sampling >= 3`, ranging from `6.09` to `41.11`. Therefore their D11 repeat differences are substantially larger than the variability induced by these frozen sample-phase perturbations.

**Boundary:** this is not a total measurement-noise model. It tests only deterministic sampling-phase sensitivity. / 전체 측정 noise를 추정한 것이 아니라 sample-phase 민감도만 검증했다.

## 5. Repeat-Index Decomposition / 반복번호 분해

Balanced decomposition separates D11 within-case variation into:
- a common repeat-index component (`repeat 1/2/3` means across cases);
- remaining case×repeat residual.

For every primary descriptor, `repeat_index_share <= 0.25`. Therefore the common repeat-number effect explains only a minority of the within-case variation.

This means:
- no evidence that repeat `1`, `2`, or `3` carries a common direction across all seven cases strong enough to dominate the D11 repeat variation;
- most repeat-sensitive variance is case-specific/idiosyncratic under this additive decomposition.

**Boundary:** repeat number is treated only as an identifier. D12 does not infer spatial position, scan order, instrument drift, or causal meaning from it.

## 6. Secondary Residual Structure / 보조 residual 구조

Case-centered, within-case-standardized PCA on the five primary descriptors:
- PC1 cumulative: `39.2353%`;
- PC1–PC2: `74.8913%`;
- PC1–PC3: `88.9949%`;
- `RESID_PCA80_DIM = 3`.

Thus the case-specific repeat residuals are neither a single common latent direction nor fully independent across five descriptors. This result is descriptive and does not change the gate.

## 7. Comparator Descriptors / 비교 descriptor

- `ac1_mid`: `R_sampling=0.0828` → `COMPARABLE_TO_SAMPLING_PHASE`; repeat-index share `0.0526`.
- `mad_diff_mid`: `R_sampling=0.0` → `COMPARABLE_TO_SAMPLING_PHASE`; repeat-index share `0.1429`.
- `median_mid`: extremely sampling-phase robust because median was invariant under the frozen decimations, but its D11 variation remained overwhelmingly case-dominated; repeat-index share `0.4063` (`MIXED_REPEAT_STRUCTURE`).

These comparators show that D12 is not mechanically labeling every descriptor as sampling-robust or repeat-informative.

## 8. Frozen Gate Application / 고정 gate 적용

### `REPRESENTATION_SENSITIVITY_DOMINANT`
Requires `>=3/5` primary descriptors `COMPARABLE_TO_SAMPLING_PHASE`.
- observed: `0/5` → **FAIL**.

### `CROSS_CASE_REPEAT_INDEX_STRUCTURE`
Requires `>=3/5` sampling-robust and `>=3/5` cross-case repeat-index structured.
- sampling-robust: `5/5` PASS;
- cross-case repeat-index structured: `0/5` FAIL.
- **FAIL**.

### `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
Requires `>=3/5` sampling-robust, `>=3/5` case-specific residual dominant, and `<3/5` representation-sensitive.
- sampling-robust: `5/5`;
- condition-specific residual dominant: `5/5`;
- representation-sensitive: `0/5`.
- **PASS**.

### `MIXED_REPEAT_PROVENANCE`
Not selected because the stronger condition-specific gate passed.

### `HOLD_DATA_INTEGRITY`
Not selected; source and D11 reproduction integrity passed.

**Final / 최종:** **`ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`**.

## 9. Interpretation Boundary / 해석 경계

Supported / 허용:
- the five D11 repeat-sensitive descriptor differences survive the frozen sample-phase perturbation test;
- those differences are not dominated by a common repeat-index effect across cases;
- under the frozen diagnostics, the residual repeat variation is condition-specific/idiosyncratic.

Not supported / 금지:
- claiming the residuals are definitely physical melt instability;
- claiming sensor noise has been ruled out;
- claiming predictive/generalizable value;
- using repeat number as a physical spatial/temporal factor without authoritative metadata;
- escalating to complex ML on the same 21 tracks merely because the variation is sampling-robust.

## 10. Consequence / 후속

The immediate scientific bottleneck is now **external validation**, not feature engineering. The D12-positive condition-specific variation should next be tested only through:
1. an independent-condition coupling dataset with equivalent temporal measurements, or
2. a qualified same-specimen physical outcome dataset.

The same-BP4 confocal branch remains `HOLD_PUBLICATION_NOT_VERIFIED`; therefore the next work should triage authoritative public sources for an **independent-condition dynamic-coupling validation asset** before any predictive model is authorized.
