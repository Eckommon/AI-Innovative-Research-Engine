---
id: PORTFOLIO-R48-RESULT
type: stage0-portfolio-selection
created: 2026-09-30
issue: 183
state: COMPLETED_SELECTED
selection: SELECT_US_EIA_GEN_001_GENERATOR_STRUCTURE_PERFORMANCE_TO_FUTURE_RETIREMENT_F01
scorecard_commit: 6fc8132426cf10bd54baf195c6d915884ccdf7ea
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R48 Result / 결과

**`SELECT_US_EIA_GEN_001_GENERATOR_STRUCTURE_PERFORMANCE_TO_FUTURE_RETIREMENT_F01`**

R48 executed the longitudinal-first candidate universe frozen before Issue binding at `5a7d40c57ef1b8401e9761e821306b36fc857691`, bounded source/lineage revalidation at `d04e3fe028656709f81b59e5f17443c700158d2b`, and the single immutable scorecard at `6fc8132426cf10bd54baf195c6d915884ccdf7ea`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-EIA-GEN-001` | **43** | **SELECT_F01** |
| `US-SEC-IA-001` | **40** | HOLD_EVENT_HETEROGENEITY |
| `US-EPA-RCRA-001` | **40** | HOLD_IMMEDIATE_SOURCE_FAMILY_OVERLAP |
| `US-FMCSA-CAR-001` | **38** | HOLD_BULK_HISTORY_AND_MATURE_CRASH_PREDICTION |

No tie-break was required.

## Why EIA / EIA 선정 이유

EIA provides identifiable historical monthly 860M files, annual 860 history, direct retired-generator records and independent 923 operating-performance data. The exact unit prospect is Plant ID + Generator ID. Unlike the prior SDWIS route, longitudinal support does not depend on assuming that a replace-in-place latest download contains history.

The candidate does **not** earn high novelty merely because retirement is important; generator retirement is a mature research topic. Selection is based on prospective falsifiability, deterministic identity, explicit history and strong next-gate information value.

## Authorized next work / 허가되는 다음 작업

Exactly one separate outcome-blind `US-EIA-GEN-F01` may be frozen next.

It must prove:
- exact Plant ID + Generator ID identity and stability;
- ≥12 historical monthly EIA-860M files under a frozen window;
- operable/retired tab semantics;
- sufficient historical retirement events;
- generator lifecycle consistency and edge cases;
- usable EIA-923 linkage without assuming unsupported generator-level equivalence;
- strict exclusion of planned-retirement/announced-retirement fields from predictive exposures;
- future monthly-file sealing.

## Non-claims / 비주장

R48 establishes no generator-retirement relationship, adviser-withdrawal relationship, RCRA-enforcement relationship, carrier-crash relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.

## Identifier supersession / 식별자 교정

After this immutable selection was recorded, repository re-read established that `US-EIA-GEN-001 / US-EIA-GEN-F01` were already occupied by the distinct PORTFOLIO-R36 commissioning-slippage branch. Under `DEC-278`, the **R48 retirement concept alone** is canonically relabeled `US-EIA-RET-001 / US-EIA-RET-F01`. The 43/45 score, ranking, source evidence, candidate concept and outcome firewall are unchanged. The immutable scorecard itself is not rewritten.
