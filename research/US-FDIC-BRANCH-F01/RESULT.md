---
id: US-FDIC-BRANCH-F01-RESULT
type: structural-feasibility-result
created: 2026-09-18
issue: 160
research: US-FDIC-BRANCH-F01
disposition: PASS
staging_commit: bfba6b52c8b09257d3430f6661b663779c23eb63
workflow_run: 35250781694
contract_commit: 6568d9bd0d897abb0bcabf8eaf04f2e54f50177f
gate: PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY
---

# US-FDIC-BRANCH-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY`**

The final immutable outcome-blind evidence passes **18/18** frozen requirements. Exact FDIC `UNINUMBR` provides sufficient historical physical-location continuity and ownership-change support for a separately preregistered N01 design.

최종 immutable outcome-blind evidence는 고정된 **18/18** 요구조건을 모두 통과했습니다. FDIC exact `UNINUMBR`는 별도 사전등록 N01 설계를 진행할 만큼 충분한 물리적 branch-location 종단 연속성과 소유권 변경 support를 제공합니다.

## Structural support / 구조적 support

- 2022–2024 structurally usable branch-year rows: **233,669**
- distinct valid `UNINUMBR`: **81,218**
- `UNINUMBR` observed in at least 2 of 3 years: **77,753**
- `UNINUMBR` observed in all 3 years: **74,698**
- exact `UNINUMBR` identities with historical `CERT` change: **2,499**
- historical identity-field validity: **100%**
- rows by year: 2022 **79,172** / 2023 **77,770** / 2024 **76,727**

These are structural feasibility facts only. They are not branch-closure, ownership-effect, prediction, causal, ranking, or novelty results.

## Implementation correction provenance / 구현 보정 계보

Attempt 01 preserved all historical empirical evidence but returned 17/18 because the implementation incorrectly required literal `UNINUMBR` text inside an unexpanded OpenAPI/JS transport payload for frozen requirement #8. That result remains immutable.

Correction `08403a21ef34462149b3a22228c3f3a02300b50f` changed **no scientific requirement or threshold**. Attempt 02 resolved only transport/schema evidence with an official 2025 SOD `HEAD` request requesting `YEAR,CERT,BRNUM,UNINUMBR`; the server returned HTTP 200 and **no response body was read**. Attempt 02 was committed at `bfba6b52c8b09257d3430f6661b663779c23eb63`.

## Future-outcome firewall / 미래 outcome 방화벽

No 2025 SOD data row, future branch membership, future History/Structure Change event membership, closure/non-continuation disposition, relationship, predictive metric, causal estimate, bank/branch ranking, or novelty result was opened or computed.

## Consequence / 후속 조치

This PASS authorizes **only** a separately preregistered outcome-blind `US-FDIC-BRANCH-N01` design stage. N01 must define exposure/comparator construction and future-disposition adjudication rules before any candidate future membership is opened. E01 remains unauthorized.

Incremental monetary cost: **0 USD**.
