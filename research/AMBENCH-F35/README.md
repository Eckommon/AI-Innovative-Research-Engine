---
id: AMBENCH-F35
type: preregistration
state: PREREGISTERED_SOURCE_DESIGN_GATE_ACTIVE
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-E33
  - AMBENCH-F34
  - DEC-072
incremental_monetary_cost_usd: 0
---

# AMBENCH-F35 — NIST RHF Residual-Heat External Source/Identity Gate
# AMBENCH-F35 — NIST RHF 잔류열 외부 Source/Identity Gate

## Purpose / 목적

**KO:** E33에서 관찰된 equivalent-track-length / prior-scan-history 연관을 더 직접적인 독립 물리 실험에서 반증·확인할 수 있는지 판단하기 위해 NIST RHF dataset `mds2-2507`을 source/design 수준에서 적격성 평가한다.

**EN:** Qualify NIST RHF dataset `mds2-2507` at source/design level as a more direct independent physical test of the equivalent-track-length / prior-scan-history relationship observed in E33.

F35 performs source/identity/design qualification only. It does not compute a RHF treatment effect, re-estimate publication outcomes, or fit a model.

## Frozen source / 고정 source

NIST `Process Monitoring Dataset from the Additive Manufacturing Metrology Testbed (AMMT): RHF Experiment`, DOI `10.18434/MDS2-2507`.

Prospectively known from official NIST sources before raw dataset inspection:
- IN625 bare-plate laser scans on the AMMT;
- 2 mm × 3 mm patches / pads with varying laser power and speed profiles;
- NIST AMMT Datasets page describes a layout of 55 pads;
- associated RHF paper defines a Residual Heat Factor from temporal and spatial scan history and controls laser power proportional to RHF;
- in-situ melt-pool monitoring and post-process quality measurements were used.

## Publication-level exposure / 논문 수준 사전노출

Before F35 preregistration, the official NIST publication abstract had already disclosed a directional publication-level conclusion that RHF-based compensation reduced melt-pool-size variability.

Permanent disclosure:

`NEW_F35_PUBLICATION_LEVEL_OUTCOME_BLIND = NO__DIRECTIONAL_RHF_RESULT_PREOBSERVED`

However:

`NEW_F35_RAW_DATA_NUMERICAL_OUTCOME_BLIND = YES`

at preregistration, meaning no `mds2-2507` numerical monitoring, microscopy, quality-result, or treatment-effect value has been opened or used to choose the source gate.

Any descendant numerical execution must be confirmatory/reproduction, not pristine discovery.

## Allowed / 허용
- current official NIST PDR/NERDm metadata and version lineage;
- official RHF data-description/source documentation;
- component names, sizes, SHA-256, identifiers and file schemas;
- small documentation/design files after exact current checksum verification;
- archive member names without opening measurement values, when an archive itself is small enough and clearly design/documentation-only;
- experiment hierarchy, patch/pad IDs, scan strategies, power/velocity profiles, control/treatment labels, camera/file naming, microscopy/file naming and timing semantics;
- zero-incremental-cost standard execution only.

## Forbidden / 금지
During F35:
- no candidate numerical MPM/microscopy/quality outcome values;
- no RHF-vs-control effect calculation;
- no ranking of conditions by outcome;
- no post-hoc endpoint selection;
- no image processing/model fitting;
- no large/raw measurement download unless the source gate separately establishes necessity, bounded size and zero-cost safety;
- no paid API/cloud/SaaS/GPU/storage.

## Frozen qualification dimensions / 고정 적격성 차원

1. **Immutable source identity** — current version, component names/sizes/checksums and relevant small-document bytes can be frozen.
2. **Independent experiment/unit semantics** — physical patches/pads/tracks/repeats and nesting can be identified without treating frames/pixels as independent units.
3. **Direct residual-history intervention** — source design explicitly distinguishes RHF/residual-history-aware power control from appropriate comparator conditions, rather than only varying generic P/V parameters.
4. **Deterministic condition→monitoring route** — condition/pad/track IDs map to MPM records without using outcomes.
5. **Deterministic condition→post-process route** — condition/pad/track IDs map to visible-light microscopy or other post-process physical-quality records without invented identity.
6. **Low-DOF confirmatory experimentability** — a small predefined descriptor/statistic can later test RHF/residual-history transfer without high-capacity ML or pseudo-replication.
7. **Claim-transfer integrity / cost** — future result can be bounded as independent RHF/residual-history confirmation, not same-construct E33 replication, and required source qualification remains zero incremental cost.

## Frozen gates / 고정 gate

### `PASS_F35_RHF_EXTERNAL_CONFIRMATORY_SOURCE_READY`
All seven dimensions PASS. A separate frozen confirmatory numerical experiment may then be preregistered.

### `PARTIAL_F35_RHF_DESIGN_READY_ROUTE_GAP`
Direct RHF design and authoritative source are established but exact MPM/post-process pairing, independent-unit structure, or bounded numerical route is incomplete.

### `HOLD_F35_RHF_SOURCE_OR_IDENTITY_GAP`
Current authoritative public source cannot establish the required experiment/source semantics without unsupported substitution.

### `REJECT_F35_NOT_INDEPENDENT_RESIDUAL_HISTORY_TEST`
The public dataset does not actually expose a defensible independent residual-history test relevant to E33.

## Exact work order / 정확한 작업 순서
1. resolve current `mds2-2507` NERDm/PDR version and complete component inventory;
2. freeze current file identities, sizes and checksums;
3. identify small design/documentation files and verify exact bytes before reading;
4. recover pad/condition/RHF/control hierarchy and independent physical units without outcomes;
5. recover deterministic MPM and post-process file-ID semantics;
6. determine whether any required raw archive can remain unopened during source qualification;
7. apply the seven frozen dimensions and exactly one gate;
8. write result/decision/claim/Issue/STATUS and re-read;
9. only after PASS may a separate confirmatory numerical hypothesis be preregistered.

## Capability / Portfolio / 비용
Reuse source-integrity/preregistration patterns; classification remains `SHARED-INTERNAL-CANDIDATE`. No new Skill/MCP/Plugin/shared paid resource is authorized. Incremental monetary cost: `0 USD`.
