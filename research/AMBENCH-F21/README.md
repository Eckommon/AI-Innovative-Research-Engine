---
id: AMBENCH-F21
type: semantic-feasibility-preregistration
state: PREREGISTERED
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
---

# AMBENCH-F21 — X16 XCT Semantic Qualification Gate
# AMBENCH-F21 — X16 XCT 의미론 검증 Gate

## Purpose / 목적

**KO:** F20에서 cryptographic identity와 16-part workbook mapping이 확인된 `OverhangX16_ImageHistograms.xlsx`에 대해, numerical outcome을 사용하지 않고 authoritative NIST documentation만으로 histogram workbook의 A/B column 의미, units, preprocessing/reconstruction context, and a minimal future XCT endpoint transform을 고정한다.

**EN:** Using only authoritative NIST documentation and without numerical outcome analysis, qualify the physical/semantic meaning of columns A/B in the F20-verified `OverhangX16_ImageHistograms.xlsx`, relevant units and reconstruction/preprocessing context, and a minimal eligible future XCT endpoint transform.

## Frozen sources / 고정 source

Primary:
- NIST X16 XCT dataset `mds2-2514`;
- `DataDescription_OverhangPartX16_XCT.pdf`;
- F20-verified workbook `OverhangX16_ImageHistograms.xlsx`, SHA-256 `7cc48fc8aa7a86af4e00c24bfcf91373ef15a8bc1e10d404e61ba8f4d29c422f`.

Supporting authoritative method source:
- NIST JRES 125:125031, DOI `10.6028/jres.125.031`, because current NIST AMMT page states X16 XCT uses the same measurement system as X4.

## Outcome-blindness / outcome blindness

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains frozen.

Allowed:
- PDF text and figures;
- workbook sheet names/dimensions/text headers only;
- measurement/reconstruction/threshold/cropping semantics;
- formulas or transformations defined before viewing numerical outcomes.

Forbidden:
- reading/printing numerical histogram cell values;
- comparing parts numerically;
- selecting endpoints because they vary across parts;
- process↔XCT association/modeling;
- feature selection or high-capacity ML.

## Frozen questions / 고정 질문

1. What exactly does workbook column A represent?
2. What exactly does workbook column B represent?
3. What are the units/scales of A and B?
4. How were histogram values derived from XCT volumes (reconstruction, bit depth, cropping, thresholding if relevant)?
5. Are histogram bins directly comparable across all 16 parts under a common acquisition/reconstruction scale?
6. What single or minimal low-degree-of-freedom XCT endpoint can be defined from the histogram without outcome-driven tuning?
7. What artifact/uncertainty caveats constrain interpretation?

## Frozen endpoint hierarchy / 고정 endpoint hierarchy

The future endpoint must be chosen by authoritative semantics, not observed variation:

1. If NIST explicitly defines a physically meaningful pore/void threshold or derived defect fraction in the X16 documentation/workbook schema, freeze that authoritative measure.
2. Else, if A is grayscale/digital level and B is count/frequency with a common scale, permit only a preregistered distribution-location/shape summary that requires **no data-dependent threshold**. Preferred order:
   - normalized histogram centroid / mean digital level;
   - normalized histogram interquartile width;
   - no thresholded pore fraction unless a threshold is authoritative.
3. If the documentation does not support common scaling or column semantics, `HOLD_F21_SEMANTICS`.

No endpoint may be numerically computed in F21.

## Frozen gates / 고정 판정

### `PASS_F21_XCT_SEMANTICS_READY`
All must hold:
- authoritative A/B semantics established;
- units/scales established sufficiently for cross-part comparability;
- reconstruction/cropping context established;
- one minimal endpoint/transform can be frozen without outcome tuning;
- artifact caveats documented.

### `PARTIAL_F21_MEASUREMENT_CONTEXT_READY`
Measurement/reconstruction context is authoritative but workbook A/B or endpoint semantics remain incomplete.

### `HOLD_F21_SEMANTICS`
Authoritative sources are insufficient or contradictory for A/B/common-scale/endpoint interpretation.

### `REJECT_F21_ENDPOINT_ROUTE`
Workbook semantics show that the proposed histogram route cannot support a comparable part-level endpoint.

## Cost / 비용

Zero-incremental-cost routes only. Any potentially billable action requires explicit user approval before execution.

## Consequence / 후속

Only `PASS_F21_XCT_SEMANTICS_READY` can authorize a separately preregistered E19 design. E19 must still verify authoritative XYPT bytes against NERDm SHA-256 `b5f6c58540799f57c64b59ab4c0770f1aad8ac32b6bfb3161babdf244e32ff31` before running the already-frozen F19 segmentation.
