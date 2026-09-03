---
checkpoint_id: CHK-20260903-F45-RANGE-INGRESS-ACTIVE
active_issue: 63
active_research: AMBENCH-F45
last_completed_issue: 62
last_completed_research: AMBENCH-F44
last_decision: DEC-091
updated: 2026-09-03
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.55-f44-source-hold-f45-range-ingress-active`  
**State / 상태:** `E43_COMPLETED_HOLD__F44_COMPLETED_SOURCE_HOLD__F45_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #63 `AMBENCH-F45`.

## Governance / 거버넌스
GitHub remains Source of Truth. `DEC-055` Continuity Overlay and `COST-001` zero-incremental-cost default remain active. Billable work requires explicit user approval. Runtime/source-integrity/evaluation logic remains `SHARED-INTERNAL-CANDIDATE`; no duplicate Skill/MCP/Plugin or assumed shared paid quota.

## Completed E43 / 완료 E43

**`HOLD_E43_RUNTIME_OR_INTEGRITY`**.

Exact source and F42 path integrity passed in recovery, but N0 hit the prospectively frozen `480 s` runtime cap (`rc=124`); R1 was not executed. No N0-vs-R1 `MP_width` comparison exists. `DEC-088` closes E43 and forbids within-E43 timestep/domain/resolution/solver rescue.

## Completed F44 / 완료 F44

**`HOLD_F44_RUNTIME_OR_INTEGRITY`** — specifically a source-ingress HOLD, not a representation reject.

F44 preregistered FULL41 vs TOP1 top-surface MP_Stats equivalence, but its three bounded whole-object NIST transfers failed before calibration construction:
1. `IncompleteRead(13,532,892 bytes read, 4,546,684 more expected)`;
2. HTTP `524`;
3. HTTP `524`.

Consequences:
- archive size/SHA were not verified in the F44 run;
- calibration Path was not constructed;
- FULL41 and TOP1 were not executed;
- no 8,181-coordinate `MP_width`/`MP_length` comparison exists.

The Actions workflow completed successfully only in the operational sense and correctly persisted the scientific HOLD. `CLM-116` and `DEC-090` are authoritative. Issue #62 is closed.

## Active F45 / 활성 F45

**AMBENCH-F45 — Checksum-Preserving Resumable Source-Ingress Qualification**; Issue #63; execution authorized by `DEC-091`.

F45 is source-only. It builds no simulator and accesses no MP_Stats/performance/physical outcome.

### Frozen source identity / 고정 source identity
- NIST `mds2-2507` v1.0.1;
- component `RHF_Command.zip`;
- size `18,079,576` bytes;
- SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`.

### Frozen range protocol / 고정 range protocol
- chunk size `1,048,576` bytes (1 MiB);
- 18 sequential, non-overlapping ranges;
- exact HTTP `206 Partial Content` required;
- exact `Content-Range` and requested body length required;
- maximum 3 attempts per unchanged range;
- 90 s read timeout per attempt;
- fixed 3 s retry delay;
- workflow cap 15 min;
- no adaptive chunk size, concurrency, whole-object fallback, alternate mirror/endpoint, raw artifact persistence or paid service.

### Frozen gates / 고정 gate
- `PASS_F45_CHECKSUM_PRESERVING_RANGE_INGRESS`: all 18 ranges reconstruct exact size/SHA and valid ZIP/P01 identity;
- `REJECT_F45_RANGE_PROTOCOL_NOT_SUPPORTED`: deterministic HTTP range semantic incompatibility;
- `HOLD_F45_SOURCE_OR_NETWORK`: metadata/source drift, exhausted network retries, or workflow cap.

Current run: GitHub Actions `33736865119`; ingress step active at last verified read.

## Exact Next Action / 정확한 다음 행동

Finish run `33736865119`, verify `research/AMBENCH-F45/RESULT.md` against the frozen source/range/size/SHA/ZIP contract, close Issue #63 with the observed gate, synchronize STATUS/HANDOFF, and only if F45 PASS decide whether a separately numbered representation-equivalence experiment may reuse the qualified ingress protocol. Do not reopen or rewrite F44.
