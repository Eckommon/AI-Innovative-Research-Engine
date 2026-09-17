---
id: PORTFOLIO-R36
type: stage0-cross-domain-reselection
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FAA-AIP-F01
parent_disposition: HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R36 — independent cross-domain reselection after FAA-AIP F01 HOLD

## Mission / 목적

Select exactly one next **outcome-blind F01** candidate after `US-FAA-AIP-F01` terminated at its frozen state-concordance gate. R36 must not rescue the FAA branch, lower its 99% threshold, reconcile its 49 conflicts, or reuse FAA delay outcomes.

The portfolio is deliberately diversified across energy infrastructure, higher education, banking, and hospital operations. Candidate outcome rows remain unopened until a later branch is separately designed and authorized.

## Frozen candidates / 고정 후보

### 1. `US-EIA-GEN-001` — proposed generator schedule → subsequent commissioning slippage

**Question:** Can public EIA generator inventories support a source-native generator-level longitudinal design in which previously declared project schedule/status attributes are linked to later actual commercial-operation timing or continued delay?

- prospective exposure/source family: EIA-860 annual and/or EIA-860M proposed-generator inventory;
- future outcome family: later EIA-860/860M operating status and actual operation date;
- identity prospect: exact EIA plant code + generator ID, with no name/geospatial repair;
- practical value: generation-project execution bottlenecks and infrastructure delivery;
- F01 only: prove exact longitudinal generator identity, date semantics, snapshot lineage, support/cardinality and outcome firewall.

No project delay direction, technology ranking, causal claim, probability or schedule-performance result is authorized in R36.

### 2. `US-EDU-FIN-001` — institutional financial-resource trajectory → subsequent operating/closure status

**Question:** Can IPEDS institutional finance/enrollment structure be linked prospectively to later institution operating/closure status using exact `UNITID` only?

- prospective exposure/source family: NCES IPEDS finance, enrollment and institutional characteristics;
- future outcome family: later official institution operating/closure status available through College Scorecard/Department of Education or IPEDS continuation status;
- identity prospect: exact `UNITID` present in both authorized datasets only;
- no OPEID↔UNITID manual/name/address reconciliation is permitted;
- practical value: institutional sustainability and education-market capacity stress;
- F01 only: prove exact UNITID continuity, temporal separation, source versioning and sufficient independent institutions.

No institution closure prediction, ranking, financial-health label or causal claim is authorized in R36.

### 3. `US-FDIC-BANK-001` — quarterly bank financial structure → subsequent failure event

**Question:** Can FDIC quarterly financial records and failure records support a prospectively separated institution-level design using exact FDIC certificate number (`Cert`)?

- prospective exposure family: FDIC/FFIEC quarterly financial data;
- future outcome family: FDIC Failures and Assistance / Failed Bank List;
- identity prospect: exact FDIC certificate number only;
- practical value: financial-system fragility calibration and public-data reproducibility;
- known risk: very high methodological/regulatory precedent, so novelty/mission value must be penalized conservatively;
- F01 only: prove exact longitudinal identity, historical snapshot support, event-date semantics and enough outcome-blind support.

No failure probability, bank ranking, supervisory inference or recommendation is authorized in R36.

### 4. `US-CMS-HOSP-001` — hospital care-process structure → subsequent unplanned-visit outcome

**Question:** Can CMS hospital provider-level process-of-care measures be linked prospectively to later unplanned hospital-visit measures with exact CMS Certification Number (`CCN`)?

- prospective exposure family: CMS Provider Data Catalog `Timely and Effective Care - Hospital` or structurally equivalent provider-level process measures;
- future outcome family: later `Unplanned Hospital Visits - Hospital`;
- identity prospect: exact CCN only;
- practical value: operational quality signals and provider-performance measurement;
- known risk: CMS already integrates broad quality frameworks and academic precedent is likely substantial;
- F01 only: prove exact CCN/time-window identity, archive/version support, independent provider cardinality and outcome firewall.

No hospital quality ranking, clinical recommendation, provider risk score or causal claim is authorized in R36.

## Frozen source anchors / 고정 공식 소스 앵커

These anchors establish source families only; they do **not** authorize candidate outcome access:

- EIA-860 annual: `https://www.eia.gov/electricity/data/eia860/`
- EIA-860M monthly inventory: `https://www.eia.gov/electricity/data/eia860m/index.php`
- NCES IPEDS Data Center: `https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?rtid=1`
- College Scorecard documentation/data: `https://collegescorecard.ed.gov/data/`
- FDIC Bank Data Guide / downloads: `https://www.fdic.gov/bank-data-guide/data-downloads`
- FDIC Failures and Assistance: `https://banks.data.fdic.gov/bankfind-suite/failures`
- CMS Provider Data Catalog hospitals: `https://data.cms.gov/provider-data/topics/hospitals`

## Frozen score rubric / 고정 평가표

Each candidate receives one immutable 0–5 score on exactly nine dimensions, total `/45`:

1. **Mission bottleneck fit** — likelihood of exposing an actionable real-world bottleneck rather than only reproducing a known association.
2. **Cross-dataset information gain** — value created by combining distinct tables/snapshots/systems rather than reading one published metric.
3. **Direct outcome quality** — future outcome is directly observed and temporally separable.
4. **Independent-unit prospect** — enough genuinely independent generators/institutions/banks/hospitals are likely available.
5. **Practical decision value** — result could inform infrastructure, market, operational or institutional decisions without unsafe targeting.
6. **Zero-cost operability** — official public data and standard compute suffice under COST-001.
7. **Source-native join defensibility** — exact official ID continuity is strong; agency-curated/manual crosswalk dependence is penalized.
8. **Next-gate information gain** — an outcome-blind F01 can cheaply falsify or validate the hardest assumption before outcomes.
9. **Low overlap / novelty risk** — high direct literature, agency-integrated scoring, or mature supervisory-model overlap receives a lower score.

R36 gives dimension 7 explicit priority in interpretation because the FAA branch showed that apparent code similarity without sufficiently strong source-native concordance is not enough.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:

1. source-native join defensibility;
2. next-gate information gain;
3. low overlap / novelty risk;
4. independent-unit prospect;
5. zero-cost operability;
6. direct outcome quality.

If still tied, **no selection** is made until an outcome-blind source/literature discriminator is documented. Candidate outcome rows must not be opened to break a tie.

## Revalidation order / 재검증 순서

After this contract is committed and Issue-bound:

1. official source/schema/current-access revalidation;
2. internal-history overlap check against prior repo branches;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable scorecard;
5. select at most one separate F01 candidate.

The candidate pool, rubric, tie-break and score dimensions may not be changed after revalidation evidence is observed.

## Non-claims / 비주장

R36 establishes no generator delay relationship, school closure risk, bank failure risk, hospital outcome relationship, causal effect, ranking, prediction, novelty, or commercial recommendation.

Incremental monetary cost must remain **0 USD**.
