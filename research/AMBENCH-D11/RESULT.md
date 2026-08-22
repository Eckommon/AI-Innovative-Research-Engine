---
id: AMBENCH-D11-RESULT
type: diagnostic-result
state: COMPLETED_MIXED_TEMPORAL_INFORMATION
evidence_class: OBSERVED_DERIVED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/README.md
  - Issue #27
  - Run 32553063163
---

# AMBENCH-D11 Result — Within-BP4 Dynamic-Coupling Temporal-Information Diagnostic
# AMBENCH-D11 결과 — BP4 내부 동적 coupling 시간정보 진단

**Issue / 이슈:** #27  
**Evidence Run / 증거 Run:** GitHub Actions `32553063163`  
**Job / Job:** `96982816961`  
**Run conclusion / 실행 결론:** `success`  
**Frozen final gate / 고정 최종 판정:** **`MIXED_TEMPORAL_INFORMATION`**  
**Cost / 비용:** `COST-001` compliant — standard public-repository `ubuntu-latest`, public NIST source, no GPU/larger runner, no paid API/SaaS/cloud/data. / 추가 금전비용 0원.  
**Raw data / raw 데이터:** `RAW_DATA_TRANSIENT_ONLY`; no raw-data Actions artifact; `RAW_TEARDOWN=SUCCESS`.

## 1. Executive Result / 핵심 결과

**KO:** BP4 dynamic-coupling의 21개 waveform은 하나의 단순한 결론으로 축약되지 않았다. 정규화 시간축 `tau=0.05..0.95`의 **원 waveform pointwise 변동은 매우 강하게 process-case 지배**였으며, 901/901 grid point 모두에서 repeat-level within-fraction이 `0.20` 이상인 지점은 하나도 없었다. 반면 사전고정 8개 temporal descriptor 중 `5/8`은 case 내부 repeat 변동 비율이 `>=0.20`인 `REPEAT_INFORMATIVE`로 나타났고, descriptor 공간의 `PCA95_DIM=6`으로 D06 thermal representation의 저차원 구조(`2`)와도 달랐다. 따라서 coupling을 단순 case proxy라고 단정하는 gate도, waveform 전체가 강한 repeat-level 정보를 가진다고 단정하는 gate도 통과하지 못해 최종 판정은 **`MIXED_TEMPORAL_INFORMATION`**이다.

**EN:** The 21 BP4 dynamic-coupling waveforms do not reduce to one simple conclusion. Pointwise variation in the normalized-time **raw waveform is strongly process-case dominated**: across all `901/901` valid grid points, none had repeat-level within-fraction `>=0.20`. In contrast, `5/8` preregistered temporal descriptors were `REPEAT_INFORMATIVE` with within-case fractions `>=0.20`, and the descriptor space had `PCA95_DIM=6`, unlike D06's low-dimensional thermal representation (`2`). Thus neither the frozen case-proxy gate nor the strong waveform-level repeat-information gate is satisfied, yielding **`MIXED_TEMPORAL_INFORMATION`**.

D11 is an information-structure diagnostic only. It does **not** establish physical-outcome utility, prediction, generalization, or causality. / D11은 정보구조 진단일 뿐 물리 outcome 효용·예측·일반화·인과성을 확립하지 않는다.

## 2. Source Integrity & Execution / 원천 무결성·실행

Frozen NIST source / 고정 NIST source:
- PDR `mds2-3842`;
- exact version `1.0.3`;
- manifest expected = actual SHA-256 `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb`;
- ZIP bytes `93,566`;
- ZIP expected = actual SHA-256 `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`;
- exact track count `21 = 7 cases × 3 repeats`;
- every frozen descriptor finite/nonconstant;
- normalized waveform valid grid points `901/901`, invalid `0`;
- workflow steps all `success`;
- Actions artifacts for the run: `0`;
- end-of-run raw teardown: `SUCCESS`.

No source-integrity HOLD condition was triggered. / source 무결성 HOLD 없음.

## 3. Frozen Descriptor Variance Results / 고정 descriptor 분산 결과

`within_fraction = SS_within / (SS_between + SS_within)`.

| Descriptor | within_fraction | Frozen label |
|---|---:|---|
| `median_mid` | `0.0003519954` | `CASE_DOMINATED` |
| `iqr_mid` | `0.5706644395` | `REPEAT_INFORMATIVE` |
| `mad_diff_mid` | `0.0000003314` | `CASE_DOMINATED` |
| `ac1_mid` | `0.1841574694` | `MIXED_VARIATION` |
| `early_contrast` | `0.2235847868` | `REPEAT_INFORMATIVE` |
| `late_contrast` | `0.3750992986` | `REPEAT_INFORMATIVE` |
| `early_shape_slope` | `0.6611836993` | `REPEAT_INFORMATIVE` |
| `late_shape_slope` | `0.7350150566` | `REPEAT_INFORMATIVE` |

Counts / 개수:
- `CASE_DOMINATED_COUNT = 2/8`;
- `REPEAT_INFORMATIVE_COUNT = 5/8`;
- `MIXED_VARIATION = 1/8`.

The result is heterogeneous by descriptor family: level/step-size summaries (`median_mid`, `mad_diff_mid`) are nearly entirely case-structured, while dispersion, edge contrast, and normalized-time slope descriptors retain much larger within-case repeat variation. / descriptor 종류별 구조가 이질적이다.

## 4. Direct Normalized-Waveform Diagnostic / 직접 정규화 waveform 진단

Frozen grid: `tau = 0.050, 0.051, ..., 0.950` (`901` points).

- valid points: `901`;
- invalid points: `0`;
- `WF_MEDIAN_WITHIN = 0.0043387546`;
- `WF_HIGH_REPEAT_FRACTION = 0.0`.

Thus the **pointwise waveform amplitude/shape is overwhelmingly between-case structured** under this normalized-time comparison. No grid point reaches the preregistered `within_fraction >= 0.20` high-repeat threshold. / pointwise waveform 자체는 강한 case 구조이며 high-repeat grid point는 0개다.

This result is not contradicted by the descriptor result: nonlinear/summary descriptors such as IQR, contrasts, and slopes can amplify track-to-track differences that remain small relative to the dominant absolute waveform-level case separation. / summary descriptor의 repeat 변동과 waveform amplitude의 case 지배는 동시에 성립할 수 있다.

## 5. Descriptor Effective Dimension / descriptor 유효차원

All eight descriptors were valid.

- PC1 cumulative explained variance: `31.7476%`
- PC1–PC2: `54.0017%`
- PC1–PC3: `72.1967%`
- PC1–PC4: `85.6556%`
- PC1–PC5: `92.7997%`
- PC1–PC6: `96.2788%`
- **`PCA95_DIM = 6`**

This is structurally different from D06, where `PCA95_DIM=2` for the eight thermal occupancy features. However, D11 does not interpret higher descriptor dimension as proven physical information or usefulness. / D06보다 고차원이지만 이를 물리적 효용 증명으로 해석하지 않는다.

## 6. Descriptive Process Association / 기술적 process 연관

Seven case medians only; these associations cannot change the frozen gate. / 7개 case median만 사용하며 gate 변경 불가.

Notable `|rho| >= 0.80` associations:
- `median_mid` ↔ normalized VED: `rho = +0.9285714`;
- `median_mid` ↔ beam diameter: `rho = -0.8017837`;
- `mad_diff_mid` ↔ laser power: `rho = -0.8846517`;
- `early_contrast` ↔ beam diameter: `rho = -0.8017837`;
- `early_shape_slope` ↔ beam diameter: `rho = +0.8017837`.

Other descriptor/process associations were below the frozen descriptive strong-association threshold. These are seven-case associations and are not causal evidence. / 7-case 기술적 상관이며 인과 근거가 아니다.

## 7. Frozen Gate Application / 고정 gate 적용

### `COUPLING_PROCESS_CASE_PROXY_DOMINANT`
Requires all:
- `>=6/8` case-dominated descriptors → **FAIL (`2/8`)**;
- `WF_MEDIAN_WITHIN <=0.10` → **PASS (`0.0043388`)**;
- `PCA95_DIM <=3` → **FAIL (`6`)**.

### `REPEAT_LEVEL_TEMPORAL_INFORMATION_PRESENT`
Requires all:
- `>=3/8` repeat-informative descriptors → **PASS (`5/8`)**;
- `WF_MEDIAN_WITHIN >=0.20` → **FAIL (`0.0043388`)**;
- `WF_HIGH_REPEAT_FRACTION >=0.50` → **FAIL (`0.0`)**.

### `HOLD_DATA_INTEGRITY`
**FAIL** — all integrity checks passed.

### Final / 최종
**`MIXED_TEMPORAL_INFORMATION`**.

## 8. Interpretation Boundary / 해석 경계

Supported / 허용:
- direct normalized waveform amplitude is strongly case-structured;
- five frozen derived temporal descriptors contain substantial within-case repeat variation under the preregistered variance heuristic;
- descriptor representation is materially higher-dimensional than the prior D06 thermal representation;
- the coupling modality has a mixed information structure that should not be collapsed to either “pure case proxy” or “clear repeat-level waveform signal.”

Not supported / 금지:
- claiming coupling predicts melt-pool/topography outcomes;
- claiming the repeat-varying descriptors are physically meaningful without an independent outcome/validation source;
- claiming higher `PCA95_DIM` means better information automatically;
- tuning D11 descriptors/windows/thresholds to obtain a stronger label;
- escalating to FFT/wavelet/neural features or higher-capacity models inside D11;
- treating 21 tracks as 21 independent process conditions.

## 9. Consequence / 후속

The frozen D11 consequence for `MIXED_TEMPORAL_INFORMATION` applies:
1. preserve the mixed result without post-hoc tuning;
2. do not promote coupling to physical utility/predictive evidence;
3. do not simply escalate model capacity on the same 21 tracks;
4. a next step must be separately preregistered and should distinguish whether the repeat-sensitive descriptor family reflects reproducible temporal morphology, measurement/noise structure, or condition-specific instability before any predictive use;
5. independent-condition or qualified same-specimen physical-outcome validation remains necessary for broader promotion.

**Disposition / 처리:** complete Issue #27 as `MIXED_TEMPORAL_INFORMATION`. / Issue #27을 MIXED 결과로 완료 종료.
