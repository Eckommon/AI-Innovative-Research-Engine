---
id: PORTFOLIO-R56
type: stage0-survivor-probability-reselection
created: 2026-10-13
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EPA-RCRA-N01
parent_disposition: HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R56 — N01-survivor-first reselection after RCRA support HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** with unusually high probability of surviving not only structural F01, but also a later N01 common-support / observation-opportunity gate.

R56 incorporates the durable RCRA lesson: structurally excellent source architecture is insufficient if the frozen exposure produces a small treated arm or too few recent future-event opportunities.

No candidate future-event membership, relationship, prediction, ranking, causal result or exposure tuning may be opened during scoring.

## Frozen candidate universe / 고정 후보군

### 1. `US-CMS-NPI-002` — active provider structural complexity → future NPI deactivation

Unit: exact 10-digit NPI.

Official current architecture:
- CMS monthly NPPES full replacement file;
- separate monthly NPI deactivation update;
- weekly incremental update;
- NPI Registry daily query surface;
- full monthly file includes active and deactivated NPI identity/date semantics;
- current Version 2 files reflect expanded field lengths from 2026.

Prospective event:
- first source-native NPI deactivation after a future lock, observed in a later CMS deactivation/weekly update.

Candidate non-tautological exposure family:
- for active Type-2 organization NPIs only, a prospectively frozen structural-complexity definition based on taxonomy plurality and/or practice-location plurality;
- no deactivation/reactivation/history field may define exposure.

Why this may survive N01:
- national-scale NPI universe;
- direct exact identity;
- monthly full replacement + weekly updates;
- direct deactivation event body;
- likely large exposed/control arms under common taxonomy/location structure.

Critical limitation:
- NPI deactivation is an administrative registry event and does **not** equal provider closure, insolvency, death or quality failure;
- reactivation is possible;
- Type-1 and Type-2 providers must not be mixed without a prospectively justified design.

F01 only:
- prove exact NPI identity, current Version-2 schemas, active Type-2 structural support, taxonomy/location linkage, historical/deactivation-date support, update lineage and future-event sealing.

### 2. `US-FAA-AIR-002` — aircraft registry structure → future source-native deregistration

Unit:
- aircraft entity under a prospectively proven compound identity using source-native registration and serial/manufacturer fields.

Official current architecture:
- complete aircraft registry download refreshed daily;
- Master, Deregistered Aircraft, Document Index, make/model and engine reference files in one bundle;
- official yearly archives 2012–2021 remain public.

Prospective event:
- new row in the source-native Deregistered Aircraft file after a future lock.

Candidate exposure family:
- non-outcome aircraft age / engine / category / registration structure.

Strength:
- direct daily future-event opportunity and large national universe.

Critical limitation:
- N-number reassignment prevents N-number-alone identity;
- deregistration reasons are heterogeneous;
- compound identity continuity must be proved prospectively.

### 3. `US-PHMSA-PIPE-002` — pipeline operator infrastructure structure → future reportable incident

Unit:
- exact PHMSA operator ID, within one frozen pipeline system family.

Official current architecture:
- operator-ID list;
- annual-report raw data for gas distribution/gathering/transmission, hazardous liquids, LNG and UNGS;
- report data updated monthly in response to supplemental reports;
- reportable incident data and long-run incident trend files.

Prospective event:
- later source-native reportable incident after a future lock.

Candidate exposure family:
- non-outcome operator infrastructure mix such as mileage/material/installation-age distribution.

Strength:
- long historical annual-report lineage and operationally meaningful incidents.

Critical limitation:
- operator-level incidents are relatively sparse and exposure must be frozen within one system family;
- supplemental revisions complicate snapshot timing;
- prior incidents/enforcement cannot be exposures.

### 4. `US-FCC-ULS-002` — wireless-license structure → future license termination/expiration

Unit:
- exact source-native license/call-sign identity within a single frozen radio-service family.

Official current architecture:
- complete ULS databases updated weekly;
- daily transaction files contain new/modified licenses;
- downloadable pipe-delimited license/application data;
- FCC Open Data/OData surface.

Prospective event:
- source-native termination/expiration/cancellation status transition after a future lock.

Candidate exposure family:
- non-outcome license/service/geographic/technical structure.

Strength:
- large universe and dense daily/weekly update opportunities.

Critical limitation:
- event semantics may be largely administrative/renewal-driven;
- call-sign reuse/service-specific identity rules require F01;
- prior FCC work creates moderate internal overlap.

## Frozen source anchors / 공식 소스

### CMS NPI
- `https://download.cms.gov/nppes/NPI_Files.html`
- `https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination`

### FAA
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`

### PHMSA
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/data-and-statistics-overview`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids`
- `https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids`

### FCC ULS
- `https://opendata.fcc.gov/Wireless/FCC-Universal-Licensing-System-ULS-/x28i-i4z4`
- official ULS complete and daily transaction database downloads.

## Frozen /45 rubric

Nine 0–5 dimensions:
1. mission bottleneck fit
2. cross-table information gain
3. direct future-event quality
4. independent-unit prospect
5. practical decision value
6. zero-cost operability
7. deterministic identity
8. **N01 survivor probability** — arm scale, common support, recent event opportunity
9. low overlap / novelty risk

Tie-break:
1. N01 survivor probability;
2. direct future-event body;
3. deterministic identity;
4. repeated update lineage;
5. non-tautological exposure breadth;
6. novelty.

## Frozen exclusions

- no RCRA multi-NAICS rescue or threshold revision;
- no automatic promotion of a prior held candidate;
- no prior/current outcome, enforcement or deactivation flag as exposure;
- no name/address/geographic/fuzzy identity repair;
- no paid/private source;
- no future candidate membership during scoring;
- no interpretation of NPI deactivation as provider closure or quality failure.

## Required execution order

After this contract commit and Issue binding:
1. current official source/access/schema revalidation;
2. canonical project-overlap check;
3. one immutable /45 scorecard;
4. select at most one separate outcome-blind F01.

Incremental monetary cost must remain **0 USD**.
