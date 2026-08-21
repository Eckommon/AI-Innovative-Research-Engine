# Wave 1 — Korea / 한국 데이터셋 탐색

**Work Queue / 작업 큐:** Issue #3  
**State / 상태:** `FIRST_PASS_COMPLETE`  
**Date / 기준일:** 2026-08-21

## 1. Objective / 목적

**한국어**  
P0 연구 소재에 대해 한국의 공식 공공데이터를 실제 데이터셋 수준으로 선별하고, 데이터의 시간·공간 해상도, 조인 가능성, 결과변수 후보, Dataset IPS와 고가치 조합을 기록한다.

**English**  
Screen official Korean public datasets at the dataset level for P0 research topics and record temporal/spatial resolution, joinability, candidate outcomes, Dataset IPS, and high-value combinations.

## 2. Shortlist / 우선 후보

| ID | Dataset / 데이터셋 | Domain / 분야 | Structure / 구조 | Dataset IPS* | State |
|---|---|---|---|---:|---|
| `KR-GRID-001` | KPX 모선별 5분 단위 상태추정 / KPX 5-minute bus-level state estimates | grid / 전력망 | monthly high-frequency bus voltage and estimated inflow/outflow MW; 5-min | **95** | `PRIORITY_A` |
| `KR-GRID-002` | KPX 5분 단위 전력수요 예측 / KPX 5-minute demand forecasts | grid/load / 전력수요 | 5-minute forecast files by month | **90** | `PRIORITY_A` |
| `KR-RENEW-001` | KPX 지역별 5분단위 풍력 계량데이터 / regional 5-minute wind metering | renewable/grid / 재생·계통 | region + trade date + 5-minute Wh metering | **87** | `PRIORITY_A` |
| `KR-LOAD-001` | KEPCO 산업분류별 전력사용량 API / electricity use by industry classification | regional/industry load / 지역·산업부하 | month + province/city + KSIC industry + kWh/customer/revenue | **91** | `PRIORITY_A` |
| `KR-LOAD-002` | KEPCO 법정동/시간대별 전력사용량 시범통계 / legal-dong × time-of-day power-use pilot data | fine-grained demand / 세부 수요 | legal-dong and time-of-day pilot statistics | **88** | `PRIORITY_A` |
| `KR-CLIMATE-001` | KMA ASOS 시간자료 / KMA ASOS hourly observations | weather/climate / 기상·기후 | real-time hourly station observations; temperature, precipitation, pressure, humidity etc. | **91** | `PRIORITY_A` |
| `KR-IND-001` | 한국산업단지공단 전국산업단지현황 / KICOX national industrial-complex statistics | industrial geography / 산업입지 | quarterly CSV; industrial-complex identity, area, tenant/operating firms etc. | **82** | `PRIORITY_B` |
| `KR-IND-002` | 공장등록현황 시도×업종 / registered factories by province × KSIC | manufacturing structure / 제조 구조 | monthly; 17 provinces × KSIC classification | **79** | `PRIORITY_B` |
| `KR-PORT-001` | PORT-MIS 선박관제·운항·입출항 데이터 / vessel control, movement and port calls | logistics / 항만물류 | vessel call sign + port + arrival/departure timestamp; near-real-time/API or annual extracts | **90** | `PRIORITY_A` |
| `KR-PORT-002` | 외항화물·컨테이너 정보 / international cargo and container data | trade/logistics / 무역·물류 | port + call sign + country/OD + cargo/container + timestamps | **89** | `PRIORITY_A` |

`*` 첫 IPS는 공식 metadata와 문서에 기반한 기준별 screening score이며 실제 파일 schema·결측·ID 안정성 검토 후 조정할 수 있다.  
`*` First-pass IPS values are criterion-based screening scores from official metadata and may change after file-level schema, missingness, and identifier-stability inspection.

## 3. Key Verified Characteristics / 주요 검증 특성

### `KR-GRID-001` — unusually high-resolution public grid state data / 이례적으로 세밀한 공개 계통상태 데이터
KPX describes monthly 5-minute bus-level state estimates containing time, bus number, estimated kV, and estimated MW inflow/outflow sums. The official board contained 168 monthly entries as of the 2026-08 review; the June 2026 release is split into five large ZIP files.  
KPX는 시간, 모선번호, 상태추정 kV 및 송전단 유입/유출 조류 합계 MW를 5분 간격으로 월별 공개한다. 2026-08 조사 시 공식 게시판에는 168개 월별 게시물이 존재했고, 2026년 6월 데이터는 5개의 대용량 ZIP으로 나뉘어 제공됐다.

### `KR-LOAD-001` — industry × geography electricity-use API / 산업×지역 전력사용 API
KEPCO Open Data exposes `year`, `month`, province (`metroCd`), city/county/district (`cityCd`) and KSIC-derived industry (`bizCd`) as query dimensions and returns JSON/XML.  
KEPCO 전력데이터 개방포털은 `year`, `month`, 시도(`metroCd`), 시군구(`cityCd`), 한국표준산업분류 기반 `bizCd`를 조회축으로 제공하며 JSON/XML로 응답한다.

### `KR-CLIMATE-001` — station/time joins / 관측소·시간 조인
KMA ASOS offers real-time hourly observations through REST JSON/XML, and separate station metadata includes station number and latitude/longitude history. This supports explicit spatial mapping rather than name-only joins.  
KMA ASOS는 REST JSON/XML 기반 실시간 시간자료를 제공하며 별도 지점정보에는 지점번호와 위·경도 이력이 있어 명칭 추정이 아니라 명시적 공간 매핑이 가능하다.

### `KR-PORT-001/002` — operational logistics identifiers / 운영 물류 ID
PORT-MIS-derived APIs expose port, vessel call sign, arrival/departure time, control events, cargo/container and origin/destination-related fields. This enables event-level linkage unavailable in many aggregate port-statistics systems.  
PORT-MIS 계열 API는 항만, 호출부호, 입출항시각, 관제 이벤트, 화물/컨테이너 및 출발·도착 관련 필드를 제공해 단순 집계 통계보다 세밀한 이벤트 수준 연결이 가능하다.

## 4. High-Value Combinations / 고가치 조합

### `C-KR-001` — Grid Bottleneck Intelligence / 전력망 병목 지능화
`KPX bus-state 5min + KPX demand forecast + renewable metering + KMA weather + KEPCO regional/industry load`  
**Combination IPS estimate / 추정:** **97/100**

**Hypothesis candidate / 가설 후보**  
한국의 모선별 전압·조류 상태와 5분 수요·재생에너지·기상을 결합하면 단순 총수요/피크수요보다 지역·시간별 voltage/flow stress와 forecast error regime을 더 잘 탐지할 수 있다.  
Combining bus-level voltage/flow states with 5-minute demand, renewable metering and weather can detect localized voltage/flow stress and forecast-error regimes better than aggregate demand or peak-load indicators alone.

**Potential target / 결과 후보:** abnormal `state-estimated kV/MW`, stress episodes, demand-forecast error, renewable-induced variability. / 비정상 전압·조류, stress episode, 수요예측오차, 재생에너지 변동성.

**Main risk / 핵심 위험:** mapping `bus_number` to public geographic/asset semantics may be incomplete. / `모선번호`를 공개 지리·설비 의미와 연결하는 mapping이 불완전할 수 있음.

### `C-KR-002` — Industrial-Complex Energy Stress / 산업단지 에너지 스트레스
`KICOX industrial complexes + registered factories/KSIC + KEPCO industry electricity + KMA weather (+ KPX grid)`  
**Combination IPS estimate:** **94/100**

**Hypothesis candidate / 가설 후보:** 산업구성·단지규모·기온조건을 결합하면 지역별 산업 전력수요 탄력성과 계절/폭염 peak exposure를 설명할 수 있다. / Industrial mix, complex scale and weather may explain regional industrial electricity-demand elasticity and seasonal/heat-wave peak exposure.

**Constraint / 제약:** KICOX 일부 생산·수출·고용 항목은 2025 Q3부터 공표가 일시 중단되어 outcome coverage가 약해질 수 있다. / Some KICOX production/export/employment fields have been temporarily suspended since 2025 Q3, weakening outcome coverage.

### `C-KR-003` — Port Weakest-Link Intelligence / 항만 최약고리 지능화
`PORT-MIS vessel timestamps + facility use + cargo/container + KMA weather`  
**Combination IPS estimate:** **95/100**

**Target candidates / 결과 후보:** anchorage/berth delay proxies, vessel turnaround, port congestion, disruption/recovery. / 정박·선석 지연 proxy, 선박 turnaround, 항만 혼잡, 장애·회복.

### `C-KR-004` — AI/Data-Center Regional Load Proxy / AI·데이터센터 지역부하 Proxy
`KEPCO information-communications/general-use electricity + legal-dong time-of-day demand + regional grid state + land/building candidate data`  
**State:** `HOLD_PROXY_VALIDATION`

한국도 시설별 데이터센터 실제 소비전력·냉각·물사용을 전국적으로 직접 식별하는 공개 source는 이번 first pass에서 확인하지 못했다. 정보통신업·일반용 수요 등을 무비판적으로 데이터센터 소비로 간주하지 않는다.  
This first pass did not establish a nationwide public source that directly identifies facility-level data-center electricity, cooling, and water use. Information-communications or general-use electricity categories must not be treated uncritically as data-center consumption.

## 5. Cross-National Mapping Notes / 국가 간 비교 매핑 주의

- KEPCO/KICOX의 한국표준산업분류(KSIC)는 미국 NAICS 또는 EU NACE와 별도 mapping이 필요하다. / KSIC requires explicit mapping to U.S. NAICS or EU NACE.
- `법정동`, `시군구`, `시도`, 산업단지 경계는 서로 다른 공간단위다. / legal-dong, city/county/district, province and industrial-complex boundaries are distinct spatial units.
- KPX `bus_number`는 행정구역 ID가 아니다. / KPX `bus_number` is not an administrative geography key.
- 5분 계통자료와 월별 전력사용량을 결합할 때 aggregation-level mismatch를 명시해야 한다. / 5-minute grid data and monthly consumption require explicit aggregation-level reconciliation.

## 6. Verified Sources / 검증 출처

- KPX 모선별 5분 상태추정: https://kpx.or.kr/board.es?bid=0067&mid=a10109020500
- KPX 5분 전력수요 예측: https://new.kpx.or.kr/board.es?bid=0065&mid=a10109020700&npage=1
- Public Data Portal — bus-state dataset: https://www.data.go.kr/data/15051423/fileData.do
- Public Data Portal — regional 5-minute wind metering: https://www.data.go.kr/data/15099452/fileData.do
- KEPCO power-use-by-industry API: https://bigdata.kepco.co.kr/cmsmain.do?pcode=000493&pstate=indus&redirect=Y&scode=S01
- KEPCO shared/pilot data: https://bigdata.kepco.co.kr/cmsmain.do?pcode=000502&pstate=L&redirect=Y&scode=S01
- KMA ASOS hourly API: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057210
- KICOX industrial-complex statistics: https://www.data.go.kr/data/15085886/fileData.do
- KICOX registered factories by industry: https://www.data.go.kr/data/15085508/fileData.do
- Ministry of Oceans and Fisheries port facility use: https://www.data.go.kr/data/3056955/openapi.do
- vessel control: https://www.data.go.kr/data/15006354/openapi.do
- international cargo: https://www.data.go.kr/data/15056658/openapi.do
- container data: https://www.data.go.kr/data/15131742/openapi.do

## 7. First-Pass Decision / 1차 판단

**한국어**  
한국 Wave 1에서 가장 강한 후보는 `C-KR-001`이다. 미국 EIA-930이 balancing-authority 수준의 시간별 데이터를 제공하는 반면, 한국 KPX는 공개된 모선별 5분 상태추정을 통해 훨씬 더 세밀한 물리계통 signal을 제공한다. 단, 모선번호의 지리·설비 의미 mapping 가능성을 먼저 확인해야 실제 지역 병목 모델로 승격할 수 있다.

**English**  
The strongest Korean Wave 1 candidate is `C-KR-001`. Whereas U.S. EIA-930 provides hourly balancing-authority-level data, Korea's public KPX bus-level 5-minute state estimates provide a substantially finer physical grid signal. However, geographic/asset mapping of bus identifiers must be validated before promotion to a localized bottleneck model.

**Issue #3 disposition / 처리:** `FIRST_PASS_OBJECTIVE_COMPLETE`; proceed to Issue #4 EU / 유럽연합.  
Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
