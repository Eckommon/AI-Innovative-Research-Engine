---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260823-E30-PREREGISTERED-EXECUTION-ACTIVE
active_issue: 48
active_research: AMBENCH-E30
last_completed_issue: 47
last_completed_research: AMBENCH-E29
last_decision: DEC-062
created: 2026-08-22
updated: 2026-08-23
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Current State / 현재 상태
- Active Issue: #48 `AMBENCH-E30`.
- Last completed: #47 `AMBENCH-E29 — PASS_E29_STRONG_DIRECTIONAL_EFFECT`.
- `DEC-055`: v2.1 + compact Shared Capability/Portfolio Continuity Overlay active.
- `DEC-062`: E30 P2/P3 spatial robustness falsification preregistered.

## E29 anchor / E29 기준점
P1 physical-plate n=3 vs n=3: `Delta_primary = 29.083049409 µm`, exact one-sided `p=0.05`, plate rank-biserial `1.0`, 44 common-valid tracks, same-direction common sensitivity. Strong internal directional signal only, not broad causal proof.

## Active E30 design / 활성 E30 설계
- same six plates: T72/T82/T92 vs T102/T112/T122;
- P2/P3 only and nested within physical plate;
- same NIST authoritative pixel/reference/scale reconstruction contract;
- >=41/45 valid tracks required in every plate-position cell;
- one arithmetic mean per plate-position;
- one equal-weight combined robustness endpoint per plate: `(P2 mean + P3 mean)/2`;
- diagnostics `Delta_P2`, `Delta_P3`;
- primary `Delta_combined` and exact one-sided 20-allocation permutation on six plate endpoints;
- combined rank-biserial threshold >=7/9;
- global common-valid tracks across all 12 cells >=36/45 and positive `Delta_common_combined` required for strong PASS;
- combined Delta <=0 with integrity pass => `FALSIFIED_E30_SPATIAL_GENERALITY`;
- no P1 rescue, P2/P3 dropping, unequal post-hoc weighting, imputation, pseudo-replication, endpoint search, sign/scale/source change or model escalation.

Exposure:
`NEW_E30_NUMERICAL_OUTCOME_BLIND = NO__INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

## Minimum Operability / 최소 운영
All seven functions remain PRESENT/EQUIVALENT; no `MISSING-BLOCKING` and no duplicate control file required.

## Capability / Portfolio
Recurring preregistration + immutable-source + exact-small-n workflow remains `SHARED-INTERNAL-CANDIDATE`. Shared content/infrastructure/resource reconciliation remains nonblocking; shared paid resource availability is not assumed.

## Exact Next Action / 정확한 다음 행동
Execute E30 only after this state sync: current NERDm exact identity/hash validation for root README, Micrographs surface-reference and all 12 P2/P3 components; frozen reconstruction and >=41/45 coverage; sanitized aggregates only; frozen robustness/falsification gate; durable claims/decision/memory; close Issue #48; synchronize STATUS/HANDOFF and re-read.

Any potentially billable action requires explicit prior approval.
