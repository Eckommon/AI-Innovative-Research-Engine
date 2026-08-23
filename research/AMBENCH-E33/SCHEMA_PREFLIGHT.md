---
id: AMBENCH-E33-SCHEMA-PREFLIGHT
type: schema-design-preflight
created: 2026-08-23
source_of_truth: nist-current-nerdm
numerical_outcome_values_emitted: false
raw_artifacts_committed: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-E33 Schema/Design Preflight / Schema·Design 사전점검

## Boundary / 경계
- Current NIST metadata, README design text, XLSX structure and **string-valued cells only**. / 현재 NIST metadata, README 설계 문구, XLSX 구조 및 **문자열 cell만** 사용.
- Numeric XLSX cell values are never emitted or inspected by this workflow. / XLSX 숫자 cell 값은 이 workflow에서 출력·검토하지 않음.
- No condition effect, outcome statistic, ranking, model, or image archive access. / 조건 effect, outcome statistic, ranking, model, image archive 접근 없음.

## Current source identity / 현재 source identity
- dataset: `mds2-3662`
- version: `1.0.1`
- component_count: `5`
- components_with_checksum: `5`

## README integrity and bounded design strings / README 무결성·설계 문구
- size: `8473`
- sha256_nerdm: `e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918`
- sha256_local: `e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918`
- checksum_match: `True`
- bounded_lines:
  - L4: and Area Measurements from Beam on Plate Experiments
  - L29: top surface bright field images and tabulated measurements of the melt pool width
  - L30: and top surface area of the last track of each fabricated sample.
  - L52: and area measurements from beam on plate experiments,
  - L84: The experiments were conducted using an EOS M290 machine located at the NIST Gaithersburg campus. Beam-on-plate experiments were performed on a 76 mm x 76 mm x 6 mm nickel alloy 625 plate using vendor-recommended parameters for the alloy. These parameters included a laser power of 285 W, a scan speed of 960 mm/s, and a hatch spacing of 110 μm. The skywriting option was enabled, which turned off the laser after reaching the end of a track, allowing the beam to decelerate and accelerate back to the programmed velocity before turning back on at the start of the next track.
  - L87: This data represents an 18-track rapid-turnaround artifact with an isosceles trapezoid geometry, captured at various stages of fabrication. The scanning strategy was recorded using a Printrite 3D system by Sigma Additive, which samples commands sent to the EOS M290 controller at 100 kHz. The artifact was produced as a set of partial geometries, each following the entire 18-track scan strategy up to a specific track number (1 to 18) and stops prematurely at that number to create solidified "snapshots" of the fabrication process. For the converging case, the first track started at the wide end of the trapezoid, while for the diverging case, it started at the narrow end. The scanning strategy data is provided in CSV files for both converging and diverging 18-track samples, containing x, y, laser power, and gating (laser on/off) commands following the xy2-100 protocol. To obtain the scan strategy for a specific partial geometry to input into a simulation model the CSV file can be truncated to the corresponding number of rows.
  - L90: Top-surface bright-field images of each fabricated sample were collected using a Zeiss AxioImager.Z2 microscope.  Two operators used ImageJ software to trace the inner chevron boundaries of the solidified melt pool of the last fabricated track of each sample, the maximum melt pool width and total top-surface area of the melt pool for each sample was then tabulated.
  - L102: Scan Strategy Data
  - L104: singleTrack.csv: Scan strategy for a single track scan
  - L106: scanStrategyDiverging.csv:  Scan strategy for the diverging case
  - L108: scanStrategyConverging.csv: Scan strategy for the converging case
  - L112: Set1_single_track.bmp: One single-track image
  - L114: Set1_Diverging_(2,3,4,5,6,7,8,18)tracks.tif: Nine diverging scan images
  - L116: Set1_Converging_18tracks.tif: One converging scan image
  - L118: Set1_single_track_withlines.bmp: One single-track image approximated melt pool width line in red color
  - L120: Set1_Diverging_(2,3,4,5,6,7,8,18)tracks_withlines.tif: Nine diverging scan images with approximated melt pool lines in red color
  - L122: Set1_Converging_18tracks_withlines.tif: One converging scan image approximated melt pool lines in red color
  - L124: Set2_Diverging_Samples.png: Stitched image containing 1 to 18 track samples with three repeats for diverging case
  - L126: Set2_Converging_Samples.png: Stitched image containing 1 to 18 track sample with three repeats for converging case
  - L128: Measurement Data
  - L130: Measurements.xlsx:  Contains tabulated measurements of the melt pool width and area for images in Set1 and Set2

## Measurements.xlsx integrity / Measurements.xlsx 무결성
- size: `376701`
- sha256_nerdm: `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`
- sha256_local: `9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf`
- checksum_match: `True`
- sheet_count: `1`

### Sheet `Sheet1`
- dimension: `B1:U49`
- merged_ranges: `['H25:H26', 'C25:C26', 'H24:T24', 'S46:T49', 'D4:E4', 'F4:G4', 'I25:N25', 'O25:T25', 'C2:G2', 'H4:H5', 'C4:C5', 'H2:T2', 'C3:G3', 'H3:T3', 'I4:N4', 'O4:T4']`
- string_cells:
  - `C2`: Set 1
  - `H2`: Set 2 
  - `C3`: Operator 1
  - `H3`: Operator 1 
  - `C4`: Track #
  - `D4`: Melt Pool Width Measurements (µm)
  - `F4`: Melt Pool Area Measurements (µm2)
  - `H4`: Track #
  - `I4`: Melt Pool Width Measurements (µm)
  - `O4`: Melt Pool Area Measurements (µm2)
  - `D5`: Diverging
  - `E5`: Converging
  - `F5`: Diverging
  - `G5`: Converging
  - `I5`: Diverging (D1)
  - `J5`: Divering (D2)
  - `K5`: Diverging (D3)
  - `L5`: Coverging (C1)
  - `M5`: Coverging (C2)
  - `N5`: Converging (C3)
  - `O5`: Diverging (D1)
  - `P5`: Divering (D2)
  - `Q5`: Diverging (D3)
  - `R5`: Coverging (C1)
  - `S5`: Coverging (C2)
  - `T5`: Converging (C3)
  - `H24`: Operator 2
  - `H25`: Track #
  - `I25`: Melt Pool Width Measurements (µm)
  - `O25`: Melt Pool Area Measurements (µm2)
  - `I26`: Diverging (D1)
  - `J26`: Divering (D2)
  - `K26`: Diverging (D3)
  - `L26`: Coverging (C1)
  - `M26`: Coverging (C2)
  - `N26`: Converging (C3)
  - `O26`: Diverging (D1)
  - `P26`: Divering (D2)
  - `Q26`: Diverging (D3)
  - `R26`: Coverging (C1)
  - `S26`: Coverging (C2)
  - `T26`: Converging (C3)
  - `S46`: Outliers
- string_cell_count: `43`

