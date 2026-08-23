---
checkpoint_id: CHK-20260823-D25-BLOCK-DOMINANT-HIERARCHICAL-STRUCTURE
active_issue: none
active_research: none
last_completed_issue: 43
last_completed_research: AMBENCH-D25
last_decision: DEC-052
updated: 2026-08-23
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline / 최신 검증 baseline:** `v0.31-d25-block-dominant-hierarchical-structure`  
**State / 상태:** `D25_COMPLETED__BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`  
**Active Work Queue / 활성 작업 큐:** none.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval **before execution**; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative external raw bytes are transient-only.
- `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.

## Completed AMBENCH Chain / 완료 계보
- #11 F02 — `PASS`
- #13 E03 — `NO_MATERIAL_GAIN`
- #15 F04 — `PARTIAL`
- #17 E05 — `MIXED`
- #19 D06 — `PROCESS_CASE_PROXY_DOMINANT`
- #21 F07 — `PARTIAL_SOURCE_READY`
- #22 F08 — `PARTIAL_CASE_LEVEL_READY`
- #24 E09 — `INCONCLUSIVE_CASE_LEVEL`
- #26 F10 — `HOLD_PUBLICATION_NOT_VERIFIED`
- #27 D11 — `MIXED_TEMPORAL_INFORMATION`
- #29 D12 — `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
- #31 F13 — `PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`
- #32 E14 — `HOLD_SOURCE_INTEGRITY`
- #33 F15 — `PARTIAL_REGISTERED_SCHEMA_READY`
- #34 F16 — `PARTIAL_PUBLIC_ENDPOINT_READY`
- #35 F17 — `PARTIAL_X16_SOURCE_READY`
- #36 F18 — `PARTIAL_MANAGEABLE_X16_ROUTE_READY`
- #37 F19 — `PARTIAL_F19_SEGMENTATION_RULE_READY`
- #38 F20 — `PASS_F20_WORKBOOK_IMMUTABLE_SCHEMA_READY`
- #39 F21 — `REJECT_F21_ENDPOINT_ROUTE`
- #40 F22 — `PARTIAL_F22_ALL_FOUR_IMMUTABLE_BYTES_READY__SCHEMA_HEADER_HOLD`
- #41 F23 — `PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`
- #42 E24 — `NO_MATERIAL_E24_ASSOCIATION`
- #43 D25 — **`D25_BLOCK_DOMINANT_HIERARCHICAL_STRUCTURE`**

## D25 Final / D25 최종
Preregistration: `research/AMBENCH-D25/README.md`.  
Execution: `research/AMBENCH-D25/EXECUTION_RESULT.md`.  
Result: `research/AMBENCH-D25/RESULT.md`.  
Claims: `CLM-086..088`. Decision: `DEC-052`. Memory: `MEM-047-AMBENCH-D25`.

### E24 reproduction / E24 재현
- source SHA ×4 exact PASS;
- 36/40 part×block units;
- 9/10 blocks; Block 1 excluded;
- beta `0.015305236`;
- predictor partial R² `0.019321313`;
- frozen reproduction integrity PASS.

### Outcome hierarchy / Outcome 계층
- part-only R² `0.000602`;
- block-only R² `0.998820`;
- part+block R² `0.999421`;
- block|part partial R² `0.999421`;
- part|block partial R² `0.509735` of the tiny post-block remainder;
- residual fraction after part+block `0.000579`.

The registered XCT aggregate outcome is therefore block/build-progression dominant under the frozen D25 gate.

### Predictor hierarchy / Predictor 계층
- part-only R² `0.747172`;
- block-only R² `0.205094`;
- part+block R² `0.952265`;
- residual fraction after part+block `0.047735`.

Thus the melt-pool predictor is itself strongly structured by part/location and block progression rather than behaving as a free independent perturbation.

### Sign structure / 부호 구조
- pooled beta `-0.278047`;
- part-adjusted `-1.026589`;
- block-adjusted `-0.022349`;
- part+block-adjusted `+0.015305`;
- `STRUCTURAL_SIGN_REVERSAL=YES`;
- `BLOCK_REMOVAL_EXPLAINS_REVERSAL=NO`.

All four part-specific x↔y Spearman diagnostics remain negative. The weak positive E24 beta is therefore a tiny fully adjusted residual estimand, not the dominant build-level association.

## Branch Decision / branch 결정
`DEC-052`: do not feature-fish, switch endpoints or increase model capacity on the same registered-X4 aggregate representation. E24 + D25 are informative negative evidence against a material local melt-pool-area → XCT-voxel association on this representation.

## Exact Next Eligible Work / 정확한 다음 행동
No experiment is active.

Next highest-leverage work is an **independent-condition / independently varied dataset qualification** before another mechanistic experiment. The next gate should prioritize a source where:
1. process variation is deliberately or naturally independent of part/block identity;
2. structural outcome variation is interpretable independently of deterministic build progression;
3. replication supports condition-level inference;
4. source integrity can be established through zero-cost official routes.

Do not automatically return to `mds2-3761`, X16, or high-capacity ML to rescue E24. E14 and preserved X16 branches remain unchanged. Any paid/potentially paid route requires explicit prior user approval.