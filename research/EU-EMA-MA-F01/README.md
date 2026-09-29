---
id: EU-EMA-MA-F01
type: outcome-blind-structural-feasibility
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R44
parent_decision: DEC-259
selected_candidate: EU-EMA-MA-001
future_withdrawal_suspension_membership_opened: false
incremental_monetary_cost_usd: 0
---

# EU-EMA-MA-F01 — exact EMA-product structural gate before future marketing-authorisation withdrawal/suspension

## Mission / 목적

Determine, **before opening any post-baseline withdrawal/suspension membership**, whether official European Medicines Agency public medicine data can support a deterministic human centrally-authorised-medicine prospective design using exact EMA product identity and source-native legal/status semantics.

F01 is structural only. It does not test whether therapeutic area, orphan/generic status, additional monitoring, authorisation age, holder identity or any other historical characteristic predicts withdrawal or suspension.

## Frozen population / 고정 모집단

The focal population is **human medicines in the EMA centralised procedure** only.

Veterinary medicines, withdrawn applications for initial authorisation, withdrawn variation/post-authorisation applications, refused applications, national-only authorisations and non-medicine documents may be inspected only to establish separation semantics and may not be pooled into focal support/event counts.

## Frozen official source anchors / 공식 소스

### Medicine data / JSON
- `https://www.ema.europa.eu/en/medicines/download-medicine-data`
- `https://www.ema.europa.eu/en/about-us/about-website/download-website-data-json-data-format`

EMA documents that centrally authorised medicine JSON/table data expose fields including:
- `category`
- `name_of_medicine`
- `ema_product_number`
- `medicine_status`
- `european_commission_decision_date`
- `medicine_url`
- revision/publication metadata.

After Issue binding, the runner may resolve and download the official current centrally-authorised-medicine table/JSON body identified from these pages and must fingerprint the exact body.

### Marketing-status / event semantics
- `https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/notifying-change-marketing-status`
- individual official EMA medicine/EPAR pages identified from the current medicine dataset.

Historical medicine pages/events dated on or before **2026-09-29** may be opened only for source/schema/event-semantics support.

## Frozen EMA product identity / 고정 식별자

Primary identity is exact source-native **EMA product number** for human centrally authorised medicines.

Allowed normalization:
1. convert source value to text;
2. trim leading/trailing ASCII whitespace;
3. uppercase ASCII letters;
4. retain slash separators unchanged;
5. accept only exact pattern `^EMEA/H/C/[0-9]{6}$`.

Prohibited:
- zero-padding;
- slash insertion/deletion;
- numeric-only reconstruction;
- medicine-name/holder/active-substance matching;
- fuzzy/manual/geospatial repair;
- procedure/reference-number substitution.

## Frozen baseline / 고정 기준시점

The baseline is the official centrally-authorised medicine dataset resolved and downloaded **after Issue binding on 2026-09-29**.

F01 may inspect baseline rows only for:
- exact product identity;
- human/veterinary category;
- current medicine status;
- European Commission decision date;
- medicine URL;
- non-outcome structural metadata.

F01 does not define a predictive exposure.

## Frozen future event window / 미래 event 창

A later descendant may identify a future event only from official EMA medicine/EPAR status changes dated:

- **start:** 2026-09-30
- **end:** 2027-03-31 inclusive.

In F01:
- no event row/page newly dated on or after 2026-09-30 may be used to classify future withdrawal/suspension membership;
- no baseline medicine may be classified as future withdrawn/suspended/survived;
- future pages may receive metadata-only requests only when no future event membership/content is consumed.

## Frozen event hierarchy / event 계층

Potential descendant event classes must remain separate:

1. **marketing-authorisation withdrawal after approval**;
2. **marketing-authorisation suspension**;
3. **expiry/non-renewal**;
4. **withdrawn initial marketing-authorisation application**;
5. **withdrawn variation/post-authorisation application**;
6. **refused application/opinion**.

For marketing-authorisation withdrawal after approval, a later descendant must also distinguish:
- voluntary/commercial/portfolio-holder withdrawal;
- safety/benefit-risk/regulatory withdrawal or suspension;
- unknown/other reason.

F01 may use historical pre-cutoff EPAR pages only to prove that these distinctions are source-defensible. It may not collapse them after observation.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R44 selection `EU-EMA-MA-001`, checkpoint `CHK-20260929-PORTFOLIO-R44-TERMINAL`, last decision `DEC-259` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official documentation access | medicine-data, website-JSON and marketing-status anchors are reachable or officially redirected |
| 4 | Baseline resolution | official EMA pages resolve a zero-cost centrally-authorised-medicine table or JSON entity body from an EMA-owned source |
| 5 | Baseline schema | focal dataset exposes category, medicine name, EMA product number, medicine status, European Commission decision date and medicine URL concepts |
| 6 | Exact ID syntax | ≥ **99.90%** of nonblank focal human EMA product numbers satisfy the exact frozen pattern; invalid values are excluded, not repaired |
| 7 | Human-medicine support | ≥ **1,000** distinct qualified human centrally-authorised EMA product numbers exist |
| 8 | Current authorised support | ≥ **750** distinct qualified human products have a source-native status representing an authorised/currently valid medicine at baseline |
| 9 | Decision-date support | ≥ **99.00%** of qualified focal human rows have a parseable nonblank European Commission decision/authorisation date |
| 10 | Medicine URL identity linkage | ≥ **99.00%** of qualified focal human IDs have a nonblank official EMA medicine URL associated with the same source row |
| 11 | Historical withdrawn-authorisation support | ≥ **25** distinct qualified human EMA product IDs can be identified from pre-2026-09-30 official EMA pages as **marketing authorisation withdrawn after approval**, not merely application/variation withdrawal |
| 12 | Historical event-date support | ≥ **95.00%** of those historical withdrawn-authorisation products expose both an authorisation-issued date and a withdrawal-of-marketing-authorisation date with withdrawal date not earlier than authorisation date |
| 13 | Withdrawal reason support | ≥ **90.00%** of those historical withdrawn-authorisation products expose source-native/public reason text sufficient to classify at least voluntary/commercial vs safety/regulatory vs unknown/other without holder/name inference |
| 14 | Event-class separation | official source structure/documentation separately identifies marketing-authorisation withdrawal, suspension, expiry/non-renewal, initial-application withdrawal and variation/post-authorisation-application withdrawal |
| 15 | Historical identity concordance | ≥ **95.00%** of historical withdrawn-authorisation EMA product IDs exact-match a qualified product ID in the baseline dataset under only the frozen identity rule |
| 16 | Future source seal | post-2026-09-29 future event membership opened = **false** and future entity rows/pages consumed for membership = **0** |
| 17 | Outcome/identity firewall | relationship/prediction/ranking/causal metric computed = **false**; medicine-name/holder/substance/fuzzy/manual identity repair used = **false** |
| 18 | Reproducibility and cost | immutable JSON/Markdown records final URLs/metadata, baseline SHA-256, schema/counts, historical event IDs/date/reason support, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen historical-event discovery rule / historical event 탐색 규칙

Historical event support may use only EMA-owned pages discoverable from:
- the official focal medicine dataset;
- official EMA medicine search/category/status surfaces;
- official EMA marketing-status pages.

The runner may not use a search-engine result list, Wikipedia, commercial pharmaceutical databases or hand-curated external lists as the historical event cohort.

If the official EMA source architecture cannot enumerate at least 25 historical withdrawn-authorisation products without external/manual discovery, Gate 11 fails.

## Frozen reason classification / reason 분류

Reason classes are semantic only and must be supported by source-native/public EMA wording:

- `VOLUNTARY_COMMERCIAL`: holder request, commercial reasons, permanent discontinuation/portfolio reasons;
- `SAFETY_REGULATORY`: explicit safety, benefit-risk, regulatory non-compliance or authority-initiated suspension/withdrawal;
- `OTHER_UNKNOWN`: source reason present but not defensibly assignable to the first two.

No medicine-specific outcome may be used to change the class definitions after execution.

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_READY`

Any valid empirical failure:

`HOLD_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. The population, product-ID rule, minimum support, historical-event threshold, event hierarchy and future firewall may not be loosened after observation.

Transport/parser/official-host-migration defects may be corrected only when no scientific criterion changes and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `EU-EMA-MA-N01` design.

N01 must freeze one non-tautological historical exposure, eligibility/exclusions, comparator/matching or stratification rules, future event hierarchy, competing event handling, minimum event support and statistical gate **before** future withdrawal/suspension membership is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that any medicine characteristic predicts or causes withdrawal/suspension; no prescribing recommendation, safety signal, medicine ranking, investment signal, regulatory recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
