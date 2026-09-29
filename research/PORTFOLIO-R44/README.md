---
id: PORTFOLIO-R44
type: stage0-cross-domain-reselection
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: CA-CORP-F01
parent_disposition: HOLD_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R44 — independent cross-domain reselection after CA-CORP F01 HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `CA-CORP-F01` terminated under its frozen 14/18 structural HOLD.

R44 must not rescue CA-CORP by substituting another corporation baseline, reinterpreting anniversary/annual-filing/meeting dates as incorporation dates, loosening the date requirement, changing the legal population, or opening future section-212 membership.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `EU-EMA-MA-001` — centrally authorised medicine structure → subsequent marketing-authorisation withdrawal/suspension

Unit: one centrally authorised medicine/marketing authorisation.

- historical exposure prospect: non-outcome medicine/authorisation structure from official EMA medicine data tables and EPAR metadata;
- future event prospect: later European Commission marketing-authorisation withdrawal or suspension under a prospectively fixed reason hierarchy;
- source-native identity prospect: exact **EMA product number** (for example `EMEA/H/C/...`);
- official source strength: EMA publishes downloadable medicine data tables updated overnight and medicine pages exposing authorisation/withdrawal dates and reasons;
- critical limitation: withdrawals may be voluntary/commercial, regulatory/safety-related or otherwise heterogeneous; no undifferentiated withdrawal endpoint is allowed;
- F01 only: prove exact EMA product-number continuity, current/historical table lineage, withdrawal/suspension reason/date semantics, minimum support and a sealed future-event boundary.

No medicine-risk score, prescribing recommendation, investment signal, pharmacovigilance claim or causal claim is authorized.

### 2. `US-FERC-HYDRO-001` — hydropower licence/project structure → subsequent licence surrender/termination

Unit: one FERC hydropower project/licence.

- historical exposure prospect: non-outcome active-license/project structure from FERC hydropower public data;
- future event prospect: later licence surrender, termination or equivalent project-level legal end state under a prospectively fixed adjudication hierarchy;
- source-native identity prospect: exact **FERC Project Number**;
- official source strength: FERC publishes a public Active Licenses hydropower dataset with downloadable CSV/XLSX and dataset API metadata;
- critical limitation: a reproducible zero-cost machine-readable historical surrender/termination event source has not yet been established;
- F01 only: prove exact project identity, active-source lineage, event source/date/reason semantics, sufficient support and future-event sealing.

No project failure score, relicensing recommendation, market signal or causal claim is authorized.

### 3. `AU-ACNC-CHARITY-001` — charity reporting/governance structure → subsequent registration revocation

Unit: one ACNC-registered charity.

- historical exposure prospect: Annual Information Statement, governance and non-outcome Charity Register structure;
- future event prospect: later ACNC registration revocation under a prospectively fixed revocation-reason hierarchy;
- source-native identity prospect: exact **ABN**;
- official source strength: ACNC publishes downloadable Charity Register and annual AIS datasets through official public-data channels;
- critical limitation: direct overlap with prior IRS exempt-organisation and UK-charity families is high, and revocation can be tied to filing default, creating tautology risk;
- anti-tautology boundary: filing-default/nonlodgment state, pending revocation notice or equivalent trigger may not be used as exposure;
- F01 only: prove exact ABN continuity, historical snapshot support, revocation reason/date semantics, anti-tautology separation and future membership sealing.

No donor recommendation, charity viability score, governance ranking or causal claim is authorized.

### 4. `UK-IPO-TM-001` — UK trade-mark application/registration structure → subsequent adverse final status

Unit: one UK trade-mark application/registration.

- historical exposure prospect: non-outcome application/registration structure from official UKIPO journal/register surfaces;
- future event prospect: later refused, invalidated, revoked or otherwise prospectively defined adverse final status, kept separate from ordinary expiry/non-renewal;
- source-native identity prospect: exact **UK trade-mark application/registration number**;
- official source strength: UKIPO Trade Mark Journal pages expose exact application numbers and publication dates;
- critical limitation: anonymous bulk historical/current status lineage has not yet been established, and ordinary expiry is mechanically time-driven;
- F01 only: prove exact identity, zero-cost machine-readable historical/current status source, adverse-event semantics, support/cardinality and a sealed future boundary.

No brand-value score, prosecution advice, infringement opinion or causal claim is authorized.

## Frozen official source anchors / 공식 소스

### EMA
- `https://www.ema.europa.eu/en/medicines/download-medicine-data`
- `https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/notifying-change-marketing-status`
- individual EPAR medicine pages using exact EMA product number

### FERC hydropower
- `https://data.ferc.gov/active-hydropower-projects/active-licenses/`
- FERC hydropower public-data/eLibrary surfaces only

### ACNC
- `https://www.acnc.gov.au/charity/about-charity-register/download-charity-register-data`
- official ACNC/data.gov.au Charity Register and Annual Information Statement datasets

### UKIPO
- official Trade Mark Journal / register surfaces under `https://www.ipo.gov.uk/`
- UK Government/IPO official data pages only

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

- CA-CORP and descendants: immediate rescue prohibited.
- R43 held UK-CHARITY, UK-EA-PERMIT and USDA-PACA candidates are not re-entered.
- R42/R41/R40 held candidates remain outside the immediate pool.
- `AU-ACNC-CHARITY-001` receives a severe nonprofit-overlap penalty for prior IRS/UK-charity work and must retain the anti-tautology boundary.
- FERC hydropower does not revive prior FAA/EIA/utility branches; it is a distinct licensed-project legal-state family but receives infrastructure/regulatory overlap credit conservatively.
- EMA withdrawal must keep voluntary/commercial withdrawal separate from safety/regulatory suspension or withdrawal.
- UKIPO ordinary expiry/non-renewal may not be treated as an adverse event merely because registration duration elapsed.
- FCA bulk extracts and any paid commercial registry remain excluded by COST-001.
- USPTO maintenance remains excluded for unstable anonymous zero-cost operational access.

## Non-claims / 비주장

R44 establishes no medicine-withdrawal relationship, hydropower-licence termination relationship, charity-revocation relationship, trade-mark adverse-status relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
