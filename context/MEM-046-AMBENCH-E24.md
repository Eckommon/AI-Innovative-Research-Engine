---
id: MEM-046-AMBENCH-E24
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# MEM-046 — AMBENCH-E24 controlled experiment

## Durable memory / 영속 메모리
- E24 is the first preregistered numerical experiment on checksum-verified/headerless-mapped `mds2-3761` after F23.
- Primary: col16 `melt_pool_area_t100_mm2` → col40 `xct_voxel_mean5`.
- Hierarchy: raw row → part×layer median → ten fixed 25-layer blocks; part/block fixed effects.
- Coverage: 36/40 eligible part×block units, 9/10 included blocks; Block 1 excluded by frozen rule.
- Primary beta `0.015305`; full R² `0.999432`; predictor partial R² `0.019321`; 20,000-draw block permutation p `0.007900`.
- t80 beta `0.016772`, partial R² `0.025308`; t120 beta `0.017831`, partial R² `0.021048`; no material sign disagreement.
- +25-layer shift: beta `0.011634`, partial R² `0.009379`; locality criterion PASS.
- Part-specific Spearman rhos all negative: `-0.460255`, `-0.268917`, `-0.483333`, `-0.694567`; do not equate these with the fixed-effect estimand.
- Frozen final gate: `NO_MATERIAL_E24_ASSOCIATION` because primary partial R² < 0.05.
- Inherited exposure remains `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`.
- Do not feature-fish or escalate model capacity on the same registered representation.
- Next: preregistered diagnostic decomposition of part/block dominance and sign reversal before deciding on a new independent experiment.
- Incremental monetary cost: `0 USD`; any potentially billable future route still requires explicit prior approval.