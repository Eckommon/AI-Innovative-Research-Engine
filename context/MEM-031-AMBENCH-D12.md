---
id: MEM-031-AMBENCH-D12
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D12/RESULT.md
  - DEC-030
---

# MEM-031 — AMBENCH-D12 Durable Memory / 지속 메모리

`AMBENCH-D12` completed as **`ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`**.

Key durable facts / 핵심 사실:
- exact NIST `mds2-3842` v1.0.3 source and D11 descriptor reproduction passed;
- D11 primary repeat-sensitive descriptors: `iqr_mid`, `early_contrast`, `late_contrast`, `early_shape_slope`, `late_shape_slope`;
- sampling-phase diagnostic: all `5/5` primary descriptors `ROBUST_TO_SAMPLING_PHASE` with `R_sampling` from about `6.09` to `41.11`;
- balanced repeat decomposition: all `5/5` primary descriptors `CASE_SPECIFIC_RESIDUAL_DOMINANT`, `repeat_index_share <= 0.25`;
- primary counts: representation-sensitive `0/5`, sampling-robust `5/5`, cross-case repeat-index structured `0/5`, condition-specific residual dominant `5/5`;
- residual PCA on the five primary descriptors: `RESID_PCA80_DIM=3`;
- result does not prove physical melt instability and does not rule out sensor/process noise or unobserved heterogeneity;
- next bottleneck is external validation via an independent-condition dynamic-coupling dataset or qualified same-specimen physical outcome, not further feature/model engineering on the same 21 tracks;
- same-BP4 confocal branch remains `HOLD_PUBLICATION_NOT_VERIFIED`.

Cost governance / 비용:
`DEC-028` clarifies that any potentially billable action requires explicit user approval before execution; post-hoc reporting is not authorization. D12 itself used a verified zero-incremental-cost path.
