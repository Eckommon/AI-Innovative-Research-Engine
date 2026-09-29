---
id: PORTFOLIO-R47-RESULT
type: stage0-portfolio-selection
created: 2026-09-30
issue: 181
state: COMPLETED_SELECTED
selection: SELECT_US_EPA_SDWIS_001_PUBLIC_WATER_SYSTEM_STRUCTURE_TO_FUTURE_HEALTH_BASED_VIOLATION_F01
scorecard_commit: 1b8a57f551b3d032ff8f66cfb2bcd6517042eb8d
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R47 Result / 결과

**`SELECT_US_EPA_SDWIS_001_PUBLIC_WATER_SYSTEM_STRUCTURE_TO_FUTURE_HEALTH_BASED_VIOLATION_F01`**

R47 executed the candidate universe frozen before Issue binding at `c3bfe8cd3f85516e7adf4e700103992ab9a29193`, bounded revalidation at `be77edbf75164a0ef50e7d932c146f1e81fa8a29`, and the single immutable scorecard at `1b8a57f551b3d032ff8f66cfb2bcd6517042eb8d`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-EPA-SDWIS-001` | **43** | **SELECT_F01** |
| `US-ED-POSTSEC-001` | **38** | HOLD_MATURE_CLOSURE_PREDICTION_AND_IDENTITY_CROSSWALK |
| `AU-ASIC-COMP-001` | **35** | HOLD_COMPANY_REGISTRY_OVERLAP |
| `EU-EMAS-ORG-001` | **34** | HOLD_HISTORICAL_DEREGISTRATION_LINEAGE_UNPROVEN |

No tie-break was required.

## Why SDWIS / SDWIS 선정 이유

EPA ECHO's SDWA national download already defines exact quarterly joins across public-water-system, facilities, violations/enforcement, site visits and related tables using `SUBMISSIONYEARQUARTER + PWSID`. PWSID is a documented two-letter state/region code plus seven digits. The data are zero-cost, nationwide and refreshed quarterly.

Selection does **not** assert that any system characteristic predicts a later violation. Any descendant must prohibit current/prior violation, enforcement-priority, unresolved-noncompliance and other direct outcome-proximal fields from becoming predictive exposures.

## Authorized next work / 허가되는 다음 작업

Exactly one separate outcome-blind `US-EPA-SDWIS-F01` may be frozen next. It must prove exact PWSID identity, quarterly source lineage, active-system support, system/facility/violation join semantics, health-based event taxonomy, reporting-lag handling, competing merger/deactivation states and a future-refresh firewall before any future violation membership is opened.

## Non-claims / 비주장

R47 establishes no drinking-water violation relationship, college-closure relationship, company-deregistration relationship, EMAS-registration-end relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
