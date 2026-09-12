---
id: CA-GRAIN-F01-RESULT
type: outcome-blind-source-join-feasibility
issue: 106
gate: HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 Result

**`HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT`**

- Transport Canada full-data download: HTTP 200; CSV schema inspected outcome-blind.
- Frozen identity: `All Western grain` × `Average Dwell Time at Origin`.
- Structurally supported target rows: **0**; distinct source dates: **0**; carriers: **0**.
- GSW frozen crop-year CSVs accessible: **2/2**.
- GSW explicit date-derived week keys: **81**; TC week keys: **0**; explicit-date common week keys: **0**.
- No grain-volume or dwell-time magnitude was persisted or analyzed; no relationship was computed.

If the result is `PARTIAL`, the unresolved point is calendar/week identity semantics, not an observed relationship. Any repair must be prospectively specified before an effect test.
