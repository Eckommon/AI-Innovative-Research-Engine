---
id: MEM-048-AMBENCH-F26
type: memory
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F26/RESULT.md
  - DEC-054
---

# MEM-048 — AMBENCH-F26 durable memory / F26 영속 메모리

## Result / 결과
`PASS_F26_INDEPENDENT_CONDITION_CANDIDATE_READY`.

Primary candidate:
**AMB2025-07 optical route, NIST `mds2-4103`.**

Primary independent groups:
- 0.75 ms turnaround: physical repeat plates T72, T82, T92;
- 5.0 ms turnaround: physical repeat plates T102, T112, T122.

P1/P2/P3 are sectioned pieces nested within each physical plate and must never be counted as independent repeats.

Current `mds2-4103` NERDm:
- version 1.0.0;
- 552 components;
- all six repeat plates have plate-specific `Cross_Sections/Tracks_Results` P1/P2/P3 CSV identities.

Thermography:
`AMB2025_07_THERMOGRAPHY_PDR = NOT_VERIFIED` under current official public evidence. It is not needed for the selected optical-only next route.

Secondary candidate:
`mds2-3662` rapid-turnaround IN625. NERDm v1.0.1, all five components checksum-bearing. Small README/workbook/scan-strategy components were locally hash verified; no outcome numbers were read. It remains a strong fallback but has a more complex track-count×direction design and source-author repeat outlier removals.

Not selected:
- `mds2-2525`: repeat-resolved public physical pairing not verified;
- `mds2-3842`: same-specimen physical outcome absent; cross-BP pairing prohibited.

## Protocol deviation / 프로토콜 deviation
While reviewing the current NIST AMB2025-06/07 measurement-description PDF, numerical values from a single-track calibration table were unintentionally exposed. No AMB2025-07 pad turnaround-condition result values were read or compared.

Inherited descendant disclosure:
`NEW_F26_B_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED_CALIBRATION_TABLE_PREOBSERVED`.

## Exact next eligible work / 정확한 다음 작업
Separately preregister an AMB2025-07 six-plate controlled experiment before opening `mds2-4103` result values:
1. choose one pad geometry;
2. choose one fixed cross-section position;
3. choose one primary melt-pool geometry measurand;
4. plate = independent replicate;
5. P sections = nested outcomes;
6. freeze small-sample exact/permutation statistic and effect-size gate;
7. no endpoint fishing/high-capacity ML;
8. carry the limited calibration-table pre-exposure disclosure.

No paid/potentially paid action is authorized without prior explicit user approval.
