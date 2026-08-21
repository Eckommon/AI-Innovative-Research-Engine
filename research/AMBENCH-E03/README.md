---
id: AMBENCH-E03
type: experiment
state: PREREGISTERED
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
**State / 상태:** `PREREGISTERED`  
**Parent feasibility / 상위 feasibility:** `AMBENCH-F02 — PASS`

## 1. Research Question / 연구 질문

**KO:** exact 21-track 수준에서 thermography 정보가 laser power·scan speed·spot size만 사용하는 process baseline보다 melt-pool depth/width 예측력을 실질적으로 향상시키는가?  
**EN:** At the exact 21-track level, does thermography provide material predictive value for melt-pool depth/width beyond a process-only baseline using laser power, scan speed, and spot size?

## 2. Frozen Sources & Alignment / 고정 소스·정렬

- NIST thermography `mds2-2716`
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
- cross-section depth spread
- cross-section width spread

No duplication of a thermography signal into two independent supervised samples. / 하나의 thermography signal을 두 독립 supervised sample로 복제하지 않는다.

## 4. Frozen Validation / 고정 검증

Seven-fold **leave-one-process-case-out (LOCO)** using cases:
`0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2`.

Each fold holds out all three repeats belonging to one process case. / 각 fold에서 하나의 process case에 속한 3개 반복을 모두 holdout한다.

## 5. Frozen Model Families / 고정 모델군

1. `PROCESS_ONLY`: low-capacity regression on laser power + scan speed + spot size.
2. `THERMO_ONLY`: the same low-capacity regression family on preregistered compact thermography features.
3. `PROCESS_PLUS_THERMO`: process parameters + identical thermography features.

No CNN, transformer, deep video model, or capacity escalation is allowed in E03. / E03에서는 CNN·Transformer·deep video model 및 결과 기반 용량확대를 금지한다.

## 6. Thermography Feature Freeze Rule / 열화상 feature 고정 규칙

Before outcome fitting, derive a compact interpretable feature manifest from each track's raw `Signal` using only the thermography source and physics-neutral summary operations. Candidate feature classes may include distributional intensity summaries, temporal duration/frame-count descriptors, peak/quantile statistics, and simple spatial extent/centroid descriptors **only where raw HDF5 axes/units make the operation unambiguous**. / outcome fitting 전에 thermography source만으로 해석가능한 소규모 feature manifest를 고정하며, HDF5 축·단위가 명확한 경우에만 분포·시간·peak/quantile·단순 공간범위 등의 기술량을 허용한다.

Any feature requiring an undocumented temperature conversion, calibration interpretation, or arbitrary threshold is `HOLD` unless the exact rule is first grounded in NIST metadata. / 문서화되지 않은 온도변환·calibration 해석·임의 threshold가 필요한 feature는 NIST 근거가 먼저 확보되지 않는 한 HOLD한다.

## 7. Frozen Metrics / 고정 지표

Primary: LOCO RMSE separately for `depth_mean_um` and `width_mean_um`. / depth·width별 LOCO RMSE.  
Secondary: MAE, fold residuals, sensitivity to cross-section spread. / MAE·fold residual·단면 spread 민감도.

## 8. Frozen Gate / 고정 게이트

Compare `PROCESS_PLUS_THERMO` with `PROCESS_ONLY`:

- `VALIDATED_MATERIAL_GAIN`: ≥10% RMSE reduction on at least one target and no >10% RMSE degradation on the other.
- `MIXED`: ≥10% gain on one target but >10% degradation on the other, or smaller positive gains that do not reach the material threshold.
- `NO_MATERIAL_GAIN`: neither target improves by ≥10%.
- `HOLD`: exact raw transport/decoding, feature extraction, or target construction requires unsupported assumptions.

The 10% threshold is inherited from `AMBENCH-001` and frozen before E03 outcome inspection. / 10% 기준은 `AMBENCH-001`에서 계승하며 E03 결과 확인 전에 고정한다.

## 9. Leakage Controls / 누출 통제

- case-level split only; random row/track split prohibited
- fold-local preprocessing/scaling only
- no optical outcomes in thermography feature construction
- no held-out outcomes for feature selection
- failed/missing tracks explicitly recorded; no silent deletion
- track-level sample count remains 21; optical cross-sections do not inflate `n`

## 10. Execution Order / 실행 순서

1. download thermography HDF5 and verify official SHA-256;
2. enumerate exact 21 line groups and metadata;
3. rebuild the 21-track optical target table from checksum-verified XLSX;
4. freeze the compact thermography feature manifest;
5. implement deterministic extraction and integrity checks;
6. run the three model families under identical LOCO folds;
7. apply the frozen gate without post-hoc model/feature expansion;
8. record negative as well as positive results.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and the snapshot-lineage gate. / 관련 규약 준수.
