# AMBENCH-D06 Result / outcome 비사용 열표현 구조 진단 결과

**Issue / 이슈:** #19  
**Evidence Run / 증거 Run:** `32541722347`  
**Run conclusion / 실행 결론:** `success`  
**Frozen gate / 고정 게이트:** **`PROCESS_CASE_PROXY_DOMINANT`**  
**Outcome use / outcome 사용:** none / 없음  
**Cost / 비용:** `COST-001` compliant — public repository standard `ubuntu-latest`; no larger/GPU runner, paid API/data, optical download, or artifact upload. / 추가 금전비용 없는 경로.

## 1. Executive Result / 핵심 결과

**KO:** E05의 사전고정 8개 calibrated thermal occupancy feature는 21개 track의 반복 수준 독립변동보다 **7개 process-case 차이를 매우 강하게 재표현**하는 구조로 나타났다. 8/8 feature의 case 내부 분산 비율이 사전 기준 `0.10` 이하였고, 표준화된 8차원 thermal 표현의 분산 95% 이상을 설명하는 데 필요한 주성분은 `2개`뿐이었다. 따라서 사전등록 gate는 `PROCESS_CASE_PROXY_DOMINANT`다. 이 결과는 E05의 width 개선을 지우지 않지만, 이를 독립 repeat-level 신호 또는 일반화 가능한 물리법칙으로 승격하는 것을 지지하지 않는다.

**EN:** The eight preregistered E05 calibrated thermal occupancy features primarily **re-express the seven process-case differences** rather than preserving substantial independent repeat-level variation across the 21 tracks. All 8/8 features had within-case variance fractions below the frozen `0.10` threshold, and only `2` principal components were required to explain at least 95% of the standardized 8D thermal variance. The preregistered gate therefore resolves to `PROCESS_CASE_PROXY_DOMINANT`. This does not erase the E05 width improvement, but it does not support promoting that improvement to an independent repeat-level signal or a generalizable physical law.

## 2. Integrity / 무결성

- exact frozen thermography bytes: `549,979,044`
- actual SHA-256 = expected SHA-256 = `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- exactly `21` tracks = `7` process cases × `3` repeats
- exact E05 calibration coefficients and `30,000 fps` metadata verified
- exact E05 integer thresholds `366 / 836 / 1081 / 1380 DL`
- exactly the same 8 E05 thermal features reproduced
- no optical depth/width file was downloaded or used
- workflow job and all diagnostic steps completed `success`

## 3. Primary Diagnostic A — Repeat-vs-Case Variance / 반복·case 분산

Frozen rule: a feature is `CASE_DOMINATED` when `within_fraction <= 0.10`.

| Thermal feature | within_fraction | Gate |
|---|---:|---|
| `hot_pixel_time_integral_1150_px_s` | `0.0010494751` | `CASE_DOMINATED` |
| `any_hot_duration_1150_s` | `0.0000901699` | `CASE_DOMINATED` |
| `hot_pixel_time_integral_1260_px_s` | `0.0039033959` | `CASE_DOMINATED` |
| `any_hot_duration_1260_s` | `0.0005043360` | `CASE_DOMINATED` |
| `hot_pixel_time_integral_1298_px_s` | `0.0040152346` | `CASE_DOMINATED` |
| `any_hot_duration_1298_s` | `0.0000727159` | `CASE_DOMINATED` |
| `hot_pixel_time_integral_1336_px_s` | `0.0046257915` | `CASE_DOMINATED` |
| `any_hot_duration_1336_s` | `0.0000974706` | `CASE_DOMINATED` |

**Result / 결과:** `case_dominated_count = 8/8`.

The within-case fractions are not merely below `0.10`; all are below approximately `0.00463`, indicating that the dominant variance in these eight features occurs between process cases. / 단순 threshold 통과 수준을 넘어, 8개 모두 약 `0.00463` 이하로 case 간 변동이 압도적이다.

## 4. Primary Diagnostic B — Thermal Effective Dimension / thermal 유효차원

Standardized 8D thermal PCA/SVD: / 표준화 8D PCA/SVD

- PC1 cumulative explained variance: `78.6005%`
- PC1–PC2 cumulative explained variance: `98.2647%`
- PC1–PC3 cumulative explained variance: `99.9446%`
- `PCA95_DIM = 2`

Frozen rule `LOW_DIMENSIONAL if PCA95_DIM <= 3` therefore passes. / 저차원 조건 통과.

## 5. Secondary Diagnostic — Process Association / process 연관성

`strong_process_count = 4/8` at frozen `|r| >= 0.90`.

All four `any_hot_duration_*` features were strongly associated with scan speed: / 네 duration feature 모두 scan speed와 강한 연관

- `1150 °C`: `r = -0.980971`
- `1260 °C`: `r = -0.983176`
- `1298 °C`: `r = -0.984337`
- `1336 °C`: `r = -0.985145`

This is descriptive association only and is not a causal claim. / 기술적 연관이며 인과 주장이 아니다.

## 6. Secondary Diagnostic — LOCO Geometry & Conditioning / LOCO 구조·conditioning

Across the seven LOCO training folds: / 7개 fold

- process-only condition number remained approximately `1.006–1.058`;
- thermal-only condition number was approximately `221.8–488.8`;
- combined condition number was approximately `434.9–1298.0`.

All tested matrices retained numerical rank, but thermal/combined feature spaces were substantially more ill-conditioned than the process-only design. These are secondary diagnostics and do not alter the frozen gate. / rank는 유지됐으나 thermal/combined 공간의 conditioning이 훨씬 나빴으며, 이는 보조지표로 gate를 변경하지 않는다.

LOCO nearest-neighbor distances also varied substantially by held-out process case, consistent with heterogeneous extrapolation geometry. No post-hoc distance threshold is introduced. / case별 외삽거리가 크게 달랐으며 사후 threshold는 추가하지 않는다.

## 7. Frozen Gate Application / 고정 게이트 적용

Primary conditions: / 주 조건

- `case_dominated_count >= 6` → **TRUE (`8/8`)**
- `PCA95_DIM <= 3` → **TRUE (`2`)**

Frozen rule: both true → **`PROCESS_CASE_PROXY_DOMINANT`**.

No secondary metric changes this classification. / 보조지표로 판정을 변경하지 않는다.

## 8. Interpretation Boundary / 해석 경계

Supported / 지지되는 해석:
- the current eight E05 thermal features contain very little within-process-case repeat variation relative to between-case variation;
- their standardized geometry is effectively low-dimensional;
- the four duration features strongly track scan speed descriptively;
- E05's apparent width benefit may arise from a process-case-level re-expression and therefore requires independent information before broader promotion.

Not supported / 지지되지 않는 해석:
- thermography is useless;
- the E05 width result was false;
- scan speed causally determines every thermal feature;
- the 21 repeats are equivalent to 21 independent process conditions;
- a larger model on the same features/tracks would necessarily improve generalization.

## 9. Decision Consequence / 후속 의사결정

Under the preregistered consequence for `PROCESS_CASE_PROXY_DOMINANT`: / 사전등록 후속규칙

1. **do not escalate model capacity on the same 21 tracks and same representation**; / 동일 21-track·표현에서 모델 고용량화 금지
2. prioritize **additional independent process-condition evidence** or a **genuinely different sensing/data relationship**; / 독립 공정조건 또는 새로운 sensing/data 관계 우선
3. any predictive follow-up requires a new preregistration; / 예측 후속은 별도 사전등록
4. the E05 width improvement remains recorded as `MIXED`, not promoted to a general law. / E05 width 결과는 MIXED로 보존.

## 10. Cost & Reproducibility / 비용·재현성

The run used the repository's public standard GitHub-hosted runner and public/free NIST/PyPI inputs only. No larger/GPU runner, optical outcome download, or Actions artifact upload was used. / public 표준 runner·무료 공개입력만 사용했다.

**Disposition / 처리:** close D06 as `COMPLETED — PROCESS_CASE_PROXY_DOMINANT` and move the project to independent-information candidate triage. / D06 종료 후 독립정보 확대 후보 선별로 이동.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and frozen-gate controls. / 관련 규약 준수.
