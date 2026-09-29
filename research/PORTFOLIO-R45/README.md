---
id: PORTFOLIO-R45
type: stage0-cross-domain-reselection
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: EU-EMA-MA-F01
parent_disposition: HOLD_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R45 — independent cross-domain reselection after EMA F01 HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `EU-EMA-MA-F01` terminated under its prospectively frozen 15/18 structural HOLD.

R45 must not rescue EMA by narrowing the focal population, lowering date-support thresholds, substituting another date field, weakening historical event-date support, collapsing event classes, or opening future withdrawal/suspension membership.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `US-MSHA-MINE-001` — mine operating/employment structure → subsequent serious/fatal accident event

Unit: one MSHA Mine ID.

- historical exposure prospect: non-outcome mine type/status, employment/production and bounded inspection/violation structure from official MSHA public datasets;
- future event prospect: later source-native serious/fatal accident/injury event under a prospectively fixed degree/event hierarchy;
- source-native identity prospect: exact **Mine ID**;
- official source strength: MSHA publishes open-government mine, quarterly employment/production and accident/injury datasets with stable Mine ID concepts and regular updates;
- critical limitation: accident/injury rows have their own document number as row key, so F01 must prove deterministic Mine-ID linkage and event severity/date semantics rather than assume all accident rows are comparable;
- anti-tautology boundary: future-event flags, accident rows inside the future window, fatality summaries, or mechanically outcome-defining fields may not be historical exposure;
- F01 only: prove exact Mine-ID support across baseline/employment/accident sources, historical lineage, severe-event semantics, minimum mine/event support and sealed future-event membership.

No mine safety score, enforcement targeting, employment recommendation or causal claim is authorized.

### 2. `US-NCUA-CU-001` — credit-union call-report structure → subsequent involuntary liquidation

Unit: one federally insured credit union charter.

- historical exposure prospect: non-outcome financial/operating structure from official NCUA quarterly Call Report data;
- future event prospect: later **involuntary liquidation**, kept separate from ordinary voluntary merger, assisted merger, conservatorship and voluntary liquidation;
- source-native identity prospect: exact **credit-union charter number**;
- official source strength: NCUA publishes quarterly final call-report ZIP/CSV data from 1994 onward, active credit-union lists, merger reports and conservatorship/liquidation public records;
- critical limitation: the public event table foregrounds credit-union name/city/state and may require exact charter-number recovery from official event-detail/charter-event sources; name matching is prohibited;
- F01 only: prove exact charter identity across call reports and adverse charter-event records, event-type separation, historical support, future sealing and zero-cost operability.

No credit-risk score, depositor recommendation, supervisory recommendation or causal claim is authorized.

### 3. `US-CMS-NH-001` — nursing-home staffing/quality structure → subsequent Medicare termination notice

Unit: one nursing home/provider CCN.

- historical exposure prospect: non-outcome Provider Information, staffing, quality and inspection structure from official CMS Provider Data Catalog;
- future event prospect: later CMS Medicare termination notice for the same CCN, kept separate from ownership changes, voluntary closure and non-termination sanctions;
- source-native identity prospect: exact **CMS Certification Number (CCN)**;
- official source strength: CMS publishes current nursing-home datasets plus archived data and public termination notices carrying provider CCN;
- critical limitation: public termination notices are posted for only a bounded recent period, so historical event lineage/support may be limited;
- anti-tautology boundary: termination notice status, immediate termination-pending fields or equivalent direct outcome encodings may not be used as exposure;
- F01 only: prove exact CCN continuity, archived baseline support, historical termination lineage/cardinality, event semantics and future sealing.

No facility ranking, patient recommendation, enforcement targeting or causal claim is authorized.

### 4. `US-FDA-PMA-001` — Class III device PMA structure → subsequent withdrawal/suspension of PMA approval

Unit: one original FDA PMA application.

- historical exposure prospect: non-outcome PMA approval/application structure from official FDA downloadable PMA data;
- future event prospect: later FDA withdrawal or temporary suspension of **approved PMA**, kept separate from supplement withdrawal and applicant withdrawal before approval;
- source-native identity prospect: exact **PMA Number**;
- official source strength: FDA provides the PMA database/download files and publishes legal procedures for withdrawal/suspension of PMA approval;
- critical limitation: database rows also include supplements with their own withdrawal dates, creating a high risk of confusing supplement-level administrative withdrawal with withdrawal of the original approval;
- F01 only: prove original-PMA identity, event-level separation, historical withdrawal/suspension support and a future firewall.

No device safety score, clinical recommendation, market signal or causal claim is authorized.

## Frozen official source anchors / 공식 소스

### MSHA
- `https://www.msha.gov/mine-data-retrieval-system`
- `https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp`
- official MSHA accident/injury and quarterly employment/production datasets only

### NCUA
- `https://ncua.gov/analysis/credit-union-corporate-call-report-data/quarterly-data`
- `https://ncua.gov/analysis/chartering-mergers`
- `https://ncua.gov/support-services/conservatorships-liquidations`

### CMS nursing homes
- `https://data.cms.gov/provider-data/topics/nursing-homes`
- `https://www.cms.gov/medicare/health-safety-standards/certification-compliance/public-notices`

### FDA PMA
- `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm`
- `https://www.fda.gov/medical-devices/premarket-approval-pma/pma-review-process`

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

- EMA and descendants: immediate rescue prohibited.
- R44 held FERC, ACNC and UKIPO candidates are not re-entered.
- R43/R42/R41/R40 held candidates remain outside the immediate pool.
- NCUA receives a conservative financial-institution overlap penalty because FDIC branch work exists, but credit-union charter events are a different unit/event family.
- CMS receives a healthcare-provider closure/quality maturity penalty and must use exact CCN only.
- FDA receives a medical-regulatory overlap penalty after EMA and must keep original PMA approval events separate from supplements.
- MSHA may not define an event using outcome information unavailable before the future window and may not use name/operator matching to repair Mine ID.
- Paid commercial sources remain excluded by COST-001.

## Non-claims / 비주장

R45 establishes no mine-accident relationship, credit-union liquidation relationship, nursing-home termination relationship, PMA-withdrawal relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
