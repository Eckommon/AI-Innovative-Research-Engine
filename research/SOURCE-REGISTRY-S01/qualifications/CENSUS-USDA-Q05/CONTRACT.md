---
id: SOURCE-QUAL-CENSUS-USDA-Q05
created: 2026-10-21
parent_issue: 244
frozen_before_any_source_row_id_access: true
parent_q04_immutable_result_commit: 058fe1b87fa4e3deac08dbdeeab3509b1a99a5a3
type: independent-source-native-geography-key-syntax-support
scientific_f01_authorized: false
cost_usd: 0
---

# Q05 — Census 2024 × USDA 2023 raw identifier-only structural preflight / 신규 군코드 구조 검증 사전계약

**Independent scientific scope:** Reuse Q04's immutable two already verified source bodies for exactly *one new preregistered structure-only attempt*. This is a separately frozen ID/key access, NOT a changed Q04 source/header decision, and NOT reopening terminal FEMA×EPA Q03. The prior Q04 D2 receipt exists at `research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q04/evidence/attempt-01.json`. E01 Issue #203 terminal closed, S01 #244 sole active.

## Fixed exact original source identity before any record ID read

Census 2024 national county Gazetteer exact URL:
`https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip`.
**Original immutable Q04 SHA256:** `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`, **bytes 141,679**, ZIP member exactly `2024_Gaz_counties_national.txt` (647,830 uncompressed). Exact header has literal tab-delimited `GEOID`, and other (nonallowed) geography/area/location fields.

USDA ERS 2023 Rural Urban Continuum Codes exact URL:
`https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=89142`.
**Original immutable Q04 SHA256:** `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`, **bytes 629,322**, exact CSV header `FIPS,State,County_Name,Attribute,Value`, long-format nonunique county records.

For **each** source perform exactly one first-party, HTTP200, no-redirect, 40sec timeout, max 2 MiB GET and compute **full-body SHA and length before any record-level access**. If either digest/length changes: terminal `HOLD_Q05_SOURCE_VINTAGE_CHANGED` and do not parse any source row IDs; no retry/mirror/repair or source alternate. Avoid direct ZIP/CSV raws in any artifact.

## Prospective key-only data access / 실제 판독 허용 범위

- Census: decode only the `GEOID` field of each tab-delimited 2024 national-counties row. All other columns incl USPS, ANSICODE, NAME, ALAND, AWATER, lat/long **excluded** from read projection. No geometry, place names, population or unit-value selection.
- USDA: decode only literal source `FIPS` from each comma-delimited 2023 RUCC row. **Never** inspect `Attribute`, `Value`, State, County_Name, metro/nonmetro category, outcomes, trends or RUCC code. File is long-format; repeated county FIPS are an allowed native data grain, deduplicate **only for availability support**. No selecting one attribute/value based on outcomes.
- Both identifiers: strip only surrounding ASCII whitespace; require exactly five ASCII decimal digits `^[0-9]{5}$`, first two `SS !=00`, last three `CCC not in {'000','999'}`; no numeric casts, inferred padding, names/crosswalk, state-matching fuzzy repair. Reject and count invalid rows **only in aggregate**; don't serialize/print any actual county ID. Distinct Census GEOIDs should be one row per county: if any duplicate, `HOLD_Q05_UNEXPECTED_CENSUS_KEY_GRAIN` not dedup-repair. USDA duplicates permitted and explicitly counted. Reject if either ID data file has bad header or unexpected ZIP member.
- 2023 RUCC and 2024 Gazetteer county equivalents may differ, including Connecticut geography changes, Virginia independent cities, or outlying territories; **numeric FIPS equality is only string syntax**, not actual identical 2023/2024 geographic unit or comparable rural-urban status.
- No aggregation of rurality `Value`, population, area, density, lat/long or any outcome. No physical file saved, no individual county/site list and no matched IDs printed.

## Frozen denominator and gates / 결과 전 검증기준

Record aggregate structural counters only:
`census_2024_unique_5digit_geoid`,
`usda_2023_unique_5digit_fips`,
`distinct_key_overlap`,
`usda_keys_not_present_in_2024_census`,
`census_keys_not_present_in_usda`,
`overlap_share_of_usda_keys`,
`distinct_state_prefixes_in_overlap`,
`usda_duplicate_fips_rows`,
`invalid_census_key_rows`, `invalid_usda_key_rows`, `census_duplicate_key_rows`.
Never output actual key values.

Pass source-native syntax-only support if ALL:
1. `census_2024_unique_5digit_geoid >= 3000`;
2. `usda_2023_unique_5digit_fips >= 3000`;
3. `distinct_key_overlap >= 3000`;
4. `overlap_share_of_usda_keys >= 0.95`;
5. `distinct_state_prefixes_in_overlap >= 50`;
6. `usda_duplicate_fips_rows > 0` (evidence consistent with the observed long `Attribute/Value` layout);
7. `census_duplicate_key_rows == 0`;
8. neither original SHA/length/header/membership nor freeze/guard violated.

If these hold, `PASS_Q05_SOURCE_NATIVE_FIPS_SYNTAX_SUPPORT_ONLY__GEOGRAPHY_VINTAGE_UNVERIFIED`. If support fails, `HOLD_Q05_INSUFFICIENT_NATIVE_FIPS_SUPPORT`. If duplicates in Census `HOLD_Q05_UNEXPECTED_CENSUS_KEY_GRAIN`. If source digest/length changed, `HOLD_Q05_SOURCE_VINTAGE_CHANGED`. Other parser/schema failures: `HOLD_Q05_SOURCE_ACCESS_OR_SCHEMA`. A source-ID result does not authorize scientific F01, rurality/demographic inference or join comparability.

## Evidence integrity / 정본 보존

All offline tests (>=10 synthetic boundary tests) must pass **before original source ID access**. Write exactly one JSON+MD Q05 receipt under `research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q05/evidence/`. Its safety envelope includes `source_case_rows_emitted=false`, `individual_identifiers_emitted=false`, `future_outcome_values_emitted=false`, `science_f01_authorized=false`, `incremental_monetary_cost_usd=0`. CI must use unique `refs/heads/evidence/s01/census-usda-q05/<run-id>` **not** direct main; subsequently independently inspect and review-only promote exact artifacts by PR. Failed original attempt cannot be rerun to rescue result; preserve immutable HOLD if original evidence persistence fails.

**Next steps:** Q05 is a D2+source-native-ID feasibility check only. To compare any rural/business/social outcomes requires a new preregistered science route with explicit 2023↔2024 county-geography concordance strategy, observational design, bias/power criteria, fresh source vintage and independent Issue authority. No such science work is automatically authorized.

**Cost: 0 USD.** No paid compute, external API, third issue, or E01 reactivation.
