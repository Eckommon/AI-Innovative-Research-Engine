---
id: UK-GRID-E01
type: controlled-cross-dataset-experiment
state: PREREGISTERED_OUTCOME_BLIND
created: 2026-09-03
parent_candidate: C-UK-001
parent_feasibility:
  - UK-GRID-F01
  - UK-GRID-F02
issue: 70
decision: DEC-100
mission_anchor: MEM-054
incremental_monetary_cost_usd: 0
---

# UK-GRID-E01 — SCOTEX Day-Ahead Boundary Stress × Realized Thermal-Cost Test
# UK-GRID-E01 — SCOTEX Day-Ahead Boundary Stress × 실현 Thermal-Cost 검정

## 1. Research question / 연구 질문

**EN:** Does higher day-ahead operational stress on the SCOTEX boundary associate with higher realized same-day SCOTEX thermal-constraint cost?

**KO:** SCOTEX 경계의 day-ahead 운영 stress가 높을수록 같은 날 실현된 SCOTEX thermal-constraint cost가 높아지는가?

This is the **single numerical experiment** authorized for the current UK-grid branch under `DEC-098`, `DEC-099`, and `DEC-100`. No same-branch tuning experiment is authorized afterward.

## 2. Outcome-blind boundary selection / 결과 비사용 boundary 선정

`SCOTEX` was selected before any selected 2026 observation-level numerical values from the three experimental fields were retrieved:
- `Limit (MW)`;
- `Flow (MW)`;
- `Daily Cost (GBP)`.

Selection is based only on official NESO structural semantics and F02 eligibility:
- NESO identifies SCOTEX with the Anglo-Scottish B6 boundary (`SP Transmission → NGET`);
- current NESO Scottish-boundary material describes predominant north-to-south Scotland→England transfer and increasing transfer requirements driven by additional Scottish generation, particularly onshore/offshore wind;
- the same official material describes B6 base capability as limited by a thermal constraint on the Harker–Moffat 400 kV circuit;
- NESO boundary-flow-smoothing work explicitly names `SCOTEX (B6)` among constrained Scotland/northern-England boundaries where short-term flow volatility and associated constraint cost matter operationally.

No observed 2026 SCOTEX result magnitude was used for selection.

### Documentation exposure / 문서 예시 노출

Official schema pages contain generic field examples. These are treated as documentation examples, not as selected SCOTEX 2026 observations. They do not change the outcome-blind state of the selected experimental window.

## 3. Frozen official sources / 고정 공식 source

### A. Day-ahead state
NESO `Day Ahead Constraint Flows and Limits`
- resource ID: `38a18ec1-9e40-465d-93fb-301e80fd1352`;
- `Constraint Group`;
- `Date (GMT/BST)`;
- `Limit (MW)` — source-defined maximum amount of power that can flow through the constraint boundary;
- `Flow (MW)` — source-defined day-ahead forecast based on next-day wind forecast, generation dispatch and demand forecast;
- half-hourly settlement-period basis.

NESO states that from `2024-04-22`, the Day Ahead Constraint Flow method no longer incorporates expected constraint mitigation/optimisation actions. The entire frozen 2026 experiment lies after this method boundary.

### B. Realized outcome
NESO `Thermal Constraint Costs Data 26-27`
- resource ID: `c730b788-4328-43dc-9f84-27fd3adeda59`;
- `Settlement Date`;
- `Constraint Group`;
- `Daily Cost (GBP)` — source-described daily spend for the named constraint.

## 4. Frozen evaluation window / 고정 평가기간

**`2026-04-01` through `2026-07-31`, inclusive.**

Expected calendar dates: exactly **122**.

Rationale frozen before numerical access:
- four complete calendar months;
- wholly inside F02-qualified SCOTEX overlap;
- August is excluded prospectively;
- as of 2026-09-03, the endpoint is more than 30 days old, providing a conservative maturity buffer against freshest-source revisions.

The 30-day buffer is a project heuristic, not an asserted NESO official correction lag.

**The evaluation window may not be changed after numerical access.**

## 5. Independent unit and nesting / 독립단위·nested 구조

Independent unit:

**one `SCOTEX × Settlement Date` / SCOTEX 1일**.

The 48 half-hourly day-ahead rows within a date are nested inputs. They are not treated as 48 independent cost outcomes.

## 6. Frozen primary predictor / 고정 1차 predictor

For each qualified date `d`:

`S_d = max_t( Flow_{d,t} / Limit_{d,t} )`

where `t` spans the 48 unique SCOTEX half-hour timestamps on that source calendar date.

Rules:
- preserve the **signed** source Flow;
- do **not** use `abs(Flow)`;
- require every `Limit > 0`;
- no learned coefficients, threshold optimisation, normalization or post-hoc transformation.

Rationale:
- source defines Limit as maximum boundary flow;
- source-defined and planning-described dominant B6 transfer direction is north-to-south;
- signed `Flow/Limit` therefore retains direction rather than treating reverse flow as equivalent positive-direction boundary stress.

The predictor is an **operational boundary-stress ratio**, not an assertion that every published day-ahead limit equals one immutable circuit thermal rating.

## 7. Frozen primary outcome / 고정 1차 outcome

`C_d = explicit same-day SCOTEX Daily Cost (GBP)`.

Rules:
- exactly one explicit cost record per frozen date is required;
- missing cost is **never** converted to zero;
- no smoothing, inflation adjustment, log transform or winsorization for the primary Spearman test;
- all costs must be finite and non-negative; otherwise numerical-integrity HOLD.

## 8. Stage A — pre-numerical structural gate / 수치 접근 전 구조 gate

Before any selected observation-level Flow/Limit/Cost value is requested, query only source identity/date fields and verify:

### Day-ahead
- exact group = `SCOTEX`;
- exact frozen date set = all 122 dates from 2026-04-01 through 2026-07-31;
- exactly `48` rows per date;
- all day-ahead timestamps unique;
- total structural rows = `122 × 48 = 5,856`.

### Thermal cost
- exact group = `SCOTEX`;
- exact frozen date set = all 122 dates;
- exactly one record per settlement date;
- all settlement dates unique;
- total structural rows = `122`.

If any structural requirement fails:

**`HOLD_E01_SOURCE_CARDINALITY`**

and Stage B numerical queries must **not execute**.

No date deletion, imputation, nearest-date join or narrower post-hoc window is authorized.

## 9. Stage B — frozen numerical integrity / 고정 수치 무결성

Only after Stage A passes:

1. record extraction UTC timestamp immediately before numerical queries;
2. query only the frozen SCOTEX fields/window;
3. hash exact numerical query responses with SHA-256;
4. verify all `Flow`, `Limit`, and `Daily Cost` values are numeric and finite;
5. verify every `Limit > 0`;
6. verify every `Daily Cost >= 0`;
7. re-verify exact date/timestamp cardinality after numerical retrieval;
8. do not persist raw daily/half-hour values in the public research result; persist hashes and aggregate statistics only.

Any failure requiring imputation, reinterpretation, row deletion, source substitution or metric redefinition yields:

**`HOLD_E01_NUMERICAL_INTEGRITY`**.

## 10. Frozen primary statistic / 고정 1차 통계

### 10.1 Spearman association
Compute average-tie ranks and:

`rho_obs = Spearman(S_d, C_d)`

across the complete chronological 122-day sequence.

### 10.2 Temporal-alignment surrogate null
To reduce dependence on an iid-day assumption, preserve both observed series while destroying their exact date alignment through **all circular shifts** of the 122-day cost series.

For shift `k = 0..121`:

`rho_k = Spearman(S_d, circular_shift(C_d, k))`.

The one-sided circular-shift temporal-alignment p-value is:

`p_circ = count(rho_k >= rho_obs) / 122`.

Shift `0` is the observed alignment and is included. Minimum attainable p is `1/122 ≈ 0.00820`.

This is a preregistered temporal-alignment surrogate test, **not** a claim of a conventional iid randomization experiment or causal identification.

### 10.3 Practical materiality threshold
Prospective project heuristic:

**`rho_obs >= 0.30`**.

This is a practical-effect threshold selected before outcomes, not a universal grid-engineering standard.

## 11. Frozen gates / 고정 게이트

### `PASS_E01_SCOTEX_STRESS_COST_SIGNAL`
All structural/numerical integrity checks pass **and**:
- `rho_obs >= 0.30`;
- `p_circ <= 0.05`.

### `PARTIAL_E01_DIRECTIONAL_ONLY`
Integrity passes and `rho_obs > 0`, but one or both PASS thresholds are not met.

### `NO_E01_MATERIAL_DIRECTIONAL_RELATION`
Integrity passes and `rho_obs <= 0`.

### `HOLD_E01_SOURCE_CARDINALITY`
Stage A source/date/cardinality requirements fail; numerical values must remain unopened by E01.

### `HOLD_E01_NUMERICAL_INTEGRITY`
Stage A passes, but Stage B cannot support the frozen metric without prohibited alteration.

No outcome may be converted to PASS by changing boundary, dates, predictor, sign, threshold, transformation or statistic.

## 12. Frozen secondary descriptives / 고정 2차 기술통계

For interpretation only; cannot rescue the primary gate:
- number of days with `S_d > 1`;
- minimum/median/maximum `S_d`;
- minimum/median/maximum daily cost;
- highest-stress quartile vs lowest-stress quartile median-cost difference;
- Cliff's delta for high- vs low-stress quartile costs.

Quartile group size is `floor(122/4) = 30`; ties are resolved by chronological order after sorting by `(stress, date)` solely for deterministic group membership.

## 13. Claim boundary / 주장 경계

A PASS would support the bounded proposition:

> Within the frozen mature 2026 SCOTEX window, a source-defined day-ahead boundary-stress ratio carries material temporal information about same-day realized SCOTEX thermal-constraint cost.

It would **not** establish:
- causal effect of forecast stress on cost;
- causal effect of Scottish wind alone;
- that a single Harker–Moffat circuit caused each daily cost;
- an immutable physical thermal rating interpretation of every operational `Limit`;
- generalization to ESTEX, other constraint groups, other years or other electricity systems.

## 14. Stop / portfolio-return rule / 중단·포트폴리오 복귀 규칙

After exactly one E01 execution, regardless of PASS/PARTIAL/NO/HOLD:

**return to Stage 0 Mission-ROI portfolio review.**

No same-branch threshold tuning, alternative boundary test, date-window optimization or predictor fishing is authorized automatically.

## 15. Sources / 출처

Official NESO source surfaces used for preregistration:
- `https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits`
- `https://www.neso.energy/data-portal/day-ahead-constraint-flows-and-limits/day_ahead_constraint_flows_and_limits`
- `https://www.neso.energy/data-portal/thermal-constraint-costs/thermal_constraint_costs_data_26-27`
- `https://www.neso.energy/publications/electricity-ten-year-statement-etys/electricity-transmission-network-requirements/scottish-boundaries`

## 16. Cost / 비용

Incremental monetary cost remains **0 USD**. No paid API, paid runner, GPU runner or billable external service is authorized.
