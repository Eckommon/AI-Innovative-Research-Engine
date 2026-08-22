---
id: AMBENCH-F17-RESULT
type: source-identity-semantic-feasibility-result
state: COMPLETED_PARTIAL_X16_SOURCE_READY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F17/README.md
  - Issue #35
---

# AMBENCH-F17 Result — Overhang X16 Original In-Situ ↔ XCT Source/Identity/Semantic Feasibility
# AMBENCH-F17 결과 — Overhang X16 원본 in-situ ↔ XCT source/identity/semantic feasibility

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_X16_SOURCE_READY`**

## 1. Executive result / 핵심 결과

**KO:** Overhang X16 원본 in-situ `mds2-2309`와 current XCT `mds2-2514`는 동일한 2019-07-03 AMMT build와 동일 16개 technical replicate part를 대상으로 하는 authoritative same-build pair로 충분히 식별된다. 양쪽 Data.gov distribution에는 systematic `.sha256` sidecar가 존재하며, in-situ User Notes는 실제로 zero-cost authoritative route에서 열려 16-part numbering/layout 및 250-layer source organization을 확인했다. 따라서 F16의 `mds2-3761`보다 immutable-component provenance 구조는 명백히 강하다.

그러나 XCT의 작은 component(Data Description PDF, histogram workbook, checksum sidecar)는 현재 실행경로에서 실제 byte retrieval이 실패했고, `OverhangX16_ImageHistograms.xlsx`의 비수치 sheet/column semantics도 확인하지 못했다. 또한 향후 in-situ representation을 multi-GB raw camera processing 없이 재현 가능하게 만들 수 있는 경로가 아직 고정되지 않았다. 따라서 full checksum-pair PASS가 아니라 **`PARTIAL_X16_SOURCE_READY`**이다.

**EN:** The original Overhang X16 in-situ `mds2-2309` and current XCT `mds2-2514` are sufficiently identified as an authoritative same-build pair covering the same July 3, 2019 AMMT build and the same sixteen technical replicate parts. Both Data.gov distributions expose systematic `.sha256` sidecars, and the in-situ User Notes were actually retrieved through a zero-cost authoritative route, confirming the 16-part numbering/layout and 250-layer source organization. This is materially stronger immutable-component provenance than F16's `mds2-3761` route.

However, actual byte retrieval of a small XCT component (Data Description PDF, histogram workbook, or checksum sidecar) failed in the current execution context, the non-numerical sheet/column semantics of `OverhangX16_ImageHistograms.xlsx` remain unverified, and a practical reproducible in-situ representation route that avoids immediate multi-GB raw-camera processing has not yet been frozen. Therefore the full checksum-pair gate does not pass; the final result is **`PARTIAL_X16_SOURCE_READY`**.

## 2. In-situ source / in-situ 원천

Current Data.gov/NIST metadata:
- identifier: `ark:/88434/mds2-2309`;
- DOI: `10.18434/mds2-2309`;
- issued: `2020-10-16`;
- modified: `2020-10-06`;
- current catalog check: 2026-08-03;
- 89 public resources.

The public distribution systematically pairs data resources with `.sha256` sidecars, including:
- `DAQ_L001-L025.zip` + `.sha256` and subsequent layer-group DAQ archives;
- MPM AVI/TIFF layer-group archives + `.sha256`;
- `OverhangX16_In-situData_UserNotes.pdf` + `.sha256`;
- `XYPT_L001-025.zip` through `XYPT_L226-250.zip`, each with `.sha256`.

The authoritative User Notes PDF was successfully retrieved in F17. It states:
- experiment date July 3, 2019;
- 16 nominally identical parts in one build;
- replicated material, scan strategy, and laser processing parameters;
- part layout/numbering `1-1` through `4-4`;
- 250 layers;
- XYPT files grouped in ten ZIPs of 25 layers;
- MPM and DAQ files likewise organized by layer groups;
- some MPM frames can be missing and parts `1-1` through `1-4` have a layer-image visibility limitation after melting.

These are future modeling constraints, not numerical outcomes.

## 3. XCT source / XCT 원천

Current Data.gov/NIST metadata:
- identifier: `ark:/88434/mds2-2514`;
- DOI access: `10.18434/mds2-2514`;
- issued: `2022-02-28`;
- modified: `2021-12-03`;
- current catalog check: 2026-08-03;
- description explicitly says the dataset contains post-build XCT measurements of the sixteen parts built in the in-situ `mds2-2309` Overhang X16 dataset.

The current distribution exposes systematic component/checksum pairs, including:
- `DataDescription_OverhangPartX16_XCT.pdf` + `.sha256`;
- `OverhangX16_ImageHistograms.xlsx` + `.sha256`;
- per-part `Surface_STLs/OverhangPartX16_Part{group}_{member}.stl` + `.sha256`;
- per-part TIFF stacks `OverhangX16_Part{group}_{member}_Cropped.tif` + `.sha256`.

NIST metrics report:
- total dataset size about `11.294 GB`;
- `OverhangX16_ImageHistograms.xlsx` about `193.26 KB`;
- individual STL/TIFF sources are hundreds of MB each.

The small histogram workbook is therefore a potentially manageable ex-situ summary asset, but F17 did **not** read its numerical cells or establish its non-numerical schema semantics.

## 4. Same-build / part identity / 동일 build·part identity

The current XCT dataset description directly states that its sixteen measured parts are the parts built as part of the Overhang X16 in-situ process-monitoring dataset `mds2-2309`.

The in-situ User Notes visually/textually define sixteen positions as a `4 × 4` label family `1-1`…`4-4`. Current XCT resource names preserve the same family (`Part1_1`…`Part4_4`). Therefore future **part-level identifier pairing is deterministic at the metadata level**.

Boundary:
- these are 16 technical/within-build replicates;
- they are not 16 independent process conditions;
- future inference must preserve this hierarchy.

## 5. XCT DOI conflict / XCT DOI 충돌

### Conflicting source
The NIST AMMT datasets summary page currently places the X16 XCT section under a `Data DOI and download` pointer to `mds2-2309`—the in-situ dataset DOI.

### Stronger current dataset-level evidence
Current Data.gov XCT metadata identifies the XCT dataset itself as:
- identifier `ark:/88434/mds2-2514`;
- DOI access `10.18434/mds2-2514`;
- description: XCT measurements of the same sixteen parts from in-situ `mds2-2309`.

### F17 disposition
`CURRENT_X16_XCT_IDENTITY = mds2-2514` is qualified for downstream source identity.

The AMMT summary-page `mds2-2309` XCT pointer is retained as an **active historical/source-page conflict; cause unknown**. F17 does not silently delete or rewrite the conflicting source.

## 6. Small-file access tests / 소형 파일 접근시험

### In-situ
`OverhangX16_In-situData_UserNotes.pdf` — **RETRIEVED / PASS**.

Its `.sha256` sidecar was visible in current Data.gov metadata but sidecar byte fetch returned cache miss.

### XCT
Attempts to retrieve:
- Data Description PDF;
- Data Description checksum sidecar;
- `OverhangX16_ImageHistograms.xlsx`;
- histogram checksum sidecar
through available zero-cost authoritative paths did not return usable source bytes in this execution context.

Thus:
- XCT current component identity/sidecar existence: VERIFIED;
- actual small XCT component byte retrieval: NOT VERIFIED;
- local checksum reproduction: NOT COMPUTED.

No paid or unverified mirror route was substituted.

## 7. Practical representation / 규모·표현성

The in-situ dataset is rich but large. User Notes show MPM camera and DAQ sources are grouped by 25 layers and the MPM source is intrinsically high-volume. F17 did not identify a small authoritative precomputed melt-pool feature summary equivalent to the F15 registered representation.

Therefore a future experiment must first freeze a **manageable zero-cost representation path**. It must not assume that all multi-GB camera data can be downloaded/processed merely because checksum sidecars exist.

The small XCT histogram workbook is attractive as a candidate summary outcome source, but its semantic schema must be qualified before numerical use.

## 8. Frozen gate application / 고정 gate 적용

### `PASS_X16_CHECKSUMMED_PAIR_READY`
- in-situ authoritative identity: PASS;
- XCT current authoritative identity: PASS;
- same-build/same-16-part relation: PASS;
- systematic checksum-sidecar structure both sources: PASS;
- small authoritative component from each source actually retrieved: **FAIL** (XCT failed);
- part identity semantics: PASS at metadata level;
- DOI conflict resolved by stronger current dataset-level evidence while preserved: PASS;
- no material semantic contradiction: PASS so far.

Result: **FAIL**.

### `PARTIAL_X16_SOURCE_READY`
- authoritative pair/same-build relation: PASS;
- checksum-sidecar structure: PASS;
- actual XCT small-file retrieval and/or semantic detail incomplete: PASS condition;
- practical in-situ representation incomplete: PASS condition.

Result: **PASS**.

### `HOLD_X16_IDENTITY_CONFLICT`
Not selected. Current dataset-level Data.gov evidence sufficiently identifies XCT as `mds2-2514` while preserving the AMMT-page conflict.

### `HOLD_X16_ACCESS_OR_SCALE`
Not selected as the final label because source pairing and checksum structure are already materially qualified and at least the in-situ documentation was retrievable; remaining access/scale limitations fit the preregistered PARTIAL gate.

### `REJECT_NOT_DETERMINISTICALLY_PAIRED`
Not applicable.

## 9. Final / 최종

**`PARTIAL_X16_SOURCE_READY`**

## 10. Consequence / 후속

Do **not** start numerical process–XCT modeling yet.

The next highest-leverage step is a narrowly preregistered **X16 manageable-representation feasibility gate** that attempts, before numerical outcomes are inspected, to establish:
1. the non-numerical schema/part mapping of `OverhangX16_ImageHistograms.xlsx` through an authoritative zero-cost route;
2. an authoritative low-volume in-situ representation or a frozen subset/aggregation strategy that is computationally feasible without downloading all raw MPM data;
3. checksum-verifiable retrieval of the exact small sources selected for that future experiment.

If those pass, a later experiment may test a low-degree-of-freedom 16-part process-signature ↔ XCT-summary relationship while explicitly treating the 16 parts as within-build technical replicates, not independent process conditions.

No high-capacity ML is authorized by F17. E14 and F16 remain unchanged.