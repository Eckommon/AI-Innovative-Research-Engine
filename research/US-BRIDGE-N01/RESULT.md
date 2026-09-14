---
id: US-BRIDGE-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-14
issue: 131
gate: PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-N01 Result / 결과

**`PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE`**

## Frozen design support / 고정 설계 지원

- Unique bridges with >=1 eligible consecutive interval: **619,599**.
- Unique exposed bridges under FEMA `DR` physical-hazard timing: **494,625**.
- Unique control-candidate bridges with no exposed eligible interval: **124,974**.
- Deterministic matched exposed-control pairs: **89,800**.
- Matched state/territory FIPS: **52**.
- Matched `CULVERT` pairs: **15,245**.
- Matched `NON_CULVERT` pairs: **74,555**.
- Matched pairs with interval-length difference <=365 days: **97.8140%**.
- Exact pair-identity fingerprint: `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`.
- Pair identities: `research/US-BRIDGE-N01/PAIR_IDENTITIES.jsonl.gz` using canonical JSONL compressed after fingerprinting.

## Outcome-blind integrity / 결과 비개봉 무결성

Condition Items 58/59/60/62 were not opened and their fixed-width row bytes were not sliced. No bridge-condition deterioration indicator, rate, change, p-value or disaster-linked relationship was calculated. Matching used only the preregistered bridge/county/date/class/reconstruction/cadence design fields and FEMA `DR` event identity. No fuzzy repair or outcome-dependent inclusion was used. Raw source bytes remained transient.

## Interpretation boundary / 해석 경계

This result establishes only whether the preregistered temporal exposed/control design is identifiable. It is not evidence that disasters worsen or improve bridge condition. Static hazard mapping and generic NBI deterioration prediction remain outside any novelty claim.

## Exact next action / 정확한 다음 행동

Open a separate US-BRIDGE-E01 authorization that reproduces the exact N01 pair fingerprint before opening condition values; then execute only the prospectively frozen deterioration/McNemar contract.

Incremental monetary cost: **0 USD**.
