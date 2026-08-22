---
id: AMBENCH-D11-WORK-QUEUE
type: work-queue
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/README.md
  - registry/DEC-026.md
  - Issue #27
---

# AMBENCH-D11 Work Queue / 작업 큐

**KO:** D11은 F10 HOLD 이후 immediate fallback으로 승인된 현재 공식 진단 Work Queue이며, GitHub Issue #27이 활성 상태다. numerical execution이 시작되면 frozen `README.md`의 descriptor·threshold·gate를 변경하지 않는다.

**EN:** D11 is the current official diagnostic Work Queue approved as the immediate fallback after the F10 HOLD, with GitHub Issue #27 active. Once numerical execution begins, the frozen descriptors, thresholds, and gates in `README.md` must not change.

Execution boundary / 실행 경계:
- source: NIST `mds2-3842` v1.0.3;
- expected ZIP SHA-256: `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`;
- checksum verification mandatory;
- 21 authoritative tracks required;
- standard public-repository runner or local compute only;
- `COST-001`: zero incremental monetary cost;
- `RAW-001`: raw source bytes transient only;
- no paid route, GPU/larger runner, or raw-data artifact upload;
- apply exactly one frozen D11 gate;
- write `RESULT.md`, claims, decision, Issue disposition, STATUS/HANDOFF after execution.

**Current state:** `PREREGISTERED — ISSUE #27 ACTIVE — EXECUTION NOT YET RUN`.
