---
id: AMBENCH-F16-RESULT
type: source-integrity-feasibility-result
state: COMPLETED_PARTIAL_PUBLIC_ENDPOINT_READY
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-F16/README.md
  - Issue #34
---

# AMBENCH-F16 Result — mds2-3761 Source-Integrity / Access Gate
# AMBENCH-F16 결과 — mds2-3761 원천 무결성 / 접근성 게이트

**Frozen final gate / 고정 최종 판정:** **`PARTIAL_PUBLIC_ENDPOINT_READY`**

## 1. Executive result / 핵심 결과

**KO:** NIST/Data.gov의 현행 공개 metadata는 `ark:/88434/mds2-3761`와 Part 1–4의 authoritative ZIP endpoint를 명확히 제공하고 있으며 F15의 registered schema/registration semantics와 충돌하지 않는다. 그러나 현재 확인 가능한 official public metadata에서는 exact data-bearing PDR release/version lineage와 각 ZIP의 immutable checksum/equivalent byte identifier를 확립하지 못했고, Part 1 authoritative bytes도 두 verified zero-cost retrieval routes에서 회수되지 않았다. 따라서 F16은 full immutable-source PASS가 아니라 `PARTIAL_PUBLIC_ENDPOINT_READY`이다. Numerical process–structure modeling remains unauthorized.

**EN:** Current NIST/Data.gov public metadata clearly establishes `ark:/88434/mds2-3761` and authoritative Part 1–4 ZIP endpoints, consistent with F15's registered schema/registration semantics. However, the official public metadata available in this session did not establish an exact data-bearing PDR release/version lineage or immutable checksums/equivalent byte identifiers for the ZIPs, and authoritative Part 1 bytes could not be retrieved through two verified zero-cost routes. Therefore F16 resolves to `PARTIAL_PUBLIC_ENDPOINT_READY`, not a full immutable-source PASS. Numerical process–structure modeling remains unauthorized.

## 2. Current official public identity / 현행 공식 공개 식별

Data.gov current metadata, last checked 2026-08-03, establishes:
- identifier: `ark:/88434/mds2-3761`;
- issued: `2025-05-09`;
- modified: `2025-03-13`;
- access level: public;
- `part1` → `https://data.nist.gov/od/ds/mds2-3761/part1.zip`;
- `part02` → `https://data.nist.gov/od/ds/mds2-3761/part02.zip`;
- `part03` → `https://data.nist.gov/od/ds/mds2-3761/part03.zip`;
- `part04` → `https://data.nist.gov/od/ds/mds2-3761/part04.zip`;
- documentation DOI: `10.6028/NIST.AMS.100-69`.

The NIST AMS publication independently describes the registered dataset as CSV files organized by layer and part and hosted at the same NIST dataset identifier.

## 3. Immutable provenance finding / immutable provenance 결과

Within the verified official public routes available in this session:
- no exact data-bearing PDR version identifier was established;
- no authoritative SHA-256 (or equivalent immutable byte-level identifier) for `part1.zip`–`part04.zip` was established;
- Data.gov provides direct current distribution URLs but not component hashes in the visible harvested metadata;
- no authoritative version-pinned component manifest was recovered.

This is an `UNKNOWN / DATA_GAP`, not evidence that NIST lacks internal integrity metadata.

## 4. Part 1 retrieval finding / Part 1 회수 결과

Two zero-cost authoritative retrieval mechanisms were tested after F16 freeze:
1. Data.gov → NIST download endpoint through the web retrieval path;
2. direct NIST URL through the provided transient download tool.

Both failed to return source bytes. The web path reported a cache/fetch failure; the transient downloader reported download failure.

A single pre-registration availability probe against the same official Part 1 URL had also failed and recovered zero bytes; this chronology was disclosed in the preregistration.

Result:
- Part 1 authoritative bytes retrieved: `NO`;
- local SHA-256: `NOT_COMPUTED`;
- archive inventory: `NOT_INSPECTED`;
- Parts 2–4 retrieval: `NOT_ATTEMPTED`, per frozen order requiring Part 1 to pass first.

## 5. Gate application / gate 적용

### `PASS_IMMUTABLE_SOURCE_READY`
- authoritative identity/current endpoints: PASS;
- exact release/version lineage: FAIL / NOT_VERIFIED;
- immutable integrity evidence all four ZIPs: FAIL / NOT_VERIFIED;
- Part 1 authoritative byte retrieval + verification: FAIL;
- Part 1 deterministic archive inventory: NOT_REACHED.

Result: **FAIL**.

### `PARTIAL_PUBLIC_ENDPOINT_READY`
- authoritative identifier/current endpoints established: PASS;
- F15 schema/registration semantics remain qualified: PASS;
- one or more of version lineage / immutable hashes / byte retrieval remain unverified: PASS;
- no source contradiction established: PASS.

Result: **PASS**.

### `HOLD_SOURCE_RETRIEVAL`
Not selected because immutable identity/hash evidence is not otherwise sufficient; the gap is broader than retrieval alone.

### `HOLD_PROVENANCE_OR_VERSION`
Not selected as the stronger final label because current authoritative public endpoints and dataset identity are coherent and usable for continued source qualification; no material provenance conflict was observed, only incomplete immutable provenance.

### `REJECT_SOURCE_MISMATCH`
Not applicable; no contradictory authoritative bytes were retrieved.

## 6. Final / 최종

**`PARTIAL_PUBLIC_ENDPOINT_READY`**

## 7. Consequence / 후속

Do **not** preregister or execute numerical in-situ melt-pool ↔ XCT modeling yet.

The next decision should not repeatedly hammer the same inaccessible endpoint. Preferred next work is to search for an authoritative zero-cost route that exposes either:
1. version-pinned PDR component metadata/checksums for `mds2-3761`; or
2. an official alternative distribution/cache with immutable integrity evidence.

If that cannot be established without paid resources, keep `mds2-3761` as a high-value qualified-but-not-immutable-ready asset and triage another external process–structure dataset. E14 remains frozen and unchanged.

No paid/potentially paid route was used.