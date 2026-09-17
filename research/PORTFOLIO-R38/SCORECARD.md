---
id: PORTFOLIO-R38-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-18
issue: 159
contract_commit: 81216245922df756667295a4ffeb89fb41bd274f
revalidation_commit: 51c51480bd1adff6e37676266d15b42a54ca29fd
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R38 immutable scorecard / 불변 평가표

Exactly one scorecard under the frozen nine-dimension `/45` rubric.

| Candidate | Bottleneck | Cross-data | Outcome | Independent units | Practical | $0 operability | Exact join | Next-gate info | Low overlap | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `US-FDIC-BRANCH-001` | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 2 | **39** | **SELECT_F01** |
| `US-CMS-DIALYSIS-001` | 4 | 4 | 3 | 5 | 5 | 5 | 5 | 4 | 1 | **36** | HOLD_MATURE_QUALITY_FRAMEWORK |
| `US-FRA-XING-001` | 3 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 0 | **35** | HOLD_DIRECT_PREDICTION_OVERLAP |
| `US-FCC-BDC-001` | 4 | 3 | 3 | 5 | 4 | 4 | 3 | 5 | 3 | **34** | HOLD_IDENTITY_AND_OUTCOME_AMBIGUITY |

No tie-break is required.

## Selection rationale

`US-FDIC-BRANCH-001` has the best mission-ROI after conservative overlap penalties. SOD and BankFind expose source-native branch/institution identifiers at large national scale, while an outcome-blind F01 can cheaply test the hardest unresolved assumption: whether exact branch identity/history can distinguish genuine closure/non-continuation from acquisition, sale/lease, merger or identifier transition without name/address reconciliation.

The score deliberately gives only **2/5** on low-overlap/novelty because FDIC itself has analyzed branch openings/closures and lower-deposit closure patterns. Therefore any descendant branch must not present generic deposit→closure association as novel.

FRA receives **0/5** for low-overlap because FRA GXAPS and extensive contemporary literature already perform crossing-inventory→collision prediction using the same core datasets/identity. CMS is technically clean but embedded in a mature ESRD quality framework. FCC retains useful information gain but Provider-ID nullability and withdrawal semantics weaken exact prospective identity/outcome quality.

## Boundary

Candidate future event rows remain unopened. This scorecard authorizes only a separate outcome-blind FDIC structural F01 contract; it establishes no branch-closure relationship, prediction, ranking, causal effect or novelty claim. Cost: 0 USD.
