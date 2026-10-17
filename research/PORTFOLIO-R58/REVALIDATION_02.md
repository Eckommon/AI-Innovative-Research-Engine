---
id: PORTFOLIO-R58-REVALIDATION-02
issue: 226
created: 2026-10-17
frozen_contract: 86f2bf09b4fd2c38dbd89608eb80a368a428c7e5
first_party_empirical_run: 39023285368
first_party_empirical_evidence_commit: ce017ddf5249c89b72349f945084b9c05798098d
status: PRE_SCORE_ACCESS_AND_EXACT_UNIT_DOCUMENTATION_VERIFIED__ROW_JOINS_UNTESTED
candidate_future_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R58 — bounded official-source revalidation / 후보 채점 전 출처·식별·기존 종료연구 재검증

## Actual canonical runner evidence / 실제 GitHub 실행 근거

[Run #39023285368](https://github.com/Eckommon/AI-Innovative-Research-Engine/actions/runs/39023285368) on the zero-cost standard GitHub Ubuntu runner ran 10/10 offline boundary tests and actually returned **HTTP 200** for all seven exact first-party objects: NHTSA campaign and quarterly ZIP (4-byte `PK0304` signature each), both NHTSA text dictionaries, Census 2023 CBP county ZIP (4-byte ZIP signature), BLS 2024 Q1 county `01001.csv` CSV first header only, and NOAA Storm Events details 2023 gzip (2-byte `1f8b` signature). [Source evidence](evidence/source-endpoint-preflight-01.json).

**Epistemic limit / 중요 한계:** This proves server access for small file prefixes and first-party published field descriptions; it **does not** prove that entire archives download safely, ZIP members are parseable, record identity/cardinality, timely revisions, statistical effects, or any F01 gate. No source event rows, later-quarter employment, product-level recall memberships or cross-dataset joins were accessed. It is PRE-SCORE structural evidence only.

## C1 — NHTSA campaigns + quarterly remedy reporting / 캠페인·분기 이행보고

Official [NHTSA dataset catalog](https://www.nhtsa.gov/nhtsa-datasets-and-apis) supplies exact campaign and quarterly ZIP objects, source dictionaries and periodic updates, and identifies the recall campaign number as a primary public query path. Both archives' ZIP signatures validated from official `static.nhtsa.gov`, both source dictionaries accessible (3053 and 1244 bytes). **Still unverified:** exact field-level campaign ID equality across the two ZIPs, whether all quarterly reports are versioned rather than edited in place, frozen last-period cutoff and a valid separate prospective future-reporting event. An individual recall is not a vehicle-failure rate. Prior R57 NHTSA *vehicle engineering population* candidate did not qualify, and this is not that same unit or endpoint.

## C2 — Census CBP establishment structure × BLS QCEW labor / CBP 사업체 구조 × BLS 고용

Census official [2023 county ZIP index](https://www2.census.gov/programs-surveys/cbp/datasets/2023/) lists `cbp23co.zip` and separate record layouts. Its exact source ZIP signature is valid under real runner. Official [BLS QCEW CSV slices](https://www.bls.gov/cew/additional-resources/open-data/csv-data-slices.htm) document direct `data.bls.gov/cew/data/api/{year}/{qtr}/area/{area_fips}.csv`, `area_fips` five characters, `industry_code` and year/quarter, with ownership/disclosure fields; real first-line header from 2024 Q1 county Autauga (`01001`) was accessible with HTTP 200 and **no row values read**. [BLS area title docs](https://www.bls.gov/cew/classifications/areas/qcew-area-titles.htm) note Connecticut county geography change starting 2024. **Unverified:** correct corresponding Census `state`+`county` fields for the same reference vintage, NAICS 2017→2022 industry concordance, suppressed populations, and 2023 CBP release lag. QCEW and CBP both contain employment/payroll; avoid contemporaneous mechanical predictor leakage. No 2024 Census CBP version is assumed.

## C3 — NOAA Storm Events hazard exposure × BLS QCEW county-industry employment / 기상충격·후속 고용

NOAA official [Storm Events bulk CSV directory](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/) provides the pinned **2023 events detail** gzip `StormEvents_details-ftp_v1.0_d2023_c20260323.csv.gz`; metadata in current official ZIP folder lists archive snapshots with **d=event year, c=creation date**, and future revisions are possible. Official [bulk field guide](https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Bulk-csv-Format.pdf) explicitly defines `state_fips`, `cz_type` (C county/parish; Z forecast zone; M marine), `cz_fips` (county or zone code depending on type), `begin_date_time`, `event_id`. As documented, **only `cz_type=C`** can be considered for an exact 2+3 FIPS county candidate; zonal and marine reports must not be transformed into counties by centroid or name.

Actual canonical runner validated NOAA gzip signature HTTP 200 and BLS 2024 Q1 `area_fips`, `industry_code`, `qtr`, `disclosure_code` **header** under HTTP 200, using no event/employment rows. **Unverified:** exact source-native county validity and 5-digit `state_fips+cz_fips` normalization, observed C/Z/M fractions, county boundary changes, NOAA observation opportunity/selection bias and QCEW sector common support. Storm report counts cannot be interpreted as exogenous hazards without reporting intensity and exposure controls; labor changes alone do not establish causality.

## Prior canonical route equivalence / 기존 연구 재실행 차단

Earlier `research/US-AIR-F01/DERIVED_NOAA_DATE_SUPPORT.csv` documents NOAA **aviation weather/date** support, **not** a Storm Events County FIPS × industry QCEW panel. There is no exact `US-NOAA-QCEW` or `US-BLS-CBP` F01 in the current canonical research tree. FDA/NHTSA motor-carrier routes and R57 vehicle product-denominator HOLD are distinct. FAA aircraft F01 stopped operationally after three diagnostics; no replacement of historic snapshot requirements, no fourth workaround. R58 does NOT revive a terminal equivalent by mere renaming.

## Eligibility status before scoring / 채점 전 선별 자격

| Candidate | First-party prefix / metadata | Exact join fields **documented** | Actual exact row joins | Fatal pre-score defect known? |
|---|---|---|---|---|
| NHTSA campaign quarterly | YES (two ZIP + two dictionaries) | Candidate campaign key described | **NO** | None proven, revision/quarterly identity risk |
| Census CBP × BLS QCEW | YES (Census ZIP + BLS CSV header) | 5-char QCEW area; CBP county layout documented | **NO** | None proven, NAICS+geography-vintage+lag risk |
| NOAA Storm Events × QCEW | YES (NOAA gzip + BLS CSV header) | NOAA `CZ_TYPE=C`, `STATE_FIPS`, `CZ_FIPS`; QCEW `area_fips` | **NO** | None proven, zones must be excluded |

All three qualify **only for prospective conditional structural-F01 Stage-0 consideration**. They are **NOT empirical source-row PASS**, do not yet satisfy exact cardinality or future outcome-release gates. Score per the originally frozen /45 dimensions; no retroactive threshold adjustment, automatic runner-up promotion or statistical inference. Cost 0 USD.
