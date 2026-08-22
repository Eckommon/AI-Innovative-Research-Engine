---
id: AMBENCH-E09-RESULT
type: controlled-experiment-result
state: COMPLETED_INCONCLUSIVE_CASE_LEVEL
evidence_class: DERIVED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-E09/README.md
  - research/AMBENCH-E09/AMENDMENT-01.md
  - docs/RAW_DATA_TRANSIENT_POLICY.md
  - Issue #24
  - Run 32550309862
---

# AMBENCH-E09 Result — Unpaired BP4 Coupling → BP1 Thermal/Geometry Case-Family Ordering / 비paired BP4 coupling → BP1 열·형상 case-family 순서 검증 결과

**Issue / 이슈:** #24  
**Evidence Run / 증거 Run:** GitHub Actions `32550309862`  
**Job / Job:** `96975852410`  
**Run conclusion / 실행 결론:** `success`  
**Frozen final gate / 고정 최종 gate:** **`INCONCLUSIVE_CASE_LEVEL`**  
**Raw policy / 원천데이터 정책:** `RAW_DATA_TRANSIENT_ONLY`  
**Cost / 비용:** `COST-001` compliant — standard public-repository `ubuntu-latest`, public NIST sources, no GPU/larger runner, no paid API/cloud/data, no raw-data artifact upload. / 추가 금전비용 0원 경로.

## 1. Executive Result / 핵심 결과

**KO:** BP4 dynamic laser coupling은 7개 nominal case의 coupling-weighted VED **크기**를 변화시켰지만, BP4 process-only VED의 **순위(ordering)는 단 하나도 바꾸지 않았다**. 따라서 사전등록된 순위 기반 검증에서 모든 endpoint의 `rho_coupled`와 `rho_process`가 동일했고 `delta_rho = 0`이었다. 1차 BP1 thermal endpoint는 두 predictor 모두와 `rho = 0.07143`으로 낮았고, 세 공정축 중 speed·power 2개만 부호가 일치했다. 고정 gate 어느 양성·음성 분류에도 정확히 들어가지 않아 최종 결과는 **`INCONCLUSIVE_CASE_LEVEL`**이다.

**EN:** BP4 dynamic laser coupling changed the **magnitudes** of coupling-weighted VED across the seven nominal cases but did **not change the rank ordering of any case** relative to BP4 process-only VED. Consequently, every preregistered rank-based endpoint had identical `rho_coupled` and `rho_process`, so `delta_rho = 0`. The primary BP1 thermal endpoint correlated only `rho = 0.07143` with either predictor, while two of three process axes (speed and power) were sign-concordant. No frozen positive or negative label was exactly satisfied, so the final result is **`INCONCLUSIVE_CASE_LEVEL`**.

This result does **not** show that dynamic coupling is physically redundant in general. It shows that, under this frozen **unpaired seven-case aggregate ordering test**, coupling supplied no incremental **rank-order** information beyond the process-only ordering. / coupling 일반적 무용성을 뜻하지 않고 이번 aggregate ordering 설계에서 추가 rank 정보가 없었다는 뜻이다.

## 2. Integrity & Reproducibility / 무결성·재현성

### BP4 `mds2-3842`
- exact version: `1.0.3`;
- exact manifest SHA-256: `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb`;
- ZIP bytes: `93,566`;
- expected = actual ZIP SHA-256: `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`.

### BP1 frozen sources / BP1 고정 입력
- thermography bytes: `549,979,044`;
- expected = actual thermography SHA-256: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`;
- optical XLSX bytes: `25,811`;
- expected = actual optical SHA-256: `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`.

All workflow steps completed successfully. / 전체 workflow step 성공.

## 3. Case `3.2` Identity Resolution / case `3.2` 식별자 해결

The preregistered filename-only preflight ran **before any numeric coupling file content was read**. / 숫자값 열람 전 ZIP central-directory filename·metadata만 검사했다.

Preflight:
- `PREFLIGHT_MODE = FILENAMES_AND_ZIP_METADATA_ONLY_NO_FILE_CONTENT_READ`;
- archive entries = `21`;
- unique expected TXT basenames = `21/21`;
- missing expected = none;
- extra TXT = none;
- duplicate-content conflicts = none.

The exact archive directly contains three distinct files:
- `3_2_1sv.txt` — size `27,825`, CRC `71e50308`;
- `3_2_2sv.txt` — size `27,825`, CRC `ca5a0d43`;
- `3_2_3sv.txt` — size `27,825`, CRC `4838c784`.

**Preflight result:** **`3.2_ID_RESOLVED_BY_ARCHIVE`**.

Interpretation / 해석:
- F08의 `summary_of_data_files.csv`가 Line 2와 Line 3에 `3_2_2sv.txt`를 중복 기재한 **source-internal provenance inconsistency 자체는 기록상 유지**한다.
- 그러나 checksum-verified exact ZIP archive의 직접 증거가 별도 `3_2_3sv.txt`의 존재를 확인했으므로 **E09 분석을 위한 case 3.2 third-repeat file identity는 해결됐다**.
- 원 source CSV를 조용히 수정하거나 재작성하지 않는다. / source CSV 자체를 수정한 것으로 간주하지 않는다.

## 4. Frozen BP4 Coupling Descriptor / 고정 BP4 coupling descriptor

Each track used the preregistered central normalized-time `20–80%` median; no smoothing/manual crop/target-aware selection was used. / 각 track에서 고정 `τ∈[0.20,0.80]` 중앙값 사용.

All 21 files parsed successfully and every track had `outside_nominal_0_1 = 0`. / 모든 coupling sample이 명목 0–1 범위 내.

| Case | `C_case` | Full-track median sensitivity |
|---|---:|---:|
| `0` | 0.6347681 | 0.6347681 |
| `1.1` | 0.7287823 | 0.7301885 |
| `1.2` | 0.5507982 | 0.5509989 |
| `2.1` | 0.6152821 | 0.6162867 |
| `2.2` | 0.6480267 | 0.6492318 |
| `3.1` | 0.6649222 | 0.6650985 |
| `3.2` | 0.5964035 | 0.5964035 |

## 5. Process-only vs Coupling-informed Predictor / process-only 대비 coupling predictor

Frozen predictor:
`X_coupled = X_process × (C_case/C_case0)`.

| Case | `X_process` | `C_ratio` | `X_coupled` |
|---|---:|---:|---:|
| `0` | 1.00 | 1.000000 | 1.000000 |
| `1.1` | 2.09 | 1.148108 | 2.399546 |
| `1.2` | 0.71 | 0.867716 | 0.616078 |
| `2.1` | 0.80 | 0.969302 | 0.775442 |
| `2.2` | 1.20 | 1.020887 | 1.225065 |
| `3.1` | 1.14 | 1.047504 | 1.194155 |
| `3.2` | 0.86 | 0.939561 | 0.808023 |

### Critical structural result / 핵심 구조 결과

Both predictors have exactly the same seven-case rank order: / 두 predictor의 case 순위가 완전히 동일하다.

`1.1 > 2.2 > 3.1 > 0 > 3.2 > 2.1 > 1.2`

Therefore any Spearman rank correlation with any fixed BP1 endpoint is necessarily identical for `X_process` and `X_coupled` in this dataset. / 따라서 이번 frozen rank test에서는 coupling이 순위 정보를 추가할 수 없었다.

## 6. Frozen BP1 Case Endpoints / 고정 BP1 case endpoint

| Case | `Y_thermal` | Thermal sensitivity [s] | Width [µm] | Depth [µm] |
|---|---:|---:|---:|---:|
| `0` | 4.246133 | 0.011000 | 135.5850 | 139.7940 |
| `1.1` | 3.269100 | 0.010967 | 106.5360 | 227.1480 |
| `1.2` | 4.988567 | 0.010900 | 141.0015 | 102.1545 |
| `2.1` | 3.192433 | 0.008733 | 113.0565 | 108.8475 |
| `2.2` | 5.430300 | 0.013233 | 155.6640 | 175.1565 |
| `3.1` | 4.689467 | 0.011033 | 134.0670 | 166.0830 |
| `3.2` | 3.806533 | 0.010933 | 130.0995 | 116.8860 |

`Y_thermal` = case median of preregistered `hot_pixel_time_integral_1298C_px_s`. / 기존 E05 정의 그대로 재계산.

## 7. Frozen Rank Statistics / 고정 순위통계

| Endpoint | `rho_process` | `rho_coupled` | `delta_rho` |
|---|---:|---:|---:|
| Primary thermal | 0.0714286 | 0.0714286 | **0.0000000** |
| Thermal sensitivity | 0.7500000 | 0.7500000 | **0.0000000** |
| Width | -0.1428571 | -0.1428571 | **0.0000000** |
| Depth | 1.0000000 | 1.0000000 | **0.0000000** |

The perfect depth rank correlation is descriptive and is **not** evidence that coupling adds information, because process-only has the exact same `rho = 1.0`. / depth의 1.0은 coupling incremental evidence가 아니다.

Likewise, the thermal-sensitivity `rho = 0.75` is identical for both predictors and cannot be promoted as coupling-specific evidence. / sensitivity의 0.75도 coupling 고유효과가 아니다.

## 8. Frozen Factor-Axis Concordance / 공정축 부호 일치

Primary thermal endpoint:

| Axis | `ΔX_coupled` | `ΔY_thermal` | State |
|---|---:|---:|---|
| spot `1.1−1.2` | +1.783468 | -1.719467 | `DISCORDANT` |
| speed `2.2−2.1` | +0.449623 | +2.237867 | `CONCORDANT` |
| power `3.1−3.2` | +0.386132 | +0.882933 | `CONCORDANT` |

Concordance = **`2/3`**.

## 9. Exact Permutation Reference / exact permutation 참고

All `7! = 5,040` case-label permutations were evaluated for primary `delta_rho`.

Because the two predictors have identical ranks, **every permutation also has `delta_rho = 0`**:
- observed `delta_rho = 0.0`;
- permutation min = `0.0`;
- permutation max = `0.0`;
- one-sided `Pr(delta_perm >= delta_obs) = 1.0`;
- two-sided `Pr(|delta_perm| >= |delta_obs|) = 1.0`.

This is a descriptive case-label-null reference, not a randomized causal p-value. / 인과 p-value 아님.

## 10. Frozen Gate Application / 고정 gate 적용

### Full positive `CROSS_MODAL_ORDERING_SIGNAL`
Fails:
- 7 analyzable cases: **PASS**;
- `rho_coupled >= 0.70`: **FAIL** (`0.07143`);
- `delta_rho >= +0.20`: **FAIL** (`0.0`);
- axis concordance `3/3`: **FAIL** (`2/3`).

### `PARTIAL_CROSS_MODAL_SIGNAL`
Fails because `rho_coupled < 0.60` and `delta_rho = 0`. / 조건 미충족.

### `PROCESS_ONLY_OR_REDUNDANT_AT_CASE_LEVEL`
Frozen rule requires `delta_rho <= 0` **and** `rho_process >= 0.60`.  
The first condition passes, but primary `rho_process = 0.07143`; therefore this label does **not** apply. / process-only 자체가 primary thermal ordering을 잘 설명하지 못해 이 label 불가.

### `NO_COHERENT_CROSS_MODAL_RELATIONSHIP`
Frozen rule requires `rho_coupled < 0.60` and fewer than `2/3` available axes concordant.  
`rho_coupled` is low, but concordance is exactly `2/3`; therefore this label does **not** apply.

### `MIXED_ENDPOINT_SPECIFIC`
Amendment-01 allows this override only after a positive primary candidate; the primary candidate is not positive, so the override does **not** apply.

### Final

**`INCONCLUSIVE_CASE_LEVEL`**

The result is scientifically informative despite the label: the frozen ordering test detects **zero incremental rank-order information from coupling**, but the primary process-only ordering is also weak, preventing the stronger preregistered `PROCESS_ONLY_OR_REDUNDANT_AT_CASE_LEVEL` label. / coupling 추가 rank 정보는 0이지만 process-only 자체도 primary를 설명하지 못해 더 강한 redundant 판정은 하지 않는다.

## 11. Interpretation Boundary / 해석 경계

Supported / 지지되는 해석:
- exact archive evidence resolves the E09 case `3.2` third-file identity;
- BP4 coupling varies systematically across cases and is reproducible at the frozen descriptor level;
- multiplying process VED ordering by the measured coupling ratio changes magnitudes but preserves the seven-case rank exactly;
- therefore the frozen rank-order test shows no incremental rank information from coupling;
- primary thermal response is poorly rank-correlated with either process-only or coupling-informed predictor;
- secondary endpoints are heterogeneous: depth is perfectly rank-correlated, width is weakly negative, thermal-duration sensitivity is moderately/highly positive, but none gains from coupling over process-only.

Not supported / 지지되지 않는 해석:
- `dynamic coupling is useless in general`;
- `coupling is redundant at all resolutions`;
- `BP1 and BP4 are paired sensors/tracks`;
- `depth is causally determined by coupling`;
- `rho=1.0 depth` is coupling-specific evidence;
- higher-capacity modeling would necessarily reveal a signal;
- roughness has been harmonized or the `Ra` provenance conflict resolved.

## 12. Raw-Data & Cost Execution / raw-data·비용 실행

`RAW-001` was applied exactly:
1. source/version/checksum fixed;
2. raw NIST data downloaded only to ephemeral `work/raw`;
3. filename-only preflight before coupling numeric read;
4. numeric analysis after gate;
5. no `actions/upload-artifact`;
6. no raw source committed to repository;
7. `rm -rf work/raw` at end;
8. `RAW_TEARDOWN=SUCCESS`.

No incremental monetary cost was introduced. / 추가 금전비용 없음.

## 13. Disposition / 처리

Close E09 as **`COMPLETED — INCONCLUSIVE_CASE_LEVEL`**. / E09 종료.

Do not tune the rank test or increase model capacity inside E09. Any follow-up must be a new preregistered hypothesis that changes the scientific relationship being tested rather than optimizing this result away. Candidate directions may include a magnitude-sensitive physical relationship, within-BP4 coupling dynamics, or genuinely independent process conditions; none is automatically authorized by E09. / 후속은 별도 사전등록 필요.

Official artifacts comply with `LANG-001`, `COST-001`, `RAW-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `MEMORY-001`, and `WRITEBACK-001`. / 관련 규약 준수.
