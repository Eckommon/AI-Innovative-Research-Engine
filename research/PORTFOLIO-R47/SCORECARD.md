---
id: PORTFOLIO-R47-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-30
issue: 181
contract: c3bfe8cd3f85516e7adf4e700103992ab9a29193
revalidation: be77edbf75164a0ef50e7d932c146f1e81fa8a29
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R47 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R47 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-EPA-SDWIS-001 | US-ED-POSTSEC-001 | AU-ASIC-COMP-001 | EU-EMAS-ORG-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 4 | 4 |
| 2. Cross-dataset / cross-table information gain | 5 | 5 | 3 | 4 |
| 3. Direct future-event quality | 5 | 5 | 4 | 2 |
| 4. Independent-unit prospect | 5 | 4 | 5 | 5 |
| 5. Practical decision value | 5 | 5 | 4 | 4 |
| 6. Zero-cost operability | 5 | 5 | 5 | 4 |
| 7. Source-native/deterministic join defensibility | 5 | 3 | 5 | 4 |
| 8. Next-gate information gain | 5 | 5 | 4 | 5 |
| 9. Low overlap / novelty risk | 3 | 1 | 1 | 2 |
| **Total /45** | **43** | **38** | **35** | **34** |

## Candidate dispositions / 후보 판정

### US-EPA-SDWIS-001 — 43/45 — SELECT_F01

- Official quarterly national ZIP/CSV architecture already defines exact `SUBMISSIONYEARQUARTER + PWSID` joins across system, facilities, violations and enforcement tables.
- PWSID is source-native and highly defensible.
- The public-health/regulatory event family is direct, but descendant design must prohibit current/prior compliance and enforcement variables from becoming tautological predictors.
- Novelty credit is conservative because drinking-water compliance research exists; selection rests on prospective design quality and mission information gain, not domain novelty.

### US-ED-POSTSEC-001 — 38/45 — HOLD_MATURE_CLOSURE_PREDICTION_AND_IDENTITY_CROSSWALK

- Official closure events and dates are strong.
- OPEID↔UNITID granularity and branch/location identity require substantial structural validation.
- Recent high-quality college-closure prediction research sharply reduces novelty/marginal portfolio value.

### AU-ASIC-COMP-001 — 35/45 — HOLD_COMPANY_REGISTRY_OVERLAP

- ACN and weekly current snapshots are operationally strong and deregistration date is directly exposed.
- Bounded deregistered-company retention and event-reason heterogeneity remain important.
- Immediate overlap with CA-CORP and mature corporate-closure research substantially reduces marginal value.

### EU-EMAS-ORG-001 — 34/45 — HOLD_HISTORICAL_DEREGISTRATION_LINEAGE_UNPROVEN

- Current positive register and Excel download are useful.
- Historical deregistration/end-state lineage is not yet established, and disappearance may not be interpreted as an event.
- Prior EMAS withdrawal/drop-out studies also reduce novelty credit.

## Frozen selection / 고정 선정

**`SELECT_US_EPA_SDWIS_001_PUBLIC_WATER_SYSTEM_STRUCTURE_TO_FUTURE_HEALTH_BASED_VIOLATION_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-EPA-SDWIS-F01` may be designed. Before any future violation membership is opened, F01 must freeze and test:

1. exact PWSID syntax and system-level cardinality;
2. reproducible quarterly SDWIS ZIP/snapshot lineage;
3. active public-water-system support;
4. deterministic system/facility/table joins under `SUBMISSIONYEARQUARTER + PWSID`;
5. historical violation/event taxonomy and dates;
6. a prospectively fixed **health-based / serious compliance event** hierarchy;
7. merger/deactivation/inactive-system competing states;
8. reporting-lag handling and a future-quarter firewall;
9. prohibition on violation/enforcement/current-compliance fields as predictive exposures;
10. zero incremental monetary cost.

If exact temporal lineage or a defensible non-tautological event design cannot be established, F01 must HOLD.

## Non-claims / 비주장

The scorecard establishes no drinking-water violation relationship, college-closure relationship, company-deregistration relationship, EMAS-registration-end relationship, prediction, ranking, causal effect or novelty claim. No candidate future-event membership was used in scoring.

Incremental monetary cost: **0 USD**.
