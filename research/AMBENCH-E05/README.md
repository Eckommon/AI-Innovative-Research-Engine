---
id: AMBENCH-E05
type: experiment
state: COMPLETED_MIXED
evidence_class: VALIDATED_MIXED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E03/RESULT.md
  - research/AMBENCH-F04/RESULT.md
  - research/AMBENCH-E05/RESULT.md
---

# AMBENCH-E05 — Current Corrected-Calibration Thermal-Dynamics Incremental-Value Experiment / 현행 corrected-calibration 열동역학 추가가치 실험

**Issue / 이슈:** #17  
**State / 상태:** `COMPLETED — MIXED`  
**Evidence Run / 증거 Run:** `32540607059` — `success`  
**Parent feasibility / 상위 feasibility:** `AMBENCH-F04 — PARTIAL`

## 1. Final Result / 최종 결과

**KO:** current v1.3.1 corrected calibration과 사전고정 4개 물리 온도경계에서 만든 8개 thermal occupancy-dynamics feature는 process-only 대비 **width RMSE를 13.2004% 개선**했지만 **depth RMSE를 61.4134% 악화**했다. 고정 게이트에 따라 `MIXED`다.  
**EN:** Eight preregistered thermal occupancy-dynamics features derived from the current v1.3.1 corrected calibration improved **width RMSE by 13.2004%** versus process-only but worsened **depth RMSE by 61.4134%**. Under the frozen gate, the result is `MIXED`.

Detailed result / 상세 결과: `research/AMBENCH-E05/RESULT.md`.

## 2. Frozen Design / 고정 설계

Canonical sample / 표본:
- `21` physical tracks = 7 process cases × 3 repeats
- two optical cross-sections per track remain nested and are averaged to one depth/width target.

Validation / 검증:
- seven-fold leave-one-process-case-out (LOCO)
- each fold `18 train / 3 held-out tracks`
- no random row split.

Estimator / 추정기:
- `StandardScaler(training fold only) + Ridge(alpha=1.0, fit_intercept=True)`
- `PROCESS_ONLY`: laser power + scan speed + spot size
- `CAL_THERMAL_ONLY`: 8 frozen thermal features
- `PROCESS_PLUS_CAL_THERMAL`: 3 process + 8 thermal
- no hyperparameter search or post-hoc capacity escalation.

## 3. Pre-Execution Calibration Amendment / 실행 전 calibration 정정

Before any E05 outcome was computed or inspected, the preregistration was amended to prioritize the **exact frozen HDF5** `Coeff_c=43,920,000` over a rounded later-publication value. / outcome 확인 전 exact HDF5 coefficient 우선으로 정정.

Frozen calibration / 고정식:
`T(S,ε) = 14388 / [0.9655·ln(0.5·43,920,000/S + 1)] − 197.2/0.9655`

Frozen integer DL thresholds / 고정 threshold:
- `1150 °C → 366 DL`
- `1260 °C → 836 DL`
- `1298 °C → 1081 DL`
- `1336 °C → 1380 DL`

Feature definitions, model, split, metrics and the 10% gate were not changed by the amendment. / feature·모델·split·metric·gate 변경 없음.

## 4. Frozen Eight Features / 고정 8개 feature

For each `θ ∈ {1150,1260,1298,1336 °C}`: / 각 온도경계

- `hot_pixel_time_integral_θ_px_s = Σ_t count(pixels≥θ) / 30000`
- `any_hot_duration_θ_s = count_t[any pixel≥θ] / 30000`

Explicit exclusions / 제외:
- no historical per-repeat emissivity reconstruction;
- no exact historical TTAM/TSCR/TLCR reproduction claim;
- no manually selected pixels or smoothing;
- no morphology, CNN, transformer, learned embedding, target-aware feature selection, or `1400 °C` threshold.

E05 is a **new current-calibration hypothesis**, not an exact reproduction of the original 2022 single-track challenge pipeline. / 역사적 exact 재현 아님.

## 5. Pooled LOCO Result / pooled LOCO 결과

| Target | Process-only RMSE | Cal-thermal only RMSE | Combined RMSE | Combined improvement |
|---|---:|---:|---:|---:|
| mean depth | **19.640602 µm** | 83.535220 µm | 31.702560 µm | **-61.413380%** |
| mean width | **14.163938 µm** | 19.715121 µm | **12.294246 µm** | **+13.200372%** |

MAE / MAE:
- depth: process `16.188459`, combined `22.036992` µm
- width: process `11.661809`, combined `8.664866` µm

The process-only baselines numerically reproduce E03, confirming identical target/split/baseline construction. / E03 process baseline 수치 재현으로 target·split 동일성 확인.

## 6. Frozen Gate / 고정 게이트

The gate was fixed before execution: / 실행 전 고정
- `VALIDATED_MATERIAL_GAIN` if one target improves ≥10% and the other does not degrade >10%;
- `MIXED` if one target improves ≥10% while the other degrades >10%, or if the best gain is positive but <10%;
- `NO_MATERIAL_GAIN` otherwise;
- `HOLD` for integrity failures.

Observed / 관측:
- width `+13.200372%`
- depth `-61.413380%`

**Final / 최종: `MIXED`.**

## 7. Interpretation Boundary / 해석 경계

Supported / 지지:
- physical temperature-domain representation materially changed the result relative to E03 raw-DL summaries;
- current occupancy features contain a material incremental signal for width under the frozen experiment;
- the same representation is not robust across targets and strongly destabilizes depth generalization.

Not supported / 비지지:
- thermography is generally predictive of melt-pool geometry;
- current features should replace process variables;
- case-specific fold gains are validated subgroup laws;
- higher-capacity models would solve the depth failure.

## 8. Cost Governance / 비용 거버넌스

`COST-001` was satisfied: / 무비용 규약 준수
- public repository;
- standard `ubuntu-latest` runner;
- public/free NIST and package inputs;
- no larger/GPU runner;
- no `actions/upload-artifact` and no persisted large raw data.

Any future potentially billable route still requires explicit user approval before execution. / 향후 비용가능 경로는 사전승인 필수.

## 9. Disposition / 처리

Close E05 as `COMPLETED — MIXED`. Do not tune E05 post hoc. / E05 사후 tuning 금지.

Any next AM Bench experiment must be separately preregistered and should prioritize explaining or falsifying the **width-benefit / depth-failure asymmetry**, or expand independent process-condition evidence, rather than automatically increasing model capacity. / 후속은 width 개선·depth 실패 비대칭의 원인구분 또는 독립표본 확장을 우선.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and snapshot-lineage controls. / 관련 규약 준수.
