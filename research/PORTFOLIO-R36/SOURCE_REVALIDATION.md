# PORTFOLIO-R36 Source / Internal-History / Overlap Revalidation

Date: 2026-09-17
Contract: `6550f4cfbde9df2702c793b902d7676f05700d61`
Issue: #155
Candidate outcomes opened: **false**
Incremental monetary cost: **0 USD**

## Method boundary

This revalidation inspects official source availability/schema descriptions, repository history, and public literature/agency-framework descriptions only. It does not open candidate future outcome rows or calculate any candidate relationship.

## 1. `US-EIA-GEN-001`

### Official source support

- EIA-860 currently publishes annual generator-level detailed data, including plant/generator identity, operational status, planned generators and associated attributes. Current annual data include 2025 and historical years.
- EIA-860M is the monthly supplement monitoring existing and proposed generating units. The current public page (release 2026-08-26 for July 2026 inventory) states that it tracks proposed-generator status and schedule and includes comprehensive retired-generator inventory since 2017-era releases.
- The exact prospective identity route is source-native EIA plant code + generator ID across EIA-860/860M snapshots; F01 must prove longitudinal uniqueness and status/date semantics without opening a future slippage outcome.

Official anchors:
- `https://www.eia.gov/electricity/data/eia860/`
- `https://www.eia.gov/electricity/data/eia860m/index.php`

### Internal history

No prior repository branch matching EIA proposed-generator commissioning/slippage was found in bounded internal search.

### Overlap / novelty risk

EIA itself has already published aggregate analyses of generator/solar project delays using EIA-860/860M, including a 2023 article on solar delays and a 2025 article on expected-online-date delays. Therefore R36 must **not** claim novelty for observing that delays exist. Remaining information gain is narrower: whether exact generator-level longitudinal snapshots can support a preregistered, independent-unit bottleneck design that distinguishes schedule/status trajectories without post-hoc identity repair.

Revalidation status: **STRONG_F01_CANDIDATE__SOURCE_NATIVE_ID__AGENCY_DELAY_PRECEDENT_PENALTY**.

## 2. `US-EDU-FIN-001`

### Official source support

- IPEDS publishes downloadable finance, enrollment, graduation/outcome and institutional data with `UNITID` as the institutional identifier.
- College Scorecard institution-level documentation includes IPEDS `UNITID`, but Department of Education Title-IV entity construction and branch/main-campus relationships can involve OPEID/UNITID crosswalk logic. The frozen candidate therefore permits only exact UNITID-present-in-both-source use and prohibits any local OPEID/name/address repair.

Official anchors:
- `https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?rtid=1`
- `https://collegescorecard.ed.gov/data/`

### Internal history

No prior repository branch matching IPEDS finance → institution closure/operating status was found in bounded internal search.

### Overlap / novelty risk

Direct overlap is severe. Kelchen, Ritter and Webber's NBER work `Predicting College Closures and Financial Distress` assembles institution operating dates, finance, enrollment/staff and other characteristics and explicitly develops predictive models of closure/financial distress. The 2026 published chapter and 2024 working paper make the proposed R36 relation near-direct precedent rather than a white-space discovery.

Revalidation status: **TECHNICALLY_STRONG__DIRECT_NEAR_IDENTICAL_LITERATURE_OVERLAP**.

## 3. `US-FDIC-BANK-001`

### Official source support

- FDIC Bank Data Guide exposes quarterly financial data/API/bulk downloads for FDIC-insured institutions and historical Call Reports.
- FDIC Failures and Assistance / Failed Bank List exposes failure dates and `Cert`, the FDIC certificate number assigned to identify institutions.
- The prospective identity route is exact `Cert` only.

Official anchors:
- `https://www.fdic.gov/bank-data-guide/data-downloads`
- `https://banks.data.fdic.gov/bankfind-suite/failures`

### Internal history

No prior repository branch matching FDIC Call Report financial structure → bank failure was found in bounded internal search.

### Overlap / novelty risk

Bank-failure prediction from CAMEL/financial ratios is a mature literature and closely aligned with supervisory-risk practice. Published work explicitly uses FDIC-insured bank failures and financial indicators for failure prediction. This is an excellent exact-ID calibration problem but a weak innovation-discovery candidate.

Revalidation status: **EXACT_ID_AND_DIRECT_OUTCOME__MATURE_SUPERVISORY_AND_LITERATURE_OVERLAP**.

## 4. `US-CMS-HOSP-001`

### Official source support

- CMS Provider Data Catalog currently publishes provider-level `Timely and Effective Care - Hospital` datasets and provider-level `Unplanned Hospital Visits - Hospital` datasets through download/API routes.
- Provider-level hospital files use CMS Certification Number semantics, giving a strong exact-CCN identity prospect.

Official anchors:
- `https://data.cms.gov/provider-data/topics/hospitals`
- `https://data.cms.gov/provider-data/topics/hospitals/unplanned-hospital-visits`

### Internal history

No prior repository branch matching CMS timely/effective process measures → later unplanned visits was found in bounded internal search.

### Overlap / novelty risk

CMS already treats readmission/unplanned-visit measures as formal hospital-quality measures, performs risk adjustment and significance testing, and operates the Hospital Readmissions Reduction Program for specified readmission outcomes. A generic process-measure → readmission relation therefore has substantial agency-framework and research overlap even though source-native CCN joins are strong.

Revalidation status: **TECHNICALLY_STRONG__AGENCY_INTEGRATED_QUALITY_FRAMEWORK_OVERLAP**.

## Portfolio implication before scoring

All four candidates remain in the frozen pool. No candidate is removed after revalidation. The immutable scorecard must preserve these overlap penalties rather than rewrite candidate definitions or inspect outcomes.
