---
id: SOURCE-QUAL-CENSUS-USDA-Q04
kind: prospective-independent-dual-first-party-source-schema-receipt
created: 2026-10-21
parent_issue: 244
canonical_base: 54f05a89a9c3dd69d524577aab557ba00c50ad70
frozen_before_source_body_access: true
track_a_scientific_status: INCONCLUSIVE_US_CMS_NPI_E01_TERMINAL
allowed_data_read: original_bytes_and_headers_only
scientific_f01_authorized: false
zero_cost_required: true
---

# CENSUS×USDA Q04 — independently frozen first-party county-identity source access / 신규 정부원본 D2·헤더 적격성 사전계약

**Independence / 독립성:** New Census Bureau and USDA ERS dual-source family; NOT FEMA/EPA Q01/Q02/Q03 rescue, NOT any past CMS E01 follow-up, not a new scientific F01/N01/E01, not R60 or a rural-urban inference. Q03 remains terminal `HOLD_Q03_OPERATIONAL_INTEGRITY`; original Q01 remains `HOLD_SOURCE_ACCESS_OR_SCHEMA`. S01 #244 is sole active operational issue under `DEC-324`; Issue #203 remains closed.

## Official discovery evidence / 공식 안내 출처

- Census 2024 Gazetteer official catalog: `https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2024.html`, section Counties and 2024 geography (the catalog states ZIP/tab-delimited national release; includes Puerto Rico, with no population/housing counts). Source-native `GEOID` is documented geographic identifier but requires exact archived source header confirmation.
- USDA ERS Rural-Urban Continuum Codes public catalog: `https://www.ers.usda.gov/data-products/rural-urban-continuum-codes`. The 2023 download is CSV ~614.57 KB, last-updated label 2024-01-22; 2023 OMB metro definitions and 2020 Census urbanization framework mean **2023 RUCC vs 2024 Gazetteer geography cannot be assumed 1:1**. USDA documentation describes 3,235 county/county-equivalent RUCC records including outlying territories and aggregated metropolitan coding in 9 Virginia independent cities. Metadata is for prospective qualification only, no RUCC numeric outcomes read.

## Frozen source GET contract / 실제 원본 GET 동결

Source A exactly `https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip` (HTTPS Census first-party, ZIP, maximum 2 MiB, compressed bytes SHA256 recorded). Require exactly **one nonredirected GET** with HTTP 200. ZIP is opened **only to inspect archive member path and first header row**, not geographic case/coordinate/name/area values; compressed SHA and length recorded. Require a single non-directory, unencrypted `.txt` member, maximum uncompressed 4 MiB; text header delimited by tabs with literal `GEOID`. ZIP member name is **not** guessed or repaired; a different member shape is HOLD. If CSV dialect differs, HOLD.

Source B exactly `https://www.ers.usda.gov/media/5768/2023-rural-urban-continuum-codes.csv?v=89142` (official ERS website download URI exposed by published catalog at research time, potential version query is frozen verbatim, no redirects to alternate hosts, maximum 2 MiB). Require exactly **one nonredirected GET** with HTTP 200. Treat as UTF-8 with optional BOM, CSV comma header and require a unique literal column named `FIPS` for prospective county join; if this expectation does not match the actual publisher header, `HOLD_Q04_SOURCE_ACCESS_OR_SCHEMA` with **no retroactive schema normalization**. File label/update-time may differ from actual HTTP Date; never infer first publication time.

**Exact network budget:** 1 Census GET + 1 USDA GET, each at most 2 MiB plus 1 byte, explicit 40-second timeout, no retry, mirror, redirection, alternative data product, authenticated client or paid service. SHA256 of full original downloaded raw bytes is computed **before** inspecting header/member; no expected digest yet because this is a newly pre-registered *first acquisition*. Once source SHA recorded, any future Q05 must freeze those SHA bytes prospectively.

## Predeclared Q04 strictly source-metadata-only gates / 독립 허용 범위

1. Source identity exactly matches frozen URLs and allowed `.gov` domains; no redirects.
2. Both bounded HTTP 200 content bodies obtained without retry; record observed UTC, byte count and sha256, headers Content-Type, ETag, Last-Modified if present (not publication date).
3. Census ZIP magic correct, one safe text member, nonencrypted, header contains literal `GEOID`; only member/header tokens opened.
4. USDA CSV decoded with UTF-8-SIG strict, comma header literal `FIPS` unique; header only, no rural-urban codes or case rows.
5. Zero row counts, geographic identifiers, site names, outcome values or cross-dataset overlap computed; **never** treat a D2 source-body receipt as a verified county join or science readiness.
6. No raw source ZIP/CSV, individual identifiers, case-row samples, censored data, names, stats, inferred effects, or response bodies stored as GitHub artifacts; only source metadata+header field names.
7. Output sole receipt `attempt-01.json` plus matching `attempt-01.md` under Q04 `evidence/` with `source_case_rows_emitted=false`, `future_outcome_values_emitted=false`, `individual_identifiers_emitted=false`, `science_f01_authorized=false`, `incremental_monetary_cost_usd=0`.
8. Before first original source access, 8+ synthetic guard tests must PASS. On any error, report **terminal `HOLD_Q04_SOURCE_ACCESS_OR_SCHEMA`** or `HOLD_Q04_OPERATIONAL_INTEGRITY`, never silently fallback or repair.
9. **Durability:** in the same free Actions run, use previously offline-tested `tools/persist_s01_evidence_branch.py` to push exactly one `refs/heads/evidence/s01/census-usda-q04/<run-id>` branch (no direct `main` push, no overwrite, no force). After CI, independently inspect exact original artifact SHA and evidence branch, then only via reviewed expected-head PR copy/promote evidence into canonical main. If evidence branch publication fails, original Q04 scientific/source result stays operational HOLD; no repeat/fabricated receipt.
10. Q04 criteria **D2 source-byte/header receipt only**. PASS disposition `PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN` if both official original-body fingerprints and literal headers pass. A transport/schema failure is `HOLD_Q04_SOURCE_ACCESS_OR_SCHEMA`, a persistence/run integrity failure is `HOLD_Q04_OPERATIONAL_INTEGRITY`. A D2 PASS does **not** establish aligned county vintages, RUCC value availability, aggregation rules, risk factors, ecological associations, statistics or new F01. Any Q05 structural relationship requires fresh prospective ID/time/crosswalk contract **before** opening row IDs.

## Strict process / 정확한 실행 순서

A. Commit this contract to canonical main **before any of the two source body GET requests**.
B. Implement runner/offline tests and immutable per-run evidence branch workflow; tests BEFORE first GET. Do not add new Issue.
C. Run one bounded free public GitHub Actions operation. Record run outcome and branch ref, inspect receipts, independently promote to main via review PR. Do **not** rerun original Q04 on failure.
D. Only after durable complete proof decide next separate Q05 structural preflight or next source prospect; there is **no automatic research hypothesis, no data outcome analysis, no cost**.

**Cost / 비용: 0 USD**. Paid resources require user approval.
