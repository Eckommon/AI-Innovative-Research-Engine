---
id: CA-GRAIN-F01
issue: 106
state: COMPLETED_PASS
mission_anchor: MEM-054
portfolio_decision: DEC-146
authorization_decision: DEC-147
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-F01 — Weekly Grain-Pressure × Rail-Dwell Source/Join Feasibility
# CA-GRAIN-F01 — 주간 곡물압력 × 철도대기 source/join 타당성

Canonical contract is Issue #106. Frozen source families are Transport Canada weekly rail performance and Canadian Grain Commission Grain Statistics Weekly crop years `2023-24` and `2024-25`; structural interval `2023-08-01` through `2025-07-31`.

F01 is outcome-blind. Only access/provenance, hashes/byte counts, archive/schema/header labels, textual source identities, dates/week semantics, row/distinct counts, nonblank-presence booleans and prospective weekly join cardinality may be persisted. Grain-volume and dwell-time magnitudes are prohibited.

Possible gates:
- `PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`
- `PARTIAL_CA_GRAIN_F01_SOURCE_READY_JOIN_SEMANTICS_PENDING`
- `HOLD_CA_GRAIN_F01_SOURCE_OR_IDENTITY_SUPPORT`

Incremental monetary cost: **0 USD**.

## Final disposition / 최종 종결

- gate: **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**
- corrected Run: `34688361775`
- initial technical Run `34673025029`: **invalidated by `PROBE_AUDIT.md`**
- claim: `CLM-149`
- decision: `DEC-148`
- relationship/effect testing: **not authorized**
- canonical restart: **Stage 0 portfolio control**

This PASS establishes only frozen weekly source/schema/join feasibility. It is not evidence that grain pressure affects rail dwell.
