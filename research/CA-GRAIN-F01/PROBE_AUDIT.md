---
id: CA-GRAIN-F01-PROBE-AUDIT-001
type: technical-probe-audit
issue: 106
initial_run: 34673025029
initial_gate: HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT
disposition: INVALIDATE_INITIAL_GATE_PENDING_CORRECTED_PROBE
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 Probe Audit / 초기 probe 감사

The first source-probe Run `34673025029` completed successfully as software execution, but its emitted HOLD is **not accepted as the scientific F01 gate**.

Two outcome-blind implementation defects were identified before Issue #106 closure:

1. Header resolution used substring matching and therefore selected `Carrier_SortId`, `Commodity_SortId`, and `Measure_SortId` before the textual label columns `Carrier`, `Commodity`, and `Measure`. The frozen textual identities `All Western grain` and `Average Dwell Time at Origin` were consequently compared against sort IDs, mechanically producing zero target rows.
2. The Transport Canada ZIP contains annual English CSV members for 2023, 2024, and 2025, but the first probe selected only the first English candidate (2023). The frozen F01 interval is 2023-08-01 through 2025-07-31, so the probe did not inspect the full frozen structural interval.

These are probe-implementation errors, not source failures and not outcome feedback. The frozen source families, target identities, interval, PASS requirements, and no-magnitude boundary remain unchanged. A corrected runner may therefore repeat the same outcome-blind F01 contract using exact textual-label header resolution and all annual English members covering the frozen interval.

No grain-volume or dwell-time magnitude was analyzed or persisted, and no relationship was computed. Incremental monetary cost remains **0 USD**.
