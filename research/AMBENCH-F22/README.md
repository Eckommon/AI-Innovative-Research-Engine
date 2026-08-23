---
id: AMBENCH-F22
type: feasibility-preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-F22 — `mds2-3761` NERDm Immutable Source Recovery
# AMBENCH-F22 — `mds2-3761` NERDm 불변 source 회수

## Purpose / 목적

**KO:** F15/F16에서 schema는 확인됐지만 immutable source integrity가 미확립이었던 NIST fully registered X4 dataset `mds2-3761`을 F20에서 검증된 zero-cost NERDm + transient GitHub-hosted runner 방식으로 재검증한다. 본 단계는 source/identity/inventory gate이며 numerical process↔XCT 분석이 아니다.

**EN:** Re-evaluate immutable source integrity for NIST fully registered X4 dataset `mds2-3761`, whose schema was qualified in F15/F16 but whose component bytes/checksums were not. Apply the F20-proven zero-cost NERDm + transient public GitHub-hosted runner pattern. This is a source/identity/inventory gate, not a numerical process↔XCT experiment.

## Frozen authoritative dataset / 고정 권위 dataset
- identifier: `ark:/88434/mds2-3761`
- current Data.gov distributions:
  - `part1.zip`
  - `part02.zip`
  - `part03.zip`
  - `part04.zip`
- description: NIST AMS 100-69 / DOI `10.6028/NIST.AMS.100-69`.

## Frozen recovery order / 고정 회수 순서
1. fetch current `https://data.nist.gov/od/id/mds2-3761?format=nerdm`;
2. exact-match the four registered ZIP components;
3. require SHA-256 checksum metadata and official NIST downloadURL for each component;
4. transiently retrieve `part1.zip` first on a public standard GitHub-hosted `ubuntu-latest` runner;
5. verify local SHA-256 against authoritative NERDm hash;
6. inspect archive inventory and CSV schema only — no numerical outcome values;
7. expand to parts 2–4 only if part1 byte/hash gate passes;
8. raw ZIP/CSV bytes are transient only; no artifact/cache/raw commit.

## Frozen inventory/schema checks / 고정 inventory·schema 검사
For each byte-valid part archive:
- ZIP opens successfully;
- exactly 250 CSV members expected, one per layer;
- deterministic layer identifier coverage 1..250 must be recoverable from filenames or archive structure without reading numerical outcomes;
- CSV header width must be 40 columns as documented in AMS 100-69;
- header names may be recorded; numerical data rows may not be emitted or summarized in F22.

If filename convention prevents an exact layer-number proof, record the exact inventory evidence and apply PARTIAL/HOLD rather than infer.

## Frozen gates / 고정 판정

### `PASS_F22_REGISTERED_X4_IMMUTABLE_SOURCE_READY`
All four ZIPs satisfy:
- exact NERDm component identity;
- authoritative SHA-256 and NIST downloadURL;
- transient byte retrieval;
- local SHA-256 exact match;
- valid archive inventory consistent with 250 layer CSVs;
- 40-column header/schema verification;
- no material identity conflict.

### `PARTIAL_F22_PART1_BYTE_READY`
- all-four NERDm immutable metadata is established; and
- `part1.zip` passes local byte/hash/inventory/schema checks; but one or more remaining part ZIPs are not byte-verified.

### `PARTIAL_F22_IMMUTABLE_METADATA_READY`
- NERDm establishes exact component SHA-256 + URLs for the relevant ZIPs, but no ZIP completes local byte verification.

### `HOLD_F22_SOURCE_ACCESS`
- authoritative metadata exists but current verified zero-cost execution cannot retrieve enough bytes to establish even the part1 byte gate.

### `REJECT_F22_INTEGRITY_MISMATCH`
- authoritative/local hash mismatch, invalid ZIP, material component identity conflict, or archive structure contradicts the documented registered dataset.

## Outcome boundary / outcome 경계
`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = YES`.

F22 may inspect:
- metadata;
- hashes;
- file names;
- archive counts;
- CSV headers/schema.

F22 may **not** inspect, aggregate, compare, model, or emit numerical process/melt-pool/LWI/XCT values.

## Cost / 비용
Zero-incremental-cost official public routes only. Public standard GitHub-hosted runners are allowed under the already-verified public-repository zero-cost rule. No larger runner, paid API/source, artifact storage, cache, or paid service. Any potentially billable route requires explicit prior user approval.

## Consequence / 후속
Only `PASS_F22_REGISTERED_X4_IMMUTABLE_SOURCE_READY` authorizes a separately preregistered low-degree-of-freedom registered process/melt-pool ↔ XCT experiment. PARTIAL/HOLD states do not authorize modeling.
