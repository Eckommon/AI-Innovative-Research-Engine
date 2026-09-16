# PORTFOLIO-R30 Process Nonconformity / 절차 비적합 기록

Date: 2026-09-16

## What happened / 발생 내용

The durable candidate/scoring contract and source revalidation were committed before scoring, as required:

- candidate/scoring contract commit: `faf01cbe5a114f69bf96fdafa075521aa619662b`
- source revalidation commit: `540f27da69d109a6b731b3d41d02eb5a99c29252`

However, the scorecard was then committed at:

- scorecard commit: `e848a6c77920aa7e31eb1e1038e4f9914cbc6b7e`

**before a dedicated GitHub Issue number had been bound to R30.** The intended README order said to bind a dedicated R30 Issue and then score.

## Scientific/evidence impact assessment / 과학·증거 영향

This is an orchestration-order nonconformity, not an outcome-leakage event:

- the candidate pool was already frozen before scoring;
- the 9-dimension rubric and tie-break were already frozen before scoring;
- source/access/overlap facts used for scoring were already durably recorded before the scorecard;
- no candidate outcome magnitude or candidate-specific relationship was opened;
- no score was changed after seeing an outcome;
- the scorecard is now immutable for R30 and must not be re-scored merely to repair process ordering.

## Corrective rule / 교정 규칙

1. Create and bind the dedicated R30 Issue now.
2. The Issue must explicitly reference all three pre-issue commits above.
3. Treat the existing scorecard as the sole R30 scorecard; do not modify candidate scores after Issue binding.
4. Finalization may ratify the frozen scorecard only if the Issue reproduces the same candidate pool, rubric, tie-break, source boundary and no-outcome condition.
5. Future portfolio rounds must create the Issue immediately after the candidate/rule contract and before any scorecard commit.

No candidate outcome was opened. Incremental monetary cost remains 0 USD.
