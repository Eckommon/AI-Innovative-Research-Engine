---
id: AMBENCH-E33
type: preregistration
state: PREREGISTERED_DESIGN_MAP_GATE_PENDING
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-F32
  - DEC-067
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 — Geometry-Matched Rapid-Turnaround History Falsification
# AMBENCH-E33 — Geometry-Matched Rapid-Turnaround History 반증 실험

## Purpose / 목적

**KO:** NIST `mds2-3662` Set 2의 converging/diverging 18-track rapid-turnaround artifacts를 이용해, 서로 다른 spatial track geometry를 단순 비교하지 않고 **동일 물리 track 위치를 역매칭**한 뒤, 그 위치에 도달하기 전 누적된 prior-track history 차이가 top-surface melt-pool geometry와 단조롭게 연관되는지 low-DOF 방식으로 검증한다.

**EN:** Use NIST `mds2-3662` Set 2 converging/diverging 18-track rapid-turnaround artifacts to test whether differences in accumulated prior-track history are monotonically associated with top-surface melt-pool geometry **after matching the same physical track locations in reverse scan order**, rather than naively comparing different spatial geometries at the same track number.

This is an independent rapid-turnaround scan-history falsification/mechanistic-transfer experiment. It is **not** a same-construct replication of AMB2025-07 `0.75 ms vs 5.0 ms` turnaround time.

## Pre-outcome source facts / outcome 전 source 사실

Current source:
- dataset `mds2-3662`, NERDm version `1.0.1`;
- `README.txt` SHA-256 `e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918`;
- `Measurements.xlsx` SHA-256 `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`;
- `Scan Strategy Data.zip` SHA-256 `f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee`.

Schema/design-only preflight establishes:
- Set 2 has track snapshots `1..18`;
- three physical repeats per direction: `D1,D2,D3` and `C1,C2,C3`;
- two operators measured the same physical samples;
- width columns: operator 1 `I:N`, operator 2 `I:N` in the lower block;
- area columns: operator 1 `O:T`, operator 2 `O:T` in the lower block;
- numeric measurement values have not been emitted or inspected by the preflight;
- each partial geometry is a fabricated snapshot whose last track is measured;
- converging starts at the wide end and diverging starts at the narrow end of the same 18-track isosceles-trapezoid design.

## Mandatory design-map gate / 필수 design-map gate

Before any measurement value is opened, `Scan Strategy Data.zip` process-input coordinates must establish a deterministic one-to-one same-track-location mapping.

Expected candidate map from documentation:
`C(t) ↔ D(19−t)`, for `t=1..18`.

### `PASS_E33_REVERSE_GEOMETRY_MAP`
- 18 converging and 18 diverging laser-on track segments are recoverable from process inputs;
- endpoint-geometry matching is one-to-one;
- every converging track `t` uniquely maps to diverging track `19−t` within a pre-outcome process-input geometric tolerance determined by recording resolution rather than outcome values.

### `HOLD_E33_GEOMETRY_MAP_UNRESOLVED`
If the deterministic reverse map is not supported, E33 must stop without opening `Measurements.xlsx` numerical values. No same-track-number fallback is authorized.

## Analysis unit / 분석 단위

Independent physical unit = fabricated Set-2 partial artifact at a given direction × track-count × repeat identity.

- `D1/D2/D3` and `C1/C2/C3` are physical repeats within a snapshot condition;
- Operator 1/2 are **measurement repeats nested within the same physical sample** and must never increase independent n;
- track-count snapshots are distinct partial artifacts, not repeated measurements of one physical artifact.

## Operator aggregation / operator 집계

For each physical sample and endpoint:
- if both operator measurements are numeric, use their arithmetic mean;
- if exactly one operator measurement is numeric, use that single available measurement and record the operator-missing flag;
- if neither is numeric, the physical sample is missing;
- operator-specific analyses are frozen sensitivity checks only.

## Source-outlier and missing policy / source outlier·결측 정책

Primary analysis uses **all numeric Set-2 measurements present in the checksum-frozen workbook** and applies no new value-based exclusion, trimming, winsorization, imputation, or thresholding.

Reason: source-publication outlier history is known prospectively, but a value-dependent exclusion decision after outcome access would violate the current blindness boundary. Robust condition summaries therefore use the median of physical repeats.

For each direction/location, at least `2 of 3` physical repeats must remain numeric after operator aggregation. Otherwise that location block is unavailable. At least `16 of 18` geometry-matched blocks are required for primary inference; otherwise final gate is `HOLD_E33_INSUFFICIENT_VALID_BLOCKS`.

Any source-authored outlier flag identifiable **solely from pre-existing workbook metadata/style and not from values** may be reported as a sensitivity analysis, but it cannot replace or rescue the frozen primary analysis.

## Geometry-matched history construction / geometry-matched history 구성

Conditional on `PASS_E33_REVERSE_GEOMETRY_MAP`:

For converging track index `t ∈ {1,...,18}`:
- same physical track location in diverging sequence = `19−t`;
- converging prior-track count = `t−1`;
- matched diverging prior-track count = `(19−t)−1 = 18−t`;
- frozen history contrast:

`h_t = (t−1) − (18−t) = 2t − 19`.

Thus `h_t ∈ {-17,-15,...,+15,+17}` and is fixed entirely by process order before outcomes.

## Primary endpoint / 1차 endpoint

**Top-surface maximum melt-pool width (µm)**.

Pre-outcome rationale:
- directly documented physical geometry measurand;
- simpler local geometry quantity than total segmented area;
- less topologically compound than area;
- supports direct same-track-location interpretation.

For each `t`:
1. operator-collapse C1/C2/C3 at converging `t`;
2. operator-collapse D1/D2/D3 at diverging `19−t`;
3. `Cmed_t = median(valid C repeats)`;
4. `Dmed_t = median(valid D repeats at matched location)`;
5. `d_t = Cmed_t − Dmed_t`.

No direction of `d_t` or history association is preregistered.

## Primary statistic / 1차 통계

Primary association:
**Spearman rank correlation `rho_width = Spearman(h_t, d_t)`**, two-sided.

Inference:
- deterministic Monte Carlo permutation of the `d_t` values across fixed `h_t` values;
- `100,000` permutations;
- PRNG seed `20260823`;
- two-sided extremeness criterion `|rho_perm| >= |rho_observed|`;
- add-one p-value: `(extreme + 1) / (100000 + 1)`.

Also report:
- `rho_width`;
- permutation p;
- number of valid matched locations;
- median and mean of `d_t` descriptively;
- sign counts of `d_t`;
- no location-specific p-value search.

## Primary gate / 1차 gate

### `PASS_E33_GEOMETRY_MATCHED_HISTORY_ASSOCIATION`
All must hold:
1. valid matched blocks `>=16`;
2. `|rho_width| >= 0.50`;
3. two-sided permutation `p <= 0.05`;
4. Operator-1-only and Operator-2-only sensitivity `rho` signs both match the primary `rho` sign when each has >=16 valid blocks.

### `MIXED_E33_OPERATOR_OR_EFFECT_INSTABILITY`
Primary items 1–3 pass, but operator-specific sign stability fails or cannot be established.

### `NO_E33_GEOMETRY_MATCHED_HISTORY_ASSOCIATION`
Valid-block requirement passes but items 2–3 are not both satisfied.

### `HOLD_E33_INSUFFICIENT_VALID_BLOCKS`
Fewer than 16 matched locations satisfy the predefined repeat-validity rule.

The secondary endpoint cannot rescue a failed primary gate.

## Secondary sensitivity endpoint / 2차 sensitivity endpoint

**Top-surface melt-pool area (µm²)** using the identical operator aggregation, reverse-location mapping, `h_t`, median-repeat aggregation, Spearman statistic, 100,000-permutation seed, and validity rules.

Interpretation:
- same sign + `p<=0.05`: cross-measurand strengthening;
- opposite statistically strong sign: `MEASURAND_CONFLICT`, regardless of primary PASS;
- null area result does not invalidate a width PASS but limits generalization.

No combined width+area optimization or endpoint switching is allowed.

## Forbidden / 금지

- same-track-number C(t) vs D(t) comparison as a substitute if reverse geometry map fails;
- counting operators as independent samples;
- counting rows/cells as independent physical replication beyond the documented artifacts;
- removing values because they look extreme;
- choosing track-count subsets after values are visible;
- changing width to area because area looks stronger;
- high-capacity ML, feature search, image modeling, or hyperparameter tuning;
- claiming replication of AMB2025-07 turnaround-time effect;
- paid API/cloud/SaaS or larger runner without explicit user approval.

## Exposure / 노출

`NEW_E33_NUMERICAL_MEASUREMENT_OUTCOME_BLIND = YES_WITH_DISCLOSED_PUBLICATION_DESIGN_CONTEXT`

Meaning:
- no `Measurements.xlsx` numerical value or candidate condition effect has been emitted in the E33/F32 preflight chain;
- source/publication design context, including existence of prior source-authored outliers and general study purpose, is known;
- the primary test is therefore frozen nondirectionally and uses a robust median physical-repeat summary.

## Capability / Portfolio / 비용

Reuse existing source-integrity, schema-only preflight, small-sample/permutation patterns. Classification remains `SHARED-INTERNAL-CANDIDATE`; no new Skill/MCP/Plugin or shared infrastructure promotion is justified.

Incremental monetary cost: `0 USD`.
