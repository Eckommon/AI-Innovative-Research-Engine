---
id: CA-CORP-F01
type: outcome-blind-structural-feasibility
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R43
parent_decision: DEC-255
selected_candidate: CA-CORP-001
future_section212_membership_opened: false
incremental_monetary_cost_usd: 0
---

# CA-CORP-F01 — exact Corporation-ID structural gate before future section-212 non-compliance dissolution

## Mission / 목적

Determine, **before opening any post-baseline section-212 dissolution membership**, whether official Corporations Canada open data, federal-corporation API and monthly legal-transaction publications can support a deterministic corporation-level prospective design using exact source-native corporation identity.

F01 is structural only. It does not test whether governance, age, jurisdiction, directors, registered-office structure or any other historical characteristic predicts dissolution.

## Frozen legal population / 고정 모집단

The focal legal population is **Canada Business Corporations Act (CBCA)** corporations only.

Other acts and entity families—NFP Act, cooperatives, Boards of Trade, special-act corporations and other federal bodies—may be present in the official database but are excluded from the focal support counts and may not be pooled after observation.

## Frozen official source anchors / 공식 소스

### Federal corporation open data
- `https://ised-isde.canada.ca/site/corporations-canada/en/data-services`

The exact current official **Download a dataset** target resolved from this page after Issue binding is the frozen baseline corporation dataset. The body may be read only after Issue binding and must be fingerprinted.

### Federal Corporation API
- `https://ised-isde.canada.ca/site/corporations-canada/en/accessing-federal-corporation-json-datasets`

The API is used only for structural identity/schema concordance. No post-baseline dissolution membership may be discovered through status-specific future queries in F01.

### Monthly legal transactions
- `https://ised-isde.canada.ca/site/corporations-canada/en/data-services/monthly-transactions`
- historical monthly pages published on or before **2026-09-29**
- CBCA **Certificates of Dissolution – Section 212**
- CBCA **Certificates of Dissolution – Section 210 or 211**
- Certificates of Amalgamation
- Certificates of Discontinuance

Historical monthly transaction rows whose effective dates are **on or before 2026-08-31** may be opened in F01 solely for identity/cardinality/event-semantics support.

### Status semantics
- `https://ised-isde.canada.ca/site/corporations-canada/en/search-tips`

Official status semantics distinguish active, dissolved, inactive-amalgamated and inactive-discontinued states.

## Frozen corporation identity / 고정 식별자

Primary identity is the Corporations Canada **Corporation Number / corporationId**.

Allowed deterministic normalization is frozen before empirical row access:

1. convert the source value to text without numeric rounding;
2. trim leading/trailing ASCII whitespace;
3. if the value matches exactly `^[0-9]+-[0-9]$`, remove that single hyphen;
4. otherwise retain an all-digit value unchanged;
5. accept only a resulting nonblank decimal digit string of length **4 through 8**.

Prohibited:
- zero-padding;
- deleting any character other than the single hyphen in the exact pattern above;
- check-digit invention or repair;
- business-number substitution;
- name/address/director matching;
- fuzzy/geospatial/manual reconciliation.

The normalized token must equal the API `corporationId` representation when both are available.

## Frozen baseline / 고정 기준시점

The baseline is the official federal-corporation open-data dataset resolved and downloaded **after Issue binding on 2026-09-29**. Its exact URL, HTTP metadata and SHA-256 become the immutable baseline fingerprint.

F01 may inspect baseline rows only for:
- exact corporation identity;
- governing legislation;
- current legal status;
- incorporation/continuance and non-outcome structural fields;
- active-CBCA cardinality;
- API concordance.

F01 does not define a predictive exposure.

## Frozen future event window / 미래 event 창

A later descendant may identify a future event only from official Corporations Canada legal transactions with effective dates:

- **start:** 2026-09-30
- **end:** 2027-03-31 inclusive.

In F01:
- no monthly transaction entity row with effective date on or after 2026-09-30 may be opened, parsed, searched or cached;
- no baseline corporation may be classified as future dissolved/survived;
- future monthly index pages may receive metadata-only access only if no entity rows are consumed.

## Frozen event semantics / event 의미

Primary future event prospect is **CBCA section 212 dissolution for non-compliance**.

The descendant must keep separate:
- section 212 non-compliance dissolution;
- section 210/211 voluntary/corporation-initiated dissolution;
- amalgamation;
- discontinuance;
- NFP/cooperative/other-act dissolution;
- revival.

No generic `dissolved` status may substitute for section-212 event adjudication.

## Anti-tautology firewall / 순환성 방화벽

The following may **never** be used as historical exposure in descendants:

- annual-filing overdue flags or counts;
- notice of intent to dissolve membership/date;
- dissolution-pending status;
- active-intent-to-dissolve status;
- compliance-certificate ineligibility mechanically caused by overdue filings;
- any field directly encoding a section-212 trigger or pending dissolution.

F01 may document that these fields/statuses exist, but must not compute them as candidate predictors.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R43 selection `CA-CORP-001`, checkpoint `CHK-20260929-PORTFOLIO-R43-TERMINAL`, last decision `DEC-255` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official documentation access | data-services, API-documentation, monthly-transactions and search-tips anchors are reachable or officially redirected |
| 4 | Open-data baseline resolution | official data-services page resolves a zero-cost federal-corporation dataset body from a Government of Canada source |
| 5 | Baseline parseability/schema | baseline is machine-readable and exposes Corporation Number/corporationId, governing legislation, current legal status and at least one incorporation/continuance date concept |
| 6 | Exact ID syntax | ≥ **99.90%** of nonblank corporation identifiers qualify under the frozen normalization; invalid values are excluded, not repaired |
| 7 | Active CBCA support | ≥ **250,000** distinct qualified corporation IDs are CBCA and legally active at baseline |
| 8 | Independent identity support | ≥ **500,000** distinct qualified corporation IDs exist across the complete federal-corporation baseline |
| 9 | Status semantics | ≥ **99.90%** of nonblank focal CBCA status values map exactly to officially documented legal-status labels without inference |
| 10 | Historical monthly lineage | at least **18 distinct monthly transaction publication months** from 2025-01 through 2026-08 are officially accessible without opening any post-baseline future row |
| 11 | Historical section-212 support | ≥ **5,000** distinct qualified CBCA Corporation IDs appear in section-212 dissolution transactions with effective date ≤ 2026-08-31 |
| 12 | Historical event identity coverage | ≥ **95.00%** of qualified historical section-212 Corporation IDs exact-match a corporation in the baseline complete dataset under only the frozen normalization |
| 13 | Event-class separation | official transaction families/documentation separately identify section 212, section 210/211, amalgamation and discontinuance |
| 14 | API identity concordance | a deterministic pre-fixed sample of up to **100** baseline qualified IDs yields ≥ **99.00%** exact corporationId concordance where API responses are available; no name matching |
| 15 | Anti-tautology firewall | runner computes no overdue-filing, intent-to-dissolve, dissolution-pending or equivalent trigger exposure and records the prohibited-field list unchanged |
| 16 | Future source seal | post-2026-09-29 transaction entity rows opened = **0** and future section-212 membership opened = **false** |
| 17 | Outcome/identity firewall | future relationship/prediction/ranking/causal metric computed = **false**; business-number/name/address/director/fuzzy/geo/manual repair used = **false** |
| 18 | Reproducibility and cost | immutable JSON/Markdown records source URLs/metadata, baseline SHA-256, schema, counts, historical-month/event identities, API sample rule/results, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen API sample rule / API 표본 규칙

If Gate 14 is reached, sort all qualified baseline corporation IDs lexicographically and take the first **100**. Do not choose IDs based on status, dissolution history, API response availability or any outcome-related field.

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_READY`

Any valid empirical failure:

`HOLD_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. The legal population, identity normalization, minimum support, historical window, event hierarchy and future firewall may not be loosened after observation.

Transport/parser/official-host-migration defects may be corrected only when no scientific criterion changes and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `CA-CORP-N01` design.

N01 must freeze one non-tautological historical exposure, eligibility/exclusions, comparator/matching or stratification rules, future section-212 event adjudication, competing legal transitions, minimum event support and statistical gate **before** future section-212 membership is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that any corporate structure predicts or causes non-compliance dissolution; no credit score, corporate ranking, investment signal, regulatory recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
