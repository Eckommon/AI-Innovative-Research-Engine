---
checkpoint_id: CHK-20260823-E29-PREREGISTERED-EXECUTION-ACTIVE
active_issue: 47
active_research: AMBENCH-E29
last_completed_issue: 46
last_completed_research: AMBENCH-F28
last_decision: DEC-060
updated: 2026-08-23
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.37-e29-preregistered-execution-active`  
**State / 상태:** `E29_PREREGISTERED__EXECUTION_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #47 `AMBENCH-E29`.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `DEC-055`: v2.1 + compact Shared Capability/Portfolio Continuity Overlay active; mission work is not reset.
- Current-state authority: `STATUS.md` + `context/SESSION_HANDOFF.md` + live Issues.
- `COST-001` + `DEC-028`: potentially billable action requires explicit prior approval; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative raw external bytes transient only; no raw Actions artifact/cache.
- Bilingual major records, preregistration, evidence/provenance, verification, and write-back remain mandatory.

## Minimum Operability / 최소 운영
All seven required functions remain PRESENT/EQUIVALENT; no `MISSING-BLOCKING` state. No duplicate root control file is required. Reusable workflow remains `SHARED-INTERNAL-CANDIDATE`; shared content/infrastructure/resource reconciliation remains nonblocking and shared budget/quota is not assumed.

## Last completed / 최근 완료
Issue #46 `AMBENCH-F28` — `PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`.

## Active E29 / 활성 E29
Preregistration: `research/AMBENCH-E29/README.md`; decision: `DEC-060`.

Frozen experiment:
- 0.75 ms plates: T72/T82/T92;
- 5.0 ms plates: T102/T112/T122;
- independent replicate = physical plate;
- P1 only;
- primary reconstruction = `(overlap_depth_y - surface_y_reference) * authoritative pixel scale`;
- >=41/45 valid tracks required per plate;
- primary plate endpoint = arithmetic mean of valid reconstructed overlap depths;
- direction = `0.75 ms > 5.0 ms`, inherited from E27 before its parser incident;
- exact one-sided 20-allocation permutation;
- strong effect requires `Delta_primary > 0`, `p_exact <= 0.05`, `r_rb >= 7/9`, and positive common-track sensitivity with >=36/45 common tracks.

Exposure disclosure:
`NEW_E29_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Exact Next Action / 정확한 다음 행동
Execute E29 with current F28-verified NIST source contracts on a zero-cost standard public GitHub-hosted runner:
1. re-query current NERDm and require exact component size/SHA identities;
2. transiently retrieve six P1 files, Micrographs surface-reference table, and authoritative README;
3. parse the single authoritative physical pixel scale;
4. reconstruct without adaptation;
5. enforce >=41/45 plate coverage and nonnegative documented formula;
6. compute six plate endpoints, exact one-sided permutation, plate-level rank-biserial, and common-track sensitivity;
7. write sanitized aggregated results only;
8. apply frozen E29 gate, persist claims/decision/memory, close/HOLD Issue #47, synchronize and re-read.

Incremental monetary cost must remain 0 USD.
