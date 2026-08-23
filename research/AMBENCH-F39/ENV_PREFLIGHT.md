---
id: AMBENCH-F39-ENV-PREFLIGHT
type: external-execution-environment-preflight
created: 2026-08-23
candidate_controller_performance_executed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F39 3DThesis Execution Environment Preflight / 3DThesis 실행환경 사전점검

## Boundary / 경계
- Upstream build + bundled example execution only.
- No C0–C4 controller performance comparison is executed here.
- Upstream source is transient checkout; no third-party source code is vendored into this repository.

## Immutable upstream identity / 고정 upstream identity
- repository: 
- pinned_commit: 
- default upstream branch observed separately: 
- license: upstream README declares open-source 3-clause BSD; local license head: 

## Build/runtime verification / 빌드·실행 검증
- runner: GitHub hosted standard Ubuntu runner
- cmake_configure: 
- cmake_build: 
- cmake_install: 
- bundled_example: 
- example_execution: 
- expected_csv_output_count: 
- MP_Stats_declaration_hits_in_example_inputs: 

## Actuator encoding surface / actuator 표현 surface
Upstream README/documented path syntax provides :
- path/order: encoded by path-line ordering and XYZ target sequence;
- power: encoded by beam power × per-segment , including variable-power strategies;
- timing: encoded by line velocity or spot duration, with zero-power path/positioning segments available for laser-off travel/delay representation.

Pinned example  preview is intentionally reported only as input-format evidence, not as a candidate controller result:



## Output surface / output surface
Upstream README documents temperature/temperature-history and solidification outputs including melt-pool  maximum width/length. The bundled  example executed successfully in this pinned environment.

## F39 consequence / F39 결과
**PASS_F39_RUNTIME_ENVIRONMENT_EXECUTES**

This establishes that one open, pinned, zero-cost thermal simulation runtime can encode all three actuator classes and emit physical/thermal endpoints. It does **not yet** establish the full , because the common history-state generator and matched C0–C4 controller contracts must still be frozen and verified before performance execution.
