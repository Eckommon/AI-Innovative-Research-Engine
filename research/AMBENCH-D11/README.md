---
id: AMBENCH-D11
type: diagnostic-preregistration
state: PREREGISTERED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D06/RESULT.md
  - research/AMBENCH-E09/RESULT.md
  - research/AMBENCH-F10/RESULT.md
  - registry/DEC-026.md
---

# AMBENCH-D11 — Within-BP4 Dynamic-Coupling Temporal-Information Diagnostic
# AMBENCH-D11 — BP4 내부 동적 coupling 시간정보 진단

## 1. Purpose / 목적

**KO:** checksum-verified NIST `mds2-3842` BP4 dynamic-laser-coupling 21개 waveform(`7 cases × 3 repeats`)이 process-case label을 단순 재표현하는지, 아니면 case 내부 repeat 수준에서 독립적인 시간구조 변동을 보존하는지를 진단한다.

**EN:** Diagnose whether the 21 checksum-verified NIST `mds2-3842` BP4 dynamic-laser-coupling waveforms (`7 cases × 3 repeats`) merely re-express process-case labels or preserve independent repeat-level temporal variation within cases.

D11 is an **information-structure diagnostic**, not a predictive, causal, or physical-outcome validation experiment. / D11은 정보구조 진단이며 예측·인과·물리 outcome 검증 실험이 아니다.

## 2. Why D11 Is the Next Eligible Step / D11 선정 이유

- D06 found the prior BP1 thermal representation `PROCESS_CASE_PROXY_DOMINANT`: all `8/8` features were case-dominated and `PCA95_DIM=2`.
- E09 showed that BP4 coupling changed predictor magnitude but not the seven-case rank; all frozen rank endpoints had `delta_rho=0`.
- F10 verified that same-BP4 confocal measurement occurred but could not establish an exact current public version-identifiable confocal dataset, so the frozen fallback is a within-BP4 temporal-information diagnostic.
- D11 therefore tests the distinct coupling modality **without collapsing each track to one case-level scalar/rank** and without inventing a physical outcome.

## 3. Data Boundary / 데이터 경계

Frozen source / 고정 source:
- NIST PDR: `mds2-3842`
- exact version: `1.0.3`
- coupling ZIP bytes: `93,566`
- expected SHA-256: `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`
- expected files: `21 = 7 cases × 3 repeats`
- case `3.2` archive identity: `3_2_1sv.txt`, `3_2_2sv.txt`, `3_2_3sv.txt` directly verified in E09
- coupling sampling: `100 kHz`
- coupling observable: dimensionless `P_lc = 1 - P_rho/P_app`

`RAW-001` applies: source ZIP/text bytes are transient only. / source bytes는 일시 처리하며 repo에 영구 저장하지 않는다.

## 4. Prior-Observation Disclosure / 기존 관측 공개

- `RAW_COUPLING_PREOBSERVED = YES` — the coupling time-series files were numerically accessed during E09 execution.
- `E09_CASE_MEDIANS_PREOBSERVED = YES` — seven case medians are already known.
- `NEW_D11_TEMPORAL_DIAGNOSTICS_UNCOMPUTED_AT_PREREG = YES` — the D11 descriptor variance decomposition, normalized-waveform variance decomposition, and D11 PCA gate have not been computed before this preregistration.

D11 must **not** be described as fully outcome-blind. / D11을 full outcome-blind로 표현하지 않는다.

## 5. Frozen Parsing & Normalized Time / 고정 parsing·정규화 시간

For every track / 각 track:
1. read only finite `(t, P_lc)` rows;
2. require at least 100 finite rows;
3. require non-decreasing time and `t_max > t_min`;
4. define `tau = (t - t_min)/(t_max - t_min)`;
5. primary shape domain: `0.05 <= tau <= 0.95`;
6. primary central domain: `0.20 <= tau <= 0.80`;
7. no smoothing, manual crop, peak picking, target-aware filtering, or case-specific preprocessing.

`tau`-slope descriptors below are normalized-shape slopes, **not physical time derivatives**. / `tau` 기울기는 shape descriptor이며 실제 시간미분으로 해석하지 않는다.

## 6. Frozen Eight Temporal Descriptors / 고정 8개 시간 descriptor

Exactly these eight track-level descriptors are primary / 아래 8개만 주 descriptor:

1. `median_mid`  
   `median(P_lc)` for `0.20 <= tau <= 0.80`.

2. `iqr_mid`  
   `Q75(P_lc) - Q25(P_lc)` for `0.20 <= tau <= 0.80`.

3. `mad_diff_mid`  
   median absolute consecutive-sample difference `median(|P_lc[i+1]-P_lc[i]|)` within the central domain.

4. `ac1_mid`  
   lag-1 Pearson autocorrelation of consecutive central-domain samples.

5. `early_contrast`  
   `median(P_lc, 0.05<=tau<0.20) - median_mid`.

6. `late_contrast`  
   `median(P_lc, 0.80<tau<=0.95) - median_mid`.

7. `early_shape_slope`  
   ordinary least-squares slope of `P_lc` versus `tau` over `0.05<=tau<0.20`.

8. `late_shape_slope`  
   ordinary least-squares slope of `P_lc` versus `tau` over `0.80<tau<=0.95`.

No descriptor may be replaced, added, or dropped because of the observed result. / 결과를 보고 descriptor를 교체·추가·삭제하지 않는다.

## 7. Primary Diagnostic A — Descriptor Repeat-vs-Case Variance / descriptor 반복-vs-case 분산

For each descriptor `f` across the 21 tracks:
- `SS_between = sum_c n_c (mean_c - grand_mean)^2`, with `n_c=3`;
- `SS_within = sum_c sum_r (x_cr - mean_c)^2`;
- `within_fraction_f = SS_within / (SS_between + SS_within)`.

Frozen descriptor labels / 고정 분류:
- `CASE_DOMINATED` if `within_fraction <= 0.10`;
- `MIXED_VARIATION` if `0.10 < within_fraction < 0.20`;
- `REPEAT_INFORMATIVE` if `within_fraction >= 0.20`.

The thresholds are diagnostic heuristics frozen before D11 execution, not significance levels. / 통계적 유의수준이 아닌 사전고정 진단 휴리스틱.

## 8. Primary Diagnostic B — Normalized-Waveform Variance / 정규화 waveform 분산

To test the waveform directly rather than only descriptors:

1. linearly interpolate each track on the fixed grid `tau = 0.050, 0.051, ..., 0.950` (`901` points);
2. at each grid point `j`, compute the same seven-case/three-repeat `within_fraction_j` using between/within sums of squares;
3. exclude only a grid point whose total variance is numerically zero (`<=1e-15`);
4. report:
   - `WF_MEDIAN_WITHIN = median(within_fraction_j)` over valid grid points;
   - `WF_HIGH_REPEAT_FRACTION = fraction(valid j with within_fraction_j >= 0.20)`.

If more than `10%` of the 901 grid points are invalid/undefined, D11 is `HOLD_DATA_INTEGRITY`. / grid 10% 초과 undefined 시 무결성 HOLD.

## 9. Primary Diagnostic C — Effective Dimension / 유효차원

Build the `21 × 8` descriptor matrix.

- standardize each non-constant descriptor with sample mean and sample standard deviation;
- compute SVD/PCA;
- `PCA95_DIM` = minimum number of PCs reaching cumulative explained variance `>=95%`.

If more than two primary descriptors are undefined or constant across all 21 tracks, D11 is `HOLD_DATA_INTEGRITY`. Constant/undefined descriptors are not silently replaced. / 2개 초과 descriptor가 무정의·상수면 HOLD이며 대체 금지.

## 10. Secondary Diagnostic — Process Association / 보조 process 연관성

This diagnostic is descriptive and **cannot change the final gate**.

For each descriptor:
1. take the seven case medians;
2. compute Spearman correlation separately with official BP4 case-level:
   - laser power;
   - scan speed;
   - beam diameter `D4sigma`;
   - official normalized `VEDsigma/VEDsigma0`;
3. report all correlations;
4. label `STRONG_PROCESS_ASSOCIATION` descriptively when `|rho| >= 0.80`.

Do not duplicate case-level process values across 21 tracks and treat them as 21 independent process observations. / case process값을 21개 독립관측처럼 복제하여 추론하지 않는다.

## 11. Frozen Final Gates / 고정 최종 판정

Apply exactly one gate after integrity checks.

### `COUPLING_PROCESS_CASE_PROXY_DOMINANT`
All must hold:
1. at least `6/8` descriptors are `CASE_DOMINATED` (`within_fraction <=0.10`);
2. `WF_MEDIAN_WITHIN <= 0.10`;
3. `PCA95_DIM <= 3`.

Interpretation: the tested coupling representation is predominantly case-structured, analogous to D06's diagnostic conclusion. / 시험한 coupling 표현이 주로 case 구조를 재표현.

### `REPEAT_LEVEL_TEMPORAL_INFORMATION_PRESENT`
All must hold:
1. at least `3/8` descriptors are `REPEAT_INFORMATIVE` (`within_fraction >=0.20`);
2. `WF_MEDIAN_WITHIN >= 0.20`;
3. `WF_HIGH_REPEAT_FRACTION >= 0.50`.

Interpretation: coupling preserves material repeat-level temporal variation beyond case labels under this diagnostic. This **does not establish physical usefulness or predictive value**. / case label을 넘는 repeat 수준 시간변동은 있으나 물리적 효용·예측력을 뜻하지 않음.

### `MIXED_TEMPORAL_INFORMATION`
Integrity passes but neither of the two gates above is fully satisfied. / 무결성 통과 후 위 두 조건 모두 충족하지 않음.

### `HOLD_DATA_INTEGRITY`
Any material source/checksum/schema/identity/parser failure, fewer than 21 authoritative tracks, more than two undefined/constant primary descriptors, or more than 10% invalid normalized-waveform grid points. / 데이터 무결성 문제.

## 12. No-Post-Hoc Rules / 사후 변경 금지

After D11 numerical execution begins, do not:
- change the eight primary descriptors;
- change `tau` windows or interpolation grid;
- change thresholds `0.10`, `0.20`, `6/8`, `3/8`, `0.50`, or `PCA95_DIM<=3`;
- smooth waveforms or add FFT/wavelet/neural features to rescue a result;
- add BP1 thermography/optical or unavailable BP4 confocal outcomes;
- infer physical utility from repeat-level information alone;
- escalate model capacity inside D11.

Any such continuation requires a new preregistered hypothesis. / 변경·확장은 별도 사전등록 필요.

## 13. Cost & Execution Boundary / 비용·실행 경계

- `COST-001`: zero incremental monetary cost only.
- Eligible execution: public NIST source + local compute or standard public-repository GitHub-hosted runner.
- no paid API/SaaS/cloud/GPU/larger runner;
- no raw-data Actions artifact upload;
- `RAW-001` transient download/teardown.

## 14. Consequence / 후속 규칙

- `COUPLING_PROCESS_CASE_PROXY_DOMINANT` → deprioritize same-21-track coupling feature/model escalation; prioritize genuinely new independent conditions or wait for a qualified same-specimen physical outcome source.
- `REPEAT_LEVEL_TEMPORAL_INFORMATION_PRESENT` → permit a new preregistered follow-up aimed at identifying a qualified physical outcome or independent-condition validation; do not claim utility from D11 alone.
- `MIXED_TEMPORAL_INFORMATION` → preserve mixed structure and triage which descriptor family carries repeat variation before any modeling, under a separate preregistration.
- `HOLD_DATA_INTEGRITY` → stop and resolve source/integrity issues before interpretation.

**State:** `PREREGISTERED — EXECUTION NOT YET RUN`.
