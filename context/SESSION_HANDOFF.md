---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260822-D12-PREREG
active_issue: 29
active_research: AMBENCH-D12
last_completed_issue: 27
last_completed_research: AMBENCH-D11
last_decision: DEC-029
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Current State / 현재 상태
- **Checkpoint:** `CHK-20260822-D12-PREREG`
- **Active Issue:** #29 `AMBENCH-D12`
- **Active research:** `AMBENCH-D12`
- **Last completed:** #27 `AMBENCH-D11 — MIXED_TEMPORAL_INFORMATION`
- **Last decision:** `DEC-029`

## Cost Authority / 비용 권위
`COST-001` is clarified by `DEC-028`: any potentially billable action requires explicit user approval **before execution**. Spending first and reporting later is prohibited and not retroactive authorization. Unknown billing = `HOLD_COST_APPROVAL`. D12 may execute only on a verified zero-incremental-cost route.

## D11 Controlling Result / D11 지배 결과
- direct waveform strongly case-structured: `WF_MEDIAN_WITHIN=0.0043387546`, `WF_HIGH_REPEAT_FRACTION=0.0`;
- repeat-sensitive descriptors `5/8`: `iqr_mid`, `early_contrast`, `late_contrast`, `early_shape_slope`, `late_shape_slope`;
- `ac1_mid` mixed;
- `median_mid`, `mad_diff_mid` case-dominated;
- descriptor `PCA95_DIM=6`;
- final gate `MIXED_TEMPORAL_INFORMATION`.

## Active D12 / 활성 D12
Preregistration: `research/AMBENCH-D12/README.md`.

D12 asks whether D11 repeat-sensitive descriptor variation is:
1. sampling/representation sensitive;
2. consistently structured by repeat index across cases;
3. robust but condition-specific case×repeat variation;
4. mixed provenance.

Frozen diagnostics:
- reproduce D11 within-fractions to `<=1e-9` absolute tolerance;
- balanced case+repeat SS decomposition and `repeat_index_share`;
- factor-2 phases 0/1 and factor-4 phases 0/1/2/3 decimation, retaining original full-track `tau`;
- `R_sampling` with thresholds 3.0 / 1.5;
- secondary case-centered residual PCA on the five primary descriptors.

Frozen final gates:
`REPRESENTATION_SENSITIVITY_DOMINANT`, `CROSS_CASE_REPEAT_INDEX_STRUCTURE`, `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`, `MIXED_REPEAT_PROVENANCE`, `HOLD_DATA_INTEGRITY`.

No physical-cause, physical-outcome, predictive, generalization, or causal claim is authorized.
