---
id: AMBENCH-POST-E14-TRIAGE
type: research-triage
state: COMPLETED_SELECTED_F15
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# AMBENCH Post-E14 Triage / E14 이후 외부검증 후보 선별

## Decision / 결정

**SELECT:** NIST PDR `mds2-3761`, *A Fully Registered In-Situ and Ex-Situ Dataset for Metal Powder Bed Fusion Additive Manufacturing: Data Processing, Feature Extraction, Registration, and Uncertainties*, as the next external-validation feasibility candidate.

**KO:** E14의 frozen stationary-Al 실험은 authoritative result bytes를 현재 검증 가능한 0원 경로에서 회수하지 못해 `HOLD_SOURCE_INTEGRITY`로 보존한다. 동일 retrieval을 반복하거나 실험을 재설계하지 않고, 다음 외부검증 후보로 NIST `mds2-3761` fully registered X4 dataset을 선택한다.

**EN:** Preserve the frozen E14 stationary-Al experiment at `HOLD_SOURCE_INTEGRITY`; do not repeatedly retry or redesign it. Select NIST `mds2-3761` as the next external-validation feasibility candidate.

## Why `mds2-3761` / 선정 이유

Official NIST/Data.gov material establishes that the dataset:
- is public and NIST-authored;
- integrates four nominally identical LPBF overhang parts from one build;
- provides 250 layer CSV files per part;
- contains only registered numerical values in machine coordinates;
- has 40 columns per measured point;
- combines commanded and measured laser position/power/speed;
- includes in-situ coaxial melt-pool length/width/area at multiple thresholds;
- includes layerwise optical intensity features;
- includes ex-situ XCT voxel values;
- documents spatial/temporal registration and uncertainty.

This directly supports process–structure / in-situ–ex-situ relationship validation rather than merely increasing feature capacity on the BP4 21-track dataset.

Primary official sources:
- NIST PDR/Data.gov identifier: `ark:/88434/mds2-3761`;
- NIST AMS 100-69, DOI `10.6028/NIST.AMS.100-69`;
- original in-situ source `mds2-2233`;
- original ex-situ source `mds2-2291`.

## Comparison / 비교

### E14 retry
- scientific leverage: high;
- frozen design quality: high;
- current authoritative byte accessibility: blocked;
- decision: **PRESERVE HOLD**, no redesign.

### `mds2-3761` registered X4
- scientific leverage: high;
- same-coordinate in-situ + ex-situ pairing: strong;
- repeated nominal parts: four;
- public metadata and full data schema: strong;
- current exact version/checksum/component-byte reproducibility: not yet established in this session;
- decision: **SELECT F15, SOURCE/IDENTITY GATE FIRST**.

### generic/synthetic surrogate datasets
- may be easy to download but do not provide the same authoritative empirical multi-modal validation value;
- decision: **DEFER**.

## Cost boundary / 비용 경계

`COST-001` + `DEC-028` remain mandatory. Any potentially billable retrieval/compute requires explicit user approval before execution. F15 is metadata/source-feasibility only on verified zero-incremental-cost routes.

## Next / 다음

Activate `AMBENCH-F15` to determine whether `mds2-3761` is reproducibly source-identifiable and sufficiently deterministic at part/layer/row/feature level for a later separately preregistered external process–structure experiment.
