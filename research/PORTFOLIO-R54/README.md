---
id: PORTFOLIO-R54
type: stage0-survivor-first-static-source-reselection
created: 2026-10-08
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-CMS-NH-F01
parent_disposition: BLOCKED_IMPLEMENTATION_CMS_ARCHIVE_METADATA_RESOLUTION__SCIENTIFIC_GATE_NOT_EXECUTED
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R54 — survivor-first static/API-source reselection after CMS implementation block

## Mission / 목적

Select at most one next **outcome-blind F01** with materially higher probability of surviving source resolution, F01 structural gates and a later N01 common-support design.

R54 responds to recent failures by adding one interpretive priority ahead of novelty:

> **direct machine-readable body / static-file or documented API transport must already be source-native and reproducibly addressable before F01 selection.**

No SPA-only archive discovery, post-selection reverse engineering, future-event membership, relationship, prediction, ranking or causal result is allowed during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `US-FRA-RR-001` — railroad operating structure → future reportable rail-equipment accident

Unit:
- one source-native railroad identified by the exact FRA railroad/reference code validated in F01.

Exposure prospect:
- prior-year non-outcome Form 55 operational structure only, such as train miles, employee hours and other source-native operating denominators.

Future event prospect:
- a later source-native Form 54 Rail Equipment Accident/Incident above the prospectively applicable reporting threshold.

Official architecture:
- FRA Safety Data Portal publishes full Form 54 and Form 55 datasets;
- documented DataDownloadService directly exposes `GetAccident54DataByRailroad`, `GetAccident55DataByRailroad`, schemas and railroad reference data;
- FRA publishes current and previous data dictionaries plus reporting-threshold guidance.

Critical boundaries:
- mergers/code changes and consolidated/system railroad identities require source-native adjudication;
- reporting monetary thresholds change by year and must be period-correct;
- prior accident/casualty fields may not become predictive exposures;
- N01 must demonstrate common support across railroads rather than letting a few Class I carriers dominate.

### 2. `US-EPA-RCRA-001` — hazardous-waste handler structure → future inspection-conditioned violation

Unit:
- one RCRA handler/site identified by exact source-native `ID_NUMBER`.

Exposure prospect:
- non-outcome handler structure: generator/TSDF/transporter status, NAICS and facility attributes.

Future event prospect:
- at a later prospectively locked source-native evaluation opportunity, a violation identified from RCRA evaluation/violation records.

Official architecture:
- ECHO publishes a direct RCRAInfo ZIP;
- six CSV tables share `ID_NUMBER + ACTIVITY_LOCATION`;
- the violation/SNC history file carries explicit `YRMONTH` lineage;
- evaluation rows contain evaluation date/type and `FOUND_VIOLATION`.

Critical boundaries:
- inspection opportunity is non-random, so any descendant outcome must be evaluation-conditioned;
- prior/current violation, SNC, enforcement, penalty or inspection-outcome variables are prohibited predictive exposures;
- handler status changes and generator-category transitions require prospective handling.

### 3. `US-FAA-NTSB-AIR-001` — registered-aircraft structure → future NTSB accident

Unit:
- one U.S.-registered aircraft.

Identity prospect:
- FAA N-number plus aircraft serial/manufacturer-model fields, with exact temporal identity rules frozen in F01.

Exposure prospect:
- non-outcome aircraft registry characteristics only.

Future event prospect:
- later NTSB aviation accident involving the same aircraft under an exact source-native registration identity rule.

Official architecture:
- FAA publishes the complete Aircraft Registration Database for download;
- NTSB aviation data expose RegistrationNumber and aircraft characteristics.

Critical boundaries:
- N-numbers can be reassigned and ownership/registration changes occur;
- aircraft serial continuity must be proven before any N-number-only join is accepted;
- operational exposure hours are not available from the registration file, creating likely N01 confounding/common-support limits.

### 4. `US-NHTSA-REC-001` — vehicle/product structure → future safety recall

Unit:
- one source-native vehicle product family under a prospectively validated make/model/model-year or other NHTSA product identity.

Exposure prospect:
- non-outcome product attributes only.

Future event prospect:
- later source-native NHTSA recall campaign.

Official architecture:
- NHTSA publishes static Recall ZIPs from 1949-present and daily-updated files/APIs;
- recall records carry campaign identifiers and product descriptors;
- complaints, investigations and manufacturer communications are separately downloadable.

Critical boundaries:
- make/model/model-year is not necessarily a unique engineering platform;
- complaints, investigations and manufacturer communications are direct defect precursors and are prohibited predictive exposures in the first descendant;
- recall timing may be manufacturer-initiated or NHTSA-influenced and product exposure denominators are incomplete.

## Frozen official source anchors / 공식 source

### FRA
- `https://railroads.dot.gov/safety-data/new-safety-data-site`
- `https://data.transportation.gov/stories/s/Data-Downloads-Landing-Page/yh67-9te8/`
- `https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx`
- FRA Database Dictionaries and annual reporting-threshold guidance.

### EPA RCRA
- `https://echo.epa.gov/tools/data-downloads`
- `https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary`

### FAA / NTSB
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry`
- FAA Aircraft Registration Database / Master File specification
- `https://www.ntsb.gov/pages/AviationDownloadDataDictionary.aspx`

### NHTSA
- `https://www.nhtsa.gov/nhtsa-datasets-and-apis`
- static recall files / `RCL.txt` data dictionary.

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions:

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

## Frozen survivor-first tie-break / 동점 규칙

If totals tie:
1. direct static/API transport and row-bearing lineage;
2. deterministic identity;
3. event ascertainment/opportunity design;
4. likely N01 common support;
5. event support/frequency;
6. novelty.

If still tied, no selection until an outcome-blind discriminator is recorded.

## Frozen exclusions / 제외

- no CMS archive rescue;
- no promotion of R53 FRA merely because it was runner-up: FRA must compete anew;
- no re-entry of terminal FCC, PHMSA, SDWIS, CRA, SEC-IA, EIA-retirement or exact prior branches;
- no outcome/enforcement/inspection-result precursor as a predictive exposure;
- no entity repair by name/address/geography where source-native identity is required;
- no paid/private data;
- no future-event membership during portfolio scoring.

## Required execution / 필수 실행

After Issue binding:
1. current official-source/direct-body revalidation;
2. internal canonical overlap check;
3. bounded external literature/framework overlap review;
4. exactly one immutable /45 scorecard;
5. select at most one separate outcome-blind F01.

## Non-claims / 비주장

R54 establishes no railroad-accident relationship, hazardous-waste violation relationship, aircraft-accident relationship, vehicle-recall relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
