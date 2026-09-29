---
id: PORTFOLIO-R47
type: stage0-cross-domain-reselection
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-USDA-ORG-F01
parent_disposition: BLOCKED_TRANSPORT_USDA_INTEGRITY_FULL_EXPORT_ROUTE__SCIENTIFIC_GATE_NOT_EXECUTED
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R47 — independent cross-domain reselection after USDA transport-block

## Mission / 목적

Select at most one next **outcome-blind F01** after `US-USDA-ORG-F01` terminated operationally under the mandatory branch-stop rule.

R47 must not rescue the USDA route through a third transport workaround, Data History scraping, a paid/private source, or any change to the frozen USDA scientific contract.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `US-EPA-SDWIS-001` — public-water-system structure → subsequent health-based violation / serious compliance event

Unit: one U.S. public water system identified by exact SDWIS PWSID.

- historical exposure prospect: non-outcome system structure such as system type, primary water source, ownership, population served, seasonal status, service area and facility structure;
- future event prospect: later prospectively defined health-based violation / high-severity compliance event from official SDWIS violation/enforcement records;
- source-native identity prospect: exact **PWSID**, documented as two-letter state/region code + seven digits;
- official source strength: EPA ECHO publishes quarterly national SDWIS ZIP files containing public-water-system, facilities, violations/enforcement, site visits and related tables, joined by `SUBMISSIONYEARQUARTER + PWSID`;
- anti-tautology boundary: prior/current violation, enforcement-priority, unresolved noncompliance, monitoring-failure or equivalent direct outcome precursor may not be used as a descendant predictive exposure;
- critical limitation: reporting lag, archived/resolved violation semantics, system mergers/deactivation and quarter-version lineage must be prospectively handled;
- F01 only: prove exact PWSID syntax/coverage, historical snapshot continuity, active-system support, violation/event semantics, deterministic joins and future-quarter sealing.

No drinking-water safety ranking, enforcement recommendation, utility score or causal claim is authorized.

### 2. `US-ED-POSTSEC-001` — postsecondary-institution structure → subsequent institution/location closure

Unit: one U.S. Title-IV institution/location.

- historical exposure prospect: non-outcome College Scorecard/IPEDS/FSA institutional structure such as sector, control, awards, enrollment and financial/academic structure;
- future event prospect: later official Department of Education closed-school event;
- identity prospect: exact **8-digit OPEID** at closure-location level, with UNITID↔OPEID mapping admitted only through an official Department/Scorecard crosswalk established by F01;
- official source strength: Federal Student Aid publishes a **Weekly Closed School Search File** and documents OPEID as a search identifier; the closed-school database assigns closure dates after Department verification;
- critical limitation: UNITID and 8-digit OPEID are not assumed one-to-one; multi-branch institutions, teach-outs, affiliation changes and closure-location granularity must be resolved before any join;
- anti-tautology boundary: Department closure flags, teach-out/close-out status or known loss-of-Title-IV eligibility due to closure may not be exposure;
- F01 only: prove current zero-cost institutional baseline, exact OPEID/UNITID crosswalk lineage, closure-date/event semantics, cardinality and future closure sealing.

No school ranking, enrollment recommendation, financial-viability score or causal claim is authorized.

### 3. `AU-ASIC-COMP-001` — Australian-company registry structure → subsequent deregistration

Unit: one ASIC registered company.

- historical exposure prospect: non-outcome company type/class/subclass, jurisdiction and registration-age structure from the public company dataset;
- future event prospect: later deregistration under a prospectively fixed status/date rule;
- source-native identity prospect: exact **ACN**;
- official source strength: ASIC/Data.gov.au publishes a free weekly Company Dataset with Company Name, ACN, Type, Class, Sub Class, Status, Date of Registration and, since March 2025, **Date of Deregistration**;
- critical limitation: current bulk data retain deregistered companies only for a bounded period, corporate deregistration is a mature event family, and this branch overlaps recent CA-CORP/company-registry work;
- F01 only: prove exact ACN syntax/coverage, weekly snapshot reproducibility, deregistration retention/event semantics, sufficient support and future-snapshot sealing.

No insolvency prediction, company-quality ranking, investment signal or causal claim is authorized.

### 4. `EU-EMAS-ORG-001` — EMAS organisation structure → subsequent registration end / deregistration

Unit: one EMAS-registered organisation.

- historical exposure prospect: non-outcome organisation/site structure, NACE sector, country, size and environmental-statement metadata;
- future event prospect: later verified end of EMAS registration under a prospectively fixed deregistration/expiry/status hierarchy;
- identity prospect: exact **EMAS registration number** if directly present in official register export;
- official source strength: the European Commission describes the EMAS register as the comprehensive list of registered organisations/sites and states that search results can be downloaded in Excel;
- critical limitation: the current public register is primarily a positive/current register, and a reproducible historical deregistration/end-state lineage has not yet been established;
- F01 only: prove exact registration identity, zero-cost export access, temporal archive/history, deregistration semantics, support and future membership sealing.

No environmental-performance ranking, certification recommendation or causal claim is authorized.

## Frozen official source anchors / 공식 소스

### EPA SDWIS
- `https://echo.epa.gov/tools/data-downloads/sdwa-download-summary`
- `https://echo.epa.gov/tools/data-downloads`
- `https://echo.epa.gov/help/sdwa-faqs`

### U.S. postsecondary / FSA
- `https://collegescorecard.ed.gov/data/`
- Federal Student Aid Weekly Closed School Search / Closed School Reports under `fsapartners.ed.gov`

### ASIC
- `https://data.gov.au/data/dataset/asic-companies`
- official ASIC Company Dataset help/current CSV/ZIP resources on Data.gov.au

### EMAS
- `https://green-forum.ec.europa.eu/green-business/emas/emas-register_en`
- official European Commission EMAS register / Facts and Figures surfaces

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-dataset / cross-table information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

Dimension 7 remains the first interpretive priority.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:
1. source-native/deterministic join defensibility;
2. next-gate information gain;
3. low overlap / novelty risk;
4. direct future-event quality;
5. independent-unit prospect;
6. zero-cost operability;
7. cross-dataset information gain.

If still tied, no selection until an outcome-blind discriminator is documented.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:
1. current official source/schema/access revalidation;
2. canonical internal-history overlap check;
3. bounded external literature/framework overlap review;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- USDA Organic and descendants: immediate transport-route rescue prohibited.
- R46 held PHMSA, TGA and ECHA candidates are not re-entered.
- Recent CA-CORP/company-registry work gives ASIC a strong same-event-family overlap penalty.
- SDWIS descendant exposures may not contain prior/current violation/enforcement/outcome-proximal flags.
- Postsecondary closure descendants may not use known closure/teach-out/Title-IV-loss precursor flags as exposures.
- EMAS may not infer deregistration from disappearance alone unless historical source semantics establish that rule prospectively.
- Paid commercial registry/API sources remain excluded under COST-001.

## Non-claims / 비주장

R47 establishes no drinking-water violation relationship, postsecondary closure relationship, company-deregistration relationship, EMAS-registration-end relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
