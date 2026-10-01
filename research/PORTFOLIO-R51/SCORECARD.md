---
id: PORTFOLIO-R51-SCORECARD
type: immutable-stage0-scorecard
created: 2026-10-02
issue: 189
contract: b6a3f3ffed0fc1c076c4088150a1b9397c215863
revalidation: 7319d62b441618a9f43ba49911e51064cda79c00
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R51 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R51 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-PHMSA-PIPE-001 | US-FAA-AIR-001 | US-CMS-REV-001 | US-NCUA-CU-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 4 | 5 | 5 |
| 2. Cross-table / cross-source information gain | 5 | 4 | 5 | 5 |
| 3. Direct future-event quality | 5 | 4 | 5 | 5 |
| 4. Independent-unit prospect | 5 | 5 | 4 | 5 |
| 5. Practical decision value | 5 | 4 | 5 | 5 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 3 | 5 | 2 |
| 8. True longitudinal + prospective common-support information gain | 5 | 5 | 3 | 4 |
| 9. Low overlap / novelty risk | 2 | 4 | 3 | 4 |
| **Total /45** | **42** | **38** | **40** | **40** |

## Candidate dispositions

### US-PHMSA-PIPE-001 — 42/45 — SELECT_F01

- Source-native Operator ID, annual infrastructure reports and incident files create a strong exact-identity / cross-source architecture.
- Historical forms and report lineage are explicit rather than inferred from update cadence.
- A single facility family can be frozen prospectively to preserve common support.
- Prior FMCSA×PHMSA highway-hazmat access friction and mature safety literature reduce low-overlap credit, but do not make this the same terminal route.

### US-CMS-REV-001 — 40/45 — HOLD_HISTORICAL_RETENTION_SURVIVOR_SELECTION_RISK

- ENRLMT_ID identity and revocation semantics are exceptionally strong.
- Current revoked-under-bar retention is not a complete historical event archive.
- Current approved-enrollment baseline creates survivor/common-support uncertainty.
- Keep as a high-value future candidate if a complete event lineage can be established prospectively.

### US-NCUA-CU-001 — 40/45 — HOLD_EVENT_KEY_AND_RARE_EVENT_RISK

- Quarterly call-report history since 1994 is excellent.
- Involuntary liquidation is a direct institutional event.
- The current event surface does not directly demonstrate the same charter identifier as the call-report source, so exact join defensibility is materially weaker.
- Rare future liquidation count may also make N01 support thin.

### US-FAA-AIR-001 — 38/45 — HOLD_STABLE_IDENTITY_ADJUDICATION_REQUIRED

- Current and yearly archived registry bodies are unusually strong.
- Deregistered Aircraft is a direct source-native event file.
- N-number reassignment prevents treating N-number alone as a stable aircraft identity.
- F01 would need to prove a documented exact stable identity/composite before any prospective design.

## Frozen selection / 고정 선정

**`SELECT_US_PHMSA_PIPE_001_OPERATOR_STRUCTURE_TO_FUTURE_REPORTABLE_INCIDENT_F01`**

No tie-break is required.

## Authorized next gate

Exactly one separate outcome-blind `US-PHMSA-PIPE-F01` may be designed.

Before any future incident membership is opened, F01 must prospectively freeze and test:

1. exactly one pipeline facility family;
2. exact Operator ID syntax and continuity;
3. annual-report source lineage across multiple years;
4. incident-file source access and schema;
5. exact annual-report ↔ incident Operator ID joinability;
6. source-native incident date and severity semantics;
7. sufficient active/operator support;
8. historical incident support;
9. operator reorganizations/ID changes;
10. non-tautological structural fields;
11. future incident-source firewall;
12. plausible N01 common support;
13. zero incremental monetary cost.

## Non-claims

R51 establishes no pipeline-incident relationship, aircraft-deregistration relationship, Medicare-revocation relationship, credit-union-liquidation relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
