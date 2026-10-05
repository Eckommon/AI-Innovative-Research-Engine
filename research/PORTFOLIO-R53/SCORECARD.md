---
id: PORTFOLIO-R53-SCORECARD
type: immutable-stage0-scorecard
created: 2026-10-06
issue: 193
contract: 0015791279ada44f79201c155acdc03a21da96ac
revalidation: 56ba44bac21ff65dc6f8544713b07379ebe40dc2
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R53 — immutable survivor-first /45 scorecard

This is the single scorecard authorized by the frozen R53 contract. Scores may not be changed after this commit.

| Dimension | US-CMS-NH-001 | US-FRA-RR-001 | UK-FHRS-EST-001 | AU-ACQSC-CARE-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 4 | 5 |
| 2. Cross-dataset / cross-table information gain | 5 | 5 | 4 | 4 |
| 3. Direct future-event quality | 5 | 5 | 4 | 3 |
| 4. Independent-unit prospect | 5 | 4 | 5 | 5 |
| 5. Practical decision value | 5 | 5 | 4 | 5 |
| 6. Zero-cost operability | 5 | 5 | 5 | 4 |
| 7. Source-native/deterministic join defensibility | 5 | 4 | 5 | 5 |
| 8. Next-gate information gain / survivor probability | 5 | 5 | 3 | 2 |
| 9. Low overlap / novelty risk | 2 | 3 | 3 | 3 |
| **Total /45** | **42** | **41** | **37** | **36** |

## Candidate dispositions

### US-CMS-NH-001 — 42/45 — SELECT_F01

Selection is driven by survivor probability, not novelty:
- exact CCN across active-provider, inspection, deficiency and penalty tables;
- large active provider cohort;
- dense historical deficiency ledger;
- explicit standard-survey opportunity to control ascertainment;
- archived/recurring source surfaces that can be tested before any future survey outcome is opened.

Novelty is deliberately scored only 2/5 because staffing/ownership/deficiency relationships are established research themes.

### US-FRA-RR-001 — 41/45 — HOLD_STRONG_ALTERNATIVE_IDENTITY_REGIME_ADJUDICATION

FRA has excellent operational and accident source depth and frequent events. It trails CMS only because railroad-code continuity, mergers/consolidations and changing reportability thresholds require more F01 adjudication before a stable prospective unit can be guaranteed.

### UK-FHRS-EST-001 — 37/45 — HOLD_HISTORICAL_RATING_LINEAGE_UNPROVEN

Exact FHRSID and current rating semantics are strong, but R53 did not establish a sufficiently reproducible row-bearing historical rating ledger. Current/latest-state API strength alone is not enough after recent source-lineage failures.

### AU-ACQSC-CARE-001 — 36/45 — HOLD_REGIME_TRANSITION_AND_EVENT_SUPPORT

Current Provider ID is strong, but the Aged Care Act 2024 transition weakens historical comparability and provider-level suspension/revocation support is less certain and likely less dense.

## Frozen selection

**`SELECT_US_CMS_NH_001_STANDARD_SURVEY_SERIOUS_DEFICIENCY_F01`**

No tie-break is required.

## Authorized next gate

Exactly one separate outcome-blind `US-CMS-NH-F01` may be designed.

Before any future standard-survey deficiency membership is opened, F01 must prove:
1. exact CCN syntax/coverage and uniqueness in active Provider Information;
2. ≥12 independently fingerprintable archived monthly CMS nursing-home releases under one frozen window;
3. deterministic CCN joins across Provider Information, Inspection Dates and Health Deficiencies;
4. source-native standard-health-survey identification;
5. source-native scope/severity semantics and a prospectively fixed serious-deficiency threshold;
6. sufficient historical standard-survey and serious-deficiency event support;
7. inspection-date completeness;
8. stable active-provider longitudinal support;
9. exclusion of all prior/current ratings, deficiency/penalty/enforcement variables from predictive exposures;
10. future monthly-refresh and future standard-survey membership seal;
11. zero incremental monetary cost.

If archived monthly releases are not independently row-bearing/fingerprintable, or exact standard-survey outcome ascertainment cannot be separated from complaint/other inspections, F01 must HOLD.

## Non-claims

R53 establishes no nursing-home deficiency relationship, railroad accident relationship, food-hygiene rating relationship, aged-care regulatory-event relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
