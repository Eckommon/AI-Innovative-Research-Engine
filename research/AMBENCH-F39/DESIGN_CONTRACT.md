---
id: AMBENCH-F39-DESIGN-CONTRACT
type: controller-comparison-design-contract
state: FROZEN_PRE_PERFORMANCE
created: 2026-08-23
source_of_truth: github
controller_performance_observed_before_freeze: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F39 Design Contract — Common-State, Matched-Budget C0–C4
# AMBENCH-F39 설계 계약 — Common-State, Matched-Budget C0–C4

## 1. Purpose / 목적

Freeze an executable, low-DOF comparison in which the only material difference among history-aware controllers is **which actuator classes consume the same feedforward recent-scan-history state**.

This is a simulation falsification benchmark, not a direct physical replication of E29/E33/E36.

## 2. Runtime / 실행환경

- simulator: `ORNL-MDF/3DThesis`;
- immutable upstream commit: `2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`;
- license: BSD-3-Clause;
- standard GitHub Ubuntu runner, CMake/OpenMP;
- corrected runtime preflight: `PASS_F39_RUNTIME_ENVIRONMENT_EXECUTES`;
- upstream source remains transient; no third-party source is vendored.

3DThesis path syntax natively encodes path/order, per-segment power multiplier (`Pmod`), line velocity and spot duration. Upstream documentation also exposes temperature-history and melt-pool `MP_Stats` width/length outputs.

## 3. Thermal benchmark / 열 benchmark

The first added-value test is deliberately a **source-native semi-analytic thermal benchmark**, not an IN625 validation claim.

Material constants are frozen to the upstream IN718 example / Stump–Plotkowski benchmark values already present in pinned 3DThesis:
- `T0 = 1273 K`;
- `TL = 1610 K`;
- `k = 26.6 W/(m K)`;
- `c = 600 J/(kg K)`;
- `rho = 7451 kg/m3`.

Beam file starts from the pinned upstream example:
- nominal beam power `P0 = 600 W`;
- upstream example beam widths/depth `10e-6 m`;
- efficiency `1.0`.

Benchmark path:
- one layer / surface raster;
- 21 parallel hatches;
- hatch spacing `0.1 mm`;
- laser-on hatch length `3.0 mm`;
- nominal laser-on velocity `1.0 m/s`;
- canonical C0 order = increasing hatch index with serpentine direction;
- 20 inter-hatch transitions;
- nominal transition dwell budget `D0 = 0.75 ms` per transition, total `15 ms`.

The 3 mm × 2 mm / 0.1 mm hatch layout and RHF state parameters below are taken as a benchmark abstraction from the NIST RHF study. The thermal material/beam model is the pinned 3DThesis benchmark, so no claim of quantitative reproduction of that NIST physical experiment is allowed.

## 4. One common feedforward history state / 하나의 공통 feedforward history state

State definition is the published Residual Heat Factor form from Yeung & Lane (2020):

`H_i = sum_{k in S_i} ((R-d_ik)/R)^2 * ((T-t_ik)/T) * L_k`

where `S_i` contains prior nominal C0 scan-command points within spatial radius `R` and elapsed-time window `T`.

Freeze:
- `R = 0.29 mm`;
- `T = 6 ms`;
- nominal C0 history uses constant laser power;
- nominal laser path is discretized at `10 us` intervals for state construction;
- normalized state `H_N = min(H/(mean(H)+std(H)), 1)`.

**Critical fairness rule:** `H_N` is computed once from the nominal C0 schedule before any controller simulation and is then frozen as the identical feedforward state field used by C1–C4. It is not recomputed from each controller's realized thermal outcome. Therefore C4 cannot gain advantage from a different/better state estimator.

Track risk used by timing/path controllers:
`r_j = mean(H_N values assigned to nominal C0 laser-on points of hatch j)`.

All ties use ascending original hatch index.

## 5. Frozen controllers / 고정 controller

### C0 — Fixed baseline
- `Pmod = 1` for all laser-on segments;
- canonical increasing-index serpentine hatch path;
- each inter-hatch zero-power positioning event has dwell `D0 = 0.75 ms`.

### C1 — History-state power only
Raw RHF-shaped multiplier:
`q_i = 1 - 0.25 * H_N(i)`.

To remove total-energy advantage/disadvantage, energy-neutralize prospectively:
`Pmod_i = q_i / mean_timeweighted(q over all laser-on commands)`.

Because all laser-on command intervals have equal duration, the time-weighted mean is the arithmetic mean. The resulting total commanded laser-on energy equals C0 exactly.

Timing and path remain C0.

### C2 — History-state power + timing/dwell
Power schedule = C1.

For the transition before hatch `j` (`j=2..21`), let the risk be `r_j`. Freeze:
`d_j = D0 * [1 + (r_j - mean(r_2..r_21))]`.

Properties by construction:
- each `d_j` is non-negative because `r_j in [0,1]`;
- each `d_j <= 2*D0 = 1.5 ms`;
- `sum(d_j) = 20*D0 = 15 ms` exactly.

Thus C2 redistributes a fixed cooling-time budget toward higher nominal history risk but cannot add total build time.

Path remains C0.

### C3 — History-state local path/order only
- power = C0;
- total timing budget = C0 with uniform `D0` transitions;
- hatch order = ascending `r_j`, tie-break by original hatch index;
- each hatch keeps its canonical laser-on direction assigned by original hatch parity.

To isolate scan order, the benchmark represents each inter-hatch repositioning as a zero-power positioning event with the same fixed dwell `D0`, independent of geometric jump distance. This is an explicit thermal-benchmark abstraction and is **not** a scanner-kinematics model.

### C4 — Joint shared-state power + timing + path/order
- power schedule = C1;
- timing schedule = C2, attached to the risk identity of the next hatch;
- hatch order = C3.

No additional parameter, state estimator, optimization loop or controller-specific model is allowed.

## 6. Matched constraints / 동일 제약

Across C0–C4:
- same material and heat-source model;
- same 21 physical hatch segments and hatch spacing;
- same laser-on nominal velocity and total laser-on duration;
- same total commanded laser-on energy (C1/C2/C4 energy-neutralized; C0/C3 fixed at 1);
- same total transition dwell time = `15 ms`;
- same domain/resolution/output settings;
- same state field `H_N` for C1–C4;
- no controller sees 3DThesis output while its path file is generated.

## 7. Primary output / 1차 output

Primary is the simulator's documented `MP_Stats` **maximum melt-pool width trajectory**.

Treat the trajectory as one deterministic simulation outcome, not as independent repeated samples. No row-level p-value is allowed.

Frozen scalar stability metric:
`CV_width = sample_SD(positive MP_Stats width values) / mean(positive MP_Stats width values)`.

The positive-value rule is frozen before controller execution because zero/no-melt records are not width observations. Also report:
- mean positive width;
- maximum positive width;
- number of positive width records;
- total modeled process time;
- total commanded laser-on energy proxy.

If the pinned runtime cannot expose the documented MP_Stats width field for the custom benchmark, do **not** switch endpoint: hold the performance experiment for schema correction.

## 8. Added-value falsification gate for the descendant execution / 후속 실행 판정

Primary comparator = **C2**, not C0.

### `PASS_E40_JOINT_CONTROL_ADDED_VALUE`
All must hold:
1. source/runtime/controller integrity gates PASS for all C0–C4;
2. total laser energy and total transition-dwell budgets match by construction and verified generated inputs;
3. C4 `CV_width <= 0.90 * C2 CV_width` (at least 10% stability improvement over the strong two-actuator comparator);
4. C4 mean positive width remains within ±5% of C2 mean width, preventing trivial stability by collapsing the melt pool;
5. C4 CV_width is not worse than both C1 and C3;
6. no endpoint/controller retuning after results.

### `PARTIAL_E40_JOINT_CONTROL_SMALL_INCREMENT`
C4 improves over C2 but by <10%, while integrity and mean-width constraints hold.

### `NO_E40_JOINT_CONTROL_ADDED_VALUE`
C4 fails to improve over C2 or violates the mean-width constraint.

### `HOLD_E40_RUNTIME_OR_OUTPUT_SCHEMA`
Runtime/input/output integrity does not support the frozen comparison.

The 10%/5% thresholds are prospective engineering materiality heuristics, not source-derived universal thresholds.

## 9. Claim boundary / 주장 경계

Even a future E40 PASS would establish only **incremental value in this pinned semi-analytic thermal benchmark**. It would not establish physical-machine superiority, patent novelty, IN625/IN718 universality, scanner-kinematic feasibility or production readiness.

## 10. Cost / 비용

Standard public GitHub runner only, no paid API/solver/cloud/GPU. Incremental monetary cost `0 USD`.
