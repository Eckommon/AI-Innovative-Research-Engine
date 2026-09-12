---
id: US-RCRA-F01
issue: 121
state: COMPLETED_PASS
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

## Terminal disposition / 최종 판정

**`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`** — See `RESULT.md`, `CLM-162`, and `DEC-168`. PASS is source/join/time feasibility only; no disaster-compliance relationship test is authorized.
