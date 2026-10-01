---
id: PORTFOLIO-R50-SCORECARD
type: immutable-stage0-scorecard
created: 2026-10-01
issue: 188
contract: 4bee3df90e8b174b1851f921eff097f6f5dda00d
revalidation: 8515e7c5469112a9175e49f19601b1f7b0134669
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R50 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R50 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-FCC-ULS-001 | US-FAA-AIR-001 | US-CMS-REV-001 | US-FDA-DECRS-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 4 | 4 | 5 | 4 |
| 2. Cross-table / cross-source information gain | 5 | 4 | 5 | 4 |
| 3. Direct future-event quality | 5 | 4 | 5 | 3 |
| 4. Independent-unit prospect | 5 | 5 | 4 | 4 |
| 5. Practical decision value | 4 | 4 | 5 | 4 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 4 | 5 | 4 |
| 8. True longitudinal + prospective common-support information gain | 5 | 5 | 3 | 2 |
| 9. Low overlap / novelty risk | 3 | 4 | 2 | 2 |
| **Total /45** | **41** | **39** | **39** | **32** |

## Candidate dispositions / 후보 판정

### US-FCC-ULS-001 — 41/45 — SELECT_F01

- Source-native 9-digit Unique System Identifier explicitly handles call-sign reassignment.
- Complete weekly files plus daily transaction files create a strong historical/prospective lineage architecture.
- Canceled and Terminated are direct status classes and can remain distinct from Expired.
- Event ascertainment does not inherently require an inspection/enforcement-selection filter.
- Strong expected common support can be tested within a single prospectively frozen radio-service family before future transactions are opened.

### US-FAA-AIR-001 — 39/45 — HOLD_IDENTITY_ADJUDICATION_REQUIRED

- Daily registry, yearly archives and a source-native deregistered-aircraft file are unusually strong.
- Aircraft deregistration is direct but heterogeneous.
- Exact stable identity requires F01 adjudication because N-number alone is reassignable and an exact composite has not yet been established.
- Keep as a high-value future candidate if FCC fails structurally.

### US-CMS-REV-001 — 39/45 — HOLD_HISTORICAL_RETENTION_COMMON_SUPPORT_RISK

- ENRLMT_ID and revocation effective dates/reasons are excellent.
- The revoked dataset is restricted to entities currently revoked and still under a re-enrollment bar rather than a complete historical revocation archive.
- This creates prospective retention/common-support uncertainty despite strong identity.

### US-FDA-DECRS-001 — 32/45 — HOLD_HETEROGENEOUS_END_STATE_LINEAGE

- Daily current registration is operationally useful.
- Removal combines enforcement inactivation, expiration, deregistration and other drops.
- Historical reason-specific end-state lineage is not yet sufficiently demonstrated.

## Frozen selection / 고정 선정

**`SELECT_US_FCC_ULS_001_LICENSE_STRUCTURE_TO_FUTURE_CANCEL_TERMINATE_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-FCC-ULS-F01` may be designed.

Before any future cancellation/termination membership is opened, F01 must prospectively freeze and test:

1. one radio-service family or a schema-compatible service set;
2. exact 9-digit Unique System Identifier syntax/coverage;
3. complete-file and daily-transaction lineage;
4. active-license baseline support;
5. Canceled/Terminated/Expired status separation;
6. source-native grant/expiration/cancellation date semantics;
7. historical C/T event support;
8. exact complete↔transaction identity continuity;
9. non-tautological baseline structural fields;
10. future daily-transaction firewall;
11. plausible N01 common support before future outcomes;
12. zero incremental monetary cost.

## Non-claims / 비주장

R50 establishes no FCC cancellation/termination relationship, FAA deregistration relationship, Medicare revocation relationship, FDA registration-end relationship, prediction, ranking, causal effect or novelty claim. No candidate future-event membership was used in scoring.

Incremental monetary cost: **0 USD**.
