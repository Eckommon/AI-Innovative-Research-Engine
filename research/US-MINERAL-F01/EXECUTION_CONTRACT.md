---
id: US-MINERAL-F01-EXECUTION-CONTRACT
type: source-semantic-execution-contract
created: 2026-09-04
trade_rows_opened: false
outcome_concentration_computed: false
incremental_monetary_cost_usd: 0
---

# US-MINERAL-F01 Census Execution Contract / Census 실행 계약

## 1. Frozen period / 고정 기간

- Primary bounded period: **2023-01 through 2023-12**.
- Rationale: USGS OFR 2025-1047 states the underlying assessment used year 2023 data unless otherwise noted; F01 therefore fixes the Census public-file compatibility test to the same statistical year.
- This gate does not open any `IMP_DETL` or port trade rows. Only documentation bytes and HTTP HEAD metadata are read.

## 2. Official static-file availability / 공식 정적 파일 존재성

- 2023 Merchandise Trade Imports monthly ZIPs available for all 12 months: **YES**
- 2023 Port Imports HS6 monthly ZIPs available for all 12 months: **YES**

### Merchandise / `IMP_DETL` carrier ZIPs

| Month | HEAD | Content-Type | URL |
|---|---:|---|---|
| 2023-01 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2301.ZIP` |
| 2023-02 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2302.ZIP` |
| 2023-03 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2303.ZIP` |
| 2023-04 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2304.ZIP` |
| 2023-05 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2305.ZIP` |
| 2023-06 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2306.ZIP` |
| 2023-07 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2307.ZIP` |
| 2023-08 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2308.ZIP` |
| 2023-09 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2309.ZIP` |
| 2023-10 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2310.ZIP` |
| 2023-11 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2311.ZIP` |
| 2023-12 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Merch/im_m/IMDB2312.ZIP` |

### Port HS6 carrier ZIPs

| Month | HEAD | Content-Type | URL |
|---|---:|---|---|
| 2023-01 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2301.ZIP` |
| 2023-02 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2302.ZIP` |
| 2023-03 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2303.ZIP` |
| 2023-04 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2304.ZIP` |
| 2023-05 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2305.ZIP` |
| 2023-06 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2306.ZIP` |
| 2023-07 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2307.ZIP` |
| 2023-08 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2308.ZIP` |
| 2023-09 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2309.ZIP` |
| 2023-10 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2310.ZIP` |
| 2023-11 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2311.ZIP` |
| 2023-12 | 200 | application/zip | `https://www.census.gov/trade/downloads/2023/Port/im_hs6_m/PORTHS6MM2312.ZIP` |

## 3. Frozen parse and identity rules / 파싱·식별 규칙

- Parse Census fixed-width files strictly according to the official record layout; do not infer columns from whitespace.
- `IMP_DETL` raw identity key is frozen as: `commodity × cty_code × cty_subco × dist_entry × dist_unlad × rate_prov × year × month`.
- The research aggregation key is: `mineral × cty_code × dist_entry × dist_unlad × year × month` after the frozen USGS→HTS mapping is applied.
- `cty_subco` and `rate_prov` are tariff/reporting dimensions, not separate mineral/source-country/node identities; sum them only after validating the raw full key.
- A repeated raw full identity key is **fail-closed**: do not silently deduplicate or sum duplicates. Stop that file/month and inspect source integrity before any outcome metric.
- Use monthly (`*_mo`) fields only for monthly analysis; never sum YTD (`*_yr`) fields across months.
- Primary concentration weight is `gen_val_mo` (General Imports, Total Value). This matches the Port HS6 file `value_mo`, which is also General Imports, Total Value.
- `cards_mo` is a support/count diagnostic only; it is not a concentration weight.

## 4. Quantity, mode and suppression rules / 수량·운송·억제 규칙

- Quantity units are code-specific and come from the official Census concordance (`unit_qy1`, `unit_qy2`). Do not sum heterogeneous quantity units across HTS codes unless an explicit common-unit conversion is separately preregistered.
- Core concentration therefore uses published value, not quantity or shipping weight.
- Blank, suppressed or otherwise unavailable quantity/shipping-weight fields are **not imputed**. They remain unavailable and may only affect quantity/weight diagnostics, not the value-based core metric.
- Census disclosure rules can suppress quantity/shipping weight and can combine/alter district/port presentation. Preserve official published district/port codes exactly; do not manually disaggregate, reallocate, or reverse-engineer suppressed geography.
- `air_val_mo` and `ves_val_mo` are mutually exclusive mode components of general-import value for air and vessel. `cnt_val_mo` is a subset of vessel value, not a third additive mode.
- If a later mode decomposition is used, define `other_value = gen_val_mo - air_val_mo - ves_val_mo`; containerized vessel remains a vessel subcategory. Negative residuals or parse inconsistencies are fail-closed diagnostics.
- Actual-port HS6 outputs, if used, must be labeled **published port-of-unlading statistics** rather than transaction-level physical routing truth because Census disclosure protection can affect port presentation.

## 5. Null and code-validity rules / 결측·코드 유효성 규칙

- Mandatory research keys (`commodity`, `cty_code`, `dist_entry`, `dist_unlad`, `year`, `month`) and primary weight `gen_val_mo` must parse successfully. A malformed/blank mandatory key or primary value is fail-closed for that source month.
- Zero is a valid published numeric value and is not converted to null.
- Official special/combined district or country designations are retained as published if they are valid reference codes; they are not reassigned to a guessed geography.
- Only HTS10 codes in the frozen 2023 Census concordance and in `MAPPING_IDENTIFIABILITY.md` are eligible for the primary `IMP_DETL` experiment.

## 6. Revision and snapshot policy / 개정·스냅샷 정책

- Census merchandise statistics are revised; therefore **the experiment uses one contemporaneous official 2023 snapshot**, not an assumed first-release 2023 vintage.
- At the first outcome-bearing execution, download all 12 official 2023 monthly ZIPs in one run and record for each: URL, access timestamp, HTTP metadata, ZIP SHA-256, member filename(s), member byte size and member SHA-256.
- Persist that manifest before computing concentration outputs. Never silently replace a file if Census later changes it; a changed hash creates a new source snapshot/version.
- For reproducibility, all primary 2023 metrics must come from one manifest version. Mixing files from different snapshot manifests is prohibited.
- Any Census statistical correction notice relevant to 2023 that changes a frozen file must be recorded as a new snapshot, not patched manually.

## 7. Documentation snapshots / 문서 스냅샷

- IMP_DETL layout: HTTP `200`, SHA-256 `01b6b67130b64e6513b70e1ed4f9898b83f059b51a22a942e761f40b76c86260`, URL `https://www.census.gov/foreign-trade/reference/products/layouts/imdb.html`
- Port HS6 layout: HTTP `200`, SHA-256 `7abeb4184d7c3c83319f380ee40335802b0b8ec7be43ae273bbf5a30c8ad1e1c`, URL `https://www.census.gov/foreign-trade/reference/products/layouts/dporths6i.html`
- Revision procedure: HTTP `200`, SHA-256 `ff360d80938f9026e13f6dc71c21380728f0b39469658a5a1818a5131a223e7b`, URL `https://www.census.gov/foreign-trade/guide/revisions.html`
- Trade statistical guide: HTTP `200`, SHA-256 `17bd40c019edd0f84470688a6d0272416f710db791b53443ef60ac2eff337aff`, URL `https://www.census.gov/foreign-trade/guide/sec2.html`

## 8. Final contract preflight / 최종 계약 사전검증

- all 12 `IMP_DETL` carrier months reachable: **PASS**
- all 12 Port HS6 carrier months reachable: **PASS**
- duplicate/revision/suppression/null/quantity-unit rules: **FROZEN**
- bounded period and snapshot/hash plan: **FROZEN**

**`EXECUTION_CONTRACT_READY_FOR_F01_FINAL_GATE`**

Incremental monetary cost remained **0 USD**. No paid source, API credential, dashboard scraping, larger runner, or commercial trade database was used.
