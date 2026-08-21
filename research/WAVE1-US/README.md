# Wave 1 — United States / 미국 데이터셋 탐색

**Work Queue:** Issue #2  
**State / 상태:** `FIRST_PASS_COMPLETE`  
**Date / 기준일:** 2026-08-21

## 1. Objective / 목적

P0 연구 소재에 대해 미국의 공식·공공 연구데이터를 실제 데이터셋 수준으로 선별하고 `Dataset IPS → join candidate → hypothesis candidate` 경로를 구축한다.  
Screen U.S. official/public research datasets for P0 topics and construct a `Dataset IPS → join candidate → hypothesis candidate` path.

## 2. Shortlist / 우선 후보

| ID | Dataset / 데이터셋 | Domain / 분야 | Access / 접근 | Coverage / 범위 | Dataset IPS* | State |
|---|---|---|---|---|---:|---|
| `US-AM-001` | NIST Fully Registered In-Situ & Ex-Situ PBF Dataset | smart manufacturing / 스마트제조 | Data.gov/NIST; ZIP | four AMMT Overhang Part X4 parts; registered numerical process + in-situ + XCT data | **94** | `PRIORITY_A` |
| `US-GRID-001` | EIA Hourly Electric Grid Monitor / EIA-930 | grid / 전력망 | EIA Open Data API | hourly balancing-authority demand, forecast, generation, interchange | **91** | `PRIORITY_A` |
| `US-GRID-002` | LBNL Queued Up 2026 | interconnection / 계통연계 | XLSX + codebook/report | project-level queues through end-2025; ~98% of installed U.S. generating capacity represented by covered operators | **89** | `PRIORITY_A` |
| `US-CLIMATE-001` | NOAA Storm Events Database | climate/infrastructure / 기후·인프라 | bulk CSV HTTP/FTP | 1950–May 2026; event, location, fatality files; full event-type coverage from 1996 | **87** | `PRIORITY_A` |
| `US-MINERAL-001` | USGS Mineral Commodity Summaries 2026 Data Release | critical minerals / 핵심광물 | USGS Science Data Catalog | 2021–2025 source period; 90+ minerals/materials | **89** | `PRIORITY_A` |
| `US-PORT-001` | BTS Port Data | ports/logistics / 항만·물류 | JSON/XML/CSV API | U.S. port characteristics; updated May 2026 | **81** | `PRIORITY_B` |
| `US-PORT-002` | BTS vessel berthing/dwell & port performance series | ports/logistics / 항만·물류 | BTS Data Inventory/API/dashboard | port/vessel time metrics; weekly/monthly series depending product | **86** | `PRIORITY_A` |

`*` IPS values are first-pass criterion-based screening scores from verified metadata and documentation; file-level analysis may revise them. / IPS는 검증된 metadata·문서 기반 1차 기준별 점수이며 파일 수준 분석 후 변동 가능.

## 3. High-Value Combinations / 고가치 조합

### `C-US-001` — Grid Bottleneck Intelligence / 전력망 병목 지능화
`EIA-930 hourly grid + LBNL Queued Up + NOAA Storm Events (+ transmission asset data)`  
**Combination IPS estimate / 추정:** `93/100`

**Hypothesis candidate / 가설 후보:** 지역별 load growth, queue congestion, weather hazard를 결합하면 단순 peak-load 지표보다 신규 대규모 부하의 interconnection delay 또는 local stress를 더 잘 설명할 수 있다. / Combining regional load growth, queue congestion and weather hazards may explain interconnection delay or local stress better than peak-load measures alone.

### `C-US-002` — Port Weakest-Link Intelligence / 항만 최약고리 지능화
`BTS berth/dwell + port characteristics + NOAA weather + Census/BTS trade`  
**Combination IPS estimate:** `91/100`

Target candidates / 결과 후보: berth duration, dwell-time anomaly, throughput disruption, recovery time. / 접안시간·체류시간 이상·처리량 차질·회복시간.

### `C-US-003` — Critical Mineral Resilience / 핵심광물 회복력
`USGS MCS + trade + prices + recycling capacity + technology demand proxies`  
**Combination IPS estimate:** `92/100`

Target candidates: import-reliance stress, supply concentration, recovery/recycling leverage. / 수입의존 스트레스·공급집중·회수/재활용 효과.

### `C-US-004` — Registered Manufacturing Quality / 정렬 제조품질
NIST's registered PBF dataset already aligns process parameters, laser power, in-situ melt-pool characteristics, layerwise optical intensity and ex-situ XCT voxel values in a common machine coordinate system.  
NIST 데이터셋 자체가 공정변수·laser power·in-situ melt pool·layerwise optical intensity·ex-situ XCT voxel을 공통 machine coordinate로 정렬한다.

**Combination IPS estimate:** `96/100`  
This is a stronger downstream research candidate than AMBENCH-001 for reproducible ML because registration and uncertainty are explicitly documented. / 데이터 registration과 uncertainty가 명시되어 있어 AMBENCH-001보다 재현 ML 연구에 유리한 후속 후보.

## 4. Data-Center Data Gap / 데이터센터 데이터 공백

**Observed / 관측:** EIA launched voluntary pilot surveys in March 2026 covering Texas, Washington, and Northern Virginia/DC and asking about energy sources, electricity use, site characteristics, server metrics, and cooling systems. A mature public facility-level national dataset is therefore not yet equivalent to EIA-930 or EIA-861.  
**관측:** EIA는 2026년 3월 Texas·Washington·Northern Virginia/DC를 대상으로 에너지원·전기사용·site 특성·server metric·cooling system을 묻는 voluntary pilot survey를 시작했다. 따라서 전국 시설단위 공개 데이터는 아직 EIA-930/EIA-861 수준으로 성숙하지 않았다.

**Engine consequence / 엔진 판단:** `AI data center × grid × cooling × water` remains `P0`, but the U.S. project candidate is `HOLD_DATA_GAP` until a defensible facility-level source is available or a transparent proxy methodology is defined. / 소재 우선순위는 P0를 유지하되 시설단위 소스 또는 투명한 proxy 방법이 마련될 때까지 `HOLD_DATA_GAP`.

## 5. Verified Source Notes / 검증 출처 메모

- EIA Open Data: https://www.eia.gov/opendata/ — hourly balancing-authority demand, forecast, generation, interchange.
- LBNL Queued Up 2026: https://emp.lbl.gov/queues — project-level Excel, CC BY 4.0, data through 2025.
- NOAA Storm Events: https://www.ncei.noaa.gov/stormevents/ftp.jsp — bulk CSV, 1950–2026.
- NIST registered PBF dataset: https://catalog.data.gov/dataset/a-fully-registered-in-situ-and-ex-situ-dataset-for-metal-powder-bed-fusion-additive-manufa
- USGS MCS 2026 Data Release: https://data.usgs.gov/datacatalog/data/USGS%3A69837e43b66b01367d7ec7c7
- BTS Port Data: https://catalog.data.gov/dataset/port-data
- BTS Port Performance: https://www.bts.gov/ports
- EIA data-center pilot survey: https://www.eia.gov/pressroom/releases/press585.php

## 6. Next Actions / 다음 행동

1. promote `C-US-001` and `C-US-004` as highest-value U.S. feasibility candidates / 미국 최우선 feasibility 후보로 승격;
2. preserve `AI data center` as a data-gap watch rather than fabricate facility-level precision / 데이터센터는 precision을 가정하지 않고 data-gap watch 유지;
3. use U.S. candidates as reference mappings when screening Korea and EU / 한국·EU 비교 reference로 사용;
4. later inspect exact file schemas before any `EXPERIMENT` promotion / 실험 승격 전 파일 schema 정밀검토.

**Issue #2 disposition / 처리:** `FIRST_PASS_OBJECTIVE_COMPLETE`; proceed to Issue #3. / 1차 목적 완료 후 Issue #3으로 이동.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
