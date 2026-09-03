---
id: UK-GRID-E01-DESIGN-CONTRACT
type: frozen-experiment-contract
state: FROZEN_BEFORE_NUMERICAL_ACCESS
created: 2026-09-03
issue: 70
boundary: SCOTEX
start_date: 2026-04-01
end_date: 2026-07-31
expected_days: 122
expected_halfhours_per_day: 48
incremental_monetary_cost_usd: 0
---

# UK-GRID-E01 Frozen Design Contract / 고정 실험 계약

This file is the compact executable contract. If code and prose conflict, **stop as HOLD; do not silently reinterpret the design**.

## Frozen identity / 고정 identity

- boundary/group: exact source string `SCOTEX` only;
- day-ahead resource: `38a18ec1-9e40-465d-93fb-301e80fd1352`;
- thermal-cost resource: `c730b788-4328-43dc-9f84-27fd3adeda59`;
- window: `2026-04-01 <= date <= 2026-07-31`;
- independent unit: one SCOTEX settlement date;
- expected dates: every calendar date in the inclusive window, exactly `122`.

## Stage A — numerical fields prohibited / Stage A — 수치 field 금지

Allowed projections only:
- day-ahead: `Constraint Group`, `Date (GMT/BST)`;
- thermal cost: `Constraint Group`, `Settlement Date`.

PASS requirements:
- day-ahead date set exactly equals frozen 122-day calendar set;
- exactly 48 unique timestamps for each date;
- total day-ahead structural rows = `5856`;
- thermal-cost date set exactly equals frozen 122-day calendar set;
- exactly one thermal record per date;
- total thermal structural rows = `122`.

If any check fails: `HOLD_E01_SOURCE_CARDINALITY`; **do not make Stage B queries**.

## Stage B — numerical fields / Stage B — 수치 field

Allowed only after Stage A PASS:
- day-ahead: `Constraint Group`, `Date (GMT/BST)`, `Limit (MW)`, `Flow (MW)`;
- thermal: `Constraint Group`, `Settlement Date`, `Daily Cost (GBP)`.

Immediately before Stage B record `extraction_utc`.
Persist exact Stage B response SHA-256 hashes.

Numerical PASS requirements:
- all 5856 Flow values finite numeric;
- all 5856 Limit values finite numeric and `> 0`;
- all 122 Daily Cost values finite numeric and `>= 0`;
- Stage B identity/date/cardinality exactly matches Stage A;
- no imputation or row deletion.

Failure: `HOLD_E01_NUMERICAL_INTEGRITY`.

## Predictor / predictor

For each date:

`stress = max(Flow / Limit)` across exactly 48 half-hours.

- signed Flow;
- no absolute value;
- no clipping;
- no trained parameters;
- no alternative predictor can replace it after access.

## Outcome / outcome

`same-day explicit SCOTEX Daily Cost (GBP)`.

No missing→zero conversion, log transform, smoothing, winsorization or inflation adjustment for primary test.

## Primary statistic / 1차 통계

1. Average-rank Spearman `rho_obs` across 122 chronological days.
2. For each circular cost shift `k=0..121`, compute `rho_k` against unchanged stress series.
3. One-sided `p_circ = count(rho_k >= rho_obs) / 122`.
4. Materiality heuristic: `rho_obs >= 0.30`.

### Final gates

- `PASS_E01_SCOTEX_STRESS_COST_SIGNAL` iff numerical integrity PASS and `rho_obs >= 0.30` and `p_circ <= 0.05`.
- `PARTIAL_E01_DIRECTIONAL_ONLY` iff numerical integrity PASS and `rho_obs > 0` but PASS condition is false.
- `NO_E01_MATERIAL_DIRECTIONAL_RELATION` iff numerical integrity PASS and `rho_obs <= 0`.
- Stage A/Stage B HOLD gates override all statistical gates.

## Secondary descriptives / 2차 기술통계

Non-rescuing only:
- stress min/median/max;
- cost min/median/max;
- count `stress > 1`;
- bottom/highest stress quartile median costs;
- median difference;
- Cliff's delta.

Quartile size = `30`. Deterministic membership sort = `(stress, date)`.

## Persistence / 저장

Public durable result may contain:
- gate;
- extraction UTC;
- response hashes;
- cardinalities/integrity diagnostics;
- aggregate primary/secondary statistics.

Do not persist the 122 daily cost/stress pairs or 5856 raw half-hour observations in the result file.

## Prohibited after access / 접근 후 금지

- changing SCOTEX to ESTEX or another boundary;
- extending/shortening date window;
- dropping days to improve result;
- switching signed to absolute Flow;
- choosing mean/percentile stress as primary;
- changing rho/materiality/p threshold;
- adding a regression/model to rescue the gate.

After one execution: **return to Stage 0**.
