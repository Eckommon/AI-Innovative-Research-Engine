---
id: PORTFOLIO-R48-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-30
issue: 183
contract: 5a7d40c57ef1b8401e9761e821306b36fc857691
revalidation: d04e3fe028656709f81b59e5f17443c700158d2b
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R48 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R48 contract. Scores may not be changed after this commit.

| Dimension / 기준 | US-EIA-GEN-001 | US-SEC-IA-001 | US-EPA-RCRA-001 | US-FMCSA-CAR-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 4 | 5 | 5 |
| 2. Cross-dataset / cross-table information gain | 5 | 5 | 5 | 4 |
| 3. Direct future-event quality | 5 | 4 | 4 | 5 |
| 4. Independent-unit prospect | 5 | 5 | 5 | 5 |
| 5. Practical decision value | 5 | 4 | 5 | 5 |
| 6. Zero-cost operability | 5 | 5 | 5 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 5 | 5 | 5 |
| 8. Longitudinal/next-gate information gain | 5 | 5 | 4 | 3 |
| 9. Low overlap / novelty risk | 3 | 3 | 2 | 1 |
| **Total /45** | **43** | **40** | **40** | **38** |

## Candidate dispositions / 후보 판정

### US-EIA-GEN-001 — 43/45 — SELECT_F01

EIA provides explicit historical monthly 860M files, annual 860 history, direct source-native retirement records and independent EIA-923 operating-performance data. Plant ID + Generator ID offers a strong unit key. Retirement research is mature, so novelty credit remains conservative; selection is based on reproducible prospective design quality and mission information gain.

### US-SEC-IA-001 — 40/45 — HOLD_EVENT_HETEROGENEITY

Historical ADV/ADV-W lineage is strong and exact CRD joinability is promising. However, full withdrawal is a regulatory event that may represent business cessation, adviser reorganization, jurisdictional transition or other administrative change. F01 would need strong full/partial and SEC/state-transition semantics before any business-exit interpretation.

### US-EPA-RCRA-001 — 40/45 — HOLD_IMMEDIATE_SOURCE_FAMILY_OVERLAP

RCRAInfo has excellent exact site identity and dated enforcement/evaluation/violation history. It remains a strong future candidate. Immediate EPA-family overlap after SDWIS, inspection-selection concerns and mature compliance/enforcement literature reduce marginal portfolio value for this round.

### US-FMCSA-CAR-001 — 38/45 — HOLD_BULK_HISTORY_AND_MATURE_CRASH_PREDICTION

USDOT identity and reportable-crash semantics are strong, but reproducible national multi-month bulk snapshot lineage is not yet as directly established as EIA/SEC. FMCSA crash prediction is also an explicitly mature research area.

## Frozen selection / 고정 선정

**`SELECT_US_EIA_GEN_001_GENERATOR_STRUCTURE_PERFORMANCE_TO_FUTURE_RETIREMENT_F01`**

No tie-break is required.

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `US-EIA-GEN-F01` may be designed.

Before any future-retirement membership is opened, F01 must freeze and test:
1. exact Plant ID + Generator ID identity;
2. at least 12 distinct historical monthly 860M files from a prospectively fixed baseline window;
3. active/operable generator support and deterministic identity stability;
4. source-native retirement month/year semantics;
5. sufficient historical retirement events;
6. exact or explicitly mapped 860/860M↔923 plant/generator information linkage;
7. exclusion of planned-retirement fields and direct retirement announcements from predictive exposures;
8. treatment of generator-ID reuse/renaming, plant reconfiguration and retired/reactivated edge cases;
9. future-month file seal and reporting/revision lag;
10. zero incremental monetary cost.

PASS may authorize only a separate outcome-blind N01.

## Non-claims / 비주장

The scorecard establishes no generator-retirement relationship, adviser-withdrawal relationship, RCRA-enforcement relationship, carrier-crash relationship, prediction, ranking, causal effect or novelty claim. No candidate future-event membership was used in scoring.

Incremental monetary cost: **0 USD**.
