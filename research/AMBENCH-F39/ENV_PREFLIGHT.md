---
id: AMBENCH-F39-ENV-PREFLIGHT
type: external-execution-environment-preflight
created: 2026-08-23
report_version: v2_safe_writeback
candidate_controller_performance_executed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F39 3DThesis Execution Environment Preflight / 3DThesis 실행환경 사전점검

## Boundary / 경계
- Upstream build + bundled example execution only.
- No C0–C4 controller performance comparison is executed here.
- Upstream source is transient checkout; no third-party source code is vendored into this repository.

## Immutable upstream identity / 고정 upstream identity
- repository: ORNL-MDF/3DThesis
- pinned_commit: 2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60
- default upstream branch observed separately: master
- license: upstream README declares open-source 3-clause BSD; local license head: BSD 3-Clause License  Copyright 2019 UT-Battelle, LLC 

## Build/runtime verification / 빌드·실행 검증
- runner: GitHub hosted standard Ubuntu runner
- cmake_configure: PASS
- cmake_build: PASS
- cmake_install: PASS
- bundled_example: solidification_mpstats
- example_execution: PASS
- expected_csv_output_count: 1
- MP_Stats_declaration_hits_in_example_inputs: 2

## Actuator encoding surface / actuator 표현 surface
Upstream README/documented path syntax provides: Mode X Y Z Pmod Vel/Time
- path/order: encoded by path-line ordering and XYZ target sequence;
- power: encoded by beam power multiplied by per-segment Pmod, including variable-power strategies;
- timing: encoded by line velocity or spot duration, with zero-power path/positioning segments available for laser-off travel/delay representation.

Pinned example Path.txt preview is input-format evidence only, not a candidate controller result:

    Mode	X(mm)	Y(mm)	Z(mm)	Pmod	Time(s)
1	0	0	0	0	0
0	5	1	0	1	1

## Output surface / output surface
Upstream README documents temperature/temperature-history and solidification outputs including melt-pool MP_Stats maximum width/length. The bundled solidification_mpstats example executed successfully in this pinned environment.

## F39 consequence / F39 결과
**PASS_F39_RUNTIME_ENVIRONMENT_EXECUTES**

This establishes that one open, pinned, zero-cost thermal simulation runtime can encode all three actuator classes and emit physical/thermal endpoints. It does not yet establish the full PASS_F39_EXECUTABLE_ADDED_VALUE_TEST_READY, because the common history-state generator and matched C0–C4 controller contracts must still be frozen and verified before performance execution.
