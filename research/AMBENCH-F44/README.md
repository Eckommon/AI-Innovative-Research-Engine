---
id: AMBENCH-F44
type: runtime-representation-equivalence-gate
created: 2026-09-03
status: PREREGISTERED
predecessor: AMBENCH-E43
source_dataset: mds2-2507
simulator: ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60
incremental_monetary_cost_usd: 0
capability_status: SHARED-INTERNAL-CANDIDATE
---

# AMBENCH-F44 — Surface-Only MP_Stats Representation Equivalence Gate
# AMBENCH-F44 — Surface-Only MP_Stats 표현 동등성 Gate

## Purpose / 목적

E43 ended `HOLD_E43_RUNTIME_OR_INTEGRITY` because the exact 335,421-point representation timed out at the prospectively frozen 480 s N0 runtime cap. F44 does **not** rescue or reinterpret E43. It separately tests whether pinned 3DThesis's documented `Z Num=1` top-surface representation preserves the top-surface `MP_width` field needed by the path-order question.

No E43 N0-vs-R1 performance comparison exists and none is used here.

## Upstream semantic basis / upstream 의미 근거

Pinned 3DThesis documents that a Z domain with `Num 1` uses only the Z `Max` value. Its `Solidify_Surface` implementation tracks liquid points on the surface, then separately evaluates melt depth below them. In pinned `Melt::calc_mp_info`:

- the seed grid layer is explicitly `z_grid_num = sim.domain.znum - 1`;
- local melt-pool search preserves the same k layer;
- width and length are calculated only from x/y coordinates of those local liquid surface points;
- depth is calculated separately and is used to assign the already calculated width/length to points below the surface.

Therefore exact top-surface `MP_width` equivalence under `Z Num=1` is a source-code-grounded hypothesis, not an outcome-selected shortcut.

Authoritative upstream basis:
- `ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60/README.md`
- `src/Run.cpp::Solidify_Surface`
- `src/Melt.cpp::calc_mp_info`
- `src/Melt.cpp::local_neighbor_check`

## Frozen source / 고정 source

Reuse F42 source identity exactly:

- NIST dataset `mds2-2507`, version `1.0.1`;
- component `RHF_Command.zip`;
- size `18,079,576` bytes;
- SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- P01 member `RHF_Command/RHF_P01_layer0001.csv`;
- parsed rows `25,051`;
- positive-power source-native runs `39`;
- full run-length vector must exactly reproduce F42 before calibration construction.

Bounded source-download hardening from E43 `AMENDMENT-03` may be reused: maximum 3 complete attempts, <=240 s read timeout per attempt, final size and SHA verification mandatory.

## Frozen calibration path / 고정 calibration path

Use a deterministic source-native **prefix through the end of positive-power run 6**:

- run IDs: `[1,2,3,4,5,6]` in original P01 order;
- positive run lengths: `[251,376,251,376,21,40]`;
- positive rows: `1,315`;
- preserve source leading-off rows: `200`;
- preserve the first five source inter-run gaps: `[614,614,614,1067,423]` rows;
- stop immediately at the end of run 6; do not append the run-6→run-7 gap or full-source trailing-off block;
- modeled prefix time = `(200 + 1315 + 614 + 614 + 614 + 1067 + 423) * 10 us = 0.04847 s`;
- common 600 W benchmark energy proxy = `1,315 * 10 us * 600 W = 7.89 J`.

Coordinate translation must use the **full 39-run F42 positive geometry** min-x/min-y basis before taking the run-1–6 prefix, so the calibration path remains in the exact E43 coordinate frame.

This prefix is chosen prospectively because it is the earliest source-native sequence and contains both the four long initial runs and the first two short runs. It is not selected using simulator outputs.

## Frozen simulator cases / 고정 simulator cases

Both cases use:

- exact pinned 3DThesis commit `2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`;
- `Solidification` mode;
- `Tracking Surface`;
- `Timestep 1e-5 s`;
- same prefix Path file byte-for-byte;
- same pinned example `Material.txt`, `Beam.txt`, `Output.txt`, `Settings.txt`;
- same X domain: `Min -0.001`, `Max 0.004`, `Res 5.0e-5`;
- same Y domain: `Min -0.001`, `Max 0.003`, `Res 5.0e-5`;
- same standard public GitHub Ubuntu runner;
- no MPI;
- no path compression change, buffer change, material change, beam change, endpoint change, filtering, interpolation or post-result retuning.

### Case A — FULL41

Z domain inherited from E43:

```text
Z
{
  Min -0.001
  Max 0.000
  Res 2.5e-5
}
```

Expected grid = `101 x 81 x 41 = 335,421` points.

### Case B — TOP1

Only Z representation changes:

```text
Z
{
  Min -0.001
  Max 0.000
  Num 1
}
```

Pinned documentation states that when `Num=1`, only `Max` is used. Expected grid = `101 x 81 x 1 = 8,181` points at top surface `z=0`.

## Frozen runtime caps / 고정 runtime cap

- FULL41: `180 s` hard cap;
- TOP1: `180 s` hard cap;
- workflow: `10 min` hard cap.

A timeout is `HOLD`, not evidence for or against equivalence. No cap extension inside F44.

## Frozen output comparison / 고정 출력 비교

Expected final CSV schema:

`x,y,z,MP_width,MP_length,MP_depth`

Comparison uses **all top-surface rows**, not only positive rows.

1. FULL41 rows are restricted only by the preregistered structural condition `z == 0` (within parser absolute tolerance `1e-15` solely for decimal parsing).
2. TOP1 must contain only the same top-surface coordinate plane.
3. Coordinate key = exact parsed `(x,y)` pair.
4. Coordinate sets must be identical and must contain exactly `8,181` unique points.
5. `MP_width` must match at every coordinate with frozen absolute tolerance `1e-12 m`.
6. `MP_length` is a secondary same-coordinate check with the same `1e-12 m` tolerance.
7. Positive-width support (`MP_width > 0`) must be exactly identical by coordinate.
8. No trimming, winsorization, region-of-interest filtering, positive-only primary matching, rank transformation or tolerance adjustment is allowed.
9. `MP_depth` is intentionally excluded from equivalence because TOP1 removes subsurface representation by design.

Persist only aggregate equivalence diagnostics, mismatch counts/max absolute differences, source/path hashes and runtimes. Raw simulator CSV and generated Path remain transient.

## Frozen gates / 고정 gate

### `PASS_F44_SURFACE_ONLY_MPSTATS_EQUIVALENT`
All integrity/runtime/schema/coordinate checks pass, and both `MP_width` and `MP_length` match all 8,181 top-surface coordinates within `1e-12 m`, with identical positive-width support.

### `PARTIAL_F44_MPWIDTH_ONLY_EQUIVALENT`
All integrity/runtime/schema/coordinate checks pass and `MP_width` plus positive-width support pass exactly as frozen, but `MP_length` does not. This may qualify a future **width-only** experiment but not generic MP_Stats equivalence.

### `REJECT_F44_SURFACE_ONLY_REPRESENTATION`
Both cases execute validly and coordinate mapping is valid, but `MP_width` fails the frozen equivalence condition.

### `HOLD_F44_RUNTIME_OR_INTEGRITY`
Source/hash/build/runtime/output-schema/coordinate integrity fails, either case times out/non-zero, or fewer/more than 8,181 unique top-surface coordinates are available.

## Claim boundary / 주장 경계

A PASS establishes only equivalence of pinned 3DThesis top-surface `MP_width`/`MP_length` for this source-native calibration prefix under the frozen model settings. It does not establish full-P01 runtime feasibility, N0-vs-R1 path-order performance, NIST physical reproduction, material universality, scanner feasibility, production readiness, or patent novelty.

If F44 passes, a separate decision is required before any new full-P01 TOP1 N0-vs-R1 experiment.

## Cost / 비용

Incremental monetary cost remains `0 USD`. Any billable compute requires explicit prior user approval.
