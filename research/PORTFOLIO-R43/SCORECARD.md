---
id: PORTFOLIO-R43-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-29
issue: 172
contract: a52045f7526c0f601d40cba0387d92141f90e75d
revalidation: 03a9d54874eac0a79f704ccb45a27def350f5e9a
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R43 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R43 contract. Scores may not be changed after this commit.

| Dimension / 기준 | CA-CORP-001 | UK-CHARITY-001 | UK-EA-PERMIT-001 | US-USDA-PACA-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 5 | 4 |
| 2. Cross-dataset / cross-table information gain | 4 | 4 | 4 | 2 |
| 3. Direct future-event quality | 5 | 4 | 5 | 5 |
| 4. Independent-unit prospect | 5 | 5 | 5 | 4 |
| 5. Practical decision value | 5 | 5 | 5 | 4 |
| 6. Zero-cost operability | 5 | 5 | 4 | 4 |
| 7. Source-native/deterministic join defensibility | 5 | 5 | 4 | 2 |
| 8. Next-gate information gain | 5 | 4 | 4 | 5 |
| 9. Low overlap / novelty risk | 2 | 1 | 1 | 3 |
| **Total /45** | **41** | **38** | **37** | **33** |

## Candidate rationales / 후보별 근거

### CA-CORP-001 — 41/45 — SELECT_F01

- Exact source-native Corporation Number/corporationId and current anonymous JSON access provide strong deterministic identity.
- Monthly legal transactions distinguish non-compliance dissolution from other legal-state changes.
- Anti-tautology risk is explicit and testable: overdue-filing flags, intent-to-dissolve notices and dissolution-pending states are banned as exposure.
- The branch has high next-gate information value because one structural F01 can determine historical snapshot support, exact identity/cardinality, event-class separation and future sealing.
- Corporate dissolution/failure is mature, so novelty is scored conservatively at 2.

### UK-CHARITY-001 — 38/45 — HOLD_NONPROFIT_OVERLAP_AND_REMOVAL_HETEROGENEITY

- Daily full-register downloads and exact charity identity are strong.
- Removal reason is source-native but heterogeneous; removal is not equivalent to operational failure.
- Prior IRS-EO work creates direct nonprofit-registry overlap, so novelty/information gain are intentionally discounted.

### UK-EA-PERMIT-001 — 37/45 — HOLD_ENVIRONMENTAL_OVERLAP_AND_LICENCE_BOUNDARY

- Permit identity and surrender/revocation fields are strong.
- Anonymous public-register/API access exists, but some reusable datasets operate under the Environment Agency Conditional Licence.
- Prior EPA/RCRA/US-WW work creates substantial thematic and methodological overlap.

### US-USDA-PACA-001 — 33/45 — HOLD_BULK_HISTORY_AND_IDENTITY_NOT_ESTABLISHED

- Disciplinary-event quality is potentially direct.
- Revalidation did not establish a sufficiently strong anonymous bulk historical licence/event architecture or cross-source exact licence key.
- Complaint/disciplinary fields create strong leakage risk.
- The next gate remains informative, but deterministic join and cross-table information scores are too weak relative to Canada.

## Frozen selection / 고정 선정

**`SELECT_CA_CORP_001_FEDERAL_STRUCTURE_TO_NONCOMPLIANCE_DISSOLUTION_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `CA-CORP-F01` may be designed next. Before any future non-compliance dissolution membership is opened, F01 must prove or reject:

1. current anonymous zero-cost official federal-corporation dataset/API access;
2. exact Corporation Number/corporationId semantics and coverage;
3. a prospectively frozen historical baseline/snapshot with sufficient active corporations;
4. legal-state/event semantics separating section-212 non-compliance dissolution from voluntary dissolution, amalgamation and discontinuance;
5. an anti-tautology firewall excluding overdue-filing, dissolution-pending and intent-to-dissolve variables from exposure;
6. sufficient historical dissolution-event support and reproducible monthly transaction lineage;
7. a mechanically sealed future dissolution membership and deterministic source fingerprints.

A structural PASS would authorize only a separate outcome-blind N01 design.

## Non-claims / 비주장

The scorecard establishes no corporate-dissolution relationship, charity-removal relationship, permit-revocation relationship, PACA disciplinary relationship, prediction, ranking, causal effect or novelty claim. No candidate future-event membership was opened for scoring.

Incremental monetary cost: **0 USD**.
