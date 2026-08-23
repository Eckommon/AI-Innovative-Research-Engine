---
id: AMBENCH-F20
type: source-recovery-preregistration
state: PREREGISTERED
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F19/RESULT.md
  - mds2-2514
  - mds2-2309
---

# AMBENCH-F20 — X16 Authoritative Workbook Recovery / X16 권위 workbook 회수 gate

## 1. Purpose / 목적
Resolve the final F19 blocker without numerical outcome access: recover immutable authoritative identity/bytes for `OverhangX16_ImageHistograms.xlsx`, inspect schema only, and verify whether the already-frozen F19 segmentation rule can later be validated on authoritative XYPT bytes.

F19 이후 남은 마지막 핵심 blocker를 numerical outcome 접근 없이 해소한다: `OverhangX16_ImageHistograms.xlsx`의 immutable authoritative identity/bytes를 회수하고 schema만 확인하며, 이미 고정된 F19 segmentation rule을 authoritative XYPT bytes에서 후속 검증할 수 있는 source path를 판정한다.

## 2. Frozen source / 고정 source
XCT:
- current authoritative dataset identity: `ark:/88434/mds2-2514`;
- `OverhangX16_ImageHistograms.xlsx`;
- `OverhangX16_ImageHistograms.xlsx.sha256`.

In-situ preserved from F18/F19:
- `ark:/88434/mds2-2309`;
- `XYPT_L101-L125.zip` + `.sha256`;
- `DAQ_L101-L125.zip` + `.sha256`.

No MPM/TIFF/STL expansion is authorized.

## 3. Frozen official recovery order / 고정 공식 회수 순서
1. current Data.gov POD metadata;
2. NIST PDR landing/version metadata;
3. NIST RMM/NERDm machine-readable metadata;
4. alternate NIST official `od/ds` component URLs if explicitly supported by official metadata;
5. direct authoritative component retrieval only after identity is established.

No unofficial mirror, digitized value, inferred hash, or search-result copy may substitute for authoritative NIST bytes/metadata.

## 4. Workbook qualification / workbook 판정
PASS requires one of the following immutable integrity routes:
- authoritative `.sha256` sidecar byte retrieval plus workbook byte retrieval and local hash match; or
- an authoritative NIST machine-readable metadata record that explicitly publishes an equivalent immutable checksum for the exact workbook, followed by workbook byte retrieval and local hash match.

Metadata-only existence of a `.sha256` URL is insufficient for immutable-byte PASS.

If workbook bytes are recovered, F20 may inspect **schema only**:
- workbook/sheet names;
- row/column counts;
- header text;
- merged ranges;
- formula presence/locations;
- explicit part identifiers and their mapping structure.

F20 must not report, summarize, rank, correlate, or model numerical XCT values. Cell values that are purely part labels/header text may be read; numerical outcome cells remain protected.

## 5. Segmentation preservation / segmentation 보존
F19 rule remains unchanged:
- layer 125 authoritative XYPT commanded laser-on X/Y;
- deterministic `k=16` physical-coordinate clustering;
- NIST Figure-1 topology maps left→right prefixes `1..4`, top→bottom suffixes `1..4`;
- frozen-centroid Voronoi assignment for DAQ actual X/Y;
- no manual relabeling, boundary digitization, or outcome-aware tuning.

F20 does not redesign this rule. It only determines whether authoritative XYPT bytes/checksum can be recovered under the same zero-cost constraints for future numeric validation.

## 6. Frozen gates / 고정 판정
1. `PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`
   - exact workbook immutable integrity verified;
   - schema-only inspection completed;
   - 16-part mapping semantics sufficient;
   - authoritative XYPT validation path remains viable.

2. `PARTIAL_F20_MACHINE_METADATA_ADVANCE`
   - official machine-readable metadata provides materially stronger version/hash/component provenance than F19, but exact workbook bytes/local hash or schema remain incomplete.

3. `HOLD_F20_AUTHORITATIVE_WORKBOOK_ACCESS`
   - workbook/sidecar authoritative bytes remain unavailable and no equivalent authoritative immutable checksum can be recovered.

4. `HOLD_F20_WORKBOOK_SCHEMA`
   - workbook bytes verified but schema does not establish deterministic 16-part summary semantics without reading/tuning on outcomes.

5. `REJECT_F20_ROUTE`
   - authoritative source contradicts identity, integrity, or intended X16 pairing.

## 7. Outcome blindness / outcome 보호
`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` at freeze.

Forbidden in F20:
- XCT numerical outcome extraction;
- DAQ/XYPT numerical process summaries;
- process↔XCT statistics;
- model fitting;
- feature selection based on outcome values;
- layer-group changes or raw-source expansion as rescue.

## 8. Cost / 비용
`COST-001` + `DEC-028` apply. Only verified zero-incremental-cost public NIST/Data.gov routes and provided transient compute may be used. Any potentially billable route requires explicit user approval before execution.
