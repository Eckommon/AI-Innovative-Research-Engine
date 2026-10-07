---
id: PORTFOLIO-R54-SCORECARD
type: immutable-stage0-scorecard
created: 2026-10-08
issue: 195
contract: bc9b5b49481ea2b44a2aac842f0a255e1d0de619
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R54 — immutable /45 scorecard

| Dimension | US-FRA-RR-001 | US-EPA-RCRA-001 | US-FAA-NTSB-AIR-001 | US-NHTSA-REC-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 4 | 4 |
| 2. Cross-table information gain | 5 | 5 | 4 | 3 |
| 3. Direct future-event quality | 5 | 4 | 4 | 5 |
| 4. Independent-unit prospect | 5 | 5 | 4 | 3 |
| 5. Practical decision value | 5 | 5 | 4 | 4 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 4 | 5 | 3 | 3 |
| 8. Next-gate survivor probability | 5 | 4 | 3 | 3 |
| 9. Low overlap / novelty risk | 4 | 4 | 4 | 4 |
| **Total /45** | **43** | **42** | **35** | **34** |

## Frozen selection

**`SELECT_US_FRA_RR_001_OPERATIONAL_STRUCTURE_TO_FUTURE_REPORTABLE_TRAIN_ACCIDENT_F01`**

No tie-break is required.

FRA wins despite RCRA's slightly stronger exact table key because FRA has superior event-opportunity design and next-gate survivor probability: annual railroad operational exposure and reportable train accidents are both source-native without conditioning the primary outcome on a regulator-selected inspection.

## Authorized next gate

Exactly one separate outcome-blind `US-FRA-RR-F01` may be frozen. It must establish:
- source-native railroad reference identity and merger/consolidation handling;
- ≥5 years of directly retrievable Form 55 operational rows;
- matching Form 54 accident lineage;
- applicable annual accident-reporting threshold semantics;
- sufficient active railroad and accident support;
- temporal exposure/outcome separation;
- future-year/event seal;
- no prior accident/casualty predictors;
- cost 0.

Incremental monetary cost: **0 USD**.
