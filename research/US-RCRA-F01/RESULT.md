---
id: US-RCRA-F01-RESULT
type: outcome-blind-source-join-time-feasibility
created: 2026-09-13
issue: 121
gate: PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY
relationship_computed: false
disaster_linked_compliance_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-F01 Result

**`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`**

US-RCRA-F01 passes the preregistered outcome-blind source/schema/identity/cardinality gate. This result does **not** show that disasters change RCRA compliance outcomes and does not authorize an effect test.

## Frozen feasibility evidence

- The current EPA RCRAInfo national export exposes **640** unique facilities in the documented operating-TSDF universe, exceeding the >=500 threshold.
- The exact route `RCRAInfo.ID_NUMBER == ECHO RCRA SOURCE_ID` yields one valid 5-digit county FIPS for **640/640 = 100.0%** of the operating-TSDF universe.
- Exact county-qualified operating TSDFs span **52** state/territory FIPS codes and **396** county FIPS codes; no fuzzy facility or county matching was used.
- FEMA OpenFEMA 2015-01-01 through 2024-12-31 exposes county-coded disaster/time identities. The exact TSDF geography overlaps FEMA disaster-coded counties in **52** state/territory FIPS codes, **395** counties, and **639** of the county-qualified operating TSDF facilities.
- RCRA evaluations and violations structurally cover every year 2015-2025; monthly violation/SNC history spans at least 2015-2025.
- No disaster-linked facility violation/evaluation count, rate, coefficient, ranking, or relationship statistic was computed. Raw source bytes were transient only.

## Technical audit boundary

Three implementation-only corrections were made outcome-blind before terminal disposition: the live evaluation header is `FOUND_VIOLATION`; `OPERATING_TSDF` uses six-position codes with `-` placeholders; and exact ECHO ArcGIS ID queries required smaller batches with bounded retry after a read timeout. None changed the scientific thresholds, selected facility universe semantics, exact identifiers, geography rules, or outcome boundary.

## Claim boundary

This PASS establishes **source/join/time feasibility only**. EPA/GAO already study natural-hazard vulnerability/exposure of RCRA facilities, so no novelty is claimed for static hazard mapping. No predictive or causal disaster-compliance claim is established.

## Exact next action

Return to Stage 0. If US-RCRA remains the highest-value branch, authorize a separate outcome-blind N01 design-identifiability gate before any disaster-linked compliance outcome is opened. N01 must prospectively freeze disaster incident/declaration semantics, baseline compliance, evaluation/inspection surveillance handling, multi-disaster rules, exposure window, comparator, outcome identity, model, overlap boundary, and non-causal claim language.

Incremental monetary cost: **0 USD**.
