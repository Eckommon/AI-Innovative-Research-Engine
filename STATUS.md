---
checkpoint_id: CHK-20260822-F15-PARTIAL-REGISTERED-SCHEMA
active_issue: none
active_research: none
last_completed_issue: 33
last_completed_research: AMBENCH-F15
last_decision: DEC-036
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.20-f15-partial-registered-schema-ready`  
**State / 상태:** `F15_COMPLETED__PARTIAL_REGISTERED_SCHEMA_READY`  
**Active Work Queue / 활성 작업 큐:** none.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval **before execution**; post-hoc reporting is not authorization; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative external raw bytes are transient-only.
- `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.

## Completed AMBENCH Chain / 완료 계보
- #11 F02 — `PASS`
- #13 E03 — `NO_MATERIAL_GAIN`
- #15 F04 — `PARTIAL`
- #17 E05 — `MIXED`
- #19 D06 — `PROCESS_CASE_PROXY_DOMINANT`
- #21 F07 — `PARTIAL_SOURCE_READY`
- #22 F08 — `PARTIAL_CASE_LEVEL_READY`
- #24 E09 — `INCONCLUSIVE_CASE_LEVEL`
- #26 F10 — `HOLD_PUBLICATION_NOT_VERIFIED`
- #27 D11 — `MIXED_TEMPORAL_INFORMATION`
- #29 D12 — `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
- #31 F13 — `PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`
- #32 E14 — `HOLD_SOURCE_INTEGRITY`
- #33 F15 — **`PARTIAL_REGISTERED_SCHEMA_READY`**

## F15 Final / F15 최종
Result: `research/AMBENCH-F15/RESULT.md`.  
Claims: `CLM-053..055`. Decisions: `DEC-035..036`. Memory: `MEM-036-AMBENCH-F15`.

Selected source:
- NIST PDR `ark:/88434/mds2-3761`;
- NIST AMS 100-69, DOI `10.6028/NIST.AMS.100-69`.

Verified schema/registration:
- four nominally identical LPBF parts in one build;
- 250 layer CSV files per part;
- 40 registered columns per measured point;
- XYPT-referenced machine-coordinate registration;
- commanded/real laser position, power, speed;
- in-situ melt-pool length/width/area at thresholds 80/100/120;
- layerwise optical intensity features;
- ex-situ XCT voxel values and filtered variants;
- documented registration and uncertainty methods.

Remaining gap:
- exact version-pinned release lineage not established;
- authoritative ZIP checksums/equivalent immutable integrity evidence not established;
- actual `part1.zip`–`part04.zip` archive-byte inventory not retrieved through current verified zero-cost routes.

Frozen final gate: **`PARTIAL_REGISTERED_SCHEMA_READY`**.

## Exact Next Eligible Work / 정확한 다음 행동
No experiment is active.

Next: separately preregister a narrow **`mds2-3761` source-integrity/access gate** to recover exact release/version lineage and checksum-verifiable component bytes/inventory through a verified zero-incremental-cost route. Only after that passes may a low-degree-of-freedom in-situ melt-pool ↔ XCT process–structure experiment be preregistered.

E14 remains frozen at `HOLD_SOURCE_INTEGRITY`; do not redesign it. Any paid/potentially paid retrieval route requires explicit user approval before execution.
