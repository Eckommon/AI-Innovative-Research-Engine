---
checkpoint_id: CHK-20260904-US-MINERAL-E01-PREREGISTERED
active_issue: 75
active_research: US-MINERAL-E01
last_completed_issue: 74
last_completed_research: US-MINERAL-F01
last_decision: DEC-105
updated: 2026-09-04
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__US_MINERAL_F01_PASS__US_MINERAL_E01_PREREGISTERED_OUTCOME_BLIND`  
**Active Work Queue / 활성 작업 큐:** Issue #75 `US-MINERAL-E01 — 2023 Critical-Mineral Source × Unlading-District Dual Trade-Value Concentration`.

## Fixed Mission / 고정 목적

Discover and validate **new, falsifiable, reproducible and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**. `MEM-054` remains mandatory.

## Last completed work / 마지막 완료 작업

Issue #74 / `US-MINERAL-F01` completed as:

**`PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY`**.

The gate established a deterministic source-semantic bridge from the Final 2025 U.S. critical-mineral universe through USGS Appendix-2 trade-code semantics to Census 2023 public import-node data for a prospectively qualified subset.

### Frozen primary `IMP_DETL` subset — 8 / 60

`Antimony, Barite, Beryllium, Palladium, Phosphate, Potash, Rhodium, Tellurium`.

### Frozen HS6 identity-preserving port subset — 6 / 8

`Antimony, Barite, Palladium, Phosphate, Potash, Rhodium`.

Prospective exclusions across the final 60 were applied before outcomes:
- no one-to-one Appendix-2 mapping: 6;
- multi-stage/multi-form family: 12;
- rare-earth special disaggregation: 15;
- shared expanded 2023 HTS10: 9;
- transaction unit-value allocation: 8;
- unresolved 2023 HTS vintage: 2;
- support-qualified: 8.

No Census trade row, country/district concentration, HHI, top-share, ranking, correlation or regression was opened/computed during F01.

Durable records:
- `research/US-MINERAL-F01/SOURCE_PREFLIGHT.md`;
- `research/US-MINERAL-F01/MAPPING_IDENTIFIABILITY.md`;
- `research/US-MINERAL-F01/EXECUTION_CONTRACT.md`;
- `research/US-MINERAL-F01/RESULT.md`;
- `registry/CLM-124.md`;
- `registry/DEC-105.md`;
- Issue #74 closed completed.

Incremental monetary cost: **0 USD**.

## Active E01 preregistration / 활성 E01 사전등록

`US-MINERAL-E01` is now **`PREREGISTERED_OUTCOME_BLIND`**.

Frozen primary design:
- universe: all 8 F01-qualified minerals, no post-outcome selection;
- period: 2023-01 through 2023-12;
- source: Census monthly Merchandise Trade Imports `IMP_DETL.TXT`;
- primary weight: `gen_val_mo` = General Imports, Total Value;
- primary foreign axis: country of origin;
- primary domestic axis: district of unlading;
- primary statistics: `H_country`, `H_unlad`, `D=min(H_country,H_unlad)`;
- materiality heuristic: `D >= 0.25`;
- replicated count: `K = number of 8 minerals crossing the dual threshold`.

Frozen gate:
- `PASS_E01_REPLICATED_DUAL_TRADE_VALUE_CONCENTRATION` if `K >= 2`;
- `PARTIAL_E01_SINGLE_DUAL_TRADE_VALUE_CONCENTRATION` if `K = 1`;
- `NO_E01_DUAL_TRADE_VALUE_CONCENTRATION` if `K = 0`;
- `HOLD_E01_SOURCE_OR_NUMERICAL_INTEGRITY` if the full frozen experiment cannot execute without prohibited alteration.

Interpretation is explicitly limited to **published general-import trade-value exposure concentration**, not physical mineral tonnage or causal supply-risk.

Durable preregistration:
- Issue #75;
- `research/US-MINERAL-E01/README.md`.

## Exposure boundary / 노출 경계

No E01 `gen_val_mo` outcome has yet been parsed, aggregated, ranked or persisted.

The next execution must preserve two stages:
1. Stage A — source manifest + identity/cardinality/full-key duplicate gate, with no numerical `gen_val_mo` parsing;
2. Stage B — only after Stage A PASS, parse the frozen values once and compute the preregistered metrics/gate.

No mineral/window/weight/geography/threshold retuning is allowed after Stage B begins.

## Exact next action / 정확한 다음 행동

1. Confirm State Integrity for `CHK-20260904-US-MINERAL-E01-PREREGISTERED`.
2. Implement one fail-closed E01 workflow from the committed README without changing the scientific contract.
3. Execute Stage A first and persist the 12-month Census source manifest/hash/cardinality diagnostics.
4. Only if Stage A passes, allow Stage B to compute the frozen 8-mineral 2023 trade-value concentration results.
5. Persist `RESULT.md`, claim/decision records and close Issue #75.
6. Return to mandatory mission-level review after E01 regardless of PASS/PARTIAL/NO/HOLD; do not run same-branch tuning automatically.

Incremental monetary cost remains **0 USD**. Any potentially billable work requires explicit prior user approval.
