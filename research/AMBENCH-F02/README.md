---
id: AMBENCH-F02
type: feasibility
state: COMPLETED_PASS
evidence_class: VALIDATED
region: us
domain: manufacturing
tags:
  - type/feasibility
  - state/validated
  - evidence/validated
  - region/us
  - domain/manufacturing
  - domain/additive-manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-001/README.md
  - docs/METADATA_SCHEMA.md
---

# AMBENCH-F02 — Raw Snapshot & Replicate Alignment Feasibility / AM Bench raw snapshot·반복 정렬 검증

**Issue / 이슈:** #11  
**State / 상태:** `COMPLETED — PASS`  
**Evidence run / 증거 Run:** GitHub Actions `32535986814`  
**Parent calibration / 상위 보정:** `AMBENCH-001`

## 1. Research Question / 연구 질문

**KO:** NIST AMB2022-03의 exact PDR snapshot과 raw identifier 체계만으로 thermography 3회 반복 track과 optical specimen/cross-section outcome을 어느 해상도까지 **추정 없이** 정렬할 수 있는가?  
**EN:** Using only exact NIST AMB2022-03 PDR snapshots and authoritative raw identifiers, to what resolution can three thermography repeat tracks be aligned with optical specimen/cross-section outcomes **without inference**?

## 2. Frozen Sources / 고정 소스

| Role | NIST PDR | DOI |
|---|---|---|
| thermography / 열화상 | `mds2-2716` | `10.18434/mds2-2716` |
| optical microscopy / 광학현미경 | `mds2-2718` | `10.18434/mds2-2718` |

Official NIST AMB2022-03 challenge documentation is used only to interpret experiment identity and published measurement design. / 공식 challenge 문서는 실험 ID·측정설계 해석에만 사용한다.

## 3. Frozen Relationship / 고정 관계

```text
process case
→ thermography track/repeat identity
→ optical specimen/cross-section identity
→ melt-pool depth/width outcome
```

The frozen rule that shared case identity alone is insufficient was preserved. The PASS is based on explicit line/repeat identifiers in the raw-source documentation and optical measurement workbook, not on case-number inference. / 공통 case ID만으로는 불충분하다는 고정 규칙을 유지했으며, 이번 PASS는 case 번호 추정이 아니라 raw-source 문서와 optical 측정 workbook의 명시적 line/repeat 식별자에 기반한다.

## 4. Snapshot & Version Lineage / Snapshot·버전 계보

### Thermography `mds2-2716`

All tested version-specific PDR manifests remain directly recoverable from the official NIST PDR endpoint. / 시험한 version-specific PDR manifest 모두 공식 NIST PDR에서 직접 복구 가능하다.

| PDR version | Components | Manifest SHA-256 |
|---|---:|---|
| `1.1.0` | 5 | `9ebfb0736f99075cf45a61f76fc972a51832adde0a1ecf94cdfbe711ab912758` |
| `1.2.0` | 5 | `b5f071524dcc77113bda51d2798793ef6910cebf8346ef16a07e3a6c40110c30` |
| `1.3.0` | 11 | `c9a3ca4d39d29055c74822d90093d1ebd3f5605e52e498755cafdfde71142d18` |
| `1.3.1` | 11 | `14fcd868704059cb5464e1d5421f21ac2d5023643a9eb12466db58307953199f` |

`1.2.0 → 1.3.0` added the thermography and scan-strategy distributions; no component additions/removals/content-hash changes were detected between `1.3.0` and `1.3.1`. / `1.2.0 → 1.3.0`에서 thermography·scan-strategy 배포물이 추가됐고 `1.3.0 → 1.3.1`에서는 component 추가·삭제·content hash 변경이 관측되지 않았다.

Authoritative checksum companions / 공식 checksum companion:
- thermography HDF5 `AMB2022-03-718-AMMT-StaringCamera_Signal.h5`: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`
- scan-strategy HDF5 `AMB2022-03-AMMT-718-Pad_XYPT.h5`: `7b7004753e150bc26632e9ce356e0440429160fa92cbff8fc8559202fdce2103`

### Optical microscopy `mds2-2718`

| PDR version | Components | Manifest SHA-256 |
|---|---:|---|
| `1.0.0` | 211 | `52d057004e5f8f9d2c3b8bc3deb1042c5f3cc8357bda491e01a761a4f6163ba5` |
| `1.0.1` | 211 | `160b222e30681ebf057d7c4194b1b26395824bd8ac62fa020aa7d5f087627ccc` |
| `1.0.2` | 211 | `37ed2c380e8fc1a112b04bb5a0111d9f19e7fc67546db0d6097d75d56f8bb676` |
| `1.0.3` | 211 | `62db1fe685b9d2984260542538c9cb87eba65decf01c77a904c7ce191693e234` |

No component additions, removals, or component hash/size changes were detected across the tested `1.0.0 → 1.0.3` manifests. / 시험한 `1.0.0 → 1.0.3` manifest에서 component 추가·삭제·hash/size 변경은 관측되지 않았다.

Official optical measurement workbook / 공식 optical 측정 workbook:
- file: `AMB2022-718-SH1-MeltPool_Cross-Section_Measurement_Results.xlsx`
- bytes: `25,811`
- SHA-256: `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`
- downloaded-file hash = NIST `.sha256` companion = PDR metadata checksum: **exact 3-way match / 3중 정확 일치**.

### Lineage qualification / 계보 판정

| Field | `mds2-2716` | `mds2-2718` |
|---|---|---|
| `historical_version_retention` | `MULTI_VERSION_OFFICIAL` | `MULTI_VERSION_OFFICIAL` |
| `snapshot_recoverability` | `DIRECT_OFFICIAL` | `DIRECT_OFFICIAL` |
| `archive_or_mirror_status` | `OFFICIAL_PDR_VERSIONED` | `OFFICIAL_PDR_VERSIONED` |
| `reproduction_risk` | `LOW` | `LOW` |

README-internal citation text may still display the original publication version; authoritative version-specific PDR manifests are therefore used for snapshot lineage rather than assuming README prose alone represents the current PDR version. / README 내부 인용문은 최초 출판 버전을 표시할 수 있으므로 현재 PDR 버전은 README 문구가 아니라 version-specific PDR manifest로 고정한다.

## 5. Authoritative Identifier Semantics / 권위 식별자 의미

### Thermography / 열화상
NIST README defines HDF5 groups `/ThermalData/Line_X_Y_Z/` as individual laser tracks, with:
- `X` = set,
- `Y` = subset,
- `Z` = **one of three repeats for each line**.

Each group contains raw thermographic `Signal` plus laser-power, scan-speed and spot-size attributes. / 각 group은 raw thermographic `Signal`과 laser power·scan speed·spot size 속성을 포함한다.

### Optical microscopy / 광학현미경
NIST README defines single-track micrograph names as:

```text
AMB2022-718-SH1-BP#-P#-L#-#.tiff
```

where `L#` is the track case and the final `#` is the **track number**. Example: `AMB2022-718-SH1-BP1-P1-L2.2-1.tiff`. / `L#`는 track case, 마지막 `#`는 track number다.

The authoritative optical XLSX records `Case and Line No.` values such as `Line 0_1`, `Line 0_2`, `Line 0_3`, `Line 1.1_1`, ..., `Line 3.2_3`, and records measured depth/width for each line identity. / 공식 XLSX가 각 line identity별 depth/width를 기록한다.

## 6. Alignment Matrix / 정렬 행렬

Canonical normalized line identity / 정규화 line ID:

| process_case | repeat | thermo identity semantics | optical line identity | optical cross-sections | evidence | alignment_state |
|---|---:|---|---|---:|---|---|
| `0` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 0_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `0` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 0_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `0` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 0_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.1` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 1.1_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.1` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 1.1_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.1` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 1.1_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.2` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 1.2_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.2` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 1.2_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `1.2` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 1.2_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.1` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 2.1_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.1` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 2.1_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.1` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 2.1_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.2` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 2.2_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.2` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 2.2_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `2.2` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 2.2_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.1` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 3.1_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.1` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 3.1_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.1` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 3.1_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.2` | 1 | `Line_X_Y_Z`, `Z=1` | `Line 3.2_1` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.2` | 2 | `Line_X_Y_Z`, `Z=2` | `Line 3.2_2` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |
| `3.2` | 3 | `Line_X_Y_Z`, `Z=3` | `Line 3.2_3` | 2 | NIST README + XLSX | `EXACT_TRACK_ID` |

**Multiplicity rule / 다중성 규칙:** each exact thermography line/repeat corresponds to the same exact optical line identity, but the optical workbook contains two spatial cross-section measurements for each single-track line. These are **nested spatial outcomes within one track**, not additional thermography repeats. / 각 thermography line/repeat에는 동일 optical line ID가 대응되지만 optical workbook에는 line당 2개 공간 단면 측정이 존재한다. 이 둘은 추가 thermography 반복이 아니라 동일 track 내부의 nested spatial outcome이다.

## 7. Frozen Gate Result / 고정 게이트 결과

### `PASS`

The pre-defined PASS condition is satisfied. Official NIST identifier semantics establish a reproducible mapping at **track/repeat level** from thermography `Line_X_Y_Z` identities to optical line identities and their measured cross-sections. No shared-case-only inference is required. / 사전 PASS 조건을 충족했다. NIST 공식 식별자 의미를 통해 thermography `Line_X_Y_Z`와 optical line·단면 측정 사이의 **track/repeat 수준** 대응이 재현 가능하며 shared-case만을 이용한 추정은 필요하지 않다.

## 8. Downstream Modeling Constraint / 후속 모델링 제약

A raw-level controlled experiment is now justified, but only under the following constraints: / raw-level 통제실험은 정당화되지만 다음 제약을 따른다.

1. join on exact normalized `case + line/repeat` identity; / exact `case + line/repeat` ID로 조인;
2. do not treat two optical cross-sections as two independent thermography observations; / 두 optical 단면을 독립 thermography 관측으로 간주 금지;
3. use track-level aggregation (e.g. mean + spread) or an explicit hierarchical/nested target model; / track-level 집계 또는 hierarchical/nested target 사용;
4. split validation by **process case**, not random row split, to prevent repeat leakage; / repeat leakage 방지를 위해 random row가 아닌 process-case 단위 검증;
5. start with low-capacity interpretable features/baselines because only 21 single-track identities are available. / 21개 single-track ID이므로 저용량·해석가능 baseline부터 시작.

## 9. Decision / 판단

**Feasibility:** `PASS`  
**Snapshot lineage:** `DIRECT_OFFICIAL / LOW_RISK`  
**Permitted downstream resolution:** `TRACK_REPEAT_LEVEL_WITH_NESTED_OPTICAL_OUTCOMES`  
**High-capacity ML:** `NOT_AUTHORIZED_BY_THIS_GATE`

Issue #11 may be closed as completed. The next research step may freeze a separate raw track-level controlled experiment before any model is fitted. / Issue #11은 완료 종료 가능하며 다음 연구단계에서는 모델 fitting 전에 별도 raw track-level 통제실험을 사전고정한다.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and the v0.3 snapshot-lineage gate. / 관련 규약 준수.
