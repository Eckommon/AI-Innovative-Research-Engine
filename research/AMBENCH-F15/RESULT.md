---
id: AMBENCH-F15-RESULT
type: feasibility-result
state: COMPLETED_PARTIAL_REGISTERED_SCHEMA_READY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F15/README.md
  - Issue #33
---

# AMBENCH-F15 Result — `mds2-3761` Registered In-Situ ↔ XCT External-Validation Feasibility
# AMBENCH-F15 결과 — `mds2-3761` 등록형 in-situ ↔ XCT 외부검증 feasibility

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_REGISTERED_SCHEMA_READY`**

## 1. Executive result / 핵심 결과

**KO:** NIST `mds2-3761`은 4개 nominally identical LPBF part를 대상으로 part당 250개 layer CSV와 40개 등록 feature를 제공하며, 각 row는 XYPT command position을 기준으로 command/real laser variables, in-situ melt-pool characteristics, layerwise optical intensity, ex-situ XCT voxel values를 동일 machine-coordinate framework에 등록한다. 따라서 후속 process–structure 검증을 위한 **schema/registration 준비도는 강하게 확보**된다. 다만 현재 세션의 검증 가능한 0원 경로에서는 `part1.zip`~`part04.zip`의 exact release/version, component checksum 또는 equivalent immutable integrity evidence, actual archive-byte inventory를 확립하지 못했다. 따라서 point-level numerical validation full PASS가 아니라 `PARTIAL_REGISTERED_SCHEMA_READY`다.

**EN:** NIST `mds2-3761` provides 250 layer CSV files per each of four nominally identical LPBF parts and 40 registered features per measured point. Rows register commanded/real laser variables, in-situ melt-pool characteristics, layerwise optical intensity, and ex-situ XCT voxel values to an XYPT-referenced machine-coordinate framework. This strongly establishes schema/registration readiness for later process–structure validation. However, the current verified zero-cost routes did not establish exact release/version lineage, component checksums or equivalent immutable integrity evidence, or actual archive-byte inventories for `part1.zip` through `part04.zip`. Therefore the full point-level numerical-validation PASS is not authorized; the frozen gate is `PARTIAL_REGISTERED_SCHEMA_READY`.

## 2. Authoritative source / 권위 source

- PDR identifier: `ark:/88434/mds2-3761`.
- Data.gov/NIST public dataset first published 2025-05-09; metadata modified 2025-03-13.
- NIST AMS 100-69, May 2025, DOI `10.6028/NIST.AMS.100-69`.
- Public components listed:
  - `part1.zip`
  - `part02.zip`
  - `part03.zip`
  - `part04.zip`
- Original in-situ dataset: `mds2-2233`.
- Original ex-situ XCT dataset: `mds2-2291`.

## 3. Experimental structure / 실험 구조

NIST AMS 100-69 states:
- four nominally identical parts were produced within one build;
- material, scan strategy, and laser processing parameters were held consistent by design;
- each part is approximately `5 mm × 5 mm × 9 mm` and contains `250` layers;
- scan sequence progresses Part 1 → Part 4 within each layer.

This gives a replicated-part structure, but F15 does not yet authorize treating rows, layers, or parts as statistically independent experimental replicates.

## 4. Deterministic data hierarchy / 결정론적 데이터 계층

Official schema states:
- four folders, one per part;
- each folder contains 250 CSV files, one per layer;
- each CSV has 40 columns and multiple rows;
- each row represents a measured point with all associated registered features.

Thus the maximum **documented** join resolution is point/row level. The maximum **currently authorized numerical** join resolution remains `NONE` until immutable component integrity is established.

## 5. Registered feature relationship / 등록 feature 관계

Key point-level variables documented by NIST include:
- part number;
- synchronized build time (`µs`);
- commanded laser X/Y position, power, scan speed;
- real laser X/Y position, power, scan speed from DAQ;
- in-situ melt-pool length, width, and area at thresholds 80/100/120;
- layerwise image intensity under multiple LEDs and filters;
- ex-situ XCT voxel value, 3×3×3 mean-filtered XCT, and 5×5×5 mean-filtered XCT.

The dataset therefore contains distinct in-situ and ex-situ physical information rather than a repackaging of process settings alone.

## 6. Registration semantics / 등록 의미

NIST states that data registration integrates multiple datasets spatially and temporally using XYPT command as the fundamental reference. Each registered row contains features corresponding to the command position where the melt-pool-monitoring image was captured.

Important documented limitations:
- the registered data cover camera-triggered points while laser is on, not the entire off-laser scan path;
- DAQ↔XYPT alignment is based on laser turn-on behavior;
- LWI alignment includes perspective transformation and nearest-pixel registration;
- XCT is resampled/interpolated and spatially aligned to the machine coordinate system;
- uncertainty/registration limitations remain material and must be carried into any later experiment.

## 7. Source-integrity/access finding / source 무결성·접근 결과

Current public Data.gov metadata identifies the four ZIP resources, but F15 did not establish through available zero-cost routes:
- an exact PDR release/version identifier analogous to the version-pinned AMB2022 records used previously;
- authoritative SHA-256/component checksums for the four ZIPs;
- actual ZIP byte retrieval and deterministic archive inventory.

Direct zero-cost retrieval of `part1.zip` was attempted in the provided transient environment and did not succeed. Web resource fetch also returned cache-miss rather than component bytes.

This is not evidence that the dataset is absent or invalid. It is a reproducibility/integrity gap for this execution context.

## 8. Frozen gate application / 고정 gate 적용

### `PASS_REGISTERED_POINT_LEVEL_VALIDATION_READY`
- authoritative source: PASS;
- deterministic documented four-part/250-layer schema: PASS;
- row-level registered multi-modal feature semantics: PASS;
- variable definitions/units/thresholds: PASS;
- immutable component version/checksum/byte inventory: **FAIL / NOT VERIFIED**.

Result: **FAIL**.

### `PARTIAL_REGISTERED_SCHEMA_READY`
- official NIST source and schema: PASS;
- point/layer/part registration semantics: PASS;
- distinct in-situ + ex-situ physical features: PASS;
- immutable component provenance/current byte retrieval incomplete: PASS condition.

Result: **PASS**.

Other HOLD/REJECT gates do not better match the evidence.

## 9. Final / 최종

**`PARTIAL_REGISTERED_SCHEMA_READY`**

## 10. Scientific interpretation / 과학적 해석

Supported:
- `mds2-3761` is a materially stronger process–structure external-validation candidate than further feature engineering on BP4;
- official NIST documentation supports deterministic point-level multimodal registration semantics;
- four nominal parts and 250 layers provide richer hierarchy than the prior 21-track diagnostic.

Not yet supported:
- any process→XCT association magnitude;
- predictive performance;
- causal interpretation;
- statistical independence of rows/layers/parts;
- numerical use of the registered ZIPs before exact immutable source integrity is established.

## 11. Consequence / 후속

The next eligible step is a narrow **source-integrity/access gate** for `mds2-3761`, not modeling. It should recover exact release/version lineage and checksum-verifiable component bytes/inventory for at least one part (preferably all four) through a verified zero-incremental-cost route. If that gate passes, a new separately preregistered low-degree-of-freedom in-situ melt-pool ↔ XCT experiment may be designed.

E14 remains frozen at `HOLD_SOURCE_INTEGRITY`; F15 does not supersede or redesign it.
