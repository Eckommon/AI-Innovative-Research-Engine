---
id: MEM-043-AMBENCH-F21
type: memory
state: ACTIVE
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
---

# MEM-043 — AMBENCH-F21 X16 XCT Semantic Qualification

## Result / 결과
`REJECT_F21_ENDPOINT_ROUTE`

## Durable semantic findings / 영속 의미론 결과
- verified X16 Data Description PDF: `533260` bytes, SHA-256 `d078ae297f909cad0c959aae9dae7df1accd2e1b237ec452f23674da84f5bb3d`;
- PDF render-first/text extraction PASS, raw PDF/renders not committed;
- workbook first column = histogram bin edges;
- workbook second column = voxel counts within each bin;
- histogram X-axis = 16-bit Digital Level;
- histogram Y-axis = Number of Voxels;
- histograms calculated in ImageJ from 16-bit grayscale XCT TIFF stacks;
- histograms nominally bimodal (empty/solid), but NIST requires threshold to be chosen uniquely for each part because peak means/variances differ;
- Part 1-1 has a larger XY crop; beam hardening, residual contrast, and EDM-derived artifacts are documented.

## Decision boundary / 결정 경계
The workbook-only route is rejected as a structural-quality endpoint. Do not compute a common-threshold pore fraction. Do not relabel histogram centroid/IQR as physical defect quality without additional spatial/segmentation evidence.

This does not reject:
- X16 XCT dataset itself;
- F20 workbook integrity PASS;
- frozen F19 segmentation method.

## Outcome blindness / outcome blindness
`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains intact. No numerical workbook histogram outcomes, XYPT/DAQ process values, process signatures, associations, or models were computed in F21.

## Next / 다음
Apply the successful F20 NERDm + zero-cost GitHub-hosted transient retrieval/checksum pattern to the NIST fully registered X4 dataset `mds2-3761`. Do not model until exact component hashes and archive inventory pass.

Any paid/potentially paid action requires explicit prior user approval.
