---
id: AMBENCH-E05
type: experiment
state: PREREGISTERED
evidence_class: HYPOTHESIZED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E03/RESULT.md
  - research/AMBENCH-F04/RESULT.md
---

# AMBENCH-E05 — Current Corrected-Calibration Thermal-Dynamics Incremental-Value Experiment / 현행 corrected-calibration 열동역학 추가가치 실험

**State / 상태:** `PREREGISTERED — FEATURES / MODEL / SPLIT / GATE FROZEN BEFORE E05 EXECUTION`  
**Parent feasibility / 상위 feasibility:** `AMBENCH-F04 — PARTIAL`  
**Historical-boundary rule / 역사경계:** E05 is a **new current-calibration hypothesis**, not an exact reproduction of the 2022 single-track TTAM/TSCR/TLCR pipeline. / 2022 challenge exact 재현이 아닌 신규가설.

## 0. Pre-Execution Amendment / 실행 전 정정

**KO:** E05 실행 전 무결성 검토에서 NIST 후속 논문의 rounded coefficient `C=4.391×10^7`과 frozen v1.3.1 HDF5의 exact `Coeff_c=43,920,000` 사이 차이를 발견했다. **어떠한 E05 outcome도 계산·조회하기 전**, snapshot/source-of-truth 우선 원칙에 따라 E05는 exact HDF5 coefficient `C=43,920,000`을 사용하도록 정정했다. 이로 인해 preregistered integer DL thresholds는 `366 / 836 / 1081 / 1380`으로 정정된다. Feature 정의·모델·split·metric·10% gate는 변경하지 않는다.  
**EN:** Before any E05 outcome was computed or inspected, an integrity review found a difference between the rounded later-publication coefficient `C=4.391×10^7` and the frozen v1.3.1 HDF5 exact `Coeff_c=43,920,000`. Under the snapshot/source-of-truth rule, E05 was amended **pre-execution** to use the exact HDF5 coefficient. The preregistered integer DL thresholds therefore become `366 / 836 / 1081 / 1380`. Feature definitions, estimator, splits, metrics, and the 10% gate are unchanged.

## 1. Research Question / 연구 질문

**KO:** current v1.3.1 corrected thermography calibration과 NIST 물리 온도 경계를 이용한 저차원 **thermal occupancy dynamics**가 공정변수만 사용하는 기준선보다 track-level melt-pool depth/width 예측을 실질적으로 개선하는가?  
**EN:** Do low-dimensional **thermal occupancy dynamics** derived from the current v1.3.1 corrected calibration and NIST physical temperature boundaries materially improve track-level melt-pool depth/width prediction beyond process parameters alone?

## 2. Frozen Sources / 고정 소스

Thermography / 열화상:
- NIST `mds2-2716`, PDR v1.3.1
- SHA-256 `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`

Optical / 광학 target:
- NIST `mds2-2718`, measurement XLSX
- SHA-256 `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`

Identity / 식별자:
- exact 21 physical tracks validated by `AMBENCH-F02`
- two optical cross-sections remain nested measurements and are averaged to one target per physical track.

## 3. Frozen Current Calibration / 고정 현행 calibration

Use the current corrected Sakuma-Hattori relation established in F04: / F04에서 확립한 현행식

`T(S,ε) = c2 / [A·ln(ε·C/S + 1)] − B/A`

Frozen constants / 상수:
- `A = 0.9655`
- `B = 197.2`
- `C = 43,920,000` — **exact frozen v1.3.1 HDF5 `Coeff_c`**
- `c2 = 14,388 µm/K`
- `ε = 0.5` **fixed globally** as the later NIST effective/common emissivity derived from AMB2022-03.

The later NIST publication reports the same coefficient family with rounded `C=4.391×10^7`; E05 uses the exact frozen HDF5 attribute instead. / 후속 논문 rounded 값보다 frozen HDF5 exact 값을 우선한다.

This `ε=0.5` choice is intentionally not presented as the historical per-repeat emissivity used in the original 2022 single-track challenge. / 과거 repeat별 emissivity로 주장하지 않는다.

HDF5 timing / 시간:
- `30,000 frames/s` frozen for E05 from current HDF5 metadata.
- later Pad-Y `30,686 fps` is excluded because track-specific applicability remains unverified.

## 4. Frozen Physical Thresholds / 고정 물리 온도경계

Only temperatures within the NIST documented calibrated range and directly tied to the IN718 transition semantics are used: / NIST calibration 범위·상변태 의미에 직접 연결된 경계만 사용.

- `1150 °C` — lower boundary of documented solid-cooling interval
- `1260 °C` — solidus
- `1298 °C` — solidus/liquidus midpoint
- `1336 °C` — liquidus

`1400 °C` is **excluded** from E05 because the challenge document lists the calibrated camera range up to `1389 °C`. / calibration range 상단을 넘는 1400°C 제외.

For integer raw DL, compute the exact threshold through the frozen inverse calibration and use the smallest integer DL satisfying `T(S,0.5) >= T_threshold`. Expected integer thresholds are preregistered as integrity checks: / 정수 DL gate

- `1150 °C → 366 DL`
- `1260 °C → 836 DL`
- `1298 °C → 1081 DL`
- `1336 °C → 1380 DL`

No threshold is selected using optical outcomes. / optical outcome 기반 threshold 선택 금지.

## 5. Frozen 8-Feature Manifest / 고정 8개 feature

For each physical threshold `θ ∈ {1150,1260,1298,1336}` and each of the 700 frames, define: / 각 frame

`A_θ(t) = count of pixels whose current-calibrated temperature >= θ`

Equivalent implementation may compare integer DL against the frozen threshold above because the calibration is monotonic. / monotonic calibration이므로 frozen DL threshold 비교 허용.

For each θ, extract exactly two features: / 온도별 2개

1. **`hot_pixel_time_integral_θ_px_s`**  
   `Σ_t A_θ(t) / 30000`  
   Integrated hot-pixel occupancy in pixel·seconds. / 열영역×시간 적분.

2. **`any_hot_duration_θ_s`**  
   `count_t[A_θ(t) > 0] / 30000`  
   Total sampled time containing at least one pixel above θ. / 해당 온도 이상 pixel이 존재한 총 frame 시간.

Frozen thermal columns / 고정 열 feature:
- `hot_pixel_time_integral_1150_px_s`
- `any_hot_duration_1150_s`
- `hot_pixel_time_integral_1260_px_s`
- `any_hot_duration_1260_s`
- `hot_pixel_time_integral_1298_px_s`
- `any_hot_duration_1298_s`
- `hot_pixel_time_integral_1336_px_s`
- `any_hot_duration_1336_s`

### Explicit exclusions / 명시적 제외
- no historical per-repeat emissivity reconstruction;
- no exact TTAM/TSCR/TLCR reproduction claim;
- no manually selected pixel coordinates;
- no smoothing filter;
- no connected components, centroid, morphology, CNN, transformer, or learned video embedding;
- no target-aware feature selection;
- no `1400 °C` threshold.

This isolates the information question: **does physically calibrated hot-area duration/occupancy add cross-case information beyond process parameters?** / 물리 온도경계의 면적·시간정보 자체의 추가가치만 검증.

## 6. Frozen Targets / 고정 target

Same target construction as E03: / E03 동일
- `depth_mean_um` = mean of two nested optical depth cross-sections per track
- `width_mean_um` = mean of two nested optical width cross-sections per track

Canonical `n=21` physical tracks. / 표본수 21.

## 7. Frozen Validation / 고정 검증

Seven-fold leave-one-process-case-out (LOCO): / 7-fold process-case LOCO
`0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2`.

Each fold = `18 train / 3 held-out tracks`; all repeats of the held-out process case remain outside training. / case 전체 holdout.

## 8. Frozen Model Family / 고정 모델군

Identical low-capacity estimator for all comparisons: / 동일 저용량 추정기

`StandardScaler(training fold only) + Ridge(alpha=1.0, fit_intercept=True)`

Feature families:
1. `PROCESS_ONLY` — `laser_power_W`, `scan_speed_mm_s`, `spot_size_um`
2. `CAL_THERMAL_ONLY` — the eight frozen thermal-dynamics features
3. `PROCESS_PLUS_CAL_THERMAL` — 3 process + 8 calibrated thermal features

No hyperparameter search. / hyperparameter 탐색 금지.

## 9. Frozen Metrics / 고정 지표

Primary / 주 지표:
- pooled 21-track out-of-fold RMSE for `depth_mean_um`
- pooled 21-track out-of-fold RMSE for `width_mean_um`

Secondary / 보조:
- pooled MAE
- fold/case residual summaries
- comparison to the already-frozen E03 result is descriptive only and does not change the E05 gate.

For each target: / 개선율

`Improvement = 100 × (RMSE_PROCESS_ONLY − RMSE_PROCESS_PLUS_CAL_THERMAL) / RMSE_PROCESS_ONLY`

## 10. Frozen Gate / 고정 게이트

Let `I_depth`, `I_width` be the two RMSE improvements; `I_max=max`, `I_min=min`.

1. `HOLD` if source checksum, exact 21-track target construction, calibration-threshold integrity, finite feature extraction, or LOCO execution fails without unsupported assumptions.
2. `VALIDATED_MATERIAL_GAIN` if `I_max >= 10%` **and** `I_min >= -10%`.
3. `MIXED` if (`I_max >= 10%` and `I_min < -10%`) **or** (`0 < I_max < 10%`).
4. `NO_MATERIAL_GAIN` otherwise.

The same 10% material threshold is retained from E03/AMBENCH calibration; it is not chosen after E05 results. / 기존 10% 기준 유지.

## 11. Leakage & Historical-Exposure Controls / 누출·역사노출 통제

- No random row split; process-case split only.
- No optical outcomes in feature construction.
- No feature/threshold addition after E05 execution begins.
- All preprocessing fitted training-fold only.
- E03 outcomes are already known to the project; E05 therefore does **not** claim a pristine first-ever blind study. Integrity instead comes from physically preregistering the complete E05 representation and gate before new execution. / E03 결과 노출 이력은 명시하며, E05는 새 feature·gate를 실행 전에 완전히 고정해 무결성을 확보한다.
- Negative result must be retained; no capacity escalation within E05.

## 12. COST-001 / 비용 규약

Execution is authorized without a separate paid-action approval only under all of the following: / 아래 조건에서만 별도 비용승인 없이 실행
- repository remains `public`;
- runner is a **standard** GitHub-hosted runner such as `ubuntu-latest`, not a larger/GPU runner;
- GitHub's current official billing documentation continues to state standard GitHub-hosted runners are free for public repositories;
- NIST and package downloads are public/free;
- do not upload large raw data as Actions artifacts; raw files remain ephemeral;
- result evidence should be retained in workflow logs and a small GitHub research record.

If any condition changes or billing becomes uncertain, execution becomes `HOLD_COST_APPROVAL`. / 비용불명확 시 중단.

## 13. Execution Order / 실행 순서

1. create traceable standard-runner execution trigger;
2. download and checksum-verify frozen NIST inputs;
3. analytically verify frozen DL thresholds;
4. extract exactly the eight preregistered calibrated thermal-dynamics features for 21 tracks;
5. construct exact 21-track optical targets;
6. run the three frozen model families under identical LOCO folds;
7. apply frozen gate;
8. write both positive and negative results to GitHub;
9. close execution PR without merge if used only as a traceable trigger.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, and `UNKNOWN-001`. / 관련 규약 준수.
