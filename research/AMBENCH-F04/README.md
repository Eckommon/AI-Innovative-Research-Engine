---
id: AMBENCH-F04
type: feasibility
state: COMPLETED_PARTIAL
evidence_class: OBSERVED_DERIVED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F02/README.md
  - research/AMBENCH-E03/README.md
  - research/AMBENCH-NEXT-TRIAGE.md
  - research/AMBENCH-F04/RESULT.md
---

# AMBENCH-F04 — Calibrated Thermal-Dynamics Representation Feasibility / 보정 열동역학 표현 가능성 검증

**Issue / 이슈:** #15  
**State / 상태:** `COMPLETED — PARTIAL`  
**Gate / 게이트:** `PARTIAL — CALIBRATION_REPRODUCIBLE / HISTORICAL_SINGLE-TRACK_METRIC_REPRODUCTION_INCOMPLETE`  
**Parent result / 상위 결과:** `AMBENCH-E03 — NO_MATERIAL_GAIN`

## 1. Research Question / 연구 질문

**KO:** frozen AMB2022-03 thermography snapshot에서 NIST의 공식 calibration·시간·상변태 기준을 이용해, optical outcome을 보지 않고도 21개 track 전체에 대해 재현 가능한 물리적 온도/냉각 동역학 표현을 만들 수 있는가?  
**EN:** From the frozen AMB2022-03 thermography snapshot, can NIST's official calibration, timing, and phase-transition semantics support a reproducible physical temperature/cooling-dynamics representation for all 21 tracks without using optical outcomes?

## 2. Final Answer / 최종 답

**KO:** **부분적으로 가능하다.** 현재 v1.3.1 HDF5의 corrected DL→temperature calibration은 공식 metadata와 NIST 저자 논문으로 수학적으로 복구할 수 있다. 그러나 2022 single-track challenge의 원래 TTAM/TSCR/TLCR를 21개 repeat에서 정확히 복원하려면 per-repeat emissivity, exact 30-pixel 위치, smoothing 구현 등 공개근거에 남지 않은 선택이 필요하며, 2022 결과문서와 2024 corrected calibration 사이에도 수치계보 차이가 있다. 따라서 full `PASS`가 아니라 `PARTIAL`이다.

**EN:** **Partially.** The current v1.3.1 corrected DL→temperature calibration is mathematically recoverable from official metadata and a NIST-authored publication. Exact reconstruction of the original 2022 single-track TTAM/TSCR/TLCR workflow across all 21 repeats is not fully determined by the verified public record because repeat-specific emissivity, exact 30-pixel location, smoothing implementation, and historical calibration lineage are incomplete. The correct result is `PARTIAL`, not full `PASS`.

Detailed evidence / 상세 근거: `research/AMBENCH-F04/RESULT.md`.

## 3. Frozen Sources / 고정 소스

- NIST PDR `mds2-2716`, version `1.3.1`
- frozen thermography HDF5 SHA-256 `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- NIST AMB2022-03 challenge/measurement description and measurement-result documents
- exact track identities from `AMBENCH-F02`

Optical geometry from `mds2-2718` was excluded from feature/calibration/threshold decisions in F04. / optical outcome 미사용.

## 4. Validated Current Raw & Calibration Semantics / 검증된 현행 raw·calibration 의미

- exactly `21` thermography `Line_*` groups;
- each `Signal` `[700,640,304]`, `uint16`, 12-bit;
- HDF5 frame rate `30,000 frames/s`;
- `threshold_level=100`, `threshold_zeros=true`;
- `/Calibration/ThermalCal`:
  - `Cal_Method=RegressionF_ArrayAvg`
  - `A=0.9655`, `B=197.2`, `C≈4.392×10^7`
  - `Model_input=Signal [DL]`
  - `Model_output=Emissivity-Corrected Temperature [°C]`
  - `R²=0.9988`, `RMSE=4.923`
- HDF5 note records a 2024-09-12 correction to the calibration `Model` equation.

The defensible current corrected mathematical form, corroborated by a NIST-authored publication with the same coefficients, is the Sakuma-Hattori relation: / 현행 corrected 식

`T(S,ε) = c2 / [A·ln(ε·C/S + 1)] − B/A`, with `c2=14,388 µm/K`.

## 5. Emissivity Boundary / emissivity 경계

- NIST later uses/defines an effective common `ε≈0.5` derived from AMB2022-03 for related AM Bench thermography work. / 후속 공통 effective 값.
- The original 2022 **single-track** results instead identify an apparent solidification inflection and show repeat-varying emissivity for all seven cases × three repeats. / 원 single-track은 repeat별 값.

Therefore `ε=0.5` may support a **new current-calibration representation**, but is not claimed to be the exact historical 21-repeat emissivity table. / 역사적 exact 값으로 승격 금지.

## 6. Original Single-Track Physical Algorithm / 원 single-track 물리 알고리즘

NIST documents: / 공식 정의
- 30 adjacent centerline pixels at a nominally steady-state location;
- rising-edge alignment;
- mild smoothing + averaging;
- cubic fit around approximately `±50 °C` of apparent solidification inflection;
- second-derivative zero as inflection;
- true transition midpoint `1298 °C` from solidus/liquidus `1260/1336 °C`;
- cooling-rate intervals:
  - liquid `1400→1336 °C`;
  - transition `1336→1260 °C`;
  - solid `1260→1150 °C`.

Official TTAM/TSCR/TLCR outputs are **seven process-case averages over three tracks**, not 21 repeat labels. / 결과 해상도 7개 case.

## 7. Version-Lineage Constraint / 버전계보 제약

Version-specific PDR manifests show that 2022-era v1.1.0/v1.2.0 did not include the thermography HDF5 component, while v1.3.0 modified in September 2024 introduced the current HDF5. v1.3.0 and v1.3.1 contain the same HDF5 hash. / current raw snapshot은 후대 공개본.

The 2022 result document describes `100 DL≈1077 °C` and `760 DL≈1260 °C` at `ε=0.5`, whereas the current corrected coefficients give approximately `100 DL→1007.37 °C` and `760 DL→1246.62 °C`. / 수치 불일치.

This is recorded as **calibration/version lineage divergence**, not as evidence that one source is wrong. / 오류 단정 금지.

## 8. Timing Sensitivity / 시간축 민감도

HDF5 metadata = `30,000 fps`. A later NIST-authored Pad-Y analysis computes `30,686 fps` from actual frames/duration for that pad experiment. Track-specific applicability is unverified, so F04 retains the HDF5 timing for single tracks and labels the later figure `UNKNOWN_TRACK_APPLICABILITY`. / 임의 교체 금지.

## 9. Gate / 판정

### Passed components / 통과요소
- source/version/hash lineage;
- current corrected calibration equation and units;
- later authoritative effective `ε≈0.5` semantics;
- phase-transition temperatures and cooling-rate intervals;
- correct seven-case output aggregation boundary.

### Full-PASS blockers / full PASS 차단요소
- no exact machine-readable historical per-repeat emissivity table in verified source;
- exact 30-pixel coordinates not specified;
- `mildly smoothed` not an executable filter specification;
- 2022 result-threshold conversion differs from current corrected HDF5 calibration;
- later `30,686 fps` observation not proven for single tracks.

**Final:** `PARTIAL`.

## 10. Downstream Rule / 후속 규칙

A downstream E05 is allowed only as a **new preregistered current-corrected-calibration hypothesis**. / 후속 E05는 신규 사전등록 current calibration 가설로만 허용.

It may not claim exact reproduction of the 2022 single-track challenge unless the missing historical per-repeat calibration/processing semantics are independently recovered. / 누락 historical 의미 복구 전 2022 exact 재현 주장 금지.

## 11. Cost Governance / 비용 거버넌스

`COST-001` is mandatory. F04 disposition reused official public sources and existing artifacts rather than triggering additional metered compute. Any downstream potentially billable execution requires explicit user approval in advance; unknown billing state is `HOLD_COST_APPROVAL`. / 무비용 기본·비용가능 작업 사전승인.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and snapshot-lineage controls. / 관련 규약 준수.
