---
id: SOURCE-QUAL-CENSUS-USDA-Q06
type: independent-preregistered-geography-scope-provenance-not-boundary-equivalence
created: 2026-10-23
parent_issue: 244
base_commit: eb1ebafef8bd5b58df7cade756dd419f9888dfa2
state: FROZEN_BEFORE_UNMATCHED_PREFIX_REACCESS
scientific_f01_authorized: false
cost_usd: 0
---

# Census×USDA Q06 — 13 unmatched FIPS scope provenance / 미일치 13개 지역 원본 포함범위 검증 사전계약

**Purpose / 목적:** Decide whether the **exact 13** USDA-2023-only FIPS from Q05 are exhaustively explained by the **four U.S. Island Areas explicitly excluded from the Census 2024 national Gazetteer**, without opening county names or RUCC class/value, and without treating string match as geographic-vintage equivalence. This is **NOT** posthoc Q05 repair, FEMA-EPA Q03 reopening, F01/N01/E01 scientific experiment, or new Issue/R60 selection.

## Official first-party source definitions discovered before inspection / 불일치 코드 접근 전 공식 문서 확인

- Census Bureau official 2024 Gazetteer scope: `https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2024.html`. Explicitly includes **50 states, District of Columbia, Puerto Rico**. Explicitly excludes **American Samoa, Guam, Commonwealth of Northern Mariana Islands, U.S. Virgin Islands**. It cautions that named units and geographic codes may differ across 2013-2023 ACS/2020 Census; *no* historical county equivalence is guaranteed.
- USDA ERS 2023 RUCC scope: `https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation`. States **3,235** county/county-equivalent entities inclusive of U.S. outlying territories, including island areas, 9 Virginia independent-city aggregation situations, and the 2023 OMB metro classification. These are documentation facts, not values opened in Q05.
- Census Bureau first-party ANSI/FIPS jurisdiction prefix codebook: `https://www.census.gov/library/reference/code-lists/ansi.html`. Scope-excluded prefix set is **`60` American Samoa, `66` Guam, `69` Northern Mariana Islands, `78` U.S. Virgin Islands**. Puerto Rico **`72`** is **included** in both respective documented source scopes. These four prefixes are **fixed prospectively**; no additional prefixes may be declared eligible after observing 13 unmatched.
- Census historical county change scope reference: `https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.html`. Reference-date-boundary rule is January 1 of each census data vintage; changes after that date appear in later products, not an automatically valid 2023↔2024 one-to-one concordance.
- Official CMS NPI first weekly E01 #203 terminal `INCONCLUSIVE`, [DEC-324](../../../registry/DEC-324.md) / S01 #244 sole active; these authorities are not changed.

## Frozen original first-party bytes / 두 정본 원본 SHA 고정

Use *exactly one* no-redirect GET each for original Census 2024 `https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip` and USDA 2023 `https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=89142` (max 2 MiB/each, 40s per request, zero retries/mirrors/credentials/cost). Before any record field decoding, validate **both** complete byte bodies and SHAs independently against immutable Q04/Q05:

- Census ZIP **141,679 bytes**, SHA256 `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`, ZIP one member exactly `2024_Gaz_counties_national.txt` uncompressed **647,830** bytes.
- USDA CSV **629,322 bytes**, SHA256 `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`, header exactly `FIPS,State,County_Name,Attribute,Value`.

If either changed, immediately `HOLD_Q06_SOURCE_VINTAGE_CHANGED`, do not read any key rows, retry, choose another ZIP, or claim Q05 rescue.

## Only allowed projected fields and disclosure / 허용 열

Use *only* Census `GEOID` and USDA `FIPS`; no other source row field, county name, state name, latitude, longitude, area, RUCC `Attribute`, numeric `Value`, population, category, or outcome. Keep five-character ASCII 5-digit keys transiently in memory, following existing frozen Q05 conservative `SSCCC` validity rules (no zfill/names/alias repair). No full FIPS/individual county ID/county name may be printed or stored. Output only counts of distinct keys, intersection/USDA-only keys, and **aggregate counts by the four predeclared two-character state-prefix codebook groups**, never raw 5-digit keys. Do not persist source body or raw row records. Confirm no Census-only key, no Census duplicate, preserve USDA long-format duplicate metrics.

## Frozen independent yes/no decision / 사전등록 통과·보류 기준

Expected Q05 invariants (read exact durable Q05 original JSON before network and verify, do not recompute thresholds afterward): `Census unique == 3222`, `USDA unique == 3235`, `overlap == 3222`, `USDA-only == 13`, `Census-only == 0`, **52** overlapping jurisdiction prefixes, and **6468** USDA duplicate FIPS rows. Recompute with same source-native key projection to verify no drift.

Classify `PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED` iff ALL:
1. exact both source hashes/bytes match Q04/Q05, original first-party docs remain cited, offline tests pass **before** source ID access;
2. actual source-native key census/usda/overlap/missing and repeats equal Q05 fixed counts above;
3. **all 13** USDA-only codes have state-prefix **ONLY** in prospectively fixed `{60,66,69,78}`, with **zero** unmatched `72` Puerto Rico or other state prefixes;
4. Census contains **zero** keys in those four excluded Island Area prefixes;
5. aggregate counts of the four fixed groups sum exactly **13**; don't require a retrospectively invented individual county list or numeric rurality value.

If any outside-scope unmatched FIPS or Census contains excluded-prefix keys, `HOLD_Q06_SCOPE_CANNOT_EXPLAIN_ALL_13`. If Q05 totals changed despite hashes, `HOLD_Q06_SOURCE_ID_RECONCILIATION`. Schema/parser/other failure `HOLD_Q06_SOURCE_ACCESS_OR_SCHEMA`. Evidence-branch persistence failure remains `HOLD_Q06_OPERATIONAL_INTEGRITY`, not a provenance pass.

**Interpretation firewall / 한계:** A Q06 PASS would explain the **13 source key coverage discrepancies** at territory-scope level, NOT prove shared **3,222** keys have identical geographic boundaries as of 2023 and January 1, 2024, or that USDA long-form RUCC values can be validly joined/aggregated. These require a **separately preregistered Q07 geographic vintage/field-semantic verification**, **before** any scientific F01 or rural/urban effects investigation. Neither this nor Q05 alone qualifies D3 in the source registry's frozen meaning.

## Evidence and operational guard / 실행 규약

- Prospective contract on main before any unmatched-key-prefix inspection, then synthetic offline tests >=10 PASS before original GETs; standard public Actions, 0 USD.
- Exactly one original Q06 attempt, JSON + bilingual MD only under `research/SOURCE-REGISTRY-S01/qualifications/CENSUS-USDA-Q06/evidence/attempt-01.*`.
- Required machine envelope: `qualification=CENSUS-USDA-Q06`, `science_f01_authorized=false`, `source_case_rows_emitted=false`, `individual_identifiers_emitted=false`, `future_outcome_values_emitted=false`, `incremental_monetary_cost_usd=0`.
- Publish unique `refs/heads/evidence/s01/census-usda-q06/<run-id>` (not direct main), independent artifact/commit audit then evidence-only reviewed PR promotion. Terminal failure gets immutable HOLD; no original Q06 retry or post-hoc boundary.
- Track A E01 remains closed; existing scheduled dormant CMS first-source watcher may be retired separately as cost/maintenance hygiene after verifying no active research need. This Q06 itself changes no E01 code or checkpoint.

**No monetary spend or paid source without explicit user approval.**
