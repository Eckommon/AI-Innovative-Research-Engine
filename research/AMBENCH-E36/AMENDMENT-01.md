---
id: AMBENCH-E36-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE_PRE_NUMERICAL_EXECUTION
created: 2026-08-23
source_of_truth: github
raw_analysis_numerical_statistics_computed_before_this_amendment: false
publication_level_outcomes_preobserved: true
incremental_monetary_cost_usd: 0
---

# AMBENCH-E36 Amendment 01 — Physical-Part-Level RHF Variability Contract
# AMBENCH-E36 수정 01 — Physical-Part-Level RHF 변동성 계약

## 1. Trigger / 사유

`PASS_E36_SCHEMA_READY` established, before any result-value statistic, that checksum-frozen `RHF_Analysis_Results.zip` contains exactly P01–P55, each as a headerless 10-column analysis CSV with 1,498 rows and complete numeric-looking occupancy in documented columns 5–7 (melt-pool area/length/width).

The initial schema HOLD was a parser false negative caused by treating the first numerical row as a header; it was corrected using the official NIST positional schema before any numerical outcome statistic was computed.

## 2. Permanent exposure boundary / 영구 노출 경계

Publication-level RHF direction and summary targets were already known before E36. Therefore E36 is a confirmatory/reproduction analysis, not pristine outcome-blind discovery.

Known publication context includes that the original study used per-condition melt-pool-area standard deviation as a variability metric and reported an optimized RHF setting with reduced variability versus baseline. This amendment therefore avoids using a newly selected raw-data optimum as the sole inferential gate.

## 3. Independent analysis unit / 독립 분석 단위

Independent physical unit = one fabricated rectangular part `PXX`.

- P01–P55 are 55 physical parts.
- The 1,498 analysis rows within a part are repeated scan/image observations and MUST NOT be treated as independent experimental units.
- Each part is reduced to one preregistered variability statistic before any between-part inference.

## 4. Frozen treatment groups / 고정 처리군

From checksum-frozen process-input commands, before analysis-result access:

- baseline constant-positive-power parts = `P01, P12, P23, P34, P45` (n=5);
- RHF variable-positive-power parts = the remaining 50 parts.

For stability only, preserve five deterministic index blocks:
- B1: P01 baseline + P02–P11 RHF;
- B2: P12 baseline + P13–P22 RHF;
- B3: P23 baseline + P24–P33 RHF;
- B4: P34 baseline + P35–P44 RHF;
- B5: P45 baseline + P46–P55 RHF.

These are index blocks derived from the command-design structure; they are not asserted here as exact `(R,T)` labels.

## 5. Primary endpoint / 1차 endpoint

Documented analysis column 5: **melt-pool area (pixels)**.

For every PXX, use all 1,498 numeric area values exactly as stored. No value-based trimming, winsorization, outlier removal, zero filtering, row subset search, interpolation change, or post-hoc exclusion is allowed.

Part-level variability metric:
- sample standard deviation of melt-pool area, `SD_area(PXX)`, using `ddof=1`.

No frame/row-level p-value is permitted.

## 6. Primary non-selective confirmatory test / 1차 비선택 confirmatory test

Observed statistic:

`Delta_med = median(SD_area of 5 baseline parts) - median(SD_area of 50 RHF parts)`.

Positive values mean lower median variability in the RHF group.

Inference:
- one-sided deterministic Monte Carlo permutation of the fixed 5-vs-50 group labels across the 55 part-level SD values;
- 100,000 permutations;
- PRNG seed `20260823`;
- extremeness criterion `Delta_perm >= Delta_observed`;
- add-one p-value `(extreme + 1)/(100000 + 1)`.

Block stability:
For each of the five frozen index blocks, compute
`D_b = SD_area(block baseline) - median(SD_area(10 RHF parts in that block))`.
Count positive/negative/zero block signs. This is a robustness gate, not five independent hypothesis tests.

### `PASS_E36_EXTERNAL_RHF_VARIABILITY_REDUCTION`
All must hold:
1. all 55 part-level SDs are computable from all 1,498 rows;
2. `Delta_med > 0`;
3. one-sided permutation `p <= 0.05`;
4. at least `4 of 5` block differences `D_b` are positive.

### `MIXED_E36_RHF_VARIABILITY_REDUCTION`
`Delta_med > 0` and permutation `p <= 0.05`, but fewer than 4/5 block differences are positive.

### `NO_E36_NONSEL_RHF_VARIABILITY_REDUCTION`
The valid-part requirement holds but the primary direction/significance conditions are not both met.

### `HOLD_E36_NUMERICAL_INTEGRITY`
Any source checksum/part identity/row-shape requirement fails or not all 55 part-level area SDs are computable.

## 7. Publication-form descriptive reproduction / 논문형 기술 재현

Separately report, without using it to rescue the primary gate:
- mean and median baseline part-level area SD;
- minimum RHF part-level area SD and its PXX identity;
- descriptive percent reduction of the minimum RHF SD versus mean baseline SD;
- whether the raw-data optimum is broadly compatible with the already-known publication-level optimized reduction.

Because the optimum is selected from 50 RHF candidates and publication-level optimum information was already exposed, this section is descriptive/confirmatory only and has no independent PASS authority.

## 8. Secondary measurands / 2차 measurand

Length (column 6) and width (column 7) may be summarized at part level with the identical SD construction only after the primary area calculation. They are sensitivity/descriptive results only and cannot rescue a failed area gate. No endpoint switching is allowed.

## 9. Claim boundary / 주장 경계

A PASS would support that, in this independent NIST IN625 bare-plate RHF parameter-sweep experiment, variable RHF-based power-control conditions as a group show lower part-level melt-pool-area variability than constant-power baseline under the frozen non-selective comparison.

It would NOT establish:
- randomized causal treatment assignment;
- universal superiority of every RHF parameter setting;
- exact replication of E33's equivalent-track-length contrast;
- same machine/material generalization beyond the documented experiment;
- pristine outcome blindness.

## 10. Cost / 비용

Incremental monetary cost remains `0 USD`. Standard public-repository runner only; no larger/GPU runner, paid API, paid dataset, or artifact storage escalation.
