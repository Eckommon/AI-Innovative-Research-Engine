---
id: AMBENCH-F41
type: nondegenerate-path-order-source-gate
state: PREREGISTERED
created: 2026-08-24
source_of_truth: github
inherits:
  - DEC-082
  - AMBENCH-F35
incremental_monetary_cost_usd: 0
---

# AMBENCH-F41 — Non-Degenerate Path/Order Intervention Source Gate
# AMBENCH-F41 — 비퇴화 Path/Order 개입 Source Gate

## Purpose / 목적

After F39/E40 showed that a uniform synthetic raster collapses C3→C0 and C4→C2, test whether an **independently existing public process-input path** contains source-native reorderable scan units whose risks are non-degenerate under the unchanged published RHF state.

This is a source/input-design gate only. No simulator performance and no physical outcome value may be used.

## Frozen source / 고정 source

Primary and only F41 candidate:
- NIST dataset `mds2-2507`, version expected `1.0.1`;
- checksum-frozen `RHF_Command.zip` expected SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- physical baseline part: **P01**, previously command-verified as constant-positive-power baseline;
- documented command schema: headerless `X,Y,Power,Trigger`;
- documented command timestep: `10 us`.

No P02–P55 condition is substituted if P01 fails this gate.

## Source-native scan unit extraction / source-native scan unit 추출

A **scan run** is frozen as a maximal contiguous sequence of command rows with `Power > 0`, bounded by file boundaries or one/more rows with `Power <= 0`.

Rules:
- do not split a positive-power run by geometry, curvature, distance, direction or desired result;
- do not merge runs separated by laser-off rows;
- retain original run order;
- each run must contain at least 2 positive-power command rows to be eligible;
- if fewer than 4 eligible runs exist, assign `REJECT_F41_NO_REORDERABLE_SOURCE_UNITS`.

This definition is fixed before opening P01 row content in F41.

## Unchanged RHF state / 변경 없는 RHF state

Use the F39 published-state contract unchanged:

`H_i = sum_{k in S_i} ((R-d_ik)/R)^2 * ((T-t_ik)/T) * L_k`

with:
- `R = 0.29 mm`;
- `T = 6 ms`;
- P01 baseline constant-positive power represented as `L_k = 1` for positive-power prior rows;
- elapsed time from original command-row index × `10 us`, including laser-off rows in elapsed time;
- only earlier positive-power rows contribute;
- `H_N = min(H/(mean(H)+population_SD(H)), 1)` over all positive-power command rows.

Run risk:
`r_run = mean(H_N over positive-power rows in that source-native run)`.

## Numerical stability / 수치 안정성

64 ULP at the run-risk scale is a numerical equality guard, not a research materiality threshold. Risks whose differences are inside this guard are treated as tied; ties preserve original run order.

## Frozen source gate / 고정 source 판정

### `PASS_F41_NONDEGENERATE_PATH_ORDER_SOURCE_READY`
All must hold:
1. exact archive identity/checksum PASS;
2. exact P01 command member uniquely resolved;
3. >=4 eligible source-native scan runs;
4. run-risk range `max(r_run)-min(r_run) >= 0.05` on normalized `[0,1]` RHF scale;
5. stable risk sort (ties by original run id) produces an order different from nominal;
6. no source-semantic repair or parameter retuning is required.

The `0.05` risk-range threshold is a prospective engineering distinctness heuristic, not a universal physical threshold.

### `PARTIAL_F41_WEAK_PATH_RISK_SEPARATION`
Source integrity and >=4 runs pass, and stable risk sorting differs from nominal, but risk range is > numerical tie guard and <0.05.

### `REJECT_F41_NO_REORDERABLE_SOURCE_UNITS`
Fewer than 4 eligible source-native runs.

### `REJECT_F41_PATH_RISK_DEGENERATE`
>=4 runs exist but risks are numerically tied or stable risk ordering remains nominal.

### `HOLD_F41_SOURCE_OR_SCHEMA_CONFLICT`
Required archive/member/schema/timing identity cannot be verified without reinterpretation.

## Anti-rescue / 사후구제 금지

F41 must not:
- use outcome/MPM/microscopy/analysis-result values;
- substitute a different PXX after P01 fails;
- split/merge runs based on desired risk variation;
- change `R`, `T`, normalization or risk aggregation;
- introduce a geometric heuristic or optimizer to manufacture a non-nominal order.

## Next / 다음

Only a PASS may authorize a separately preregistered descendant path/order controller benchmark. PARTIAL/REJECT must not trigger performance execution; it instead informs whether another independently preregistered source gate is justified.

## Cost / 비용

Public NIST command input + standard GitHub runner only. Incremental monetary cost `0 USD`.
