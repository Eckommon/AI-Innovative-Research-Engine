---
id: PORTFOLIO-R39
type: stage0-cross-domain-reselection
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FDIC-BRANCH-N01
parent_disposition: HOLD_US_FDIC_BRANCH_N01_BASELINE_BALANCE_NOT_IDENTIFIABLE
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R39 — independent reselection after FDIC branch N01 scientific HOLD

## Mission / 목적

Select exactly one next **outcome-blind F01** after `US-FDIC-BRANCH-N01` terminated scientifically because three prospectively frozen baseline-balance gates failed. R39 must not lower the 75% balance threshold, alter the ratio band/quartile exposure/matching order, reopen the 2025 FDIC outcome, or rescue any prior R34–R38 near-miss by cosmetic redesign.

R39 deliberately moves to four new unit/outcome families: tax-exempt organizations, county-industry business structure, disaster-to-housing-recovery geography, and private employee-benefit plans. Candidate future outcome membership remains unopened during portfolio selection.

## Frozen candidates / 고정 후보

### 1. `US-IRS-EO-001` — filed nonprofit operational/financial structure → subsequent automatic revocation

**Question:** Can IRS public Form 990-series filings and the IRS Automatic Revocation List support a prospective organization-level design using exact EIN, without name/address repair and without using prior nonfiling as a tautological exposure?

- prospective exposure family: publicly disclosed, actually filed Form 990/990-EZ/990-PF operational, financial and governance fields from historical e-file XML releases;
- future outcome family: later IRS automatic revocation of tax-exempt status under IRC §6033(j), with reinstatement and pre-existing revocation handled only by a later preregistered adjudication rule;
- source-native identity prospect: exact Employer Identification Number (`EIN`) only;
- practical value: nonprofit operational continuity, service-capacity fragility and reporting sustainability;
- anti-tautology boundary: prior missed filings/nonfiling streaks may not be used as the candidate exposure because automatic revocation is mechanically triggered by three consecutive missed annual filings;
- F01 only: prove historical Form-990 XML/index access, EIN semantics/coverage, longitudinal filed-organization support, Automatic Revocation schema/date semantics and a sealed future-membership firewall.

No nonprofit risk ranking, revocation probability, causal claim, compliance recommendation or novelty claim is authorized in R39.

### 2. `US-BLS-CBP-001` — county-industry labor-cost/employment structure → subsequent establishment contraction

**Question:** Can BLS QCEW and Census County Business Patterns support a prospective county × industry design using deterministic FIPS + NAICS keys, with historical labor-market structure separated from later establishment-count contraction?

- prospective exposure family: BLS QCEW county-industry employment, establishment, wage and payroll structure;
- future outcome family: later Census County Business Patterns establishment-count change under a separately preregistered contraction definition;
- deterministic identity prospect: county FIPS + a prospectively fixed compatible NAICS level/version only; no names/geospatial repair;
- practical value: local industry-capacity contraction and regional labor-market bottlenecks;
- known limitation: this is an aggregate cell rather than a persistent establishment identity, and NAICS revisions/suppression/release lag are first-order F01 risks;
- F01 only: prove exact geography/industry code concordance, historical release lineage, support cardinality, suppression handling and a future-period firewall.

No county/industry ranking, recession prediction, causal claim, policy recommendation or novelty claim is authorized in R39.

### 3. `US-FEMA-BPS-001` — county disaster-designation burden → subsequent residential-permit recovery

**Question:** Can FEMA disaster-designation data and Census Building Permits Survey county files support a temporally separated county-level recovery design using exact five-digit county FIPS only?

- prospective exposure family: FEMA disaster declarations/designated counties, declaration timing and assistance designation structure;
- future outcome family: later Census BPS county residential units authorized by building permits, under a separately preregistered recovery/non-recovery measure;
- source-native/deterministic identity prospect: exact five-digit county FIPS only;
- practical value: housing-recovery and local construction-capacity bottlenecks after disasters;
- known overlap: disaster recovery, construction and permit response have substantial prior literature, so novelty credit must be conservative;
- F01 only: prove county-FIPS semantics, historical monthly/annual coverage, independent-county/event support, calendar alignment and sealed future permit outcomes.

No disaster-response ranking, causal effect, recovery prediction, public-policy recommendation or novelty claim is authorized in R39.

### 4. `US-DOL-5500-001` — employee-benefit-plan operating structure → subsequent final return/termination

**Question:** Can Department of Labor Form 5500/5500-SF public datasets support a prospective plan-level continuity design using the source-native sponsor EIN + plan number identity and a later final-return/termination state?

- prospective exposure family: historical plan assets, participants, contributions, benefit-plan features and filing structure in DOL Form 5500/5500-SF public datasets;
- future outcome family: later final return/report or other directly documented plan-termination state under a separately preregistered rule;
- source-native identity prospect: exact sponsor EIN + three-digit plan number, with acknowledgement ID retained only as filing-instance metadata;
- practical value: employee-benefit-plan continuity and retirement/welfare-plan operational fragility;
- known limitation: exposure and outcome largely reside within the same EFAST/Form-5500 reporting system, reducing cross-system information gain; plan mergers/transfers/final asset distribution require prospective adjudication;
- F01 only: prove plan identity semantics across years/forms, latest-vs-all filing rules, longitudinal cardinality, final-return field semantics and a future-period firewall.

No pension/benefit-plan ranking, termination probability, fiduciary recommendation, causal claim or novelty claim is authorized in R39.

## Frozen official source anchors / 공식 소스 앵커

These anchors establish source families only and do **not** authorize candidate future outcome row access.

- IRS public disclosure datasets/downloads: `https://www.irs.gov/charities-non-profits/public-disclosure-datasets-and-downloads`
- IRS Form 990 series downloads: `https://www.irs.gov/charities-non-profits/form-990-series-downloads`
- IRS automatic revocation documentation: `https://www.irs.gov/charities-non-profits/automatic-revocation-of-exemption`
- BLS QCEW: `https://www.bls.gov/cew/`
- Census County Business Patterns: `https://www.census.gov/programs-surveys/cbp/data.html`
- FEMA OpenFEMA / disaster data family: `https://www.fema.gov/about/openfema/data-sets`
- Census Building Permits Survey: `https://www.census.gov/construction/bps/`
- DOL Form 5500 datasets: `https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/public-disclosure/foia/form-5500-datasets`
- DOL Form 5500 datasets guide: `https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/public-disclosure/foia/form-5500-datasets-guide`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-dataset information gain
3. Direct outcome quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. Next-gate information gain
9. Low overlap / novelty risk

Dimension 7 remains the first interpretive priority. Exact official identity or a prospectively fixed official deterministic code key is required. Name/address/fuzzy/geospatial/manual reconciliation is penalized and may not be introduced after outcome access.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order: (1) source-native/deterministic join defensibility, (2) next-gate information gain, (3) low overlap/novelty risk, (4) cross-dataset information gain, (5) independent-unit prospect, (6) zero-cost operability, (7) direct outcome quality. If still tied, make no selection until an outcome-blind discriminator is documented.

## Revalidation order / 재검증 순서

After this contract commit and Issue binding:

1. official source/schema/current-access revalidation;
2. internal-history overlap check against canonical branches and near-misses;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

Candidate pool, rubric, tie-break, exposure/outcome families and anti-tautology boundaries may not change after this commit. Candidate future outcome rows or memberships may not be opened to score or break a tie.

## Frozen exclusions / 고정 제외

- `US-FDIC-BRANCH-001` and descendants: immediate N01 rescue prohibited; 2025 closure/non-continuation outcomes remain sealed.
- R38 near-misses (`US-FRA-XING-001`, `US-FCC-BDC-001`, `US-CMS-DIALYSIS-001`) are not re-entered.
- R37 near-misses (`US-FSIS-SAMPLE-001`, `US-USASPEND-VENDOR-001`, `US-EPA-SDWIS-001`, `US-CMS-NH-001`) are not re-entered.
- R36 near-misses (`US-EIA-GEN-001`, `US-EDU-FIN-001`, `US-FDIC-BANK-001`, `US-CMS-HOSP-001`) are not re-entered.
- R35/R34 terminal or near-miss families (FAA-AIP, DWSRF, PHMSA, NRC, EPA-XMEDIA, BTS-Port, USCG-Vessel, MSHA) are not rescued.
- USPTO patent-maintenance concepts are excluded from this round because current maintenance-fee lookup is moving behind USPTO.gov account authentication, weakening anonymous zero-cost runner operability.

## Non-claims / 비주장

R39 establishes no nonprofit revocation relationship, county-industry contraction relationship, disaster-recovery relationship, benefit-plan termination relationship, prediction, ranking, causal effect, novelty claim or operational recommendation.

Incremental monetary cost must remain **0 USD**.
