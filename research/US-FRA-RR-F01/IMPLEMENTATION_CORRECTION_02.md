---
id: US-FRA-RR-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-10-08
issue: 196
attempt_01_commit: 107e433bbd1ab3b3aecf68e99a8de9afa5178dad
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_FRA_RR_F01_ATTEMPT_01
scientific_threshold_changed: false
historical_window_changed: false
identity_rule_changed: false
event_rule_changed: false
future_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-FRA-RR-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved.

## Demonstrated defect / 확인된 결함

The official FRA ASMX landing and WSDL both returned HTTP 200. All required operations were discovered:

- `GetRailroadData`
- `GetF54Schema`
- `GetF55Schema`
- `GetAccident54DataByRailroad`
- `GetAccident55DataByRailroad`

The WSDL source-native signatures for the two historical data operations are exactly one parameter, `year`. The three reference/schema operations are no-argument operations.

The runner's WSDL parser only added operations to its `params` dictionary when an XSD request element contained an explicit sequence. Therefore no-argument operations did not receive a `params` entry. Gate 3 incorrectly required every operation to have such an entry even though the SOAP caller already correctly treats a missing parameter sequence as an empty argument list.

This is a parser/representation defect, not a scientific gate failure.

## Attempt 02 correction

Only Gate 3 implementation logic may change:

- require all five operation names in the official WSDL binding;
- require `GetAccident54DataByRailroad` signature = `[year]`;
- require `GetAccident55DataByRailroad` signature = `[year]`;
- treat `GetRailroadData`, `GetF54Schema`, and `GetF55Schema` as valid no-argument operations whether the XSD parser materializes an explicit empty sequence or omits a `params` entry.

All downstream SOAP call logic, years 2020–2025, frozen 18 gates, thresholds, exact identity, anti-tautology boundary and 2026+ seal remain unchanged.

If Attempt 02 reaches row-level data and any frozen gate fails, that result is scientific and terminal unless another independently demonstrated implementation-only defect is isolated without changing any scientific criterion.

Incremental monetary cost remains **0 USD**.
