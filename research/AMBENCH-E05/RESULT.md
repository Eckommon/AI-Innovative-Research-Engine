# AMBENCH-E05 Result / 현행 corrected-calibration 열동역학 실험 결과

**Issue / 이슈:** #17  
**Evidence Run / 증거 Run:** `32540607059`  
**Run conclusion / 실행 결론:** `success`  
**Frozen gate / 고정 게이트:** **`MIXED`**  
**Cost / 비용:** `COST-001` compliant — public repository, standard `ubuntu-latest`, no larger/GPU runner, no large artifact upload. / 추가 금전비용 없는 경로.

## 1. Executive Result / 핵심 결과

**KO:** current v1.3.1 corrected calibration과 NIST 물리 온도경계에서 만든 8개 thermal occupancy-dynamics feature는 **melt-pool width에는 process-only 대비 13.20%의 pooled LOCO RMSE 개선**을 만들었지만, **depth에는 61.41% 악화**를 만들었다. 사전 고정 게이트에 따라 결과는 `MIXED`다. 이는 thermography의 일반적 유효성을 입증하지 않으며, 현재 표현이 width와 관련된 추가 신호를 포착할 가능성은 보이지만 depth 일반화에는 불안정하다는 제한적 증거다.

**EN:** The eight preregistered thermal occupancy-dynamics features derived from the current v1.3.1 corrected calibration improved pooled LOCO RMSE for melt-pool **width by 13.20%** versus process-only, but worsened **depth by 61.41%**. Under the frozen gate, the result is `MIXED`. This does not validate thermography in general; it provides limited evidence that this representation may carry incremental width-related information while remaining unstable for depth generalization.

## 2. Integrity / 무결성

All workflow steps completed `success`. / 전체 단계 성공.

Frozen input verification: / 고정 입력
- thermography bytes: `549,979,044`
- thermography SHA-256 actual = expected = `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- optical XLSX bytes: `25,811`
- optical SHA-256 actual = expected = `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`
- HDF5 calibration actual: `Coeff_a=0.9655`, `Coeff_b=197.2`, `Coeff_c=43,920,000`
- exactly `21` thermal track rows
- exactly `42` optical cross-sections → `21` physical-track targets
- cross-source power / scan-speed / spot-size identities all matched
- seven LOCO folds, each `18 train / 3 held-out tracks`
- exactly `126` OOF prediction rows = 21 tracks × 2 targets × 3 models

No raw NIST data or large Actions artifact was persisted. / 대용량 raw artifact 저장 없음.

## 3. Pre-Execution Calibration Thresholds / 실행 전 고정 calibration threshold

The exact frozen v1.3.1 HDF5 coefficient was used, not the rounded later-publication coefficient. / frozen HDF5 exact coefficient 우선.

Inverse-calibration integrity check: / 역변환 검증

| Temperature | Continuous DL | Frozen integer threshold |
|---|---:|---:|
| `1150 °C` | `365.3127041` | `366` |
| `1260 °C` | `835.0059850` | `836` |
| `1298 °C` | `1080.1878588` | `1081` |
| `1336 °C` | `1379.7274683` | `1380` |

All four exactly matched the amended preregistration before outcome modeling. / outcome 모델링 전 사전등록값과 일치.

## 4. Frozen Features / 고정 feature

For each temperature threshold, E05 used exactly: / 온도별 두 feature
- `hot_pixel_time_integral_θ_px_s`
- `any_hot_duration_θ_s`

for `θ ∈ {1150,1260,1298,1336 °C}` → exactly `8` thermal features.

No smoothing, exact-pixel hand selection, historical repeat-specific emissivity reconstruction, target-aware selection, morphology, CNN, transformer, or post-hoc feature expansion was used. / 사후 feature·모델 확장 없음.

## 5. Frozen Pooled LOCO Metrics / 고정 pooled LOCO 지표

### Mean depth / 평균 깊이

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **19.640602** | **16.188459** |
| `CAL_THERMAL_ONLY` | 83.535220 | 62.128660 |
| `PROCESS_PLUS_CAL_THERMAL` | **31.702560** | 22.036992 |

Combined-vs-process RMSE improvement: **`-61.413380%`** / 악화.

### Mean width / 평균 폭

| Model | RMSE (µm) | MAE (µm) |
|---|---:|---:|
| `PROCESS_ONLY` | **14.163938** | 11.661809 |
| `CAL_THERMAL_ONLY` | 19.715121 | 14.438100 |
| `PROCESS_PLUS_CAL_THERMAL` | **12.294246** | **8.664866** |

Combined-vs-process RMSE improvement: **`+13.200372%`**.

## 6. Frozen Gate Application / 고정 게이트 적용

`I_width = +13.200372% >= 10%`  
`I_depth = -61.413380% < -10%`

Frozen rule: if one target gains ≥10% while the other degrades >10%, classify `MIXED`. / 한 target 실질개선 + 다른 target 10% 초과 악화 시 MIXED.

**Final gate: `MIXED`.**

No post-hoc threshold, feature, model, split, or gate modification is permitted inside E05. / E05 내부 사후수정 금지.

## 7. Internal Replication Check / 내부 재현성 검사

The E05 `PROCESS_ONLY` baselines reproduce E03's process-only pooled metrics to numerical precision: / E03 baseline과 수치상 동일

- depth RMSE: `19.6406021163718`
- width RMSE: `14.163937981769088`

This independently confirms that E05 reused the same 21-track targets, process-case LOCO split logic, and low-capacity process baseline while changing only the preregistered thermal representation. / target·split·baseline 동일성 확인.

## 8. Fold Heterogeneity / fold 이질성

The pooled result masks substantial held-out-case heterogeneity. / case별 차이 큼.

### Depth combined vs process / depth
- improved on held-out cases `0`, `2.2`, `3.1`, `3.2`;
- degraded on `1.1`, `1.2`, `2.1`;
- especially large degradation occurred on `1.1` and `1.2`.

### Width combined vs process / width
- improved on `0`, `1.1`, `2.1`, `2.2`, `3.2`;
- degraded on `1.2`, `3.1`;
- very large width gains appeared for `2.1` and `2.2`.

These case patterns are descriptive only. They are **not promoted as validated subgroup effects** because `n=3` tracks per held-out process case and the subgroup patterns were observed after execution. / subgroup 효과로 승격 금지.

## 9. Interpretation Boundary / 해석 경계

Supported / 지지되는 해석:
- physically calibrated hot-area/time representation materially changes the information content relative to E03's generic raw-DL summaries;
- it passes the predefined material-gain threshold for **width only**;
- the same representation is not robust across both geometry targets and strongly harms depth generalization;
- thermal-only models are worse than process-only for both pooled targets, so the result does not support replacing process variables with thermography.

Not supported / 지지되지 않는 해석:
- `thermography generally predicts melt-pool geometry`;
- `thermal features are universally useful`;
- the apparent case-specific gains are established subgroup laws;
- current E05 features reproduce historical 2022 TTAM/TSCR/TLCR;
- higher-capacity modeling would necessarily solve the depth failure.

## 10. Research-Engine Implication / 연구엔진 의미

E03 and E05 together demonstrate why **representation must be treated as a falsifiable research object**, not as an implementation detail. / representation 자체를 검증대상으로 봐야 함.

- E03 raw-DL summaries: depth `-19.29%`, width `-21.17%` → `NO_MATERIAL_GAIN`.
- E05 current-calibrated occupancy dynamics: depth `-61.41%`, width `+13.20%` → `MIXED`.

The physical representation unlocked a material width signal but introduced severe target-specific instability. / 물리표현이 width 신호를 열었지만 depth 불안정성 확대.

## 11. Disposition / 처리

**Close E05 as `COMPLETED — MIXED`.**

Do not tune E05. / E05 사후 tuning 금지.

A next AM Bench hypothesis, if selected, must be separately preregistered and should prioritize **why width benefits while depth fails**, rather than simply increasing model capacity. Candidate directions may include representation diagnostics, independent sample expansion, or a different physical data relationship; no candidate is automatically promoted by this result. / 후속은 별도 사전등록 및 원인구분 우선.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and snapshot-lineage controls. / 관련 규약 준수.
