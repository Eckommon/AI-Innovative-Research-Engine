---
id: AMBENCH-F17
type: source-identity-semantic-feasibility
state: PREREGISTERED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F16/RESULT.md
  - NIST PDR ark:/88434/mds2-2309
  - NIST PDR ark:/88434/mds2-2514
---

# AMBENCH-F17 — Overhang X16 Original In-Situ ↔ XCT Source/Identity/Semantic Feasibility
# AMBENCH-F17 — Overhang X16 원본 in-situ ↔ XCT source/identity/semantic feasibility

## 1. Purpose / 목적

**KO:** F16에서 `mds2-3761`가 높은 가치에도 불구하고 immutable source provenance/byte access가 미완성으로 남았으므로, 동일 NIST AMMT 계열의 **원본 Overhang X16** 자료가 더 강한 checksum-verifiable same-build process–structure 외부검증 자산인지 판정한다.

**EN:** Because F16 left `mds2-3761` high-value but not immutable-source-ready, determine whether the **original Overhang X16** NIST AMMT sources provide a stronger checksum-verifiable, same-build process–structure external-validation asset.

Candidate pair:
- in-situ process monitoring: `ark:/88434/mds2-2309`, DOI `10.18434/mds2-2309`;
- post-build XCT: current Data.gov/PDR identity `ark:/88434/mds2-2514`, DOI `10.18434/mds2-2514`.

F17 is source/identity/semantic feasibility only. No numerical process-monitoring or XCT scientific outcome analysis, correlation, target selection, feature importance, or model fitting is authorized.

## 2. Outcome-blindness / outcome-blindness

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES`

Before F17 freeze, only public metadata were inspected: dataset descriptions, identifiers, resource names/types, publication/update dates, and existence of checksum sidecars. No X16 process-monitoring values, XCT histogram values, voxel values, STL geometry values, or derived association statistics were numerically accessed.

## 3. Governance / 거버넌스

- `COST-001` + `DEC-028`: potentially billable action requires explicit prior user approval; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: any source bytes are transient-only.
- `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `WRITEBACK-001` apply.
- No unverified mirrors or inferred mappings.

## 4. Known source conflict frozen before execution / 실행 전 고정 source conflict

NIST's AMMT datasets summary page currently lists the X16 XCT section with `Data DOI and download: https://doi.org/10.18434/mds2-2309`, which is the in-situ process-monitoring DOI.

Current Data.gov XCT metadata instead identifies:
- XCT identifier `ark:/88434/mds2-2514`;
- DOI access `https://doi.org/10.18434/mds2-2514`;
- description explicitly states the XCT files are measurements of the sixteen parts from the in-situ `mds2-2309` build.

F17 must not silently harmonize this discrepancy. It must classify whether `mds2-2514` is sufficiently authoritative to resolve the current XCT identity while preserving the AMMT-page statement as a documented stale/conflicting pointer.

## 5. Allowed metadata/semantic inspection / 허용 범위

Allowed after preregistration:
- current official Data.gov/NIST dataset metadata;
- PDR release/version history if recoverable;
- resource names, media types, sizes, download URLs, checksum-sidecar URLs;
- small checksum sidecar text;
- User Notes / Data Description PDF metadata and semantic content;
- file/folder/part/layer identifier semantics;
- workbook sheet/column names only if needed to understand `OverhangX16_ImageHistograms.xlsx`, but **not numerical cell values**;
- deterministic Part 1…16 pairing semantics between the two datasets.

Forbidden:
- numerical process-monitoring measurements;
- numerical XCT histogram/voxel/STL geometry outcomes;
- correlations or predictive tests;
- selecting a scientific endpoint because its observed numerical result looks favorable.

## 6. Frozen questions / 고정 질문

1. Is in-situ `mds2-2309` currently authoritative and checksum-sidecar rich?
2. Is XCT `mds2-2514` currently authoritative and checksum-sidecar rich?
3. Does current authoritative evidence establish that both datasets refer to the **same July 3, 2019 Overhang X16 build and same sixteen parts**?
4. Can the AMMT-page XCT DOI conflict be resolved as a stale/incorrect pointer using stronger current dataset-level evidence, without deleting the conflict from history?
5. Can at least one small source document/checksum sidecar from **each** dataset be retrieved through a verified zero-cost authoritative route?
6. Are Part identifiers 1…16 and source semantics deterministic enough for a future part-level validation design?
7. Does `OverhangX16_ImageHistograms.xlsx` have sufficiently explicit non-numerical semantics to qualify as a manageable ex-situ summary candidate, without reading outcome values?
8. Is there a practical zero-cost in-situ representation route that does not require immediately processing all multi-GB camera data, or must access/scale remain a HOLD before modeling?

## 7. Frozen gates / 고정 판정

### `PASS_X16_CHECKSUMMED_PAIR_READY`
All must hold:
- in-situ `mds2-2309` authoritative identity qualified;
- XCT `mds2-2514` authoritative identity qualified;
- same-build / same-16-part relationship deterministically established;
- checksum-sidecar structure verified for both sources;
- at least one small authoritative source document or checksum sidecar from each dataset successfully retrieved through zero-cost route;
- part identity semantics sufficient for future pairing;
- AMMT-page DOI conflict resolved by stronger current authoritative evidence and retained as historical conflict;
- no material semantic contradiction.

This gate authorizes only a **separate future preregistration**, not immediate modeling.

### `PARTIAL_X16_SOURCE_READY`
Authoritative pair/same-build relation and checksum-sidecar structure are established, but one or more of actual small-file retrieval, part-level semantic detail, or practical in-situ representation remains incomplete.

### `HOLD_X16_IDENTITY_CONFLICT`
The XCT identifier conflict cannot be defensibly resolved from current authoritative sources or same-build/part mapping is ambiguous.

### `HOLD_X16_ACCESS_OR_SCALE`
Identity/integrity pass, but zero-cost retrieval or feasible representation is insufficient to define a reproducible future numerical experiment.

### `REJECT_NOT_DETERMINISTICALLY_PAIRED`
Authoritative evidence shows the proposed in-situ and XCT assets are not the same build/parts or cannot be deterministically related.

## 8. Future modeling boundary / 후속 모델링 경계

Even if F17 passes:
- 16 parts are **technical/within-build replicates**, not 16 independent process conditions;
- no claim of process-condition generalization is authorized;
- a future experiment must use low degrees of freedom, preserve part/build hierarchy, and separately preregister target/feature aggregation before numerical outcome access;
- high-capacity ML is not authorized by F17.

## 9. Cost / 비용

F17 may use only verified zero-incremental-cost public NIST/Data.gov access and already-provided compute. Any potentially billable route must stop at `HOLD_COST_APPROVAL` until explicit user approval.