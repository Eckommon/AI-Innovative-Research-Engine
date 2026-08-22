---
id: AMBENCH-F13-RESULT
type: feasibility-result
state: COMPLETED_PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F13/README.md
  - research/AMBENCH-F13/AMENDMENT-01.md
  - Issue #31
---

# AMBENCH-F13 Result — A-AMB2022-01 External Physical-Validation Source/Identity Feasibility
# AMBENCH-F13 결과 — A-AMB2022-01 외부 물리검증 source/identity feasibility

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`**

## 1. Executive result / 핵심 결과

**KO:** NIST A-AMB2022-01 `mds2-2525`는 BP4와 독립적인 재료·실험계에서 time-resolved absorptance와 high-speed X-ray melt-pool measurements를 동일 실험 계보에서 제공하며, aluminum stationary-spot challenge는 time-dependent absorption과 time-dependent melt-pool width를 각각 공개 result component로 제공한다. 따라서 향후 별도 사전등록 하에서 **same-experiment physical validation**을 수행할 수 있는 source 준비도는 확보됐다. 그러나 D12의 핵심인 repeat-level condition-specific variation을 직접 복제하려면 공개 component 수준의 repeat-resolved event identity가 필요하며, 현재 PDR inventory에서는 이를 충분히 확립하지 못했다. 따라서 full repeat-resolved PASS가 아닌 **PARTIAL**이다.

**EN:** NIST A-AMB2022-01 `mds2-2525` provides time-resolved absorptance and high-speed X-ray melt-pool measurements in material and experimental contexts independent of BP4, with simultaneous measurement provenance. The aluminum stationary-spot challenge publicly exposes separate result components for time-dependent absorption and time-dependent melt-pool width. This is sufficient source readiness for a future separately preregistered **same-experiment physical validation**. However, direct replication of D12's repeat-level condition-specific variation requires repeat-resolved public event identity, which is not sufficiently established in the current PDR component inventory. Therefore the gate is **PARTIAL**, not full repeat-resolved PASS.

## 2. Source lineage / source 계보

- DOI: `10.18434/mds2-2525`.
- PDR release history reports:
  - `v1.3.0` — data update;
  - `v1.3.1` — checksum/size metadata completed by curator;
  - `v1.3.2` — released 2026-01-07, described as `added to additiveman collection`.
- For component-level reproducibility, F13 freezes the checksum-rich `v1.3.1` data-bearing snapshot unless a future experiment independently verifies that the relevant component bytes/checksums are unchanged in `v1.3.2`.

Relevant verified `v1.3.1` component metadata:
- `Al_Spot_TDA_Results.csv` — time-dependent absorption, SHA-256 `3f0b6812f98535f5ffbb0e2fed31f084ad9a7f9cc393c04a43ed57f0bb14bf69`;
- `Al_Spot_TDW_Results.csv` — time-dependent width, SHA-256 `06b280222eab5f82eb9dcfb0689f20a5011c16e115548cd94ce120e5a97b4f5c`;
- `Al_Scan_TDA_v2_Results.csv` — time-dependent absorption, SHA-256 `3af3478b463b867ed3c78ef6e60c75f9d613607b236933f3f9df08113884a6a8`;
- `Al_Scan_AA_MWD_ASR_Results.csv` — scan summary absorption/geometry/solidification result, SHA-256 `d3732fcddaaee046105aa90eb82547ffd0fe61edb425fc1e8f019c6f73ed0b4d`;
- `Spot on Bare Metal_Calibrated Absorption Data.csv` — time-dependent Ti-6Al-4V training absorption plus camera/frame timing, SHA-256 `0e96b220852d762fde846e406cc44c6fc874cef22e7e41db7f4025dbcc9ca274`;
- `Scan on Bare Metal_Calibrated Absorption Data.csv` — scanned Ti-6Al-4V training absorption plus camera/frame timing, SHA-256 `1c64f24e84c274d9f9ae27fb09e79b86cda2fda5bee4b67da3567c8a59ca499d`.

No numeric CSV outcome values were downloaded or analyzed under F13.

## 3. External independence / 외부 독립성

BP4 / `mds2-3842`:
- bare IN718;
- hemispherical-reflectometer-derived dynamic coupling;
- AMMT;
- 7 process cases × 3 repeats;
- 100 kHz coupling records.

A-AMB2022-01 / `mds2-2525`:
- Ti-6Al-4V training and Al 5182 challenge materials;
- integrating-sphere radiometry / dynamic absorptance;
- Advanced Photon Source experiment with high-speed X-ray imaging;
- stationary and scanned configurations;
- absorptance time resolution documented as 40 ns; X-ray frames at 50,000 fps in the aluminum challenge publication.

Therefore the candidate is materially independent of BP4 in material, measurement system, facility/context, and process condition.

## 4. Same-experiment physical pairing / 동일실험 물리 pairing

Official NIST challenge documentation and the 2024 benchmark publication state that integrating-sphere radiometry and high-speed X-ray imaging were combined so that absolute laser absorption and projected melt-pool images were recorded simultaneously.

For aluminum stationary spot:
- challenge structure includes time-dependent absorption (`TDA`) and time-dependent width (`TDW`);
- the benchmark publication explicitly presents an X-ray melt-pool image corresponding to a point in the absorption time series;
- PDR exposes `Al_Spot_TDA_Results.csv` and `Al_Spot_TDW_Results.csv` as separate result components.

This is sufficient to establish a qualified same-experiment/same-condition physical-validation branch for a future preregistration.

## 5. Repeat-resolution finding / repeat 해상도 결과

The 2024 benchmark publication reports that scanned aluminum measurements were repeated three times under identical conditions and that averages were used for final simulation comparison. It also discusses repeated stationary absorptance measurements.

However, the current public PDR component inventory exposed in the checksum-rich snapshot does not clearly provide three separately identified aluminum repeat event files linking repeat-level absorptance and repeat-level geometry as independent authoritative records.

Therefore:
- **experimental repeats existed** — supported;
- **repeat-resolved public event identity adequate to replicate D12** — `NOT_VERIFIED`.

F13 must not infer individual repeat identity from averaged/chosen challenge outputs.

## 6. Measurand boundary / measurand 경계

A-AMB `dynamic absorptance` and BP4 `dynamic laser coupling` are closely related laser-energy interaction measurements but are not treated as numerically interchangeable:
- A-AMB uses integrating-sphere radiometry and reports absorbed power/relative absorption;
- BP4 uses reflected-power-derived coupling from a calibrated hemispherical reflectometer.

A future experiment may compare **temporal morphology concepts** only after separately freezing normalization and descriptor-transfer rules.

## 7. Outcome-blindness correction / outcome-blindness 정정

See `AMENDMENT-01.md`.

Before F13 preregistration, the source-triage search exposed publication-level aggregate scanned-aluminum geometry values. Therefore:

`NEW_EXTERNAL_OUTCOME_BLIND = NO — PUBLICATION_LEVEL_AGGREGATES_PREOBSERVED`.

No numerical PDR result CSV was accessed and no F13 gate criterion uses those aggregate values.

## 8. Frozen gate application / 고정 gate 적용

### `PASS_REPEAT_RESOLVED_EXTERNAL_VALIDATION_READY`
- reproducible source/components: PASS;
- external independence: PASS;
- same-experiment physical pairing: PASS;
- deterministic time semantics: PASS at source-design level;
- >=3 separately identifiable repeated measurements with absorptance and physical outcome at repeat level: **FAIL / NOT_VERIFIED**.

Result: **FAIL**.

### `PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`
- authoritative reproducible source/components: PASS;
- external material/condition independence: PASS;
- same-experiment/same-condition absorptance + physical outcome provenance: PASS;
- time-resolved pairing or qualified physical outcome can be defined: PASS;
- repeat-resolved public identity insufficient for direct D12 replication: PASS.

Result: **PASS**.

Other HOLD/REJECT gates do not apply.

## 9. Final / 최종

**`PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`**

## 10. Consequence / 후속

The next eligible experiment is **not** a repeat-level D12 replication. The strongest qualified branch is a separately preregistered, low-degree-of-freedom **A-AMB aluminum stationary-spot time-resolved absorptance ↔ time-dependent melt-pool-width morphology test**, with explicit acknowledgment that it is a single-/aggregate-event external physical-validation study rather than repeat-level generalization.

Before numeric CSV access, that experiment must freeze:
- exact `v1.3.1` component checksums (or independently verified unchanged `v1.3.2` bytes);
- time-zero and time alignment rules;
- resampling resolution;
- absorptance normalization;
- a very small descriptor set derived from D11/D12 concepts without tuning;
- geometry endpoint transformation;
- exact null/comparison statistics and gate;
- protection against using preobserved publication-level aggregate scan values.

No high-capacity model is authorized by F13.
