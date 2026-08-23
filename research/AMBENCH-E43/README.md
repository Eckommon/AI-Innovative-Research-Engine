---
id: AMBENCH-E43
type: source-grounded-path-order-only-thermal-benchmark
state: PREREGISTERED
created: 2026-08-24
source_of_truth: github
inherits:
  - AMBENCH-F42
  - DEC-084
custom_performance_observed_before_preregistration: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 — P01 Source-Grounded Path-Order-Only Thermal Benchmark
# AMBENCH-E43 — P01 Source-Grounded Path-Order-Only 열 Benchmark

## Purpose / 목적

Falsify whether the F41 unchanged-RHF risk order provides incremental melt-pool-width spatial stability relative to the **nominal P01 source-run order**, using the exact F42 matched transfer and pinned 3DThesis runtime.

This is intentionally **path/order only**. No history-informed power or timing controller is permitted in E43.

## Frozen runtime / 고정 runtime

- simulator: `ORNL-MDF/3DThesis`;
- commit: `2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`;
- standard GitHub-hosted Ubuntu runner only;
- CMake/OpenMP build;
- BSD-3-Clause upstream;
- solidification mode tracking: `Surface`;
- numerical solidification `Timestep = 1e-5 s`.

The `1e-5 s` timestep is frozen before performance because the pinned source default is `1e-5 s` and every F42 transferred source spot command has duration `10 us = 1e-5 s`.

If either case fails/does not finish under the standard-runner execution cap, assign HOLD. Do not reduce domain resolution, alter timestep, trim source commands or substitute a different runtime/commit after failure.

## Frozen source-transfer inputs / 고정 source-transfer 입력

Source and mapping are inherited unchanged from F42:
- NIST `mds2-2507` v1.0.1 P01;
- `RHF_Command.zip` SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- 25,051 source rows;
- 7,408 positive-power rows;
- 39 source-native positive runs;
- every positive source row -> one Mode=1 spot at exact translated XY for `10 us`, `Pmod=1`;
- same source-derived leading/trailing and 38 ordinal transition-duration slots;
- laser-on `0.07408 s`, laser-off `0.17643 s`, total `0.25051 s`;
- benchmark energy proxy at common 600 W = `44.448 J`;
- domain `X=[-1,4] mm`, `Y=[-1,3] mm`, `Z=[-1,0] mm`;
- resolution `50 um x 50 um x 25 um` => `101 x 81 x 41 = 335,421` grid points;
- upstream IN718 benchmark material constants and 600 W / 10 um Gaussian beam basis;
- output = `x,y,z,MP_width,MP_length,MP_depth` via `MP_Stats`.

### N0 — Nominal source order
`[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]`

Expected generated path SHA-256 from F42:
`7b2860908b2c96b167e1f383af5fa150b92184ad433e1ca9b3320dba68eeb475`.

### R1 — Frozen F41 RHF-risk order
`[5,39,6,18,24,22,20,21,23,25,27,17,16,28,29,15,14,13,30,26,31,7,32,19,12,11,33,34,10,8,9,38,35,36,37,1,3,2,4]`

Expected generated path SHA-256 from F42:
`778adef0041061f2413b35539798c3c5836b3290c1054e4c71b39f5dc689cd9b`.

Generated inputs must reproduce both hashes before simulation or E43 HOLDs.

## Frozen primary endpoint / 고정 1차 endpoint

E40 source-semantic correction applies permanently:

`MP_width` is the **per-grid-point maximum melt-pool-width spatial field**, not a temporal trajectory.

For each deterministic simulation independently:
1. retain finite `MP_width > 0` records only;
2. `mean_width = arithmetic mean(positive MP_width)`;
3. `SD_width = sample standard deviation(positive MP_width)`;
4. `CV_width = SD_width / mean_width`.

No grid row is treated as an independent replicate and **no row-level p-value** is allowed.

Also report:
- positive `MP_width` record count;
- maximum positive `MP_width`;
- final CSV row count;
- input hashes and budget invariants.

## Prospective materiality / 사전 materiality

Primary effect:

`improvement = 1 - CV_R1 / CV_N0`.

The following are prospective engineering heuristics, not universal physical thresholds:
- material CV improvement: `>= 10%`;
- mean-width preservation: `R1 mean_width / N0 mean_width` within `[0.95, 1.05]`;
- positive-width footprint preservation: `R1 positive_count / N0 positive_count` within `[0.90, 1.10]`.

The footprint constraint prevents an apparent CV gain produced mainly by collapsing or expanding the set of modeled melted grid points.

## Frozen gates / 고정 판정

### `PASS_E43_PATH_ORDER_ADDED_VALUE`
All must hold:
1. exact source/archive/runtime/input-hash integrity PASS;
2. both simulations complete under unchanged frozen settings;
3. both have at least `100` finite positive `MP_width` records;
4. `CV_R1 <= 0.90 * CV_N0`;
5. mean-width ratio in `[0.95,1.05]`;
6. positive-record-count ratio in `[0.90,1.10]`;
7. no post-result retuning/filter/endpoint switch.

### `PARTIAL_E43_PATH_ORDER_SMALL_GAIN`
Integrity/coverage/mean/footprint constraints pass and `CV_R1 < CV_N0`, but improvement is `<10%`.

### `NO_E43_PATH_ORDER_ADDED_VALUE`
Integrity/coverage pass but R1 fails to reduce CV, or mean/footprint preservation fails.

### `HOLD_E43_RUNTIME_OR_INTEGRITY`
Any required source/input hash, runtime completion, output schema, finite positive coverage (`>=100` each), or fixed-setting integrity condition fails.

## Forbidden adaptations / 금지 적응

E43 must not:
- add power modulation, variable timing, controller feedback or an optimizer;
- alter F41 order or F42 transfer mapping;
- reduce resolution/timestep/domain after runtime difficulty;
- filter spatial regions after seeing outputs;
- switch from `MP_width` to length/depth to rescue a result;
- use row-level pseudo-replication;
- claim NIST physical reproduction, scanner feasibility, novelty or production superiority.

## Reporting / 보고

Persist only:
- immutable source/runtime identity;
- generated input hashes and budget checks;
- output row/positive-record counts;
- frozen aggregate width metrics/ratios;
- final gate.

Do not commit upstream source, full generated paths, or raw simulator output CSVs.

## Cost / 비용

Standard public GitHub runner only; no GPU/larger runner/paid solver/API/data. Incremental monetary cost `0 USD`.
