---
id: AMBENCH-F04
type: feasibility
state: ACTIVE
evidence_class: OBSERVED_HYPOTHESIZED
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F02/README.md
  - research/AMBENCH-E03/README.md
  - research/AMBENCH-NEXT-TRIAGE.md
---

# AMBENCH-F04 — Calibrated Thermal-Dynamics Representation Feasibility / 보정 열동역학 표현 가능성 검증

**Issue / 이슈:** #15  
**State / 상태:** `ACTIVE — CALIBRATION/ALGORITHM RECOVERY`  
**Parent result / 상위 결과:** `AMBENCH-E03 — NO_MATERIAL_GAIN`

## 1. Research Question / 연구 질문

**KO:** frozen AMB2022-03 thermography snapshot에서 NIST의 공식 calibration·시간·상변태 기준을 이용해, optical outcome을 보지 않고도 21개 track 전체에 대해 재현 가능한 물리적 온도/냉각 동역학 표현을 만들 수 있는가?  
**EN:** From the frozen AMB2022-03 thermography snapshot, can NIST's official calibration, timing, and phase-transition semantics support a reproducible physical temperature/cooling-dynamics representation for all 21 tracks without using optical outcomes?

## 2. Frozen Sources / 고정 소스

- NIST PDR `mds2-2716`, version `1.3.1`
- frozen thermography HDF5 SHA-256 `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- NIST AMB2022-03 challenge/measurement description and measurement-result documents
- exact track identities from `AMBENCH-F02`

Optical geometry from `mds2-2718` is excluded from feature/calibration/threshold decisions in F04. / F04의 feature·calibration·threshold 결정에서 optical geometry를 제외한다.

## 3. Already Validated Raw Semantics / 기존 검증 raw 의미

From E03 outcome-blind runs: / E03 outcome-blind run 근거
- exactly `21` thermography `Line_*` groups;
- each `Signal` shape `[700,640,304]`, `uint16`, 12-bit digital levels;
- `n_frames=700`;
- frame rate `30,000 frames/s`;
- source metadata `threshold_level=100`, `threshold_zeros=true`;
- group attrs preserve laser power, scan speed, D4σ spot size;
- NIST calibration group exists and includes regression coefficients/quality metadata.

## 4. Official NIST Physical Semantics / 공식 NIST 물리 의미

Current official NIST challenge/result documentation states: / NIST 공식 문서
- `TSCR`: cooling rate immediately after complete solidification, below solidus, at the center of each track;
- `TLCR`: liquid cooling rate immediately before solidification, above liquidus, at the center of each track;
- `TTAM`: time above the midpoint between solidus and liquidus;
- IN718 solidus `1260 °C`, liquidus `1336 °C`, midpoint/transition `1298 °C` are the benchmark assumptions used across the related thermography analysis;
- a `110 °C` range below solidus is documented for solid cooling-rate definition in the related AMB2022 thermography methodology.

For the single-track results, NIST states TAM/cooling-rate values are determined from `30 adjacent pixels` at the track centerline at a nominally steady-state location. Apparent solidification temperature is determined and emissivity is used to convert apparent temperature to true temperature. / single-track 결과는 정상상태 위치의 중심선 인접 30 pixel 기반이며 apparent solidification temperature와 emissivity 보정을 사용한다.

## 5. Resolution Boundary / 해상도 경계

The official result document explicitly states the reported single-track TAM and cooling-rate values are **averages of three individual tracks**. Table 2 therefore provides seven process-case values, not 21 repeat-level labels. / 공식 결과값은 3개 track 평균이므로 Table 2는 7개 process-case 결과이지 21개 repeat label이 아니다.

Published case-level values: / 공개 case-level 값

| Case | TTAM (s) | TSCR (°C/s) | TLCR (°C/s) |
|---|---:|---:|---:|
| 0 | 1.22E-03 | 6.99E+05 | 4.14E+05 |
| 1.1 | 1.30E-03 | 7.32E+05 | 4.06E+05 |
| 1.2 | 1.04E-03 | 5.11E+05 | 3.65E+05 |
| 2.1 | 8.96E-04 | 7.85E+05 | 5.06E+05 |
| 2.2 | 1.59E-03 | 6.11E+05 | 3.25E+05 |
| 3.1 | 1.38E-03 | 7.05E+05 | 3.81E+05 |
| 3.2 | 1.03E-03 | 7.49E+05 | 4.33E+05 |

These values may be used only for **case-level reproduction validation**, not as 21 independent supervised outcomes. / 이 값은 case-level 재현검증에만 사용하며 21개 독립 target으로 사용하지 않는다.

## 6. Calibration Ambiguity Still Open / 아직 열린 calibration 쟁점

The HDF5 contains calibration coefficients, but F04 does **not** infer the mathematical formula from coefficient names alone. The exact digital-level → apparent-temperature → emissivity-corrected-temperature transformation, its domain, and any per-case emissivity rule must be recovered from authoritative NIST metadata/documentation or processing code. / HDF5 coefficient 이름만으로 수식을 추정하지 않으며 exact 변환식·적용범위·case별 emissivity 규칙을 NIST 근거로 복구해야 한다.

## 7. Frozen Feasibility Gate / 고정 feasibility 게이트

### `PASS`
- exact calibration equation/units/domain recovered from authoritative source;
- deterministic implementation succeeds on all 21 tracks;
- timing semantics explicit;
- compact calibrated temporal feature manifest can be frozen without optical outcomes or undocumented thresholds;
- case-level TSCR/TLCR/TTAM can serve as a reproducible validation reference at the correct aggregation level.

### `PARTIAL`
Calibration itself is reproducible, but one or more cooling-rate quantities require case-specific emissivity/inflection or algorithm choices that are only partially documented, or official validation remains case-level only. / calibration은 재현되나 일부 냉각률 계산이 부분 문서화된 선택에 의존하거나 검증이 case-level로 제한된다.

### `HOLD`
Required calibration/time/transition semantics cannot be implemented without unsupported assumptions. / 필수 의미를 근거 없는 가정 없이 구현 불가.

## 8. Next Execution / 다음 실행

1. inspect all `mds2-2716` v1.3.1 PDR components for README, processing scripts, calibration records, and checksum companions;
2. search authoritative files for calibration equation, emissivity, solidification-inflection and cooling-rate algorithm details;
3. execute an outcome-blind calibration probe only if the formula is explicit;
4. compare reconstructed **case averages** to official TTAM/TSCR/TLCR without using optical geometry;
5. assign `PASS / PARTIAL / HOLD`.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and the snapshot-lineage gate. / 관련 규약 준수.
