---
checkpoint_id: CHK-20260914-US-BRIDGE-E01-ACTIVE
active_issue: 132
active_research: US-BRIDGE-E01
last_completed_issue: 131
last_completed_research: US-BRIDGE-N01
last_decision: DEC-180
updated: 2026-09-14
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_BRIDGE_E01_ACTIVE__PAIR_IDENTITY_REVALIDATION_FIRST`

US-BRIDGE-N01 / Issue #131 is terminal at `PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE`. Issue #132 / **US-BRIDGE-E01** is the sole intended active research experiment under DEC-180.

The E01 runner MUST validate the frozen N01 artifact before any NBI condition byte is sliced or decoded: 89,800 pairs, pair identity SHA-256 `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`, compressed artifact SHA-256 `4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3`, 15,245 CULVERT and 74,555 NON_CULVERT. Any mismatch is a pre-outcome fail-closed HOLD.

## Exact next action / 정확한 다음 행동

Execute the single frozen E01 runner. Only after identity PASS may it open Items 58/59/60/62, construct the preregistered deterioration indicators, retain complete matched pairs, run the exact two-sided McNemar/binomial test once, and apply the frozen +5pp / p<0.05 dispositions without rescue.

Incremental monetary cost remains **0 USD**.
