---
id: PORTFOLIO-R41-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-21
issue: 167
contract: b3e5e1cac40ba05e839930ed6dcd2e8d1d3962b0
revalidation: 4f481865e2690ee0c6d7716daeb814c4935e5fc6
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R41 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R41 contract. Scores may not be changed after this commit. / 본 문서는 R41 계약이 허용한 유일한 scorecard이며 commit 이후 점수를 변경하지 않는다.

| Dimension / 기준 | US-HUD-MF-001 | US-FAA-REG-001 | US-SEC-ADV-001 | UK-CH-DISS-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 4 | 4 | 4 |
| 2. Cross-dataset / cross-table information gain | 4 | 4 | 4 | 3 |
| 3. Direct future-event quality | 3 | 4 | 3 | 5 |
| 4. Independent-unit prospect | 5 | 4 | 5 | 5 |
| 5. Practical decision value | 5 | 4 | 4 | 4 |
| 6. Zero-cost operability | 5 | 5 | 4 | 3 |
| 7. Source-native/deterministic join defensibility | 4 | 3 | 5 | 5 |
| 8. Next-gate information gain | 5 | 5 | 5 | 4 |
| 9. Low overlap / novelty risk | 2 | 3 | 3 | 2 |
| **Total /45** | **38** | **36** | **37** | **35** |

## Candidate rationales / 후보별 근거

### US-HUD-MF-001 — 38/45 — SELECT_F01

- Strong public-service/asset-continuity relevance and exact FHA Project Number prospect.
- Current HUD active/terminated multifamily mortgage products are operationally accessible at zero incremental cost.
- Direct event quality is deliberately capped at 3 because the current public-page field list does not prove a machine-readable adverse termination reason; mere terminated membership is too heterogeneous.
- Deterministic-join score is 4, not 5, because optional property/inspection crosswalk remains unproven.
- Next-gate value is 5 because one bounded F01 can falsify the two decisive unknowns: current termination-reason semantics and exact project/property linkage.
- Novelty/overlap is 2 because FHA termination/prepayment/default and affordable-housing exit are mature topics. No novelty claim is authorized.

### US-SEC-ADV-001 — 37/45 — HOLD_EVENT_HETEROGENEITY_AND_FUTURE_SOURCE_BOUNDARY

- Exact regulatory identifier prospect is strong and historical ADV/ADV-W tables are official and machine-readable.
- Future-event quality is capped at 3 because full withdrawal can encode voluntary closure or jurisdictional switching, while SEC cancellation is a distinct legal event.
- Zero-cost operability is 4 because post-2024 current data moves to IAPD rather than the same historical bulk path.
- High next-gate value remains, but same-agency/financial-regulation overlap and event heterogeneity keep the branch below HUD.

### US-FAA-REG-001 — 36/45 — HOLD_IDENTITY_REASSIGNMENT_AND_EVENT_HETEROGENEITY

- Free official daily bulk data and explicit Deregistered file make source operation strong.
- N-number cannot be treated as stable aircraft identity; serial/manufacturer-model continuity must be demonstrated.
- Deregistration/status events are direct but heterogeneous.
- Same-agency aviation overlap with prior FAA-AIP is penalized conservatively despite different unit/event semantics.

### UK-CH-DISS-001 — 35/45 — HOLD_MATURE_DISSOLUTION_FRAMEWORK

- Exact company number and dissolved/date-of-cessation semantics are strongest in the pool.
- The free live-company snapshot and daily accounts data are substantial, but dissolved search/API access introduces authenticated API-key operational handling and restoration/cessation semantics.
- Corporate dissolution/failure is highly mature and the exposure/outcome are largely inside the same registry ecosystem, so low-overlap/novelty and cross-system information-gain scores are conservative.

## Frozen selection / 고정 선정

**`SELECT_US_HUD_MF_001_MULTIFAMILY_STRUCTURE_TO_ADVERSE_TERMINATION_F01`**

No tie-break is required. / 동점규칙 적용 불필요.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-HUD-MF-F01` may be designed. Before any future terminated-mortgage membership is opened, F01 must freeze and test:

1. exact FHA Project Number syntax/coverage and active-file identity;
2. current terminated-file schema including termination date and a reason/code sufficient to distinguish adverse default/claim from routine prepayment/voluntary/maturity/refinance;
3. historical snapshot/version availability or another prospectively fixed baseline capable of a future event window;
4. if property/inspection structure is proposed, exact official project/property crosswalk without address/name/fuzzy/geospatial/manual repair;
5. minimum active-project cardinality and geographic/program support;
6. mechanically sealed future terminated-file membership until a later N01/E01 authorization;
7. deterministic source fingerprints and 0 USD incremental cost.

If current public terminated bytes do not expose a defensible termination reason, F01 must HOLD rather than redefine all termination as adverse after observation.

## Non-claims / 비주장

The scorecard does not establish a HUD termination relationship, SEC adviser-exit relationship, FAA deregistration relationship, UK dissolution relationship, prediction, ranking, causal effect or novelty claim. No candidate-specific future event membership was used in scoring.

Incremental monetary cost: **0 USD**.
