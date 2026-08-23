---
id: AMBENCH-F31-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-F31 Amendment 01 — Do not presuppose the alternate-geometry plate IDs / 대체 geometry plate ID를 선가정하지 않는다

## Trigger / 발생
Before F31 source/design execution and before any alternate-geometry measurement outcome was inspected, prior F26 records were re-read. They state that the AMB2025-07 bare subset contains **12 physical plates = 4 conditions × 3 repeats**. Existing NERDm inventory also shows plate families beyond the six T72/T82/T92/T102/T112/T122 plates used in E29/E30.

Therefore the original F31 wording that asked whether the alternate geometry maps to the **same six physical plates** is an unsupported narrowing assumption.

## Corrected source-only question / 보정된 source-only 질문
F31 must identify from authoritative design metadata/documentation the exact physical plate groups associated with:
- `5 mm × 5 mm` vs `1 mm × 5 mm` pad geometry;
- `0.75 ms` vs `5.0 ms` turnaround condition;
- three physical repeats per condition, if documented.

F31 must **not assume in advance** whether the alternate geometry uses the same plates or a distinct six-plate set.

## Gate override / gate 보정
For `PASS_F31_ALTERNATE_PAD_GEOMETRY_ROUTE_READY`, replace the original condition “same six target physical plates can be deterministically bound” with:

> **the authoritative alternate-geometry turnaround groups and their physical repeat plate identities can be deterministically bound to a distinct interpretable outcome representation.**

If the authoritative design shows a separate six-plate repeat set for the alternate geometry, that is a valid and scientifically stronger replication axis rather than a failure.

## Unchanged / 불변
F31 remains source/design only. No measurement outcome values, pixel-coordinate rows, outcome-summary rows, images/masks, effect calculations, statistical tests or outcome-driven source selection are allowed.

No frozen outcome or effect has been observed in F31 at the time of this amendment.

Incremental monetary cost: `0 USD`.
