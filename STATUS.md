---
checkpoint_id: CHK-20260823-E27-PREREGISTERED-SCHEMA-PREFLIGHT
active_issue: 45
active_research: AMBENCH-E27
last_completed_issue: 44
last_completed_research: AMBENCH-F26
last_decision: DEC-056
updated: 2026-08-23
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.33-e27-preregistered-schema-preflight`  
**State / 상태:** `E27_PREREGISTERED__SCHEMA_PREFLIGHT_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #45 `AMBENCH-E27`.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `DEC-055`: GPT Project ↔ GitHub ↔ Agent Capability Integration v2.1 is adopted as a **Continuity Overlay**, not a mission reset.
- Mission work priority remains: `CURRENT MISSION WORK > integrity/safety P0 > capability upgrade > distribution`.
- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval before execution; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative external raw bytes are transient-only.
- `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.
- README no longer duplicates dynamic current-state values; current state authority is `STATUS.md` + `context/SESSION_HANDOFF.md` + live Issues.

## Minimum Operability Baseline / 최소 운영 기준선
Functional equivalents are PRESENT/EQUIVALENT; no root `AGENTS.md` bootstrap is required now:
- Mission/Scope: README + `docs/GOVERNANCE.md`
- Authority: governance + GPT/GitHub sync + hallucination-control protocols
- Current state/work: STATUS + SESSION_HANDOFF + live Issues
- Human/Cost gate: `COST-001`, `DEC-028`, no-cost policy
- Decision/evidence: `DEC-*`, `CLM-*`, decision/claim ledgers
- Verification: preregistered gates + GitHub Actions + state-integrity workflow
- Continuation: STATUS/HANDOFF write-back and re-read

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
- #35 F17 — `PARTIAL_X16_SOURCE_READY`
- #36 F18 — `PARTIAL_MANAGEABLE_X16_ROUTE_READY`
- #37 F19 — `PARTIAL_F19_SEGMENTATION_RULE_READY`
- #38 F20 — `PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`
- #39 F21 — `REJECT_F21_ENDPOINT_ROUTE`
- #40 F22 — `PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`
- #41 F23 — `PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`
- #42 E24 — `NO_MATERIAL_E24_ASSOCIATION`
- #43 D25 — `D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`
- #44 F26 — `PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`

## Active AMBENCH-E27 / 활성 E27
Preregistration: `research/AMBENCH-E27/README.md`. Decision: `DEC-056`.

Frozen design:
- source: NIST `mds2-4103` v1.0.0;
- 0.75 ms: T72/T82/T92;
- 5.0 ms: T102/T112/T122;
- physical plate = independent replicate;
- geometry: 5 mm × 5 mm pad, P1, x=0.460 mm;
- primary: average overlap depth;
- sensitivity: average depth;
- exact one-sided 20-allocation label-permutation reference test;
- strong PASS: Δ>0, p<=0.05, rank-biserial>=0.777778.

Inherited disclosure:
`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`.
No six-plate P1 pad outcome value was used in E27 preregistration.

## Capability Overlay Delta / Capability overlay delta
Recurring state-reconciliation, frozen-gate/preregistration, NERDm immutable-source qualification and evidence/cost-gate workflows are classified `SHARED-INTERNAL-CANDIDATE` only. Central repository `Eckommon/AI-Agent-Capability-Library` exists; overlap remains `UNVERIFIED`. No Skill/MCP/Plugin creation blocks E27.

## Exact Next Action / 정확한 다음 행동
1. NERDm metadata preflight for frozen primary/sensitivity files.
2. Local SHA-256 verification and header/identifier-only schema qualification.
3. If deterministic six-plate P1 mapping passes, execute the frozen numerical test.
4. Persist result/claims/decision, close or HOLD Issue #45 as appropriate, synchronize STATUS/HANDOFF, and re-read live state.

Any paid/potentially paid route requires explicit prior user approval.