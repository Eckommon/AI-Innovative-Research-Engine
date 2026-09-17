---
id: PORTFOLIO-R38
type: stage0-cross-domain-reselection
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FSIS-SAMPLE-F01
parent_disposition: BLOCKED_TRANSPORT_FSIS_SOURCE_WAF__SCIENTIFIC_GATE_NOT_EXECUTED
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R38 — independent reselection after FSIS transport-blocked terminal

## Mission / 목적

Select exactly one next outcome-blind F01 after `US-FSIS-SAMPLE-F01` terminated operationally because official FSIS source access was blocked by HTTP 403 in the canonical zero-cost runner environment before scientific execution. R38 must not relabel that transport failure as scientific HOLD, alter the FSIS frozen contract, or use paid/proxy/third-party-mirror workarounds.

The portfolio is deliberately diversified across rail safety, bank branch access, broadband competition, and dialysis-facility operations. Candidate future outcome rows remain unopened during R38.

## Frozen candidates / 고정 후보

### 1. `US-FRA-XING-001` — grade-crossing inventory/control structure → subsequent crossing collision

- exposure family: FRA Highway-Rail Crossing Inventory current/historical Form 71 records;
- future outcome family: later FRA Highway-Rail Grade Crossing Accident/Incident Form 57 records;
- source-native identity prospect: exact U.S. DOT Crossing ID only;
- practical value: grade-crossing safety and infrastructure-control bottlenecks;
- known overlap: FRA already operates GXAPS and extensive literature directly models/predicts collisions from inventory characteristics, so direct-overlap/novelty penalties must be severe;
- F01 only: prove exact Crossing ID continuity, historical snapshot/time semantics, independent-crossing support and sealed future collision membership.

### 2. `US-FDIC-BRANCH-001` — branch deposit/network position → subsequent branch closure

- exposure family: FDIC Summary of Deposits annual branch-office records;
- structural identity family: FDIC BankFind Locations / structure-history data;
- future outcome family: later branch closure/non-continuation under a separately preregistered definition that distinguishes closure from acquisition/sale/identity change;
- source-native identity prospect: exact `UNINUMBR` with `CERT`/`BRNUM` as documented structural fields; no name/address repair;
- practical value: physical banking-access contraction, local service continuity and branch-network resilience;
- known overlap: FDIC publishes branch-opening/closure analyses and has documented lower-deposit closure patterns, so generic 'low deposits predict closure' is not a novelty claim;
- F01 only: prove longitudinal branch-ID semantics, disposition/structure-history support, cardinality and a future-period firewall before any closure membership is opened.

### 3. `US-FCC-BDC-001` — provider availability footprint/concentration → subsequent provider withdrawal

- exposure family: FCC Broadband Data Collection fixed-availability public downloads/provider list;
- future outcome family: later provider-level geographic availability withdrawal/non-continuation under a separately preregistered definition;
- source-native identity prospect: exact FRN and/or FCC Provider ID only;
- practical value: broadband competition/resilience and local provider-access bottlenecks;
- known limitation: FCC documentation states Provider ID may be null in fixed-availability submissions, so F01 must prove identity coverage before any downstream design;
- F01 only: prove historical snapshot availability, FRN/Provider-ID continuity, independent-provider/geography support and sealed future withdrawal membership.

### 4. `US-CMS-DIALYSIS-001` — dialysis facility operational/quality structure → subsequent facility discontinuation

- exposure family: CMS Dialysis Facility provider/quality datasets and archived releases;
- future outcome family: later facility discontinuation/termination or other separately preregistered direct facility-state event;
- source-native identity prospect: exact CMS Certification Number (`CCN`) only;
- practical value: dialysis access continuity and facility operational bottlenecks;
- known overlap: CMS has a mature dialysis quality/QIP framework and extensive facility-quality research, so quality-prediction novelty receives a strong penalty;
- F01 only: prove CCN continuity, archive/version lineage, sufficient independent facilities and direct future state-event availability without opening membership.

## Frozen official source anchors / 공식 소스

- FRA Safety Data: `https://railroads.dot.gov/safety-data`
- FRA Crossing Inventory: `https://railroads.dot.gov/railroad-safety/divisions/crossing-safety-and-trespass-prevention/crossing-inventory`
- FDIC SOD: `https://banks.data.fdic.gov/bankfind-suite/SOD`
- FDIC bulk data: `https://banks.data.fdic.gov/bankfind-suite/bulkData/bulkDataDownload`
- FCC BDC reference documents: `https://help.bdc.fcc.gov/hc/en-us/articles/6789299021723-Key-Reference-Documents`
- CMS Dialysis Facilities: `https://data.cms.gov/provider-data/topics/dialysis-facilities`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-dataset information gain
3. Direct outcome quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

Dimension 7 is the first interpretive priority. Exact official identity is required; name/address/fuzzy/geospatial/manual reconciliation is penalized.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order: (1) source-native join defensibility, (2) next-gate information gain, (3) low overlap/novelty risk, (4) cross-dataset information gain, (5) independent-unit prospect, (6) zero-cost operability, (7) direct outcome quality. If still tied, make no selection until an outcome-blind discriminator is documented.

## Revalidation order / 재검증 순서

1. official source/schema/current-access revalidation;
2. internal-history overlap check;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

Candidate pool, rubric and tie-break may not change after this commit. Candidate future outcome rows may not be opened to score or break a tie.

## Non-claims / 비주장

R38 establishes no rail-collision relationship, branch-closure relationship, broadband-withdrawal relationship, dialysis-discontinuation relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
