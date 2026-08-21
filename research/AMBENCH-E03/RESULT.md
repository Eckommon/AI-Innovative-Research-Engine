---
id: AMBENCH-E03-RESULT
type: result
state: COMPLETED_NO_MATERIAL_GAIN
evidence_class: VALIDATED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E03/README.md
  - research/AMBENCH-F02/README.md
---

# AMBENCH-E03 Result — Preregistered Track-level Thermography Experiment / 사전등록 Track-level 열화상 실험 결과

**Issue / 이슈:** #13  
**Evidence Run / 증거 Run:** GitHub Actions `32537495534`  
**Artifact / 아티팩트:** `ambench-e03-run4-preregistered-results`, ID `9465900222`, artifact SHA-256 `9a7df463fb0ca774c7caf097bcea2b0bcb600c1644d62ba8da7faf1556a9e2ce`  
**Frozen gate result / 고정 게이트 결과:** **`NO_MATERIAL_GAIN`**

## 1. Integrity / 무결성

Run 4 completed all stages successfully. / Run 4 전 단계 성공.

- thermography HDF5 bytes: `549,979,044`
- thermography SHA-256: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43` — exact frozen match
- optical workbook bytes: `25,811`
- optical SHA-256: `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931` — exact frozen match
- exact optical rows: `42` cross-sections → `21` physical track targets
- exact thermal rows: `21`
- process parameters independently matched across thermography and optical sources for every selected track / 모든 선택 track에서 두 source의 power·velocity·beam/spot parameter 일치
- validation: seven-fold leave-one-process-case-out, `18 train / 3 test` per fold
- OOF predictions: `21 tracks × 2 targets × 3 models = 126`

## 2. Frozen Models / 고정 모델

All use fold-local `StandardScaler` + `Ridge(alpha=1.0, fit_intercept=True)`. / 모두 fold-local 표준화 + 동일 Ridge.

- `PROCESS_ONLY`: 3 process features
- `THERMO_ONLY`: 10 preregistered raw-digital-level thermal features
- `PROCESS_PLUS_THERMO`: 13 combined features

No tuning or post-result feature/model expansion occurred. / 결과 후 tuning·feature/model 확장 없음.

## 3. Pooled LOCO Result / Pooled LOCO 결과

### Depth / 깊이

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **19.6406** | **16.1885** |
| `PROCESS_PLUS_THERMO` | 23.4295 | 18.4237 |
| `THERMO_ONLY` | 31.8638 | 22.5367 |

Combined-vs-process RMSE improvement: **`-19.2914%`** — degradation / 악화.

### Width / 폭

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **14.1639** | **11.6618** |
| `PROCESS_PLUS_THERMO` | 17.1620 | 12.7315 |
| `THERMO_ONLY` | 20.4189 | 14.1125 |

Combined-vs-process RMSE improvement: **`-21.1668%`** — degradation / 악화.

## 4. Frozen Gate / 고정 판정

Both target improvements are negative. Therefore the preregistered gate resolves deterministically to:

**`NO_MATERIAL_GAIN`**

**KO:** 고정된 10개 raw thermography summary feature는 본 21-track·LOCO 설계에서 process-only baseline에 비해 melt-pool depth 또는 width의 일반화 RMSE를 개선하지 못했으며, 두 target 모두 오히려 약 19–21% 악화했다.  
**EN:** Under the frozen 21-track LOCO design, the ten raw thermography summary features did not improve generalization RMSE beyond the process-only baseline for either melt-pool depth or width; both targets degraded by approximately 19–21%.

## 5. Fold Heterogeneity / Fold 이질성

The pooled negative result is not uniform across process cases. / pooled 악화가 모든 case에서 동일한 것은 아니다.

Examples where combined thermal information reduced fold RMSE: / 개선 예
- case `3.1` depth: `17.8551 → 7.3010 µm`
- case `3.2` depth: `20.8858 → 10.5298 µm`
- case `2.1` width: `19.3985 → 12.1550 µm`
- case `2.2` width: `15.2181 → 10.3544 µm`

Examples of large degradation: / 큰 악화 예
- case `1.2` depth: `22.9713 → 36.8847 µm`
- case `1.2` width: `16.5546 → 33.3031 µm`
- case `1.1` depth: `35.8446 → 43.9541 µm`
- case `1.1` width: `22.1323 → 25.9585 µm`

This heterogeneity does **not** override the pooled frozen gate. It suggests only that the current compact thermal summaries may be case-dependent and are not robust enough for across-process-case generalization. / 이 이질성은 pooled 고정 게이트를 뒤집지 않으며, 현 compact thermal summary가 case-dependent할 가능성과 공정조건 외삽 일반화의 부족을 시사하는 수준으로만 해석한다.

## 6. Optical Target Scale / Optical target 규모

Across the 21 exact tracks: / 21개 exact track
- depth mean range: `101.7405–228.1830 µm`
- width mean range: `104.9490–157.4235 µm`
- depth cross-section spread range: `0.138–8.970 µm`
- width cross-section spread range: `0.345–14.490 µm`

Cross-section spreads remain descriptive uncertainty information and were not used as independent samples or outcome weights. / 단면 spread는 불확실성 기술량으로만 보존했으며 독립표본·가중치로 사용하지 않았다.

## 7. Interpretation Boundary / 해석 경계

### Supported / 지지되는 해석
- exact raw thermography → optical track-level controlled evaluation is technically reproducible;
- process-only low-capacity baseline outperformed the frozen raw-DL thermal and combined models under process-case LOCO;
- the specific ten-feature thermal representation has **no validated material incremental value** under E03.

### Not supported / 지지되지 않는 해석
- thermography is useless in general;
- calibrated temperature fields, spatial/temporal morphology, scan-path-aware features, or higher-sample datasets cannot help;
- deep learning would necessarily improve the result;
- fold-specific improvements constitute a validated subgroup effect.

Those are separate hypotheses and require separate preregistration. / 위 주장은 별도 가설·사전등록이 필요하다.

## 8. Research Value / 연구 가치

This is a useful negative calibration result for the innovation engine. / 혁신 탐색 엔진의 유용한 음성 보정 결과다.

It demonstrates the engine can:
1. recover versioned raw snapshots;
2. prove cross-modality identity alignment;
3. freeze feature/model/metric decisions before outcomes;
4. execute leakage-aware cross-condition validation;
5. reject an intuitive multimodal hypothesis when empirical performance does not support it.

No model-capacity escalation is authorized inside E03. / E03 내부에서 모델 용량 확대는 승인하지 않는다.
