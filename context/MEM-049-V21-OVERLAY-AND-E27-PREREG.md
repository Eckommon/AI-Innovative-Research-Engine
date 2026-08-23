---
id: MEM-049-V21-OVERLAY-AND-E27-PREREG
type: memory
created: 2026-08-23
source_of_truth: github
---

# MEM-049 — v2.1 Overlay Adoption + E27 Preregistration / v2.1 Overlay 채택 + E27 사전등록

## Verified state / 검증 상태

- F26 remains completed `PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`.
- No active issue existed before E27 initiation.
- `STATUS.md` and `context/SESSION_HANDOFF.md` matched at the F26 checkpoint.
- Root `AGENTS.md` is absent, but existing README/governance/sync/hallucination-control/status/handoff records functionally satisfy Minimum Operability Baseline; no new AGENTS file was needed.
- A P0 current-state drift was found: README duplicated an obsolete F08 current baseline while STATUS/HANDOFF were at F26.
- Durable correction: README now avoids dynamic current-state duplication and points to STATUS + SESSION_HANDOFF + live Issues as current-state authority.
- v2.1 continuity overlay adoption is recorded in `DEC-055`.

## Capability delta / Capability delta

Recurring project workflow is classified `SHARED-INTERNAL-CANDIDATE` only:
- state/checkpoint reconciliation;
- preregistration/frozen-gate execution;
- NIST NERDm immutable-source qualification;
- evidence/provenance/cost-gate enforcement.

The existing Central Capability Repository `Eckommon/AI-Agent-Capability-Library` was confirmed to exist. A broad code-search query returned no direct match for the above combined terms; this is insufficient to claim absence, so central overlap remains `UNVERIFIED` and does not block mission work.

## E27 preregistration / E27 사전등록

`research/AMBENCH-E27/README.md` and `DEC-056` freeze:
- six physical plates, 3 vs 3;
- P1 only, 5 mm × 5 mm pad at x=0.460 mm;
- primary average overlap depth;
- sensitivity average depth;
- one-sided exact 20-allocation label-permutation reference test;
- no outcome-driven redesign.

Next: create/activate E27 Issue, synchronize active state, perform NERDm + schema preflight, then execute numerical test only if integrity passes.

## Cost / 비용

All work in this checkpoint used zero-incremental-cost GitHub/NIST/public routes. Paid/potentially paid actions remain subject to prior approval.