---
id: US-EIA-GEN-F01-RESULT
type: structural-feasibility-result
created: 2026-09-17
issue: 156
research: US-EIA-GEN-F01
disposition: HOLD
staging_commit: 3cc19e706fa341c7bf27b919f8abd9e07855292d
contract_commit: 140715aecd58bf5371f7c0a6a46feccf761d9457
gate: HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY
---

# US-EIA-GEN-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY`**

The immutable outcome-blind run passed **17 of 18** frozen requirements. The only failed requirement was gate 8: the January-2024 Planned snapshot contained **664** eligible 2024–2025 planned solar generator keys, below the prospectively frozen minimum of **1,000**.

고정된 18개 요구조건 중 **17개가 PASS**했고, 유일한 실패는 gate 8입니다. 2024-01 Planned snapshot의 2024–2025 계획 태양광 generator key는 **664개**로 사전고정한 최소 **1,000개**에 미달했습니다.

## Strong structural support that does not override HOLD

- COLOCATED focal solar generators: **95**
- STANDALONE focal solar generators: **569**
- distinct COLOCATED Plant IDs: **92**
- states containing both exposure classes: **15**
- focal exact-key ambiguity rate: **0%** / unambiguous rate **100%**
- valid planned month/year: **100%**
- positive finite nameplate capacity: **100%**
- plant-state consistency: **100%**
- manifest SHA-256: `095cb0a34ab94c37253cc3051ca6d4c849a4cf3d4870195b1e8f16197f1ccfe6`

These facts show a clean and potentially useful cohort, but they cannot retroactively reduce the frozen 1,000-unit requirement.

## Future-outcome firewall

The December-2025 official workbook was fingerprinted and inspected only for workbook/sheet/header structure. No future data row, generator membership, status value, actual-operation date, schedule change, commissioning-slippage metric, relationship, prediction, causal estimate, plant/developer ranking or novelty claim was opened/computed.

## Consequence / 후속 조치

`US-EIA-GEN-N01` is **not authorized** under this branch. The 1,000-unit gate must not be lowered after observing the 664-unit cohort, and the exposure window may not be broadened post hoc to rescue this F01. Return to independent portfolio reselection or a separately preregistered new candidate/branch whose design is not conditioned on this outcome.

Incremental monetary cost: **0 USD**.
