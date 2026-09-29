---
id: PORTFOLIO-R43
type: stage0-cross-domain-reselection
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: UK-CQC-LOC-F01
parent_disposition: HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R43 — independent cross-domain reselection after CQC F01 HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `UK-CQC-LOC-F01` terminated under its prospectively frozen exact-Location-ID support gates.

R43 must not rescue CQC by allowing punctuation after observation, lowering support thresholds, substituting Provider ID, using name/address/postcode/fuzzy/geospatial/manual identity repair, or relabeling all deactivations as closures.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `CA-CORP-001` — federal corporation filing/status structure → subsequent non-compliance dissolution

Unit: one Corporations Canada federal corporation.

- historical exposure prospect: non-outcome corporate status, governing legislation, registered-office/director and filing-history structure from official federal corporation data;
- future event prospect: later **dissolved for non-compliance** under the CBCA, prospectively separated from voluntary dissolution, amalgamation and discontinuance;
- source-native identity prospect: exact **Corporation Number / corporationId**;
- official source strength: Corporations Canada exposes open data, a federal corporation JSON API, current status semantics, and monthly transaction lists including notices/certificates of dissolution;
- anti-tautology boundary: overdue-filing flags, notice-of-intent-to-dissolve membership, dissolution-pending status and any field mechanically encoding the later non-compliance dissolution may not be used as historical exposure;
- F01 only: prove exact corporation identity, historical snapshot/data availability, dissolution reason semantics, minimum active support, future transaction sealing and anti-tautology separation.

No corporate failure probability, credit score, investment decision or causal claim is authorized.

### 2. `UK-CHARITY-001` — charity reporting/governance structure → subsequent removal from register

Unit: one Charity Commission registered charity in England and Wales.

- historical exposure prospect: non-outcome annual-return, governance/classification and financial structure from the daily full-register extracts;
- future event prospect: later removal from the Register of Charities under a prospectively fixed **removal_reason** hierarchy;
- source-native identity prospect: exact registered **charity number** plus suffix where source semantics require it;
- official source strength: Charity Commission provides daily full-register JSON/tab-delimited downloads including charity, annual-return-history and event-history tables; current data definitions include `date_of_removal`, `reporting_status` and `removal_reason`;
- critical limitation: this overlaps conceptually with the prior IRS exempt-organization branch; novelty/information-gain credit must therefore be conservative;
- anti-tautology boundary: prior removal status, removal date/reason, submission-default status or equivalent mechanically proximate removal trigger may not be an exposure;
- F01 only: prove exact charity identity across historical reporting and removal fields, sufficient longitudinal support, reason semantics, snapshot reproducibility and future membership sealing.

No charity viability score, donor recommendation, governance ranking or causal claim is authorized.

### 3. `UK-EA-PERMIT-001` — environmental-permit compliance structure → subsequent permit surrender/revocation

Unit: one Environment Agency environmental permit in England.

- historical exposure prospect: prior non-outcome permit structure and compliance-assessment/breach history under a later F01-frozen permit family;
- future event prospect: later source-native **surrender** or **revocation**, prospectively separated from ordinary variation/transfer;
- source-native identity prospect: exact **permit/registration reference**;
- official source strength: Environment Agency Public Registers provide searchable/downloadable complete registers and an API without registration; the permit ontology includes status, effective date, surrender date, revocation date and cancellation date; historical compliance datasets are publicly published;
- critical limitation: Environment Agency datasets can carry conditional reuse licences, and EPA/RCRA environmental-compliance work already exists in this project, requiring strong overlap penalty;
- F01 only: prove exact permit identity across compliance and register sources, licence-compatible zero-cost use, event semantics, historical lineage, cardinality and future-event sealing.

No facility enforcement targeting, environmental-risk score or causal claim is authorized.

### 4. `US-USDA-PACA-001` — produce-license business structure → subsequent PACA suspension/revocation

Unit: one USDA Perishable Agricultural Commodities Act licensee.

- historical exposure prospect: non-outcome licence/business structure available from official PACA licence search/public information;
- future event prospect: later licence suspension or revocation under a prospectively fixed disciplinary-event hierarchy;
- source-native identity prospect: exact PACA licence identifier if the official source exposes a stable machine-readable key;
- official source strength: USDA AMS operates PACA licensing/enforcement and an official licence search with complaint information;
- critical limitation: anonymous bulk historical snapshot access and stable machine-readable licence identity have not yet been established; complaint/disciplinary fields may also create anti-tautology leakage;
- F01 only: prove exact licence identity, anonymous zero-cost historical source access, disciplinary-event semantics, cardinality, anti-tautology separation and future-event sealing.

No produce-firm risk score, enforcement recommendation or causal claim is authorized.

## Frozen official source anchors / 공식 소스 앵커

### Corporations Canada
- `https://ised-isde.canada.ca/site/corporations-canada/en/data-services`
- `https://ised-isde.canada.ca/site/corporations-canada/en/accessing-federal-corporation-json-datasets`
- `https://ised-isde.canada.ca/site/corporations-canada/en/data-services/monthly-transactions/certificates-dissolution-cbca-section-212`

### Charity Commission
- `https://register-of-charities.charitycommission.gov.uk/en/register/full-register-download`
- `https://api-portal.charitycommission.gov.uk/content/API_data_definition_v1.pdf`

### Environment Agency
- `https://environment.data.gov.uk/public-register/view/index`
- `https://www.api.gov.uk/ea/public-registers-for-environmental-information/`
- `https://www.data.gov.uk/dataset/d49096ed-e89c-488f-9bae-d79ef4891394/national-compliance-assessment`

### USDA PACA
- `https://www.ams.usda.gov/rules-regulations/paca/epacaportal`
- `https://www.ams.usda.gov/rules-regulations/paca`

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

If still tied, make no selection until an outcome-blind discriminator is documented.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:

1. current official source/schema/access revalidation;
2. canonical internal-history overlap check;
3. bounded external literature/framework overlap check;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- CQC and descendants: immediate rescue prohibited.
- R42 held candidates BSEE, SAM and Ofsted are not re-entered.
- R41/R40 held candidates remain out of the immediate pool.
- `UK-CHARITY-001` receives a strong conceptual-overlap penalty for the prior IRS exempt-organization branch.
- `UK-EA-PERMIT-001` receives a strong environmental-compliance overlap penalty for prior EPA/RCRA branches.
- PACA complaint/enforcement information may not be used as historical exposure if it mechanically encodes the later disciplinary event.
- FCA Register bulk extracts are excluded from this no-cost pool because official bulk extracts are paid; free API-key access does not justify a bulk-snapshot assumption.
- USPTO maintenance remains excluded for unstable anonymous zero-cost operational access.

## Non-claims / 비주장

R43 establishes no corporation-dissolution relationship, charity-removal relationship, permit-revocation relationship, PACA disciplinary relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
