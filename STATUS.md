---
checkpoint_id: CHK-20260823-F28-PREREGISTERED-SOURCE-SCHEMA
active_issue: 46
active_research: AMBENCH-F28
last_completed_issue: 45
last_completed_research: AMBENCH-E27
last_decision: DEC-058
updated: 2026-08-23
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.35-f28-preregistered-source-schema`  
**State / 상태:** `F28_PREREGISTERED__SOURCE_SCHEMA_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #46 `AMBENCH-F28`.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `DEC-055`: v2.1 Continuity Overlay active; mission work is not reset.
- Current-state authority: `STATUS.md` + `context/SESSION_HANDOFF.md` + live Issues; README does not duplicate dynamic state.
- `COST-001` + `DEC-028`: potentially billable action requires explicit prior approval; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative raw external bytes transient only.
- Bilingual major records, evidence/source provenance, preregistration, verification and write-back remain mandatory.

## Minimum Operability / 최소 운영
Existing functional equivalents remain sufficient; no root `AGENTS.md` bootstrap is required. Reusable state/preregistration/NERDm/evidence workflows remain `SHARED-INTERNAL-CANDIDATE`; central capability reconciliation is nonblocking.

## Last completed / 최근 완료
Issue #45 `AMBENCH-E27` — **`HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`**.

E27 frozen primary/sensitivity summaries were exact NIST source/hash matches but did not contain T72/T82/T92/T102/T112/T122 physical plate identifiers. Therefore the preregistered six-plate 3-vs-3 numerical test was not run and no source/endpoint substitution occurred.

Permanent exposure disclosure from E27:
**`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`**.
The E27 scientific design was frozen before the parser incident; no six-plate mapping, group comparison, permutation test or model was performed from emitted values.

## Active F28 / 활성 F28
Preregistration: `research/AMBENCH-F28/README.md`. Decision: `DEC-058`.

Purpose: determine whether the six public plate-specific P1 `*_pixel_points.csv` components in NIST `mds2-4103` are:
- directly analysis-ready for a deterministic per-plate geometry endpoint;
- or immutable plate-specific annotation data requiring an additional authoritative reconstruction contract;
- or unusable for the intended route.

F28 is source/schema/provenance only. No condition effect or geometry outcome may be computed.

Frozen plates: T72/T82/T92/T102/T112/T122, P1 only.

## Exact Next Action / 정확한 다음 행동
1. Query current NERDm for all six exact P1 components and hashes.
2. Retrieve only the six small P1 CSVs and inspect bounded header/schema/row-count information without raw values.
3. Use small authoritative documentation only for reconstruction semantics; do not emit outcome values.
4. Apply frozen F28 gate and write back claims/decision/memory.
5. Close/HOLD Issue #46, synchronize STATUS/HANDOFF, re-read live state.

Incremental monetary cost remains 0 USD.