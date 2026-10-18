---
id: SOURCE-QUAL-FEMA-EPA-Q01
created: 2026-10-19
type: prospective-secondary-source-qualification
parent_issue: 244
status: FROZEN_BEFORE_FIRST_FULL_SOURCE_ACCESS
outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# SOURCE-QUAL-FEMA-EPA-Q01 / FEMA 재난 × EPA county 대기질 원천검증

This is a separately prospective source-body qualification within authorized S01 Issue #244, not an F01 or E01. Original S01 12/12 proof and D0-D4 grades stay immutable, as do frozen E01 Issue #203, decision DEC-318, the 346,859 matched pairs and its official first-weekly release gate. / 이번 검증은 별도의 출처자격 확인일 뿐 과학적 연구 승인이 아니다.

## Exact frozen official sources / 불변 원천

- FEMA OpenFEMA v2 full DisasterDeclarationsSummaries CSV: https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv ; source-native fipsStateCode (2 digit), fipsCountyCode (3 digit), with special cases and non-county records. https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2
- EPA AQS AirData full 2024 county annual AQI ZIP: https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2024.zip ; expected State Code and County Code fields, only monitored counties; official https://aqs.epa.gov/aqsweb/airdata/download_files.html and https://aqs.epa.gov/aqsweb/airdata/FileFormats.html .

## Preregistered fixed source checks / 실증 전 조건

1. Exactly one first-party HTTPS GET per source in zero-cost canonical GitHub Actions. No guessed mirrors, redirect-following, authentication, paid API or unauthorized access.
2. Complete FEMA source bytes bounded at 64MiB and EPA ZIP at 8MiB, exact SHA256, bytes, observed UTC, HTTP headers.
3. FEMA CSV first header only. EPA ZIP check safe archive member and read **only CSV header**, never event or AQI record values. Do NOT aggregate county keys or outcome distribution at this stage.
4. Confirm source-native exact schema fields: FEMA fipsStateCode/fipsCountyCode and EPA State Code/County Code; any difference is a source-schema HOLD, not a posthoc repair.
5. Publication date, file vintage and transport Last-Modified are separate from fetch time and cannot prove first publication.
6. If full bodies and schema are proved then D2_PAIR_READY_KEYS_DOCUMENTED_ONLY, never an exact FIPS join PASS; if either fails then HOLD_SOURCE_ACCESS_OR_SCHEMA, not general unavailability. No future study or F01 selection.
7. Store only one immutable JSON/MD source-qualification report; never store source body/records or individual identifiers; no outcome event count/economic, health, AQI effect, prediction or causal result.
8. Prior NOAA×BLS terminal HOLD, FDIC/RCRA N01 HOLD and old R57/R58/R59 held candidates cannot be rescued. No third open Issue. Cost strictly 0 USD.

## Execution order / 다음 실행

Merge this prospective contract before any source GET; write deterministic bounded reader and offline safeguards; use free one-time Actions; independently inspect immutable evidence, leave E01 canonical primary and S01 #244 secondary. No auto R60 or change of scientific checkpoint.

**Scientific status:** NOT_EXECUTED. **Cost:** 0 USD.
