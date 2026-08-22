---
id: AMBENCH-E09
type: controlled-experiment-preregistration
state: PREREGISTERED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
parent:
  - AMBENCH-F08
related:
  - research/AMBENCH-F08/RESULT.md
  - research/AMBENCH-F02/README.md
  - research/AMBENCH-E05/RESULT.md
  - research/AMBENCH-D06/RESULT.md
---

# AMBENCH-E09 — Unpaired BP4 Coupling → BP1 Thermal/Geometry Case-Family Ordering Test / 비paired BP4 coupling → BP1 열·형상 case-family 순서 검증

**State / 상태:** `PREREGISTERED — NO COUPLING OUTCOME ACCESS YET`  
**Parent gate / 상위 게이트:** `AMBENCH-F08 = PARTIAL_CASE_LEVEL_READY`  
**Execution boundary / 실행경계:** no BP4 coupling time-series values may be inspected until this preregistration is frozen in GitHub and the active Issue is created. / 본 사전등록과 Issue 고정 전 BP4 coupling 시계열 값 열람 금지.

## 1. Scientific Question / 과학적 질문

**KO:** 서로 다른 bare-plate specimen에서 측정되었고 정확한 track/repeat pairing이 불가능한 조건에서, BP4의 **dynamic laser coupling을 포함한 coupling-weighted process-energy ordering**이 BP4 process-only energy-density ordering보다 BP1의 thermal response case-family ordering을 더 잘 설명하는가? 그리고 동일한 ordering이 BP1 melt-pool width/depth에서도 보조적으로 관찰되는가?

**EN:** With BP1 and BP4 measured on separate bare-plate specimens and with no valid track/repeat pairing, does a BP4 **coupling-weighted process-energy ordering** explain BP1 thermal-response case-family ordering better than BP4 process-only energy-density ordering? Secondarily, is the same ordering observed for BP1 melt-pool width and depth?

This is a **cross-specimen, unpaired, case-family ordering test**, not a paired-sensor, predictive-generalization, or causal experiment. / 이는 cross-specimen 비paired case-family ordering 검증이며 paired sensor·일반화 예측·인과 실험이 아니다.

## 2. Why This Question / 질문 선택 근거

- `AMBENCH-D06` found the existing BP1 thermal representation to be `PROCESS_CASE_PROXY_DOMINANT`; therefore a useful next relationship must test whether a genuinely different physical modality adds information beyond process-case ordering. / 기존 thermal feature가 process proxy 지배이므로 새 modality의 추가정보를 직접 검증해야 한다.
- `AMBENCH-F08` established that BP4 dynamic coupling is physically distinct from thermography, but BP1 and BP4 are different plates and matching case labels do not imply identical processing conditions. / distinct modality이나 paired identity는 없음.
- NIST AMB2022-03 documentation states that the dynamic-coupling measurements use the same power/speed perturbation pattern as the thermography single tracks **except for a different laser diameter**, while the actual thermography and coupling parameter tables explicitly preserve the seven nominal case families. / power·speed perturbation 구조는 공통이나 spot diameter는 다름.

The experiment therefore tests **ordering transfer across homologous perturbation families**, not equality of absolute measurements. / 절대값 동일성이 아니라 homologous perturbation family의 ordering transfer를 검증한다.

## 3. Outcome-Blindness Declaration / outcome 비사용 선언

### What is blind / 비사용 범위

- BP4 `mds2-3842` coupling time-series values have **not** been downloaded or inspected in F08/E09 before this preregistration. / BP4 coupling 값 미열람.
- No coupling feature, threshold, window, statistic, or gate below was selected after seeing BP4 coupling outcomes. / coupling outcome 기반 사후선택 없음.

### What is not blind / 이미 알려진 범위

BP1 thermography/geometry outcomes were used in earlier project experiments (`E03`, `E05`, `D06`) and therefore cannot honestly be described as unseen. / BP1 결과는 과거 실험에서 이미 관측됨.

**Integrity classification / 무결성 분류:**  
`NEW_MODALITY_OUTCOME_BLIND = YES`  
`FULL_OUTCOME_BLIND = NO — BP1_PREOBSERVED`

Bias control / 편향 통제:
1. the **primary BP1 thermal endpoint** is fixed at the NIST-defined melt-midpoint threshold `1298 °C`, not selected from prior case-level performance;
2. both geometry targets, **width and depth**, are retained symmetrically as secondary endpoints; width is not selected alone despite E05's prior width gain;
3. no previously observed BP1 case-by-case subgroup pattern may be used to change the E09 feature set, thresholds, ordering metric, or gate.

## 4. Frozen Sources / 고정 소스

| Role | Source | Frozen use |
|---|---|---|
| BP1 thermography | NIST PDR `mds2-2716`, current validated project snapshot v1.3.1 | existing deterministic E05 feature extraction only |
| BP1 geometry | NIST PDR `mds2-2718`, checksum-verified optical workbook | track-level mean width/depth, nested cross-sections respected |
| BP4 coupling | NIST PDR `mds2-3842`, current v1.0.3 | coupling time-series after preregistration only |
| experiment design | NIST `AMB2022-03 Benchmark Measurements and Challenge Problems`, v1.01 | parameter vectors, plate identity, case-family semantics |

No surface-roughness harmonization is permitted because F08 records the unresolved `Ra = 0.15 µm` vs `5.8 µm` source conflict. / roughness는 공통 covariate에서 제외.

## 5. Frozen Case-Family Correspondence / 고정 case-family 대응

The unit of cross-BP comparison is **nominal case family**, never repeat identity. / cross-BP 비교단위는 case family이며 repeat가 아니다.

| Case | Perturbation | BP1 P [W] | BP1 v [mm/s] | BP1 D4σ [µm] | BP1 VED/VED0 | BP4 P [W] | BP4 v [mm/s] | BP4 D4σ [µm] | BP4 VED/VED0 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `0` | baseline | 285 | 960 | 67 | 1.00 | 285 | 960 | 110 | 1.00 |
| `1.1` | smaller spot | 285 | 960 | 49 | 1.87 | 285 | 960 | 76 | 2.09 |
| `1.2` | larger spot | 285 | 960 | 82 | 0.67 | 285 | 960 | 131 | 0.71 |
| `2.1` | faster scan | 285 | 1200 | 67 | 0.80 | 285 | 1200 | 110 | 0.80 |
| `2.2` | slower scan | 285 | 800 | 67 | 1.20 | 285 | 800 | 110 | 1.20 |
| `3.1` | higher power | 325 | 960 | 67 | 1.14 | 325 | 960 | 110 | 1.14 |
| `3.2` | lower power | 245 | 960 | 67 | 0.86 | 245 | 960 | 110 | 0.86 |

`VED/VED0` is taken from the authoritative NIST tables and is used as the process-only case-order comparator. / process-only 비교순서는 NIST 공식 VED ratio 사용.

## 6. BP4 Coupling Feature — Frozen Before Access / BP4 coupling feature 사전고정

For each authoritatively identifiable BP4 track file: / 각 BP4 track

1. require monotonically non-decreasing finite time values and finite coupling samples after invalid-value removal; / time·coupling finite 검사;
2. define normalized record time `τ = (t - t_min) / (t_max - t_min)`;
3. define the primary track coupling descriptor:
   - `C_track = median(P_lc(t))` for `0.20 <= τ <= 0.80`;
4. no smoothing, manual crop, peak selection, or target-aware filtering; / smoothing·수동선택 금지;
5. case aggregation:
   - `C_case = median(C_track)` over **unique, authoritatively identifiable** files for that case.

Sensitivity descriptor, frozen now / 민감도 분석:
- `C_full_track = median(P_lc(t))` over all finite samples.
- It may be reported only as a sensitivity analysis and cannot replace the primary descriptor post hoc.

### Case `3.2` identity preflight / `3.2` 식별자 preflight

Before reading numeric coupling values after download, inspect archive filenames only. / 값 읽기 전 filename inventory 우선.

- If three distinct case-`3.2` files are directly present and deterministically identify three repeats, mark `3.2_ID_RESOLVED_BY_ARCHIVE` and use all three.
- If only two unique identifiable files exist or the third identity remains ambiguous, do **not** infer `3_2_3sv.txt`; aggregate only verified unique files and mark `3.2_PARTIAL_REPEAT_ID`.
- Mandatory sensitivity: repeat all case-level statistics excluding case `3.2` whenever `3.2_PARTIAL_REPEAT_ID` applies.
- If fewer than 6 total nominal case families remain analyzable, outcome = `HOLD_DATA_INTEGRITY` before scientific interpretation.

Cross-BP repeat `1/2/3` pairing remains prohibited even if BP4's internal third-repeat identity is resolved. / BP4 내부 repeat 해결과 cross-BP pairing은 별개.

## 7. Frozen Predictors / 고정 predictor

### Process-only comparator / process-only 비교군

`X_process(case) = BP4 VEDσ(case) / BP4 VEDσ(case 0)`

Use the official NIST ratios listed above; do not recompute a substitute if the authoritative table is available. / 공식 NIST ratio 우선.

### Coupling-informed predictor / coupling 정보 predictor

`X_coupled(case) = X_process(case) * [C_case / C_case0]`

Interpretation / 해석:
- dimensionless **coupling-weighted VED-order proxy**;
- not labeled exact absorbed energy density;
- the NIST README caveat that laser coupling approximates absorption remains mandatory.

The experiment asks whether adding the measured coupling ratio changes the case ordering in a way that better corresponds to BP1 response ordering. / coupling 추가가 BP1 response ordering 설명력을 높이는지 검증.

## 8. Frozen BP1 Endpoints / 고정 BP1 endpoint

### Primary thermal endpoint / 1차 thermal

`Y_thermal(case)` = median across the three BP1 tracks of the already-defined E05 feature:

`hot_pixel_time_integral_1298C_px_s`

Reason fixed before BP4 outcome access / 선택근거:
- `1298 °C` is the NIST AMB2022-03 midpoint between nominal solidus/liquidus used for the track time-above-melt challenge;
- the feature integrates spatial and temporal hot occupancy and was defined before E09.

### Thermal sensitivity endpoint / thermal 민감도

`any_hot_duration_1298C_s`, case median across BP1 tracks. / E05에서 이미 정의된 sister feature.

### Secondary geometry endpoints / 2차 geometry

Using F02's exact BP1 track/repeat ↔ optical identity and respecting two cross-sections as nested observations:
- `Y_width(case)` = median of track-level **mean width [µm]** across the three BP1 tracks;
- `Y_depth(case)` = median of track-level **mean depth [µm]** across the three BP1 tracks.

Width and depth are always reported together. / width·depth 대칭 보고.

## 9. Frozen Statistics / 고정 통계

All statistics are case-level; there is no row-level BP1↔BP4 join. / 모든 통계는 case-level.

For each endpoint `Y`:

1. `rho_process(Y) = Spearman(X_process, Y)`;
2. `rho_coupled(Y) = Spearman(X_coupled, Y)`;
3. `delta_rho(Y) = rho_coupled(Y) - rho_process(Y)`.

Primary statistic / 1차 통계:
- `delta_rho_thermal` for `Y_thermal`.

### Factor-axis sign concordance / 공정축 방향 일치

Three frozen high-energy-vs-low-energy contrasts:
- spot axis: `1.1 - 1.2`;
- speed axis: `2.2 - 2.1`;
- power axis: `3.1 - 3.2`.

An axis is concordant when `sign[ΔX_coupled] == sign[ΔY_thermal]`; ties count as non-concordant. / 부호 일치 여부.

If case `3.2` remains partial, the power axis is marked `NOT_TESTABLE` rather than silently reconstructed. / power축 강제복원 금지.

### Exact permutation reference / exact permutation 참고값

Report an exact case-label permutation reference for `delta_rho_thermal` when all 7 cases are available (`7! = 5040` permutations), or the exact permutation set for the analyzable case count otherwise. / case label permutation reference 보고.

This is an exploratory calibration under a case-label null, **not** a causal/randomized-experiment p-value. / 무작위 실험 p-value로 해석 금지.

## 10. Frozen Decision Gate / 고정 판정 게이트

### `CROSS_MODAL_ORDERING_SIGNAL`
Requires all of:
1. at least 7 analyzable case families including baseline;
2. `rho_coupled(Y_thermal) >= 0.70`;
3. `delta_rho_thermal >= +0.20`;
4. thermal factor-axis sign concordance = `3/3`;
5. no material integrity failure.

Interpretation: BP4 coupling changes the process-energy case ordering in a way that materially improves correspondence with BP1 thermal ordering. / coupling이 process-only ordering보다 BP1 thermal ordering과 더 잘 대응.

### `PARTIAL_CROSS_MODAL_SIGNAL`
Any of:
- primary rank criteria pass but one factor axis is unavailable because `3.2_PARTIAL_REPEAT_ID`; or
- `rho_coupled >= 0.60`, `delta_rho > 0`, and at least `2/3` available axes are concordant, without meeting the full gate.

### `PROCESS_ONLY_OR_REDUNDANT_AT_CASE_LEVEL`
- `delta_rho_thermal <= 0` and `rho_process(Y_thermal) >= 0.60`.

Interpretation: coupling does not improve the case-family ordering beyond the process-only comparator under this design. / coupling 추가정보 미확인.

### `NO_COHERENT_CROSS_MODAL_RELATIONSHIP`
- `rho_coupled(Y_thermal) < 0.60` and fewer than `2/3` available axes are concordant, absent an integrity hold.

### `MIXED_ENDPOINT_SPECIFIC`
- primary thermal criteria and geometry secondary endpoints conflict materially in direction/order, or geometry width/depth show opposite strong patterns that prevent one coherent physical interpretation.

This label may coexist only as the final gate when the primary signal is not sufficient for a single coherent interpretation. / endpoint 충돌 시 혼합결론.

### `HOLD_DATA_INTEGRITY`
Any of:
- fewer than 6 analyzable nominal case families;
- time/coupling schema inconsistent with README in a way that prevents deterministic extraction;
- version/checksum mismatch;
- unresolved identifier problem contaminates more than the predeclared `3.2` sensitivity case;
- `COST-001` cannot be satisfied.

## 11. Null & Interpretation / 귀무·해석

**Primary null / 1차 귀무:** adding BP4 coupling information does not materially improve case-family rank correspondence with BP1 thermal response beyond BP4 process-only VED ordering. / coupling 추가가 process-only ordering 대비 실질적 개선 없음.

A positive result supports only:
- **aggregate cross-specimen ordering correspondence**;
- a hypothesis that dynamic coupling contains upstream physical information worth testing in a future genuinely paired or better-matched experiment.

It does **not** establish:
- same physical track or repeat identity;
- identical BP1/BP4 processing conditions;
- causal mediation `coupling → thermal → geometry`;
- a deployable predictive model;
- generalization outside these seven nominal perturbation families.

## 12. No Post-Hoc Expansion / 사후확장 금지

Inside E09, do not after outcome access:
- change the primary coupling window;
- replace median with mean/peak to improve the result;
- select only width or only favorable geometry targets;
- add CNN/transformer/high-capacity models;
- introduce surface roughness as a harmonized covariate;
- directly pair BP1/BP4 repeats;
- rewrite the case `3.2` filename conflict;
- change thresholds `0.70`, `+0.20`, `0.60`, or the axis-concordance rules.

Any such change requires a new preregistered hypothesis. / 변경은 별도 사전등록 필요.

## 13. COST-001 / 비용

Planned execution is permitted only with zero incremental monetary cost:
- official public NIST data;
- local computation or standard public-repository GitHub-hosted runner only;
- no GPU/larger runner;
- no paid API/SaaS/cloud/data;
- no large artifact upload.

`mds2-3842` measurement ZIP is only ~94 kB by F08 manifest, but it remains outcome-bearing and must not be downloaded until this preregistration is frozen and the active Issue exists. / 크기와 무관하게 사전등록 전 outcome data 접근 금지.

## 14. Execution Order / 실행 순서

After this file is committed and the Issue is opened:
1. verify exact frozen PDR versions and checksums;
2. download `mds2-3842` ZIP under `COST-001`;
3. filename-only `3.2` identity preflight before numeric read;
4. deterministic coupling feature extraction exactly as above;
5. recover the frozen BP1 E05/F02 case-level endpoints without changing definitions;
6. compute `X_process`, `X_coupled`, rank statistics, axis concordance, and permutation reference;
7. apply exactly one frozen final gate;
8. write `RESULT.md`, Claim Ledger, Decision Log, Issue closure, STATUS/HANDOFF/MEMORY.

No scientific result is claimed by this preregistration itself. / 본 문서는 결과가 아니라 실행 전 고정설계다.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `MEMORY-001`, and `WRITEBACK-001`. / 관련 규약 준수.