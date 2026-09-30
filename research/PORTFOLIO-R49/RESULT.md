---
id: PORTFOLIO-R49-RESULT
type: stage0-portfolio-selection
created: 2026-09-30
issue: 186
state: COMPLETED_SELECTED
selection: SELECT_US_SEC_IA_001_ADVISER_STRUCTURE_TO_FUTURE_FULL_ADVW_WITHDRAWAL_F01
scorecard_commit: 4f102b484bdc204c07d3d57da1f11a32c7e27337
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R49 Result / 결과

**`SELECT_US_SEC_IA_001_ADVISER_STRUCTURE_TO_FUTURE_FULL_ADVW_WITHDRAWAL_F01`**

R49 executed the common-support-aware candidate universe frozen before Issue binding at `02c6730b43ff9e73a7933587b9a4d862b2637c9f`, bounded revalidation at `f0110bce638973cd8236c11391f82db2b6dc0416`, and the single immutable scorecard at `4f102b484bdc204c07d3d57da1f11a32c7e27337`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-SEC-IA-001` | **40** | **SELECT_F01** |
| `US-EPA-RCRA-001` | **40** | HOLD_SELECTION_BIAS_COMMON_SUPPORT_RISK |
| `US-CMS-NPI-001` | **38** | HOLD_EVENT_HETEROGENEITY_AND_REACTIVATION |
| `US-FDA-DEV-001` | **38** | HOLD_ESTABLISHMENT_ATTRIBUTION_MANY_TO_MANY |

SEC and RCRA tied at 40/45. The frozen tie-break resolved:
- join defensibility: 5 = 5;
- longitudinal + prospective common-support information gain: **SEC 5 > RCRA 4**.

## Why SEC / SEC 선정 이유

SEC provides long structured Form ADV filing lineage, historical Form ADV-W data, source-native full/partial withdrawal semantics and firm-level CRD identifiers. Unlike an inspection-conditioned enforcement event, future ADV-W filing ascertainment does not inherently depend on whether the adviser was inspected or evaluated.

Selection does **not** interpret full withdrawal as business failure. SEC guidance establishes that registration withdrawal can reflect regulatory transitions, including SEC→state or SEC-registered→exempt-reporting-adviser changes. Any descendant must preserve those distinctions.

## Authorized next work / 허가되는 다음 작업

Exactly one separate outcome-blind `US-SEC-IA-F01` may be frozen next.

F01 must prove:
- exact CRD identity coverage in ADV and ADV-W;
- deterministic ADV↔ADV-W joinability;
- full-versus-partial withdrawal classification;
- historical filing/event date semantics;
- current active SEC-adviser support;
- SEC→state / SEC→ERA transition handling;
- future filing seal;
- no direct withdrawal/cessation/ineligibility exposure;
- zero incremental monetary cost.

## Non-claims / 비주장

R49 establishes no adviser-withdrawal relationship, NPI-deactivation relationship, RCRA-enforcement relationship, device-recall relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
