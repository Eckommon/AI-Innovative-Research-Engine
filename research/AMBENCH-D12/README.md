---
id: AMBENCH-D12
type: diagnostic-preregistration
state: PREREGISTERED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/RESULT.md
  - DEC-027
  - DEC-028
---

# AMBENCH-D12 — Repeat-Sensitive Coupling Descriptor Provenance/Stability Diagnostic
# AMBENCH-D12 — repeat-sensitive coupling descriptor 출처·안정성 진단

## 1. Purpose / 목적

**KO:** D11에서 `REPEAT_INFORMATIVE`로 분류된 BP4 dynamic-coupling temporal descriptor의 within-case 변동이 (a) sampling/representation 민감도 수준인지, (b) case를 넘어 반복번호에 일관된 구조인지, 또는 (c) sampling-phase 변화보다 큰 condition-specific case×repeat 변동인지 구분한다.

**EN:** Determine whether the within-case variation of D11 repeat-sensitive BP4 dynamic-coupling temporal descriptors is (a) comparable to sampling/representation sensitivity, (b) structured consistently by repeat index across cases, or (c) condition-specific case×repeat variation that is materially larger than sampling-phase sensitivity.

D12 is a **provenance/stability diagnostic**, not a physical-outcome, prediction, or causality experiment. / D12는 provenance·안정성 진단이며 물리 outcome·예측·인과 실험이 아니다.

## 2. Why This Is Next / 다음 단계인 이유

D11 produced `MIXED_TEMPORAL_INFORMATION`:
- direct normalized waveform: strongly case-structured (`WF_MEDIAN_WITHIN=0.0043387546`, `WF_HIGH_REPEAT_FRACTION=0.0`);
- `5/8` derived descriptors: within-case fraction `>=0.20`;
- `PCA95_DIM=6`.

The unresolved question is whether the five repeat-sensitive descriptors represent robust track-level temporal morphology or are substantially explained by representation/sampling sensitivity or condition-specific instability. No higher-capacity model is justified until this provenance question is narrowed.

## 3. Source & Cost Boundary / 원천·비용 경계

Frozen source:
- NIST PDR `mds2-3842`;
- version `1.0.3`;
- manifest SHA-256 `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb`;
- ZIP `93,566 B`;
- ZIP SHA-256 `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`;
- `21 = 7 cases × 3 repeats` authoritative track files.

Governance:
- `RAW-001`: source bytes transient-only;
- `COST-001` + `DEC-028`: zero incremental monetary cost path only unless explicit user approval exists **before** any potentially billable action;
- no paid API/data/SaaS/cloud/GPU/larger runner/storage/artifact route;
- if zero-charge status cannot be established: `HOLD_COST_APPROVAL`, no execution.

## 4. Outcome/Selection Boundary / outcome·선정 경계

- `FULL_OUTCOME_BLIND = NO` — D11 descriptor results are already observed.
- `NEW_D12_DIAGNOSTIC_BLIND = YES` — D12 additive-decomposition and sampling-phase robustness statistics have not been computed before this preregistration.
- The primary descriptor subgroup is **explicitly conditioned on D11**; this is a follow-up provenance test, not fresh discovery.

Frozen D11 descriptor set / 전체 8개:
1. `median_mid`
2. `iqr_mid`
3. `mad_diff_mid`
4. `ac1_mid`
5. `early_contrast`
6. `late_contrast`
7. `early_shape_slope`
8. `late_shape_slope`

Primary D11 repeat-sensitive subgroup / 1차 5개:
- `iqr_mid`
- `early_contrast`
- `late_contrast`
- `early_shape_slope`
- `late_shape_slope`

Comparators / 비교군:
- `ac1_mid` — D11 `MIXED_VARIATION`;
- `median_mid`, `mad_diff_mid` — D11 `CASE_DOMINATED` negative controls.

No descriptor may be added or removed after D12 execution begins. / 실행 후 descriptor 추가·삭제 금지.

## 5. Frozen Descriptor Definitions / 고정 descriptor 정의

Use exactly the D11 definitions and native finite coupling samples after normalized time:
`tau = (t - t_min)/(t_max - t_min)`.

Windows:
- early: `0.05 <= tau < 0.20`
- mid: `0.20 <= tau <= 0.80`
- late: `0.80 < tau <= 0.95`

Definitions are identical to D11; no smoothing or target-aware filtering. / D11과 동일하며 smoothing·사후필터 금지.

## 6. D11 Reproduction Integrity Gate / D11 재현 무결성

Before interpreting D12, reproduce the D11 baseline descriptor values and within-fractions from the exact source.

Required:
- 21 tracks and 3 repeats per each of 7 cases;
- all 8 descriptors finite/nonconstant;
- each D11 descriptor within-fraction reproduced to absolute tolerance `<= 1e-9` against the durable D11 values;
- exact source hashes match.

Any failure → `HOLD_DATA_INTEGRITY`; do not continue to provenance interpretation.

## 7. Diagnostic A — Balanced Case + Repeat-Index Decomposition / 진단 A

For each descriptor `d`, on the balanced `7 cases × 3 repeats` table `y(c,r)`:

- grand mean `g`;
- case means `m_c`;
- repeat-index means `m_r`.

Frozen sums of squares:
- `SS_case = 3 * Σ_c (m_c - g)^2`
- `SS_repeat = 7 * Σ_r (m_r - g)^2`
- `SS_residual = Σ_(c,r) [y(c,r) - m_c - m_r + g]^2`

Because the design is balanced, D11 within-case variation decomposes as:
`SS_within = SS_repeat + SS_residual`.

Primary provenance statistic:
`repeat_index_share = SS_repeat / (SS_repeat + SS_residual)`.

Frozen label:
- `CROSS_CASE_REPEAT_INDEX_STRUCTURED` if `repeat_index_share >= 0.50`;
- `CASE_SPECIFIC_RESIDUAL_DOMINANT` if `repeat_index_share <= 0.25`;
- `MIXED_REPEAT_STRUCTURE` otherwise.

**Interpretation boundary:** repeat index is an authoritative repeat identifier only. D12 does not infer physical position, scan chronology, sensor drift, or causal mechanism from repeat numbers unless an authoritative source independently establishes it.

## 8. Diagnostic B — Sampling-Phase Robustness / 진단 B

Purpose: test whether D11 repeat differences materially exceed deterministic native-sample phase sensitivity.

For every track, retain the original `tau` values and recompute all 8 descriptors on the following frozen decimation variants:
- factor 2, phases `{0,1}`;
- factor 4, phases `{0,1,2,3}`.

Thus each track has six decimated descriptor estimates. Do **not** renormalize `tau` after decimation; use original full-track `tau` so the perturbation reflects sampling phase only.

For each descriptor `d`:

`S_repeat(d) = median over 7 cases of MAD across the 3 baseline repeat values`

`S_phase(d) = median over 21 tracks of MAD across the 6 decimation-phase estimates`

with standard MAD `median(|x - median(x)|)`.

Define scale safeguard:
`eps_d = max(1e-12, 1e-9 * IQR_21_baseline(d))`.

Frozen robustness ratio:
`R_sampling(d) = S_repeat(d) / max(S_phase(d), eps_d)`.

Frozen label:
- `ROBUST_TO_SAMPLING_PHASE` if `R_sampling >= 3.0`;
- `COMPARABLE_TO_SAMPLING_PHASE` if `R_sampling <= 1.5`;
- `INTERMEDIATE_SAMPLING_ROBUSTNESS` otherwise.

This tests only deterministic sampling-phase sensitivity; it does **not** quantify total sensor noise. / deterministic sampling phase만 검사하며 전체 sensor noise 추정이 아니다.

## 9. Secondary Cross-Descriptor Residual Structure / 보조 residual 구조

For the five primary D11 repeat-sensitive descriptors only:
1. subtract each descriptor's case mean from every track;
2. standardize each descriptor by its pooled within-case standard deviation;
3. run PCA on the `21 × 5` case-centered residual matrix;
4. report `RESID_PCA80_DIM` and cumulative variance.

This is descriptive only and cannot change the final gate. A low-dimensional residual pattern may indicate coordinated repeat variation but cannot identify whether the mechanism is physical or instrumental.

## 10. Frozen Final Gates / 고정 최종 판정

Apply only to the five primary D11 repeat-sensitive descriptors after integrity passes.

### `REPRESENTATION_SENSITIVITY_DOMINANT`
At least `3/5` primary descriptors are `COMPARABLE_TO_SAMPLING_PHASE`.

### `CROSS_CASE_REPEAT_INDEX_STRUCTURE`
All must hold:
- at least `3/5` primary descriptors are `ROBUST_TO_SAMPLING_PHASE`;
- at least `3/5` primary descriptors are `CROSS_CASE_REPEAT_INDEX_STRUCTURED`;
- fewer than `3/5` are `COMPARABLE_TO_SAMPLING_PHASE`.

### `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
All must hold:
- at least `3/5` primary descriptors are `ROBUST_TO_SAMPLING_PHASE`;
- at least `3/5` primary descriptors are `CASE_SPECIFIC_RESIDUAL_DOMINANT`;
- fewer than `3/5` are `COMPARABLE_TO_SAMPLING_PHASE`.

### `MIXED_REPEAT_PROVENANCE`
Integrity passes but none of the three stronger provenance gates is satisfied.

### `HOLD_DATA_INTEGRITY`
Any frozen source/hash/track-count/D11-reproduction/descriptor-validity failure.

## 11. No-Post-Hoc Rules / 사후 변경 금지

After numerical execution begins, do not:
- change descriptor definitions or windows;
- change decimation factors/phases;
- substitute smoothing, FFT, wavelet, neural features, or filters;
- change `0.50`, `0.25`, `3.0`, `1.5`, or `3/5` thresholds;
- exclude an inconvenient case/repeat absent a preregistered integrity failure;
- infer physical cause from repeat index;
- promote a robust descriptor to physical usefulness without an independent-condition or qualified physical-outcome validation.

Any such change requires a new preregistered hypothesis. / 변경은 별도 사전등록 필요.

## 12. Consequence / 후속 규칙

- `REPRESENTATION_SENSITIVITY_DOMINANT` → deprioritize D11 repeat-sensitive descriptors; do not model them as independent signal.
- `CROSS_CASE_REPEAT_INDEX_STRUCTURE` → next step is metadata/source investigation of what repeat index could represent; no physical-cause claim yet.
- `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION` → next step is an independent-condition or same-specimen outcome validation path when a qualified source exists; meanwhile classify the variation as robust but causally unresolved.
- `MIXED_REPEAT_PROVENANCE` → no model escalation; triage only the descriptor families that are both sampling-robust and provenance-coherent under a new preregistration.
- `HOLD_DATA_INTEGRITY` → stop and resolve source/reproduction conflict before further analysis.

**State:** `PREREGISTERED — D12 NUMERICAL DIAGNOSTICS NOT YET RUN`.
