---
id: US-IRS-EO-F01
type: outcome-blind-structural-feasibility
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R39
selection: US-IRS-EO-001
future_outcome_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-IRS-EO-F01 — Form 990 exact-EIN structural gate before automatic-revocation outcomes

## Mission / 목적

Determine, **before opening any future Automatic Revocation List membership**, whether official IRS public disclosure sources can support a later prospective organization-level experiment linking historical filed Form-990-series structure to a subsequent direct IRS automatic-revocation event using exact source-native EIN only.

This is a structural/source/cardinality gate, not an association test. No organization is classified as future revoked/not-revoked in F01.

## Frozen source families / 고정 소스

### Historical exposure-side data that F01 may read

Only the official Form 990-series **index CSVs for posting years 2022, 2023 and 2024** may be downloaded and parsed in the empirical gate:

- `https://apps.irs.gov/pub/epostcard/990/xml/2022/index_2022.csv`
- `https://apps.irs.gov/pub/epostcard/990/xml/2023/index_2023.csv`
- `https://apps.irs.gov/pub/epostcard/990/xml/2024/index_2024.csv`

Official source/documentation anchors:

- `https://www.irs.gov/charities-non-profits/form-990-series-downloads`
- `https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-teos-faqs`
- `https://www.irs.gov/charities-non-profits/copies-of-eo-returns-available`
- `https://www.irs.gov/e-file-providers/current-valid-xml-schemas-and-business-rules-for-exempt-organizations-and-other-tax-exempt-entities-modernized-e-file`

F01 may inspect the download-page HTML, FAQ text and schema-page metadata. It may issue body-free `HEAD` requests to listed XML ZIP bundles. It may **not** download bulk XML ZIP payloads in F01; that belongs only to a later outcome-blind exposure-design step if F01 passes.

### Outcome-side source that remains sealed

Official automatic-revocation documentation/schema may be read:

- `https://www.irs.gov/charities-non-profits/automatic-revocation-of-exemption`
- `https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads`
- `https://www.irs.gov/pub/irs-tege/auto-revocation-data-dictionary.pdf`

The bulk outcome endpoint is frozen as:

- `https://apps.irs.gov/pub/epostcard/data-download-revocation.zip`

F01 may issue **only a body-free `HEAD` request** to that ZIP. It may not use `GET`, Range GET, unzip, stream, cache, preview, grep, count or otherwise inspect any automatic-revocation data row.

`future_outcome_rows_opened` must equal exactly **0**.

## Frozen identity semantics / 식별자 규칙

- Historical filed-return identity: index `EIN`, normalized only by trim + removal of an optional display hyphen and left-preservation as a 9-character digit string. Numeric coercion is prohibited because leading zeroes must survive.
- Outcome identity prospect: Automatic Revocation data-dictionary `TIN`, documented as a 9-character Taxpayer Identification Number. A later experiment may join only by exact normalized 9-digit `EIN == TIN`.
- No organization name, DBA/sort name, address, ZIP, state, geocoding, fuzzy match, manual repair or external identifier crosswalk is permitted.
- `OBJECT_ID` is a filing/document locator, **not** organization identity.
- Multiple returns for the same EIN are permitted historically; F01 does not choose a financial exposure or deduplicate to an organization-year analytical row.

## Frozen anti-tautology boundary / 순환성 방지

Automatic revocation is statutorily triggered by failure to file a required annual return/notice for three consecutive years. Therefore the following are permanently prohibited as candidate exposure variables in the descendant hypothesis:

- count/streak of missed filings;
- years since last filing when mechanically equivalent to a missed-filing streak;
- Form 990-N/990-series nonfiling flags that encode the statutory trigger;
- any feature derived from observed future revocation membership.

A later outcome-blind N01, if authorized, must select substantive operational/financial/governance information from returns that were actually filed.

## Frozen temporal firewall / 시간 방화벽

- F01 empirical rows: Form-990 index posting years **2022–2024 only**.
- 2025 and 2026 Form-990 index rows are not needed and must not be read by F01.
- No Automatic Revocation List row of any date may be read by F01.
- Documentation may describe revocation effective/posting/reinstatement dates without exposing row membership.
- The known IRS 2020 COVID filing-extension revocation-date anomaly must be recorded as a future adjudication caveat; F01 does not open those rows and does not correct any observed event.

## Immutable 18-gate contract / 불변 18개 gate

All gates are frozen **before Issue creation and before historical index row access**. A valid empirical failure is a scientific `HOLD_US_IRS_EO_F01_*`; thresholds may not be relaxed after observing counts. A transport/parser/implementation defect before a valid gate result may be corrected separately without changing this contract or overwriting the first attempt.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | live canonical state is `PORTFOLIO_R39_SELECTED_US_IRS_EO_001__F01_CONTRACT_REQUIRED`, checkpoint `CHK-20260918-PORTFOLIO-R39-TERMINAL`, last decision `DEC-236` |
| 2 | Issue binding | empirical runner may execute only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official historical source | all three frozen 2022–2024 index URLs resolve from `apps.irs.gov` over HTTPS and return parseable CSV bodies |
| 4 | Frozen index schema | each index exposes, case/spacing-normalized, the documented concepts `Return ID`, `Filing Type`, `EIN`, `Tax Period`, `Submission Date`, `Taxpayer Name`, `DLN`, `Object ID` |
| 5 | Exact EIN syntax | ≥99.90% of nonblank historical index EIN values normalize to exactly 9 digits; blank/invalid values are not repaired |
| 6 | Historical filing support | combined 2022–2024 index rows ≥ **500,000** |
| 7 | Independent organization support | distinct valid exact EINs across 2022–2024 ≥ **150,000** |
| 8 | Longitudinal filed-organization support | ≥ **75,000** distinct valid EINs occur in at least two of the three frozen posting-year indexes |
| 9 | Tax-period parseability | ≥99.00% of rows with valid EIN have a nonblank tax period that can be normalized without inference to a 6-digit `YYYYMM` or 4-digit `YYYY` source representation |
| 10 | Filing locator integrity | ≥99.90% of rows with valid EIN have nonblank Object ID; duplicated nonblank Object IDs across the combined indexes ≤0.10% of such rows |
| 11 | Submission chronology | ≥99.00% of rows with valid EIN have a parseable documented Submission Date; runner records min/max dates by posting-year index without opening later indexes |
| 12 | Source-family availability | IRS official download page documents Form 990-series XML access and public index files for each frozen posting year, and at least one listed 2024 XML ZIP endpoint accepts a body-free `HEAD` request |
| 13 | Return-family structural availability | official IRS documentation/schema pages explicitly cover the Form 990 family including 990, 990-EZ and 990-PF; F01 does not infer family from names or download XML payloads |
| 14 | Exact outcome identity semantics | official IRS Automatic Revocation documentation/data dictionary documents 9-character TIN/EIN plus revocation effective date and posting date, with reinstatement semantics separately documented |
| 15 | Direct-event semantics | official IRS documentation states automatic revocation follows three consecutive missed required annual filings and is effective on the original due date of the third missed return/notice |
| 16 | Sealed outcome endpoint | frozen automatic-revocation ZIP endpoint accepts body-free `HEAD` (or a method-equivalent metadata-only request that returns no entity body); response body bytes consumed = **0** |
| 17 | Outcome/tautology firewall | automatic-revocation data rows opened = **0**; 2025/2026 Form-990 index rows opened = **0**; nonfiling/missed-filing streak exposure variables constructed = **0**; no name/address repair used |
| 18 | Reproducibility and cost | immutable JSON/Markdown evidence records exact URLs, HTTP metadata, row/cardinality counts, normalized schema names, SHA-256 of the three historical index bodies, contract SHA, runner SHA and `incremental_monetary_cost_usd = 0` |

## Frozen terminal rule / 종결 규칙

`PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY` requires **18/18 PASS**.

Any valid gate failure produces terminal scientific HOLD with the failed gate numbers named. No post-observation threshold reduction, posting-year substitution, alternate identifier, fuzzy match, third-party mirror, paid service, 2025/2026 historical supplementation, or future-outcome inspection is allowed to rescue the design.

A PASS authorizes only a **separate outcome-blind N01 design**. It does not authorize opening the Automatic Revocation List rows yet. N01 must prospectively define the filed-return cohort, substantive non-tautological exposure, return-amendment/deduplication policy, temporal risk window, reinstatement handling and future outcome adjudication before any event membership is opened.

## Non-claims / 비주장

F01 makes no claim that financial weakness, governance characteristics, revenue concentration, organization size or any other filed-return feature predicts or causes automatic revocation. It creates no organization ranking, probability, compliance recommendation or novelty claim.

Incremental monetary cost must remain **0 USD**.
