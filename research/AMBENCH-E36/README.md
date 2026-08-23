---
id: AMBENCH-E36
type: preregistration
state: PREREGISTERED_SCHEMA_GATE_ACTIVE
created: 2026-08-23
source_of_truth: github
inherits:
  - AMBENCH-F35
  - DEC-074
incremental_monetary_cost_usd: 0
---

# AMBENCH-E36 — RHF External Confirmatory Reproduction, Schema-First
# AMBENCH-E36 — RHF 외부 Confirmatory Reproduction, Schema-First

## Purpose / 목적

**KO:** E33의 prior-scan-history ↔ melt-pool geometry 연관을 독립 RHF 실험에서 저자유도 방식으로 반증·확인한다. 먼저 checksum-frozen `RHF_Analysis_Results.zip`의 member/schema/결측 구조만 확인하고, numerical cells를 열기 전에 physical-part-level 분석계약을 별도 amendment로 동결한다.

**EN:** Falsify/confirm the E33 prior-scan-history ↔ melt-pool-geometry relationship in the independent RHF experiment using a low-degree-of-freedom design. First inspect only member/schema/missingness structure of checksum-frozen `RHF_Analysis_Results.zip`; freeze the physical-part-level numerical contract in a separate amendment before opening numerical cells.

## Permanent exposure disclosure / 영구 노출 고지

Before E36 preregistration, the associated publication had already exposed both direction and summary targets, including the reported optimized RHF condition and its reduction in melt-pool-area variability relative to baseline.

Permanent:

`NEW_E36_PUBLICATION_LEVEL_OUTCOME_BLIND = NO__RHF_DIRECTION_AND_SUMMARY_TARGETS_PREOBSERVED`

At preregistration:

`NEW_E36_RAW_ANALYSIS_CSV_NUMERICAL_OUTCOME_BLIND = YES`

Therefore E36 is a **confirmatory reproduction/falsification**, never pristine discovery.

## Frozen source / 고정 source

NIST `mds2-2507` v1.0.1.

`RHF_Analysis_Results.zip`:
- size: `1,637,430` bytes;
- SHA-256: `306a3d26e6e77d6fef44b1bf7b1dd2c817560a84f21f27fc4cec8cdb10cabe59`.

Physical units/treatment structure already qualified in F35:
- parts `P01–P55`;
- baseline constant-positive-power: `P01, P12, P23, P34, P45`;
- RHF variable-power: remaining 50 parts;
- physical part is the independent unit; rows/frames/pixels are nested measurements.

## Stage A — schema gate / 단계 A — schema gate

Allowed before any numerical outcome access:
- download exact `RHF_Analysis_Results.zip` and require current NERDm SHA-256 match;
- archive member names/sizes;
- expected `PXX` identity coverage;
- CSV header strings and column order;
- row counts;
- field non-empty counts / missingness counts;
- lexical type classification (`numeric-looking`, blank, nonnumeric) **without emitting/parsing numeric values into outcome statistics**;
- whether columns documented as area/length/width exist in every part.

Forbidden in Stage A:
- emitting any numerical data cell from the result CSV;
- min/max/mean/median/std/correlation/ranking of result columns;
- comparing baseline/RHF outcome distributions;
- choosing endpoint based on observed values;
- image/AVI/microscopy access.

### Schema gates / schema 판정
- `PASS_E36_SCHEMA_READY` — P01–P55 result members and required physical outcome columns are consistently identified with adequate non-empty coverage for a frozen part-level statistic.
- `HOLD_E36_SCHEMA_OR_IDENTITY_GAP` — PXX coverage, column semantics or data occupancy is insufficient/ambiguous; numerical access remains prohibited.

## Stage B — numerical contract / 단계 B — 수치 계약

Only after `PASS_E36_SCHEMA_READY`, create an outcome-still-unopened amendment that freezes:
- exact primary column;
- within-part aggregation/variability metric;
- finite/missing handling;
- baseline vs RHF group definition (must use F35 command-derived groups, not outcome-derived groups);
- exact part-level statistic and resampling/permutation rule;
- minimum valid-part requirement;
- PASS/NO/MIXED/HOLD gates;
- secondary publication-target reproduction, if any, clearly separated from the primary falsification.

No numerical result CSV cell may be opened until that amendment is committed.

## Pre-frozen scientific preference / 사전 고정 과학적 우선순위

Subject to exact schema confirmation, the preferred primary physical measurand is **melt-pool area**, because:
- it is directly documented by the NIST RHF data-description;
- the RHF mechanism and publication use temporal variability of melt-pool area as a process-uniformity observable;
- using area avoids endpoint search across area/length/width after numerical exposure.

Do not switch to width/length because numerical area results are inconvenient. If the area column is unusable at schema level, E36 must HOLD or amend before numerical exposure with a source-semantic reason only.

## Claim boundary / claim 경계

E36 can support or falsify external residual-history **mechanistic transfer** from E33, but cannot claim:
- same experimental construct as E33;
- new discovery of RHF efficacy;
- independence from the published RHF analysis;
- frame-level/sample-size inflation;
- causal generalization beyond these physical parts/conditions.

## Cost / 비용
Incremental monetary cost: `0 USD`. Any potentially billable route requires explicit prior approval.
