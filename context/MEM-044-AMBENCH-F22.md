---
id: MEM-044-AMBENCH-F22
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# MEM-044 — AMBENCH-F22 durable handoff / F22 영속 인수인계

## Final / 최종
`AMBENCH-F22` final descriptive gate: **`PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`**.

## What is now solved / 해결된 것
Current NIST NERDm for `mds2-3761` provides exact component metadata for all four registered part archives. All four were transiently downloaded on zero-cost public standard GitHub-hosted runners and local SHA-256 values matched exactly:
- part1: `0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3`
- part02: `bf72d9e160d94094f9268fcf3f76a532c8a29fb64aff1afbec20256acaee178e`
- part03: `89e9e1afadca22b9c34177d82972272a4e73789b19388f0c83d62a9ebd53d878`
- part04: `6c3f655a1482001119c54d1f1e404a34eb401f386fffc06147628b36c7c8d7c5`

Each ZIP is valid and contains exactly 250 CSV files with deterministic `L0001.csv`–`L0250.csv` coverage. Source-byte integrity is no longer the dominant blocker.

## Important correction / 중요 정정
The CSV files are headerless. The original Part 1 workflow assumed a textual header and accidentally read first numerical lines during schema checking. Initial persisted first-row values were removed from the current-facing result, but the event remains in Git history and is documented in `AMBENCH-F22/AMENDMENT-01.md`.

Current exposure state:
**`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`**.

Do not claim pristine outcome blindness in any future `mds2-3761` experiment.

## Exact next eligible work / 정확한 다음 eligible 작업
No modeling yet.

Separately preregister a **headerless serialization/schema mapping gate** that:
1. freezes exact positional column order 1..40 from NIST AMS 100-69;
2. validates structural field count with values suppressed;
3. verifies position→semantic mapping deterministically across the four archives;
4. preserves hierarchy rows ⊂ layers ⊂ parts;
5. carries the limited pre-exposure disclosure;
6. only then permits preregistration of a low-degree-of-freedom registered process/melt-pool ↔ XCT experiment.

## Cost / 비용
Incremental monetary cost in F22: `0 USD`. Paid/potentially paid routes remain prior-approval only.
