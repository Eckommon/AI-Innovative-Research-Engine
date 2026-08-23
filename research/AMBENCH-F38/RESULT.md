---
id: AMBENCH-F38-RESULT
type: prior-art-novelty-separation-result
state: COMPLETED
created: 2026-08-23
source_of_truth: github+public-primary-sources
incremental_monetary_cost_usd: 0
legal_novelty_verified: false
patentability_verified: false
obviousness_verified: false
---

# AMBENCH-F38 Result — Multi-Actuator History-Control Prior-Art / Novelty Separation
# AMBENCH-F38 결과 — Multi-Actuator History-Control 선행기술 / Novelty 분리

## Candidate combination / 후보 조합

`recent scan events → shared history/thermal state → coordinated actuator policy {laser power, turnaround/skywriting timing, local scan order/path} → melt-pool stability objective`

This audit is a bounded public-source research separation, **not** a legal patentability/FTO search.

## Source findings / 출처 결과

### A. Recent-scan / residual-heat / thermal-history state estimation — `KNOWN`

Authoritative prior art exists.
- Yeung & Lane (2020) RHF defines a residual-heat state from distance to prior scan points, elapsed time and prior laser power, then uses that state for process control.
- Path-level thermal models also explicitly reconstruct thermal history from manufacturing toolpaths and process parameters.

Disposition: `KNOWN_CORE`.

### B. History/temperature-informed laser-power modulation — `KNOWN`

Strong prior art exists.
- RHF directly modulates laser power from residual-history state.
- Earlier GCF work uses geometry/heat-accumulation proxies for power control.
- Real-time/pre-sintering temperature based laser-power control patents/publications predate F37.

Disposition: `KNOWN_CORE`.

### C. Thermal-history-informed scan path/order optimization — `KNOWN`

Prior art exists independently of F37.
- optimized scan strategies modify path/timing to reduce local heat accumulation;
- thermal-model-driven / temperature-state-driven scan sequence optimization selects next scan locations to improve thermal uniformity;
- path-level thermal modeling explicitly treats scan strategy as a determinant of thermal history.

Disposition: `KNOWN_CORE`.

### D. Timing/dwell/skywriting as thermal-control variable — `KNOWN`

Prior art exists.
- feedforward thermal-history work adjusts dwell time to mitigate heat buildup;
- patent disclosures use monitored/predicted interlayer temperature to alter dwell time, including combinations with laser power;
- scan-strategy literature modifies no-laser travel / inter-track timing to increase cooling time;
- skywriting timing is documented as materially affecting melt-pool morphology.

Disposition: `KNOWN_CORE`.

### E. Shared thermal state coordinating >=2 actuator classes — `KNOWN`

Strong two-actuator prior art exists.
- Riensche et al. (2022) uses graph-theory thermal simulation to identify heat buildup and changes **laser power + dwell time** for controlled processing.
- Patent family `WO2024026100A2` / corresponding US publication describes thermal-history prediction and correction using power and dwell, and states the underlying LPBF system can independently alter power, dwell, scan path and laser velocity.
- `US20240359237A1` describes real-time interlayer-temperature/model based mitigation using dwell time and laser power, with combinations of process variables contemplated.

Disposition: `KNOWN_MULTI_ACTUATOR_2PLUS`.

### F. Exact shared-state three-actuator `{power + timing + path/order}` coordination — `NOT IDENTIFIED IN BOUNDED SEARCH`

The bounded public search did **not** identify an authoritative pre-existing source that clearly discloses all of the following together as one material control architecture:
1. one shared recent-scan/thermal-history state estimator;
2. coordinated laser-power control;
3. coordinated timing/turnaround/dwell control;
4. coordinated local scan-order/path selection;
5. a joint policy/objective rather than merely listing the variables as independently adjustable machine settings.

However, this absence is weak evidence only because:
- A–E are densely occupied prior art;
- `WO2024026100A2` places power, dwell and scan path in the same controllable LPBF system and already jointly optimizes power+dwell from thermal-history predictions;
- thermal-state-driven scan-order optimization is separately known;
- combining adjacent known controls may face substantial obviousness/inventive-step risk;
- terminology and patent-family coverage in a bounded free search is incomplete.

Disposition: `BOUNDED_EXACT_COMBINATION_NOT_FOUND__HIGH_ADJACENT_PRIOR_ART`.

## Frozen A–F classification / 고정 분류

| Element | Result | Research implication |
|---|---|---|
| A history-state estimation | KNOWN | not differentiating |
| B history-informed power | KNOWN | not differentiating |
| C thermal-history-informed path/order | KNOWN | not differentiating |
| D adaptive timing/dwell/skywriting | KNOWN | not differentiating |
| E shared-state >=2 actuators | KNOWN | power+dwell already disclosed |
| F exact shared-state power+timing+path/order | NOT IDENTIFIED in bounded search | narrow research-gap candidate only |

## Frozen F38 gate / 고정 F38 판정

**`NOVELTY_PARTIAL_GAP_F38`**

Meaning:
- the exact three-actuator shared-state architecture was not identified in this bounded public search;
- nearly every constituent and a material two-actuator thermal-state control architecture are already known;
- therefore the remaining gap is **narrow** and carries **high adjacent-prior-art / obviousness risk**.

Mandatory status remains:
- `LEGAL_NOVELTY_UNVERIFIED`;
- `PATENTABILITY_UNVERIFIED`;
- `OBVIOUSNESS_UNVERIFIED`;
- `FREEDOM_TO_OPERATE_UNVERIFIED`.

## Research value vs novelty / 연구가치와 novelty 분리

F37's mechanism convergence remains useful even if legal novelty ultimately fails. The research question can be reframed from “is multi-actuator history control new?” to the falsifiable engineering question:

> Does **joint** control of power + timing + local path/order from one recent-history state materially outperform strong known baselines such as history-informed power-only, power+dwell, or thermal-state scan-order control under equal productivity/quality constraints?

This added-value question is not answered by the current evidence and is the more defensible next research target.

## Exact next action / 정확한 다음 행동

**AMBENCH-F39 — Multi-Actuator Added-Value Falsification Design Gate.**

Before prototype spending, freeze a zero-cost experiment/simulation design comparing:
1. constant control baseline;
2. history-state power-only (RHF-like);
3. history-state power + timing/dwell;
4. history-state path/order-only;
5. joint history-state power + timing + path/order.

Require matched thermal-history state definition, productivity constraint and melt-pool stability/quality endpoints. The joint controller must show incremental value over the strongest known two-actuator comparator, not merely over constant parameters.

## Public source record / 공개 출처 기록

Key primary/patent families used in the bounded separation:
- Yeung & Lane, 2020, `A residual heat compensation based scan strategy for powder bed fusion additive manufacturing`, DOI `10.1016/j.mfglet.2020.07.005` / NIST publication record;
- Riensche et al., 2022, `Feedforward control of thermal history in laser powder bed fusion: Toward physics-based optimization of processing parameters`, DOI `10.1016/j.matdes.2022.111351`;
- patent family `WO2024026100A2` / `US20260097434A1`, `Feedforward control of laser powder bed fusion`;
- `US20240359237A1`, `Determination and mitigation of anomalous interlayer temperature in manufacturing processes`;
- Liu et al., 2022, optimized scanning strategy for short-scan heat accumulation, DOI `10.1016/j.addma.2022.103256`;
- thermal-state/scan-sequence optimization literature used only to establish that C is occupied prior art.

## Cost / capability / 비용

Incremental monetary cost `0 USD`. No paid patent database/API was used. No Skill/MCP/Plugin promotion; workflow remains `SHARED-INTERNAL-CANDIDATE`.
