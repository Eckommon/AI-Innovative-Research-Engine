---
id: PORTFOLIO-R41-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-21
issue: 167
contract: b3e5e1cac40ba05e839930ed6dcd2e8d1d3962b0
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R41 — bounded source / overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event row, membership, effect, prediction, ranking or causal result was opened. Revalidation used only official source/documentation pages, source-family metadata, canonical repository history and bounded literature/framework descriptions.

## 1. US-HUD-MF-001

**Official-source finding / 공식 소스 확인**

HUD currently publishes separate monthly **Active MF Insured Mortgages** and **Terminated MF Insured Mortgages** files. The public page states both contain FHA Project Number and core mortgage/project fields, and is current as of 2026-08-31. HUD also publishes active multifamily property/contract datasets. Historic HUD system documentation explicitly describes a terminated multifamily mortgage database containing HUD Project Number, **Termination Reason** and **Termination Date**; current public-page field listing does not itself enumerate those two termination fields.

**Implication / 함의**

Exact FHA Project Number is a strong identity prospect and source access is operationally attractive, but a future F01 must directly verify whether the current terminated bytes expose a machine-readable termination-reason/date field sufficient to distinguish default/claim from prepayment/voluntary/maturity/refinance. It must not infer adverse termination from mere terminated-file membership. Crosswalk to property/inspection identifiers is also unproven and may not use address matching.

**Overlap / 중복**

HUD multifamily prepayment/opt-out/default/termination is a mature housing-finance/preservation topic. The candidate receives overlap penalty; its value is the narrower public-data exact-project structural gate, not a novelty claim.

## 2. US-FAA-REG-001

FAA's releasable aircraft database is a free daily-refreshed archive containing Master, Document Index, Deregistered Aircraft and related files. Official data documentation states that the Deregistered file contains U.S. civil aircraft deregistered by FAA and exposes N-Number, manufacturer-assigned Serial Number and status coding.

N-number alone is not accepted as immutable identity because reassignment is possible. A future F01 must demonstrate a deterministic aircraft identity using source-native serial/manufacturer-model semantics and must prospectively separate heterogeneous deregistration/enforcement/invalid-registration states.

This family is distinct from prior airport-infrastructure FAA-AIP work but receives a same-agency/aviation overlap penalty.

## 3. US-SEC-ADV-001

SEC currently provides historical Form ADV Part 1 and Form ADV-W CSV datasets through 2024, while 2025-present data are directed to IAPD. Form ADV-W is the formal notice for full or partial withdrawal and includes cessation timing/reason information. SEC guidance also distinguishes withdrawal from SEC registration, switching to state registration, and possible SEC cancellation when an adviser fails to withdraw/correct eligibility.

A future F01 must prove exact Organization CRD/SEC-number continuity and a reproducible zero-cost current/future source path. Ordinary state-registration switching and voluntary withdrawal cannot be pooled with adverse cessation/cancellation.

This is distinct from R40's public-issuer/Form-25 candidate but receives a conservative same-agency/financial-regulation overlap penalty.

## 4. UK-CH-DISS-001

Companies House provides a free monthly bulk snapshot for live companies and free daily accounts data. Official public data/API schemas use exact company number and expose company status and date of cessation/dissolution. The dissolved-company search endpoint requires an API key even though public company information is free.

Identity and event semantics are strong, but company dissolution/failure prediction is a mature field and the exposure/outcome remain largely inside one registry ecosystem. A future F01 would also need to resolve restored companies and cessation-date semantics prospectively.

## Canonical-history exclusions / 내부이력 제외

- FCC ULS branch remains terminal negative evidence and is not rescored.
- R40 held SEC-issuer, FMCSA-carrier and NCES-school candidates are not re-entered.
- DOL/PBGC benefit-plan termination variants are excluded as overlap with R39 DOL-5500.
- Prior FAA-AIP terminal work is not rescued; aircraft registry is treated as a different unit/event family with explicit overlap penalty.
- No prior canonical artifact was found for these exact four R41 candidate IDs before the R41 contract.

## Revalidation conclusion / 재검증 결론

All four frozen candidates remain eligible for one-time scoring. HUD has the highest **next-gate information value** because the identity/source family is strong while the exact current termination-reason semantics and optional property crosswalk are sharply falsifiable. Companies House has the strongest identity/event semantics but the highest mature-framework overlap. FAA has strong free bulk access with identity/reassignment risk. SEC ADV has good historical tabular lineage but future-source and event-heterogeneity risk.

Incremental monetary cost: **0 USD**.
