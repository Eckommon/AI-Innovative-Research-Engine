---
id: AMBENCH-F10-RESULT
type: feasibility-result
state: COMPLETED_HOLD_PUBLICATION_NOT_VERIFIED
evidence_class: OBSERVED_DERIVED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F10/README.md
  - Issue #26
  - research/AMBENCH-POST-E09-TRIAGE.md
---

# AMBENCH-F10 Result — BP4 Coupling ↔ Same-BP4 Confocal Topography Source/Identity Feasibility
# AMBENCH-F10 결과 — BP4 coupling ↔ 동일 BP4 confocal topography 소스·식별자 실행가능성

**Frozen gate / 고정 판정:** **`HOLD_PUBLICATION_NOT_VERIFIED`**  
**Outcome access / outcome 접근:** `NEW_CONFOCAL_OUTCOME_BLIND = YES` maintained / confocal 수치값 미열람 유지  
**Cost / 비용:** `COST-001` compliant — public NIST/NIST-PDR/Data.gov/web metadata only; no paid route. / 추가 금전비용 0원.  
**Raw data / raw 데이터:** no confocal raw-data download required; `RAW-001` boundary preserved. / confocal raw 다운로드 없음.

## 1. Executive Result / 핵심 결과

**KO:** NIST의 공식 AMB2022-03 Version 1.01 문서는 `AMB2022-718-SH1-BP4`를 dynamic laser coupling single-track plate로 명시하고, coupling specimen들이 ex-situ laser scanning confocal microscopy로 측정되어 complete 3D surface profile이 취득됐다고 명확히 기록한다. 따라서 **동일 BP4의 distinct ex-situ topography measurement가 실제 수행됐다는 사실은 검증된다.** 그러나 현재 NIST의 공식 Direct AM Bench Data Links에서 AMB2022-03의 공개 PDR publication은 thermography `mds2-2716`, optical microscopy `mds2-2718`, microstructure `mds2-2775`, dynamic coupling `mds2-3842`만 직접 열거되며, F10 targeted search에서도 BP4 confocal/topography의 exact public PDR identifier, version/manifest, component checksum inventory 또는 deterministic 21-track map을 확립하지 못했다. 따라서 사전등록 gate는 `HOLD_PUBLICATION_NOT_VERIFIED`다.

**EN:** The official NIST AMB2022-03 Version 1.01 document explicitly identifies `AMB2022-718-SH1-BP4` as the single-track dynamic-laser-coupling plate and states that the coupling specimens were measured ex situ by laser scanning confocal microscopy to obtain complete 3D surface profiles. Thus, the **same-BP4 distinct ex-situ topography measurement is verified as having been performed**. However, the current official NIST Direct AM Bench Data Links list only thermography `mds2-2716`, optical microscopy `mds2-2718`, microstructure `mds2-2775`, and dynamic coupling `mds2-3842` as AMB2022-03 public PDR publications, and targeted F10 searches did not establish an exact public BP4 confocal/topography PDR identifier, version/manifest, component checksum inventory, or deterministic 21-track map. The preregistered gate is therefore `HOLD_PUBLICATION_NOT_VERIFIED`.

This is **not proof that the confocal data do not exist or can never become public**. It means an exact currently verifiable public measurement publication/component set was not established under the frozen F10 rules. / 이는 confocal 데이터의 영구 부재 증명이 아니라 현 시점의 exact 공개 publication 미확립이다.

## 2. Required Questions / 필수 질문 결과

| F10 question | Result | Evidence state |
|---|---|---|
| Exact authoritative public confocal publication? | **NOT VERIFIED** | `DATA_GAP` |
| Exact version/manifest recoverable? | **NO — publication identity missing** | `HOLD` |
| Component paths/sizes/checksums recoverable? | **NO — no qualified publication component set** | `HOLD` |
| Measurement semantics known? | **PARTIAL / YES at method level** — complete 3D surface profiles; steady-state height profiles, end-of-track mass accumulation/loss, chevron shape are described | `V2_PRIMARY_VERIFIED_METHOD` |
| Same specimen BP4 established? | **YES at measurement-description level** — `AMB2022-718-SH1-BP4` explicitly named | `V2_PRIMARY_VERIFIED` |
| Deterministic track/repeat mapping to 21 coupling tracks? | **NOT VERIFIED** | `DATA_GAP` |
| Maximum defensible join now? | **SPECIMEN-LEVEL ONLY as a measurement fact; no data join authorized** | `DERIVED_BOUNDARY` |
| Distinct physical information? | **YES** — ex-situ 3D surface topography, not coupling/process repackaging | `V2_PRIMARY_VERIFIED` |

## 3. Primary Official Evidence / 주요 공식 근거

### 3.1 NIST AMB2022-03 Version 1.01
The official measurement description states:
- half the bare-plate samples were processed with thermography and half with in-situ laser coupling;
- thermography samples were later cross-sectioned, while laser-coupling samples were measured using laser confocal microscopy;
- `AMB2022-718-SH1-BP4` is the **single-laser-track** coupling plate;
- BP4, BP5 and BP6 were measured ex situ by laser scanning confocal microscopy;
- complete 3D surface profiles were measured for steady-state height, track-end mass accumulation/loss, chevron-feature shape, and adjacent-track effects;
- the 2022 document stated that results/data would be released for model comparisons.

**Boundary:** the historical statement that the data *would be released* is not converted into evidence that an exact current public dataset is available.

### 3.2 Current NIST Direct AM Bench Data Links
The current authoritative guidance states that active AM Bench 2022 data links point to NIST PDR publications and that additional PDR datasets will be added as they become publicly available. Under AMB2022-03 it currently lists:
1. `mds2-2716` — thermography and scan strategy;
2. `mds2-2718` — optical microscopy;
3. `mds2-2775` — cross-sectional microstructure;
4. `mds2-3842` — dynamic laser coupling.

No BP4 confocal/topography PDR entry was established from this current official list.

### 3.3 Targeted publication/catalog search
F10 additionally searched current NIST/Data.gov-indexed material using combinations of:
- `AMB2022-718-SH1-BP4`;
- `AMB2022-03 surface topography`;
- `laser scanning confocal`;
- `3D surface profiles`;
- `IN718 laser tracks`;
- NIST PDR/Data.gov additive-manufacturing catalogs.

These searches recovered the measurement-description evidence and related 2024 AMB2022-03 papers, but did **not** establish an exact public BP4 confocal/topography PDR component set.

A 2024 NIST-authored microstructure paper discusses surface-topography behavior and states that complete optical and EBSD/EDS datasets are available via `mds2-2718` and `mds2-2775`; it does not identify a separate BP4 confocal PDR dataset in the material examined during F10.

## 4. Frozen Gate Application / 고정 gate 적용

### `PASS_SAME_BP4_TRACK_LEVEL_READY`
**FAIL** — exact authoritative public confocal publication, version/manifest, component checksums, and track/repeat mapping are not established.

### `PARTIAL_SAME_BP4_CASE_LEVEL_READY`
**FAIL** — this gate requires an established same-BP4 public source with usable measurement semantics. The measurement event is established, but the public source itself is not.

### `HOLD_PUBLICATION_NOT_VERIFIED`
**PASS** — official documentation states that confocal measurement occurred, but an exact public version-identifiable measurement publication/component set cannot be established.

### `HOLD_IDENTITY_OR_SEMANTIC_GAP`
Not selected because the blocker occurs **before** file-level identity/semantics: no qualified public publication/component set was established to inspect.

### `REJECT_NOT_SAME_BP4_OR_NOT_DISTINCT`
**FAIL** — official documentation supports same-BP4 measurement and distinct 3D topography; the branch is not scientifically rejected.

**Final / 최종:** **`HOLD_PUBLICATION_NOT_VERIFIED`**.

## 5. Interpretation Boundary / 해석 경계

Supported / 허용:
- BP4 was a dynamic-coupling single-track specimen and was measured ex situ by laser scanning confocal microscopy;
- the intended confocal observable is distinct 3D surface-topography/height information;
- a same-BP4 coupling↔confocal experiment remains scientifically attractive if a qualified public data publication and deterministic track identity become available;
- current public-source qualification is insufficient to authorize that experiment.

Not supported / 금지:
- claiming that BP4 confocal data are permanently unavailable;
- inferring a hidden PDR identifier;
- using paper figures as numerical confocal outcomes;
- substituting BP1 optical microscopy or another specimen for BP4 confocal data;
- pairing coupling tracks to confocal tracks by case labels alone;
- proceeding to coupling→topography modeling inside F10.

## 6. Consequence / 후속

Per frozen F10 consequence:
1. do **not** force or infer the same-BP4 confocal source;
2. move the immediate research queue to a **new separately preregistered within-BP4 dynamic-coupling temporal-information diagnostic**;
3. that fallback should test whether coupling waveforms preserve repeat-level information beyond process case using repeat-vs-case variance, temporal descriptors/effective dimension, and process association;
4. it must not claim physical-outcome utility without a same-specimen outcome dataset;
5. the same-BP4 confocal branch remains `HOLD` and can be re-opened only if an exact authoritative public publication becomes verifiable.

**Disposition / 처리:** close Issue #26 as `COMPLETED — HOLD_PUBLICATION_NOT_VERIFIED`; next work requires a new preregistration. / #26을 HOLD 결과로 완료 종료하고 후속은 새 사전등록으로 진행.
