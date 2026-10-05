---
id: PORTFOLIO-R53
type: stage0-survivor-first-reselection
created: 2026-10-06
status: CONTRACT_FROZEN_PRE_ISSUE
parent: CA-CRA-CHARITY-F01
parent_disposition: HOLD_CA_CRA_CHARITY_F01_EXACT_REGISTRATION_FUTURE_REVOCATION_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R53 — survivor-first cross-domain reselection after CRA charity HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** with a materially higher probability of surviving F01 and N01 into a controlled experiment.

R53 responds to repeated recent failure modes:
- latest-only or discontinuous historical lineage;
- rare/insufficient terminal events;
- exact-ID coverage gaps;
- inspection/event ascertainment without a frozen observation opportunity;
- clean but too-small matching/common-support regions.

The score rubric remains the canonical 9-dimensional /45 rubric, but interpretive priority is frozen as:

1. row-bearing historical lineage;
2. source-native exact identity;
3. direct and sufficiently frequent event ascertainment;
4. likely N01 common support;
5. novelty/overlap.

No candidate future-event membership, relationship, prediction, ranking or causal result may be opened for scoring.

## Frozen candidates / 고정 후보

### 1. `US-CMS-NH-001` — nursing-home structure/staffing → serious deficiency at a future standard health survey

Unit:
- one Medicare/Medicaid-certified nursing home identified by exact **CMS Certification Number (CCN)**.

Prospective exposure family:
- non-outcome facility structure and staffing only, such as ownership type, certified beds, resident census, chain structure, nurse staffing hours/turnover and case-mix concepts.

Primary future event prospect:
- at the **next source-native standard health survey** after a future prospective lock, at least one health deficiency with source-native scope/severity at or above a preregistered serious-harm threshold.

Official source architecture:
- CMS Provider Data Catalog Provider Information: one row per active nursing home, exact CCN;
- Inspection Dates: survey dates/types for the past three cycles;
- Health Deficiencies: one citation per row with CCN, inspection date, tag, scope/severity, status/correction date;
- Penalties: fines/payment denials with CCN and penalty/inspection dates;
- CMS dataset pages expose Archived Data and recurring planned updates.

Frozen anti-tautology boundary:
- current/prior health ratings, deficiency counts/scores, fines, penalties, Special Focus status, abuse icon, enforcement/citation status and any variable derived from survey outcomes are prohibited predictive exposures.

Critical design boundary:
- event ascertainment is inspection-conditioned. A descendant must lock a **standard survey opportunity**, not compare arbitrary calendar time with unequal inspection exposure.

### 2. `US-FRA-RR-001` — railroad operational structure → future reportable rail-equipment accident

Unit:
- one source-native reporting railroad, using exact FRA railroad code/reference identity prospectively validated in F01.

Exposure prospect:
- non-outcome annual/period operational structure from Form 55 or other official operational data.

Future event prospect:
- later source-native Rail Equipment Accident/Incident report (Form 54) under a prospectively fixed reporting threshold/event hierarchy.

Official source architecture:
- FRA Safety Data Portal provides full Train Accident, Casualty and Operational datasets;
- FRA DataDownloadService exposes annual railroad-level Form 54 and Form 55 data and a railroad reference file;
- database schemas/file structures are separately published.

Critical limitations:
- railroad mergers/code changes must be handled source-natively;
- accident reporting thresholds change over time and must be frozen by period;
- operational exposure and accident outcome must be temporally separated;
- casualty/accident fields may not leak into exposure.

### 3. `UK-FHRS-EST-001` — food-establishment structure → future poor hygiene rating

Unit:
- one Food Hygiene Rating Scheme establishment identified by exact **FHRSID**.

Exposure prospect:
- non-outcome business type, authority and stable establishment metadata.

Future event prospect:
- a later official FHRS inspection/rating with a prospectively fixed poor-rating threshold.

Official source architecture:
- Food Standards Agency Ratings API exposes FHRSID, RatingDate, RatingValue, business type, authority and component scores.

Critical limitations:
- current API is strong for exact identity and latest rating but a reproducible row-bearing historical rating ledger is not yet established;
- local-authority inspection timing is heterogeneous;
- prior/current rating and component scores are prohibited exposures.

### 4. `AU-ACQSC-CARE-001` — aged-care provider structure → future registration suspension/revocation or regulatory order

Unit:
- one Australian aged-care registered provider identified by exact **Provider ID (PRV-...)** under the current Provider Register.

Exposure prospect:
- provider/service structure, registration categories and non-outcome attributes.

Future event prospect:
- later source-native suspension/revocation/Commission regulatory order under one prospectively fixed event hierarchy.

Official source architecture:
- Aged Care Quality and Safety Commission Provider Register exposes Provider ID, registration status/end date and Excel register;
- Commission publishes regulatory/compliance materials and current/former banning-order data.

Critical limitations:
- the Aged Care Act 2024 transition materially changed the registration/enforcement regime;
- comparable pre-transition historical provider/event lineage is not yet established;
- banning orders can concern persons/workers as well as providers and may not be used as an entity-level substitute.

## Frozen source anchors / 공식 source

### CMS
- `https://data.cms.gov/provider-data/dataset/4pq5-n9py` — Provider Information
- `https://data.cms.gov/provider-data/dataset/r5ix-sfxw` — Health Deficiencies
- Nursing Home consolidated data dictionary under Provider Data Catalog
- Provider Data Catalog nursing-home topic / archived data surfaces

### FRA
- `https://railroads.dot.gov/safety-data`
- `https://railroads.dot.gov/safety-data/new-safety-data-site`
- `https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx`

### UK FHRS
- `https://api.ratings.food.gov.uk/Help`
- `https://api.ratings.food.gov.uk/Help/Api/GET-Establishments-id`

### Australia aged care
- `https://www.agedcarequality.gov.au/service-and-reports`
- `https://www.agedcarequality.gov.au/providers/compliance-enforcement/banning-orders`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on:

1. Mission bottleneck fit
2. Cross-dataset / cross-table information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. Next-gate information gain / survivor probability
9. Low overlap / novelty risk

Total: **/45**.

## Frozen tie-break / 동점 규칙

If totals tie:
1. row-bearing historical lineage / next-gate information gain;
2. deterministic identity;
3. event ascertainment/frequency;
4. independent-unit prospect;
5. zero-cost operability;
6. novelty.

If still tied, no selection until an outcome-blind discriminator is recorded.

## Frozen exclusions / 제외

- no rescue of CRA charity, SDWIS, EIA retirement, SEC IA, FCC ULS or PHMSA pipeline exact branches;
- no current/prior outcome or enforcement field as a predictive exposure;
- no entity repair by name/address/geography when a source-native key is required;
- no paid/private data source;
- no future-event membership during portfolio scoring.

## Required execution / 필수 실행

After Issue binding:
1. current official-source/access revalidation;
2. internal canonical overlap check;
3. bounded literature/framework overlap review;
4. one immutable /45 scorecard;
5. select at most one separate outcome-blind F01.

## Non-claims / 비주장

R53 does not establish that staffing causes nursing-home deficiencies, railroad operations cause accidents, establishment attributes cause poor food-hygiene ratings, or aged-care structure causes regulatory action.

Incremental monetary cost must remain **0 USD**.
