---
id: US-MSHA-MINE-N01-RESULT
type: prospective-design-result
created: 2026-09-29
issue: 178
research: US-MSHA-MINE-N01
disposition: HOLD
attempt_01_commit: 8790f19866bb875b284738b8d465b1d0830b4293
attempt_01_run: 36548634237
contract_commit: 1d5f60ac0fca0aa81fad325bfc12e716ef370fec
gate: HOLD_US_MSHA_MINE_N01_PROSPECTIVE_DESIGN_NOT_READY
---

# US-MSHA-MINE-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_MSHA_MINE_N01_PROSPECTIVE_DESIGN_NOT_READY`**

The first pre-outcome cohort-lock execution is valid and passes **15/18** frozen design gates. Failed gates are **6, 11 and 14**. Future serious/fatal event membership remained unopened; therefore this is a design/support falsification, not an outcome result.

사전고정 N01 설계의 첫 실행은 유효하며 **15/18**을 통과했습니다. 실패 gate는 **6, 11, 14**입니다. 미래 serious/fatal event membership은 열지 않았으므로 이는 outcome 결과가 아니라 prospective design/support의 실패입니다.

## Failed frozen gates / 실패 gate

### Gate 6 — exposure-stratum support

Only **6** exact `COAL_METAL_IND × CURRENT_MINE_TYPE` strata met n≥40, below the frozen minimum **8**:

- C × Facility: 172
- C × Surface: 252
- C × Underground: 153
- M × Facility: 306
- M × Surface: 5,807
- M × Underground: 204

The stratum-count requirement may not be lowered after observation.

### Gate 11 — exposed match coverage

- RAMP_UP exposed mines: **1,722**
- accepted matched pairs: **964**
- coverage: **55.9814%**
- frozen threshold: **60.00%**

The 0.50-SD calipers, exact strata or comparator definition may not be relaxed after observing this result.

### Gate 14 — Q1 labor-intensity balance

Post-match baseline balance:

- X1 = ln(1 + Q1 hours): |SMD| = **0.01966** — PASS
- X2 = ln(1 + Q1 employees): |SMD| = **0.01740** — PASS
- X3 = ln(Q1 labor intensity): |SMD| = **0.12402** — **FAIL**
- frozen threshold: |SMD| ≤ **0.10**

The matching algorithm may not be retuned or rematched after this observation.

## Support that passed / 통과한 지원

- source fingerprints exactly equal the F01 frozen bytes
- eligible mines: **6,894** vs threshold 5,000
- RAMP_UP support: **1,722** vs threshold 1,000
- comparator support: **3,447** vs threshold 2,000
- prior severe history constructed only from frozen pre-cutoff rows
- matched pairs: **964** vs threshold 800
- historical six-month serious/fatal plausibility: **54** distinct eligible mines vs threshold 40
- future event membership opened: **false**
- future RR/RD/p-value/relationship computed: **false**
- prohibited identity repair used: **false**
- cost: **0 USD**

## Locked-cohort artifact status / cohort artifact 상태

The runner produced `locked-cohort.csv` with **964** pairs and SHA-256:

`94f7552c02222425c8da27bf7e82c3c0ace785e2e212dadcd18b6bc42a4e9c5a`.

Because the pre-outcome design failed 3 gates, this CSV is preserved only as immutable **negative design evidence**. It is **not an authorized prospective cohort**, may not be adjudicated against future outcomes, and may not be repaired or rematched.

## Consequence / 후속 조치

Do not open future serious/fatal membership for this exact N01. Do not lower the stratum threshold, reduce the match-coverage requirement, widen calipers, alter comparator ranks, remove exact-match factors or rematch to cure X3 balance.

Return to independent Stage-0 portfolio reselection. The MSHA F01 structural PASS remains valid, while this specific labor-intensity-ramp N01 is terminal negative evidence.

No E01 is authorized.

Incremental monetary cost: **0 USD**.
