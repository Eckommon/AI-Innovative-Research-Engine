# US-CMS-NPI-E01 — Alternatives to passive CMS weekly-release waiting / CMS 주간 공개 대기 대안 검토

**Assessed / 검토:** 2026-10-16 KST  
**Scope / 범위:** Scientific source equivalence, legitimate official-channel early detection, and independent parallel research.  
**Status / 상태:** OPERATIONAL_RESEARCH_ASSESSMENT_ONLY — E01 WAIT_SOURCE UNCHANGED  
**Frozen E01 contract:** `48843c9979336dcd10fdff984f458277062d6f20`  
**Active issue:** [#203](https://github.com/Eckommon/AI-Innovative-Research-Engine/issues/203)  
**Cost boundary:** `COST-001`, **0 USD incremental**; seek user approval before any cost-bearing option.

## Conclusion / 결론

**KO:** E01 최초 적격 공식 CMS NPPES V2 주간 증분 자료를 다른 제품·API·제3자 추정자료로 **대체해 동일 사전등록 실험을 실행할 수는 없다**. 그러나 출처 공개 여부를 더 일찍 **메타데이터 수준에서 확인**하거나 **별도 신규 연구를 병렬 추진**해 프로젝트의 연구 생산성을 유지하는 것은 가능하다. 346,859쌍, 사건정의, 18개 게이트, 사전등록 통계 기준과 E01의 불변 원본은 바꾸지 않는다.

**EN:** There is no evidenced equivalent source that makes the frozen E01 first eligible *weekly incremental* analysis executable before the official CMS weekly is released. Do not substitute a different source or manufacture early outcome evidence. Legitimate metadata-only detection improvements and a separate explicitly preregistered parallel study remain available; these cannot be promoted as E01.

## Officially documented source distinctions / 공식 출처별 차이

| Route / 경로 | Officially supported facts / 공식 확인 내용 | E01 equivalence / E01 동등성 | Action / 권고 |
|---|---|---|---|
| CMS [NPPES V2 weekly ZIP listing](https://download.cms.gov/nppes/NPI_Files.html) | Official weekly incremental; initial historical anchor `100526_101126`, last authenticated program watch 2026-10-15 20:58 KST showed 0 future eligible weekly | **Only approved frozen E01 target**, after separate first-publication adjudication | Keep current six-hour metadata-only watch |
| **Official ZIP URL / HTTP HEAD metadata probe** | A tentative **future filename** can be derived from the *historical official filename pattern* (for example `NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip`); filename/URL **not verified to exist**. A compliant `HEAD` request, if server supports it, can inspect status/Content-Length/Last-Modified/ETag/Date **without downloading ZIP** | **Not independently sufficient** to certify weekly issuance, HTML listing, file content, first-publication order, or release approval | Possible separately logged zero-cost *early warning* only after week ends; no bulk scans or access-control circumvention; treat 200/404/405/403 as operational metadata, no scientific PASS |
| [NPI Registry / official CMS API](https://npiregistry.cms.hhs.gov/api-page) | CMS says registry queried daily, no cost for registry viewing; registry itself explicitly restricts queries/hour since 2024-06-25 and says **bulk queries must use DDS file** | **Not equivalent** to a weekly **population-wide deactivation incremental** or to 346,859 matched-pair outcome release | At most a low-volume, rules-compliant, independently specified descriptive pilot; do not bulk-query locked cohort or fill E01 outcomes |
| [CMS monthly full and deactivation ZIPs](https://download.cms.gov/nppes/NPI_Files.html) | Official, free monthly distribution and a monthly deactivation report. The frozen 2026-10-12 monthly baselines are already locked in the E01 runner | Monthly ZIP is **baseline**, not a future incremental 2026-10-12..18 V2 weekly | Do not substitute or extend event horizon after outcome |
| [Data.CMS.gov data API](https://data.cms.gov/api-docs) | Official CMS open datasets/API endpoints are **dataset-specific**, rather than a universal alias of NPPES weekly incrementals | **No identified identical NPPES weekly outcome** | Use only for separately specified cross-dataset hypothesis after field/schema/population comparison |
| Third-party mirrors or copied CMS download indices | May reproduce or lag official materials; provenance/update time and exact byte identity not guaranteed | **Not primary E01 first-publication authority** | Independent reference/alert only if provenance verifiable; never silently replace CMS ZIP |

**Additional official source:** CMS [Data Dissemination](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination) explicitly describes the **daily-updated query-only NPI Registry** and **weekly incremental NPPES downloads** as different mechanisms; weekly files cover newly assigned, updated, and newly deactivated NPIs, and are supplemental to monthly full replacement. Official [NPI Registry](https://npiregistry.cms.hhs.gov/) explicitly warns of hourly query limits and DDS-for-bulk requirement. The [CMS FAQ](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/bulk-upload-reviewing-updating-digital-contact-information-national-plan-provider-enumeration-system) confirms availability of an NPI Registry API as a query interface. These official materials do **not** demonstrate an early bulk future-outcome feed.

## Recommended two-track execution / 권장 이중 트랙

**Track A — Protect and detect / 기존 E01 보존·조기 탐지**

1. Preserve **Issue #203** as the only active E01 scientific checkpoint and keep the unchanged `tools/run_us_cms_npi_e01.py`, 18 scientific gates, baseline, exact ZIP transport and source-release procedure.
2. Continue the verified `watch-us-cms-npi-e01-source.yml` official **HTML-only** watcher. Actual GitHub cron dispatch has lagged by multiple hours; its timestamp must **not** be equated with CMS publication time.
3. Optionally add a **separate metadata-only HEAD experiment** targeting a clearly marked *hypothesized* URL **after the relevant coverage week ends**, in a no-cost and low-frequency manner. It must not open/download ZIP contents, update `source-candidate-01`, mutate Issue execution marker, or claim source approval. **No HTTP HEAD result has been verified in this assessment**; no automated probing was deployed by this decision.
4. Upon an officially listed first future V2 weekly, lock the earliest **observed** candidate, independently adjudicate preceding publication chronology and possible missed/withdrawn earlier weeks, match exact official ZIP URL and committed raw candidate SHA, then authorize E01 **once**. Insufficient chronology remains `HOLD_SOURCE_LINEAGE_REVIEW`, not a fabricated PASS.

**Track B — Keep the mission advancing / 병렬 독립 연구**

Conduct a separate portfolio **reselection / candidate feasibility screen**, using only already published public data and pre-outcome rules, under a **different, explicitly separate research identifier and Issue** if governance allows. Complete F01 source/license/join and structural preflight *before* accessing outcome distributions. Do not label API sampled/descriptive findings as the frozen E01 result, cherry-pick a posthoc positive from 346,859 pairs, or mutate the sole canonical active E01 checkpoint. The next parallel study must be selected from portfolio rules rather than presumed to be CMS-equivalent.

## Not authorized / 현재 승인되지 않은 행위

- Guessing and fetching unpublished or unlisted ZIP **bodies**, evading access restrictions, scraping the NPI Registry at bulk scale, or using a commercial API without cost/rights verification.
- Retrospectively substituting a monthly file, a later week, a third-party mirror, registry spot checks or another CMS enrollment program for the frozen E01 future endpoint.
- Claiming `PASS_US_CMS_NPI_E01_SOURCE_RELEASE_LOCK`, statistical significance, medical closure/quality, or actual data-source availability without verified original evidence.
- Modifying `context/checkpoint.json`, `STATUS.md`, `context/SESSION_HANDOFF.md`, the E01 science runner or the Issue execution marker based on this alternatives assessment alone.

## Evidence / 참조

1. CMS NPPES [official file listing](https://download.cms.gov/nppes/NPI_Files.html), source product separation and V2 announcement.
2. CMS [Data Dissemination](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination), registry daily vs weekly incremental semantics, weekly supplemental to monthly.
3. NPI Registry [official search](https://npiregistry.cms.hhs.gov/), query limits since 2024-06-25 and explicit DDS requirement for bulk.
4. CMS [digital contact information FAQ](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/bulk-upload-reviewing-updating-digital-contact-information-national-plan-provider-enumeration-system), official registry/API/downloading pathways.
5. [Data.CMS.gov API documentation](https://data.cms.gov/api-docs), separate data-catalog architecture.
6. Internal exact research gate: `research/US-CMS-NPI-E01/SOURCE_RELEASE_PROCEDURE.md`; immutable preflight `research/US-CMS-NPI-E01/evidence/source-preflight-03.json`; official live scheduled GitHub Actions runs `38684815636` and `38731182357` (last CMS HTML observed at 2026-10-15 20:58 KST with zero qualifying future weeklies).

**Disposition / 판정:** `CONTINUE_E01_WAIT_SOURCE_AND_ALLOW_SEPARATE_PARALLEL_FEASIBILITY`, **not** `PASS_US_CMS_NPI_E01`. No added cost or raw future-outcome access.
