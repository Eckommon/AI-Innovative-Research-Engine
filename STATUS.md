---
checkpoint_id: CHK-20260822-D12-PREREG
active_issue: 29
active_research: AMBENCH-D12
last_completed_issue: 27
last_completed_research: AMBENCH-D11
last_decision: DEC-029
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline label / 최신 검증 baseline:** `v0.14-bp4-repeat-provenance-prereg`  
**State / 상태:** `D12_PREREGISTERED__EXECUTION_NOT_YET_RUN`  
**Active Work Queue / 활성 작업 큐:** Issue #29 `AMBENCH-D12`

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `READ-001` + `STATE-001` + `CHECKPOINT-001` mandatory.
- `COST-001` + `DEC-028`: **any monetary-cost action requires explicit user approval before execution; after-the-fact reporting is not approval.** Unknown/potential billing without prior approval = `HOLD_COST_APPROVAL`, no execution.
- `RAW-001`: authoritative external raw bytes are transient-only.
- `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.

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

## Active D12 / 활성 D12
Preregistration: `research/AMBENCH-D12/README.md`.  
Decision: `DEC-029`. Boundary claim: `CLM-044`.  
Issue: #29.

Purpose: distinguish whether D11 repeat-sensitive descriptors are dominated by sampling/representation sensitivity, cross-case repeat-index structure, robust condition-specific case×repeat variation, or mixed provenance.

Frozen diagnostics:
1. exact D11 reproduction gate (`<=1e-9` absolute tolerance);
2. balanced case + repeat-index SS decomposition;
3. factor-2 and factor-4 sampling-phase decimation;
4. `R_sampling` robustness ratio;
5. secondary residual PCA.

Frozen final gates:
- `REPRESENTATION_SENSITIVITY_DOMINANT`
- `CROSS_CASE_REPEAT_INDEX_STRUCTURE`
- `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
- `MIXED_REPEAT_PROVENANCE`
- `HOLD_DATA_INTEGRITY`

Interpretation boundary: D12 cannot establish physical cause, physical-outcome utility, prediction, generalization, or causality.

## Persistent Holds / 지속 HOLD
- same-BP4 confocal analysis — `HOLD_PUBLICATION_NOT_VERIFIED`;
- BP1↔BP4 physical track/repeat pairing — `NOT_AUTHORIZED`;
- BP4 roughness harmonization — `ACTIVE_SOURCE_CONFLICT`;
- AMB2025-07 predictive thermal↔geometry — HOLD pending public thermography source.
