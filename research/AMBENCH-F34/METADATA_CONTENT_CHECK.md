---
id: AMBENCH-F34-METADATA-CONTENT-CHECK
type: bounded-metadata-content-check
created: 2026-08-23
candidate_outcomes_inspected: false
large_archives_downloaded: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F34 Bounded Metadata Content Check / 제한 Metadata 내용 점검

## Integrity / 무결성
- dataset: `mds1103vzr`
- version: `1.0.4`
- Metadata.zip SHA-256 NERDm: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`
- Metadata.zip SHA-256 local: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`
- checksum_match: `True`

## `Metadata/2018_AMMTLaserScanAngles.txt`
- byte_size: `3307`
- line_count: `35`
- design_token_counts: `{'part': 0, 'cube': 0, 'gcode': 0, 'strategy': 0, 'layer': 0, 'mpm': 0, 'camera': 0, 'trigger': 0, 'scan': 0, 'angle': 0, 'position': 0, 'laser': 3}`
- nonnumeric/headings-only lines:
  - L1: i_laser
  - L13: i_laser
  - L25: k_laser

## Qualification consequence / 적격성 결과
- This Metadata.zip file is laser-incidence-angle calibration metadata.
- `part`, `cube`, `gcode`, `strategy`, `layer`, `mpm`, `camera`, and `trigger` token presence is reported above rather than inferred.
- No part→scan-strategy assignment is claimed unless explicitly present in this checksum-frozen file.
- No candidate outcome or large archive was opened.

