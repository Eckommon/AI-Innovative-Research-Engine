---
id: AMBENCH-E43-AMENDMENT-03
type: execution-harness-network-hardening
created: 2026-09-03
experiment_contract_changed: false
performance_output_observed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Amendment 03 — Bounded Source-Download Hardening
# AMBENCH-E43 보정 03 — 제한된 Source Download 보강

## Trigger / 발동 근거

The exact GitHub failed-job rerun (`run_attempt=2`) again failed in Step 3 before build or simulation.

Attempt 2 terminated while reading the same NIST `RHF_Command.zip` response with:

`http.client.IncompleteRead: IncompleteRead(7651036 bytes read, 10428540 more expected)`

The first attempt had terminated with `TimeoutError: The read operation timed out` at the same source-fetch stage. In both attempts:
- build was skipped;
- N0/R1 simulator execution was skipped;
- no E43 performance output was observed.

## Authorized harness-only change / 허용되는 하네스 전용 변경

A recovery workflow may harden **network transfer only** as follows:
- maximum 3 complete-download attempts for each required HTTP resource;
- per-attempt read timeout up to 240 seconds;
- discard any incomplete attempt and restart from byte 0;
- bounded retry delay of 5 seconds;
- after download, require the unchanged exact `RHF_Command.zip` size `18,079,576` bytes and SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4` before parsing;
- no acceptance of partial/resumed content unless the final complete file independently passes the same size/SHA contract.

The recovery workflow must fail closed to `HOLD_E43_RUNTIME_OR_INTEGRITY` and persist a terminal result even when download/build/runtime/output parsing fails.

## Scientific invariants / 과학적 불변조건

No change is authorized to:
- NIST dataset/component identity;
- exact P01 member and 25,051-row / 7,408-positive-row contract;
- F42 N0/R1 path-generation logic or expected hashes;
- run order;
- pinned `ORNL-MDF/3DThesis@2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`;
- material/beam/domain/resolution;
- Solidification / Surface / `Timestep=1e-5 s`;
- 480-second per-case runtime cap or 20-minute experiment workflow cap;
- spatial positive `MP_width` CV endpoint;
- mean-width, positive-record-count, 10% materiality or any other frozen gate.

## Evidence / 근거

- `RUN_DIAGNOSTIC.md`
- `STEP3_FAILURE_DIAGNOSTIC.md`
- `RERUN_MONITOR.md`
- `RERUN2_FAILURE_DIAGNOSTIC.md`

## Boundary / 경계

This amendment corrects source-transfer reliability only. It cannot be used to alter or rescue an E43 simulator result.
