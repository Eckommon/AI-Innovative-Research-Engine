---
checkpoint_id: CHK-20260903-F44-SURFACE-EQUIVALENCE-ACTIVE
active_issue: 62
active_research: AMBENCH-F44
last_completed_issue: 61
last_completed_research: AMBENCH-E43
last_decision: DEC-089
updated: 2026-09-03
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.54-e43-hold-f44-surface-equivalence-active`  
**State / 상태:** `F41_PASS__F42_PASS__E43_COMPLETED_HOLD__F44_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #62 `AMBENCH-F44`.

## Governance / 거버넌스
GitHub remains Source of Truth. `DEC-055` Continuity Overlay and `COST-001` zero-incremental-cost default remain active. Billable work requires explicit user approval. Runtime/source-integrity/evaluation logic remains `SHARED-INTERNAL-CANDIDATE`; no duplicate Skill/MCP/Plugin or assumed shared paid quota.

## Completed F41 / 완료 F41

**`PASS_F41_NONDEGENERATE_PATH_ORDER_SOURCE_READY`**.

Checksum-frozen NIST RHF P01 process input exposes 39 source-native positive-power runs with stable non-nominal risk ordering. No physical outcome/simulator-performance value was used.

## Completed F42 / 완료 F42

**`PASS_F42_SOURCE_GROUNDED_PATH_TRANSFER_READY`**.

Frozen source→3DThesis transfer:
- NIST `mds2-2507` v1.0.1;
- `RHF_Command.zip` size `18,079,576`, SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- source rows `25,051`, positive rows `7,408`, source-native runs `39`;
- laser-on `0.07408 s`, laser-off `0.17643 s`, total `0.25051 s`;
- common 600 W benchmark energy proxy `44.448 J`;
- E43 domain `101 x 81 x 41 = 335,421` points;
- N0 path SHA-256 `7b2860908b2c96b167e1f383af5fa150b92184ad433e1ca9b3320dba68eeb475`;
- R1 path SHA-256 `778adef0041061f2413b35539798c3c5836b3290c1054e4c71b39f5dc689cd9b`.

## Completed E43 / 완료 E43

**Final gate: `HOLD_E43_RUNTIME_OR_INTEGRITY`**.

Historical execution was first blocked twice by source-transfer transport failures; those were diagnosed as network failures before simulation. Under `AMENDMENT-03` / `DEC-087`, bounded network hardening only was applied, with all scientific/runtime inputs unchanged.

Recovery run `33733996919` then verified exact source identity, F42 path hashes and pinned 3DThesis build. Runtime result:
- N0 executed and hit the prospectively frozen `480 s` cap with `rc=124`;
- R1 was not executed under fail-closed sequencing;
- therefore no N0-vs-R1 `MP_width` performance comparison exists.

`DEC-088` closes E43 as a runtime/resource HOLD. Do not lower E43 timestep/domain/resolution, extend paid runtime, switch endpoint/filter, or change solver inside E43.

Durable: `research/AMBENCH-E43/RESULT.md`, `registry/CLM-115.md`, `registry/DEC-088.md`, Issue #61 closed.

## Active F44 / 활성 F44

**AMBENCH-F44 — Surface-Only MP_Stats Representation Equivalence Gate**; Issue #62; preregistered under `DEC-089`.

### Why / 이유

Pinned 3DThesis documents that Z `Num 1` uses only Z `Max`. In pinned source code, `Solidify_Surface` tracks surface liquid points and `Melt::calc_mp_info` computes melt-pool width/length from x/y coordinates of the top-surface local liquid pool; depth is handled separately and used to propagate already-calculated width/length below the surface.

Therefore F44 tests whether the top-surface `MP_width` field can be preserved while removing subsurface evaluation points. This is a separate representation qualification, not an E43 rescue.

### Frozen calibration / 고정 calibration

Use deterministic original-order P01 prefix through positive-power run 6:
- run IDs `[1,2,3,4,5,6]`;
- positive rows `1,315`;
- leading off `200` rows;
- first five inter-run gaps `[614,614,614,1067,423]`;
- modeled prefix time `0.04847 s`;
- energy proxy `7.89 J`;
- full 39-run geometry is still used for the F42 coordinate-translation basis.

### Frozen cases / 고정 cases

Common:
- pinned `ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`;
- `Solidification / Surface / Timestep=1e-5 s`;
- same calibration Path bytes, material, beam, output, settings and X/Y domain.

Cases:
- FULL41 = `101 x 81 x 41 = 335,421` points;
- TOP1 = `101 x 81 x 1 = 8,181` points using Z `Num 1`.

Hard caps: `180 s` each, workflow `10 min`, standard public GitHub runner only.

### Frozen equivalence / 고정 동등성

Compare **all 8,181 top-surface coordinates including zeros**:
- identical `(x,y)` coordinate set;
- coordinate-wise `MP_width` max absolute difference <= `1e-12 m`;
- identical positive-width coordinate support;
- secondary `MP_length` difference <= `1e-12 m`;
- `MP_depth` excluded by design;
- no ROI/filter/tolerance retuning.

Frozen gates:
- `PASS_F44_SURFACE_ONLY_MPSTATS_EQUIVALENT`;
- `PARTIAL_F44_MPWIDTH_ONLY_EQUIVALENT`;
- `REJECT_F44_SURFACE_ONLY_REPRESENTATION`;
- `HOLD_F44_RUNTIME_OR_INTEGRITY`.

## Exact Next Action / 정확한 다음 행동

Finish the preregistered `.github/workflows/ambench-f44-surface-equivalence.yml` execution, verify `research/AMBENCH-F44/RESULT.md` against the frozen source/runtime/schema/8,181-coordinate equivalence contract, close Issue #62 with the observed gate, and only then decide whether a separate full-P01 TOP1 path-order experiment is scientifically and operationally authorized.
