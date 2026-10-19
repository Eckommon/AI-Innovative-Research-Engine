---
id: SOURCE-QUAL-FEMA-EPA-Q02
type: independent-prospective-source-product-qualification
parent_issue: 244
created: 2026-10-19
base_commit: d9651b8f5aa8f9d42cc900ba525d27ac27269ad9
status: FROZEN_BEFORE_NEW_EPA_PRODUCT_BODY_ACCESS
original_q01_disposition: HOLD_SOURCE_ACCESS_OR_SCHEMA
science_f01_authorized: false
incremental_monetary_cost_usd: 0
---

# Q02 — FEMA×EPA distinct annual concentration by monitor / 별도 제품 원천 스키마 검증

**No Q01 rescue / Q01 불변:** `FEMA-EPA-Q01` remains terminal `HOLD_SOURCE_ACCESS_OR_SCHEMA` for *county AQI* header. Q02 is a different product with its own prospective contract and independent immutable evidence; Q01 original contract, SHA, result, grades and scientific route cannot be revised.

## First-party source-product basis / 출처별 제품확인
- Existing immutable FEMA D2 original receipt (reuse, do not re-download): `research/SOURCE-REGISTRY-S01/qualifications/FEMA-EPA-Q01/evidence/source-qualification-01.json`, FEMA DisasterDeclarationsSummaries V2 first-party `https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv`; `fipsStateCode` + `fipsCountyCode`. Original full-body SHA `0c51c72b0fd4f616afeb01bb1f7e95f6b7f1349832f7b3be9d12e7dd7e5aaa30`. This is a source receipt, **not** a validated county join.
- **Different EPA product** official AirData 2024 *Concentration by Monitor*, specifically listed as `annual_conc_by_monitor_2024.zip`: `https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_2024.zip` ([official download](https://aqs.epa.gov/aqsweb/airdata/download_files.html); [Annual Summary FileFormats](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html#4)). The documented *monitor-level* schema contains `State Code`, `County Code`, `Site Num`, `Parameter Code`, `Year`, `Pollutant Standard`, `Event Type`. The actual specific ZIP CSV first header remains **UNVERIFIED** until this prospective probe. Do **not** infer those fields from the failed AQI product.

## Fixed qualification / 사전검증 10 gates
1. Confirm original Q01 terminal Result and original immutable FEMA receipt SHA and header status from committed GitHub only. No re-opening Q01, no raw FEMA download.
2. Exactly one no-redirect, HTTPS GET for **only** the frozen EPA concentration product, with max 16 MiB entire ZIP, timeout 55 seconds, no mirror, login or API key. Zero-cost public standard Actions.
3. Record exact EPA bytes/SHA-256, UTC, HTTP status, content type, ETag and Last-Modified separately from product vintage and first publication. Never store the ZIP or rows.
4. ZIP magic, non-encrypted single safe CSV member named exactly `annual_conc_by_monitor_2024.csv`; read **only the first header** capped at 16 KiB and hash it.
5. Verify **all seven literal EPA header fields** listed above; any missing field = `HOLD_SOURCE_ACCESS_OR_SCHEMA_Q02` and no guessing/alias rescue.
6. Show `FEMA county grain` versus `EPA monitor×parameter×sample duration×standard×event-type grain` explicitly. Shared county FIPS labels alone do **not** verify join cardinality, temporal compatibility, uniqueness or actual support.
7. No EPA monitor case row, county support counts, disaster/AQI/PM concentrations, association, regression, natural experiment or causal claim. No future CMS source or rows.
8. One new immutable Q02 JSON/MD with validated D2 individual-source evidence only (if successful), `DUAL_D2_SOURCE_HEADERS_ONLY` at most for the pair; **never D3**, F01 authorized false, independent S01 registry unchanged.
9. One free one-shot run after this contract is merged before any Q02 source-body GET. Offline synthetic boundary tests before source GET. A failure is HOLD; do not retry with renamed fields, other files or redirect.
10. Track A E01 Issue #203 / `DEC-318` remains authoritative, secondary Issue #244 only, no third Issue or R60, no paid spend. F01 first requires a *separate prospective structural plan* for 2024 pairing, monitor multiplicity, special FEMA county codes and nonrandom EPA coverage.

**Possible verdicts / 결과:** `DUAL_D2_SOURCE_HEADERS_ONLY_Q02`, `HOLD_SOURCE_ACCESS_OR_SCHEMA_Q02`, `HOLD_SOURCE_TRANSPORT_Q02`. No scientific hypothesis or outcome revealed.

**Cost ceiling:** strictly 0 USD.
