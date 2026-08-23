---
id: AMBENCH-F37
type: cross-experiment-mechanism-audit
state: PREREGISTERED_ACTIVE
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F37 — Scan-History / Turnaround / RHF Cross-Experiment Mechanism Convergence Audit
# AMBENCH-F37 — Scan-History / Turnaround / RHF 교차실험 Mechanism Convergence Audit

## Purpose / 목적

Audit whether three already-completed controlled evidence strands support one bounded **path-dependent thermal-history mechanism class**, or whether their apparent directional agreement is only superficial.

Frozen evidence set:
1. `AMBENCH-E29` — AMB2025-07 IN718, 0.75 ms vs 5.0 ms turnaround, physical-plate P1 overlap-depth endpoint;
2. `AMBENCH-E33` — IN625, converging/diverging opposite scan histories under equivalent programmed track lengths, width primary + area sensitivity;
3. `AMBENCH-E36` — IN625 RHF experiment, constant-power baseline vs residual-history-informed variable-power conditions, part-level melt-pool-area variability.

No additional favorable experiment may be added after seeing the F37 audit outcome.

## Frozen audit dimensions / 고정 감사 차원

Each dimension is `PASS / PARTIAL / FAIL / UNKNOWN`:

1. **Experiment independence** — distinct physical experiments/datasets and independent physical units.
2. **Mechanism relevance** — intervention/design actually changes or encodes elapsed/spatial prior-scan thermal history, not merely a correlated label.
3. **Intervention triangulation** — evidence spans materially different levers (turnaround timing, scan-order/history, history-conditioned power control).
4. **Directional coherence** — outcomes are consistent with stronger/uncompensated residual-history exposure changing melt-pool geometry or variability, and history compensation reducing instability.
5. **Measurand triangulation** — evidence is not restricted to one identical derived metric.
6. **Material/context breadth** — more than one alloy/experimental context contributes, while preserving domain-shift boundaries.
7. **Causal isolation** — alternative design differences are sufficiently controlled to claim one common causal mechanism rather than only mechanism-class consistency.
8. **Exposure/verification integrity** — preregistration/exposure limitations are disclosed and verified results, not unexecuted claims, are used.

## Frozen gates / 고정 gate

### `PASS_F37_BOUNDED_MECHANISM_CLASS_CONVERGENCE`
Requires:
- dimensions 1–5 and 8 = PASS;
- dimensions 6–7 at least PARTIAL;
- no experiment direction contradicts the mechanism-class interpretation;
- resulting claim is explicitly **mechanism-class convergence**, not same-construct replication or universal causality.

### `PARTIAL_F37_DIRECTIONAL_CONVERGENCE_ONLY`
Multiple experiments agree directionally, but one or more of dimensions 2–5 is only PARTIAL or causal/measurand differences are too large for mechanism-class convergence.

### `HOLD_F37_SEMANTIC_OR_SOURCE_CONFLICT`
A material source/claim semantic conflict prevents a reliable audit.

### `REJECT_F37_COMMON_MECHANISM`
At least one strong verified experiment contradicts the proposed common mechanism class or evidence collapses to the same non-independent source construct.

## Innovation translation boundary / 혁신 전환 경계

If F37 PASSes, it may generate a **research innovation hypothesis**, not a novelty/patent/commercial claim:

> A shared recent-scan-history state estimator may be usable to coordinate multiple process actuators — laser power, turnaround/skywriting time, and local scan order — to stabilize melt-pool geometry under path-dependent heating.

This hypothesis must be classified as `NOVELTY_UNVERIFIED`. RHF/history-based power control already exists in prior art; F37 cannot claim that history-aware control itself is new.

Any subsequent novelty/competitive/patent search must be a separate source-audit step.

## Cost / capability / 비용

Zero incremental monetary cost only. No new Skill/MCP/Plugin promotion; workflow remains `SHARED-INTERNAL-CANDIDATE`.
