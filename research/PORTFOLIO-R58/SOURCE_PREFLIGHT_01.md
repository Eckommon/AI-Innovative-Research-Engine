---
id: PORTFOLIO-R58-SOURCE-PREFLIGHT-01
issue: 226
created: 2026-10-16
frozen_contract_commit: 86f2bf09b4fd2c38dbd89608eb80a368a428c7e5
type: first-party-documentation-only-outcome-blind
status: PARTIAL_DOCUMENTED_SOURCES_BINARY_ACCESS_NOT_YET_VERIFIED
candidate_rows_opened: false
incremental_monetary_cost_usd: 0
---

# R58 source preflight 01 — Official documentation only / R58 원천 문서 1차 확인

**Important / 중요:** This is a first-party *documentation/URL* preflight, NOT a real CSV/ZIP transport test. No candidate outcome membership, effect, positivity, association, score, or future release was read. Do not claim success at F01 based on this document.

## C1 NHTSA quarterly recall campaigns / NHTSA 캠페인

First-party [NHTSA Datasets and APIs](https://www.nhtsa.gov/nhtsa-datasets-and-apis) explicitly links a current recall-campaign file **`FLAT_RCL_POST_2010.zip`**, `FLAT_RCL_Qrtly_Rpts.zip`, and the separately published dictionaries `RCL.txt` and `RCL_Qrtly_Rpts.txt`.

- Explicit exact official files: `https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_POST_2010.zip`, `https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_Qrtly_Rpts.zip`, `https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt`, `https://static.nhtsa.gov/odi/ffdd/rcl/RCL_Qrtly_Rpts.txt`. These are link-discovery anchors only; **current binary readability not yet verified in canonical runner**.
- Official document establishes campaign-based lookup and separate quarterly reporting under 49 CFR Part 573. Campaign number is a *candidate join key*, not a proven exact identifier across the two ZIP bodies.
- F01 must validate exact campaign-number field equality, quarterly report time/order, backfilling, quantitative support and whether published quarterly status is an administrative process rather than actual repair. Do not convert recall rates to per-vehicle failure risk.
- **Access risk:** static host may block HEAD but allow bounded GET as was observed on FAA HTML; only real allowed binary test decides, never proxy/mirror/heuristic.

## C2 Census CBP × BLS QCEW / 고용 구조

- Official [Census CBP 2023 county CSV release](https://www.census.gov/data/datasets/2023/econ/cbp/2023-cbp.html) explicitly links a 12.7MB **County File** ZIP plus CSV layouts; Census [current data notice](https://www.census.gov/programs-surveys/cbp/data.html) still identifies **2023** as most recent reference year, and notes no firm 2024 release date due to methodology policy change. **Do not backfill or claim 2024 CBP exists**.
- Official [BLS QCEW direct files](https://www.bls.gov/cew/downloadable-data-files.htm) publish annual/quarterly county/industry NAICS CSVs, including 2024/2025 links, with downloadable schema; QCEW [Open Data Access](https://www.bls.gov/cew/additional-resources/open-data/home.htm) provides year/area/industry slices. Direct CSV requires **independent runtime acquisition test**, not assumed because listed.
- Exact five-character county FIPS and source-native NAICS vintages are *hypothesized* match fields: county-equivalent changes, industry aggregation 2-digit mapping, disclosure/suppression and ownership sectors may break exact comparability.
- Employment and payroll appear in **both** sources; future outcome must be temporally separated from structural exposure and not mechanically reuse overlapping fields. The stale Census 2024 CBP release may block a later truly prospective year, so fail closed.

## C3 NOAA Storm Events × BLS QCEW / 기상충격·고용

- Official [NOAA NCEI Storm Events database](https://www.ncei.noaa.gov/access/storm-events-database/) identifies nationwide storm reports and directs users to publicly accessible CSV or cloud-bucket bulk data; QCEW CSVs documented above.
- Source-native county ID, county-equivalent continuity, date/hazard classes, revisions and lagged labor coverage **must all be verified in true CSV bytes** before scores. No nearest-centroid or ad hoc county mapping if exact FIPS unavailable.
- Storm reports are a selected severe-weather reporting corpus, not comprehensive physical exposure or a natural experiment by default; subsequent employment association cannot be causal merely because storm dates precede QCEW.

## Canonical prior-route firewall / 기존 종료 연구 차단

- FAA terminal operational BLOCKED: [`US-FAA-AIR-F01/RESULT.md`](../US-FAA-AIR-F01/RESULT.md), three bounded official archive diagnostics and required 2020/2021 ZIP source inaccessible. No fourth workaround.
- Previous SEC adviser / CRA charity/FCC ULS / FDIC branch designs have terminal source/identity/balance failures; NONE of these exact routes was promoted into R58.
- R57 NHTSA *product-level engineering-platform* candidate was held for missing exact per-product denominator. R58 **campaign-ID/quarterly report** is a materially different *administrative* question; it must independently prove the identifier join and avoid a posthoc repair of product-level recall-risk denominators.
- E01 original NPI deactivation case and Issue #203 remain fully independent.

## Pre-score next gate / 채점 전 다음 게이트

**`CONTINUE_R58_SOURCE_BYTES_AND_EXACT_JOIN_PREFLIGHT`** — inspect only official metadata and safe schema/identity fields in a zero-cost canonical environment, with outputs stripped of case/company/person identifiers; fingerprint public source objects and verify source-native historical/temporal linkage. No candidate-specific future event membership, rates, uplift, ranking or scoring until its source access/identity/overlap audit is durable.

Source docs are **OBSERVED**; source-body access and exact joins are **UNVERIFIED**. No scores or F01 authorization. Cost **0 USD**.
