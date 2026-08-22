---
id: AMBENCH-E14
type: experiment-preregistration
state: PREREGISTERED_NUMERICAL_PDR_OUTCOME_NOT_ACCESSED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
predecessor: AMBENCH-F13
---

# AMBENCH-E14 — A-AMB Aluminum Stationary-Spot Absorptance ↔ Melt-Pool-Width External Physical-Dynamics Test
# AMBENCH-E14 — A-AMB 알루미늄 stationary-spot 흡수율 ↔ melt-pool width 외부 물리동역학 검증

## 1. Purpose / 목적

**KO:** D12에서 확인된 BP4 coupling의 sampling-robust temporal variation이 독립적인 A-AMB 실험계에서 실제 melt-pool geometry dynamics와 연결될 수 있는지, 고용량 모델 없이 낮은 자유도의 time-resolved physical relation으로 시험한다. E14는 D12 repeat-level generalization이 아니라 F13이 허용한 **same-experiment external physical validation**이다.

**EN:** Test, without high-capacity modeling, whether laser-energy temporal dynamics in an independent A-AMB experiment are associated with measured melt-pool geometry dynamics. E14 is a **same-experiment external physical validation**, not a repeat-level generalization of D12.

## 2. Frozen Source / 고정 원천

Authoritative source: NIST PDR DOI `10.18434/mds2-2525`, checksum-rich data-bearing snapshot `v1.3.1`.

Primary components:
- `Al_Spot_TDA_Results.csv` — time-dependent absorption; expected SHA-256 `3f0b6812f98535f5ffbb0e2fed31f084ad9a7f9cc393c04a43ed57f0bb14bf69`;
- `Al_Spot_TDW_Results.csv` — time-dependent melt-pool width; expected SHA-256 `06b280222eab5f82eb9dcfb0689f20a5011c16e115548cd94ce120e5a97b4f5c`.

Version URL to archive as provenance: `https://data.nist.gov/od/id/ark:/88434/mds2-2525/pdr:v/1.3.1`.

Current public NIST challenge semantics frozen before numerical access:
- stationary aluminum laser duration `1.982 ms`;
- TDA time zero = start of laser irradiation;
- TDA nominal time interval = `40 ns`;
- TDW time values are at `20 µs` intervals and correspond to melt-pool width measured at the original sample-surface plane while the laser is on.

If component bytes do not match the exact expected checksums, E14 stops at `HOLD_SOURCE_INTEGRITY`.

## 3. Contamination / Outcome-Blindness Boundary / 오염·outcome-blindness 경계

Inherited from F13 Amendment-01:

`NEW_EXTERNAL_OUTCOME_BLIND = NO — PUBLICATION_LEVEL_AGGREGATES_PREOBSERVED`

Before E14 preregistration, publication-level aggregate **scanned-aluminum** geometry values had been exposed during source triage. These values:
- are not stationary-spot time-series values;
- are forbidden as E14 inputs, thresholds, tuning targets, or interpretation anchors.

At the moment this preregistration is frozen:
- no numerical `Al_Spot_TDA_Results.csv` values have been analyzed;
- no numerical `Al_Spot_TDW_Results.csv` values have been analyzed;
- no E14 correlation, descriptor, alignment, or gate statistic has been observed.

## 4. Schema Resolution Gate / schema 해석 gate

After preregistration, headers and numerical files may be accessed only to execute the frozen analysis. The execution must identify:
- time column and units;
- applied laser power if present;
- absolute absorbed power if present;
- relative absorption/absorptance if present;
- melt-pool width column and units.

Frozen absorbed-power resolution rule:
1. use the authoritative absolute absorbed-power column if present;
2. otherwise compute `P_abs(t) = P_applied(t) * A_rel(t)` with percent converted to fraction;
3. if neither route is deterministically available, `HOLD_SCHEMA_OR_ALIGNMENT`.

No target-aware column selection is allowed.

## 5. Time Alignment / 시간 정렬

- common event clock uses authoritative PDR time columns;
- time zero is the start of laser irradiation;
- primary window is the intersection of both files within laser-on time, capped at `[0, 0.001982] s`;
- TDW timestamps define interval boundaries;
- for each adjacent valid TDW pair `(t_i, t_{i+1})`, compute:
  - `A_i = mean(P_abs(t))` for TDA samples satisfying `t_i <= t < t_{i+1}`;
  - `R_i = mean(A_rel(t))` over the same interval when relative absorption is available;
  - `ΔW_i = W(t_{i+1}) - W(t_i)`;
- intervals without at least 10 finite TDA samples or finite width endpoints are invalid;
- no smoothing, manual cropping, interpolation, peak selection, or lag optimization.

At least 50 valid aligned intervals are required; otherwise `HOLD_SCHEMA_OR_ALIGNMENT`.

## 6. Primary Statistical Test / 1차 통계검정

Primary statistic:

`rho_primary = Spearman(A_i, ΔW_i)`

Rationale / 근거: absorbed power is the local energy-input quantity; width increment is the corresponding low-degree-of-freedom geometry-dynamics quantity.

### Circular-shift null / circular-shift 귀무분포

To preserve serial structure, do not randomly shuffle individual samples.

For `N` valid aligned intervals:
- observed = shift `k=0`;
- null shifts = every circular shift `k=1..N-1` of `A` relative to fixed `ΔW`;
- one-sided positive p-value: `p_pos = count(rho_k >= rho_0 for k=0..N-1) / N`;
- one-sided negative p-value: `p_neg = count(rho_k <= rho_0 for k=0..N-1) / N`.

No lag search is permitted.

## 7. Frozen Sensitivity / 고정 sensitivity

If relative absorption is deterministically available:

`rho_rel = Spearman(R_i, ΔW_i)`

using the same interval alignment and circular-shift procedure.

This sensitivity cannot rescue a failed primary gate by itself.

## 8. Small Descriptor-Transfer Set / 최소 descriptor 전이 세트

Descriptive only; cannot change the primary gate.

Transfer exactly three D11/D12 morphology concepts to the interval-level sequences:
- `early_contrast`: median of normalized-time `0.05 <= tau < 0.20` minus median of `0.20 <= tau <= 0.80`;
- `late_contrast`: median of `0.80 < tau <= 0.95` minus median of `0.20 <= tau <= 0.80`;
- `early_shape_slope`: OLS slope versus normalized time over `0.05 <= tau < 0.20`.

Compute these separately for:
- absorbed-power interval sequence `A_i`;
- width-increment sequence `ΔW_i`.

Do not tune windows, add FFT/wavelets, or create additional descriptors.

## 9. Frozen Gates / 고정 판정

Apply exactly one gate in this order.

### `HOLD_SOURCE_INTEGRITY`
Any expected component checksum mismatch or authoritative source retrieval failure.

### `HOLD_SCHEMA_OR_ALIGNMENT`
Required columns/units cannot be deterministically resolved, time axes violate the frozen semantics, or fewer than 50 valid aligned intervals remain.

### `POSITIVE_EXTERNAL_PHYSICAL_DYNAMICS`
All:
- `rho_primary >= +0.40`;
- `p_pos <= 0.05`;
- if relative-absorption sensitivity exists, `rho_rel > 0`.

### `DISCORDANT_EXTERNAL_DYNAMICS`
All:
- `rho_primary <= -0.40`;
- `p_neg <= 0.05`.

### `NO_MATERIAL_DYNAMIC_ASSOCIATION`
All:
- `abs(rho_primary) < 0.20`;
- `p_pos >= 0.20`;
- `p_neg >= 0.20`;
- if sensitivity exists, `abs(rho_rel) < 0.20`.

### `INCONCLUSIVE_EXTERNAL_DYNAMICS`
Fallback when integrity/alignment passes but none of the stronger outcome gates apply.

## 10. Interpretation Boundaries / 해석 경계

E14 may support only a statement about this stationary-Al same-experiment temporal relationship.

E14 does **not** authorize:
- repeat-level D12 generalization;
- numerical equivalence of A-AMB absorptance and BP4 coupling;
- causality beyond the experimental temporal association;
- cross-material predictive transfer;
- high-capacity ML;
- post-hoc lag/window/descriptor optimization.

## 11. Cost & Raw Data / 비용·raw data

- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval **before execution**; unknown billing = `HOLD_COST_APPROVAL`.
- E14 is authorized only through verified zero-incremental-cost public NIST access and already-provided local/transient compute.
- `RAW-001`: source CSV bytes are transient only; persist checksums, schema/integrity summaries, code logic, derived statistics, and final decision, not raw source files.

**Frozen state / 고정 상태:** `PREREGISTERED_NUMERICAL_PDR_OUTCOME_NOT_ACCESSED`.
