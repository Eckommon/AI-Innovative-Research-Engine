---
id: US-WATERWAY-E01-RESULT
issue: 100
state: COMPLETED_HOLD
final_gate: HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT
claim: CLM-143
decision: DEC-139
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E01 Result / 결과

## Final gate / 최종 판정

**`HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`**

Stage A passed, but frozen Stage B stopped on a source-semantics violation before model fitting: `RuntimeError: invalid USGS discharge value USGS-07249455 2016-12-23: '-399'`.

The preregistered contract accepted only finite nonnegative Daily USGS `00060/00003` discharge observations. Therefore `-399` cannot be silently recoded, dropped, imputed or used to exclude the gage inside E01.

No primary relationship coefficient, causal effect, prediction, novelty or utility result was established. Sensitivities cannot rescue the primary HOLD.

Incremental monetary cost: **0 USD**.
