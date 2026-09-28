---
id: US-HUD-MF-N01-RESULT
type: outcome-blind-design-result
created: 2026-09-28
issue: 169
research: US-HUD-MF-N01
disposition: HOLD
attempt_01_commit: a18d9a1dd157cde5f393312831f500d0939513f7
workflow_run: 36395660448
contract_commit: 01c5a19215a30572c74309cd5b1dbe9851880224
gate: HOLD_US_HUD_MF_N01_MATCHED_INSPECTION_DESIGN_NOT_IDENTIFIABLE
---

# US-HUD-MF-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_HUD_MF_N01_MATCHED_INSPECTION_DESIGN_NOT_IDENTIFIABLE`**

Immutable Attempt 01 is a valid outcome-blind execution and passes **17/18** frozen requirements. Gate 15 fails because post-match balance for `log1p(UNITS)` is **|SMD| = 0.178049**, above the prospectively frozen **0.15** threshold.

Attempt 01은 유효한 outcome-blind 실행이며 **17/18**을 통과했습니다. 그러나 `log1p(UNITS)`의 post-match |SMD|가 **0.178049 > 0.15**이므로 exact N01은 terminal HOLD입니다.

## Strong support that did pass / 통과한 구조 support

- exact active FHA projects reproduced: **15,632**
- deterministic property-linked projects: **15,425**
- deterministic latest pre-cutoff inspection property IDs: **23,865**
- eligible baseline cohort: **8,247** (threshold 7,000)
- frozen linear quantiles: **Q25 = 87**, **Q75 = 97**
- LOW candidates: **2,151**
- HIGH candidates: **2,116**
- matched pairs: **1,438** (threshold 1,200)
- matched states: **50** (threshold 20)
- matched SOA categories/sub-categories: **16** (threshold 8)
- pair-manifest SHA-256: `65426aa525f0caab7544aefa8ba3259d087ea5eb5db35a27989b440d80ad812b`
- projects reused across pairs: **0**

## Frozen balance result / 고정 balance 결과

Absolute post-match SMD:

- `balance_ratio`: **0.05656**
- `interest_rate`: **0.01718**
- `log1p_original_mortgage`: **0.08708**
- `months_to_maturity`: **0.05606**
- `log1p_units`: **0.17805 — FAIL**

Exact state and exact SOA balance both passed by construction.

The observed near-miss does not authorize rematching, a caliper, another distance metric, propensity-score substitution, variable removal, threshold relaxation or exposure redefinition. Those changes would be post-observation rescue.

관측된 근소한 balance 실패를 이유로 caliper·다른 거리함수·propensity model·변수삭제·threshold 완화·노출재정의를 적용하지 않습니다.

## Outcome firewall / 결과 방화벽

- post-2026-09-21 terminated rows opened: **0**
- future adverse membership opened: **false**
- future entity-body bytes consumed: **0**
- relationship/prediction/ranking/causal metric computed: **false**
- incremental monetary cost: **0 USD**

No future event feedback contributed to the HOLD.

## Consequence / 후속 조치

This HOLD does **not** authorize `US-HUD-MF-E01`. The exact HUD matched-inspection design is terminal negative design evidence. Return to independent Stage-0 portfolio reselection rather than rescuing the same design.

이 HOLD는 E01을 허가하지 않습니다. 동일 설계를 사후 조정하지 않고 독립적인 Stage-0 portfolio reselection으로 복귀합니다.

Incremental monetary cost: **0 USD**.
