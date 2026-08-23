---
id: AMBENCH-E33-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-E33/README.md
  - research/AMBENCH-E33/DESIGN_MAP_PREFLIGHT.md
  - registry/DEC-068.md
  - Issue #51
---

# AMBENCH-E33 Amendment 01 — Publication-Level Outcome Exposure & Reverse-Mapping Semantic Correction
# AMBENCH-E33 수정 01 — 논문 수준 outcome 노출 및 역매칭 의미 보정

## 1. Event / 사건

**KO:** E33의 최초 preregistration 및 endpoint/statistic/gate 동결 후, 실패한 process-input endpoint-location gate를 source-only로 해석하기 위해 공식 NIST 연계 논문 `The trace of heat: on the predictive power of modeling transient diffusion`을 확인했다. 이 과정에서 논문의 converging/diverging 설계 설명뿐 아니라 publication-level melt-pool outcome 비교와 수치적/방향적 결과가 도구 출력에 노출됐다.

**EN:** After E33's initial preregistration and freezing of its endpoint/statistic/gates, the official NIST-associated paper `The trace of heat: on the predictive power of modeling transient diffusion` was consulted to interpret the failed process-input endpoint-location gate. Tool output exposed not only the converging/diverging design description but also publication-level melt-pool outcome comparisons and numerical/directional results.

## 2. Exposure consequence / 노출 결과

The prior disclosure:
`NEW_E33_NUMERICAL_MEASUREMENT_OUTCOME_BLIND = YES_WITH_DISCLOSED_PUBLICATION_DESIGN_CONTEXT`

is superseded by:

`NEW_E33_NUMERICAL_MEASUREMENT_OUTCOME_BLIND = NO__PUBLICATION_LEVEL_CONVERGING_DIVERGING_OUTCOMES_EXPOSED_AFTER_PREREGISTRATION__RAW_MEASUREMENTS_XLSX_VALUES_STILL_UNOPENED`.

Important boundary:
- E33 `Measurements.xlsx` numerical cells remain unopened at the time of this amendment;
- no project-side recomputation of converging/diverging effects has occurred;
- the primary width endpoint, area sensitivity endpoint, operator nesting rule, physical-repeat aggregation, two-sided Spearman statistic, permutation count/seed, validity threshold and PASS/MIXED/NO/HOLD gates were frozen **before** this publication-level outcome exposure;
- therefore any descendant execution is a preregistered confirmatory/reanalysis exercise, **not** a pristine outcome-blind discovery experiment.

## 3. Design-semantic correction / 설계 의미 보정

The original preregistration described expected `C(t) ↔ D(19−t)` as a **same physical track-location** mapping. Process-input endpoint coordinates falsified that statement:
- 18 converging and 18 diverging laser-on segments are recoverable;
- endpoint-coordinate nearest-neighbour matching is one-to-one as `C(t) ↔ D(t)`, not reverse;
- therefore `C(t) ↔ D(19−t)` is **not** same physical XY location.

The official paper instead describes comparison of **equivalent track lengths** between converging and diverging scan strategies, with scan order reversed relative to those equivalent-length tracks.

Accordingly, E33 may proceed only if checksum-frozen process-input geometry independently verifies, without measurement outcomes, that:

`C(t) ↔ D(19−t)` is a deterministic **equivalent programmed track-length** mapping.

This amendment changes only the scientific meaning and pre-outcome qualification metric of the reverse map:
- from `same physical location`;
- to `equivalent programmed vector/track length under opposite scan-history order`.

It does **not** change the already-frozen outcome endpoint, aggregation, `h_t = 2t−19`, statistic, permutation procedure, validity thresholds, or decision gates.

## 4. Revised pre-outcome map gate / 보정된 outcome 전 map gate

Before opening any measurement value, `Scan Strategy Data.zip` must show:
1. exactly 18 laser-on segments in each strategy;
2. reverse-index pairing `C(t) ↔ D(19−t)`;
3. each reverse pair has equivalent process-input laser-on path/vector length within a fixed engineering tolerance established from the input recording resolution and source design, not outcomes;
4. the reverse pairing is globally better as a length-equivalence map than the same-index alternative.

If these conditions fail, retain `HOLD_E33_GEOMETRY_MAP_UNRESOLVED` and do not open numerical outcomes.

If they pass, record `PASS_E33_EQUIVALENT_LENGTH_REVERSE_MAP` and execute the **unchanged** preregistered numerical plan.

## 5. Interpretation boundary / 해석 경계

Even after a map PASS, E33 may support only a controlled **equivalent-track-length / different prior-scan-history** comparison within this IN625 beam-on-plate experiment. It must not claim:
- same physical XY location;
- same-construct replication of AMB2025-07 turnaround-time contrast;
- pristine outcome blindness;
- broad causal generalization across materials, machines or powder conditions.

## 6. Cost / 비용
Incremental monetary cost: `0 USD`. Any potentially billable action remains behind explicit user approval.
