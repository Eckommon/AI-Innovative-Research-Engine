---
id: US-UTIL-N01-SUPERSEDED-RUN-35007936755
type: execution-invalid-preservation
created: 2026-09-16
issue: 137
run: 35007936755
classification: EXECUTION_PARSER_INVALID_FOR_GATE
scientific_contract_changed: false
reliability_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# Superseded execution Run 35007936755

Run `35007936755` completed technically but its staging gate is **invalid for scientific adjudication**.

Two implementation defects were identified before terminalizing Issue #137:

1. `run_us_util_n01.py` imported the unpatched base F02 worksheet/header selectors instead of the already prospectively adjudicated execution resolver in `tools/us_util_f02_longitudinal_preflight_historical_urls.py`. As a result, the AMI parser selected the tiny `territories` worksheet (only 1–6 parsed rows/year) instead of the worksheet with the largest Utility-ID cardinality, and the Reliability classifier failed to exclude `Minus LOS` / `Loss of Supply Removed` variants.
2. The runner added `invalid_meter_rows == 0` as a hard PASS condition although Issue #137 did not preregister that requirement. Invalid/unparseable rows may be excluded from eligible exact utility-state-year support, but they cannot introduce a new terminal gate after authorization.

This run therefore does **not** establish `HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT`.

The correction is execution-only:
- reuse the F02 largest-identity worksheet rule;
- reuse the F02 primary IEEE with-MED rule excluding LOS variants;
- preserve all Issue #137 years, denominator, quantiles, matching, calipers, single-use rule and thresholds;
- judge terminal disposition only against the requirements actually frozen in Issue #137.

No Reliability magnitude was opened, no AMI→Reliability relationship was computed, no NOAA storm magnitude was used, and no scientific threshold was changed.

Incremental monetary cost remained **0 USD**.
