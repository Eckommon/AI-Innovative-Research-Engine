---
id: SOURCE-QUAL-CENSUS-USDA-Q04-RESULT
created: 2026-10-21
parent_issue: 244
prospective_contract_commit: 2dff1a76c99d5ac0699d21ddd0e0fa0a796eb1b5
actual_run: 39454161182
original_immutable_evidence_branch_commit: e87e4642b39aefaea14754b8b5fd6481b8d0c4bf
evidence_promoted_main_commit: fce69ef2b8fb9659d70457be93a5a2d6d9bb9329
disposition: PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN
incremental_monetary_cost_usd: 0
science_f01_authorized: false
---

# Census × USDA Q04 final D2 receipt / 이종 기관 원본·헤더 D2 최종 판정

**Terminal source-only decision / 원본검증 종결:** `PASS_Q04_DUAL_D2_HEADERS_ONLY__KEY_BRIDGE_UNPROVEN`. This is **not** a county geography bridge or science F01 PASS.

**Prospective integrity / 선행동결:** [Q04 CONTRACT](CONTRACT.md) merged at `2dff1a76c99d5ac0699d21ddd0e0fa0a796eb1b5` **before** either original source-body request. [Actual CI Run #39454161182](https://github.com/Eckommon/AI-Innovative-Research-Engine/actions/runs/39454161182) concluded SUCCESS; 11 Q04 + 9 persistence offline tests **20/20 PASS**, then two source GETs, then immutable per-run evidence branch push. [Exact original attempt JSON](evidence/attempt-01.json) was created on protected run-specific ref `refs/heads/evidence/s01/census-usda-q04/39454161182`, commit `e87e4642b39aefaea14754b8b5fd6481b8d0c4bf`, parent `c1a22c0c65e3ec0e294ffc3b4333c2507cdcd187`. An independent [evidence-only PR #271](https://github.com/Eckommon/AI-Innovative-Research-Engine/pull/271) promoted only JSON+MD onto canonical main `fce69ef2b8fb9659d70457be93a5a2d6d9bb9329`; no direct GitHub Actions `main` push occurred.

## Verified first-party raw source hashes / 실제 정부 원본 전체 바이트 지문

| Agency and version / 기관·자료 | Original bytes | Full raw SHA-256 | Actual original header |
|---|---:|---|---|
| U.S. Census 2024 national counties Gazetteer ZIP | 141,679 | `3c337402b5c6e8d5aa26b4278ccf4edc8989f2683765b3ffbf22296cdb2df3a0` | exact `GEOID`; ZIP member `2024_Gaz_counties_national.txt`, 647,830 uncompressed bytes |
| USDA ERS 2023 Rural-Urban Continuum Codes official CSV | 629,322 | `ec455ee2a8bc5fc8e070575ea5bee7dce46fc6037f8c3449cbf56e8b45331fa7` | exact `FIPS,State,County_Name,Attribute,Value` |

Both original bodies returned HTTP 200, had full SHA and byte count recorded before parsing, and only their **header tokens** were accessed. No records for individual counties, RUCC `Value`, names, coordinates, geographic overlap, effects, or raw objects persisted. USDA uses a **long-format Attribute/Value layout**; do not assume it is one record per county or collapse counties without a separate prospective key-grain contract.

**Geography caveat / 지리연혁 차이:** Census 2024 Gazetteer vintage and USDA 2023 RUCC classification can differ in boundary definitions and county-equivalent inclusions. Full-body source proof and having `GEOID`/`FIPS` columns do **not** certify same place, statistical comparison, unbiased sampling, or impact.

## Strict next action / 허용된 다음 단계

If pursuing source-identity feasibility, first **independently preregister** Q05 source SHA-vintage binding, exact `GEOID` vs `FIPS` string-normalization, long-format key repetition, exclusion and 2023/2024 geography limitations. Then only the fixed identifier fields may be read, no RUCC values, density, population, areas, lat/long or outcome selection. Q05 must use the live-proven independent evidence branch write and reviewed promotion. Failure in unchanged SHA or key integrity is terminal HOLD, no Q04 rescue.

Track A `INCONCLUSIVE_US_CMS_NPI_E01` terminal, closed; S01 Issue #244 remains sole active. Additional monetary cost **0 USD**.
