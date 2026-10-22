---
id: SOURCE-QUAL-CENSUS-USDA-Q06-RESULT
created: 2026-10-23
parent_issue: 244
preregistered_contract_commit: 120930e4bb234ba0c6e652df1c9713fc94e3a2a6
original_run_id: 39837664450
original_evidence_branch_commit: 492e8d2e3db68b847e4a3972d27d0af97a06ab8e
evidence_promotion_main_commit: 9d84f6f1ed16ed6b9f6e25d2e6ec1aa03d7c5469
disposition: PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED
science_f01_authorized: false
incremental_monetary_cost_usd: 0
---

# Census 2024 × USDA 2023 Q06 — first-party Island Areas source-scope terminal verdict / 13개 불일치 원본 포함범위 최종 판정

**Actual preregistered source-only disposition / 원본 포함범위 판정:**
`PASS_Q06_ALL_13_EXPLAINED_BY_DOCUMENTED_ISLAND_AREA_SCOPE__BOUNDARY_EQUIVALENCE_UNVERIFIED`.

## Immutable real execution / 실제 검증

- [Frozen Q06 contract](CONTRACT.md) was merged on main at `120930e4bb234ba0c6e652df1c9713fc94e3a2a6` **before inspecting the unmatched key prefix groups**.
- [Original Actions Run #39837664450](https://github.com/Eckommon/AI-Innovative-Research-Engine/actions/runs/39837664450) **SUCCESS**. **12/12** Q06 offline tests + **9/9** immutable branch-persistence safeguards passed **before** the original first-party source reads.
- Census Gazetteer 2024 original: HTTP 200, **141,679 bytes**, SHA-256 `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0`. USDA RUCC 2023 original: HTTP 200, **629,322 bytes**, SHA-256 `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7`. All exact Q04/Q05 frozen source digests and sizes matched **before any row IDs were inspected**.
- Original [immutable JSON receipt](evidence/attempt-01.json) and [bilingual Markdown receipt](evidence/attempt-01.md) were pushed to unique run-only ref `refs/heads/evidence/s01/census-usda-q06/39837664450`, commit `492e8d2e3db68b847e4a3972d27d0af97a06ab8e`, parent `10161c2225a5bf683fdda0dcef1fdb5a604adad6`. Independent [two-file-only evidence PR #282](https://github.com/Eckommon/AI-Innovative-Research-Engine/pull/282) promoted the exact receipts to canonical main `9d84f6f1ed16ed6b9f6e25d2e6ec1aa03d7c5469`. No raw bytes, county names, individual 5-digit FIPS, RUCC attributes/values, area, coordinates or effects persisted.

## Precommitted four-excluded-territory codebook / 네 외곽 영토 범위

| Frozen jurisdiction FIPS prefix | Official territory name / 지명 | USDA-only unique county-code keys |
|---|---|---:|
| `60` | American Samoa / 아메리칸사모아 | **5** |
| `66` | Guam / 괌 | **1** |
| `69` | Northern Mariana Islands / 북마리아나제도 | **4** |
| `78` | U.S. Virgin Islands / 미국령 버진아일랜드 | **3** |
| **Total / 합계** | | **13** |

All **13/13** original USDA-only FIPS keys from Q05 fall within the **four predefined** jurisdiction prefixes; there are **zero** unmatched keys outside them, zero Census-2024 keys with excluded prefixes, and no Census-only keys. Q05 invariants were independently reverified exactly: Census **3,222**, USDA **3,235**, source-native syntax overlap **3,222**, **52** distinct shared state/territory prefixes, **6,468** repeated USDA FIPS rows, **zero** invalid code rows and **zero** Census duplicate identifiers.

Sources for prospective territorial definition:
- Official [Census 2024 Gazetteer](https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2024.html) excludes those four Island Areas and includes Puerto Rico (`72`).
- Official [USDA 2023 RUCC documentation](https://www.ers.usda.gov/data-products/rural-urban-continuum-codes/documentation) includes 3,235 county equivalents across U.S. states, Puerto Rico and outlying territories.
- [Census ANSI geographic code lists](https://www.census.gov/library/reference/code-lists/ansi.html) provide the four prespecified jurisdiction identifiers.

## Strictly unproven claims / 금지된 추론

**Coverage difference resolved, geographic boundary equivalence NOT verified.** Shared five-character codes do **not** prove 2023 USDA and 2024 Census geography is spatially identical, do not establish independent RUCC `Attribute`/`Value` grain and never identify a rural/business/health effect. In particular USDA 2023 documentation references Connecticut's 2022 planning-region changes, and 2024 Census Gazetteer warns against assuming one-to-one geographic equivalence across vintages. A separately frozen Q07 official source/vintage and semantic bridge is required **before any further source row or outcome access**.

Track A `US-CMS-NPI-E01` is terminal `INCONCLUSIVE_US_CMS_NPI_E01` and Issue #203 CLOSED. FEMA×EPA Q01/HOLD, Q02 D2 and Q03 terminal operational HOLD are preserved. Sole source-registry Issue #244 remains OPEN, checkpoint `CHK-20261020-SOURCE-REGISTRY-S01-ACTIVE`, `DEC-324` unchanged. **New monetary cost: 0 USD.**
