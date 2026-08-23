---
id: AMBENCH-F21-SEMANTIC-SOURCE-RESULT
type: sanitized-semantic-source-result
created: 2026-08-23
source_of_truth: github-actions
raw_source_committed: false
numerical_xct_outcomes_emitted: false
---

# AMBENCH-F21 X16 XCT Semantic Source Result

## Integrity / 무결성
- NERDm fetch: PASS
- component metadata: PASS
- component: DataDescription_OverhangPartX16_XCT.pdf
- NERDm size: 533260 bytes
- expected SHA-256: d078ae297f909cad0c959aae9dae7df1accd2e1b237ec452f23674da84f5bb3d
- authoritative PDF download: PASS
- actual SHA-256: d078ae297f909cad0c959aae9dae7df1accd2e1b237ec452f23674da84f5bb3d
- SHA-256 match: YES
- PDF tooling: PASS
- render-first: PASS
- render-first page count: 6
- text extraction: PASS
- raw PDF/render artifact committed: NO

## Semantic contexts / 의미론 문맥
### Context 1
```text
performed on the Additive Manufacturing Metrology Testbed (AMMT) by Ho Yeung and Brandon Lane
on July 3, 2019. The files discussed in this document include image sequences for each part,
stereolithography files (.STL) of the surface data extracted from XCT, STL of the ‘as-designed’ part
geometry, VGStudioi project files, and a spreadsheet summarizing voxel-based histograms of the parts.

     The XCT measurement system and conditions used in this dataset are nominally identical to those in
```

### Context 2
```text
on July 3, 2019. The files discussed in this document include image sequences for each part,
stereolithography files (.STL) of the surface data extracted from XCT, STL of the ‘as-designed’ part
geometry, VGStudioi project files, and a spreadsheet summarizing voxel-based histograms of the parts.

     The XCT measurement system and conditions used in this dataset are nominally identical to those in
the “OverhangX4” XCT dataset [1]. Users should refer heavily to the data description document provided
```

### Context 3
```text
After fabrication, each part was electrical discharge machined (EDMed) from the build substrate. The
EDM processing attempted to cut as close to the substrate surface as possible along the bottom of the part
(the XY planar surface in the -Z direction). No additional support structure was included in the build
design, and some portion of the part was removed, effectively reducing the 5 mm Z-direction thickness
shown in Figure 2. Additionally, some parts have apparent residual surface features stemming from the
```

### Context 4
```text
After fabrication, each part was electrical discharge machined (EDMed) from the build substrate. The
EDM processing attempted to cut as close to the substrate surface as possible along the bottom of the part
(the XY planar surface in the -Z direction). No additional support structure was included in the build
design, and some portion of the part was removed, effectively reducing the 5 mm Z-direction thickness
shown in Figure 2. Additionally, some parts have apparent residual surface features stemming from the
EDM process (see Section 4.4)
```

### Context 5
```text
(the XY planar surface in the -Z direction). No additional support structure was included in the build
design, and some portion of the part was removed, effectively reducing the 5 mm Z-direction thickness
shown in Figure 2. Additionally, some parts have apparent residual surface features stemming from the
EDM process (see Section 4.4)

3.2 XCT acquisition
```

### Context 6
```text
The parts were scanned on a Zeiss Metrotom 800 at the Georgia Institute of Technology. The same XCT
setup and parameters described in [1] were also used to generate this dataset. Table 1 is repeated from that
publication for reference. All reconstruction, registration, and resampling parameters and methods were
replicated for this dataset using VGStudio Max software.

Table 1: XCT measurement and scan Parameters, replicated from [1].
```

### Context 7
```text
Source to Detector Distance             787.756 mm
                      Source to Object Distance               60.000 mm
                      Voxel Size                              11.953 μm x 11.953 μm x 11.953 μm
                      Focal Spot Size                         8 μm
                      Physical Filter                         0.5 mm Cu
```

### Context 8
```text
4.     Data Descriptions
4.1 Stereolithography (STL) Surface Files.
STL surface files were generated using the same methods described in [1]. These are provided in the
“Surface_STLs.zip” folder with filenames “OverhangPartX16_PartX_Y.stl”, where X_Y indicates the
corresponding part number in Figure 1.
```

### Context 9
```text
4.1 Stereolithography (STL) Surface Files.
STL surface files were generated using the same methods described in [1]. These are provided in the
“Surface_STLs.zip” folder with filenames “OverhangPartX16_PartX_Y.stl”, where X_Y indicates the
corresponding part number in Figure 1.

        4.2 Scaled and Cropped TIFF Image Stacks
```

### Context 10
```text
corresponding part number in Figure 1.

        4.2 Scaled and Cropped TIFF Image Stacks
        Tagged-image file format (TIF or TIFF) image stacks of each of the 16 parts are provided in this dataset,
        which compose16-bit grayscale values from the XCT measurement. The image stacks are nominally
        aligned with the coordinate system shown in Figure 2, where each image slice is in the XY plane,
```

### Context 11
```text
4.2 Scaled and Cropped TIFF Image Stacks
        Tagged-image file format (TIF or TIFF) image stacks of each of the 16 parts are provided in this dataset,
        which compose16-bit grayscale values from the XCT measurement. The image stacks are nominally
        aligned with the coordinate system shown in Figure 2, where each image slice is in the XY plane,
        consisting of 11.953 μm × 11.953 μm pixels. Subsequent slices in the stack proceed in the Z direction,
        nominally oriented with the build direction, and are 11.953 μm between each slice. Note that the total size
```

### Context 12
```text
Figure 3: Example TIF stack image of Part 1-1. This particular part was cropped to a larger size in XY to include the particle attached
                                                               on the right-hand side.
```

### Context 13
```text
TIFF image stacks are provided in the “TIFF_Stacks.zip” folder. Each image stack filename is
        “OverhangX16_PartX_Y_Cropped.tif”, where “X_Y” indicates the corresponding part number in Figure 1.


        4.3 Spreadsheet with Voxel-Value Histograms
```

### Context 14
```text
4.3 Spreadsheet with Voxel-Value Histograms
        Voxel-value histogram data was processed in ImageJ, and copied to an Excel spreadsheet file called
        “OverhangX16_ImageHistograms.xlsx”. These histograms are provided to help users select appropriate
        thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
```

### Context 15
```text
4.3 Spreadsheet with Voxel-Value Histograms
        Voxel-value histogram data was processed in ImageJ, and copied to an Excel spreadsheet file called
        “OverhangX16_ImageHistograms.xlsx”. These histograms are provided to help users select appropriate
        thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
        histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
```

### Context 16
```text
4.3 Spreadsheet with Voxel-Value Histograms
        Voxel-value histogram data was processed in ImageJ, and copied to an Excel spreadsheet file called
        “OverhangX16_ImageHistograms.xlsx”. These histograms are provided to help users select appropriate
        thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
        histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
        contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
```

### Context 17
```text
Voxel-value histogram data was processed in ImageJ, and copied to an Excel spreadsheet file called
        “OverhangX16_ImageHistograms.xlsx”. These histograms are provided to help users select appropriate
        thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
        histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
        contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
        within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
```

### Context 18
```text
“OverhangX16_ImageHistograms.xlsx”. These histograms are provided to help users select appropriate
        thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
        histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
        contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
        within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
        the means and variances of each peak within each bimodal histogram differ, such that any chosen threshold
```

### Context 19
```text
thresholding values to separate solid from empty voxels. The first sheet in the XLSX file includes the
        histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
        contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
        within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
        the means and variances of each peak within each bimodal histogram differ, such that any chosen threshold
        value to distinguish empty and solid voxels will need to be chosen uniquely for each part’s respective data.
```

### Context 20
```text
histogram plots in Figure 4. Each subsequent sheet is labelled based on the part’s histogram data which it
        contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
        within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
        the means and variances of each peak within each bimodal histogram differ, such that any chosen threshold
        value to distinguish empty and solid voxels will need to be chosen uniquely for each part’s respective data.
             10000000
```

### Context 21
```text
contains. The first column of each sheet indicates the histogram bin edges, and second column the counts
        within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
        the means and variances of each peak within each bimodal histogram differ, such that any chosen threshold
        value to distinguish empty and solid voxels will need to be chosen uniquely for each part’s respective data.
             10000000
                10000000
```

### Context 22
```text
within each bin. All histograms are nominally bimodal, indicating both empty and solid voxels. However,
        the means and variances of each peak within each bimodal histogram differ, such that any chosen threshold
        value to distinguish empty and solid voxels will need to be chosen uniquely for each part’s respective data.
             10000000
                10000000
                                                                                                                          6000000
```

### Context 23
```text
8000000                                                                                                  5000000
                                                                                                                             5000000
    Number of Voxels
    Number of Voxels
```

### Context 24
```text
5000000
    Number of Voxels
    Number of Voxels
```

### Context 25
```text
Number of Voxels
                                                                                                                 Number of Voxels
```

### Context 26
```text
35000   40000
                                                                                                                                                                                                          40000
                                               16-bit
                                                  16-bit
                                                      Digital
                                                         Digital
```

### Context 27
```text
40000
                                               16-bit
                                                  16-bit
                                                      Digital
                                                         Digital
                                                              Level
```

### Context 28
```text
Level
                                                                 Level
                                                                                                                                                              16-bit
                                                                                                                                                                 16-bit
                                                                                                                                                                     Digital
                                                                                                                                                                        Digital
```

### Context 29
```text
Level
                                                                                                                                                              16-bit
                                                                                                                                                                 16-bit
                                                                                                                                                                     Digital
                                                                                                                                                                        Digital
                                                                                                                                                                             Level
```

### Context 30
```text
14000000
            14000000
                                                                                                              Number of Voxels
                                                                                                              Number of Voxels
Number of Voxels
Number of Voxels
```

### Context 31
```text
14000000
                                                                                                              Number of Voxels
                                                                                                              Number of Voxels
Number of Voxels
Number of Voxels
```

### Context 32
```text
Number of Voxels
                                                                                                              Number of Voxels
Number of Voxels
Number of Voxels
```

### Context 33
```text
Number of Voxels
Number of Voxels
Number of Voxels
```

### Context 34
```text
40000 45000
                                                                                                                                                                                             45000
                                               16-bit
                                                  16-bit
                                                      Digital
                                                         Digital
```

### Context 35
```text
45000
                                               16-bit
                                                  16-bit
                                                      Digital
                                                         Digital
                                                              Level
```

### Context 36
```text
Digital
                                                              Level
                                                                 Level                                                                                        16-bit
                                                                                                                                                                 16-bit
                                                                                                                                                                     Digital
                                                                                                                                                                        Digital
```

### Context 37
```text
Level
                                                                 Level                                                                                        16-bit
                                                                                                                                                                 16-bit
                                                                                                                                                                     Digital
                                                                                                                                                                        Digital
                                                                                                                                                                             Level
```

### Context 38
```text
Figure 4: Voxel value histograms of the sixteen parts’ XCT data. Data is calculated from TIFF image stacks in ImageJ.

4.4 Notes on XCT Image Artifacts, Features, and Differences
Several measurement artifacts exist that may result in erroneous analyses if proper data pre-conditioning is
```

### Context 39
```text
Figure 4: Voxel value histograms of the sixteen parts’ XCT data. Data is calculated from TIFF image stacks in ImageJ.

4.4 Notes on XCT Image Artifacts, Features, and Differences
Several measurement artifacts exist that may result in erroneous analyses if proper data pre-conditioning is
not considered or attempted. These include the XCT measurement-specific artifacts described in [1], such
as beam hardening, residual contrast artifacts, etc., or surface features largely stemming from the EDM
```

### Context 40
```text
4.4 Notes on XCT Image Artifacts, Features, and Differences
Several measurement artifacts exist that may result in erroneous analyses if proper data pre-conditioning is
not considered or attempted. These include the XCT measurement-specific artifacts described in [1], such
as beam hardening, residual contrast artifacts, etc., or surface features largely stemming from the EDM
process rather than the AM process itself. As example, Figure 5-left shows an attached particle, and right
```

### Context 41
```text
4.4 Notes on XCT Image Artifacts, Features, and Differences
Several measurement artifacts exist that may result in erroneous analyses if proper data pre-conditioning is
not considered or attempted. These include the XCT measurement-specific artifacts described in [1], such
as beam hardening, residual contrast artifacts, etc., or surface features largely stemming from the EDM
process rather than the AM process itself. As example, Figure 5-left shows an attached particle, and right
shows an erroneous cut from EDM. EDM cut features are particularly noticeable on the bottom of each
```

### Context 42
```text
Several measurement artifacts exist that may result in erroneous analyses if proper data pre-conditioning is
not considered or attempted. These include the XCT measurement-specific artifacts described in [1], such
as beam hardening, residual contrast artifacts, etc., or surface features largely stemming from the EDM
process rather than the AM process itself. As example, Figure 5-left shows an attached particle, and right
shows an erroneous cut from EDM. EDM cut features are particularly noticeable on the bottom of each
part, as shown in Figure 6.
```

### Context 43
```text
z

  Figure 6: 3D view of Part 4-1 showing marks on bottom surface from EDM wire. Top highlights a gash from the EDM wire, and
                             bottom is a residual kerf from where the part detached from the base plate.

5.    Data Files
```

### Context 44
```text
➢   OverhangPart_9x5x5mm.STL – stereolithography file of the as-designed external dimensions of
         each part.
     ➢   OverhangX16_ImageHistograms.xlsx – Excel worksheet described in Section 4.3 containing
         voxel-value histogram plots and data
     ➢   Surface_STLs> - folder containing part surface STL files described in Section 4.1
             o OverhangPartX16_PartX_Y.stl – filename for sixteen part surface STL where X_Y is the
```

### Context 45
```text
each part.
     ➢   OverhangX16_ImageHistograms.xlsx – Excel worksheet described in Section 4.3 containing
         voxel-value histogram plots and data
     ➢   Surface_STLs> - folder containing part surface STL files described in Section 4.1
             o OverhangPartX16_PartX_Y.stl – filename for sixteen part surface STL where X_Y is the
                  part number described in Figure 1.
```

### Context 46
```text
➢   OverhangX16_ImageHistograms.xlsx – Excel worksheet described in Section 4.3 containing
         voxel-value histogram plots and data
     ➢   Surface_STLs> - folder containing part surface STL files described in Section 4.1
             o OverhangPartX16_PartX_Y.stl – filename for sixteen part surface STL where X_Y is the
                  part number described in Figure 1.
     ➢   TIFF_Stacks> - folder containing XCT voxel data as TIFF stack files described in Section 4.2
```

### Context 47
```text
voxel-value histogram plots and data
     ➢   Surface_STLs> - folder containing part surface STL files described in Section 4.1
             o OverhangPartX16_PartX_Y.stl – filename for sixteen part surface STL where X_Y is the
                  part number described in Figure 1.
     ➢   TIFF_Stacks> - folder containing XCT voxel data as TIFF stack files described in Section 4.2
             o OverhangX16_PartX_Y_Cropped.tif – filename for sixteen TIFF stack files where X_Y
```

### Context 48
```text
o OverhangPartX16_PartX_Y.stl – filename for sixteen part surface STL where X_Y is the
                  part number described in Figure 1.
     ➢   TIFF_Stacks> - folder containing XCT voxel data as TIFF stack files described in Section 4.2
             o OverhangX16_PartX_Y_Cropped.tif – filename for sixteen TIFF stack files where X_Y
                  is the part number described in Figure 1.
```

### Context 49
```text
part number described in Figure 1.
     ➢   TIFF_Stacks> - folder containing XCT voxel data as TIFF stack files described in Section 4.2
             o OverhangX16_PartX_Y_Cropped.tif – filename for sixteen TIFF stack files where X_Y
                  is the part number described in Figure 1.
```

### Context 50
```text
6.    Impact
This dataset is supplementary to the in-situ measurement data discussed in [2]. The combination of in-situ
and ex-situ AM fabrication data, provided in a well-documented and publicly disseminated format, enables
researchers and NIST collaborators to perform a wide range of analyses pertaining to the rapid qualification
of AM parts. This is enabled by identifying correlations between process signatures measured in-situ, to
```
## Boundary / 경계
- workbook numerical histogram cells inspected: NO
- numerical process values inspected: NO
- association/modeling performed: NO
- raw transient teardown: SUCCESS
