# AMBENCH-F04 Result / 보정 열동역학 feasibility 결과

**Issue / 이슈:** #15  
**Date / 기준일:** 2026-08-22  
**Final gate / 최종 게이트:** `PARTIAL — CALIBRATION_REPRODUCIBLE / HISTORICAL_SINGLE-TRACK_METRIC_REPRODUCTION_INCOMPLETE`  
**Cost boundary / 비용경계:** `COST-001` — no new metered execution used for this disposition. / 신규 metered 실행 없이 판정.

## 1. Executive Result / 핵심 결과

**KO:** 현재 NIST PDR v1.3.1에 보존된 thermography calibration은 공식 HDF5 metadata와 NIST 저자 논문을 결합하면 수학적으로 재현 가능한 수준까지 복구된다. 그러나 2022 AMB2022-03 single-track challenge의 TTAM/TSCR/TLCR를 **원래 방식 그대로 21개 repeat에서 재현**하기에는 per-repeat emissivity 산정, `nominally steady-state` pixel 위치, `mildly smoothed` 처리 등 일부 구현 선택이 정확한 machine-readable 규칙으로 남아 있지 않고, 2022 결과문서와 2024 corrected HDF5 calibration 사이에도 수치 계보 차이가 존재한다. 따라서 full `PASS`가 아니라 `PARTIAL`이다.

**EN:** The current NIST PDR v1.3.1 thermography calibration is recoverable to a mathematically reproducible form by combining the official HDF5 metadata with a NIST-authored publication. However, the original 2022 single-track TTAM/TSCR/TLCR workflow cannot be reproduced exactly across all 21 repeats from the currently verified public record because some implementation choices—per-repeat emissivity estimation, the exact `nominally steady-state` pixel location, and `mildly smoothed` processing—are not fully specified as machine-readable rules, and there is a numerical lineage difference between the 2022 result document and the 2024-corrected HDF5 calibration. The correct gate is therefore `PARTIAL`, not `PASS`.

## 2. Frozen Raw Source / 고정 raw 소스

- NIST PDR: `mds2-2716`
- frozen distribution: v1.3.1
- HDF5 SHA-256: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- 21 `Line_*` groups = 7 process cases × 3 repeats
- each `Signal`: `[700,640,304]`, `uint16`, 12-bit
- metadata frame rate: `30,000 frames/s`
- source zeroing: `threshold_level=100`, `threshold_zeros=true`

These facts were previously reproduced in Runs `32537038475` and `32537157650`; F04 reused the existing evidence rather than creating a new metered run. / 기존 증거를 재사용했다.

## 3. Current Corrected Calibration / 현행 corrected calibration

The official HDF5 `/Calibration/ThermalCal` stores: / HDF5 직접 metadata

- `Cal_Method = RegressionF_ArrayAvg`
- `Coeff_a = 0.9655`
- `Coeff_b = 197.2`
- `Coeff_c = 43,920,000`
- `Model_input = Signal [DL]`
- `Model_output = Emissivity-Corrected Temperature [°C]`
- `R-square = 0.9988`
- `RMSE = 4.923`
- dataset note: `Update 9/12/24: Corrected Calibration/ThermalCal/Model equation.`

The stored `Model` text is syntactically incomplete-looking, so it is **not** executed as code by inference. / HDF5 문자열 자체를 추정 실행하지 않는다.

A later NIST-authored open publication gives the Sakuma-Hattori transformation with the same coefficients: / 동일 coefficient를 사용하는 NIST 저자 공식식

`T(S, ε) = c2 / [A · ln(ε·C/S + 1)] − B/A`

where / 변수
- `A = 0.9655`
- `B = 197.2`
- `C = 4.391×10^7`
- `c2 = 14,388 µm/K`
- the later pad analysis estimates `ε = 0.5`.

This establishes a defensible mathematical interpretation of the current corrected calibration. / 현행 corrected calibration의 수학적 의미는 방어 가능하게 복구됨.

## 4. Emissivity Hierarchy / emissivity 계층

Two distinct authoritative uses must not be conflated. / 두 사용례를 혼동 금지.

### A. Effective common emissivity / 공통 effective emissivity
NIST later documents `ε ≈ 0.5` as an effective emissivity derived from AMB2022-03 and uses it in related AM Bench thermography algorithms and later Pad-Y analysis. / 후속 분석의 공통값.

### B. Original AMB2022-03 single-track challenge / 원 single-track challenge
The 2022 result document states that the apparent solidification temperature is identified for each track and emissivity is then used to map that apparent inflection to the assumed true solidification transition. Figure 1 shows **three emissivity values for each of the seven process cases**, i.e. repeat-level variation rather than one exact constant for all 21 tracks. / 원 challenge는 repeat별 emissivity 변동을 사용.

Therefore, `ε=0.5` is authoritative as a later effective/common representation, but it is **not promoted as the exact historical per-repeat emissivity table** for the 2022 single-track results. / `0.5`를 과거 21개 exact 값으로 간주하지 않는다.

## 5. Original Single-Track Algorithm / 원 single-track 알고리즘

NIST's 2022 challenge description states: / 공식 정의

1. use `30 adjacent pixels` along the melt-path centerline at a `nominally steady-state` location;
2. align temperature histories by rising edges;
3. `mildly smooth` and average them into a representative steady-state thermal history;
4. identify the solidification discontinuity;
5. fit a cubic polynomial over approximately `±50 °C` around the apparent inflection;
6. define the inflection where the second derivative of the cubic fit is zero;
7. assume this inflection corresponds to the midpoint of IN718 solidus/liquidus: `1298 °C` (`1260/1336 °C`);
8. calculate cooling-rate slopes using:
   - liquid: `1400 → 1336 °C`;
   - transition: `1336 → 1260 °C`;
   - solid: `1260 → 1150 °C`.

The official result table reports **averages of three individual tracks** for seven process cases, not 21 repeat-level output labels. / 공식 결과는 7개 case 평균.

## 6. Version-Lineage Finding / 버전계보 발견

Existing version-specific NIST PDR manifests show: / 기존 PDR manifest 재검사

- v1.1.0 and v1.2.0 (`modified=2022-07-15`) contain the README/sample photos but **do not contain the thermography HDF5** in their component manifests;
- v1.3.0 (`modified=2024-09-17`) introduces the thermography HDF5 and scan-strategy HDF5;
- v1.3.0 and v1.3.1 contain the same frozen thermography HDF5 hash;
- the HDF5 itself records the 2024-09-12 calibration-Model correction.

Therefore the current distributed HDF5 is a later data-publication snapshot relative to the July 2022 challenge result document. / 현행 HDF5는 2022 결과문서보다 후대 snapshot.

## 7. Numerical Calibration Divergence / calibration 수치 차이

The July 2022 result document describes pad preprocessing thresholds as approximately: / 2022 문서

- `100 DL ≈ 1077 °C at ε=0.5`
- `760 DL ≈ 1260 °C at ε=0.5`

Using the **current corrected** Sakuma-Hattori coefficients and `ε=0.5` gives: / 현행 corrected 식 직접 계산

- `100 DL → 1007.37 °C`
- `760 DL → 1246.62 °C`
- `1150 °C → 365.23 DL`
- `1260 °C → 834.82 DL`
- `1298 °C → 1079.94 DL`
- `1336 °C → 1379.41 DL`

The project records this as a **version/calibration lineage conflict**, not as proof that either historical result or current calibration is wrong. / 어느 한쪽 오류로 단정하지 않고 계보차이로 기록.

## 8. Additional Timing Sensitivity / 추가 시간축 민감도

The frozen HDF5 records `30,000 frames/s`. A 2025 NIST-authored Pad-Y study reports an empirically computed `30,686 fps` for that pad measurement from frame count / total duration. / 후속 Pad-Y 연구는 30,686 fps 보고.

F04 does **not** substitute `30,686` for the single-track HDF5 timing because track-specific applicability has not been established. / single-track에 임의 대체 금지.

This remains `TIMING_SENSITIVITY / UNKNOWN_TRACK_APPLICABILITY`. / 적용여부 미확인.

## 9. Safe Outcome-Blind Representation Boundary / 안전한 후속 표현 경계

A later experiment may define a **new current-calibration representation** using: / 후속 별도 가설에서 허용 가능

- frozen v1.3.1 raw HDF5;
- current corrected Sakuma-Hattori equation;
- explicitly fixed `ε=0.5` as the later NIST effective/common emissivity;
- HDF5 frame metadata unless a track-specific timing correction is independently established;
- physically named thresholds `1150 / 1260 / 1298 / 1336 °C` only within the documented calibrated domain;
- no claim that these reproduce the original 21-repeat historical challenge calculations.

Potential compact features may include temperature-domain time/area summaries, but they must be preregistered as a **new representation experiment** before optical outcomes are consulted. / temperature-domain feature는 새로운 사전등록 실험에서만 사용.

The following are **not frozen as historical-reproduction features**: exact original TTAM/TSCR/TLCR per repeat, exact per-repeat emissivity, exact 30-pixel coordinates, or an unspecified smoothing implementation. / 원 challenge exact 재현 feature로 고정 금지.

## 10. Gate Decision / 게이트 판정

### `PARTIAL`

Passes / 통과:
- exact current source/version/hash lineage;
- corrected mathematical calibration form;
- input/output units;
- authoritative later effective `ε≈0.5` semantics;
- physical transition temperatures and cooling-rate intervals;
- correct seven-case output aggregation boundary.

Does not pass full reproduction / full PASS 미충족:
- exact historical per-repeat emissivity table is not machine-readable in the verified source;
- exact steady-state 30-pixel coordinates are not specified;
- `mildly smoothed` is not an executable filter specification;
- current HDF5 calibration post-dates the 2022 challenge results and produces different threshold conversions;
- later Pad-Y `30,686 fps` timing observation is not proven applicable to the single-track runs;
- no new potentially metered compute was authorized under `COST-001` to rerun a 550 MB full raw extraction merely to bridge these documentary gaps.

**Disposition / 처리:** close F04 as completed `PARTIAL`. A downstream E05 may test a clearly labeled **current corrected-calibration thermal representation** as a new hypothesis, but must not present it as an exact reproduction of the historical 2022 single-track challenge pipeline. / F04 종료 PARTIAL, 후속은 신규가설로만 진행.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and snapshot-lineage controls. / 관련 규약 준수.
