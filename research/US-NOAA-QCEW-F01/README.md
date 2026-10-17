---
id: US-NOAA-QCEW-F01
created: 2026-10-17
type: prospective-outcome-blind-structural-feasibility
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R58
parent_selection_commit: 4da12e3c70f3a52ab7007dea056cbc59e11a64d0
canonical_primary: US-CMS-NPI-E01
candidate_future_employment_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-NOAA-QCEW-F01 — NOAA county storm exposure × BLS sector structural panel / NOAA 기상충격 × BLS 산업별 지역 조인

## Scope / 목적

Under the user's authorized two-track program, this **secondary** F01 tests **exact historical, outcome-blind source identity and join feasibility**, NOT whether storms cause job losses. Primary `US-CMS-NPI-E01 / Issue #203 / DEC-318` retains scientific authority, 346,859 pairs, original 18 gates and first-CMS-weekly release lock unchanged.

Distinct NOAA county-only severe-weather *exposure* under a pre-fixed 2023 source snapshot may eventually be compared to **separately preregistered later QCEW employment** after a later official release. This F01 cannot authorize observing future employment-change outcomes or assert a causal weather effect.

## Immutable official source, versions and identity / 불변 공식 원천

- NOAA official details object exactly `https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2023_c20260323.csv.gz`; official [bulk field description](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Bulk-csv-Format.pdf) has `CZ_TYPE` (C county, Z forecast zone, M marine), `STATE_FIPS`, `CZ_FIPS`, `BEGIN_DATE_TIME`, `EVENT_ID`, `EVENT_TYPE`, and is distinguishable from the file creation date.
- BLS official current historical **2024 Q1** NAICS industry slices using [documented data.bls.gov URL grammar](https://www.bls.gov/cew/additional-resources/open-data/csv-data-slices.htm):
  - `https://data.bls.gov/cew/data/api/2024/1/industry/23.csv` — construction
  - `https://data.bls.gov/cew/data/api/2024/1/industry/62.csv` — health care / social assistance
  - `https://data.bls.gov/cew/data/api/2024/1/industry/72.csv` — accommodation/food
- **No other year**, ZIP mirror, alternate weather archive-creation revision or different industry may be substituted after source adjudication. Exact HTTP byte SHA, response headers, sizes and fetch UTC must be recorded; source content is not yet fully parsed.
- Unit: BLS **5-digit county `area_fips` × one of industry codes `23,62,72` × 2024 Q1**, with private `own_code=5`, `size_code=0`, and non-suppressed QCEW disclosure status. NOAA exposure key is exact `STATE_FIPS` 2-digit + `CZ_FIPS` 3-digit, **only `CZ_TYPE=C`**. Both zero-padding rules must preserve source-native FIPS identity, no coordinates/name/fuzzy matching. Connecticut `state_fips=09` is **prospectively excluded** owing to officially documented QCEW 2024 county-equivalent transition.
- Valid 2023 storm exposure events restricted *before any row opening* to exact `EVENT_TYPE` in `Tornado`, `Flash Flood`, `Flood`, `Thunderstorm Wind`, `Hail`. Remove duplicate `EVENT_ID` with deterministic exact ID semantics; no injuries, deaths or property damage fields as model exposures. Event reports are not random draws; reporting differences and spillovers remain fundamental limitations.
- Binary storm exposure = **at least one** exact source-native eligible county storm in 2023; no posthoc hazard-category tuning. Counties with zero observed storm reports cannot be called zero physical hazard without a reporting-opportunity qualification in N01.

## Prospective 18/18 outcome-blind source/structural F01 gates / 사전등록 구조요건

Each gate is pass/fail at first valid empirical run; require **18/18 PASS** for scientific structural PASS. Failure on valid evaluated source = frozen scientific HOLD; official-host body failure = `BLOCKED_TRANSPORT` and no scientific gate evaluated; synthetic/offline tests are not empirical success.

1. **NOAA official provenance:** exact NOAA directory / field guide both first-party, source version and public read license verified without billing.
2. **NOAA reproducible bytes:** exact pinned 2023 `.csv.gz` HTTP 200, gzip parseable, compressed bytes >1MB and full-byte SHA256+fetch UTC stored.
3. **BLS exact three sector sources:** all 2024 Q1 industry `23,62,72` URLs HTTP 200, each source parseable as CSV, nonempty, full SHA256+fetch UTC stored.
4. **NOAA required schema:** NOAA header includes exact `CZ_TYPE,STATE_FIPS,CZ_FIPS,BEGIN_DATE_TIME,EVENT_ID,EVENT_TYPE` after unambiguous source-native capitalization mapping; no column repair.
5. **BLS required schema:** each sector header includes `area_fips,own_code,industry_code,year,qtr,disclosure_code,size_code`.
6. **NOAA geography firewall:** only county `CZ_TYPE=C`; all forecast-zone Z and marine M are excluded by rule without mapping to counties; provenance of counts by type recorded.
7. **NOAA exact county syntax:** >=95% of eligible county candidate storm rows have valid two-digit `STATE_FIPS`, three-digit `CZ_FIPS` and 5-digit concatenated FIPS; invalid rows excluded, not repaired.
8. **NOAA identity cardinality:** >=99.9% of nonblank exact eligible `EVENT_ID` occur only once in pinned 2023 source; duplicate IDs excluded.
9. **NOAA bounded event-time:** >=99% of eligible `CZ_TYPE=C` records have parseable `BEGIN_DATE_TIME` with year 2023; do not use ZIP creation date as event date.
10. **NOAA historical county coverage:** >=1,200 unique valid non-Connecticut FIPS counties represented by `CZ_TYPE=C` weather reports (any source-native event type).
11. **Frozen hazard subset support:** >=4,000 source-native qualified unique events across exactly `Tornado,Flash Flood,Flood,Thunderstorm Wind,Hail`, with >=900 distinct valid non-Connecticut county IDs.
12. **BLS quarter/sector fidelity:** >=99% of candidate QCEW 2024 Q1 records with exact target sector codes have `year=2024,qtr=1`, private own=5, size=0, valid 5-digit area, and non-disclosed records excluded. Qualifying denominator and excluded rows explicit.
13. **BLS exact uniqueness:** >=99.9% unique exact county×industry×year×quarter×ownership×size keys among eligible QCEW rows; ties/ambiguities excluded before joining.
14. **BLS sector support:** for each independently frozen sector 23,62,72, >=1,500 distinct qualifying non-Connecticut counties after disclosure filtering.
15. **NOAA→BLS exact intersection:** for **each** of the three sectors, >=900 exact non-Connecticut NOAA valid hazard-county IDs match BLS qualified county IDs, no fuzzy repair or crosswalk invented.
16. **Non-tautological exposure support:** source-native frozen 2023 storm presence bit can be assigned to >=95% of structurally qualified BLS county-sector candidates, independent of QCEW employment/wages and with county/sector overlap documented; absence of a report is labelled `NO_RECORDED_EVENT` not proof no storm.
17. **Future outcome and privacy firewall:** **zero** 2025/2026/2027 held-out QCEW employment-change rows or numeric outcomes opened; 2024 QCEW only metadata/eligible denominator and structural area/industry keys; no wages/employment/causal/ranking results; no personal identities and no commercial/paid API.
18. **Immutable complete evidence:** one executed exact 18-gate result includes source URLs/sha/time, parsers, all numerators/denominators, per-gate PASS/HOLD, excluded CT/zone counts, version fingerprints and no-cost proof, committed before any separate N01 decision.

## Transport and scientific ethics / 전송·연구 규율

The prior R58 7-source access test checked first 2/4 bytes, public dictionaries and only the first BLS CSV header; **no scientific F01 gate has been run**. At F01 source-resolution, do not rewrite this contract based on observed county support, enlarge county definitions, relax thresholds, replace industries or NOAA creation snapshot. If source delivery fails in canonical zero-cost GitHub runner, at most **one independently scoped transport-only correction** may be attempted and must preserve original science; two consecutive infrastructure attempts require Mission-ROI branch-stop.

The future research's economic outcome must be **a newly specified, source-native later official QCEW release** separately frozen in an eventual N01/E01; never silently treat any already-inspected employment level as future observation. An administrative weather *report* is not necessarily a randomly assigned natural hazard; observational selection confounding must be explicit.

**Execution status:** `FROZEN_PRE_ISSUE__SCIENTIFIC_NOT_EXECUTED`. 0 USD.
