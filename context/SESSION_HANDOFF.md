---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260903-F44-SURFACE-EQUIVALENCE-ACTIVE
active_issue: 62
active_research: AMBENCH-F44
last_completed_issue: 61
last_completed_research: AMBENCH-E43
last_decision: DEC-089
created: 2026-08-22
updated: 2026-09-03
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Current State / 현재 상태

- Active Issue: #62 `AMBENCH-F44 — Surface-Only MP_Stats Representation Equivalence Gate`.
- Last completed: #61 `AMBENCH-E43`, final gate **`HOLD_E43_RUNTIME_OR_INTEGRITY`**.
- `DEC-055`: compact Shared Capability/Portfolio Continuity Overlay active.
- `COST-001`: incremental monetary cost defaults to `0 USD`; billable work requires explicit user approval.
- `DEC-088`: E43 finalized as runtime HOLD; no within-E43 resolution/timestep/domain/solver rescue.
- `DEC-089`: F44 preregistered and authorized as a separate representation-equivalence gate.

## E43 final anchor / E43 최종 기준점

NIST source and F42 transfer integrity passed under recovery:
- `mds2-2507` v1.0.1;
- `RHF_Command.zip` size `18,079,576` and SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- N0 path SHA-256 `7b2860908b2c96b167e1f383af5fa150b92184ad433e1ca9b3320dba68eeb475`;
- R1 path SHA-256 `778adef0041061f2413b35539798c3c5836b3290c1054e4c71b39f5dc689cd9b`;
- pinned `ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60` build PASS.

Runtime:
- N0 executed and timed out at the frozen `480 s` cap (`rc=124`);
- R1 was not executed after fail-closed N0 timeout;
- no N0-vs-R1 `MP_width` performance comparison exists.

Interpretation: E43 is a resource/runtime HOLD only. Do not infer no path-order effect.

## Active F44 / 활성 F44

Purpose: test whether pinned 3DThesis Z `Num 1` preserves the top-surface `MP_width` field required by the path-order question while removing subsurface evaluation points.

Upstream code basis already verified at the pinned commit:
- `Solidify_Surface` tracks liquid points at `znum-1` and separately evaluates depth below them;
- `Melt::calc_mp_info` seeds/expands a local liquid pool on the top k layer and calculates width/length from x/y only;
- depth is handled separately and used to assign width/length below the surface;
- README documents that Z `Num 1` uses only Z `Max`.

### Frozen calibration

Original-order P01 prefix through positive-power run 6:
- run IDs `[1,2,3,4,5,6]`;
- run lengths `[251,376,251,376,21,40]`;
- positive rows `1,315`;
- leading off `200` rows;
- first five gaps `[614,614,614,1067,423]`;
- modeled rows `4,847` = `0.04847 s`;
- 600 W benchmark energy proxy `7.89 J`.

Full 39-run source geometry remains the coordinate-translation basis.

### Frozen cases

Common: exact pinned simulator, `Solidification / Surface / Timestep=1e-5 s`, same Path/material/beam/output/settings/X/Y.

- FULL41: `101 x 81 x 41 = 335,421` points.
- TOP1: `101 x 81 x 1 = 8,181` points using Z `Num 1`.
- hard cap `180 s` each; workflow `10 min`.

### Frozen equivalence

Compare all 8,181 top-surface coordinate rows including zeros:
- identical `(x,y)` set;
- `MP_width` absolute difference <= `1e-12 m` at every coordinate;
- identical positive-width coordinate support;
- secondary `MP_length` absolute difference <= `1e-12 m`;
- `MP_depth` excluded;
- no ROI/filter/tolerance retuning.

Gates:
- `PASS_F44_SURFACE_ONLY_MPSTATS_EQUIVALENT`;
- `PARTIAL_F44_MPWIDTH_ONLY_EQUIVALENT`;
- `REJECT_F44_SURFACE_ONLY_REPRESENTATION`;
- `HOLD_F44_RUNTIME_OR_INTEGRITY`.

## Current execution / 현재 실행

Workflow: `.github/workflows/ambench-f44-surface-equivalence.yml`.
Completion monitor: `.github/workflows/ambench-f44-monitor.yml`.

At this handoff write, `research/AMBENCH-F44/RESULT.md` has not yet been observed. Do not infer a gate until the durable result exists and is verified against the preregistration.

## Exact Next Action / 정확한 다음 행동

Read `research/AMBENCH-F44/RESULT.md` and `RUN_MONITOR.md` when available; verify source identity, calibration path identity, FULL41/TOP1 return codes, final CSV schema, 8,181-coordinate mapping, `MP_width`/support/`MP_length` mismatch counts and frozen tolerance; close/HOLD Issue #62 with the observed gate; synchronize STATUS/HANDOFF again; only then consider a separate full-P01 TOP1 path-order experiment.
