---
id: AMBENCH-E29-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-E29 Amendment 01 — Symbolic hold-reason diagnostics only / symbolic HOLD 원인 진단만 허용

## Trigger / 발생
The first preregistered E29 execution ended `HOLD_E29_INTEGRITY_OR_COVERAGE` and emitted only `RuntimeError`, which is insufficient to distinguish the preregistered integrity/coverage subgate that failed.

No plate endpoint, group effect, permutation p-value, rank effect, common-track effect, raw coordinate row, or raw surface-reference row was emitted.

## Allowed change / 허용 변경
The workflow may emit the **predefined symbolic RuntimeError message** (for example `README_NOT_UNIQUE`, `PIXEL_SCALE_NOT_UNIQUE`, `P1_COMPONENT_NOT_UNIQUE`, `PLATE_VALID_COVERAGE_LT_41`) in addition to the exception type.

This is diagnostics-only. The emitted message must be one of the workflow-authored symbolic error codes and must not include raw source values.

## Frozen design unchanged / 고정 설계 불변
No change to:
- groups or plates;
- P1 location;
- reconstruction formula or sign;
- physical-scale source;
- >=41/45 coverage requirement;
- plate aggregation;
- directional hypothesis;
- exact permutation statistic;
- rank-biserial threshold;
- common-track sensitivity;
- frozen final gates.

After identifying the symbolic subgate failure, only a serialization/parser/source-identity defect may be repaired without redesign. A scientific/data-coverage failure remains HOLD.

Incremental monetary cost: `0 USD`.
