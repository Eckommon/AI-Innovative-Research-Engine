---
id: AMBENCH-F37-RESULT
type: cross-experiment-mechanism-audit-result
state: COMPLETED
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F37 Result — Bounded Path-Dependent Thermal-History Mechanism Convergence
# AMBENCH-F37 결과 — 제한된 Path-Dependent Thermal-History Mechanism Convergence

## Frozen evidence set / 고정 근거 집합

### E29 — Turnaround-time intervention / turnaround-time 개입
- source: NIST `mds2-4103` / AMB2025-07, IN718;
- independent unit: physical plate, n=3 vs n=3;
- intervention: `0.75 ms` vs `5.0 ms` turnaround;
- endpoint: P1 reconstructed overlap depth;
- result: `Delta_primary = +29.083049409 µm`, exact one-sided permutation `p=0.05`, plate rank-biserial `1.0`;
- gate: `PASS_E29_STRONG_DIRECTIONAL_EFFECT`.

Mechanism relevance: shorter turnaround reduces elapsed cooling time between adjacent-track events, directly manipulating one temporal component of recent thermal history. E29 itself does not directly measure residual heat and therefore cannot alone establish residual heat as the unique cause.

### E33 — Opposite prior-scan-history design / 반대 prior-scan-history 설계
- source: NIST `mds2-3662` v1.0.1, IN625;
- independent structure: 18 equivalent-programmed-length reverse pairs, with three physical repeats per direction/location and nested operator measurements;
- design: converging/diverging scan strategies create opposite prior-track histories for equivalent programmed track lengths;
- width result: Spearman `rho=+1.0`, two-sided permutation `p=9.999900001e-06`, 18/18 valid;
- area sensitivity: `rho=+0.997936016512`, same p;
- gate: `PASS_E33_GEOMETRY_MATCHED_HISTORY_ASSOCIATION` with `CROSS_MEASURAND_STRENGTHENING`.

Mechanism relevance: directly encodes accumulated prior-track count/history, but the reverse pairs are equivalent programmed lengths rather than same XY locations. Thus design/context differences are reduced but not eliminated.

### E36 — Residual-history-informed power-control intervention / residual-history 기반 power-control 개입
- source: NIST `mds2-2507` v1.0.1, IN625;
- independent unit: 55 physical parts;
- process-input groups: five constant-power baselines vs 50 RHF variable-power parts;
- endpoint: part-level melt-pool-area variability, one SD per physical part;
- result: baseline median variability > RHF median variability; one-sided 100,000 label-permutation `p=0.0124798752012`; frozen block stability 5/5 positive;
- gate: `PASS_E36_EXTERNAL_RHF_VARIABILITY_REDUCTION`.

Mechanism relevance: RHF explicitly computes a control state from temporal/spatial prior-scan history and modulates power accordingly. Publication-level direction was already known, and the parameter sweep is not randomized causal assignment.

## Frozen dimension audit / 고정 차원 감사

| Dimension | Verdict | Evidence / Boundary |
|---|---|---|
| 1. Experiment independence | **PASS** | Three distinct NIST experiment/dataset identities (`mds2-4103`, `mds2-3662`, `mds2-2507`) with different physical-unit structures. |
| 2. Mechanism relevance | **PASS** | E29 changes elapsed turnaround time; E33 changes prior-track history through scan order; E36 explicitly encodes temporal/spatial prior history into RHF control. |
| 3. Intervention triangulation | **PASS** | Independent levers span timing, path/order, and laser-power modulation. |
| 4. Directional coherence | **PASS** | Shorter cooling/history exposure corresponds to larger geometry in E29; increasing relative prior history corresponds monotonically to geometry difference in E33; history-informed compensation corresponds to lower variability in E36. No verified directional contradiction. |
| 5. Measurand triangulation | **PASS** | Evidence spans reconstructed overlap depth, top-surface width/area, and within-part melt-pool-area variability rather than one identical derived metric. |
| 6. Material/context breadth | **PARTIAL** | IN718 (E29) and IN625 (E33/E36) contribute, but all are NIST laser-scanning/bare-plate-family experiments; machine/task/context breadth is not sufficient for universal transfer. |
| 7. Causal isolation | **PARTIAL** | E29 has a direct timing contrast but small plate n; E33 is not same-XY and retains scan-strategy context differences; E36 is a nonrandomized RHF parameter sweep. Common mechanism is not uniquely isolated from every alternative. |
| 8. Exposure/verification integrity | **PASS** | All three use executed, checksum/source-verified durable results. E27/E33/E36 publication/schema exposure events remain disclosed; no pristine-blindness claim is made. |

## Falsification checks / 반증 점검

### Same-construct replication?
**REJECTED.**
- E29 tests turnaround time and overlap depth;
- E33 tests scan-history contrast and surface melt-pool geometry;
- E36 tests residual-history-informed power control and within-part variability.

They cannot be pooled as one effect size or labeled direct replication.

### One unique causal mechanism proven?
**NOT ESTABLISHED.**
The experiments are consistent with a shared path-dependent thermal-history mechanism class, but none of the cross-experiment synthesis eliminates all geometry, machine, measurement and controller differences.

### Directional contradiction?
**NONE FOUND in the frozen evidence set.**
No completed strong result requires the opposite qualitative interpretation.

## Frozen F37 gate / 고정 F37 판정

**`PASS_F37_BOUNDED_MECHANISM_CLASS_CONVERGENCE`**

Reason:
- dimensions 1–5 and 8 PASS;
- material/context breadth and causal isolation are PARTIAL rather than FAIL;
- timing, scan-order/history and history-conditioned power-control interventions triangulate a common path-dependent recent-scan-history mechanism class without being mislabeled as direct replication.

## Research innovation hypothesis / 연구 혁신 가설

### `HYP-F37-01 — Multi-Actuator Recent-Scan-History Control`

**NOVELTY_UNVERIFIED.**

A shared recent-scan-history state estimator may be able to coordinate multiple process actuators — at minimum:
1. laser power,
2. turnaround/skywriting time,
3. local scan order/path selection,

to stabilize melt-pool geometry against path-dependent heat accumulation.

Conceptual architecture:

`recent scan events → history state H(t,x,y) → actuator policy {power, turnaround, local path/order} → melt-pool stability objective`

Evidence-to-component mapping:
- E29 supports turnaround time as a thermally relevant actuator candidate;
- E33 supports scan order/prior-track history as a state/trajectory variable;
- E36 supports history-conditioned power as an effective control actuator class.

## Critical novelty boundary / 핵심 novelty 경계

History-aware/RHF-based power control is already prior art and is explicitly represented in E36's source publication. Therefore F37 does **not** claim that history-conditioned control, RHF, or feedforward laser-power compensation is new.

The potentially differentiating hypothesis is the **joint/shared state estimator + multi-actuator coordination** across power, timing and path/order. Its novelty, patentability, feasibility and superiority are completely unverified.

## Exact next action / 정확한 다음 행동

**AMBENCH-F38 — Multi-Actuator History-Control Prior-Art / Novelty Separation Gate.**

Before any prototype or commercialization claim:
1. search authoritative papers/patents/standards for joint power + timing/skywriting + scan-order control driven by shared thermal-history state;
2. distinguish existing RHF/GCF/feedforward/thermal-history control from the F37 multi-actuator combination;
3. identify which elements are known, obvious combinations, genuinely unresolved, or unsupported;
4. produce `NOVELTY_REJECTED / NOVELTY_PARTIAL_GAP / NOVELTY_SEARCH_INCONCLUSIVE` only — no patentability claim without a separate legal-grade search.

## Cost / capability / 비용

Incremental monetary cost `0 USD`. No capability promotion beyond `SHARED-INTERNAL-CANDIDATE`.
