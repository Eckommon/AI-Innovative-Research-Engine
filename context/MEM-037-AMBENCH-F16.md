---
id: MEM-037-AMBENCH-F16
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F16/RESULT.md
  - registry/DEC-038.md
---

# MEM-037 — AMBENCH-F16 Result / AMBENCH-F16 결과

## Final state / 최종 상태
`AMBENCH-F16 = PARTIAL_PUBLIC_ENDPOINT_READY`.

## What is verified / 검증된 내용
- NIST identifier `ark:/88434/mds2-3761`;
- current Data.gov/NIST public Part ZIP endpoints for Parts 1–4;
- issued `2025-05-09`, modified `2025-03-13` in current Data.gov metadata;
- NIST AMS 100-69 documents the registered per-part/per-layer CSV dataset and machine-coordinate alignment;
- F15 registered schema/registration semantics remain qualified.

## What remains unverified / 미검증 내용
- exact data-bearing PDR release/version lineage;
- immutable checksum/equivalent byte-level integrity identifier for each Part ZIP;
- authoritative Part 1 source bytes and local checksum;
- actual archive inventory from authoritative bytes.

Two post-preregistration zero-cost authoritative Part 1 retrieval paths failed. Parts 2–4 were not attempted because the frozen execution order required Part 1 to pass first.

## Consequence / 후속
No numerical in-situ melt-pool ↔ XCT experiment is authorized yet. Do not repeatedly hammer the same inaccessible endpoint. Prefer targeted official NIST/PDR version/checksum metadata recovery; if unavailable within zero-cost constraints, triage another authoritative process–structure dataset.

E14 remains frozen at `HOLD_SOURCE_INTEGRITY` and is not redesigned.

## Cost boundary / 비용 경계
Any potentially billable source/compute/retrieval route requires explicit user approval before execution. Post-hoc reporting is not authorization.