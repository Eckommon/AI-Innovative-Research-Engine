---
id: AMBENCH-E03
type: experiment
state: PREREGISTERED_FEATURES_FROZEN
evidence_class: HYPOTHESIZED
region: us
domain: manufacturing
tags:
  - type/experiment
  - state/candidate
  - evidence/hypothesized
  - region/us
  - domain/manufacturing
  - domain/additive-manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-001/README.md
  - research/AMBENCH-F02/README.md
---

# AMBENCH-E03 — Track-level Thermography → Melt-Pool Geometry Controlled Experiment / Track-level 열화상→용융풀 형상 통제실험

**Issue / 이슈:** #13  
**State / 상태:** `PREREGISTERED — THERMAL FEATURES + EVALUATION RULES FROZEN BEFORE OUTCOMES`  
**Parent feasibility / 상위 feasibility:** `AMBENCH-F02 — PASS`

## 1. Research Question / 연구 질문

**KO:** exact 21-track 수준에서 thermography 정보가 laser power·scan speed·spot size만 사용하는 process baseline보다 melt-pool depth/width 예측력을 실질적으로 향상시키는가?  
**EN:** At the exact 21-track level, does thermography provide material predictive value for melt-pool depth/width beyond a process-only baseline using laser power, scan speed, and spot size?

## 2. Frozen Sources & Alignment / 고정 소스·정렬

- NIST thermography `mds2-2716`, exact PDR v1.3.1 distribution
- NIST optical microscopy `mds2-2718`
- exact `case + repeat/track` alignment validated by `AMBENCH-F02`
- thermography HDF5 official checksum: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- optical measurement XLSX SHA-256: `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`

One canonical observation is one physical single track. The two optical cross-sections for that track remain nested measurements. / 표준 관측단위는 물리 single track 1개이며 track당 두 optical 단면은 nested 측정으로 유지한다.

## 3. Frozen Target Construction / 고정 target 구성

Primary target per track: / track별 주 target
- `depth_mean_um` = mean of the two optical cross-section depth measurements
- `width_mean_um` = mean of the two optical cross-section width measurements

Secondary uncertainty descriptors: / 보조 불확실성 기술량
- `depth_spread_um` = absolute difference between the two depth measurements
- `width_spread_um` = absolute difference between the two width measurements

No duplication of a thermography signal into two independent supervised samples. / 하나의 thermography signal을 두 독립 supervised sample로 복제하지 않는다.

## 4. Frozen Validation / 고정 검증

Seven-fold **leave-one-process-case-out (LOCO)** using cases:
`0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2`.

Each fold holds out all three repeats belonging to one process case. / 각 fold에서 하나의 process case에 속한 3개 반복을 모두 holdout한다.

## 5. Frozen Model Family / 고정 모델군

All three comparisons use the same deterministic low-capacity estimator: / 세 비교 모두 동일 저용량 추정기 사용.

**`Ridge(alpha=1.0, fit_intercept=True)` after fold-local standardization.**

- `PROCESS_ONLY`: `laser_power_W`, `scan_speed_mm_s`, `spot_size_um`
- `THERMO_ONLY`: the ten frozen raw-signal summary features in §7
- `PROCESS_PLUS_THERMO`: the three process fields + the same ten thermal features

Standardization mean/variance is fitted on the training tracks inside each LOCO fold only. / 표준화 평균·분산은 각 LOCO fold의 training track에서만 적합한다.

No hyperparameter search, CNN, transformer, deep video model, feature expansion, or capacity escalation is allowed in E03. / E03에서는 hyperparameter 탐색·CNN·Transformer·deep video model·feature 추가·결과 기반 용량확대를 금지한다.

## 6. Outcome-Blind Raw Structure Evidence / Outcome 비사용 raw 구조 근거

GitHub Actions Runs `32537038475` and `32537157650` inspected only thermography source structure before any optical target use. / optical target 사용 전에 thermography 구조만 검사했다.

Observed / 관측:
- downloaded bytes: `549,979,044`
- actual SHA-256 = frozen official SHA-256: exact match
- exactly `21` `Line_*` groups
- each `Signal`: shape `[700, 640, 304]`, dtype `uint16`, gzip, chunks `[25,25,25]`
- `Signal.n_frames = 700`
- `Signal.units = digital levels`
- `Signal.bit_depth = 12`
- NIST source threshold: `threshold_level = 100`, `threshold_zeros = true`
- camera frame rate: `30,000 frames/s`
- group attributes directly preserve laser power, scan speed, and D4σ spot size
- NIST calibration metadata exists, but the primary E03 feature set does **not** convert digital levels to temperature.

This evidence makes the first axis authoritative as frame/time index through `n_frames=700`; the two remaining dimensions are treated only as image-grid pixel axes, without inventing a physical pixel-size conversion. / `n_frames=700` 근거로 첫 축은 frame/time index로 확정하며 나머지 두 축은 물리 pixel 크기를 추정하지 않고 영상 격자 축으로만 취급한다.

## 7. Frozen Thermography Feature Manifest / 고정 열화상 feature 명세

The following **10 features are frozen before optical outcome construction/fitting** and are computed from each raw 12-bit `Signal` in digital levels. The source's already-applied zeroing/threshold semantics are preserved; no new arbitrary intensity threshold is introduced. / 다음 10개 feature를 optical outcome 구성·fitting 전에 고정하며 별도 임의 threshold를 추가하지 않는다.

| Feature | Definition / 정의 |
|---|---|
| `thermal_nonzero_fraction` | fraction of all voxels/pixels across 700 frames with raw value `>0` |
| `thermal_positive_mean_dl` | mean digital level over values `>0` |
| `thermal_positive_std_dl` | population standard deviation of digital levels over values `>0` |
| `thermal_positive_p90_dl` | 90th percentile among values `>0`, derived from exact 12-bit histogram |
| `thermal_positive_p99_dl` | 99th percentile among values `>0`, derived from exact 12-bit histogram |
| `thermal_max_dl` | maximum raw digital level |
| `thermal_active_pixels_frame_mean` | mean count of `>0` pixels per frame |
| `thermal_active_pixels_frame_max` | maximum count of `>0` pixels in any frame |
| `thermal_frame_sum_mean_dl` | mean per-frame sum of raw digital levels |
| `thermal_frame_sum_max_dl` | maximum per-frame sum of raw digital levels |

Extraction is deterministic and may stream frame batches; streaming must reproduce the same statistics as full-array evaluation. / 추출은 결정론적이며 frame batch streaming을 허용하되 full-array 계산과 동일 통계를 산출해야 한다.

### Explicit exclusions / 명시적 제외
- no temperature-converted features in primary E03;
- no centroid/shape/connected-component features because physical spatial-axis calibration is not yet required or frozen;
- no manually chosen additional threshold above the source's native zeroing;
- no feature selection based on depth/width correlations.

Run `32537282914` successfully produced all 10 frozen finite features for all 21 tracks before optical outcomes were used. / Run `32537282914`에서 optical outcome 사용 전에 21개 track 모두 10개 frozen finite feature 추출에 성공했다.

## 8. Frozen Metrics / 고정 지표

Primary: / 주 지표
- `LOCO_RMSE_depth` = **pooled RMSE over all 21 out-of-fold depth predictions**, not an unweighted average of seven fold RMSEs.
- `LOCO_RMSE_width` = **pooled RMSE over all 21 out-of-fold width predictions**.

Secondary: / 보조
- pooled MAE over the same 21 out-of-fold predictions;
- fold/case-level residual summaries;
- optical cross-section spread retained as an uncertainty descriptor, not a sample weight unless separately preregistered.

For each target, Combined-vs-Process improvement is: / 개선율

`100 × (RMSE_PROCESS_ONLY − RMSE_PROCESS_PLUS_THERMO) / RMSE_PROCESS_ONLY`.

## 9. Frozen Gate / 고정 게이트

Let `I_depth` and `I_width` be the two percentage RMSE improvements above, `I_max=max(...)`, `I_min=min(...)`. Gate precedence is evaluated in this exact order: / 아래 순서로 판정한다.

1. `HOLD` if exact transport/decoding, frozen feature extraction, exact target construction, or LOCO execution cannot be reproduced without unsupported assumptions.
2. `VALIDATED_MATERIAL_GAIN` if `I_max >= 10` **and** `I_min >= -10`.
3. `MIXED` if (`I_max >= 10` and `I_min < -10`) **or** (`0 < I_max < 10`).
4. `NO_MATERIAL_GAIN` otherwise.

This precedence is a deterministic disambiguation of the already-frozen 10% material threshold; it does not change the threshold after seeing outcomes. / 이 우선순위는 기존 10% 기준의 결정론적 명확화이며 outcome 확인 후 threshold를 변경한 것이 아니다.

## 10. Leakage Controls / 누출 통제

- case-level split only; random row/track split prohibited
- fold-local preprocessing/scaling only
- no optical outcomes in thermography feature construction
- no held-out outcomes for feature selection or tuning
- failed/missing tracks explicitly recorded; no silent deletion
- track-level sample count remains 21; optical cross-sections do not inflate `n`
- all three model families use identical LOCO folds and target rows

## 11. Execution Order / 실행 순서

1. ✅ download thermography HDF5 and verify official SHA-256;
2. ✅ enumerate exact 21 line groups and metadata;
3. ✅ inspect Signal attrs/calibration metadata without optical outcomes;
4. ✅ freeze compact thermography feature manifest and estimator;
5. ✅ extract the frozen 10 features for all 21 tracks and integrity-check them;
6. rebuild the 21-track optical target table from checksum-verified XLSX;
7. run the three frozen model families under identical LOCO folds;
8. apply the frozen gate without post-hoc model/feature expansion;
9. record negative as well as positive results.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and the snapshot-lineage gate. / 관련 규약 준수.
