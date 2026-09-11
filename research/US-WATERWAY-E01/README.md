---
id: US-WATERWAY-E01
issue: 100
state: ACTIVE_STAGE_B_AUTHORIZED
mission_anchor: MEM-054
portfolio_decision: DEC-136
preregistration_decision: DEC-137
relationship_computed: false
delay_magnitudes_opened: false
hydrology_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E01 — Extreme-Flow Burden × Annual Lock Delay
# US-WATERWAY-E01 — 수문 극단일 부담 × 연간 Lock 지연

## Primary question / 주 질문

Across prospectively qualified **USGS monitoring-location × calendar-year** units, is a larger share of hydrologically extreme daily streamflow associated with higher mean annual lock delay for the deterministically matched lock set?

Observational relationship test only; not causal inference and not advance prediction.

## Stage A — outcome-blind source/panel qualification

Before reading any lock-delay magnitude or hydrology observation value:
- audit calendar years **2016–2025**;
- require USGS Daily streamflow parameter `00060` with daily-mean statistic `00003`;
- require stable deterministic USACE historical/current lock identity;
- inspect only source access, schema, IDs, date/year support, row/nonblank-presence flags and cardinality;
- treat one USGS monitoring location as one exposure cluster even if multiple locks map to it;
- persist the final gage↔lock-set map and exclusions;
- no new fuzzy/manual identity repair beyond aliases already evidenced in official USACE material.

Stage-A PASS requires all:
1. >= **12 unique USGS gages** with metadata covering 2016-01-01 through 2025-12-31 for Daily `00060` / statistic `00003`;
2. >= **20 distinct matched locks** across those gages with Annual Usage support for all 10 years;
3. >= **120 prospective gage-year cells** after structural support checks;
4. zero manual/fuzzy repairs beyond already documented official aliases;
5. incremental monetary cost = 0 USD.

Failure resolves `HOLD_US_WATERWAY_E01_PANEL_SUPPORT` and returns to Stage 0 without opening magnitudes.

## Frozen Stage B estimand — only after Stage A PASS

Primary exposure `E_gy`:
- use USGS daily mean discharge `Q` (`00060`, statistic `00003`);
- compute each qualified gage's q10 and q90 from all usable daily observations in fixed 2016–2025;
- `E_gy = (# usable days where Q < q10_g or Q > q90_g) / usable days in year`;
- no imputation or threshold tuning.

Primary outcome `Y_gy`:
- USACE Annual Usage `Average Delay (minutes)` for every prospectively mapped lock-year;
- aggregate as the **unweighted arithmetic mean across mapped qualified locks** for each gage-year;
- any nonblank numeric delay <0 is a source/semantics HOLD.

Primary model:
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`

Primary inference:
- unweighted OLS at gage-year unit;
- two-way CR1 clustering by USGS gage and calendar year;
- Student-t reference df = `min(G_gage-1, G_year-1)`;
- no alternate covariance estimator may rescue the primary gate.

Primary directional hypothesis: `beta > 0`.

Materiality floor: a **+10 percentage-point** increase in extreme-flow-day share must imply at least **+5 minutes** annual Average Delay, i.e. `0.10 * beta >= 5`.

Primary PASS requires all:
1. beta > 0;
2. two-sided 95% CI lower > 0;
3. `0.10 * beta >= 5 minutes`.

Terminal primary gates:
- `PASS_US_WATERWAY_E01_POSITIVE_MATERIAL_EXTREME_FLOW_DELAY_ASSOCIATION`
- `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E01`
- `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E01_RELATIONSHIP`
- `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`

## Prespecified non-gate sensitivities

Only after the primary gate is fixed:
1. high-flow-only share (`Q > q90_g`);
2. low-flow-only share (`Q < q10_g`);
3. leave-one-gage-out coefficient range.

Sensitivities cannot rescue the primary result.

## Prohibited

No predictor substitution, percentile tuning, lag/lead search, river cherry-picking, outcome substitution, lock ranking, causal claim, prediction claim, novelty claim or utility claim inside E01.

Incremental monetary cost remains **0 USD**.
