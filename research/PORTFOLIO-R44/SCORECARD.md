---
id: PORTFOLIO-R44-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-29
issue: 174
contract: 79d9417e186948cae224bdc43dc745436628a707
revalidation: 8f4919e209bc04e625a10057d6bd4ec16699e5ee
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R44 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R44 contract. Scores may not be changed after this commit.

| Dimension / 기준 | EU-EMA-MA-001 | US-FERC-HYDRO-001 | AU-ACNC-CHARITY-001 | UK-IPO-TM-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 4 | 4 | 3 |
| 2. Cross-dataset / cross-table information gain | 4 | 4 | 4 | 3 |
| 3. Direct future-event quality | 4 | 3 | 4 | 3 |
| 4. Independent-unit prospect | 5 | 5 | 5 | 4 |
| 5. Practical decision value | 5 | 4 | 4 | 3 |
| 6. Zero-cost operability | 5 | 4 | 5 | 3 |
| 7. Source-native/deterministic join defensibility | 5 | 5 | 5 | 5 |
| 8. Next-gate information gain | 5 | 5 | 3 | 5 |
| 9. Low overlap / novelty risk | 2 | 3 | 1 | 2 |
| **Total /45** | **40** | **37** | **35** | **31** |

## Candidate rationales / 후보별 근거

### EU-EMA-MA-001 — 40/45 — SELECT_F01

- Exact EMA product number and official authorisation/withdrawal dates are directly available.
- Official medicine tables are downloadable and updated automatically.
- Event quality is capped at 4, not 5, because commercial/voluntary withdrawal, safety/regulatory withdrawal, suspension, expiry and application withdrawal must remain separate.
- Next-gate information gain is maximal because one outcome-blind F01 can directly test current source lineage, exact identity, event-reason/date semantics and support before any future membership is opened.
- Novelty/overlap remains conservative because medicine withdrawal is a mature regulatory topic.

### US-FERC-HYDRO-001 — 37/45 — HOLD_EVENT_SOURCE_NOT_YET_ESTABLISHED

- Exact FERC Project Number and current public Active Licenses data provide strong identity and baseline support prospects.
- Event quality is capped at 3 because a deterministic historical surrender/termination source has not yet been established.
- High next-gate value remains, but source uncertainty keeps this branch below EMA.

### AU-ACNC-CHARITY-001 — 35/45 — HOLD_NONPROFIT_OVERLAP_AND_TAUTOLOGY_RISK

- Exact ABN and public Charity Register/AIS datasets are strong.
- Revocation is a direct legal event prospect, but filing-default/nonlodgment fields create mechanical leakage risk.
- Severe conceptual overlap with prior IRS/UK-charity work materially reduces marginal information value.

### UK-IPO-TM-001 — 31/45 — HOLD_BULK_STATUS_LINEAGE_NOT_ESTABLISHED

- Exact UK application number is highly defensible.
- Public journal pages are clear at individual-record level.
- Anonymous zero-cost bulk historical/current status lineage remains unproven, and ordinary expiry is not an acceptable adverse endpoint.
- The branch therefore remains lower priority despite a valuable falsification question.

## Frozen selection / 고정 선정

**`SELECT_EU_EMA_MA_001_MEDICINE_STRUCTURE_TO_AUTHORISATION_WITHDRAWAL_SUSPENSION_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `EU-EMA-MA-F01` may be designed. Before any future withdrawal/suspension membership is opened, F01 must freeze and test:

1. official downloadable medicine-table access and deterministic source fingerprinting;
2. exact EMA product-number syntax/coverage;
3. centrally authorised medicine population and minimum support;
4. current/historical authorisation date and legal-status semantics;
5. source-native withdrawal/suspension date and reason semantics that distinguish voluntary/commercial withdrawal from safety/regulatory action, expiry and application withdrawal;
6. historical event lineage and sufficient event support;
7. mechanically sealed future event membership;
8. zero incremental monetary cost.

If current public sources do not permit deterministic product-level event reason/date adjudication, F01 must HOLD rather than collapse heterogeneous events.

## Non-claims / 비주장

The scorecard establishes no medicine-withdrawal relationship, hydropower-licence termination relationship, charity-revocation relationship, trade-mark adverse-status relationship, prediction, ranking, causal effect or novelty claim. No candidate-specific future event membership was used in scoring.

Incremental monetary cost: **0 USD**.
