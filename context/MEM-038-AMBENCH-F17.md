---
id: MEM-038-AMBENCH-F17
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F17/RESULT.md
  - registry/DEC-040.md
---

# MEM-038 — AMBENCH-F17 Result / AMBENCH-F17 결과

## Final state / 최종 상태
`AMBENCH-F17 = PARTIAL_X16_SOURCE_READY`.

## Qualified pair / qualified pair
- in-situ process monitoring: `ark:/88434/mds2-2309`;
- current XCT dataset identity: `ark:/88434/mds2-2514`;
- same July 3, 2019 Overhang X16 AMMT build;
- same sixteen technical replicate parts, metadata-level IDs `1-1`…`4-4` / `Part1_1`…`Part4_4`.

## Integrity / 무결성
Current Data.gov distributions for both datasets expose systematic `.sha256` sidecars. In-situ User Notes were actually retrievable and confirm 16 nominally identical parts, 250-layer organization, 25-layer ZIP grouping, and relevant MPM/DAQ caveats.

XCT current metadata exposes checksum sidecars for Data Description, `OverhangX16_ImageHistograms.xlsx`, per-part STLs and TIFF stacks. The histogram workbook is only ~193 KB and is a potentially manageable summary candidate, but its non-numerical semantic schema was not retrieved/verified in F17.

## Source conflict / source 충돌
NIST AMMT datasets summary currently points X16 XCT to `mds2-2309`. Current Data.gov XCT dataset-level evidence identifies XCT as `mds2-2514` and explicitly links it to in-situ `mds2-2309`. Downstream current XCT identity = `mds2-2514`; preserve the AMMT-page pointer conflict with cause unknown.

## Remaining gaps / 잔여 gap
- small authoritative XCT component/checksum-sidecar actual retrieval failed in current zero-cost context;
- histogram workbook sheet/column semantics remain unverified;
- no manageable low-volume in-situ process signature has yet been frozen; raw MPM/DAQ sources remain large;
- 16 parts are within-build technical replicates, not independent process conditions.

## Exact next eligible work / 정확한 다음 eligible 작업
Before numerical modeling, separately preregister an **X16 manageable-representation feasibility gate** to:
1. recover and checksum-verify the selected small XCT summary source and inspect only non-numerical schema;
2. identify/freeze a practical zero-cost in-situ representation or limited layer/part aggregation without post-hoc outcome tuning;
3. verify deterministic part pairing and source bytes for exactly the future selected inputs.

Only if that passes may a low-degree-of-freedom 16-part process-signature ↔ XCT-summary experiment be preregistered. No high-capacity ML.

## Cost boundary / 비용 경계
Any potentially billable action requires explicit user approval before execution. Post-hoc reporting is not authorization.