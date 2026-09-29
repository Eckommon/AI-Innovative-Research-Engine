---
id: PORTFOLIO-R46-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-29
issue: 179
contract: cd713015b669a89db9f8dfd715a67fc7e06a2827
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R46 — bounded source / overlap revalidation

## Outcome firewall

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened.

## US-USDA-ORG-001

USDA AMS documentation confirms Organic INTEGRITY exposes a source-native **Operation ID**, operation certification status and effective date of status. The current data dictionary enumerates Certified, Surrendered, Suspended and Revoked among operation statuses. AMS separately publishes Final Notices of Suspension or Revocation and appeal/settlement materials.

Strengths:
- exact operation-level identity prospect;
- direct status semantics with effective dates;
- official public search/export workflow;
- separate enforcement-decision surface.

Critical uncertainty:
- durable historical snapshot lineage and exact current export schema must be proven in F01;
- Surrendered must remain separate from Suspended/Revoked;
- pending/proposed adverse action and noncompliance disposition are prohibited as exposure.

## EU-ECHA-BPR-001

ECHA currently exposes >10,000 authorised biocidal products with exact authorisation number, authorisation status and validity dates.

Strengths:
- strong exact identity;
- large support;
- clear current authorisation metadata.

Critical uncertainty:
- scheduled validity end is known ex ante and cannot be treated as adverse;
- a reproducible historical machine-readable distinction among ordinary expiry, renewal, holder-requested withdrawal and regulator-driven revocation/non-renewal has not yet been established.

## US-PHMSA-OP-001

PHMSA publishes operator-level annual-report infrastructure data and downloadable serious/significant incident data. Serious incident is explicitly defined around fatality or injury requiring inpatient hospitalization, while significant incident has broader severity criteria.

Strengths:
- exact Operator ID;
- public annual-report and incident data;
- mature downloadable event data and severity definitions.

Critical limitation:
- this is immediately adjacent to the just-terminated MSHA mine serious/fatal-event branch, so marginal portfolio information gain and novelty are heavily discounted.

## AU-TGA-ARTG-001

TGA public summaries use exact ARTG identifier numbers and expose start/effective dates. TGA separately publishes sponsor-requested cancellations, regulatory cancellations and suspensions, including review/reinstatement status.

Strengths:
- exact ARTG identity;
- direct cancellation/suspension records;
- source-native distinction between sponsor-requested and regulatory actions.

Critical limitation:
- immediate overlap with the recently completed EMA marketing-authorisation branch is high;
- event hierarchy is strong but marginal cross-domain information value is reduced.

## Canonical-history check

No earlier canonical artifact was found for these exact four R46 candidate IDs before the R46 contract. However PHMSA receives strong immediate safety-event overlap penalty from MSHA, and TGA receives strong medical-regulatory overlap penalty from EMA.

## Conclusion

All four candidates remain eligible for the single immutable scorecard. USDA Organic has the best balance of exact identity, direct source-native adverse status semantics, separate enforcement decisions, low immediate overlap and a sharply falsifiable next F01 focused on export identity/history. ECHA is second on structural novelty but has a materially weaker demonstrated adverse end-state lineage. PHMSA and TGA are operationally strong but intentionally penalised for immediate portfolio overlap.

Incremental monetary cost: 0 USD.
