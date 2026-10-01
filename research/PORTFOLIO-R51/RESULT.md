---
id: PORTFOLIO-R51-RESULT
type: stage0-portfolio-selection
created: 2026-10-02
issue: 189
state: COMPLETED_SELECTED
selection: SELECT_US_PHMSA_PIPE_001_OPERATOR_STRUCTURE_TO_FUTURE_REPORTABLE_INCIDENT_F01
scorecard_commit: a18a4b8a4972cbc20b076969140ef7c65c50e0bf
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R51 Result / 결과

**`SELECT_US_PHMSA_PIPE_001_OPERATOR_STRUCTURE_TO_FUTURE_REPORTABLE_INCIDENT_F01`**

R51 executed the terminal-equivalence-aware candidate universe frozen before Issue binding at `b6a3f3ffed0fc1c076c4088150a1b9397c215863`, revalidation at `7319d62b441618a9f43ba49911e51064cda79c00`, and the single immutable scorecard at `a18a4b8a4972cbc20b076969140ef7c65c50e0bf`.

## Immutable ranking

| Candidate | Score /45 | Disposition |
|---|---:|---|
| `US-PHMSA-PIPE-001` | **42** | **SELECT_F01** |
| `US-CMS-REV-001` | **40** | HOLD_HISTORICAL_RETENTION_SURVIVOR_SELECTION_RISK |
| `US-NCUA-CU-001` | **40** | HOLD_EVENT_KEY_AND_RARE_EVENT_RISK |
| `US-FAA-AIR-001` | **38** | HOLD_STABLE_IDENTITY_ADJUDICATION_REQUIRED |

No tie-break was required.

## Why PHMSA

PHMSA provides the strongest combined architecture in the frozen pool:
- source-native Operator ID;
- annual-report infrastructure data;
- free incident/accident source files;
- explicit historical forms/lineage;
- large operator/infrastructure structure suitable for one prospectively frozen facility family.

This route is not equivalent to the prior FMCSA×PHMSA highway-hazmat branch, which used carrier-level FMCSA inspection data and highway hazardous-material incidents.

## Authorized next work

Exactly one separate outcome-blind `US-PHMSA-PIPE-F01` may be frozen.

F01 must prove one frozen facility family, exact OpID continuity, multi-year annual-report lineage, incident source/schema access, exact annual↔incident joins, historical event support, event severity/date semantics, future-event sealing and non-tautological structural support before N01.

## Non-claims

R51 establishes no pipeline-incident relationship, aircraft-deregistration relationship, Medicare-revocation relationship, credit-union-liquidation relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
