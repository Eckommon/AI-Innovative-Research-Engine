---
id: PORTFOLIO-R49-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-30
issue: 186
contract: 02c6730b43ff9e73a7933587b9a4d862b2637c9f
revalidation: f0110bce638973cd8236c11391f82db2b6dc0416
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R49 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R49 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-SEC-IA-001 | US-CMS-NPI-001 | US-EPA-RCRA-001 | US-FDA-DEV-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 4 | 5 | 5 | 5 |
| 2. Cross-dataset / cross-table information gain | 5 | 4 | 5 | 5 |
| 3. Direct future-event quality | 4 | 3 | 4 | 5 |
| 4. Independent-unit prospect | 5 | 5 | 5 | 4 |
| 5. Practical decision value | 4 | 5 | 5 | 5 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 5 | 5 | 4 |
| 8. Longitudinal + prospective common-support information gain | 5 | 3 | 4 | 3 |
| 9. Low overlap / novelty risk | 3 | 3 | 2 | 2 |
| **Total /45** | **40** | **38** | **40** | **38** |

## Tie-break / 동점 판정

SEC and RCRA tie at **40/45**.

Frozen tie-break:
1. deterministic join defensibility: SEC 5 = RCRA 5;
2. longitudinal + prospective common-support information gain: **SEC 5 > RCRA 4**.

Therefore the tie resolves to SEC.

## Candidate dispositions / 후보 판정

### US-SEC-IA-001 — 40/45 — SELECT_F01

- Historical ADV and ADV-W filing lineage is explicit and long-lived.
- Firm-level CRD identity appears in both official forms when assigned.
- Full versus partial withdrawal is source-native.
- Broad adviser business-structure covariates give a credible path to sizable comparable arms before future withdrawal access.
- Withdrawal remains a registration event, not a presumed business failure.

### US-EPA-RCRA-001 — 40/45 — HOLD_SELECTION_BIAS_COMMON_SUPPORT_RISK

- Exact site keys and dated enforcement/evaluation history are excellent.
- However, formal enforcement is conditional on inspection/regulatory attention, so a structure-only prospective comparison may have substantial selection/common-support problems.
- Keep as a strong future candidate under an inspection-opportunity-aware design.

### US-CMS-NPI-001 — 38/45 — HOLD_EVENT_HETEROGENEITY_AND_REACTIVATION

- NPI identity and scale are excellent.
- Deactivation reasons are heterogeneous and reactivation is allowed.
- Current replacement-file architecture does not itself prove historical snapshot availability.
- Deactivation may not be interpreted as closure/licensure loss.

### US-FDA-DEV-001 — 38/45 — HOLD_ESTABLISHMENT_ATTRIBUTION_MANY_TO_MANY

- Recall is a direct and valuable event with long history.
- Establishment-level attribution through FEI/registration harmonization is not assumed complete.
- Product-level recalls create many-to-many establishment/listing structure and common-support risk.

## Frozen selection / 고정 선정

**`SELECT_US_SEC_IA_001_ADVISER_STRUCTURE_TO_FUTURE_FULL_ADVW_WITHDRAWAL_F01`**

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-SEC-IA-F01` may be designed.

Before any post-cutoff withdrawal membership is opened, F01 must freeze and test:
1. exact Organization CRD identity syntax/coverage in baseline ADV;
2. exact CRD support in historical ADV-W;
3. full versus partial withdrawal classification;
4. historical filing lineage and source fingerprints;
5. current active SEC-adviser support;
6. source-native filing/withdrawal date semantics;
7. SEC→state and SEC→exempt-reporting-adviser transition handling;
8. future filing cutoff and membership seal;
9. prohibition on direct withdrawal/ineligibility/cessation fields as predictive exposures;
10. zero incremental monetary cost.

PASS may authorize only a separate outcome-blind N01.

## Non-claims / 비주장

R49 establishes no adviser-withdrawal relationship, NPI-deactivation relationship, RCRA-enforcement relationship, device-recall relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
