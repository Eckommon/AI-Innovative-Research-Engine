---
id: AMBENCH-F39-RESULT
type: added-value-falsification-design-result
state: CORRECTED_AFTER_DESCENDANT_INPUT_PREFLIGHT
created: 2026-08-23
corrected: 2026-08-24
source_of_truth: github
candidate_controller_performance_executed: false
supersedes_gate: PASS_F39_EXECUTABLE_ADDED_VALUE_TEST_READY
incremental_monetary_cost_usd: 0
---

# AMBENCH-F39 Result — Corrected by E40 Pre-Performance Input Falsification
# AMBENCH-F39 결과 — E40 성능실행 전 입력 반증으로 정정

## Corrected frozen gate / 정정 판정

**`REJECT_F39_INCREMENTAL_TEST_NOT_IDENTIFIABLE`**

The earlier `PASS_F39_EXECUTABLE_ADDED_VALUE_TEST_READY` is superseded. The runtime and output-schema qualifications remain valid, but the actual frozen common-state generation showed that the third actuator class does not produce a distinct generated input in this benchmark.

## What remained valid / 유효하게 남는 항목

- pinned `ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60` build/install/runtime qualification: PASS;
- open BSD-3-Clause zero-cost execution route: PASS;
- deterministic `MP_width` output schema: PASS;
- common RHF-state formula and matched energy/time constraints were executable;
- no custom C0–C4 simulator performance was observed before correction.

## Descendant falsification evidence / 후속 반증 근거

E40 generated the frozen nominal common state and controller path files **without running custom performance**.

Verified in `research/AMBENCH-E40/INPUT_IDENTIFIABILITY_PREFLIGHT.md`:
- 6,300 nominal command points from 21 hatches × 300 segments × 10 us;
- hatch 1 risk differs from the steady regime;
- hatch 2–21 risk spread is only `9.99200722162641e-16`, within the explicit 64-ULP numerical equality guard;
- the frozen tie rule therefore yields canonical hatch order `[1..21]`;
- generated C3 path SHA-256 equals C0 exactly;
- generated C4 path SHA-256 equals C2 exactly;
- energy-neutralization and total 15 ms transition-dwell invariants still pass.

Therefore the path/order actuator is **not an identifiable intervention** under the frozen benchmark. C4-vs-C2 would compare byte-identical generated path/controller inputs, so no simulator run can test incremental value of the third actuator class.

## Why performance was not executed / 성능 미실행 이유

Running C0–C4 after this preflight would create a misleading “performance test” from identical C2/C4 inputs. The correct falsification action is to stop before simulation rather than retune the RHF state, path score, tie rule, `R/T/C`, raster geometry or optimizer after seeing the degeneracy.

## Source-semantic correction / source 의미 보정

E40 `AMENDMENT-01` also corrected `MP_Stats` interpretation before performance: `MP_width` is a **per-grid-point maximum melt-pool-width spatial field**, not a temporal trajectory. The numerical field/formula was not changed.

## Final interpretation / 최종 해석

F39 successfully identified a usable open runtime, but **failed to establish an identifiable three-actuator added-value comparison for the frozen uniform raster**.

This does not reject multi-actuator recent-history control in general. It rejects this specific F39 benchmark as a valid test of path/order incremental value.

## Exact next action / 정확한 다음 행동

Do not rescue F39/E40 by parameter or geometry retuning. Open a separate source/design gate to identify an **independently motivated non-degenerate path/order intervention environment** where the unchanged published RHF state produces materially distinct reorderable-unit risks before any controller performance is defined.

## Cost / capability / 비용

Incremental monetary cost `0 USD`. Runtime/evaluation logic remains `SHARED-INTERNAL-CANDIDATE`; no Skill/MCP/Plugin promotion.
