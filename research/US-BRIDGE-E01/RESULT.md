---
id: US-BRIDGE-E01-RESULT
type: preregistered-matched-pair-outcome-test
created: 2026-09-14
issue: 132
workflow_run: 34796095655
gate: NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-E01 Result / 결과

**`NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP`**

## Preregistered execution integrity / 사전등록 실행 무결성

- N01 pair identity was revalidated **before** condition access: **YES**.
- Frozen pair count: **89,800**.
- Pair identity SHA-256: `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`.
- Compressed pair artifact SHA-256: `4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3`.
- Frozen class counts: `CULVERT=15,245`, `NON_CULVERT=74,555`.
- All NBI ZIP/member hashes matched the N01 source manifest before each source's condition fields were used.
- No post-value rescue, alternative threshold, alternative outcome, one-sided test or model substitution was used.

## Primary frozen result / 주 분석 결과

- Complete analyzable matched pairs: **89,719 / 89,800 (99.9098%)**.
- Analyzable `CULVERT`: **15,239**; `NON_CULVERT`: **74,480**.
- Exposed deterioration: **9,625 / 89,719 = 10.727939%**.
- Control deterioration: **11,152 / 89,719 = 12.429920%**.
- Risk difference `exposed - control`: **-1.7020 percentage points**.
- Paired cells `(exposed, control)`: `00=70,371`, `10=8,196`, `01=9,723`, `11=1,429`.
- Discordant pairs: **17,919**.
- Exact two-sided McNemar/binomial p-value: **0.0000000000000000000000000000038729315284838527299511746654322881580031536420307**.
- Frozen positive materiality floor: **+5pp**; frozen significance gate: **p < 0.05**.

## Interpretation boundary / 해석 경계

The preregistered positive relationship was not established. The observed RD is negative, but this design does **not** authorize the reversed claim that disasters protect bridges. The result is an association under county-level FEMA exposure timing and matched NBI inspection intervals, not a causal effect. Maintenance/repair responses, inspection ascertainment, exposure misclassification, disaster severity, aging, traffic/environment and other unobserved interventions remain unresolved.

## Exact next action / 정확한 다음 행동

Return to Stage 0 independent-candidate comparison. Do not rescue US-BRIDGE post hoc and do not reinterpret the negative RD as evidence that disasters protect bridges.

Incremental monetary cost: **0 USD**.
