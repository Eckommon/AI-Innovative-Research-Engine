---
id: PORTFOLIO-R50-REVALIDATION
type: bounded-source-lineage-overlap-revalidation
created: 2026-10-01
issue: 188
contract: 4bee3df90e8b174b1851f921eff097f6f5dda00d
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R50 — bounded source / lineage / common-support revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official public source/documentation surfaces, canonical repository history and bounded external framework/literature context only.

## 1. US-FCC-ULS-001

FCC ULS public-access documentation establishes:
- complete license/application public-access ZIP files by radio service;
- daily transaction files containing previous-day new or modified license/application records;
- a source-native **9-digit Unique System Identifier** assigned to each application/license;
- the unique identifier may be used instead of or with call sign and is specifically useful when a call sign has been reassigned, distinguishing active from expired/cancelled/terminated records;
- license header fields include License Status, Grant Date, Expired Date and Cancellation Date;
- status semantics distinguish Active, Canceled, Expired and Terminated.

Strengths:
- direct source-native identity with explicit reassignment handling;
- complete + transaction data architecture rather than replace-in-place current snapshot only;
- exact event status and date concepts;
- broad service universe supports prospective common-support design without conditioning on enforcement/inspection.

Critical boundaries:
- F01 must choose a frozen radio-service family or a defensible common schema before row access;
- Expired must remain distinct from Canceled/Terminated;
- renewal/application-purpose fields that mechanically announce future status cannot be predictive exposures;
- daily transaction history must be shown reproducibly rather than assumed from documentation alone.

## 2. US-FAA-AIR-001

FAA's Releasable Aircraft Database:
- is refreshed daily;
- includes Aircraft Registration Master, Aircraft Document Index, reference files and a **Deregistered Aircraft** file;
- has published yearly registry database archives for 2012–2021;
- FAA cancellation guidance identifies deregistration reasons including accident, salvage, dismantling, permanent retirement, destruction and owner request.

Strengths:
- explicit historical archived bodies;
- direct deregistered-file event source;
- high-value physical-asset lifecycle problem;
- likely broad structural covariate support.

Critical boundaries:
- N-number alone cannot be assumed permanent because assignment/reassignment is possible;
- F01 must prove an exact stable aircraft identity using documented source fields;
- deregistration reasons are heterogeneous and may reflect export/owner request rather than physical retirement;
- daily current history after 2021 is not automatically archived as distinct official bodies.

## 3. US-CMS-REV-001

CMS provides:
- Medicare Fee-for-Service Public Provider Enrollment data for currently approved provider enrollments;
- a Revoked Medicare Providers and Suppliers dataset with `ENRLMT_ID`, NPI, Revocation Reason, Revocation Effective Date and Re-enrollment Bar Expiration Date;
- `ENRLMT_ID` is documented as a unique 15-character enrollment identifier;
- the revocation dataset is quarterly and currently contains providers/suppliers revoked and still under a re-enrollment bar.

Strengths:
- exact enrollment-level identity;
- direct revocation reason/date semantics;
- strong practical regulatory value.

Critical boundaries:
- current-revocation-under-bar retention is not a complete historical event archive;
- baseline PPEF contains currently approved enrollments, so common support around future revocation must avoid selection on currently survivable enrollment structure;
- one provider may have multiple NPIs/enrollments;
- enforcement/compliance fields may create tautology.

## 4. US-FDA-DECRS-001

FDA DECRS:
- lists currently registered drug establishments;
- is updated each business day;
- provides downloadable registration-status ZIP files;
- states that establishments are automatically removed when registration is inactivated due to compliance/enforcement, expires, is deregistered or is otherwise dropped.

Strengths:
- high-value regulated-manufacturing unit;
- frequent update cadence;
- source-native registration status surface.

Critical boundaries:
- end-state/removal semantics combine enforcement inactivation, expiration, deregistration and other drops;
- current database is primarily a current-registration surface;
- historical reason-specific end-state lineage has not been established;
- disappearance alone cannot be classified as a source-native event.

## Canonical-history overlap / 내부 중복

- No canonical artifact was found for the exact R50 candidate identifiers before the R50 contract.
- FCC ULS is a new license-lifecycle branch, not a continuation of prior transport/source families.
- FAA aircraft registration is a new physical-asset registry branch.
- CMS revocation is materially distinct from the prior held NPI deactivation concept, but remains within the same broad Medicare-provider identity ecosystem.
- FDA DECRS remains adjacent to prior FDA/FDA-establishment candidate families and receives overlap/heterogeneity discount.

## Revalidation conclusion / 재검증 결론

All four candidates remain eligible for the single immutable R50 scorecard.

**FCC ULS has the strongest combined identity + true lineage + future-event structure.** FAA is a close second but requires more identity adjudication. CMS revocation has excellent event semantics but incomplete historical retention by construction. FDA DECRS has the weakest event-class purity and historical end-state lineage.

Incremental monetary cost: **0 USD**.
