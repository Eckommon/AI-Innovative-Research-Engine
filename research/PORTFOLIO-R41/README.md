---
id: PORTFOLIO-R41
type: stage0-cross-domain-reselection
created: 2026-09-21
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FCC-ULS-F01
parent_disposition: HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R41 — independent cross-domain reselection after FCC ULS F01 HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `US-FCC-ULS-F01` terminated at its prospectively frozen 9/18 structural HOLD. R41 must not rescue the FCC branch by zero-padding/reinterpreting its system identifier, lowering thresholds, changing radio-service family, substituting another identifier, or opening future Microwave daily transaction bodies.

`US-FCC-ULS-F01`은 사전고정 18개 gate 중 9개만 통과해 terminal HOLD가 되었다. R41은 FCC branch를 사후구제하지 않고 서로 다른 unit/event family를 독립적으로 비교하여 최대 1개의 새로운 outcome-blind F01만 선택한다.

No candidate future-event membership, effect, prediction, ranking or causal result may be opened during R41 scoring. / R41 scoring 중 어떤 후보의 미래 event membership·효과·예측·순위·인과 결과도 열지 않는다.

## Frozen candidates / 고정 후보

### 1. `US-HUD-MF-001` — FHA multifamily property/mortgage structure → subsequent adverse mortgage-insurance termination

**Question / 질문:** Can HUD's active/terminated FHA multifamily mortgage and property datasets support an exact FHA-project-level prospective design that distinguishes adverse claim/default termination from routine prepayment or voluntary termination?

- historical exposure prospect: non-outcome mortgage/property/contract structure from official HUD multifamily files; a later F01 may also test deterministic crosswalk support to HUD property/inspection data, but may not assume it;
- future event prospect: a later FHA multifamily insurance termination with prospectively frozen reason hierarchy;
- source-native identity prospect: exact **FHA Project Number**;
- required anti-ambiguity rule: routine prepayment, voluntary termination, maturity/refinance and adverse/default/claim termination may not be silently pooled;
- known risk: current public active/terminated workbook description exposes FHA Project Number and mortgage structure, while reason-code availability and crosswalk to property/inspection identifiers require direct F01 verification;
- practical value: affordable-housing financing continuity and distressed multifamily asset bottlenecks.

F01 only: prove exact project identity, active→terminated source lineage, termination-reason field semantics, adequate cardinality, optional property crosswalk without fuzzy address matching, historical snapshot reproducibility and a sealed future-event firewall.

### 2. `US-FAA-REG-001` — aircraft registration/document structure → subsequent deregistration/revocation

**Question / 질문:** Can FAA's releasable aircraft registry support a prospective aircraft-level design that separates later deregistration/revocation from ordinary registration churn without treating reassigned N-numbers as stable aircraft identity?

- historical exposure prospect: registration/master/document structure from the official releasable aircraft database;
- future event prospect: later deregistration or a prospectively defined adverse registration-state transition;
- identity prospect: exact source-native aircraft serial number plus documented manufacturer/model context; **N-number alone is prohibited** because reassignment is possible;
- known strength: FAA publishes Master and Deregistered files in one free, daily-refreshed archive and documents deregistered aircraft plus status codes;
- known risk: deregistration includes heterogeneous administrative/economic reasons, and exact identity continuity across reassigned N-numbers must be proven rather than assumed;
- practical value: civil-aircraft registration continuity and administrative/enforcement bottlenecks.

F01 only: prove deterministic aircraft identity across Master/Deregistered records, event/status/date semantics, sufficient cohort/event support and a future-row firewall.

### 3. `US-SEC-ADV-001` — investment-adviser operating structure → subsequent Form ADV-W withdrawal/cancellation

**Question / 질문:** Can official SEC Form ADV Part 1 and Form ADV-W data support a prospective adviser-level design using exact regulatory identifiers while separating ordinary jurisdictional switching/voluntary withdrawal from economically or regulatorily adverse cessation?

- historical exposure prospect: non-outcome adviser operating/business structure from Form ADV Part 1;
- future event prospect: later full Form ADV-W withdrawal or separately documented SEC registration cancellation under a prospectively fixed adjudication rule;
- source-native identity prospect: exact **Organization CRD Number** and/or SEC registration number only if official files establish deterministic continuity;
- known strength: SEC publishes historical Form ADV Part 1 and ADV-W CSV tables and explicitly requires ADV-W to withdraw registration;
- known risk: ADV-W includes routine switches to state registration and voluntary exits; cancellation under Advisers Act section 203(h) is distinct and may not be silently merged;
- practical value: registered-adviser continuity and regulatory-transition bottlenecks.

F01 only: prove exact adviser identity, historical/current official source lineage, withdrawal/cancellation reason semantics, cardinality and a sealed future-event boundary.

### 4. `UK-CH-DISS-001` — Companies House filing/accounts structure → subsequent company dissolution

**Question / 질문:** Can Companies House free company and accounts data support a prospectively separated UK-company design using exact company number before later dissolved status/date is opened?

- historical exposure prospect: filing timeliness/status/SIC plus bounded electronically filed accounts structure from free Companies House products;
- future event prospect: later dissolved company status/date under a separately frozen adjudication rule;
- source-native identity prospect: exact **company number**;
- known strength: free monthly company snapshots, daily accounts files and real-time public company information/API use the company number;
- known limitation: corporate dissolution/failure is a mature research topic and the event is largely within the same registry ecosystem; novelty and cross-system information-gain credit must be conservative;
- practical value: enterprise continuity and administrative dissolution bottlenecks.

F01 only: prove exact company-number continuity, historical snapshot/account availability, dissolved-event semantics, sufficient independent-company support and a future-event firewall.

## Frozen official source anchors / 공식 소스 앵커

### HUD multifamily
- `https://www.hud.gov/hud-partners/multifamily-fhasl-active`
- `https://www.hud.gov/hud-partners/multifamily-preservation`
- `https://www.hud.gov/hud-partners/multifamily-data`

### FAA aircraft registry
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`
- `https://registry.faa.gov/database/ardata.pdf`

### SEC investment advisers
- `https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data`
- `https://www.sec.gov/files/formadv-w.pdf`
- `https://www.sec.gov/about/divisions-offices/division-investment-management/electronic-filing-investment-advisers-iard/frequently-asked-questions-form-adv-iard`

### UK Companies House
- `https://download.companieshouse.gov.uk/`
- `https://download.companieshouse.gov.uk/en_accountsdata.html`
- `https://www.gov.uk/guidance/searching-the-companies-house-register`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. **Mission bottleneck fit**
2. **Cross-dataset / cross-table information gain**
3. **Direct future-event quality**
4. **Independent-unit prospect**
5. **Practical decision value**
6. **Zero-cost operability**
7. **Source-native/deterministic join defensibility**
8. **Next-gate information gain**
9. **Low overlap / novelty risk**

Dimension 7 remains the first interpretive priority. / 7번 deterministic join defensibility를 최우선 해석 기준으로 유지한다.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:

1. source-native/deterministic join defensibility;
2. next-gate information gain;
3. low overlap / novelty risk;
4. direct future-event quality;
5. independent-unit prospect;
6. zero-cost operability;
7. cross-dataset information gain.

If still tied, make no selection until an outcome-blind source/literature discriminator is documented. / 그래도 동점이면 outcome-blind 추가 근거 전까지 선정하지 않는다.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:

1. official source/schema/current-access revalidation;
2. internal-history overlap check against canonical terminal/near-miss branches;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

Candidate identities, event families, rubric and tie-break may not change after this commit.

## Frozen exclusions / 고정 제외

- `US-FCC-ULS-001` and descendants: immediate rescue prohibited.
- R40 held candidates `US-SEC-ISSUER-001`, `US-FMCSA-CARRIER-001`, `US-NCES-SCHOOL-001` are not re-entered.
- R39 `US-DOL-5500-001` / benefit-plan termination family is not re-entered; PBGC/DOL retirement-plan termination variants are treated as overlap, not a fresh candidate.
- `US-FAA-AIP-F01` remains terminal HOLD; `US-FAA-REG-001` is a distinct aircraft-level registration family but receives a conservative same-agency/aviation overlap penalty.
- `US-SEC-ADV-001` is distinct from R40's public-issuer/Form-25 family but receives a conservative same-agency/financial-regulation overlap penalty.
- All prior R36–R40 terminal/near-miss families remain non-rescuable unless a later portfolio contract explicitly establishes a materially different unit/event family before observation.
- USPTO maintenance remains excluded because anonymous zero-cost operational access has not been sufficiently stable.

## Non-claims / 비주장

R41 establishes no HUD default relationship, aircraft deregistration relationship, investment-adviser exit relationship, company-dissolution relationship, prediction, ranking, causal effect, novelty claim, investment/regulatory/housing/aviation recommendation or commercial action.

Incremental monetary cost must remain **0 USD**.
