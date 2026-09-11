---
id: EU-GRID-F01
issue: 104
state: ACTIVE_SOURCE_OPERABILITY_FEASIBILITY
mission_anchor: MEM-054
portfolio_decision: DEC-143
authorization_decision: DEC-144
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# EU-GRID-F01 — ENTSO-E × E-OBS Source-Operability and Country-Panel Feasibility
# EU-GRID-F01 — ENTSO-E × E-OBS 소스운용성·국가패널 타당성

Canonical contract is Issue #104. Frozen countries: `FR, BE, NL, ES, PT, PL, AT, CZ`. Structural target interval: 2022-01-01 through 2025-12-31.

F01 is outcome-blind. Only source access, hashes, schema/header/unit labels, area/bidding-zone identities, timestamp/timezone/granularity semantics, nonblank-presence booleans, E-OBS version/spatial-temporal metadata, and prospective join cardinalities may be persisted. Numeric grid/weather/load/flow magnitudes are prohibited.

Possible gates:
- `PASS_EU_GRID_F01_SOURCE_PANEL_FEASIBLE`
- `PARTIAL_EU_GRID_F01_SOURCE_READY_REGISTRATION_REQUIRED`
- `HOLD_EU_GRID_F01_SOURCE_OR_IDENTITY_SUPPORT`

Incremental monetary cost: **0 USD**.
