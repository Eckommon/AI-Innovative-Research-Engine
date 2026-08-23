---
id: AMBENCH-E27
type: controlled-experiment-preregistration
state: PREREGISTERED
created: 2026-08-23
source_of_truth: github
parent: AMBENCH-F26
---

# AMBENCH-E27 — AMB2025-07 Six-Plate Turnaround-Time → Optical Geometry Controlled Experiment
# AMBENCH-E27 — AMB2025-07 6개 plate Turnaround-Time → Optical Geometry 통제 실험

## 1. Purpose / 목적

**KO:** F26에서 독립조건 후보로 승격한 NIST AMB2025-07 optical dataset (`mds2-4103`)을 이용하여, bare IN718 plate의 laser turnaround/skywriting time `0.75 ms`와 `5.0 ms`가 동일한 고정 pad/cross-section에서 solidified melt-pool overlap geometry에 강하고 반복 가능한 condition-level 차이를 만드는지 검사한다.

**EN:** Using the NIST AMB2025-07 optical dataset (`mds2-4103`) qualified in F26, test whether laser turnaround/skywriting time `0.75 ms` versus `5.0 ms` produces a strong and repeat-consistent condition-level difference in solidified melt-pool overlap geometry at one fixed pad geometry and cross-section on bare IN718 plates.

No causal claim is authorized merely by this observational label-permutation analysis; the statistic is a small-sample condition-separation test under an exchangeability reference, not proof of randomized treatment assignment.

## 2. Frozen source / 고정 source

- NIST PDR: `mds2-4103`
- current F26-qualified version: `1.0.0`
- title: `AM Bench 2025 Measurement Results Data: Optical Microscopy of arrays of adjacent laser tracks (pads) on alloy 718 plate`
- official experiment-design document: `AMB2025-06 and AMB2025-07 Benchmark Measurements and Challenge Problems`

Source integrity is mandatory. Numerical analysis may proceed only after exact NERDm component identity, size and SHA-256 are established and locally matched for every numerical component actually used.

## 3. Frozen independent groups / 고정 독립 그룹

Physical plate is the independent replicate.

- `0.75 ms`: `T72`, `T82`, `T92`
- `5.0 ms`: `T102`, `T112`, `T122`

`P1/P2/P3` are sectioned pieces nested within a plate and are **not** independent repeats.

## 4. Frozen geometry / 고정 geometry

Primary analysis uses **only P1**:

- pad: `5 mm × 5 mm`
- cross-section: `P1`
- nominal cross-section position: `x = 0.460 mm`
- NIST cross-section position uncertainty: `±0.075 mm` (`p=95%`)

Rationale frozen before outcome access: P1 is the specified 5 mm-pad cross-section closer to the pad edge/turnaround region than the central P2 section and is therefore the most direct fixed location for testing a turnaround-time intervention. No P2/P3 outcome is inspected to choose this location.

## 5. Frozen endpoints / 고정 endpoint

### Primary / 1차
**Average overlap depth** at P1, in micrometers.

NIST definition: vertical distance from the initial plate surface to the lowest intersection between two consecutive solidified melt pools. NIST describes 44 overlap-depth measurements per pad cross-section and the AMB2025-07 challenge requests an average overlap depth for each cross-section.

Expected authoritative summary component: `Cross_Sections/Tracks_Results/overlap_depths_avg.csv`. If NERDm does not establish this exact component or its schema cannot deterministically map the six P1 plates, numerical analysis is `HOLD` rather than endpoint switching.

### Sensitivity / 민감도
**Average depth** at the same P1 cross-section, in micrometers.

Expected authoritative summary component: `Cross_Sections/Tracks_Results/depths_avg.csv`. This endpoint is secondary only. Absence or schema failure does not permit replacement with another geometry endpoint.

No width, bead-height, overlap-width, P2, P3, final-track image, thermography, or post-hoc transform may replace the frozen primary.

## 6. Frozen directional hypothesis / 고정 방향 가설

`H1`: shorter turnaround (`0.75 ms`) produces greater P1 average overlap depth than longer turnaround (`5.0 ms`).

Physical rationale frozen before outcome access: a shorter inter-track turnaround interval permits less cooling before the adjacent track, so stronger thermal carryover/remelting is expected to increase overlap penetration. This is a hypothesis, not an observed result.

Sensitivity depth is expected in the same positive direction (`0.75 ms > 5.0 ms`) but cannot rescue a failed primary.

## 7. Frozen unit construction / 고정 분석단위

Use one published P1 average per physical plate:

`condition → 3 physical plates → one P1 average per plate`.

Primary vector size = exactly 6 values.

Forbidden:
- counting 44 overlap measurements as 44 independent replicates;
- treating P1/P2/P3 as independent repeats;
- pooling track-level values across plates to inflate n;
- imputation of a missing plate;
- outlier deletion after outcome inspection.

## 8. Missingness / integrity rule / 결측·무결성 규칙

Primary analysis requires all six plate-level P1 average overlap-depth values to be present, finite and deterministically identifiable.

If any primary plate is missing/ambiguous/non-finite, final gate = `HOLD_E27_INCOMPLETE_SIX_PLATE_COVERAGE` and no reduced-n hypothesis test is substituted.

Sensitivity is computed only if all six sensitivity values are present and finite; otherwise it is `NOT_COMPUTED` without affecting primary source validity.

## 9. Frozen statistic / 고정 통계

### Primary effect
`Δ = mean(overlap_depth_0.75ms) - mean(overlap_depth_5ms)`.

Report also:
- group means and medians;
- absolute Δ in μm;
- relative difference `Δ / mean(5ms)` when denominator is finite/non-zero;
- rank-biserial effect based on all 3×3 pairwise comparisons.

### Exact label-permutation reference test
Enumerate all `C(6,3)=20` assignments of the six fixed plate values into groups of three.

Test statistic = mean difference in the frozen positive direction.

`p_one_sided = count(T_perm >= T_observed) / 20`.

No Monte Carlo approximation.

Important small-n boundary: with 3 vs 3, the minimum attainable one-sided exact p is `0.05`; a conventional two-sided p<0.05 is structurally unattainable. E27 therefore does not manufacture a two-sided significance threshold.

### Effect-size/materiality rule
A strong condition separation requires both:
- positive primary Δ;
- rank-biserial effect `>= 0.777778` (at least 8 of 9 pairwise comparisons favor the frozen direction).

This is a statistical separation threshold, not an engineering-tolerance claim. No pad-specific absolute geometry uncertainty budget has been verified that would justify inventing a μm engineering materiality cutoff.

## 10. Frozen gates / 고정 판정

Apply in this order:

1. `HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`
   - exact source/hash/schema cannot be verified.

2. `HOLD_E27_INCOMPLETE_SIX_PLATE_COVERAGE`
   - any primary plate value missing/ambiguous/non-finite.

3. `PASS_E27_STRONG_TURNAROUND_GEOMETRY_SEPARATION`
   - primary Δ > 0;
   - exact one-sided permutation `p <= 0.05`;
   - rank-biserial `>= 0.777778`.

4. `REJECT_E27_DIRECTIONAL_HYPOTHESIS`
   - primary Δ <= 0 and rank-biserial <= 0.

5. otherwise `NO_STRONG_E27_TURNAROUND_SEPARATION`.

Sensitivity depth is descriptive/robustness evidence only. It cannot promote a non-PASS primary to PASS and cannot trigger endpoint switching.

## 11. Exposure disclosure / 사전노출 고지

Inherited from F26:

`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`.

The preobserved values were from a **single-track calibration table**, not AMB2025-07 pad turnaround-condition outcomes. E27 must not claim pristine outcome blindness, and those calibration numbers must not be used to select the endpoint, location, transform, direction threshold, or gate.

At preregistration time, no `mds2-4103` six-plate P1 pad outcome values have been inspected or compared.

## 12. Schema preflight / schema 사전검증

Before numerical outcome analysis:
1. query official NERDm for exact primary/sensitivity component metadata;
2. verify component size + SHA-256;
3. inspect only header/identifier schema needed to map T72/T82/T92/T102/T112/T122 + P1;
4. if schema is not deterministic, HOLD;
5. only then read the six frozen outcome values.

Schema preflight must not emit non-frozen outcome values.

## 13. Cost / 비용

Zero incremental monetary cost only:
- official NIST public source;
- public standard GitHub-hosted runner if needed;
- no artifacts/cache/larger runner;
- no paid API/SaaS/cloud/GPU.

Any potentially billable route remains `HOLD_COST_APPROVAL` under `COST-001` / `DEC-028`.

## 14. v2.1 overlay / v2.1 병행 적용

Per `DEC-055`, E27 remains Mission Work. The repeated source-integrity/preregistration/state-reconciliation workflow is only a `SHARED-INTERNAL-CANDIDATE`; no new Skill/MCP/Plugin is created as a prerequisite for this experiment.