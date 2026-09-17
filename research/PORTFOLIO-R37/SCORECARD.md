---
id: PORTFOLIO-R37-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-17
issue: 157
contract_commit: 7ad2e9bf392d3e8fdf41982d7e1a800eca377f5a
revalidation_commit: 5c79e690f5ea4745a9ca6be18829e8e6178a1509
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R37 Immutable Scorecard / 불변 점수표

This is the single scorecard authorized by the frozen R37 contract. Candidate future outcome rows, memberships, effect directions and relationship statistics remain unopened.

## Frozen rubric result

| Candidate | Bottleneck fit | Cross-dataset gain | Direct outcome | Independent units | Practical value | Zero-cost | Source-native join | Next-gate info gain | Low-overlap / novelty | Total /45 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `US-FSIS-SAMPLE-001` | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41** |
| `US-EPA-SDWIS-001` | 4 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **38** |
| `US-CMS-NH-001` | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 1 | **37** |
| `US-USASPEND-VENDOR-001` | 4 | 2 | 2 | 5 | 4 | 5 | 5 | 4 | 3 | **34** |

No tie-break is required.

## Selection

**`SELECT_US_FSIS_SAMPLE_001_ESTABLISHMENT_SAMPLING_TO_RECALL_F01`**

### Why FSIS leads

FSIS preserves the strongest remaining combination of a direct operational bottleneck, genuinely distinct official source families, a later directly observed event family, and a cheap structural falsification step. The key uncertainty is not whether FSIS performs pathogen sampling; it is whether historical establishment-specific sampling can be joined prospectively to later recall/public-health-alert records using only official establishment-number semantics with adequate coverage and without name/address repair.

The source-native-join score is deliberately **4/5, not 5/5**, because FSIS establishment numbers can carry regulatory prefixes/format variants and the later recall record family must first prove exact, documented normalization and identifier coverage before any outcome is opened.

### Why the others do not advance

- `US-EPA-SDWIS-001`: technically excellent exact `PWSID` structure, but exposure and outcome remain heavily embedded in the same mature SDWIS/ECHO compliance framework and have substantial direct literature overlap.
- `US-CMS-NH-001`: exact `CCN`, archives and facility cardinality are strong, but CMS already publishes turnover/staffing as quality constructs and direct turnover→deficiency/quality studies are mature.
- `US-USASPEND-VENDOR-001`: UEI continuity and cardinality are strong, but a future absence/interruption of awards is not a sufficiently direct adverse event and the exposure/outcome remain within the same spending platform.

## Authorization boundary

R37 authorizes only a separate outcome-blind `US-FSIS-SAMPLE-F01` structural/source/identity/cardinality gate.

It does **not** authorize opening later recall membership, calculating pathogen→recall relationships, establishment risk ranking, recall prediction, causal claims, food-safety recommendations, or novelty claims.

Incremental monetary cost: **0 USD**.
