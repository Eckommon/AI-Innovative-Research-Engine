---
id: US-RCRA-F01
issue: 121
state: ACTIVE_SOURCE_JOIN_FEASIBILITY
selection_decision: DEC-166
authorization_decision: DEC-167
relationship_computed: false
disaster_linked_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-F01 — RCRA Facility × County Disaster × Compliance Identity Feasibility

Canonical contract is Issue #121.

The gate is source/schema/identity/cardinality only. It must establish the exact public route `RCRAInfo.ID_NUMBER → ECHO SOURCE_ID → RCR_FIPS_CODE → FEMA county/time identity` and modern RCRA evaluation/violation temporal support for the operating-TSDF universe. No fuzzy facility/county matching and no disaster-linked compliance outcome aggregation is allowed.

PASS/PARTIAL requires a separate Stage-0/N01 design gate before any temporal relationship can be tested. Cost: **0 USD**.
