---
id: AMBENCH-E03
type: experiment
state: COMPLETED_NO_MATERIAL_GAIN
evidence_class: VALIDATED
region: us
domain: manufacturing
tags:
  - type/experiment
  - state/validated
  - evidence/validated
  - region/us
  - domain/manufacturing
  - domain/additive-manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-001/README.md
  - research/AMBENCH-F02/README.md
  - research/AMBENCH-E03/RESULT.md
---

# AMBENCH-E03 — Track-level Thermography → Melt-Pool Geometry Controlled Experiment / Track-level 열화상→용융풀 형상 통제실험

**Issue / 이슈:** #13  
**State / 상태:** `COMPLETED — NO_MATERIAL_GAIN`  
**Evidence Run / 증거 Run:** `32537495534`  
**Parent feasibility / 상위 feasibility:** `AMBENCH-F02 — PASS`

## 1. Research Question / 연구 질문

**KO:** exact 21-track 수준에서 thermography 정보가 laser power·scan speed·spot size만 사용하는 process baseline보다 melt-pool depth/width 예측력을 실질적으로 향상시키는가?  
**EN:** At the exact 21-track level, does thermography provide material predictive value for melt-pool depth/width beyond a process-only baseline using laser power, scan speed, and spot size?

## 2. Frozen Design / 고정 설계

- NIST thermography `mds2-2716`, PDR v1.3.1; SHA-256 `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- NIST optical workbook `mds2-2718`; SHA-256 `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`
- canonical observations: `21` physical tracks = 7 process cases × 3 repeats
- each track's two optical cross-sections remain nested measurements; target = their mean depth/width
- validation: seven-fold leave-one-process-case-out (18 train / 3 held-out tracks per fold)
- estimator for every model: fold-local `StandardScaler` + `Ridge(alpha=1.0, fit_intercept=True)`
- `PROCESS_ONLY`: laser power + scan speed + spot size
- `THERMO_ONLY`: 10 outcome-blind raw-digital-level thermal summaries
- `PROCESS_PLUS_THERMO`: all 13 features
- no tuning, random row split, deep model, or post-result feature expansion

The thermal feature manifest, estimator, pooled metric definition and gate precedence were committed before optical outcomes were combined with the model pipeline. / thermal feature·추정기·pooled metric·gate 우선순위는 optical outcome 결합 전에 GitHub에 고정했다.

## 3. Frozen Thermography Feature Manifest / 고정 열화상 feature

1. `thermal_nonzero_fraction`
2. `thermal_positive_mean_dl`
3. `thermal_positive_std_dl`
4. `thermal_positive_p90_dl`
5. `thermal_positive_p99_dl`
6. `thermal_max_dl`
7. `thermal_active_pixels_frame_mean`
8. `thermal_active_pixels_frame_max`
9. `thermal_frame_sum_mean_dl`
10. `thermal_frame_sum_max_dl`

All features use raw 12-bit digital levels and preserve NIST's source zeroing/threshold semantics; primary E03 does not apply temperature conversion. / 모든 feature는 raw 12-bit digital level 기반이며 NIST source threshold 의미를 보존하고 temperature 변환은 사용하지 않았다.

Outcome-blind Run `32537282914` successfully extracted finite values for all 10 features on all 21 tracks before outcome use. / outcome 사용 전 21개 track의 10개 feature 추출 성공.

## 4. Frozen Metric & Gate / 고정 지표·게이트

Primary metrics are pooled RMSE over all `21` out-of-fold predictions separately for mean depth and mean width. / 21개 OOF 예측 전체의 pooled RMSE.

Combined-vs-process improvement:
`100 × (RMSE_PROCESS_ONLY − RMSE_PROCESS_PLUS_THERMO) / RMSE_PROCESS_ONLY`.

Frozen precedence:
1. `HOLD` on unreproducible transport/decoding/target/execution;
2. `VALIDATED_MATERIAL_GAIN` if best improvement ≥10% and the other target degrades no more than 10%;
3. `MIXED` for material gain paired with >10% degradation or positive-but-<10% best gain;
4. `NO_MATERIAL_GAIN` otherwise.

## 5. Final Empirical Result / 최종 실증 결과

Run `32537495534` completed every frozen integrity and evaluation step successfully. It reconstructed `42` optical cross-section rows into exactly `21` track targets and independently verified power, scan speed, and beam/spot parameters across both NIST sources. / 42개 optical 단면을 21개 track target으로 정확히 구성했고 두 NIST source 간 공정조건도 독립 일치검증했다.

### Depth / 깊이

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **19.6406** | **16.1885** |
| `PROCESS_PLUS_THERMO` | 23.4295 | 18.4237 |
| `THERMO_ONLY` | 31.8638 | 22.5367 |

Combined-vs-process improvement: **`-19.2914%`**.

### Width / 폭

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **14.1639** | **11.6618** |
| `PROCESS_PLUS_THERMO` | 17.1620 | 12.7315 |
| `THERMO_ONLY` | 20.4189 | 14.1125 |

Combined-vs-process improvement: **`-21.1668%`**.

### Frozen gate / 고정 판정

**`NO_MATERIAL_GAIN`**

**KO:** 사전고정된 10개 raw thermography summary는 본 21-track LOCO 조건에서 process-only baseline에 추가적인 일반화 예측가치를 입증하지 못했다. 두 geometry target 모두 combined model의 pooled RMSE가 약 19–21% 악화했다.  
**EN:** The preregistered ten raw thermography summaries did not demonstrate incremental generalization value beyond the process-only baseline under the 21-track LOCO design; pooled RMSE degraded by about 19–21% for both geometry targets.

## 6. Heterogeneity / 이질성

Some held-out process cases improved while others degraded sharply. Examples: combined depth RMSE improved for cases `3.1` and `3.2`, and width improved for `2.1` and `2.2`; case `1.2` degraded strongly for both targets. / 일부 holdout case에서는 개선됐지만 다른 case에서 큰 악화가 발생했다.

This does **not** override the pooled gate and is not evidence of a validated subgroup effect. It only motivates separate, independently preregistered hypotheses if pursued. / 이는 pooled gate를 뒤집지 않으며 검증된 subgroup 효과도 아니다.

## 7. Interpretation Boundary / 해석 경계

Supported: / 지지됨
- exact raw cross-modality AM Bench experiments are reproducible at track level;
- the specific frozen ten-feature raw-DL representation has no validated material incremental value under cross-process-case generalization;
- the negative result is a valid calibration output of the engine.

Not supported: / 지지되지 않음
- thermography is useless in general;
- calibrated-temperature, spatial morphology, temporal dynamics, scan-path-aware features, or larger datasets cannot improve prediction;
- increasing model capacity would solve the observed generalization problem.

Any such follow-up requires a new hypothesis and preregistration, not modification of E03. / 후속은 E03 수정이 아니라 새 가설·사전등록이 필요하다.

## 8. Result Record / 결과 기록

Full metrics, fold heterogeneity, integrity details, and interpretation boundary are recorded in `research/AMBENCH-E03/RESULT.md`. Run 4 artifact: `9465900222`, SHA-256 `9a7df463fb0ca774c7caf097bcea2b0bcb600c1644d62ba8da7faf1556a9e2ce`.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and the snapshot-lineage gate. / 공식 산출물은 관련 규약을 따른다.
