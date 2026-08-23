---
id: AMBENCH-F28-DOC-SEMANTICS
type: documentation-semantics-check
created: 2026-08-23
source_of_truth: github-actions
numerical_outcome_values_emitted: false
---

# AMBENCH-F28 Authoritative Documentation Semantics / F28 권위 문서 semantics

- incremental monetary cost: 0 USD
- raw coordinate/outcome values emitted: NO

- README_integrity_pass: YES
- selected_encoding: cp1252
- relevant_line_count: 50

## Redacted method/documentation lines / 숫자 redacted 방법 문서 lines
- L66: The following dataset includes bright field optical micrographs of pad cross-sections and melt pool geometry measurements. Cross-sectional micrograph tagged image format files (TIFF) have a pixel scaling of <NUM> micrometers/pixel. The resultant micrographs come from multiple images that were stacked and stitched together using <NUM> % overlap for tiling and the extended depth of focus (EDF) wavelets method for stack processing. Measurements and image rotations, if needed, were made in ImageJ. T
- L74: Before_Images : Micrographs showing the top view of before cross-sectioning. The filename is the sample name. Scale bars provided on images.
- L90: SurfaceReference_and_Orientation_Layers.csv : List of image names and the, Y reference pixel, and step over direction. The Y reference pixel is the y-pixel number that defines the substrate surface defined by the image origin in the top left corner. The step over direction is the direction in which the tracks progress perpendicular to the scan direction. A step over direction left-to-right means the tracks number from <NUM> to <NUM> going left-to-right. A right-to-left step over direction means 
- L163: Tracks_Results : Contains all measurement data for individual tracks. There are <NUM> total tracks per cross-section. Each measurand has two CSV files that begin with the measurand in the filename. The first file is a table of each cross-section and the measurement for each track number. The second file with “avgs” in the file name provides the average values with standard deviations, uncertainty terms, and combined-expanded uncertainty for each condition. Lastly, there is a CSV file for each cr
- L168: depths.csv
- L169: depths_avg.csv
- L170: overlap_depths.csv
- L171: overlap_depths_avg.csv
- L172: overlap_widths.csv
- L173: overlap_widths_avg.csv
- L174: widths.csv
- L175: widths_avg.csv
- L176: <NUM>_AMB_T1<NUM>_P1s_pixel_points.csv : Contains pixel locations that were used for measurements and calculations. Column <NUM> is the track number. depth_x and depth_y are the (x, y) coordinates of the deepest part of each track. width_x is the x-coordinate of the trailing width. Subtracting depth_x - width_x = width measurement. width_x (n+<NUM>) – width_x (n) = overlap width where n is the track number. bead_height_y is the y-coordinate of tallest point of each melt pool. Subtracting y-coord
- L177: <NUM>_AMB_T1<NUM>_P2s_pixel_points.csv
- L178: <NUM>_AMB_T1<NUM>_P3s_pixel_points.csv
- L179: <NUM>_AMB_T4<NUM>_P1s_pixel_points.csv
- L180: <NUM>_AMB_T4<NUM>_P2s_pixel_points.csv
- L181: <NUM>_AMB_T4<NUM>_P3s_pixel_points.csv
- L182: <NUM>_AMB_T7<NUM>_P1s_pixel_points.csv
- L183: <NUM>_AMB_T7<NUM>_P2s_pixel_points.csv
- L184: <NUM>_AMB_T7<NUM>_P3s_pixel_points.csv
- L185: <NUM>_AMB_T1<NUM>_P1s_pixel_points.csv
- L186: <NUM>_AMB_T1<NUM>_P2s_pixel_points.csv
- L187: <NUM>_AMB_T1<NUM>_P3s_pixel_points.csv
- L188: <NUM>_AMB_T2<NUM>_P1s_pixel_points.csv
- L189: <NUM>_AMB_T2<NUM>_P2s_pixel_points.csv
- L190: <NUM>_AMB_T2<NUM>_P3s_pixel_points.csv
- L191: <NUM>_AMB_T3<NUM>_P1s_pixel_points.csv
- L192: <NUM>_AMB_T3<NUM>_P2s_pixel_points.csv
- L193: <NUM>_AMB_T3<NUM>_P3s_pixel_points.csv
- L194: <NUM>_AMB_T5<NUM>_P1s_pixel_points.csv
- L195: <NUM>_AMB_T5<NUM>_P2s_pixel_points.csv
- L196: <NUM>_AMB_T5<NUM>_P3s_pixel_points.csv
- L197: <NUM>_AMB_T6<NUM>_P1s_pixel_points.csv
- L198: <NUM>_AMB_T6<NUM>_P2s_pixel_points.csv
- L199: <NUM>_AMB_T6<NUM>_P3s_pixel_points.csv
- L200: <NUM>_AMB_T8<NUM>_P1s_pixel_points.csv
- L201: <NUM>_AMB_T8<NUM>_P2s_pixel_points.csv
- L202: <NUM>_AMB_T8<NUM>_P3s_pixel_points.csv
- L203: <NUM>_AMB_T9<NUM>_P1s_pixel_points.csv
- L204: <NUM>_AMB_T9<NUM>_P2s_pixel_points.csv
- L205: <NUM>_AMB_T9<NUM>_P3s_pixel_points.csv
- L206: <NUM>_AMB_T1<NUM>_P1s_pixel_points.csv
- L207: <NUM>_AMB_T1<NUM>_P2s_pixel_points.csv
- L208: <NUM>_AMB_T1<NUM>_P3s_pixel_points.csv
- L209: <NUM>_AMB_T1<NUM>_P1s_pixel_points.csv
- L210: <NUM>_AMB_T1<NUM>_P2s_pixel_points.csv
- L211: <NUM>_AMB_T1<NUM>_P3s_pixel_points.csv
- L213: SurfaceReference_and_Orientation_Layers.csv : List of image names and the, Y reference pixel, and step over direction. The Y reference pixel is the y-pixel number that defines the substrate surface defined by the image origin in the top left corner. The step over direction is the direction in which the tracks progress perpendicular to the scan direction. A step over direction left-to-right means the tracks number from <NUM> to <NUM> going left-to-right. A right-to-left step over direction means 
- L253: SurfaceReference_and_Orientation_Track4<NUM>.csv : List of image names and the, Y reference pixel, and step over direction. The Y reference pixel is the y-pixel number that defines the substrate surface defined by the image origin in the top left corner. The step over direction is the direction in which the tracks progress perpendicular to the scan direction. A step over direction left-to-right means the tracks number from <NUM> to <NUM> going left-to-right. A right-to-left step over direction m

- semantic_flags: {'mentions_pixel_coordinates': True, 'mentions_imagej': True, 'mentions_scale': True, 'mentions_overlap_depth': True, 'mentions_explicit_conversion_word': False, 'mentions_micrometer_unit': True}
