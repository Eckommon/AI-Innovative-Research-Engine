---
id: INDEX-SYNC-STATUS-20260822-F13
type: registry-maintenance
state: BACKLOG_EXPLICIT
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Registry Index Sync Status after F13 / F13 이후 Registry Index 동기화 상태

## Current authoritative records / 현재 권위 기록

Stable standalone decision/claim records remain authoritative even when aggregate indexes lag. / aggregate index가 뒤처져도 stable standalone decision/claim 파일이 권위 기록으로 유지된다.

### Decision aggregate backlog / Decision 집계 backlog
`registry/DECISION_LOG.md` currently ends at `DEC-024`.
Standalone records requiring later aggregate integration while preserving full history:
- `DEC-025` — F10 final HOLD;
- `DEC-026` — D11 activation;
- `DEC-027` — D11 final mixed result;
- `DEC-028` — monetary-cost approval must precede execution;
- `DEC-029` — D12 activation;
- `DEC-030` — D12 final robust condition-specific variation;
- `DEC-031` — select `mds2-2525` / F13;
- `DEC-032` — F13 final PARTIAL external-validation readiness.

### Claim aggregate backlog / Claim 집계 backlog
`registry/CLAIM_LEDGER.md` currently ends at `CLM-037`.
Standalone records requiring later aggregate integration while preserving full history:
- `CLM-038..039` — F10;
- `CLM-040..043` — D11;
- `CLM-044..047` — D12;
- `CLM-048..050` — F13.

## Safety rationale / 안전 근거

The available connector update operation replaces the complete UTF-8 file. Reconstructing these long aggregate files from truncated/partial reads risks accidental deletion or corruption of historical rows. Therefore this session does **not** rewrite either aggregate index from incomplete context. / 현재 connector update는 전체 파일 교체 방식이며 truncated/부분 read만으로 재구성하면 과거 row 손실 위험이 있으므로 이 세션에서는 aggregate index를 억지로 교체하지 않는다.

## Required maintenance / 후속 유지보수

At a future registry-maintenance step, read each aggregate file completely, append the listed standalone records in ID order, preserve all historical rows verbatim, then verify IDs and references. / 향후 registry maintenance에서 전체 파일을 완전 read한 뒤 ID 순으로 standalone records를 병합하고 기존 history를 그대로 보존한 후 ID/reference 정합성을 검증한다.

This backlog does not change current research state, F13 gate, checkpoint, or authority of standalone records. / 이 backlog는 현재 연구상태·F13 gate·checkpoint·standalone record의 권위를 변경하지 않는다.
