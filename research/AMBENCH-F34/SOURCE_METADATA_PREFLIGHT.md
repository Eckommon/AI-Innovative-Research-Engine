---
id: AMBENCH-F34-SOURCE-METADATA-PREFLIGHT
type: source-design-preflight
created: 2026-08-23
candidate_outcomes_inspected: false
large_archives_downloaded: false
incremental_monetary_cost_usd: 0
---

# AMBENCH-F34 Source/Metadata Preflight / Source·Metadata 사전점검

## Boundary / 경계
- Current official NIST NERDm/PDR metadata + checksum-verified `Metadata.zip` only.
- `Build Command Data.zip`, `In-situ Meas Data.zip`, and `Movies.zip` are NOT downloaded/opened.
- No candidate melt-pool/quality numerical outcome is inspected or emitted.

## Current NERDm identity / 현재 NERDm identity
- endpoint: `https://data.nist.gov/od/id/mds1103vzr?format=nerdm`
- title: Process Monitoring Dataset from the Additive Manufacturing Metrology Testbed (AMMT): 3D Scan Strategies
- version: `1.0.4`
- edition/version id: `ark:/88434/mds1103vzr`
- component_count: `9`
- top-level components:
  - `Movies.zip` | size=`698954503` | sha256=`df63cbc6f07c0cad11cff2f01355ac583da0079d04370f21e9a93f746319c545` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Movies.zip`
  - `In-situ Meas Data.zip.sha256` | size=`64` | sha256=`3562b165d9d2fb2fcebec691c578adefd340586f13b03c04faf19355ab035e83` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/In-situ%20Meas%20Data.zip.sha256`
  - `Movies.zip.sha256` | size=`64` | sha256=`3d5b6dbcba61e7552b683a23fb77aa473b2d0a327bae99d437c5e1c626d1f5e6` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Movies.zip.sha256`
  - `Build Command Data.zip.sha256` | size=`64` | sha256=`e3dac9ac48daa5fdd7192d3aeabc1bbf66c32810b18d8d27a45c690487547ae0` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Build%20Command%20Data.zip.sha256`
  - `Metadata.zip.sha256` | size=`64` | sha256=`81e97cc0291c9588785ca9dddf701be20b75a5589ce0e59d82934b93d47686ed` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Metadata.zip.sha256`
  - `Metadata.zip` | size=`2489233` | sha256=`cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Metadata.zip`
  - `Build Command Data.zip` | size=`7419446651` | sha256=`de8a05ebd27f80bd79b6545c9f8a79c0e60230290e1799d9151f14f7429594b1` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/Build%20Command%20Data.zip`
  - `In-situ Meas Data.zip` | size=`9170420366` | sha256=`4db83f84cce2f4a28e75830a5df496c9a04db5e5554513924434463081ab645f` | downloadURL=`https://data.nist.gov/od/ds/85196AB9232E7202E053245706813DFA2044/In-situ%20Meas%20Data.zip`

## Metadata.zip qualification / Metadata.zip 적격성
- size_nerdm: `2489233`
- size_local: `2489233`
- sha256_nerdm: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`
- sha256_preregistered: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`
- sha256_local: `cf788593b45675dfbf380782b9141ebafd85bf6653f8ca57f0cf69d578c60ee6`
- checksum_match_all: `True`

## Archive inventory / archive inventory
- member_count: `5`
- members:
  - `Metadata/20170619_In625_HPAlloys_0.25x1x4.pdf` | size=`174156`
  - `Metadata/2018_AMMTLaserScanAngles.txt` | size=`3307`
  - `Metadata/201807_LayerCamera_DotGrid.bmp` | size=`2561078`
  - `Metadata/20180708_PowderComposition&PSD.txt` | size=`535`
  - `Metadata/AMB2018-01_625_MaterialCertificate.pdf` | size=`499576`

## Schema/string summaries / schema·문자열 요약
### `Metadata/2018_AMMTLaserScanAngles.txt`
- bounded_design_lines:

### `Metadata/20180708_PowderComposition&PSD.txt`
- bounded_design_lines:
  - L21: IN625 Particle Size Distribution (micron)

## Pre-outcome status / outcome 전 상태
- metadata_zip_checksum_gate: `True`
- Candidate numerical outcomes inspected: `NO`
- Large archives downloaded: `NO`
- Full seven-dimension F34 gate remains pending interpretation of this metadata-only evidence.

