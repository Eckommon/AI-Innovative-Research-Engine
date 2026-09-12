---
id: CA-GRAIN-F01-RESULT
type: outcome-blind-source-join-feasibility
issue: 106
probe_revision: 2
supersedes_initial_run: 34673025029
gate: PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 Result

**`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**

The initial Run `34673025029` HOLD was invalidated by the technical audit in `PROBE_AUDIT.md`; the frozen scientific/source contract was not changed.

- Transport Canada full-data download: HTTP 200; annual English CSVs inspected for 2023, 2024 and 2025 outcome-blind.
- Frozen identity: `All Western grain` × `Average Dwell Time at Origin`, resolved against exact textual label columns.
- Structurally supported target rows: **1664**; distinct source dates: **104**; carriers: **2**.
- GSW frozen crop-year CSVs accessible: **2/2**.
- GSW explicit date-derived week keys: **81**; TC week keys: **104**; explicit-date common week keys: **81**.
- No grain-volume or dwell-time magnitude was analyzed or persisted; no relationship was computed.

PASS/PARTIAL remains source/join feasibility only and does not authorize an effect test.
