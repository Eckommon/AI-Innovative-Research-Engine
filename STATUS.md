---
checkpoint_id: CHK-20260823-F28-PASS-GEOMETRY-SOURCE-READY
active_issue: none
active_research: none
last_completed_issue: 46
last_completed_research: AMBENCH-F28
last_decision: DEC-059
updated: 2026-08-23
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.36-f28-geometry-source-ready`  
**State / 상태:** `F28_COMPLETED__PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`  
**Active Work Queue / 활성 작업 큐:** none.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `DEC-055`: v2.1 + compact Shared Capability/Portfolio Continuity Overlay active; mission work is not reset.
- Current-state authority: `STATUS.md` + `context/SESSION_HANDOFF.md` + live Issues; README does not duplicate dynamic state.
- `COST-001` + `DEC-028`: potentially billable action requires explicit prior approval; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative raw external bytes transient only.
- Bilingual major records, evidence/source provenance, preregistration, verification and write-back remain mandatory.

## Minimum Operability / 최소 운영
Seven functions are currently satisfied with no `MISSING-BLOCKING` state:
- Mission/Scope = PRESENT
- Authority/Agent Rule = EQUIVALENT
- Current State/Active Work = PRESENT
- Human/Cost/Security Gate = PRESENT
- Decision/Evidence Authority = PRESENT
- Verification Method = PRESENT
- Write-back/Continuation = PRESENT

No new root `AGENTS.md` or duplicate control layer is required. Reusable state/preregistration/NERDm/evidence workflows remain `SHARED-INTERNAL-CANDIDATE`; central capability/shared-content/shared-infrastructure/shared-resource reconciliation is nonblocking. Shared budget/quota is never assumed without canonical ledger evidence.

## Last completed / 최근 완료
Issue #46 `AMBENCH-F28` — **`PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`**.

F28 verified:
- exact one-to-one P1 `*_pixel_points.csv` binding for T72/T82/T92/T102/T112/T122;
- local size/SHA-256 matches to current NIST `mds2-4103` NERDm for all six components;
- common 7-field pixel-coordinate schema with 45 rows per plate;
- NIST authoritative measurement/reconstruction semantics and physical micrograph scaling contract;
- exact current `Cross_Sections/Micrographs/SurfaceReference_and_Orientation_Layers.csv`, size 1653 bytes, SHA-256 `98c898fd78be88c5f0a318575ad6468dc03a3cdeaa31dc19d03605a2df9f7c22`;
- exact one P1 surface-reference row for each target plate.

F28 computed no numerical geometry endpoint or condition comparison.

Permanent inherited disclosure:
**`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`**.

## Exact Next Action / 정확한 다음 행동
Per `DEC-059`, separately preregister **AMBENCH-E29 — six-plate P1 reconstructed overlap-depth turnaround-time controlled experiment** before any numerical coordinate/reference inspection.

E29 must freeze:
1. six physical plates and 0.75 ms / 5.0 ms grouping;
2. P1 only;
3. authoritative pixel/reference/physical-scale reconstruction contract;
4. primary plate-level overlap-depth endpoint;
5. track missingness/coverage rule;
6. plate aggregation rule;
7. directional hypothesis + exact 3-vs-3 permutation statistic;
8. effect-size and PASS/MIXED/NO_MATERIAL_GAIN/HOLD gates;
9. nested dependence limit: tracks are repeated measurements inside a plate, not independent replicates;
10. permanent inherited E27 exposure disclosure.

Only after preregistration may numerical coordinate/reference values be inspected. Incremental monetary cost remains 0 USD.
