---
id: PORTFOLIO-R40
type: stage0-cross-domain-reselection
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-IRS-EO-N01
parent_disposition: HOLD_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_NOT_IDENTIFIABLE
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R40 — independent cross-domain reselection after IRS-EO N01 Gate-5 HOLD

## Mission / 목적

Select exactly one next **outcome-blind F01** after `US-IRS-EO-N01` terminated at its prospectively frozen deterministic-schema-mapping Gate 5. R40 must not rescue the IRS branch by deleting the application-pending exclusion, treating schema absence as false, changing the historical year, admitting 990-EZ/990-PF, using a proxy, or opening Automatic Revocation membership.

R40 deliberately moves to four different unit/event families: SEC public issuers, FMCSA motor carriers, FCC wireless licenses, and NCES public schools. No candidate exposure→outcome relationship, effect, prediction, ranking or causal claim may be computed during portfolio selection.

Pre-contract source discovery may establish source/identifier/event semantics from official documentation and public examples. After this contract commit, candidate future-event membership may not be opened to score or break a tie.

## Frozen candidates / 고정 후보

### 1. `US-SEC-ISSUER-001` — issuer financial/filing structure → subsequent Form 25-NSE listing-registration removal

**Question:** Can SEC EDGAR submissions/XBRL and later Form 25-NSE events support a prospectively separated issuer-level design using exact subject CIK, without name/ticker reconciliation?

- prospective historical exposure family: issuer financial and filing structure available in EDGAR submissions and SEC XBRL company facts;
- future event family: later Form 25-NSE notification removing a security from exchange listing/registration, under a separately preregistered event-reason/adjudication rule;
- source-native identity prospect: exact zero-padded 10-digit issuer/subject `CIK`;
- known risk: Form 25 is filed by an exchange while the issuer appears as the subject; maturity, redemption, merger and other routine removals may make an undifferentiated Form-25 endpoint economically ambiguous;
- practical value: public-market continuity and listing-transition bottlenecks;
- F01 only: prove exact subject-CIK semantics, historical API/bulk lineage, direct event/date/reason fields, sufficient independent issuers, and a sealed future-event firewall.

No issuer distress label, delisting probability, investment recommendation, trading signal, ranking, causal claim or novelty claim is authorized.

### 2. `US-FMCSA-CARRIER-001` — carrier operating/fleet structure → subsequent FMCSA out-of-service order

**Question:** Can FMCSA public census/history sources and official Out-of-Service order records support a prospective carrier-level design using exact USDOT Number while keeping safety-audit/violation trigger information out of the historical exposure?

- prospective historical exposure family: non-outcome carrier census/operating structure such as operation type, fleet/equipment and driver structure, under a later F01-frozen historical snapshot rule;
- future event family: later direct FMCSA Out-of-Service order, with reason/date/status adjudicated prospectively;
- source-native identity prospect: exact `USDOT Number`;
- anti-tautology boundary: prior OOS orders, safety-audit failure/refusal, roadside violation/OOS metrics, and any field mechanically encoding the later OOS trigger may not be used as exposure;
- known risk: current carrier census is updated continuously and FMCSA systems are being modernized, so reproducible historical snapshot lineage is a first-order F01 risk;
- practical value: carrier operating-continuity and regulatory-transition bottlenecks;
- F01 only: prove USDOT identity continuity, historical snapshot availability, event semantics, anti-tautology separation, support/cardinality and sealed future membership.

No carrier safety score, enforcement targeting, OOS probability, routing recommendation, ranking, causal claim or novelty claim is authorized.

### 3. `US-FCC-ULS-001` — wireless-license structure → subsequent cancellation/termination

**Question:** Can FCC Universal Licensing System public-access files support a license-level prospective design using the source-native unique 9-digit system identifier, with historical license/application structure separated from a later cancelled/terminated license action?

- prospective historical exposure family: license/service/application structure and non-outcome technical/administrative characteristics from official ULS public-access files;
- future event family: later license cancellation or termination under a prospectively fixed ULS status/action hierarchy;
- source-native identity prospect: FCC-assigned unique **9-digit system identifier**, not licensee name and not a reassigned call sign;
- known strength: FCC documentation states the identifier distinguishes an active call sign from an expired, cancelled or terminated prior license when call signs are reassigned;
- known limitation: exposure and outcome largely live inside the same ULS ecosystem, reducing cross-system information gain; service-specific cancellation mechanisms may require stratification;
- practical value: spectrum-use continuity and licensing-friction bottlenecks;
- F01 only: prove exact system-ID lineage, historical complete/daily transaction-file availability, status/action semantics, service-family comparability, cardinality and future-event sealing.

No spectrum-license risk score, licensee ranking, regulatory recommendation, causal claim or novelty claim is authorized.

### 4. `US-NCES-SCHOOL-001` — public-school enrollment/staffing structure → subsequent school closure

**Question:** Can annual NCES Common Core of Data school-universe files support a prospectively separated public-school design using exact NCES School ID, with historical enrollment/staffing structure linked to a later explicit closed operational status?

- prospective historical exposure family: annual school enrollment composition, teacher FTE and structural attributes from CCD school-universe files;
- future event family: later CCD school operational status explicitly coded as closed, with temporary closure/reopening/agency-change states handled only under a preregistered hierarchy;
- source-native identity prospect: exact 12-digit NCES School ID;
- known limitation: school closure/enrollment decline is a mature education-policy research topic and the outcome is inside the same annual CCD system; novelty credit must therefore be conservative;
- practical value: local education-capacity continuity;
- F01 only: prove exact School-ID continuity, annual snapshot lineage, status-code semantics, adequate longitudinal support, temporary/agency-change adjudication and sealed future status.

This is distinct from R36 `US-EDU-FIN-001`, which concerned higher-education IPEDS/College-Scorecard institutions and exact `UNITID`; nevertheless overlap with generic institution-closure work must be penalized conservatively.

No school closure probability, school/district ranking, funding recommendation, causal claim or novelty claim is authorized.

## Frozen official source anchors / 공식 소스 앵커

These anchors establish source families only and do **not** authorize post-contract candidate event-row access during portfolio scoring.

### SEC issuer
- SEC EDGAR APIs: `https://www.sec.gov/search-filings/edgar-application-programming-interfaces`
- SEC developer resources / EDGAR archive access: `https://www.sec.gov/about/developer-resources`
- SEC forms / filer manual: `https://www.sec.gov/submit-filings`

### FMCSA carrier
- FMCSA Open Data Program: `https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program`
- FMCSA SAFER / company safety records: `https://www.fmcsa.dot.gov/safety/company-safety-records`
- FMCSA Licensing & Insurance OOS interface: `https://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search`

### FCC ULS
- FCC ULS public-access-file guide: `https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf`
- FCC ULS database downloads / daily transactions: `https://www.fcc.gov/wireless/data/public-access-files-database-downloads`

### NCES CCD
- NCES CCD public school universe: `https://nces.ed.gov/ccd/pubschuniv.asp`
- NCES CCD school-universe information/status semantics: `https://nces.ed.gov/ccd/psuinfo.asp`
- NCES CCD files: `https://nces.ed.gov/ccd/files.asp`

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

Dimension 7 is the first interpretive priority. Exact official identity must survive the proposed historical/future source boundary without name, address, ticker, call-sign-only, fuzzy, geospatial or manual reconciliation.

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:

1. source-native/deterministic join defensibility;
2. next-gate information gain;
3. low overlap / novelty risk;
4. direct future-event quality;
5. independent-unit prospect;
6. zero-cost operability;
7. cross-dataset information gain.

If still tied, make no selection until an outcome-blind source/literature discriminator is documented. Candidate future-event rows may not be opened to break a tie.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:

1. official source/schema/current-access revalidation;
2. internal-history overlap check against canonical terminal/near-miss branches;
3. bounded external literature/agency-framework overlap check;
4. exactly one immutable `/45` scorecard;
5. select at most one separate outcome-blind F01.

Candidate identities, exposure/event families, rubric, score dimensions and tie-break may not change after this commit.

## Frozen exclusions / 고정 제외

- `US-IRS-EO-001` and descendants: immediate rescue prohibited; Automatic Revocation membership remains sealed.
- R39 held candidates `US-DOL-5500-001`, `US-FEMA-BPS-001`, and `US-BLS-CBP-001` are not re-entered.
- `US-FDIC-BRANCH-001` and descendants remain non-rescuable.
- R38 near-misses `US-FRA-XING-001`, `US-FCC-BDC-001`, `US-CMS-DIALYSIS-001` are not re-entered. `US-FCC-ULS-001` is a distinct license-level ULS identity/event family and must not import BDC withdrawal logic.
- R37 near-misses `US-FSIS-SAMPLE-001`, `US-USASPEND-VENDOR-001`, `US-EPA-SDWIS-001`, `US-CMS-NH-001` are not re-entered.
- R36 near-misses `US-EIA-GEN-001`, `US-EDU-FIN-001`, `US-FDIC-BANK-001`, `US-CMS-HOSP-001` are not re-entered. `US-NCES-SCHOOL-001` is K-12 school-level CCD, not higher-education UNITID/IPEDS, but receives conservative overlap treatment.
- R35/R34 terminal or near-miss families (FAA-AIP, DWSRF, PHMSA, NRC, EPA-XMEDIA, BTS-Port, USCG-Vessel, MSHA) are not rescued.
- USPTO maintenance remains excluded because anonymous zero-cost operational access is not sufficiently stable.

## Non-claims / 비주장

R40 establishes no issuer delisting relationship, carrier OOS relationship, spectrum-license termination relationship, school-closure relationship, prediction, ranking, causal effect, novelty claim, investment/regulatory/education recommendation or commercial action.

Incremental monetary cost must remain **0 USD**.
