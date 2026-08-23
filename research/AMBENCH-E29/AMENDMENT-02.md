---
id: AMBENCH-E29-AMENDMENT-02
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-E29 Amendment 02 — Exact authoritative README selector only / authoritative README exact selector만 보정

## Trigger / 발생
The AMENDMENT-01 diagnostic rerun stopped with symbolic reason `README_NOT_UNIQUE` before any plate endpoint, group effect, permutation p-value, rank effect, or common-track effect was computed.

The E29 workflow used an overly broad selector ending with `4103_ReadMe.txt`. Current NERDm contains README-related copies/paths, while the already verified F28 authoritative documentation workflow selected the exact root filepath `4103_ReadMe.txt` and successfully established the reconstruction semantics.

## Allowed correction / 허용 보정
Replace only the README component selector:

- from: any filepath ending with `4103_ReadMe.txt`
- to: exact filepath `4103_ReadMe.txt`

This reuses the F28-verified authoritative source identity and does not introduce a new documentation source.

## Frozen scientific design unchanged / 과학 설계 불변
No change to:
- T72/T82/T92 vs T102/T112/T122 grouping;
- physical plate as independent replicate;
- P1 only;
- overlap-depth reconstruction formula or sign;
- physical-scale semantics;
- >=41/45 per-plate coverage rule;
- arithmetic-mean plate endpoint;
- inherited direction `0.75 ms > 5.0 ms`;
- exact 20-allocation one-sided permutation;
- plate-level rank-biserial threshold >=7/9;
- >=36/45 common-track sensitivity rule;
- frozen final gates;
- inherited E27 exposure disclosure.

No outcome value has been emitted by E29 before this correction. This amendment is source-identity disambiguation only.

Incremental monetary cost: `0 USD`.
