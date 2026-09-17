---
id: US-FDIC-BRANCH-N01-RESULT
type: outcome-blind-matched-design-result
created: 2026-09-18
issue: 161
research: US-FDIC-BRANCH-N01
disposition: HOLD
staging_commit: 074df7191d38970e3082cb846fd7a397dfe30ce9
workflow_run: 35251883997
contract_commit: c0f9f412b88b4ff54fd9999ff57fc3c4be40f374
gate: HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE
---

# US-FDIC-BRANCH-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE`**

The first valid immutable outcome-blind N01 run passed **15 of 18** frozen requirements. The exact design is terminal HOLD because all three prospectively frozen baseline-balance gates failed.

최초 유효 immutable outcome-blind N01 실행은 고정된 18개 요건 중 **15개를 PASS**했습니다. 그러나 사전고정한 baseline-balance gate 3개가 모두 실패했으므로 이 exact design은 terminal HOLD입니다.

## Strong support that does not override HOLD / HOLD를 뒤집지 않는 강한 support

- historically eligible stable-ownership branches: **70,113**
- eligible exact `CERT × STALPBR` strata (`n >= 8`): **1,650**
- deterministic matched DECLINE–GAIN pairs: **13,874**
- states/territories represented: **52**
- same-year exact-ID conflicts: **0**
- strict trajectory separation: PASS
- exact same-bank/same-state pairing: PASS
- duplicate `UNINUMBR` across pairs: none
- pair-manifest SHA-256: `c8256947e131df0ae7f98f59f43afb862327e9c782e7db2778ab2fe87b5a2fe8`

## Frozen balance failures / 고정 balance 실패

1. 2022 within-stratum deposit-share ratio within `[1/3, 3]`: **68.4950%** < frozen **75%**.
2. 2022 absolute branch-deposit ratio within `[1/3, 3]`: **68.4950%** < frozen **75%**.
3. 2023 absolute branch-deposit ratio within `[1/3, 3]`: **73.4684%** < frozen **75%**.

The design has abundant cardinality, but the prospectively required baseline comparability is not met. The 75% thresholds, matching order, quartile definitions, and strata may not be relaxed after observing these results.

## Future-outcome firewall / 미래 outcome 방화벽

No 2025 SOD row, future branch membership, future BankFind structure-event membership, closure/non-continuation disposition, relationship, prediction, causal estimate, bank/branch ranking, or novelty result was opened or computed.

## Consequence / 후속 조치

`US-FDIC-BRANCH-E01` is **not authorized**. Do not rescue this N01 by widening the balance ratio, lowering 75%, changing quartiles, changing the matching order, or redefining strata after observing the results. Return to independent portfolio reselection or a separately preregistered new branch/design that is not conditioned on future outcomes.

Incremental monetary cost: **0 USD**.
