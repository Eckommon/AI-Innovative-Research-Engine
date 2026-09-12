---
id: US-WW-F01-RESULT
type: outcome-blind-source-join-feasibility
created: 2026-09-12
issue: 114
gate: PASS_US_WW_F01_CWNS_NPDES_JOIN_READY
relationship_computed: false
need_dollar_magnitudes_read: false
candidate_outcome_magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WW-F01 Result

**`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`**

The preregistered source/schema/identity/cardinality gate passes without opening infrastructure-need dollar magnitudes or candidate compliance outcomes.

## Frozen gate evidence

- EPA 2022 CWNS nationwide CSV ZIP is reproducibly downloadable through the official no-auth download UI at 0 USD.
- CWNS contains deterministic `CWNS_ID`, `FACILITY_ID`, `STATE_CODE`, infrastructure/facility-type identities, `FACILITY_PERMIT` linkage and explicit need-category identities.
- Restricting to `INFRASTRUCTURE_TYPE = Wastewater` and `PERMIT_SOURCE = NPDES` yields **14,578** CWNS wastewater facilities with official NPDES linkage across **56** state/territory codes and **14,067** distinct official NPDES permit IDs.
- The preregistered cardinality requirements (>=3,000 linked facilities; >=30 states) both pass.
- In the official ECHO/ICIS-NPDES national identity package, **14,049 / 14,067 = 99.8720%** of the CWNS official NPDES IDs exact-match `ICIS_PERMITS`; the >=80% requirement passes.
- `ICIS_FACILITIES` independently supports 99.8649% exact coverage.
- `NPDES_PS_VIOLATIONS`, `NPDES_CS_VIOLATIONS`, and `NPDES_SE_VIOLATIONS` expose deterministic `NPDES_ID`, violation type/code/description and post-2022 date identities.
- CWNS need-category semantics prospectively identify wet-weather/conveyance-relevant categories including `III-A Infiltration/Inflow (I/I) Correction`, `III-B Sewer Replacement/Rehabilitation`, and `V Combined Sewer Overflow (CSO) Correction` without reading `BASE_AMOUNT` or `OFFICIAL_AMOUNT`.
- No facility-name/address fuzzy matching was used. Raw source bytes were transient and were not persisted.

## Claim boundary

This PASS establishes **join/design feasibility only**. It is not evidence that 2022 infrastructure needs predict later NPDES violations, does not establish causality or novelty, and does not authorize any relationship/effect test.

## Exact next action

Return to Stage 0. Compare a separately preregistered US-WW descendant design against independent alternatives. If US-WW advances, first freeze exposure-category identities, future compliance identity, pre-existing-compliance leakage controls, temporal window, comparator, model and inferential gate **before opening any future compliance outcome counts/rates**.

Incremental monetary cost: **0 USD**.
