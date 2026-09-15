---
id: PORTFOLIO-R27-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: 133
state: COMPLETED_SELECT
selected_candidate: US-MINE-001
selected_gate: US-MINE-F01
next_issue: PENDING_STAGE0_AUTHORIZATION
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R27 Result — Select US-MINE-F01

**`SELECT_US_MINE_F01_OPERATIONAL_STRESS_INJURY_FEASIBILITY`**

After terminal US-BRIDGE-E01, do not rescue, reverse, or reinterpret that branch. R27 reconstructs the preserved R26 alternatives and selects **US-MINE-001** for one outcome-blind structural feasibility gate only. No injury magnitude, severity distribution, exposure magnitude, injury rate, or exposure→injury relationship was opened during selection.

## Prospective scoring rule

R27 reuses the established R26 9-dimension Mission-ROI frame, 0–5 each, total /45. The only temporal reinterpretation is prospective and explicit: `Next-gate information gain` and `Low overlap / novelty risk` are scored against **information already consumed by executed branches**, not source readiness alone. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-MINE-001 operational stress → injury** | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **39** | **SELECT_STAGE0_ONLY** |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 1 | **37** | HOLD_SATURATED_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial-site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 3 | 3 | **36** | PRESERVE_JOIN_ASSET |

## Durable-state reconstruction

### US-UTIL post-F02
This is not a fresh feasibility branch. Durable state already contains:
- Issue #94 / `US-UTIL-F01` → `PASS_US_UTIL_F01_JOIN_READY`;
- Issue #96 / `US-UTIL-F02` → `PASS_US_UTIL_F02_PANEL_DESIGN_READY`;
- 842 county-qualified reliability utilities and 6,341 qualified utility×county mappings at F01;
- 883 repeated-support utilities, 4,857 qualified utility-years and 37,156 utility-year×county mappings across 2019–2024 at F02.

A later descendant may still be scientifically useful, but panel/source uncertainty is already largely consumed and the generic AMI/reliability relationship has material current literature overlap. It therefore does not lead current marginal information value.

### US-MINE-001
`DISCOVERY-R01` screened this candidate at 38/45 with prior conceptual-overlap penalty, but no `US-MINE-*` execution branch exists in durable research state. Its next gate can still resolve nontrivial source/unit/time/reporting semantics before any injury outcome is opened. That raises the current next-gate information value from the earlier 3/5 to 4/5 without changing the overlap score.

### US-PIPE-001
The candidate remains unexecuted, but the hydrologic-stress → pipeline-incident pathway retains a direct-overlap penalty. A new feasibility gate would therefore remove less mission uncertainty than US-MINE.

### C-EU-004
The preserved Wave-1 asset remains technically attractive: EEA industrial-site coordinates can join to ERA5/Copernicus physical hazard layers. Because the branch remains unexecuted, R27 raises next-gate information gain from 2/5 to 3/5. However the currently framed target remains less direct as an operational outcome, so it does not overtake US-MINE.

## Why US-MINE leads now

Current official MSHA public data expose a prospective structural chain entirely before injury magnitudes:

`mine ID + calendar quarter + subunit → employment/production reporting identity → accident/injury report mine/time identity`.

MSHA Open Government documentation states that accident/injury records and quarterly operator employment/production datasets begin on 1 January 2000. The quarterly dataset is grouped by calendar quarter, subunit and mine ID. The same official documentation states that Metal/Nonmetal operators are **not required to report production**. Therefore production-based exposure comparability cannot be assumed nationally and must be resolved outcome-blind in F01.

The immediate information question is not whether production pressure predicts injury. It is whether a deterministic, zero-cost and prospectively defensible mine-quarter exposure/outcome identity can be frozen without outcome-driven sector, contractor or denominator choices.

## Exact authorization boundary

A later `US-MINE-F01` may inspect only:
- official source accessibility and version/update semantics;
- field/schema identity;
- mine ID, calendar-quarter and subunit identity support;
- operator versus contractor identity semantics;
- employee-hours and production-field availability/nonblank support by reporting regime;
- accident/injury document identity and report-time fields;
- structural join cardinality and geography/time coverage;
- whether a sector scope can be justified from reporting semantics/support alone.

F01 must **not** compute or persist injury rates, exposure-stratified injury counts, severity distributions, production-per-hour magnitudes, model coefficients, correlations, or relationship statistics. It may not choose coal, Metal/Nonmetal, contractors, a subunit family, a time window or a denominator because of injury outcomes.

## Official source basis

- MSHA Open Government Initiative data portal: https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp
- MSHA Part 50 data home: https://arlweb.msha.gov/STATS/PART50/p50y2k/p50y2k.HTM

## Exact next action

Close PORTFOLIO-R27 as completed selection, then open exactly one separate `US-MINE-F01` outcome-blind feasibility authorization. F01 must fail closed if production/reporting semantics cannot support a prospectively comparable exposure identity. No effect/outcome test is authorized by R27.

Incremental monetary cost: **0 USD**.
