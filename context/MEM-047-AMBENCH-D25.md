---
id: MEM-047-AMBENCH-D25
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
research: AMBENCH-D25
last_decision: DEC-052
---

# MEM-047 — AMBENCH-D25 durable memory / D25 영속 메모리

## Final gate / 최종 판정
`D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`

## Reproduction / 재현
D25 exactly reproduced E24 representation and coverage:
- 36/40 part×block units;
- 9/10 blocks; Block 1 excluded;
- beta `0.015305236`;
- predictor partial R² `0.019321313`.

## Outcome variance / Outcome 분산
- part-only R² `0.000602`;
- block-only R² `0.998820`;
- part+block R² `0.999421`;
- block|part partial R² `0.999421`;
- part|block partial R² `0.509735` of the tiny post-block remainder;
- residual fraction after part+block `0.000579`.

## Predictor structure / Predictor 구조
- part-only R² `0.747172`;
- block-only R² `0.205094`;
- part+block R² `0.952265`;
- residual fraction `0.047735`.

## Sign structure / 부호 구조
- pooled beta `-0.278047`;
- part-adjusted `-1.026589`;
- block-adjusted `-0.022349`;
- part+block-adjusted `+0.015305`;
- `STRUCTURAL_SIGN_REVERSAL=YES`;
- `BLOCK_REMOVAL_EXPLAINS_REVERSAL=NO`.

All four part-specific x↔y Spearman diagnostics are negative. The small positive E24 beta is a fully adjusted residual estimand, not the dominant build-level relationship.

## Decision / 결정
`DEC-052`: stop same-representation escalation on `mds2-3761`. No feature fishing, endpoint switching, or nonlinear/high-capacity rescue attempt. Next route should qualify an independent-condition / independently varied dataset or experiment before another mechanistic test.

## Exposure / 사전노출
Inherited `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`. D25 added no new feature/endpoint selection.

## Cost / 비용
Incremental monetary cost `0 USD`. No paid/potentially paid route used.