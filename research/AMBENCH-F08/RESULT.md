---
id: AMBENCH-F08-RESULT
type: feasibility-result
state: COMPLETED
outcome: PARTIAL_CASE_LEVEL_READY
region: us
domain: manufacturing
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F08/README.md
  - Issue #22
  - GitHub Actions Run 32544237853
---

# AMBENCH-F08 Result — `mds2-3842` Dynamic Laser Coupling Identity & Information Feasibility / 동적 레이저 결합 식별자·정보이득 가능성 결과

**Frozen gate outcome / 고정 게이트 결과:** **`PARTIAL_CASE_LEVEL_READY`**  
**Execution evidence / 실행 근거:** GitHub Actions Run `32544237853` (`success`) plus official NIST AMB2022-03 measurement/challenge documentation.  
**Outcome-blind boundary / outcome 비사용:** coupling time-series ZIP was **not downloaded**; no coupling values, BP1 optical outcomes, or thermography outcomes were used to choose the relationship level or gate.

## 1. Executive Conclusion / 핵심 결론

**KO:** `mds2-3842`는 공개·version-identifiable·checksum-recorded NIST PDR 데이터셋이며, 열화상과 다른 물리량인 **time-resolved laser coupling / reflected-power-derived coupling**을 제공한다. 따라서 `REJECT_REDUNDANT_INFORMATION`은 아니다. 그러나 BP1 thermography/optical single tracks와 BP4 dynamic-coupling tracks는 공식 문서상 **서로 다른 bare plate specimens**이고, 동일 case label에서도 spot diameter 등 실제 processing condition이 다르다. 또한 PDR summary에는 case `3.2`의 third-repeat filename이 second-repeat filename과 중복되는 source-internal inconsistency가 있다. 따라서 exact physical-track 또는 cross-BP repeat pairing은 정당화되지 않으며, 허용 가능한 관계는 **unpaired nominal case-family / aggregate relationship with explicit process-parameter differences**뿐이다.

**EN:** `mds2-3842` is a public, version-identifiable, checksum-recorded NIST PDR dataset providing a physically distinct observable: **time-resolved laser coupling derived from reflected laser power**. It therefore is not redundant with the thermography representation. However, official NIST documentation identifies BP1 thermography/optical single tracks and BP4 dynamic-coupling tracks as **different bare-plate specimens**, and actual processing conditions differ even under matching case labels, especially beam diameter. The PDR summary also contains a source-internal inconsistency in the case `3.2` third-repeat filename. Exact physical-track or cross-BP repeat pairing is therefore unsupported. The defensible relationship level is an **unpaired nominal case-family / aggregate relationship with explicit process-parameter differences**.

## 2. Version & Manifest / 버전·manifest

Current official PDR endpoint / 현행 PDR:
- dataset: `mds2-3842`
- DOI: `10.18434/mds2-3842`
- title: `Dynamic Laser Coupling of Scanned Single Tracks on Bare IN718 with Varying Beam Diameter, Scan Speed, and Power`
- current version: **`1.0.3`**
- `modified`: `2025-05-22`
- `revised`: `2025-07-16T12:24:39.233174`
- current endpoint raw JSON SHA-256: `673d9fbcc345e75f8bfda18f9753b35c77aa77ea78a7ed66289596028e265e69`
- exact version ID: `ark:/88434/mds2-3842/pdr:v/1.0.3`
- exact v1.0.3 manifest SHA-256: `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb`
- current and exact-v1.0.3 component maps: **identical**.

Tested official version lineage / 시험한 공식 version 계보:

| Version | Version-specific manifest SHA-256 | Components |
|---|---|---:|
| `1.0.0` | `45e91a932dde911ced679271c5a7b6f5177c0c48bc32449959523e0ffd5be6b5` | 3 |
| `1.0.1` | `7d6626b30620ca6d1c63444bed07b3290ee68d91b93d163c284563e734754e73` | 3 |
| `1.0.2` | `24586bc9d5f31e64236e151e474d0800bfaf76da598b2b9b111f9c346dec00a5` | 3 |
| `1.0.3` | `b3fb55e489568f90fddcbaf8a7f790e8b2a15483f312bdc403f4d08f4419c1cb` | 3 |

Across `1.0.0 → 1.0.3`, no component filepath, size, or component checksum changed in the tested manifests. / 시험 범위에서 component path·size·checksum 변경 없음.

**Snapshot assessment / snapshot 평가:** `reproduction_risk = LOW` for the PDR publication itself. / PDR 자체 snapshot 재현위험 낮음.

## 3. Files & Checksums / 파일·checksum

Current v1.0.3 components / 현행 component:

| File | Bytes | PDR SHA-256 | Byte verification in F08 |
|---|---:|---|---|
| `3842_README.txt` | `7,469` | `50d24d8dc85cd9075c774c3363c5dbbf1a0a769c4349979d82c76fa6b9b906be` | **PASS — actual bytes match PDR** |
| `dynamic_laser_coupling_data.zip` | `93,566` | `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66` | **NOT DOWNLOADED — outcome-blind boundary** |
| `summary_of_data_files.csv` | `496` | `abf339b8a2b36b69bc11a31e4600a3cc845dd4f705b6a96a7a543e990824f3b4` | **PASS — actual bytes match PDR** |

The ZIP's checksum is authoritative PDR metadata but was not independently byte-verified in F08 because the archive contains the coupling time series. / ZIP hash는 공식 PDR metadata이나 outcome-blind 경계상 실제 bytes 검증은 하지 않음.

## 4. Measurement Variable Semantics / 측정변수 의미

Official `3842_README.txt` defines / 공식 README 정의:

- laser coupling `P_lc` = portion of applied laser power **not reflected** from the material;
- equation: `P_lc = 1 - P_rho / P_app`;
- `P_rho` = measured reflected laser power;
- `P_app` = applied laser power;
- `P_lc` is **unitless**, nominal range `0–1`;
- the README calls coupling an **approximation of laser absorption**, not identical to absorption, because other mechanisms such as plume absorption may contribute;
- acquisition uses a **calibrated integrating hemisphere** measuring total reflected power;
- sampling rate: **100 kHz**;
- each track data file: first column = **time from track initiation [ms]**; second column = **instantaneous laser coupling**.

This is physically distinct from BP1 thermography, whose observable is optical thermal-camera signal/apparent temperature used for thermal histories, cooling-rate/time-above-melt quantities. / 열화상과 다른 에너지 반사·결합 관측량이다.

**Distinct-information finding / 독립 물리정보 판정:** `YES — DISTINCT_PHYSICAL_MODALITY`.

## 5. Case & Repeat Identifier Semantics / case·repeat 식별자

The PDR README states seven combinations of beam diameter, scan speed, and power, with each track repeated twice after the first measurement, giving **three tracks per combination = 21 tracks**. / 7조건 × 3 tracks = 21.

`summary_of_data_files.csv` supplies this schema:
- `Case Number`
- `Laser Power [W]`
- `Scan Speed [mm/s]`
- `Spot size, D4σ [μm]`
- `Line 1`
- `Line 2 (repeat of line 1)`
- `Line 3 (repeat of line 1)`

Metadata-only mapping / outcome 미사용 filename mapping:

| Case | P [W] | v [mm/s] | D4σ [µm] | Line 1 | Line 2 | Line 3 |
|---|---:|---:|---:|---|---|---|
| `0` | 285 | 960 | 110 | `0_1sv.txt` | `0_2sv.txt` | `0_3sv.txt` |
| `1.1` | 285 | 960 | 76 | `1_1_1sv.txt` | `1_1_2sv.txt` | `1_1_3sv.txt` |
| `1.2` | 285 | 960 | 131 | `1_2_1sv.txt` | `1_2_2sv.txt` | `1_2_3sv.txt` |
| `2.1` | 285 | 1200 | 110 | `2_1_1sv.txt` | `2_1_2sv.txt` | `2_1_3sv.txt` |
| `2.2` | 285 | 800 | 110 | `2_2_1sv.txt` | `2_2_2sv.txt` | `2_2_3sv.txt` |
| `3.1` | 325 | 960 | 110 | `3_1_1sv.txt` | `3_1_2sv.txt` | `3_1_3sv.txt` |
| `3.2` | 245 | 960 | 110 | `3_2_1sv.txt` | `3_2_2sv.txt` | **`3_2_2sv.txt` (source record)** |

### Source-internal repeat conflict / 원천 내부 repeat 충돌

The case `3.2` row records **the same filename** for Line 2 and Line 3. / Line2·Line3 filename 중복.

- Do **not** silently change the third filename to `3_2_3sv.txt`.
- Exact third-repeat file identity for case `3.2` = **`CONFLICT / UNKNOWN`** until authoritative clarification or non-outcome file-level evidence resolves it.
- Because component checksums are unchanged across tested v1.0.0–v1.0.3 manifests, the tested PDR lineage does not remove this summary-file inconsistency. / tested lineage에서 summary component가 변하지 않아 현재 계보만으로는 해소되지 않음.

## 6. BP1 ↔ BP4 Alignment / BP1↔BP4 정렬 수준

Official AMB2022-03 documentation explicitly separates the specimens / 공식 문서상 시편 분리:
- `BP1` = bare plate #1, `3×7` single tracks, **in situ thermography**;
- `BP4` = bare plate #4, `3×7` single tracks, **in situ dynamic laser coupling**;
- half the bare plates were processed with thermography and half with coupling; thermography specimens were later cross-sectioned while coupling specimens were characterized by confocal microscopy.

Therefore / 따라서:
- **physical specimen identity:** `NO`;
- **exact track identity:** `NO / NOT AUTHORIZED`;
- **cross-BP repeat pairing:** `NOT ESTABLISHED`;
- matching `repeat 1/2/3` labels must not be interpreted as the same physical experiment.

### Nominal case-family relationship, not identical process conditions / 동일 조건이 아닌 nominal case-family 관계

BP1 and BP4 reuse case labels `0`, `1.1`, `1.2`, `2.1`, `2.2`, `3.1`, `3.2` and preserve the same power/speed perturbation pattern, but the actual parameter vectors are not identical. Most importantly:

| Case family | BP1 thermography D4σ [µm] | BP4 coupling D4σ [µm] |
|---|---:|---:|
| `0` / speed / power variants | 67 | 110 |
| `1.1` | 49 | 76 |
| `1.2` | 82 | 131 |

The official challenge document explicitly states dynamic-coupling measurements used the same laser-processing parameter pattern **except for a different laser diameter**. Other setup details also differ, including scan direction and documented gas/pressure/incidence conditions. / case label만으로 동일 공정조건 취급 금지.

**Supported alignment level / 허용 정렬수준:**  
**`UNPAIRED_NOMINAL_CASE_FAMILY / AGGREGATE_ONLY`** — any later analysis must carry the actual BP1 and BP4 process parameter vectors and may not call the rows paired tracks, paired repeats, or identical process conditions.

## 7. Additional Provenance Conflict / 추가 provenance 충돌

The current `3842_README.txt` states sample surface roughness `Ra = 0.15 µm`, while the 2022 AMB2022-03 challenge document Table 3 lists dynamic-coupling surface roughness `Ra = 5.8 µm`. / 현행 README와 2022 challenge 문서가 다름.

**State:** `ACTIVE_SOURCE_CONFLICT — CAUSE UNKNOWN`.  
Do not average, select one silently, or rewrite either value. A later analysis sensitive to surface roughness must resolve this conflict first. / roughness 민감 분석 전 별도 해결 필요.

## 8. Frozen Gate Application / 고정 gate 적용

| Gate | Result | Reason / 근거 |
|---|---|---|
| `PASS_DISTINCT_MODALITY_READY` | **NOT MET** | distinct modality and reproducible PDR pass, but complete deterministic repeat-file semantics and stronger BP1 alignment are not established; source conflicts remain. |
| `PARTIAL_CASE_LEVEL_READY` | **MET** | public reproducible distinct modality; seven-case/three-repeat design is authoritative; BP1 physical identity is absent and only unpaired case-family/aggregate relation is defensible. |
| `HOLD_IDENTITY_OR_SEMANTIC_GAP` | not selected | enough semantics exist for a constrained aggregate/case-family feasibility path. |
| `REJECT_REDUNDANT_INFORMATION` | false | dynamic coupling measures reflected-power-derived energy coupling, not thermographic temperature/occupancy. |

**Final / 최종:** **`PARTIAL_CASE_LEVEL_READY`**.

## 9. Consequence / 후속 결정

Eligible / 허용:
- preserve `mds2-3842` as a **qualified distinct-modality source**;
- separately preregister an **unpaired case-family/aggregate** relationship test, explicitly carrying both datasets' process parameters and treating spot-size/setup differences as domain shift/covariates;
- use coupling only after that new hypothesis freezes its aggregation, estimator, and non-causal interpretation.

Not eligible / 금지:
- BP1↔BP4 direct track join;
- BP1 repeat `1/2/3` ↔ BP4 repeat `1/2/3` pairing;
- pretending matching case labels have identical spot size/process conditions;
- silently correcting case `3.2` repeat filename;
- interpreting coupling as exact absorbed energy without the README caveat;
- using surface roughness as a harmonized variable until the `0.15 µm` vs `5.8 µm` conflict is resolved;
- any predictive/causal claim from F08 itself.

## 10. COST-001 / 비용 준수

- public repository standard `ubuntu-latest` only;
- official public NIST PDR inputs;
- no GPU/larger runner;
- no paid API/data/cloud/SaaS;
- no artifact upload;
- `dynamic_laser_coupling_data.zip` not downloaded;
- no coupling time-series values or BP1 outcome values inspected.

**Incremental monetary cost / 추가 금전비용:** `0` under the verified project execution boundary.

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001`, and the preregistered F08 frozen gate. / 관련 규약 준수.
