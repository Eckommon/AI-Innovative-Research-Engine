---
id: AMBENCH-E43-RESULT
type: source-grounded-path-order-only-thermal-benchmark-result
created: 2026-09-03
recovery_under: AMBENCH-E43-AMENDMENT-03
incremental_monetary_cost_usd: 0
---

# AMBENCH-E43 Result — P01 Source-Grounded Path-Order-Only Thermal Benchmark
# AMBENCH-E43 결과 — P01 Source-Grounded Path-Order-Only Thermal Benchmark

**Final gate / 최종 gate: `HOLD_E43_RUNTIME_OR_INTEGRITY`**

## Integrity / 무결성
- NIST version: `1.0.1`
- archive size: `18079576`
- archive SHA-256: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`
- archive download attempt used: `1`
- N0 path SHA-256: `7b2860908b2c96b167e1f383af5fa150b92184ad433e1ca9b3320dba68eeb475`
- R1 path SHA-256: `778adef0041061f2413b35539798c3c5836b3290c1054e4c71b39f5dc689cd9b`
- laser-on time: `0.07408000000000001` s
- laser-off time: `0.17643` s
- total modeled process time: `0.25051` s
- benchmark energy proxy: `44.44800000000001` J
- pinned 3DThesis: `2de7fc6d8cfa5de78b111df97b1a4d9156a8cf60`
- timestep: `1e-5 s`
- domain: `101 x 81 x 41 = 335421` grid points

## Runtime / 실행시간
- N0: `{'executed': True, 'rc': 124, 'elapsed_s': 480}`
- R1: `{'executed': False, 'rc': None, 'elapsed_s': None}`

## HOLD reasons / HOLD 사유

- N0 runtime not successful: {'executed': True, 'rc': 124, 'elapsed_s': 480}
- R1 runtime not successful: {'executed': False, 'rc': None, 'elapsed_s': None}

## Boundary / 경계

This is a deterministic pinned semi-analytic thermal benchmark. No row-level p-value is used. A PASS does not establish physical-machine superiority, NIST physical replication, scanner-kinematic feasibility, patent novelty, material universality, or production readiness.

Raw simulator CSV and generated paths remain transient and are not committed.

