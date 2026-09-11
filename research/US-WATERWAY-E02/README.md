---
id: US-WATERWAY-E02
issue: 102
state: COMPLETED_NO_PREREGISTERED_POSITIVE_RELATIONSHIP
mission_anchor: MEM-054
portfolio_decision: DEC-140
preregistration_decision: DEC-141
parent: US-WATERWAY-E01
relationship_computed: true
delay_magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E02 — Signed-Flow Extreme Burden × Annual Lock Delay
# US-WATERWAY-E02 — 부호 보존 수문 극단일 부담 × 연간 Lock 지연

## Scientific boundary / 과학적 경계

E02 is a new prospective descendant, not a modification of E01. E01 remains `HOLD_US_WATERWAY_E01_SOURCE_PANEL_OR_INFERENCE_SUPPORT`.

## Frozen cohort
- exactly the 13 USGS gages / 23 locks in `research/US-WATERWAY-E01/STAGE_A_GAGE_LOCK_MAP.csv`;
- calendar years 2016–2025;
- shared gages contribute one gage-year outcome unit;
- no new manual/fuzzy identity repair.

## Frozen exposure `E_gy`
- USGS Daily discharge `00060`, statistic `00003`;
- accept every finite numeric published value **with sign preserved**, including negative and zero;
- never delete negatives, clamp to zero, take absolute values, or impute;
- null/blank/non-numeric = missing;
- require >=330 usable days in every included gage-year;
- compute q10_g and q90_g from all usable signed observations over fixed 2016–2025;
- `E_gy = share(Q < q10_g or Q > q90_g)` within year.

## Frozen outcome `Y_gy`
- USACE Annual Usage `Average Delay (minutes)` for every prospectively mapped lock-year;
- each nonblank value must be finite and >=0;
- gage-year outcome = unweighted arithmetic mean across mapped qualified locks;
- no imputation or alternate outcome.

## Frozen primary model
`Y_gy = gage FE + calendar-year FE + beta * E_gy + error`

- unweighted gage-year OLS;
- two-way CR1 by gage and calendar year;
- Student-t df = `min(G_gage-1, G_year-1)`;
- primary hypothesis: `beta > 0`;
- materiality: `0.10 * beta >= 5 minutes`.

Primary PASS requires beta > 0, two-sided 95% CI lower > 0, and materiality >=5 minutes per +10pp extreme-day share.

Terminal gates:
- `PASS_US_WATERWAY_E02_POSITIVE_MATERIAL_SIGNED_EXTREME_FLOW_DELAY_ASSOCIATION`
- `DETECTABLE_BUT_SUBMATERIAL_US_WATERWAY_E02`
- `NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP`
- `HOLD_US_WATERWAY_E02_SOURCE_PANEL_OR_INFERENCE_SUPPORT`

## Non-gate sensitivities — only after primary gate fixed
1. high-flow-only share;
2. low-flow-only share, preserving signed Q;
3. leave-one-gage-out beta range.

Sensitivities cannot rescue or reverse primary.

## Prohibited
No abs(Q), negative-value deletion, zero coercion, alternate predictor, percentile tuning, lag/lead search, river cherry-picking, outcome substitution, causal/prediction/novelty/utility claim.

Incremental monetary cost: **0 USD**.

## Final disposition / 최종 처분

Run `34577544880` resolves E02 as **`NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP`**. Realized panel: 120 gage-years / 12 gages / 10 years. beta=93.0279684807, 95% CI=[-84.9957401818, 271.051677143], p=0.267451090193, +10pp=9.30279684807 minutes. The positive point estimate does not pass the preregistered CI gate. No automatic descendant is authorized; return to Stage 0.
