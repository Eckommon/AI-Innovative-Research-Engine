---
id: MEM-045-AMBENCH-F23
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-F23 Durable Memory / F23 영속 메모리

## Final gate / 최종 판정
`PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`

## What is now solved / 해결된 것
- `mds2-3761` raw registered CSVs are headerless.
- NIST AMS 100-69 positions 1..40 are frozen as the canonical semantic map in `research/AMBENCH-F23/README.md`.
- All four NIST ZIPs were hash/size revalidated against F22/NIST NERDm identities.
- All 1000 CSVs and 4,748,352 non-empty rows were structurally inspected.
- Every row has exactly 40 fields.
- Numeric/NaN parse failures = 0.
- Empty rows = 0.
- All 1000 first non-empty rows are numeric/NaN; no textual header exists.
- Raw ZIP/CSV bytes remain transient-only.

## Exposure state / 사전노출 상태
`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED` remains inherited from F22.

F23 added no numerical-value exposure and computed no associations/models.

## Exact next eligible work / 정확한 다음 eligible 작업
No numerical experiment is active yet.

Next work should be a separately preregistered, low-degree-of-freedom registered process/melt-pool ↔ XCT controlled experiment. Before any association result is computed, freeze:
1. scientific question and estimand;
2. predictor family and exact columns;
3. XCT outcome and exact column/transform;
4. row/layer/part aggregation policy;
5. missingness handling;
6. train/test or holdout structure, if any;
7. primary statistic/model and null/negative controls;
8. uncertainty interpretation;
9. disclosure of `VIOLATED_LIMITED`.

Do not use high-capacity ML or treat 4 parts, 250 layers, or millions of rows as independent replicates without a separately justified hierarchical design.

Any paid/potentially paid route requires explicit prior user approval.