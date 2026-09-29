---
id: US-EIA-RET-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-30
issue: 184
attempt_01_commit: 3bdc8193ccb5c9ce7e40bea5a483047d57d4fdbe
attempt_01_run: 36631547648
attempt_01_recorded_disposition: HOLD_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_NOT_READY
scientific_threshold_changed: false
historical_months_changed: false
identity_rule_changed: false
retirement_rule_changed: false
future_firewall_changed: false
population_filter_added: false
incremental_monetary_cost_usd: 0
---

# US-EIA-RET-F01 — Attempt 02 implementation-only correction

Attempt 01 remains immutable. Its recorded 9/18 HOLD is **not accepted as a terminal scientific adjudication** because the runner failed before reading any authorized Operating/Retired row bodies.

## Demonstrated implementation defect / 확인된 구현 결함

Every one of the twelve official workbooks exposed the source-native sheet set:

- `Operating`
- `Planned`
- `Retired`
- `Canceled or Postponed`
- `Operating_PR`
- `Planned_PR`
- `Retired_PR`

The Attempt 01 matcher used substring logic (`OPERAT` / `RETIR`) and therefore treated the exact main sheets and their explicitly suffixed Puerto Rico shards as two competing candidates. It rejected the workbook as ambiguous even though the exact source-native `Operating` and `Retired` sheets were directly identifiable.

Consequently:
- authorized row bodies read = 0;
- identity rows evaluated = 0;
- August operable support = 0;
- retired support = 0;
- downstream gates 8 and 11–16 were zero-valued artifacts of the matcher failure, not empirical measurements.

This is a sheet-selection/parser defect.

## Attempt 02 correction / 보정

Attempt 02 changes only deterministic sheet resolution:

1. if an exact normalized sheet title `OPERATING` (or exact `OPERABLE`) exists, select it;
2. if an exact normalized title `RETIRED` exists, select it;
3. only if an exact title is absent may the runner use a **single** non-`_PR` source-equivalent candidate;
4. `Operating_PR` / `Retired_PR` are not treated as ambiguity against the exact main sheet;
5. no `Planned`, `Planned_PR`, `Canceled or Postponed` row body is opened.

No new geography filter is introduced: the frozen F01 asks for one identifiable source-native Operating sheet and one Retired sheet per workbook, and Attempt 02 simply resolves those exact sheets as published.

## Frozen scientific boundaries retained / 유지되는 과학 경계

Unchanged:
- exactly September 2025 through August 2026;
- exact Plant ID + Generator ID normalization;
- all 18 thresholds;
- retirement date semantics;
- future file cutoff after August 2026;
- Planned/Proposed row-body prohibition;
- EIA-923 row-body prohibition;
- no relationship/prediction/ranking/causal computation;
- cost = 0 USD.

If Attempt 02 successfully reads the exact allowed sheets, every frozen empirical failure is scientific and terminal unless a different, independently demonstrated implementation defect prevents valid evaluation.
