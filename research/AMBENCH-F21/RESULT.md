---
id: AMBENCH-F21-RESULT
type: semantic-feasibility-result
state: COMPLETED_REJECT_F21_ENDPOINT_ROUTE
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F21/README.md
  - research/AMBENCH-F21/SEMANTIC_SOURCE_RESULT.md
  - Issue #39
---

# AMBENCH-F21 Result — X16 XCT Semantic Qualification
# AMBENCH-F21 결과 — X16 XCT 의미론 검증

**Frozen final gate / 고정 최종 판정:** **`REJECT_F21_ENDPOINT_ROUTE`**

## 1. Executive result / 핵심 결과

**KO:** X16 XCT Data Description의 authoritative byte identity를 SHA-256으로 검증하고 render-first/text extraction을 수행하여 workbook 의미론을 직접 확립했다. `OverhangX16_ImageHistograms.xlsx`의 각 part sheet에서 첫 열은 **histogram bin edges**, 둘째 열은 **각 bin의 voxel counts**이다. histogram X축은 **16-bit digital level**, Y축은 **number of voxels**이며, 데이터는 16-bit grayscale XCT TIFF stack에서 ImageJ로 계산되었다.

그러나 NIST는 16개 histogram이 nominally bimodal(empty/solid)이지만 각 peak의 mean/variance가 달라 **empty/solid threshold를 part마다 별도로 선택해야 한다**고 명시한다. 또한 histogram은 spatial information을 제거한 전체 cropped image-volume distribution이며, 일부 crop geometry가 다르고(Part 1-1), beam hardening/residual contrast/EDM artifact가 존재한다. 따라서 이 workbook 단독으로 공통 threshold pore fraction 또는 직접적인 structural-defect quality endpoint를 정의하는 것은 authoritative semantics가 지지하지 않는다.

따라서 semantic source는 충분히 qualified되었지만, F21의 proposed small-workbook-only XCT endpoint route는 **`REJECT_F21_ENDPOINT_ROUTE`**이다.

**EN:** Authoritative X16 XCT Data Description bytes were cryptographically verified and processed through render-first/text extraction. The workbook semantics are explicit: the first column of each part sheet contains **histogram bin edges**, the second column contains **voxel counts within each bin**, the X-axis is **16-bit digital level**, and the Y-axis is **number of voxels**. The histograms were calculated in ImageJ from the 16-bit grayscale XCT TIFF stacks.

However, NIST explicitly states that although the histograms are nominally bimodal (empty/solid), the peak means and variances differ and the empty/solid threshold must be chosen uniquely for each part. The workbook is also a spatially collapsed distribution of cropped image volumes; at least Part 1-1 has a different crop, and NIST documents beam-hardening, residual-contrast, and EDM-related artifacts. The workbook alone therefore does not support a common-threshold pore fraction or an unambiguous structural-defect quality endpoint.

The semantic source is qualified, but the proposed small-workbook-only endpoint route is rejected.

## 2. Source integrity / source 무결성

F21 authoritative source:
- `mds2-2514` component `DataDescription_OverhangPartX16_XCT.pdf`;
- NERDm size `533260` bytes;
- NERDm SHA-256 `d078ae297f909cad0c959aae9dae7df1accd2e1b237ec452f23674da84f5bb3d`;
- local transient SHA-256 matched exactly;
- render-first PASS, 6 pages;
- text extraction PASS;
- raw PDF/renders not committed.

F20 workbook identity remains:
- `OverhangX16_ImageHistograms.xlsx`;
- SHA-256 `7cc48fc8aa7a86af4e00c24bfcf91373ef15a8bc1e10d404e61ba8f4d29c422f`;
- exactly 16 part sheets plus `Plots`.

## 3. Authoritative workbook semantics / workbook 권위 의미론

X16 Data Description Section 4.3 establishes:
- histogram data were processed in ImageJ from XCT TIFF image stacks;
- workbook: `OverhangX16_ImageHistograms.xlsx`;
- first sheet contains histogram plots;
- subsequent sheets correspond to individual parts;
- **column A / first column = histogram bin edges**;
- **column B / second column = counts within each bin**;
- histogram X-axis = **16-bit Digital Level**;
- histogram Y-axis = **Number of Voxels**;
- histograms are nominally bimodal, representing empty and solid voxels.

Therefore:
- `COLUMN_A_SEMANTIC = 16_BIT_DIGITAL_LEVEL_BIN_EDGE`;
- `COLUMN_B_SEMANTIC = VOXEL_COUNT_PER_BIN`.

## 4. Measurement and reconstruction context / 측정·재구성 문맥

The X16 document states that the XCT setup, acquisition parameters, reconstruction, registration, and resampling methods were nominally replicated from the X4 XCT dataset.

Authoritative context includes:
- Zeiss Metrotom 800;
- voxel size approximately `11.953 μm × 11.953 μm × 11.953 μm`;
- 16-bit grayscale XCT image stacks;
- part-aligned coordinate system;
- X4 supporting method: FDK reconstruction with Shepp-Logan filter, ISO50 plus advanced surface refinement for registration, 3-2-1 registration, cropped output stacks.

The X16 TIFF stacks are spatially cropped, and Part 1-1 is explicitly noted as having a larger XY crop to include an attached particle.

## 5. Threshold semantics / threshold 의미론

NIST explicitly states:
- all sixteen histograms are nominally bimodal;
- peak means and variances differ among parts;
- any threshold separating empty and solid voxels must be chosen **uniquely for each part**.

Consequences:
1. a single common digital-level threshold across all sixteen parts is not authoritative;
2. a threshold selected after observing each part would add a part-specific estimation step;
3. the histogram alone lacks spatial location and therefore cannot distinguish outside/background empty voxels from internal voids/pores;
4. whole-volume empty/solid fractions would additionally be sensitive to crop geometry.

Thus F21 does not authorize a histogram-only pore/void fraction.

## 6. Artifact and interpretation caveats / artifact·해석 주의

NIST identifies potential analysis errors from:
- beam hardening;
- residual contrast artifacts;
- other XCT measurement-specific artifacts inherited from the X4 method;
- EDM-derived surface features/cuts unrelated to the AM process;
- attached particle / crop differences for at least Part 1-1.

These factors can shift grayscale distributions or alter voxel composition without representing the desired AM process-structure signal.

## 7. Frozen endpoint hierarchy application / endpoint hierarchy 적용

### Authoritative thresholded defect fraction
**FAIL.** No common threshold is authoritative; NIST requires part-specific threshold choice. Histogram-only data also lack spatial localization needed to isolate internal defects from exterior empty voxels.

### Threshold-free normalized histogram centroid / IQR
Mathematically definable after normalizing counts, but **not qualified as a structural-quality endpoint**. A whole-volume histogram centroid/IQR can respond to:
- crop/background fraction;
- acquisition/reconstruction contrast differences;
- beam hardening/residual contrast artifacts;
- EDM-related features.

F21 will not silently reinterpret an imaging-distribution statistic as physical defect quality.

### Result
No low-degree-of-freedom histogram-only endpoint satisfying the intended process–structure interpretation can be frozen without exceeding authoritative semantics.

## 8. Frozen gate application / 고정 gate 적용

- `PASS_F21_XCT_SEMANTICS_READY`: **FAIL** — A/B semantics are known, but no suitable physical part-quality endpoint can be frozen from the workbook alone.
- `PARTIAL_F21_MEASUREMENT_CONTEXT_READY`: superseded by stronger evidence; semantics are not merely incomplete.
- `HOLD_F21_SEMANTICS`: not selected; semantics are sufficiently known.
- `REJECT_F21_ENDPOINT_ROUTE`: **PASS** — the proposed workbook-only histogram endpoint route cannot support the intended comparable structural-quality endpoint without extra spatial/segmentation information.

## 9. Outcome boundary / outcome 경계

`NEW_X16_NUMERICAL_OUTCOME_BLIND = YES` remains intact.

F21 did **not**:
- read/compare numerical workbook histogram values;
- compute part-level XCT endpoints;
- read numerical XYPT/DAQ process values;
- compute process signatures;
- run association tests or models.

## 10. Consequence / 후속

Do **not** start the previously envisioned E19 histogram-summary experiment.

The rejection is narrow:
- X16 XCT dataset: **not rejected**;
- F20 workbook integrity: **still PASS**;
- F19 segmentation method: **still frozen**;
- workbook-only structural endpoint: **rejected**.

Highest-leverage next work is to return to the NIST **fully registered X4 dataset `mds2-3761`** and re-attempt its source-integrity gate using the successful F20 pattern:
1. NIST NERDm machine-readable component identity/checksum discovery;
2. zero-cost public standard GitHub-hosted transient retrieval;
3. checksum verification and archive inventory;
4. no numerical modeling until source integrity passes.

If `mds2-3761` becomes byte-verifiable, it is preferable because its registered representation already contains in-situ process/melt-pool variables and ex-situ XCT voxel-derived information in common coordinates, avoiding the X16 histogram-only localization problem.

Any paid/potentially paid route still requires explicit prior user approval.
