---
id: PORTFOLIO-R41-RESULT
type: stage0-portfolio-selection
created: 2026-09-21
issue: 167
state: COMPLETED_SELECTED
selection: SELECT_US_HUD_MF_001_MULTIFAMILY_STRUCTURE_TO_ADVERSE_TERMINATION_F01
scorecard_commit: f03e225a5af67155cb3c558f30ed8c6ce1df4a6b
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R41 Result / 결과

**`SELECT_US_HUD_MF_001_MULTIFAMILY_STRUCTURE_TO_ADVERSE_TERMINATION_F01`**

R41 executed the four-candidate universe frozen before Issue binding at `b3e5e1cac40ba05e839930ed6dcd2e8d1d3962b0`, bounded source/internal-history/external-overlap revalidation at `4f481865e2690ee0c6d7716daeb814c4935e5fc6`, and the single immutable scorecard at `f03e225a5af67155cb3c558f30ed8c6ce1df4a6b`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-HUD-MF-001` | **38** | **SELECT_F01** |
| `US-SEC-ADV-001` | **37** | HOLD_EVENT_HETEROGENEITY_AND_FUTURE_SOURCE_BOUNDARY |
| `US-FAA-REG-001` | **36** | HOLD_IDENTITY_REASSIGNMENT_AND_EVENT_HETEROGENEITY |
| `UK-CH-DISS-001` | **35** | HOLD_MATURE_DISSOLUTION_FRAMEWORK |

No tie-break was required. Scores are terminal for R41 and will not be revised.

## Why HUD is selected / HUD 선정 이유

HUD has the strongest combination of public-service bottleneck fit, exact FHA Project Number prospect, zero-cost monthly active/terminated mortgage products and high next-gate information value. Crucially, R41 does **not** assume that terminated-file membership is adverse. Current public source descriptions establish active/terminated FHA multifamily files and project identifiers, while the exact current machine-readable termination-reason/date semantics and any exact property/inspection crosswalk remain unresolved.

따라서 다음 F01의 가치가 높다. F01은 “관계가 맞는지”가 아니라 **현재 공개파일이 adverse default/claim termination을 routine prepayment/voluntary/maturity/refinance와 정확히 분리할 수 있는지**를 먼저 falsify해야 한다.

## Authorized next work / 허가되는 다음 작업

Exactly one separate outcome-blind `US-HUD-MF-F01` contract may be frozen next. F01 must establish, before future event membership is opened:

1. official current active/terminated multifamily source access and reproducible source selection;
2. exact FHA Project Number syntax/coverage;
3. terminated-file schema and reason/date semantics sufficient to distinguish adverse from routine termination;
4. adequate active-project support;
5. if property/inspection features are contemplated, exact official project/property mapping without fuzzy address/name/geospatial repair;
6. a future monthly-snapshot firewall and deterministic fingerprints;
7. zero incremental monetary cost.

If the current public terminated file lacks a defensible reason field or exact reason semantics, the F01 must HOLD. It may not redefine all terminations as adverse after observation.

## Non-claims / 비주장

R41 establishes no HUD adverse-termination relationship, SEC adviser-exit relationship, FAA deregistration relationship, UK dissolution relationship, prediction, ranking, causal effect or novelty claim. No candidate-specific future event membership was opened for scoring.

Incremental monetary cost: **0 USD**.
