---
checkpoint_id: CHK-20260822-F17-ACTIVE-X16-SOURCE-PAIR
active_issue: 35
active_research: AMBENCH-F17
last_completed_issue: 34
last_completed_research: AMBENCH-F16
last_decision: DEC-039
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.22-f17-active-x16-source-pair`  
**State / 상태:** `F17_ACTIVE__X16_SOURCE_IDENTITY_SEMANTIC_FEASIBILITY`  
**Active Work Queue / 활성 작업 큐:** Issue #35 `AMBENCH-F17`.

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
- #33 F15 — `PARTIAL_REGISTERED_SCHEMA_READY`
- #34 F16 — `PARTIAL_PUBLIC_ENDPOINT_READY`

## Active F17 / 활성 F17
Preregistration: `research/AMBENCH-F17/README.md`. Decision: `DEC-039`.

Candidate pair:
- in-situ `ark:/88434/mds2-2309`;
- current Data.gov/PDR XCT identity `ark:/88434/mds2-2514`;
- same July 3, 2019 Overhang X16 build / sixteen technical replicate parts.

Frozen source conflict:
- NIST AMMT datasets summary currently points X16 XCT to DOI `mds2-2309`;
- current Data.gov XCT metadata identifies XCT DOI/identifier `mds2-2514` and explicitly links it to in-situ `mds2-2309`.

F17 is metadata/source/semantic feasibility only; no numerical X16 process or XCT outcomes may be analyzed.

## Exact Active Work / 현재 작업
Apply frozen F17 gates using official current NIST/Data.gov evidence, checksum-sidecar structure, same-build/part identity semantics, and zero-cost small-file access tests. No modeling.
