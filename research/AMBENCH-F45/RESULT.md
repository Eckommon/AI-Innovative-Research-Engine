---
id: AMBENCH-F45-RESULT
type: source-ingress-qualification-result
created: 2026-09-03
incremental_monetary_cost_usd: 0
---

# AMBENCH-F45 Result — Checksum-Preserving Resumable Source Ingress
# AMBENCH-F45 결과 — Checksum 보존 Resumable Source Ingress

**Final gate / 최종 gate: `HOLD_F45_SOURCE_OR_NETWORK`**

## Frozen source identity / 고정 source identity
```json
{
  "component_count": 1,
  "download_url_present": true,
  "filepath": "RHF_Command.zip",
  "nerdm_sha256": "c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4",
  "nerdm_size": 18079576,
  "version": "1.0.1"
}
```

## Frozen transfer geometry / 고정 전송 구조
- chunk size: `1048576` bytes
- expected ranges: `18`
- acquired ranges: `0`
- max attempts per range: `3`
- read timeout per attempt: `90` s
- retry delay: `3` s

## Chunk diagnostics / Chunk 진단
```json
[]
```

## Reconstruction / 재구성
```json
{}
```

- P01 member matches: `[]`

## HOLD/REJECT reasons / HOLD·REJECT 사유

- NetworkHold: range 0-1048575 exhausted attempts: attempt_1:TimeoutError:The read operation timed out | attempt_2:TimeoutError:The read operation timed out | attempt_3:TimeoutError:The read operation timed out

## Boundary / 경계

This gate qualifies source transport only. No simulator was built or run and no representation/path-order/performance inference is authorized. The transient reconstructed archive is not committed or uploaded as an artifact.

