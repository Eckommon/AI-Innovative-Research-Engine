---
id: AMBENCH-F15
type: feasibility-preregistration
state: PREREGISTERED_METADATA_ONLY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# AMBENCH-F15 — `mds2-3761` Registered In-Situ ↔ XCT External-Validation Feasibility
# AMBENCH-F15 — `mds2-3761` 등록형 in-situ ↔ XCT 외부검증 feasibility

## 1. Purpose / 목적

Determine whether NIST `mds2-3761` is reproducibly source-identifiable and deterministically usable at part/layer/row/feature level for a later external process–structure validation experiment.

NIST `mds2-3761`가 후속 process–structure 외부검증을 위해 part/layer/row/feature 수준에서 재현 가능한 source/identity/registration 준비도를 갖추는지 판정한다.

F15 is **not** a predictive experiment and does not authorize model fitting.

## 2. Frozen source / 고정 source

- PDR identifier: `ark:/88434/mds2-3761`
- NIST AMS 100-69 DOI: `10.6028/NIST.AMS.100-69`
- Public resource files listed by Data.gov:
  - `part1.zip`
  - `part02.zip`
  - `part03.zip`
  - `part04.zip`
- Original in-situ source: `mds2-2233`
- Original ex-situ XCT source: `mds2-2291`

## 3. Allowed evidence / 허용 근거

Metadata/source-only:
- official PDR/Data.gov metadata;
- NIST AMS 100-69;
- resource names/URLs;
- publication/version history if authoritative;
- checksums/file sizes if authoritative;
- archive/file inventory if bytes are retrievable at zero incremental cost;
- row/column/feature definitions;
- registration semantics;
- uncertainty semantics;
- part/layer identity.

No target-aware modeling or exploratory prediction is allowed.

## 4. Required questions / 필수 질문

1. Is an exact authoritative public publication/version identifiable?
2. Are the four part components explicitly identified and public?
3. Are component sizes/checksums/version lineage recoverable?
4. Is the file hierarchy deterministic: 4 parts × 250 layer CSVs?
5. Does each row map all modalities to the same XYPT-referenced measured point?
6. Are in-situ melt-pool and ex-situ XCT variables explicitly defined?
7. Are units, thresholds, coordinate/time semantics, and uncertainty documented?
8. What is the maximum defensible later join/validation level: row/point, layer, part, or none?
9. Can execution proceed with zero incremental monetary cost?

## 5. Frozen gates / 고정 판정

### `PASS_REGISTERED_POINT_LEVEL_VALIDATION_READY`
All:
- authoritative exact source/version/component provenance;
- component checksum or equivalent immutable integrity evidence;
- deterministic four-part and 250-layer file hierarchy;
- row-level registered in-situ + ex-situ features sharing documented machine-coordinate reference;
- variable semantics/units/thresholds sufficient;
- no material identity conflict;
- zero incremental cost.

### `PARTIAL_REGISTERED_SCHEMA_READY`
Official NIST source and registration/schema semantics strongly establish point/layer/part multi-modal alignment, but exact immutable component provenance (version/checksum/bytes) is not fully established or current zero-cost byte retrieval is blocked.

### `HOLD_IDENTITY_OR_REGISTRATION_GAP`
Publication/source exists, but part/layer/row identity or registration semantics are insufficient for deterministic cross-modal validation.

### `HOLD_SOURCE_PROVENANCE`
Source is authoritative but exact release/component/version provenance cannot be sufficiently established to support reproducible downstream execution.

### `REJECT_NOT_DISTINCT_OR_NOT_PHYSICAL`
The candidate does not actually contain distinct in-situ and ex-situ physical information in a defensibly registered relationship.

## 6. Outcome boundary / outcome 경계

No F15 numerical relationship statistic, prediction, correlation, target selection, or feature importance is allowed. F15 only qualifies the source and join level.

## 7. Cost / 비용

`COST-001` + `DEC-028`: any potentially billable action requires explicit user approval **before execution**. Unknown billing = `HOLD_COST_APPROVAL`. Paid route substitution is prohibited.

## 8. Consequence / 후속

- PASS → separately preregister a low-degree-of-freedom process/in-situ ↔ XCT validation experiment.
- PARTIAL → preserve candidate but require a source-integrity/access gate before numerical analysis.
- HOLD/REJECT → do not model; return to external-validation triage.
