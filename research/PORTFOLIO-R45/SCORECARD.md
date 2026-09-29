---
id: PORTFOLIO-R45-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-29
issue: 176
contract: 01f4518bd72f5db542e437bd5669b9c0489efdc9
revalidation: 0f86e1a1fb4998fb56a6027ed0c6f1b55248e6f1
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R45 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R45 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-MSHA-MINE-001 | US-NCUA-CU-001 | US-CMS-NH-001 | US-FDA-PMA-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 5 | 4 |
| 2. Cross-dataset / cross-table information gain | 5 | 4 | 4 | 4 |
| 3. Direct future-event quality | 5 | 5 | 4 | 4 |
| 4. Independent-unit prospect | 5 | 5 | 5 | 5 |
| 5. Practical decision value | 5 | 5 | 5 | 4 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 4 | 5 | 5 |
| 8. Next-gate information gain | 5 | 5 | 4 | 5 |
| 9. Low overlap / novelty risk | 2 | 2 | 2 | 2 |
| **Total /45** | **42** | **40** | **39** | **38** |

## Candidate rationales / 후보별 근거

### US-MSHA-MINE-001 — 42/45 — SELECT_F01

- Exact Mine ID is the strongest identity prospect in the pool.
- Official quarterly employment/production and accident/injury datasets provide strong cross-table information gain and long historical lineage.
- Serious/fatal accident events have direct source-native severity semantics.
- Zero-cost operability is high and a bounded F01 can directly falsify Mine-ID coverage, severe-event semantics, historical support and future sealing.
- Novelty/overlap remains capped at 2 because mine-safety event modelling is a mature research field.

### US-NCUA-CU-001 — 40/45 — HOLD_CHARTER_EVENT_KEY_AND_FINANCIAL_OVERLAP

- Quarterly call-report history and involuntary liquidation semantics are strong.
- Event-table charter identity remains less directly exposed than the baseline charter identity and requires an official event-detail path.
- Financial-institution distress/exit overlaps conceptually with prior FDIC work.

### US-CMS-NH-001 — 39/45 — HOLD_TERMINATION_LINEAGE_BOUNDARY

- Exact CCN and rich provider/staffing/quality/inspection sources are strong.
- Direct termination notices exist, but bounded public notice retention creates historical-lineage uncertainty.
- Healthcare facility quality/termination is a mature field.

### US-FDA-PMA-001 — 38/45 — HOLD_ORIGINAL_PMA_EVENT_SEPARATION

- Exact PMA identity and formal withdrawal/suspension rules are strong.
- The public PMA database mixes original applications and supplements; F01 would need strict event-level separation.
- Immediate medical-regulatory overlap after EMA reduces marginal portfolio value.

## Frozen selection / 고정 선정

**`SELECT_US_MSHA_MINE_001_OPERATING_STRUCTURE_TO_SERIOUS_FATAL_ACCIDENT_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-MSHA-MINE-F01` may be designed. Before any future accident membership is opened, F01 must freeze and test:

1. official mine/master, quarterly employment/production and accident/injury source access;
2. exact Mine ID syntax/coverage across source families;
3. mine-level operating-population support;
4. historical accident/injury event date and degree/severity semantics;
5. deterministic separation of fatal/serious events from non-serious reportable incidents;
6. historical severe-event support/cardinality;
7. no operator/name/manual identity repair;
8. future accident-event firewall and deterministic fingerprints;
9. zero incremental monetary cost.

If exact Mine-ID linkage or severe-event semantics are not defensible from official source-native fields, F01 must HOLD rather than redefine the endpoint after observation.

## Non-claims / 비주장

The scorecard establishes no mine-accident relationship, credit-union liquidation relationship, nursing-home termination relationship, PMA-withdrawal relationship, prediction, ranking, causal effect or novelty claim. No candidate-specific future event membership was used in scoring.

Incremental monetary cost: **0 USD**.
