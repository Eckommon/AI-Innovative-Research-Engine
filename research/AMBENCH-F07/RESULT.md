# AMBENCH-F07 Result / AMB2025-07 독립 공정조건 확장 source·identity 결과

**Issue / 이슈:** #21  
**Frozen gate / 고정 게이트:** **`PARTIAL_SOURCE_READY`**  
**Outcome-value use / outcome 값 사용:** none for gate decision / gate 판정에 미사용  
**Cost / 비용:** `COST-001` compliant — official public NIST metadata/documents only; no paid API/data/cloud/GPU and no large measurement download. / 공식 NIST 공개 metadata·문서만 사용.

## 1. Executive Result / 핵심 결과

**KO:** AMB2025-07은 D06 이후 필요한 **새로운 독립 공정조건 축**을 실제로 제공한다. NIST의 최신 상세 설명은 AMB2025-07이 bare IN718에서 `0.75 ms`와 `5.0 ms`의 두 turnaround/skywriting time을 사용하며, 각 조건에 3개 repeat plate가 있고 각 plate에 `5 mm × 5 mm`와 `1 mm × 5 mm` pad geometry가 있음을 명시한다. 또한 optical melt-pool cross-section measurement publication은 NIST PDR **`mds2-4103`**으로 직접 식별됐다. 그러나 현재 조사한 NIST의 공식 direct-data, data-publication 및 staff publication 경로에서는 대응하는 **raw/analysis-ready AMB2025-07 thermography measurement PDR publication**을 version-identifiable하게 특정하지 못했다. 따라서 exact thermal↔geometry paired manifest를 고정할 수 없으며, 사전등록 gate는 `PARTIAL_SOURCE_READY`다.

**EN:** AMB2025-07 genuinely provides a **new independent process-condition axis** relevant after D06. NIST's current detailed description specifies bare IN718 at two turnaround/skywriting times (`0.75 ms` and `5.0 ms`), with three repeat plates per turnaround condition and both `5 mm × 5 mm` and `1 mm × 5 mm` pad geometries on each plate. The optical melt-pool cross-section measurement publication is directly identifiable in the NIST PDR as **`mds2-4103`**. However, the current authoritative NIST direct-data, data-publication, and staff-publication routes investigated here do not yet provide a version-identifiable **raw/analysis-ready AMB2025-07 thermography measurement PDR publication**. The exact thermal↔geometry paired manifest therefore cannot be frozen, so the preregistered gate resolves to `PARTIAL_SOURCE_READY`.

## 2. Authoritative Source Findings / 권위 source 확인

### 2.1 Experiment design / 실험설계

NIST's AMB2025-06/07 detailed description (updated 2025-12-12) establishes: / NIST 상세설명
- primary laser power, speed, spot diameter, and hatch spacing are fixed;
- investigated variables include pad geometry and turnaround/skywriting time;
- AMB2025-07 uses bare plate with turnaround times `0.75 ms` and `5.0 ms`;
- the specimen naming convention covers `12 plates = 3 repeats × 4 conditions` across AMB2025-06/07;
- the AMB2025-07 bare-plate subset is represented by the three `0.75 ms` repeat plates and three `5.0 ms` repeat plates;
- each experiment includes the `5 mm × 5 mm` and `1 mm × 5 mm` pad geometries;
- pre-sectioning in-situ measurements omit the post-section `P#` suffix, while cross-section pieces use `P1..P3`.

**Derived independent-condition structure / 도출 독립조건 구조:** F07 contributes **2 turnaround-condition groups × 3 repeat plates**, with two pad geometries measured within the design. This is not equivalent to six unrelated process conditions; the independent process-condition count for the primary turnaround axis is `2`, with physical repeats nested within each condition. / row count를 독립조건 수로 과대계산하지 않는다.

### 2.2 Thermography semantics / 열화상 의미

The same NIST description confirms high-speed staring thermography was performed, including: / 열화상 수행 확인
- `48 kHz` frame rate;
- top-down imaging geometry;
- calibrated-temperature workflow using a high-temperature blackbody furnace;
- location-specific time-above-melting and cooling-rate measurement concepts;
- in-situ thermography on relevant samples, with AMB2025-07 challenge use on bare plates.

This establishes that the thermal modality exists experimentally. It does **not** establish that its raw/analysis-ready measurement files are presently available in a separately versioned public PDR publication. / modality 존재와 현재 public raw publication 존재는 구분한다.

### 2.3 Optical measurement publication / optical 측정 publication

A current NIST staff data-publication listing links:

`AM Bench 2025 Measurement Results Data: Optical Microscopy of arrays of adjacent laser tracks (pads) on alloy 718 plate`

The link resolves to NIST PDR identifier:

**`mds2-4103`**

The NIST listing describes cross-sectional microscopy and measurements for 2D arrays of laser tracks on solid IN718 plates and single powder layers. / IN718 pad cross-section microscopy·measurement dataset임을 공식 설명.

### 2.4 Calibration/challenge publication / calibration·challenge publication

Current NIST direct-data guidance identifies:

**`mds2-3707` — AMB2025-06 and AMB2025-07 Challenge Problem Calibration Data**

This is useful provenance/calibration context but is **not treated as a substitute for a missing raw thermography measurement publication**. / raw thermography 대체 금지.

## 3. Thermography Publication Search Boundary / thermography publication 조사 경계

Metadata-first searches were performed across current authoritative NIST routes including: / 조사 경로
- AM Bench direct-data guidance;
- AM Bench 2025 measurement/challenge pages;
- NIST `data-publications` indexed pages;
- relevant NIST staff data/software publication listings;
- NIST PDR-linked search results for AMB2025-07 thermography/time-above-melting/cooling-rate terms.

**Result / 결과:** no exact version-identifiable public raw/analysis-ready thermography PDR record was established during this gate. / exact thermography PDR 미확립.

Important epistemic boundary / 인식 경계:
- this is **`NOT_VERIFIED_PUBLICATION`**, not proof that NIST will never release or has not internally created the data;
- NIST itself states that additional AM Bench PDR datasets may be released as they become publicly available;
- therefore the correct classification is `PARTIAL_SOURCE_READY`, not a claim of permanent data absence.

## 4. Frozen Gate Application / 고정 게이트 적용

### `PASS_INDEPENDENT_EXPANSION_READY`
**FAIL / 미충족.** Experiment identity and optical PDR are strong, but exact public thermal measurement publication + deterministic thermal↔geometry manifest cannot yet be frozen. / thermal paired manifest 미확립.

### `PARTIAL_SOURCE_READY`
**PASS / 충족.** Authoritative experiment/calibration metadata are public, independent conditions are explicit, and an optical measurement PDR is public; exact raw thermal↔geometry paired measurement manifest remains incomplete/not verified. / 사전 정의와 정확히 일치.

### `HOLD_DATA_OR_IDENTITY_GAP`
Not selected / 미선택. The experiment/sample identity structure is sufficiently explicit that the candidate is not semantically ungrounded; the current gap is specifically the public thermal measurement publication. / 전체 identity 붕괴가 아니라 thermal publication gap.

### `REJECT_NO_INDEPENDENT_INFORMATION`
False / 아님. Turnaround time adds an explicit independent condition axis beyond the 2022 seven-case power/speed/spot representation. / 독립조건 축 존재.

**Final frozen gate / 최종:** **`PARTIAL_SOURCE_READY`**.

## 5. Interpretation Boundary / 해석 경계

Supported / 지지:
- AMB2025-07 is a strong future independent-information candidate;
- its experiment hierarchy is much better grounded than a simple row-count interpretation;
- optical geometry publication `mds2-4103` is publicly identifiable;
- raw/analysis-ready thermal measurement publication remains unresolved under current authoritative public evidence.

Not supported / 비지지:
- that AMB2025-07 would improve prediction;
- that AMB2025-07 validates E05;
- that optical and thermal files are already deterministically pairable;
- that unavailable-in-this-search means permanently unavailable;
- any use of challenge outcome values to optimize the F07 gate.

## 6. Decision Consequence / 후속 의사결정

Because F07 is `PARTIAL_SOURCE_READY`: / PARTIAL 후속
1. **do not open a predictive AMB2025-07 experiment yet**;
2. preserve `mds2-4103` and the explicit specimen hierarchy as qualified future assets;
3. periodically re-check for an authoritative AMB2025-07 thermography publication only when useful; no polling cost is authorized by this result;
4. move the active research queue to the next preregistered no-cost candidate with immediately available public measurement data: `mds2-3842` dynamic laser coupling, using an identity/information feasibility gate before any cross-dataset join;
5. do not infer BP4↔BP1 physical-track identity from nominal process-case similarity.

## 7. Cost & Reproducibility / 비용·재현성

No large raw measurement download or compute was necessary to decide F07. / 대용량 다운로드·계산 없이 판정.

- official public NIST sources only;
- no paid API/data/SaaS;
- no cloud/GPU/larger runner;
- no cost-bearing storage/artifact action;
- unknown future billing => `HOLD_COST_APPROVAL`.

**Disposition / 처리:** close Issue #21 as `COMPLETED — PARTIAL_SOURCE_READY`; retain AMB2025-07 as a future-qualified expansion candidate pending public thermal publication. / #21 PARTIAL로 종료·향후 thermal publication 시 재평가.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and frozen-gate controls. / 관련 규약 준수.
