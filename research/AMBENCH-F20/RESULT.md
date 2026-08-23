---
id: AMBENCH-F20-RESULT
type: source-recovery-result
state: COMPLETED_PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F20/README.md
  - research/AMBENCH-F20/RUN_RESULT.md
  - research/AMBENCH-F20/XYPT_NERDM_INVENTORY.md
  - research/AMBENCH-F20/XYPT_RUN_RESULT.md
  - Issue #38
---

# AMBENCH-F20 Result — X16 Authoritative Workbook Recovery / Schema Qualification
# AMBENCH-F20 결과 — X16 권위 workbook 회수 / schema qualification

**Frozen final gate / 고정 최종 판정:** **`PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`**

## 1. Executive result / 핵심 결과

**KO:** F20은 F19 이후 남아 있던 X16 XCT workbook blocker를 해결했다. NIST NERDm machine-readable metadata에서 `mds2-2514/OverhangX16_ImageHistograms.xlsx`의 SHA-256을 확보했고, public standard GitHub-hosted runner에서 authoritative workbook을 transient하게 회수하여 local SHA-256을 계산한 결과 NERDm checksum과 정확히 일치했다. 수치 outcome을 출력하지 않는 XML-level schema inspection은 `Plots` sheet와 `Part1_1`…`Part4_4`의 정확히 16개 part sheet를 확인했으며, 각 part sheet는 `A1:B256`, formula 0개였다. 따라서 workbook의 immutable byte identity와 16-part sheet mapping은 qualified 되었다.

동시에 `mds2-2309` NERDm metadata-only inventory는 frozen in-situ source `XYPT_L101-L125.zip`을 정확한 component로 확인하고 authoritative SHA-256, byte size, downloadURL을 제공한다. direct `.sha256` sidecar/ZIP HTTP retrieval은 해당 실행에서 실패했으나, F20 PASS가 요구한 것은 F19 segmentation을 향후 검증할 authoritative XYPT validation path의 viability이며, current NERDm의 exact component identity + SHA-256 + official URL은 이 조건을 충족한다. F20은 XYPT numerical values를 읽거나 segmentation을 실행하지 않았다.

**EN:** F20 resolves the remaining X16 XCT workbook blocker from F19. NIST NERDm machine-readable metadata provided the SHA-256 for `mds2-2514/OverhangX16_ImageHistograms.xlsx`; the authoritative workbook was transiently retrieved on a public standard GitHub-hosted runner and its locally computed SHA-256 exactly matched the NERDm checksum. XML-level schema-only inspection, without emitting numerical outcomes, established one `Plots` sheet plus exactly sixteen part sheets `Part1_1`…`Part4_4`; every part sheet has dimension `A1:B256` and zero formulas. The workbook therefore has qualified immutable byte identity and deterministic 16-part sheet mapping.

For the preserved in-situ route, an mds2-2309 NERDm metadata-only inventory identifies the frozen `XYPT_L101-L125.zip` component with an authoritative SHA-256, byte size, and official downloadURL. Direct sidecar/ZIP retrieval failed in that execution, but the F20 PASS criterion requires the authoritative XYPT validation path for the frozen F19 segmentation to remain viable; current exact NERDm component identity + checksum + official URL satisfies that source-provenance condition. F20 did not read XYPT numerical values or execute segmentation.

## 2. Workbook immutable integrity / workbook immutable 무결성

Authoritative current source:
- dataset: `ark:/88434/mds2-2514`;
- component: `OverhangX16_ImageHistograms.xlsx`;
- NERDm size: `193261` bytes;
- NERDm SHA-256: `7cc48fc8aa7a86af4e00c24bfcf91373ef15a8bc1e10d404e61ba8f4d29c422f`.

Zero-cost transient execution result:
- authoritative workbook download: `PASS`;
- local SHA-256: `7cc48fc8aa7a86af4e00c24bfcf91373ef15a8bc1e10d404e61ba8f4d29c422f`;
- expected/actual match: `YES`;
- raw workbook committed: `NO`;
- artifact/cache: `NONE`;
- raw transient teardown: `SUCCESS`.

Therefore the exact workbook bytes used for schema qualification are cryptographically tied to current authoritative NIST NERDm metadata.

## 3. Workbook schema-only qualification / workbook schema-only 판정

No numerical outcome cell values were emitted or summarized.

Observed workbook structure:
- `Plots` — dimension `A1`, formula count `0`;
- exactly sixteen part sheets:
  - `Part1_1`, `Part1_2`, `Part1_3`, `Part1_4`;
  - `Part2_1`, `Part2_2`, `Part2_3`, `Part2_4`;
  - `Part3_1`, `Part3_2`, `Part3_3`, `Part3_4`;
  - `Part4_1`, `Part4_2`, `Part4_3`, `Part4_4`;
- every part sheet dimension: `A1:B256`;
- every part sheet formula count: `0`.

This establishes deterministic workbook-level part identity mapping matching the X16 `1-1`…`4-4` technical-replicate family.

Boundary: F20 does **not** infer the physical meaning of columns A/B or the numerical histogram endpoint from sheet dimensions alone. Endpoint semantics must be frozen from authoritative documentation before E19 numerical outcome access.

## 4. XYPT authoritative validation path / XYPT 권위 검증 경로

Current mds2-2309 NERDm metadata-only inventory:
- component filepath: `XYPT_L101-L125.zip`;
- downloadURL: `https://data.nist.gov/od/ds/ark:/88434/mds2-2309/XYPT_L101-L125.zip`;
- size: `157616390` bytes;
- checksum algorithm: `sha256`;
- authoritative SHA-256: `b5f6c58540799f57c64b59ab4c0770f1aad8ac32b6bfb3161babdf244e32ff31`.

NERDm also exposes the separate sidecar component `XYPT_L101-L125.zip.sha256` with its own SHA-256 metadata.

A direct sidecar/ZIP retrieval attempt through the current runner returned failure and no local XYPT checksum was computed. This is recorded and is not silently converted into a byte-access PASS.

However, F20's frozen PASS criterion only requires that the already-frozen F19 segmentation has an authoritative future validation path. Exact NERDm component identity, immutable checksum and official source URL establish that path. Future numerical segmentation validation must still retrieve authoritative XYPT bytes and match `b5f6c58540799f57c64b59ab4c0770f1aad8ac32b6bfb3161babdf244e32ff31` before reading numerical XYPT content.

## 5. Outcome blindness / outcome 보호

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains intact.

F20 did not:
- emit or summarize XCT numerical histogram cells;
- read numerical XYPT values;
- read numerical DAQ values;
- compute part process signatures;
- compute process↔XCT associations;
- fit models;
- tune layer groups, segmentation, features, or endpoints based on outcomes.

The schema-only inspection and NERDm metadata inventory are non-outcome source qualification steps.

## 6. Cost / 비용

The repository is public and the execution used only a standard GitHub-hosted `ubuntu-latest` runner. Current GitHub policy states that standard GitHub-hosted runners are free in public repositories. No larger runner, artifact storage, cache, paid API, paid source, or paid compute route was used.

Incremental monetary cost: **`0 USD`**.

## 7. Frozen gate application / 고정 gate 적용

### `PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`
- exact workbook immutable integrity verified: **PASS**;
- schema-only inspection completed: **PASS**;
- deterministic sixteen-part workbook mapping: **PASS**;
- authoritative XYPT validation path remains viable: **PASS** via current NERDm exact component identity + SHA-256 + official URL;
- numerical outcome blindness preserved: **PASS**.

Result: **PASS**.

### Other gates
- `PARTIAL_F20_MACHINE_METADATA_ADVANCE`: not selected; workbook byte/hash/schema qualification is complete.
- `HOLD_F20_AUTHORITATIVE_WORKBOOK_ACCESS`: not applicable; workbook was retrieved and hash matched.
- `HOLD_F20_WORKBOOK_SCHEMA`: not applicable; sixteen-part sheet mapping is deterministic.
- `REJECT_F20_ROUTE`: not applicable; no source contradiction or integrity mismatch was observed.

## 8. Final / 최종

**`PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`**

## 9. Consequence / 후속

F20 removes the workbook/source-identity blocker but does **not** authorize immediate outcome analysis.

Before any E19 numerical process↔XCT experiment, the next preregistration must freeze:
1. authoritative semantic meaning of workbook columns A/B and the exact XCT endpoint/transform;
2. authoritative XYPT byte retrieval + local checksum match to `b5f6c58540799f57c64b59ab4c0770f1aad8ac32b6bfb3161babdf244e32ff31` before segmentation validation;
3. the already-frozen F19 `k=16` segmentation validation criteria without redesign;
4. exact DAQ/XYPT process-signature construction from L101–125;
5. treatment of 16 parts as within-build technical replicates, not independent process conditions;
6. exact low-degree-of-freedom statistics/null/final gates;
7. no high-capacity ML or outcome-aware feature selection.

If authoritative documentation is insufficient to freeze workbook column semantics, insert a narrow semantics feasibility gate before E19 rather than guessing.