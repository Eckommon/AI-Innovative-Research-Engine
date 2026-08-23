---
id: AMBENCH-E30-SEMANTIC-CORRECTION
type: integrity-correction
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - AMBENCH-E30
  - AMBENCH-F31
  - DEC-063
  - DEC-065
---

# AMBENCH-E30 Semantic Correction / E30 의미 해석 보정

## Trigger / 발생 원인

**KO:** F31의 source/design-only 검증 중, 현재 NIST `mds2-4103`의 checksum-verified `SampleIParameters.csv`와 NIST AMB2025-06/07 공식 challenge 문서를 대조한 결과, E30의 `P2/P3`를 동일 pad geometry의 두 공간 단면으로 취급한 해석이 잘못되었음을 확인했다.

**EN:** During the F31 source/design-only qualification, cross-checking the checksum-verified current `mds2-4103` `SampleIParameters.csv` against the official NIST AMB2025-06/07 challenge documentation established that E30 incorrectly interpreted `P2/P3` as two spatial cross-sections of the same pad geometry.

## Authoritative design mapping / 권위 설계 매핑

For every AMB2025-06/07 plate represented in the current design table:
- `P1`: `Pad_Width = 5 mm`, location `0.460 mm`;
- `P2`: `Pad_Width = 5 mm`, location `2.546 mm` in current `SampleIParameters.csv`;
- `P3`: `Pad_Width = 1 mm`, location `0.556 mm`.

The official NIST challenge document Table 8 gives the same geometry assignment and reports the P2 position as `2.545 mm`; this 0.001 mm documentation/data-table rounding difference does not affect the geometry identity.

For the bare AMB2025-07 turnaround subset specifically:
- `T72/T82/T92`: `0.75 ms`, powder thickness `0`, with P1/P2 = 5 mm and P3 = 1 mm;
- `T102/T112/T122`: `5.00 ms`, powder thickness `0`, with P1/P2 = 5 mm and P3 = 1 mm.

Current `SampleIParameters.csv` identity:
- size: `2086` bytes;
- SHA-256: `ad3efdd8757d19f435bb234483ed6ebdaea3e3ee5149aee77113d0d7bdff9e8c`;
- local/current NERDm checksum match: `YES`.

## Effect on E30 / E30 영향

The numerical E30 outputs are preserved as historical computations under the preregistered formulas, but their scientific interpretation is corrected:

1. `Delta_P2` is a **same-geometry (5 mm) second-location spatial sensitivity** relative to E29/P1.
2. `Delta_P3` is a **different-geometry (1 mm × 5 mm) directional contrast**, not a second spatial repeat of the 5 mm pad.
3. The equal-weight `P2/P3` combined endpoint is a **mixed spatial-position + pad-geometry composite**. It cannot support the pure claim `PASS_E30_SPATIALLY_ROBUST_DIRECTIONAL_EFFECT` as currently named.
4. Physical plate remains the independent unit (`n=3` vs `n=3`); this correction does not create additional independent replicates.
5. No E30 numerical value is deleted or recomputed by this correction.

## Current corrected interpretation / 현재 보정 해석

The defensible current statement is:

> **E29's turnaround direction remained positive at the second 5 mm cross-section P2 and was also positive at the already-observed alternate 1 mm geometry P3 on the same six physical plates. The historical E30 mixed P2/P3 composite was positive, but it is not a pure spatial-robustness endpoint.**

Accordingly, the historical E30 frozen gate remains part of the audit trail, but **its pure spatial-robustness interpretation is superseded in the affected scope** by `DEC-065`.

## Exposure correction / 노출 보정

Because E30 numerically inspected and reported P3, F31 cannot claim that the alternate `1 mm × 5 mm` geometry is outcome-unseen.

Current disclosure:
`NEW_F31_ALTERNATE_GEOMETRY_OUTCOME_BLIND = NO__P3_ALTERNATE_GEOMETRY_NUMERICAL_OUTCOMES_ALREADY_OBSERVED_IN_E30__PLUS_INHERITED_E27_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`.

F31 itself remains source/design-only and did not open new measurement outcomes.

## Cost / 비용
Incremental monetary cost: `0 USD`.
