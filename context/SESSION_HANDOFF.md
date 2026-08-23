---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260823-E29-PREREGISTERED-EXECUTION-ACTIVE
active_issue: 47
active_research: AMBENCH-E29
last_completed_issue: 46
last_completed_research: AMBENCH-F28
last_decision: DEC-060
created: 2026-08-22
updated: 2026-08-23
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Current State / 현재 상태
- Active Issue: #47 `AMBENCH-E29`.
- Last completed: #46 `AMBENCH-F28 — PASS_F28_PLATE_SPECIFIC_GEOMETRY_SOURCE_READY`.
- `DEC-055`: v2.1 + compact Shared Capability/Portfolio Continuity Overlay active; no mission reset.
- `DEC-060`: E29 preregistration active; numerical execution is authorized only under the frozen design and zero-cost gate.

## E29 frozen experiment / E29 고정 실험
- groups: T72/T82/T92 at 0.75 ms vs T102/T112/T122 at 5.0 ms;
- independent replicate: physical plate;
- P1 only;
- source: F28-verified current NIST `mds2-4103` immutable P1 components + authoritative README + exact Micrographs surface-reference component;
- reconstruction: `(overlap_depth_y - surface_y_reference) * authoritative pixel_scale_um_per_px`;
- no sign flip, alternate scale, source substitution, P2/P3 rescue or imputation;
- >=41/45 valid overlap-depth tracks required per plate;
- primary plate endpoint: arithmetic mean of valid reconstructed P1 track overlap depths;
- direction: `0.75 ms > 5.0 ms`, inherited from E27 before its parser incident;
- exact one-sided 20-allocation permutation on six plate endpoints;
- plate-level rank-biserial `r_rb`; strong threshold >=7/9;
- common-valid track sensitivity requires >=36/45 common tracks and positive `Delta_common` for strong PASS.

Frozen gates:
- `PASS_E29_STRONG_DIRECTIONAL_EFFECT`
- `MIXED_E29_DIRECTIONAL_SIGNAL`
- `NO_MATERIAL_GAIN_E29`
- `HOLD_E29_INTEGRITY_OR_COVERAGE`

Exposure disclosure:
`NEW_E29_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Minimum Operability / 최소 운영
All seven required functions remain PRESENT/EQUIVALENT; no `MISSING-BLOCKING` state and no new duplicate control file required.

## Capability / Portfolio
Recurring NERDm/source-integrity/reconstruction/evidence workflow remains `SHARED-INTERNAL-CANDIDATE`. Central Capability Repository/shared-content/shared-infrastructure/shared-resource reconciliation is nonblocking. Never assume shared paid quota/budget without canonical ledger evidence.

## Exact Next Action / 정확한 다음 행동
Execute E29 only after this synchronized preregistration state:
1. re-query current NERDm identities/hashes;
2. transiently retrieve six P1 components, Micrographs surface-reference table, and authoritative README;
3. parse the one documented physical pixel scale;
4. reconstruct plate track depths with the frozen formula;
5. enforce source, unique-binding, nonnegative reconstruction and >=41/45 coverage gates;
6. compute six plate endpoints, exact permutation p, plate-level rank-biserial, common-track sensitivity;
7. commit only sanitized aggregate results;
8. apply frozen gate, persist decision/claims/memory, close/HOLD #47, synchronize STATUS/HANDOFF and re-read.

Any potentially billable action requires explicit prior user approval.
