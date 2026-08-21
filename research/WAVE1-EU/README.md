# Wave 1 — European Union / 유럽연합 데이터셋 탐색

**Work Queue / 작업 큐:** Issue #4  
**State / 상태:** `FIRST_PASS_COMPLETE`  
**Date / 기준일:** 2026-08-21

## 1. Objective / 목적

**한국어**  
EU 수준에서 조화된 전력·산업·환경·기후·물류 데이터를 실제 데이터셋 및 공식 플랫폼 수준으로 선별하고, 국가 간 비교 가능한 조인 구조와 Dataset IPS/Combination IPS 후보를 만든다.

**English**  
Screen harmonized EU-level electricity, industry, environment, climate, and logistics data at the dataset/platform level and create cross-nationally comparable join structures with Dataset IPS and Combination IPS candidates.

## 2. Shortlist / 우선 후보

| ID | Dataset / Platform / 데이터셋·플랫폼 | Domain / 분야 | Structure / 구조 | Dataset IPS* | State |
|---|---|---|---|---:|---|
| `EU-GRID-001` | ENTSO-E Transparency Platform | electricity/grid / 전력망 | generation, actual/forecast load, transmission, balancing, outages, congestion management by standardized area concepts | **94** | `PRIORITY_A` |
| `EU-CLIMATE-001` | Copernicus ERA5 hourly single levels | weather/climate / 기상·기후 | global hourly gridded reanalysis from 1940; 0.25° atmosphere; API/ARCO access | **94** | `PRIORITY_A` |
| `EU-IND-001` | Eurostat short-term industrial production (`sts_ind_prod`) | industry / 산업 | harmonized NACE Rev.2 industrial production indices across B–E sectors and detailed classes | **88** | `PRIORITY_A` |
| `EU-IND-002` | EEA Industrial Reporting / Industrial Emissions Portal | industry/environment / 산업·환경 | facility location/admin + pollutant releases + waste transfers + large-combustion energy/emissions; 2007–2024 | **95** | `PRIORITY_A` |
| `EU-PORT-001` | Eurostat maritime transport | ports/logistics / 항만·물류 | port-level goods tonnes, passenger movement, vessel traffic/GT, container units/TEU; quarterly/annual | **87** | `PRIORITY_A` |
| `EU-STAT-001` | Eurostat Statistics/SDMX/Catalogue APIs | harmonization backbone / 조화 backbone | JSON-stat 2.0, SDMX 2.1/3.0, TSV/CSV-related dissemination and catalogue metadata | **92** | `INFRASTRUCTURE_A` |

`*` IPS는 공식 metadata/documentation 기반의 1차 기준별 score이며 실제 특정 extraction의 결측·coverage·API access를 검토하면 조정할 수 있다.  
`*` IPS values are first-pass criterion-based scores from official metadata/documentation and may change after inspection of missingness, coverage, and access for a specific extraction.

## 3. Key Verified Characteristics / 주요 검증 특성

### `EU-GRID-001` — standardized multi-country electricity operations / 표준화 다국가 전력 운영
ENTSO-E states that the Transparency Platform publishes generation, load, transmission, and balancing data under Regulation 543/2013, with additional outage and congestion-management views. The platform uses standardized process/document/business types and area concepts; exports/Web API require account/token handling for some automated access.  
ENTSO-E Transparency Platform은 Regulation 543/2013에 따라 발전·부하·송전·balancing 데이터를 공개하고 outage·congestion-management view도 제공한다. 표준화된 process/document/business type과 area concept를 사용하며 일부 자동화 접근은 계정·token 관리가 필요하다.

### `EU-CLIMATE-001` — harmonized physical exposure layer / 조화된 물리노출 레이어
ERA5 provides hourly globally consistent reanalysis from 1940 onwards on a regular lat/lon grid. The single-level atmospheric product is 0.25° and supports API retrieval; selected variables are also available in analysis-ready cloud-optimized Zarr.  
ERA5는 1940년 이후의 시간별 일관된 global reanalysis를 regular lat/lon grid로 제공하며 single-level atmosphere는 0.25°다. API와 일부 ARCO Zarr 접근을 지원한다.

### `EU-IND-002` — facility-level industrial outcome layer / 시설수준 산업 outcome 레이어
The European Industrial Emissions Portal covers more than 60,000 industrial sites across 65 economic activities and provides facility location/admin data, releases/transfers and waste; large combustion plants include more detailed energy-input and emissions data. EEA provides downloadable tabular and spatial versions; version 16.0 published in February 2026 covers 2007–2024.  
European Industrial Emissions Portal은 65개 경제활동의 6만 개 이상 산업시설을 다루며 시설 위치·행정정보·오염물질 배출/이동·폐기물 데이터를 제공한다. 대형연소시설은 에너지투입·배출 세부정보도 포함하며 2026년 2월 version 16.0 tabular/spatial 데이터가 2007–2024를 포괄한다.

### `EU-PORT-001` — harmonized port statistics / 조화된 항만통계
Eurostat maritime data are collected at port level and include goods weight, passengers, vessel counts/gross tonnage, and container units/TEU, available at port, maritime coastal area, country and NUTS regional levels.  
Eurostat 해운 데이터는 port-level에서 수집되고 화물중량·여객·선박척수/GT·컨테이너 unit/TEU를 포함하며 항만·MCA·국가·NUTS 지역 수준으로 제공된다.

## 4. High-Value Combinations / 고가치 조합

### `C-EU-001` — Cross-National Grid Stress Intelligence / 국가간 전력망 스트레스 지능화
`ENTSO-E load/generation/transmission/outage/congestion + ERA5 + Eurostat industrial production`  
**Combination IPS estimate / 추정:** **96/100**

**Hypothesis candidate / 가설 후보**  
기상노출·산업활동·실제 부하·발전 mix·cross-border flow·outage/congestion 정보를 결합하면 단순 national peak-load 지표보다 bidding-zone 단위 stress와 cross-border dependency regime을 더 잘 분류할 수 있다.  
Combining weather exposure, industrial activity, actual load, generation mix, cross-border flow, outages, and congestion information can classify bidding-zone stress and cross-border dependency regimes better than national peak-load indicators alone.

**Target candidates / 결과 후보:** load-forecast error, cross-border flow stress, congestion-management activation, outage-adjusted resilience. / 수요예측오차, 국경간 조류 stress, congestion-management 작동, outage 보정 회복력.

**Risk / 위험:** ENTSO-E bidding zones/control areas are not equivalent to NUTS administrative regions; explicit spatial mapping is required. / bidding zone/control area는 NUTS 행정구역과 동일하지 않아 명시적 mapping 필요.

### `C-EU-002` — Industrial Energy–Emission Efficiency / 산업 에너지–배출 효율
`EEA industrial facility reporting + Eurostat industrial production + ERA5 + energy-price/energy-system statistics`  
**Combination IPS estimate:** **95/100**

**Hypothesis candidate / 가설 후보:** facility-level emissions/energy-input와 산업생산·기상·에너지 조건을 결합하면 국가 평균보다 시설·sector별 탈탄소 효율 또는 stress를 정밀하게 구분할 수 있다. / Facility-level emissions/energy-input combined with industrial production, weather and energy conditions may distinguish decarbonization efficiency or stress more precisely than national averages.

**Constraint / 제약:** facility reporting thresholds, country reporting completeness, economic-activity coding, and time lags require explicit handling. / 보고 threshold·국가별 completeness·경제활동 coding·시차를 명시적으로 처리해야 함.

### `C-EU-003` — Port Climate & Trade Resilience / 항만 기후·무역 회복력
`Eurostat port-level maritime data + ERA5 + trade/industry statistics`  
**Combination IPS estimate:** **91/100**

**Target candidates / 결과 후보:** quarterly/annual throughput anomaly, vessel-traffic disruption, climate-exposure sensitivity. / 처리량 이상, 선박교통 차질, 기후노출 민감도.

**Limitation / 한계:** Eurostat's harmonized maritime statistics are less event-granular than Korea's PORT-MIS vessel-timestamp data; the EU strength is comparability rather than operational event resolution. / Eurostat 해운통계는 한국 PORT-MIS보다 이벤트 세밀도가 낮고 EU의 강점은 운영 해상도보다 비교가능성이다.

### `C-EU-004` — Industrial Site Climate Risk / 산업시설 기후위험
`EEA industrial-site coordinates + ERA5/Copernicus hazards + emissions/energy input`  
**Combination IPS estimate:** **94/100**

This creates a direct facility-coordinate × physical-hazard relationship suitable for spatial stress tests. / 시설 좌표와 물리위험을 직접 연결할 수 있어 공간 stress test에 적합.

## 5. EU Comparative Advantage / EU 데이터의 비교우위

**한국어**  
EU의 가장 큰 강점은 개별 데이터셋의 극단적 해상도보다 **표준·분류·국가 간 조화성**이다. Eurostat의 NACE/NUTS와 SDMX/JSON-stat API, ENTSO-E의 표준화된 electricity area/document semantics, EEA의 공통 industrial-reporting 구조가 서로 다른 회원국 데이터를 같은 연구 레이어로 올릴 수 있게 한다.

**English**  
The EU's greatest advantage is not necessarily extreme resolution of each dataset, but **standards, classifications, and cross-national harmonization**. Eurostat's NACE/NUTS and SDMX/JSON-stat APIs, ENTSO-E's standardized electricity area/document semantics, and EEA's common industrial-reporting structure make it possible to place heterogeneous Member-State evidence into a shared research layer.

## 6. Cross-National Mapping Notes / 국가간 매핑 주의

- ENTSO-E bidding zone / control area ≠ Eurostat NUTS by default. / ENTSO-E zone과 NUTS는 기본적으로 동일하지 않음.
- NACE Rev.2 must be explicitly mapped to KSIC/NAICS for Korea/U.S. comparison. / NACE Rev.2는 KSIC/NAICS와 명시 mapping 필요.
- Eurostat states that its database exposes the latest dataset state and does not itself provide full historical versioning of every dataset; engine snapshots/version hashes should therefore be stored for reproducibility. / Eurostat 최신상태 DB는 모든 과거버전을 자체 보존하지 않으므로 엔진 측 snapshot/version hash 필요.
- ERA5 grid cells require spatial aggregation/matching to facilities, ports, NUTS, or bidding zones. / ERA5 grid를 시설·항만·NUTS·bidding zone으로 공간집계·매핑해야 함.

## 7. Verified Sources / 검증 출처

- ENTSO-E Transparency Platform: https://www.entsoe.eu/data/transparency-platform/
- ENTSO-E Manual of Procedures: https://www.entsoe.eu/data/transparency-platform/mop/
- Eurostat API: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started
- Eurostat industrial production metadata: https://ec.europa.eu/eurostat/cache/metadata/EN/sts_ind_prod_esms_el.htm
- Eurostat maritime transport: https://ec.europa.eu/eurostat/web/transport/information-data/maritime-transport
- Copernicus ERA5: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels
- Copernicus API setup: https://cds.climate.copernicus.eu/en/how-to-api
- EEA Industrial Emissions Portal dataset: https://industry.eea.europa.eu/industrial-emissions/dataset
- EEA Industrial Reporting datahub: https://www.eea.europa.eu/en/datahub/datahubitem-view/9405f714-8015-4b5b-a63c-280b82861b3d

## 8. First-Pass Decision / 1차 판단

**한국어**  
EU Wave 1의 가장 강한 후보는 `C-EU-001`과 `C-EU-002`다. `C-EU-001`은 국가간 전력망·기후·산업 스트레스를 표준적으로 비교할 수 있고, `C-EU-002`는 6만 개 이상의 시설 위치·배출·에너지 데이터와 산업통계를 결합해 산업 탈탄소/효율 문제를 시설수준으로 내릴 수 있다.

**English**  
The strongest EU Wave 1 candidates are `C-EU-001` and `C-EU-002`. `C-EU-001` enables standardized cross-national grid–climate–industry stress analysis, while `C-EU-002` can combine location, emissions and energy information from more than 60,000 industrial sites with harmonized production statistics to move industrial decarbonization/efficiency analysis toward the facility level.

**Issue #4 disposition / 처리:** `FIRST_PASS_OBJECTIVE_COMPLETE`.  
Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
