---
id: US-MINE-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-16
issue: 135
workflow_run: 35006086876
gate: HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT
pair_identity_sha256: e2fde0b16457f0b50397b638c96a363a9a0dcca6d4c9ccd49cba5d744f9ba116
incremental_monetary_cost_usd: 0
---

# US-MINE-N01 Result / 결과

**`HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT`**

## Frozen design execution / 고정 설계 실행

The preregistered `ALL_SECTOR_OPERATOR_HOURS_RAMP_UP` design executed without opening the Accidents source or any injury outcome. F01 Mines and quarterly-employment source hashes reproduced exactly before exposure magnitudes were used.

사전등록한 `ALL_SECTOR_OPERATOR_HOURS_RAMP_UP` 설계를 사고 데이터·부상 outcome을 열지 않은 상태에서 실행했다. Exposure magnitude 사용 전 F01 Mines 및 quarterly-employment source hash가 정확히 재현됐다.

## Outcome-blind integrity / 결과 비개봉 무결성

- Accidents source read: **NO**.
- Injury outcome values opened: **NO**.
- Coal-production magnitude parsed: **NO**.
- Exposure→injury relationship computed: **NO**.
- Post-execution threshold/matching rescue: **NO**.
- Incremental monetary cost: **0 USD**.

## Exposure-only support / exposure-only 지원

- Eligible mines with >=1 positive-hours `(t-1,t,t+1)` sequence: **15,179**.
- Eligible three-quarter observations: **260,038**.
- First-role Coal candidates: exposed **809**, control **457**.
- First-role Metal/Nonmetal candidates: exposed **7,796**, control **5,442**.
- Deterministic 1:1 pairs: **2,084**.
- Pair coverage: Coal **214**, Metal/Nonmetal **1,870**, **49 states**.
- Pair identity fingerprint: `e2fde0b16457f0b50397b638c96a363a9a0dcca6d4c9ccd49cba5d744f9ba116`.

## Why the frozen gate is HOLD / HOLD 이유

Two preregistered requirements failed:

1. `coal_pairs_ge_300` — only **214** Coal pairs were identified against the frozen minimum of **300**.
2. `sector_matches_mines` — **60** mine-quarter records had a historical quarterly-employment sector that did not equal the current Mines-snapshot sector identity under the strict frozen comparison.

All other frozen requirements passed, including >=2,000 total pairs and >=30-state coverage. Nevertheless the contract is conjunctive: these two failures prevent PASS or E01 authorization.

사후에 Coal 최소쌍 기준을 낮추거나, 60개 mismatch를 결과를 본 뒤 새 규칙으로 재분류하지 않는다. Doing either would be a post-support rescue.

## Interpretation boundary / 해석 경계

This HOLD does **not** show that operator-hours ramp-up is unrelated to mine injuries. Injury outcomes were never opened. It means only that the exact N01 design, as preregistered, failed its own support/identity gate.

No positive, negative, protective, sector-specific or causal injury claim is authorized.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Do not open US-MINE-E01 from this N01 and do not rescue the branch by lowering the Coal-pair threshold or rewriting sector identity after support was observed. A future independent design may revisit historical sector semantics only as a separately selected, prospectively registered mission.

Incremental monetary cost remains **0 USD**.
