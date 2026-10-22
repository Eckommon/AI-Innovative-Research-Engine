---
id: SOURCE-QUAL-CENSUS-USDA-Q07
created: 2026-10-23
parent_issue: 244
base_commit: 93df7e53dff906046e5707508cfc39f2887c98d6
frozen_before_source_first_get: true
qualification_kind: 2023-census-county-gazetteer-first-party-byte-and-header-only
scientific_f01_authorized: false
cost_usd: 0
---

# Q07 — Census 2023 County Gazetteer D2 source/identity-header provenance / USDA×Census 2023년 지리기준 원본 사전등록

**Why / 필요성:** Q04 verified 2024 Census national county Gazetteer and USDA 2023 RUCC first-party bytes/headers; Q05 validated the string-key overlap; Q06 explained all 13 scope mismatches as four Island Areas excluded from 2024 Census. All Q04–Q06 results remain terminal/immutable and **none** proves the remaining 3,222 geography boundaries are identical between 2023 and 2024. Before Q08 geography key/vintage reasoning, obtain an **independently published 2023 Census county Gazetteer** as a geographically matched publication-year reference. This is a **new source/header D2 operation only**, not an automatic F01/R60, nor a Q06 correction.

## Prospectively frozen official first-party source and methods / 선행 출처

1. Official Census `2023 Gazetteer Files` catalog, counties heading, single national county Gazetteer link: `https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2023.html`.
2. **Exact new Census 2023 original ZIP URL** (link target as posted on the official 2023 catalog): `https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2023_Gazetteer/2023_Gaz_counties_national.zip`. One **no-redirect** HTTP GET; status 200 required, maximum **2 MiB**, 40s timeout, no retry/fallback/mirror or vendor.
3. The two previously frozen and *not reaccessed in Q07* reference source receipts: Census 2024 `2024_Gaz_counties_national.zip` 141,679 B SHA `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`; USDA ERS 2023 long-format RUCC CSV 629,322 B SHA `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`. These are **prior verified metadata**, not re-downloaded/decoded. Require current Q06 evidence canonical and no re-interpretation.
4. Official [Census 2024 Gazetteer](https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2024.html) warns 2013–2023 county units and codes need not have one-to-one relationships with 2024 geography. [Census county changes](https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.html) defines Jan 1 reference year and Connecticut adoption of planning regions. USDA [2023 RUCC documentation](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation) acknowledges 2022 Connecticut change and 9 Virginia independent cities coded with surrounding counties; neither source establishes county border equivalence in the target pair.

## Bounded Q07 source-byte/header-only operation / 허용 접근

- Before opening ZIP, hash **full original compressed bytes** SHA-256, byte count, observed UTC, HTTP response type, ETag/Last-Modified when available. No publication date inferred from HTTP metadata.
- ZIP magic exact; exactly **one** safe nonencrypted top-level regular CSV/TXT member with frozen expected member filename **`2023_Gaz_counties_national.txt`**, size strictly between 0 and **4 MiB** uncompressed. If member shape/name differs, HOLD; no rename/repair. Decompress/read **only the first tab-delimited header line** (max 32 KiB), UTF-8 with optional BOM and unique literal **`GEOID`**. Do **not** open or iterate any county record or any year-specific geography values.
- Emit compressed full-body fingerprint + source header column-name **metadata only**; no Census `GEOID` case value, county name, state, area, lat/long, count of county rows, USDA rural classification or geography comparison. No ZIP/CSV raw body is persisted.
- One Q07 original attempt, **10+ offline synthetic tests** before original network. On source access/ZIP/schema mismatch: `HOLD_Q07_SOURCE_ACCESS_OR_SCHEMA`. On original source-byte and header success: `PASS_Q07_2023_CENSUS_GAZETTEER_D2_HEADERS_ONLY__GEOGRAPHY_BRIDGE_UNPROVEN`. On persistence failure `HOLD_Q07_OPERATIONAL_INTEGRITY`, no repeat of same source attempt or fabricated receipt.
- Capture JSON+MD in `research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q07/evidence/attempt-01.*`; mandatory `qualification=CENSUS-USDA-Q07`, `science_f01_authorized=false`, `individual_identifiers_emitted=false`, `source_case_rows_emitted=false`, `future_outcome_values_emitted=false`, `incremental_monetary_cost_usd=0`. Independently published run-specific immutable evidence branch, followed by separate two-file-only audited promotion PR.
- Q07 **cannot** certify 2023↔2024 exact boundaries or match USDA RUCC classifications. To proceed to Q08 first preregister 2023/2024 Census GEOID source-id-only support and official geography-change/vintage exclusions, then only permitted identity fields; full geometry/crosswalk and field semantics would require **further** explicit preregistration. No automatic scientific F01.

**Track A:** `US-CMS-NPI-E01` terminal `INCONCLUSIVE` Issue #203 CLOSED, obsolete recurring watcher retired. **Track B:** sole active S01 Issue #244; Q01/Q03 HOLD preserved, Q04/Q05/Q06 PASS at their narrow evidence grades. **0 USD**.
