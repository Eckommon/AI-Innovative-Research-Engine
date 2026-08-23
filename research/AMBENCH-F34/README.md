---
id: AMBENCH-F34
type: preregistration
state: PREREGISTERED_SOURCE_DESIGN_GATE_ACTIVE
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-E33
  - DEC-070
incremental_monetary_cost_usd: 0
---

# AMBENCH-F34 — Independent External Scan-History Falsification Source Gate
# AMBENCH-F34 — 독립 외부 Scan-History 반증 Source Gate

## Purpose / 목적

**KO:** E33의 강한 within-experiment prior-scan-history ↔ melt-pool geometry association을 동일 데이터셋에서 추가 최적화하지 않고, 독립 물리 build/measurement source에서 반증 가능한지 먼저 source/design 수준에서 검증한다.

**EN:** After E33's strong within-experiment prior-scan-history ↔ melt-pool-geometry association, do not optimize the same dataset further. First determine whether an independent physical build/measurement source can support an external scan-history falsification at source/design level.

F34 performs no candidate numerical outcome analysis and no predictive/model fitting.

## Frozen priority source / 고정 우선 source

NIST **Process Monitoring Dataset from the Additive Manufacturing Metrology Testbed (AMMT): 3D Scan Strategies**.

- DOI: `10.18434/M32044`;
- legacy PDR identifier: `mds1103vzr`;
- current release lineage reaches `v1.0.4` (2026-01-08 metadata/additiveman update);
- material/build: IN625 LPBF/AMMT 3D build;
- official NIST summary: ten rectangular parts with replicated geometry and varied scan strategies;
- monitoring: in-situ melt-pool monitoring, with layer imaging and input command files documented;
- current PDR exposes four checksum-addressable top-level archives.

Known current PDR component metadata before F34 execution:
- `Build Command Data.zip` — ~`7.42 GB`, SHA-256 `de8a05ebd27f80bd79b6545c9f8a79c0e60230290e1799d9151f14f7429594b1`;
- `In-situ Meas Data.zip` — ~`9.17 GB`, SHA-256 `4db83f84cce2f4a28e75830a5df496c9a04db5e5554513924434463081ab645f`;
- `Metadata.zip` — ~`2.49 MB`, SHA-256 `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`;
- `Movies.zip` — ~`699 MB`, SHA-256 `df63cbc6f07c0cad11cff2f01355ac583da0079d04370f21e9a93f746319c545`.

## Why this source is a candidate / 후보 사유

Compared with E33 `mds2-3662`, M32044 is a different physical build and monitoring context while retaining IN625 LPBF and explicit scan-strategy variation. It may therefore support a stronger external falsification than another reanalysis of the E33 workbook.

However, F34 must **not** call it a replication until independent-unit, scan-strategy, layer/part identity, monitoring assignment and usable outcome semantics are directly recovered from authoritative source records.

## Allowed / 허용
- current official NIST PDR/NERDm metadata and release lineage;
- NIST data-description/publication design text;
- `Metadata.zip` only, if its current bytes match the PDR checksum;
- filenames, schemas, metadata values describing part IDs, layer IDs, scan-strategy assignments, sensor assignment, acquisition semantics and build hierarchy;
- archive member names and small text/CSV/JSON/YAML/XML metadata contents;
- zero-cost standard GitHub-hosted execution.

## Forbidden / 금지
During F34 source/design qualification:
- do not download/open `Build Command Data.zip` (~7.42 GB);
- do not download/open `In-situ Meas Data.zip` (~9.17 GB);
- do not download/open `Movies.zip` (~699 MB);
- do not inspect candidate melt-pool image/intensity/area/quality numerical outcomes;
- do not rank scan strategies by observed outcome;
- do not fit models or define thresholds from candidate outcomes;
- do not add a different source after F34 source evidence is inspected;
- do not incur paid API/cloud/SaaS/GPU/storage cost.

## Frozen qualification dimensions / 고정 적격성 차원

1. **Immutable source identity** — current PDR/version/component checksums are recoverable and `Metadata.zip` bytes match official SHA-256.
2. **Independent physical units** — build hierarchy identifies distinct parts/replicates/layers without treating frames as independent physical units.
3. **Explicit scan-strategy intervention** — source metadata identifies scan-strategy variation across otherwise comparable geometry/part conditions; variation is not merely sensor assignment.
4. **Deterministic strategy→monitoring route** — part/layer/strategy identifiers can map to in-situ monitoring files without opening their measurement values.
5. **Outcome semantics** — documented monitoring or physical-quality measurand exists that can later be frozen into a low-DOF external falsification endpoint.
6. **Claim-transfer integrity** — a future experiment can test a scan-history/residual-heat concept without claiming same construct, same machine, same geometry, or direct row-level identity with E33.
7. **Zero-cost feasibility** — source/design gate can be completed using metadata/small files only; multi-GB archives remain unopened until a separately preregistered experiment proves they are necessary and cost-safe.

## Frozen gates / 고정 gate

### `PASS_F34_EXTERNAL_SCAN_HISTORY_SOURCE_READY`
All seven dimensions PASS. A separate numerical experiment may then be preregistered before opening candidate outcomes.

### `PARTIAL_F34_METADATA_READY_OUTCOME_ROUTE_GAP`
Source identity, independent units and scan-strategy design are recoverable, but deterministic monitoring/outcome route or low-DOF endpoint semantics remain incomplete without opening large archives.

### `HOLD_F34_SOURCE_OR_IDENTITY_GAP`
Authoritative identifiers, physical-unit hierarchy or strategy mapping cannot be established from current zero-cost public metadata.

### `REJECT_F34_NOT_INDEPENDENT_SCAN_HISTORY_TEST`
The source does not provide a defensible independent scan-history/residual-heat falsification axis.

## Exposure / 노출

`NEW_F34_CANDIDATE_NUMERICAL_OUTCOME_BLIND = YES`

Known before source qualification: official dataset purpose, presence of varied scan strategies, replicated rectangular geometry, monitoring modalities, archive names/sizes/checksums and publication design context. No M32044 candidate numerical monitoring/quality result is used to select or gate the source.

## Exact work order / 정확한 작업 순서
1. resolve current `mds1103vzr` NERDm/PDR version identity;
2. verify all top-level component path/size/checksum metadata;
3. download only `Metadata.zip` and require exact SHA-256 match;
4. inventory member names and inspect metadata-only small files;
5. recover part/layer/scan-strategy/sensor hierarchy and deterministic file-ID semantics;
6. evaluate the seven frozen dimensions;
7. assign exactly one F34 gate;
8. write back result, Issue state, claims/decision and synchronized `STATUS.md`;
9. only after PASS may a separate external numerical hypothesis be preregistered.

## Capability / Portfolio / 비용
Reuse source-integrity/schema-only patterns; classification remains `SHARED-INTERNAL-CANDIDATE`. No new Skill/MCP/Plugin/shared paid resource is authorized. Incremental monetary cost: `0 USD`.
