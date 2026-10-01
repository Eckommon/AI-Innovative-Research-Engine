---
id: PORTFOLIO-R50
type: stage0-cross-domain-reselection
created: 2026-10-01
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-SEC-IA-F01
parent_disposition: HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R50 — lineage + common-support aware reselection after SEC source-lineage HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `US-SEC-IA-F01` terminated on a preregistered source-lineage failure.

R50 strengthens the Stage-0 screen using two reusable lessons:
1. a source advertised as periodic is not assumed longitudinal unless distinct historical bodies/transactions are actually exposed;
2. a structurally valid F01 is not enough if a later N01 is unlikely to have adequate prospective common support.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during scoring.

## Frozen candidates / 고정 후보

### 1. `US-FCC-ULS-001` — wireless-license structure → subsequent cancellation/termination

Unit: one FCC ULS license identified by exact source-native **9-digit Unique System Identifier**.

Official source prospect:
- ULS complete public-access license files by radio service;
- ULS daily transaction files for licenses newly created or modified on the previous day;
- public-access documentation explicitly states that each license has a unique 9-digit system identifier and that it distinguishes an active call sign from one that later expired, was cancelled or terminated;
- license header includes License Status, Grant Date, Expired Date and Cancellation Date;
- status codes distinguish Active, Canceled, Expired and Terminated.

Historical exposure prospect:
- non-outcome service/licence structure, license age, geography/service scope, entity/license characteristics where source-native and non-tautological.

Future event prospect:
- first later source-native `C` canceled or `T` terminated status transition under a prospectively frozen window;
- `E` expired remains a separate administrative class unless separately authorized.

Anti-tautology:
- renewal failure, cancellation request, termination notice/pending action, expiration date proximity or direct future-status precursors may not become predictive exposures.

F01 only:
- prove weekly-complete and daily-transaction access, exact unique-ID syntax/stability, status/date semantics, historical C/T event support, non-outcome baseline covariates and future-transaction sealing.

### 2. `US-FAA-AIR-001` — aircraft registry structure → subsequent deregistration

Unit: one civil aircraft registration record under a prospectively proven exact identity.

Official source prospect:
- FAA Releasable Aircraft Database, refreshed daily;
- current archive includes Aircraft Registration Master and **Deregistered Aircraft** files;
- FAA publishes yearly registry database archives for 2012–2021;
- FAA cancellation guidance distinguishes deregistration reasons including accident, salvage, dismantling, permanent retirement, destruction and owner request.

Identity prospect:
- F01 must prospectively determine whether source-native serial/manufacturer-model composite, N-number plus aircraft serial, or another documented field is sufficiently stable; N-number alone may not be assumed stable because reassignment is possible.

Future event:
- source-native deregistration/cancellation with documented event/reason semantics.

Anti-tautology:
- pending cancellation/expiration or explicit deregistration request may not be predictive exposures.

### 3. `US-CMS-REV-001` — Medicare enrollment structure → subsequent revocation

Unit: one Medicare provider enrollment, with **ENRLMT_ID** as the primary enrollment-level identity and NPI retained as a provider-level bridge.

Official source prospect:
- Medicare Fee-for-Service Public Provider Enrollment data;
- CMS Revoked Medicare Providers and Suppliers dataset;
- revocation dataset exposes ENRLMT_ID, NPI, revocation reason, revocation effective date and re-enrollment bar expiration date.

Future event:
- new source-native Medicare enrollment revocation.

Critical limitation:
- current revoked dataset represents providers/suppliers currently revoked and under a re-enrollment bar, so full historical event lineage/retention must be proven rather than assumed;
- provider may have multiple NPIs/enrollments.

Anti-tautology:
- revalidation failure, pending revocation, direct compliance/enforcement flags or known revocation reason precursors may not become predictive exposures.

### 4. `US-FDA-DECRS-001` — drug-establishment structure → subsequent registration removal/inactivation

Unit: one FDA drug establishment under a source-native registration identity proven by F01.

Official source prospect:
- Drug Establishments Current Registration Site (DECRS), updated each business day;
- FDA states an establishment is automatically removed when registration is inactivated due to compliance/enforcement, expires, is deregistered, or is otherwise dropped;
- current annual-registration status files are downloadable in ZIP format.

Future event:
- a prospectively defined source-native registration end-state only if historical lineage and reason semantics are directly recoverable.

Critical limitation:
- removal is heterogeneous: enforcement inactivation, expiration, deregistration and other drops are mixed;
- current database is primarily a current-registration surface, so historical end-state lineage cannot be inferred from disappearance alone.

## Frozen official source anchors / 공식 소스

### FCC
- `https://wireless.fcc.gov/uls/index.htm?job=transaction&page=weekly`
- ULS public-access file documentation under `wireless.fcc.gov/uls/documentation/`
- FCC ULS open-data surface

### FAA
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`
- FAA aircraft-registration cancellation guidance

### CMS
- `https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment`
- `https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revoked-medicare-providers-and-suppliers`

### FDA
- `https://www.fda.gov/drugs/drug-approvals-and-databases/drug-establishments-current-registration-site-decrs`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-table / cross-source information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. True longitudinal + prospective common-support information gain
9. Low overlap / novelty risk

Dimensions 7 and 8 are the first two interpretive priorities.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:
1. source-native/deterministic join defensibility;
2. true longitudinal + prospective common-support information gain;
3. direct future-event quality;
4. independent-unit prospect;
5. low overlap / novelty risk;
6. zero-cost operability.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:
1. current official source/schema/access revalidation;
2. explicit historical-body/transaction-lineage verification;
3. canonical internal-history overlap check;
4. bounded external literature/framework overlap review;
5. exactly one immutable `/45` scorecard;
6. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- SEC IA exact design may not be rescued by changing its frozen monthly window/source family.
- EIA retirement redundancy exposure may not be rematched or reused immediately after its N01 common-support HOLD.
- SDWIS may not add historical quarterly archives after its terminal F01.
- R49 held candidates are not automatically promoted; only CMS revocation is admitted here as a materially different event formulation from prior NPI deactivation.
- Paid/private registry sources remain excluded under COST-001.

## Non-claims / 비주장

R50 establishes no FCC termination relationship, FAA deregistration relationship, Medicare revocation relationship, FDA registration-end relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
