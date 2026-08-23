---
id: AMBENCH-E40-AMENDMENT-01
type: pre-performance-source-semantic-correction
created: 2026-08-24
applies_to: AMBENCH-F39-DESIGN-CONTRACT / AMBENCH-E40
custom_controller_performance_observed_before_amendment: false
endpoint_column_changed: false
endpoint_formula_changed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E40 Amendment-01 — MP_Stats Semantic Correction
# AMBENCH-E40 수정-01 — MP_Stats 의미 보정

## Trigger / 사유

Before any custom C0–C4 controller performance was executed, the exact pinned upstream source/documentation was re-read during E40 Stage A.

The F39 contract used the phrase **“maximum melt-pool width trajectory.”** The pinned 3DThesis documentation/source instead defines `MP_Stats` as maximum melt-pool width/length/depth **at each modeled grid point**. Stage A also verified the deterministic output field `MP_width`.

## Correction / 보정

The frozen primary numerical construction remains unchanged:

`CV_width = sample_SD(positive MP_width values) / mean(positive MP_width values)`

But its correct interpretation is now:

**spatial CV across positive per-grid-point maximum-melt-pool-width outputs**, not a temporal trajectory CV.

Unchanged:
- exact `MP_width` column;
- positive-value rule;
- sample-SD / mean formula;
- primary comparator C2;
- 10% C4-vs-C2 materiality threshold;
- ±5% C4-vs-C2 mean-width constraint;
- matched energy/time/controller constraints;
- PASS/PARTIAL/NO/HOLD gates.

No alternate endpoint, row filter, controller parameter or threshold is introduced.

## Claim boundary / 주장 경계

Any E40 result must be described as a **spatial maximum-width-field stability benchmark** in pinned 3DThesis. It is not a measured temporal melt-pool trajectory and does not validate scanner dynamics or physical-machine time-series stability.

## Gate consequence / 판정 영향

`PASS_E40_MPSTATS_SCHEMA_READY` remains valid. Stage B is authorized under this corrected source-semantic interpretation.
