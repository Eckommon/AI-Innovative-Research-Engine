---
id: US-FAA-AIP-F01-RESULT
type: structural-feasibility-result
created: 2026-09-17
issue: 154
research: US-FAA-AIP-F01
disposition: HOLD
staging_commit: e194c692251f867fd378d052f2ccb51001ada1a4
contract_commit: 4f9a2a3491bc00c0fd1e00a7b0d3bc0bc62d4254
gate: HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY
---

# US-FAA-AIP-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY`**

The immutable outcome-blind structural run passed **16 of 17** frozen requirements. The only failed requirement was the preregistered state-concordance gate: **1,196 / 1,245 = 96.0643%**, below the frozen **99%** threshold. Exactly **49** state conflicts were excluded without repair.

고정된 17개 요구조건 중 **16개가 PASS**했고, 유일한 실패는 사전등록한 state-concordance gate였습니다. **1,196 / 1,245 = 96.0643%**로 고정 기준 **99%**에 미달했습니다. **49개** state conflict는 수동·퍼지 보정 없이 제외했습니다.

## Structural support retained / 구조적 지지

- official FAA AIP FY2021–2025 files readable: **5 / 5**
- valid AIP rows: **16,691**
- distinct valid AIP LocIDs: **2,314**
- exact bounded FAA↔BTS bridged airports: **1,196**
- bridged airports in BTS on-time identity universe: **390**
- bridged airports appearing in >=2 AIP fiscal years: **1,146**
- bridged airports with FY2023–2025 grant support: **1,134**
- longitudinal BTS identity stability after ambiguity exclusion: **100%**
- potential subsequent-year support through 2026: **390**

These counts do not override the failed frozen state-concordance gate.

## Transport correction provenance / 전송 구현 교정

The first two executions failed before scientific evaluation because FAA pages/assets returned HTTP 403 to the GitHub-hosted runner. No threshold or identity rule changed. The successful immutable run used the same frozen contract and the same official FAA workbook assets with a browser-compatible request profile. This was an implementation-only transport correction, not a scientific rescue.

## Outcome firewall / 결과변수 방화벽

No BTS delay, cancellation, diversion or delay-cause numeric outcome value was opened or aggregated. No relationship, predictive metric, causal claim, airport ranking, project-effectiveness estimate or grant-conditioned delay statistic was computed. No fuzzy/name/address/geospatial/manual identity repair was used.

## Consequence / 후속 조치

`US-FAA-AIP-N01` is **not authorized**. The 99% state-concordance threshold must not be lowered and the 49 conflicts must not be manually rescued after support counts are known. This branch terminates and the project returns to an independent portfolio reselection.

Incremental monetary cost: **0 USD**.
