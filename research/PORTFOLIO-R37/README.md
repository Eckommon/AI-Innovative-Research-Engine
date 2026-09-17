---
id: PORTFOLIO-R37
type: stage0-cross-domain-reselection
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EIA-GEN-F01
parent_disposition: HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R37 — independent reselection after EIA generator F01 HOLD

## Mission / 목적

Select exactly one next **outcome-blind F01** after `US-EIA-GEN-F01` terminated because its frozen focal-cohort minimum (`>=1000`) was not met. R37 must not lower that threshold, broaden the January-2024/2024–2025 EIA exposure window, or open the still-sealed future commissioning outcomes.

The portfolio is deliberately diversified across food safety, federal procurement, drinking-water compliance, and nursing-home operations. Candidate outcome rows remain unopened until a later branch is separately designed and authorized.

## Frozen candidates / 고정 후보

### 1. `US-FSIS-SAMPLE-001` — establishment-specific pathogen sampling structure → subsequent recall/public-health alert

**Question:** Can official FSIS establishment-specific laboratory sampling records be linked prospectively to later FSIS recall/public-health-alert records using USDA establishment number only, without name/address repair?

- prospective exposure family: FSIS establishment-specific laboratory sampling datasets, with raw-poultry sampling as the preferred first source family and other FSIS regulated-product sampling only if documented before F01 row access;
- structural identity source: FSIS Meat, Poultry and Egg Product Inspection Directory / establishment demographic data;
- future outcome family: later FSIS recall/public-health-alert records or annual recall summaries that expose exact establishment number;
- identity prospect: exact USDA establishment number (`EstNumber` / official equivalent) only;
- practical value: food-safety process-control bottlenecks and establishment-level early-warning feasibility;
- known overlap: FSIS already uses Salmonella performance categories and sampling results for regulatory follow-up, so any F01 must distinguish structural feasibility from a novelty claim;
- F01 only: prove source access, identifier normalization rules, historical snapshot coverage, sufficient independent establishments, and exact recall-outcome identifier coverage while keeping future recall membership sealed.

No establishment risk ranking, recall prediction, food-safety recommendation, causality, or novelty claim is authorized in R37.

### 2. `US-USASPEND-VENDOR-001` — federal-recipient concentration structure → subsequent award interruption

**Question:** Can USAspending recipient-level award histories support a prospective vendor-dependence design using exact SAM.gov Unique Entity Identifier (`UEI`) and temporally separated future award presence/absence?

- prospective exposure family: USAspending award/transaction records with recipient UEI, awarding agency, NAICS/PSC, dates and obligations;
- future outcome family: later USAspending award/transaction presence, award continuity or interruption under a separately preregistered definition;
- identity prospect: exact recipient `UEI` only; USAspending internal recipient hash may be retained only as platform metadata, not as the cross-system canonical identity;
- practical value: federal supplier resilience, concentration and market-access bottlenecks;
- known limitation: the exposure and outcome are within the same spending platform, reducing cross-system information gain;
- F01 only: prove stable UEI coverage, temporal snapshots/download reproducibility, independent-recipient cardinality and a future-period firewall.

No contractor ranking, bid recommendation, award-probability estimate or causal claim is authorized in R37.

### 3. `US-EPA-SDWIS-001` — public-water compliance pattern → subsequent health-based violation

**Question:** Can official SDWIS/ECHO quarterly public-water-system data support a prospective system-level design linking earlier monitoring/reporting/treatment-technique compliance structure to later health-based violations using exact `PWSID`?

- prospective exposure family: SDWA public-water-system, site-visit and non-health-based violation/enforcement tables;
- future outcome family: later SDWA health-based violation indicator/category;
- identity prospect: exact 9-character `PWSID` only, with `SUBMISSIONYEARQUARTER` for snapshot separation;
- practical value: drinking-water compliance bottlenecks and regulatory prioritization research;
- known overlap: SDWIS and ECHO already integrate violation/enforcement metrics and academic/public-health literature has analyzed health-based violations; novelty must therefore be penalized conservatively;
- F01 only: prove reproducible quarterly snapshots, exact PWSID continuity, enough independent systems and an explicit outcome firewall.

No public-water-system ranking, health-risk score, causal claim or operational recommendation is authorized in R37.

### 4. `US-CMS-NH-001` — nursing-home staffing instability → subsequent severe health deficiency

**Question:** Can CMS nursing-home staffing/turnover data be linked prospectively to later severe health-inspection deficiencies using exact CMS Certification Number (`CCN`)?

- prospective exposure family: CMS Provider Data Catalog nursing-home Provider Information and/or Payroll-Based Journal-derived staffing/turnover measures;
- future outcome family: later Health Deficiencies / penalties or other separately preregistered severe-deficiency measure;
- identity prospect: exact `CCN` only;
- practical value: workforce instability and care-quality bottlenecks;
- known overlap: CMS Five-Star uses staffing, CMS publishes turnover, and multiple studies already link turnover/staffing to deficiencies and quality outcomes; novelty/direct-overlap penalties must be strong;
- F01 only: prove exact CCN continuity, archive/version availability, independent-facility support and future-outcome sealing.

No nursing-home ranking, clinical recommendation, quality score, prediction or causal claim is authorized in R37.

## Frozen official source anchors / 고정 공식 소스 앵커

These anchors establish source families only; they do **not** authorize candidate outcome row access:

- FSIS laboratory sampling data: `https://www.fsis.usda.gov/science-data/data-sets-visualizations/laboratory-sampling-data`
- FSIS raw-poultry sampling catalog: `https://catalog.data.gov/dataset/fsis-laboratory-sampling-data-raw-poultry-sampling`
- FSIS establishment directory: `https://www.fsis.usda.gov/inspection/establishments/meat-poultry-and-egg-product-inspection-directory`
- FSIS annual recall summaries: `https://www.fsis.usda.gov/food-safety/recalls-public-health-alerts/annual-recall-summaries`
- USAspending API docs: `https://api.usaspending.gov/docs/`
- USAspending API endpoints: `https://api.usaspending.gov/docs/endpoints`
- EPA SDWA download summary: `https://echo.epa.gov/tools/data-downloads/sdwa-download-summary`
- CMS nursing-home topic: `https://data.cms.gov/provider-data/topics/nursing-homes`
- CMS nursing-home archives: `https://data.cms.gov/provider-data/archived-data/nursing-homes`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. **Mission bottleneck fit** — likelihood of exposing an actionable real-world bottleneck rather than merely reproducing a published metric.
2. **Cross-dataset information gain** — value created by combining distinct official tables/systems/snapshots.
3. **Direct outcome quality** — future outcome is directly observed and temporally separable.
4. **Independent-unit prospect** — sufficient genuinely independent establishments/recipients/water systems/nursing homes are likely available.
5. **Practical decision value** — a valid result could improve operational or policy understanding without unsafe targeting.
6. **Zero-cost operability** — official public sources plus standard compute suffice under COST-001.
7. **Source-native join defensibility** — exact official identifier continuity is strong; name/address/fuzzy/geospatial/manual reconciliation is penalized.
8. **Next-gate information gain** — an outcome-blind F01 can cheaply falsify the hardest structural assumption before outcomes.
9. **Low overlap / novelty risk** — direct literature, agency-integrated scoring or mature supervisory/regulatory precedent receives a lower score.

Dimension 7 remains the first interpretive priority. Apparent entity similarity is not enough without exact source-native identity.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:

1. source-native join defensibility;
2. next-gate information gain;
3. low overlap / novelty risk;
4. cross-dataset information gain;
5. independent-unit prospect;
6. zero-cost operability;
7. direct outcome quality.

If still tied, **no selection** is made until an outcome-blind source/literature discriminator is documented. Candidate outcomes may not be opened to break a tie.

## Revalidation order / 재검증 순서

After this contract is committed and Issue-bound:

1. official source/schema/current-access revalidation;
2. internal-history overlap check against prior repo branches;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable scorecard;
5. select at most one separate outcome-blind F01 candidate.

The candidate pool, rubric, tie-break and scoring dimensions may not change after revalidation evidence is observed.

## Non-claims / 비주장

R37 establishes no food-recall relationship, vendor interruption relationship, drinking-water violation relationship, nursing-home quality relationship, prediction, ranking, causal effect, novelty claim or commercial recommendation.

Incremental monetary cost must remain **0 USD**.
