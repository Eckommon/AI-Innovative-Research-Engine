---
id: AMBENCH-F44-RESULT
type: runtime-representation-equivalence-result
created: 2026-09-03
incremental_monetary_cost_usd: 0
---

# AMBENCH-F44 Result — Surface-Only MP_Stats Representation Equivalence
# AMBENCH-F44 결과 — Surface-Only MP_Stats 표현 동등성

**Final gate / 최종 gate: `HOLD_F44_RUNTIME_OR_INTEGRITY`**

## Source and calibration integrity / source 및 calibration 무결성
- NIST version: `1.0.1`
- archive size: `None`
- archive SHA-256: `None`
- source member: `None`
- calibration run IDs: `[1, 2, 3, 4, 5, 6]`
- calibration positive rows: `None`
- calibration modeled rows: `None`
- calibration modeled time: `None` s
- calibration energy proxy: `None` J
- calibration Path SHA-256: `None`

## Frozen representations / 고정 표현
- FULL41: `101 x 81 x 41 = 335421` points
- TOP1: `101 x 81 x 1 = 8181` points
- Same Path/material/beam/output/settings/X/Y; only Z representation differs.

## Runtime / 실행시간
- FULL41: `None`
- TOP1: `None`
- TOP1/FULL41 elapsed ratio: `None`

## Output diagnostics / 출력 진단
```json
{}
```

## Frozen equivalence diagnostics / 고정 동등성 진단
```json
{}
```

## HOLD/integrity reasons / HOLD·무결성 사유

- input:RuntimeError: all bounded fetch attempts failed: attempt_1:IncompleteRead:IncompleteRead(13532892 bytes read, 4546684 more expected) | attempt_2:HTTPError:HTTP Error 524: <none> | attempt_3:HTTPError:HTTP Error 524: <none>
- build/runtime preparation failed: {'build_ok': False, 'reason': 'input integrity failed'}
- FULL41 runtime not successful: {}
- TOP1 runtime not successful: {}

## Boundary / 경계

This gate tests only pinned-model top-surface representation equivalence on the preregistered source-native P01 prefix. It does not establish full-P01 runtime feasibility or N0-vs-R1 path-order added value. `MP_depth` is intentionally excluded.

Raw simulator CSV and generated Path remain transient and are not committed.

