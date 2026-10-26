# Q09 — official TIGER 2023/2024 county geometry source listing metadata only

**Prospective contract frozen 2026-10-26 before new official directory GET.** Sole parent S01 Issue #244. E01 #203 terminal `INCONCLUSIVE`; `DEC-324` unchanged, **0 USD**. This is a **D0 source-discovery step**, not boundary equivalence analysis or repair of Q08.

## Why and what is not known
Q08 is terminal `PASS_Q08_CENSUS_2023_2024_GEOID_SYNTAX_SUPPORT_ONLY__BOUNDARY_EQUIVALENCE_UNVERIFIED`: 3,222/3,222 literal county GEOID strings match. Census states its 2023 and 2024 TIGER/Line legal boundaries are referenced to **January 1, 2023** and **January 1, 2024**, respectively. The official county geometry **national archives are ~80 MB per vintage**. No archive body, shapefile polygon, area, coordinate, county name, or USDA `Attribute/Value` has been opened or compared. Do not falsely equate unchanged identifiers with unchanged boundaries.

## Frozen first-party listing URLs and candidate archives
2023 directory exact: `https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/`. Required exact relative listed archive name: `tl_2023_us_county.zip`.
2024 directory exact: `https://www2.census.gov/geo/tiger/TIGER2024/COUNTY/`. Required exact relative listed archive name: `tl_2024_us_county.zip`.

Official Census annual TIGER source documentation:
- `https://www.census.gov/geographies/mapping-files/2023/geo/tiger-line-file.html` — legal county boundaries as of 2023-01-01.
- `https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html` — legal boundaries as of 2024-01-01.
- `https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.html` — annual county geography reference cutoff.
The directory endpoints are **not** the 80MB ZIP download URLs and no geometry source body is approved in Q09.

## Exact Q09 access and metadata constraints
- Before network, require canonical Q08 `RESULT.md` and original `evidence/attempt-01.json`, `science_f01_authorized=false`, and exactly the 3,222/3,222 common-key aggregate. Historical Q07/Q06 and E01 unchanged.
- Exactly one **nonredirected GET** of each official *directory HTML listing*, each at most **256KiB** and 40s timeout, zero retries, no mirror, no extra link follow, credentials, fee, or approved archive-body transport. The full received directory HTML bytes are SHA-256 fingerprinted before parsing; record byte length and observed UTC. Never infer 2023/2024 archive first-publication timestamp from HTTP metadata.
- Parse only anchor `href` names from the HTML. Require exactly **one** literal relative href for the preselected 2023 national COUNTY ZIP and exactly one for the 2024 national COUNTY ZIP (no query/fragment/absolute/parent/case-fold alias). If absent, duplicated, or unexpected source response, `HOLD_Q09_OFFICIAL_CATALOG_OR_SOURCE_ACCESS`.
- Record only whether each target exact archive name is listed, listing URL, SHA-256, bytes, HTTP status, and the Q09 source-generation date; **do not download ZIP, read archive records, geometry, country area, case-level county keys, or estimate geospatial overlap**. No original HTML body stored in GitHub.
- Allow `PASS_Q09_OFFICIAL_TIGER_2023_2024_COUNTY_ARCHIVES_LISTED__GEOMETRY_UNOPENED` only when both exact official listing gates pass, and **no** boundary identity/inference regardless.
- At least 10 offline synthetic tests before any network; emit only immutable safe JSON and bilingual Markdown, no raw HTML/individual IDs, `qualification=CENSUS-USDA-Q09`, `science_f01_authorized=false`, `source_case_rows_emitted=false`, `individual_identifiers_emitted=false`, `future_outcome_values_emitted=false`, `incremental_monetary_cost_usd=0`. Publish unique `refs/heads/evidence/s01/census-usda-q09/<run-id>`, independent evidence-only expected-head PR; no direct main push. Failure is terminal HOLD, never rerun the original attempt to rescue.

## Later decisions remain independent
Q09 D0 PASS only proves that official polygon archives **are advertised**. A separate prospective Q10 would need to plan geometry transport/storage budget, source-integrity rules, polygon comparison algorithm, coordinate reference systems, and a bias/precision plan **before** any 80MB archive access; do not approve Q10 or scientific F01 automatically. No new third Issue or paid service.
