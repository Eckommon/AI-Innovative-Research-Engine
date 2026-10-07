---
id: PORTFOLIO-R55-RESULT
type: stage0-portfolio-selection
created: 2026-10-08
issue: 197
state: COMPLETED_SELECTED
selection: SELECT_US_EPA_RCRA_001_HANDLER_STRUCTURE_TO_FUTURE_EVALUATION_CONDITIONED_VIOLATION_F01
scorecard_commit: f8949628b10a0af543b6240a601fcd307e7119bc
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R55 Result / 결과

**`SELECT_US_EPA_RCRA_001_HANDLER_STRUCTURE_TO_FUTURE_EVALUATION_CONDITIONED_VIOLATION_F01`**

## Immutable ranking

| Candidate | Score /45 | Disposition |
|---|---:|---|
| `US-EPA-RCRA-001` | **43** | **SELECT_F01** |
| `US-CMS-NPI-001` | **41** | HOLD_HETEROGENEOUS_DEACTIVATION |
| `US-FAA-AIR-001` | **39** | HOLD_TEMPORAL_IDENTITY_REUSE |
| `US-FDIC-BANK-001` | **38** | HOLD_RARE_MATURE_FAILURE_DOMAIN |

RCRA is selected because the direct official ZIP already contains source-native facility, evaluation, violation, enforcement, NAICS and monthly VIO/SNC history tables under documented handler keys. The next design can condition the future event on an actual evaluation opportunity instead of treating unevaluated handlers as non-events.

No future-event membership was opened. Cost remains 0 USD.
