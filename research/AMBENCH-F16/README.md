---
id: AMBENCH-F16
type: source-integrity-feasibility
state: PREREGISTERED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F15/RESULT.md
  - NIST PDR ark:/88434/mds2-3761
---

# AMBENCH-F16 — mds2-3761 Source-Integrity / Access Gate
# AMBENCH-F16 — mds2-3761 원천 무결성 / 접근성 게이트

## 1. Purpose / 목적

**KO:** F15에서 `PARTIAL_REGISTERED_SCHEMA_READY`로 판정된 NIST `mds2-3761`에 대해, 후속 in-situ melt-pool ↔ XCT process–structure 실험을 허용하기 전에 exact public release lineage, immutable component provenance, checksum-verifiable bytes, actual archive inventory를 무비용 경로에서 검증한다.

**EN:** Before any downstream in-situ melt-pool ↔ XCT process–structure experiment, test whether NIST `mds2-3761` has exact public release lineage, immutable component provenance, checksum-verifiable bytes, and actual archive inventory recoverable through verified zero-incremental-cost routes.

F16 is source/integrity feasibility only. No correlation, target selection, feature importance, prediction, or model fitting is authorized.

## 2. Governance / 거버넌스

- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval before execution. Unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: any authoritative ZIP bytes are transient-only; persist hashes/inventory, not source archives.
- `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `WRITEBACK-001` apply.

## 3. Pre-registration availability probe disclosure / 사전등록 직전 접근성 probe 공개

Immediately before this README was frozen, one zero-cost direct-download availability probe was attempted against the official Part 1 URL:
`https://data.nist.gov/od/ds/mds2-3761/part1.zip`.

The probe failed and recovered **zero source bytes**. No archive members, numerical values, or scientific outcomes were exposed. This failed availability probe is disclosed for chronology; it does not change the gates below.

## 4. Frozen authoritative identifiers / 고정 authoritative 식별자

- Dataset identifier: `ark:/88434/mds2-3761`.
- Data.gov current public distributions:
  - `https://data.nist.gov/od/ds/mds2-3761/part1.zip`
  - `https://data.nist.gov/od/ds/mds2-3761/part02.zip`
  - `https://data.nist.gov/od/ds/mds2-3761/part03.zip`
  - `https://data.nist.gov/od/ds/mds2-3761/part04.zip`
- Data description: NIST AMS 100-69, DOI `10.6028/NIST.AMS.100-69`.
- Data.gov metadata: issued `2025-05-09`, modified `2025-03-13`, public access.

## 5. Frozen questions / 고정 질문

1. Can an exact version/release snapshot for the data-bearing PDR be identified?
2. Are authoritative SHA-256 checksums, or equivalent immutable byte-level integrity identifiers, available for each Part ZIP?
3. Can at least Part 1 be retrieved from an authoritative zero-cost endpoint and byte-verified?
4. If Part 1 is retrievable, does the archive inventory deterministically contain the documented layer-organized CSV structure without relying on numerical scientific outcomes?
5. If Part 1 passes, can the same integrity procedure be extended to Parts 2–4 without paid resources?

## 6. Frozen execution order / 고정 실행 순서

1. Reverify current official Data.gov/NIST metadata and URLs.
2. Search official NIST/PDR records for exact release/version lineage and immutable hashes.
3. Attempt authoritative Part 1 retrieval only if route is verified zero-cost.
4. If bytes are recovered, compute SHA-256 locally and inspect filename/directory inventory only.
5. Expand to Parts 2–4 only after Part 1 passes.
6. Delete all transient source bytes after verification.

No unverified mirrors, figure digitization, inferred checksums, or paid retrieval are permitted.

## 7. Frozen gates / 고정 판정

### `PASS_IMMUTABLE_SOURCE_READY`
All must hold:
- authoritative dataset identity and exact data-bearing release/version lineage established;
- immutable byte-level integrity evidence established for all four Part ZIPs;
- at least Part 1 authoritative bytes retrieved and matching the frozen integrity evidence;
- Part 1 archive inventory deterministically matches the documented layer-CSV organization;
- no identity/provenance conflict.

Only this gate authorizes preregistration of a numerical process–structure experiment.

### `PARTIAL_PUBLIC_ENDPOINT_READY`
All:
- authoritative identifier and current official four-Part endpoints established;
- schema/registration semantics remain qualified from F15;
- at least one of exact version lineage, immutable hashes, or byte-level retrieval/inventory remains unverified;
- no evidence of source contradiction.

### `HOLD_SOURCE_RETRIEVAL`
Official immutable identity/hash evidence is otherwise sufficient, but authoritative bytes cannot be retrieved through available verified zero-cost routes.

### `HOLD_PROVENANCE_OR_VERSION`
Public endpoints exist but version lineage or immutable provenance is materially ambiguous/conflicted enough that byte verification cannot be meaningfully frozen.

### `REJECT_SOURCE_MISMATCH`
Retrieved authoritative content contradicts the documented dataset/part identity or archive organization.

## 8. Consequence / 후속

- PASS → separately preregister a low-degree-of-freedom in-situ melt-pool ↔ XCT process–structure experiment.
- PARTIAL/HOLD → no modeling; preserve F15/F16 evidence and either pursue another authoritative integrity route or triage another source.

No high-capacity model is authorized by F16.