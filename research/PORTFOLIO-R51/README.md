---
id: PORTFOLIO-R51
type: stage0-cross-domain-reselection
created: 2026-10-02
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R50
parent_disposition: SELECTION_INVALIDATED_PRIOR_TERMINAL_EQUIVALENCE
parent_decision: DEC-289
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R51 — terminal-equivalence-aware reselection after R50 correction

## Mission / 목적

Select at most one next **outcome-blind F01** after R50's selected FCC route was invalidated by canonical-history reconciliation.

R51 adds a mandatory candidate-eligibility screen before scoring:

> A candidate is ineligible if its candidate ID, source family, unit identity and event family are materially equivalent to a prior terminal scientific/transport branch, even if the new candidate is renamed.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during scoring.

## Mandatory prior-terminal-equivalence screen / 사전 terminal-equivalence screen

Before a candidate can receive a score, repository history must establish all of:

1. no prior terminal branch with the same unit identity + event family + materially equivalent official source route;
2. no prior HOLD/REJECT route is being resurrected by renaming;
3. any adjacent prior branch differs in a documented scientific dimension, not merely file path or identifier name;
4. held portfolio candidates that never received their own F01 remain eligible;
5. prior terminal evidence is cited as an overlap/risk penalty where relevant.

## Frozen candidates / 고정 후보

### 1. `US-PHMSA-PIPE-001` — pipeline operator/infrastructure structure → subsequent reportable incident

Unit: one pipeline operator under source-native PHMSA **Operator ID (OpID)**, with facility-type stratification frozen prospectively by F01.

Official source prospect:
- PHMSA operator OpID reference;
- annual-report data for gas distribution/gathering/transmission, hazardous liquid, LNG and UNGS;
- reportable incident/accident data downloadable free of charge;
- annual-report forms and superseded forms/instructions available back to 2010.

Historical exposure prospect:
- non-outcome infrastructure structure such as mileage, material, installation vintage, commodity/facility type and other source-native annual-report characteristics.

Future event prospect:
- first later source-native reportable incident/accident under one prospectively fixed pipeline facility family.

Anti-tautology:
- prior incident count/history;
- inspection/enforcement history;
- known integrity-management deficiency;
- immediate precursor/incident cause field;
- any future incident-derived variable.

Canonical-history boundary:
- prior `US-FMCSA-HAZ-F01` used FMCSA carrier inspection × PHMSA highway hazmat incident data and was access-limited; that is a different unit/source family.
- prior portfolio-held `US-PIPE`/PHMSA concepts did not receive this exact OpID annual-report→pipeline-incident F01.
- F01 must still reject the candidate if empirical source access reproduces the earlier PHMSA export transport limitation.

### 2. `US-FAA-AIR-001` — civil-aircraft registry structure → subsequent deregistration

Unit: one registered aircraft under an exact stable aircraft identity proven prospectively by F01.

Official source prospect:
- FAA Releasable Aircraft Database refreshed daily;
- current archive includes Registration Master, Document Index, reference files and **Deregistered Aircraft**;
- official yearly database archives exist for 2012–2021.

Historical exposure prospect:
- source-native aircraft make/model/series, manufacture-year, engine/type and registration structure that are non-outcome and non-owner-PII.

Future event prospect:
- later source-native deregistration/cancellation under a prospectively fixed event hierarchy.

Identity boundary:
- N-number alone is not assumed permanent because reassignment exists;
- F01 must prove a stable documented exact key/composite without fuzzy/name/address repair.

Canonical-history boundary:
- prior FAA-AIP/BTS branch is a different airport-level unit/event system;
- FAA Registry appeared as held candidates but has not received this exact deregistration F01.

### 3. `US-CMS-REV-001` — Medicare enrollment structure → subsequent revocation

Unit: one Medicare enrollment keyed by source-native **ENRLMT_ID**, with NPI retained only as a provider-level bridge.

Official source prospect:
- Medicare Fee-for-Service Public Provider Enrollment data;
- Revoked Medicare Providers and Suppliers dataset;
- revocation data dictionary defines ENRLMT_ID as a unique 15-character enrollment identifier and exposes NPI, Revocation Reason, Revocation Effective Date and Re-enrollment Bar Expiration Date.

Historical exposure prospect:
- non-outcome enrollment type/state/specialty/organization structure from approved enrollment data.

Future event prospect:
- first later source-native revocation of an eligible baseline enrollment.

Critical limitation:
- revoked dataset currently represents providers/suppliers that remain revoked and under a re-enrollment bar, so complete historical retention must not be assumed;
- multiple enrollments/NPIs require exact enrollment-level handling.

Anti-tautology:
- pending revocation;
- compliance/enforcement flags;
- revalidation failure;
- known revocation-reason precursors.

Canonical-history boundary:
- prior CMS/NPI candidates involved NPI deactivation or broad CMS concepts, not this exact ENRLMT_ID revocation F01.

### 4. `US-NCUA-CU-001` — credit-union financial structure → subsequent involuntary liquidation/closure

Unit: one federally insured credit union under a source-native **charter/credit-union identifier** only if F01 proves exact identity across quarterly call reports and the event source.

Official source prospect:
- quarterly NCUA Call Report ZIP files from March 1994 onward;
- active federally insured credit-union listings;
- NCUA conservatorship/liquidation history with dated event type and status;
- official liquidation semantics distinguish conservatorship, merger and involuntary liquidation/closure.

Historical exposure prospect:
- non-outcome capital, assets, liabilities, membership, loans and operating structure from quarterly call reports.

Future event prospect:
- source-native **Involuntary Liquidation** ending in Closed status, prospectively separated from conservatorship and merger.

Critical limitation:
- the public event surface may not expose the same charter identifier directly;
- if F01 cannot prove exact event-to-call-report identity without name/location repair, it must HOLD.

Anti-tautology:
- conservatorship status;
- supervisory/enforcement flags;
- merger agreement;
- liquidation notice;
- direct resolution precursor.

Canonical-history boundary:
- NCUA appeared as a held R45 portfolio candidate but has not received this exact F01.

## Frozen official source anchors / 공식 소스

### PHMSA
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids`
- official incident/accident data surfaces under PHMSA Pipeline Safety.

### FAA
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`
- FAA registration database documentation and cancellation guidance.

### CMS
- `https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment`
- `https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revoked-medicare-providers-and-suppliers`

### NCUA
- `https://ncua.gov/analysis/credit-union-corporate-call-report-data/quarterly-data`
- `https://ncua.gov/support-services/conservatorships-liquidations`

## Frozen score rubric / 고정 평가표

Each eligible candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-table / cross-source information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. True longitudinal + prospective common-support information gain
9. Low overlap / novelty risk

Dimensions 7 and 8 remain first interpretive priorities.

## Frozen tie-break / 동점 규칙

If totals tie:
1. source-native/deterministic join defensibility;
2. true longitudinal + prospective common-support information gain;
3. direct future-event quality;
4. independent-unit prospect;
5. low overlap / novelty risk;
6. zero-cost operability.

If still tied, no selection until an outcome-blind discriminator is documented.

## Required execution order / 실행 순서

After this contract commit and Issue binding:
1. re-run the prior-terminal-equivalence screen against canonical repository history;
2. current official source/schema/access revalidation;
3. explicit historical-body/event-lineage verification;
4. prospective common-support risk assessment without future membership;
5. bounded external literature/framework overlap review;
6. exactly one immutable `/45` scorecard;
7. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- FCC Microwave cancellation/termination is ineligible: prior R40 F01 terminal 9/18 HOLD.
- RCRA formal-enforcement candidates are excluded because the project already completed RCRA F01→N01→E01.
- FDA device-recall establishment branch is excluded due prior FDA-MD feasibility work.
- SEC IA, EIA retirement, SDWIS, USDA Organic and other terminal branches may not be renamed/reintroduced.
- Paid/private/commercial sources remain excluded under COST-001.

## Non-claims / 비주장

R51 establishes no pipeline-incident relationship, aircraft-deregistration relationship, Medicare-revocation relationship, credit-union-liquidation relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
