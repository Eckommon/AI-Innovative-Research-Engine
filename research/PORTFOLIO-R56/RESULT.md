---
id: PORTFOLIO-R56-RESULT
type: stage0-portfolio-selection
created: 2026-10-13
issue: 200
state: COMPLETED_SELECTED
selection: SELECT_US_CMS_NPI_002_ACTIVE_TYPE2_STRUCTURE_TO_FUTURE_NPI_DEACTIVATION_F01
scorecard_commit: 4f547b58601ca7c39e0eff6a711e42777871bfdc
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R56 Result / 결과

**`SELECT_US_CMS_NPI_002_ACTIVE_TYPE2_STRUCTURE_TO_FUTURE_NPI_DEACTIVATION_F01`**

## Immutable ranking

| Candidate | Score /45 | Disposition |
|---|---:|---|
| `US-CMS-NPI-002` | **41** | **SELECT_F01 — tie-break winner** |
| `US-PHMSA-PIPE-002` | **41** | HOLD_TIEBREAK_N01_SURVIVOR |
| `US-FAA-AIR-002` | **38** | HOLD_COMPOUND_IDENTITY |
| `US-FCC-ULS-002` | **33** | HOLD_WEAK_EVENT_SEMANTICS_OVERLAP |

CMS and PHMSA tie at 41. The frozen first tie-break is N01 survivor probability; CMS scores 5 versus PHMSA 3.

CMS is selected because the current official architecture exposes a national monthly full replacement file, a separate monthly deactivation update and weekly incremental files under exact NPI identity. This creates the strongest expected arm scale and future-event opportunity after RCRA N01 failed on support.

Selection does not assert that deactivation equals provider closure, failure or quality harm.

No future membership was opened. Cost remains 0 USD.
