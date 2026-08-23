---
id: AMBENCH-E40
type: pinned-simulation-added-value-experiment
state: PREREGISTERED_SCHEMA_GATE_ACTIVE
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-F39
  - DEC-080
incremental_monetary_cost_usd: 0
---

# AMBENCH-E40 — Pinned 3DThesis Multi-Actuator Added-Value Execution
# AMBENCH-E40 — Pinned 3DThesis Multi-Actuator Added-Value 실행

## Authority / 권한

Execute only the already-frozen `research/AMBENCH-F39/DESIGN_CONTRACT.md` using:
`ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`.

No controller-performance result has been observed before this preregistration.

## Stage A — Output schema gate / 출력 schema gate

Before custom C0–C4 performance execution:
1. rebuild the exact pinned upstream runtime;
2. rerun only the bundled `solidification_mpstats` example;
3. inspect generated CSV **header/schema and row count only**;
4. deterministically identify the documented `MP_Stats` maximum-width and length fields;
5. do not persist bundled example numerical values or statistics.

### `PASS_E40_MPSTATS_SCHEMA_READY`
Exact pinned runtime executes and a deterministic maximum-width field is recoverable from bundled MP_Stats output.

### `HOLD_E40_RUNTIME_OR_OUTPUT_SCHEMA`
Runtime or output schema cannot support the frozen width endpoint. Do not switch endpoint.

## Stage B — Frozen performance / 고정 성능 실행

Only after Stage A PASS:
- generate common nominal RHF feedforward state exactly per F39 contract;
- generate C0–C4 controller inputs;
- verify input invariants before running;
- run the exact same runtime/domain/material/beam settings;
- compute only frozen width-trajectory metrics;
- apply the already-frozen `PASS/PARTIAL/NO/HOLD` E40 gates.

## Performance gates / 성능 판정

Inherited unchanged:
- `PASS_E40_JOINT_CONTROL_ADDED_VALUE`
- `PARTIAL_E40_JOINT_CONTROL_SMALL_INCREMENT`
- `NO_E40_JOINT_CONTROL_ADDED_VALUE`
- `HOLD_E40_RUNTIME_OR_OUTPUT_SCHEMA`

Primary comparator = C2 power+timing, not C0.

## Boundary / 경계

Simulation benchmark only. Not physical-machine validation, not legal novelty evidence, not NIST experimental replication, not scanner-kinematics validation.

## Cost / 비용

Standard public GitHub runner only; incremental monetary cost `0 USD`.
