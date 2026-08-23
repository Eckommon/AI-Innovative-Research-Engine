---
id: AMBENCH-F42
type: source-grounded-path-order-transfer-feasibility-gate
state: PREREGISTERED
created: 2026-08-24
source_of_truth: github
inherits:
  - AMBENCH-F41
  - DEC-083
incremental_monetary_cost_usd: 0
---

# AMBENCH-F42 — NIST P01 Source-Grounded Path-Order Transfer Feasibility Gate
# AMBENCH-F42 — NIST P01 Source-Grounded Path-Order Transfer 타당성 Gate

## Purpose / 목적

Determine whether the exact F41 P01 source-native scan runs can be mapped into pinned 3DThesis as **two distinct, matched-budget inputs** — nominal source order vs frozen F41 risk order — before any simulator-performance experiment is preregistered.

No MPM/encoder/analysis/microscopy outcome and no custom simulator performance value is allowed in F42.

## Frozen source / 고정 source

- NIST `mds2-2507` v1.0.1;
- `RHF_Command.zip` SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- exact P01 member `RHF_Command/RHF_P01_layer0001.csv`;
- headerless `X(mm),Y(mm),Power(W),Trigger`;
- each source row = one `10 us` digital position/power command;
- F41 scan-run definition and run membership unchanged.

Frozen risk order from F41:
`[5,39,6,18,24,22,20,21,23,25,27,17,16,28,29,15,14,13,30,26,31,7,32,19,12,11,33,34,10,8,9,38,35,36,37,1,3,2,4]`.

## Source→3DThesis mapping / Source→3DThesis mapping

Pinned runtime remains:
`ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`.

### Positive-power commands
Each P01 positive-power source row is represented as one 3DThesis **Mode=1 spot command** at the exact translated source `(X,Y)` setpoint for exactly `10 us`, with benchmark `Pmod=1`.

Rationale: NIST defines each XYPT row as a 10 us digital X/Y/power command. F42 does not assume an undocumented galvo interpolation model. This is an explicit zero-order-hold command-transfer abstraction, not scanner-kinematics validation.

Within every source-native positive run:
- exact row membership is preserved;
- exact source row order is preserved;
- exact XY geometry is preserved up to one common translation;
- every positive row contributes the same 10 us benchmark laser-on duration.

### Laser-off timing
Decompose source laser-off rows into:
- one global leading off block before run 1;
- 38 ordered inter-run off-duration slots between the 39 source runs;
- one global trailing off block after run 39.

Nominal and risk-order cases both preserve:
- the same global leading/trailing off duration;
- the exact same ordered sequence of 38 inter-run off durations by **transition ordinal position**, independent of destination run identity;
- therefore identical total laser-off time and total modeled process time.

For transfer, each off-duration slot is represented as a zero-power Mode=1 spot at the next run's first translated XY point. This intentionally abstracts scanner travel distance while preserving source-derived timing budget. It must not be described as scanner kinematics.

## Common translation and domain / 공통 translation 및 domain

Apply only a rigid XY translation:
- translated `X = source_X - min(source positive X)`;
- translated `Y = source_Y - min(source positive Y)`.

Distances, run geometry and run ordering are otherwise unchanged.

Future benchmark domain is deterministically derived before performance:
- XY bounding box of translated positive source points;
- `1.0 mm` buffer on each XY side;
- upstream example XY resolution `50 um`;
- Z range `[-1.0 mm, 0]`, resolution `25 um`;
- material/beam/output basis remains the pinned 3DThesis benchmark, so no quantitative NIST physical reproduction claim is allowed.

## Frozen transfer invariants / 고정 transfer 불변조건

Nominal and risk-order generated inputs must match exactly on:
1. source positive row count;
2. per-run positive row membership/within-run order;
3. total laser-on time = positive rows × 10 us;
4. benchmark commanded energy proxy = laser-on time × common benchmark beam power;
5. leading/trailing off time;
6. ordered multiset/sequence of 38 transition-duration slots;
7. total laser-off time and total modeled process time;
8. domain/material/beam/output settings.

Generated path SHA-256 must differ between nominal and risk-order cases, proving a distinct path intervention.

## Frozen gates / 고정 판정

### `PASS_F42_SOURCE_GROUNDED_PATH_TRANSFER_READY`
All source/checksum/run identities and all transfer invariants pass; nominal and risk-order path hashes differ; derived domain is finite and <=1,000,000 grid points at the frozen resolution.

### `REJECT_F42_ORDER_NOT_DISTINCT`
Generated nominal and risk-order path inputs are byte-identical or the F41 risk order collapses during faithful transfer.

### `HOLD_F42_MAPPING_OR_RESOURCE_GAP`
Source-to-runtime mapping cannot satisfy exact run membership/timing/budget invariants, source identity changes, or derived frozen-resolution domain exceeds the bounded standard-runner feasibility cap.

## Anti-rescue / 사후구제 금지

F42 must not:
- smooth/resample/split/merge positive source runs;
- change F41 risk order;
- change 10 us source command duration;
- introduce a galvo interpolation/acceleration model;
- vary beam/material/domain between nominal and reordered inputs;
- inspect simulator performance or physical outcome values;
- reduce resolution after seeing a resource failure inside F42.

## Descendant performance rule / 후속 성능 규칙

Only F42 PASS may authorize a separately preregistered **path-order-only** performance experiment. That descendant must compare nominal vs F41 risk order first; multi-actuator combination is not authorized until path-only incremental value is separately falsified or supported.

## Cost / 비용

Public source/process input + standard GitHub runner only. Incremental monetary cost `0 USD`.
