---
id: AMBENCH-D11-WORK-QUEUE
type: work-queue
state: ACTIVE_PENDING_ISSUE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/README.md
  - registry/DEC-026.md
---

# AMBENCH-D11 Work Queue / 작업 큐

**KO:** D11은 F10 HOLD 이후 immediate fallback으로 승인된 다음 진단이다. 실행 전 GitHub Issue를 활성화하고, 실행 시 frozen `README.md`를 변경하지 않는다.

**EN:** D11 is the approved immediate fallback after the F10 HOLD. Activate a GitHub Issue before execution and do not change the frozen `README.md` once numerical execution begins.

Execution boundary / 실행 경계:
- source: NIST `mds2-3842` v1.0.3;
- checksum verification mandatory;
- 21 authoritative tracks required;
- standard public-repository runner or local compute only;
- no paid route, GPU/larger runner, or raw-data artifact upload;
- apply exactly one frozen D11 gate;
- write `RESULT.md`, claims, decision, Issue disposition, STATUS/HANDOFF after execution.
