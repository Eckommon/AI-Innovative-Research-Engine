# Global Public Data Source Registry v0.2 / 글로벌 공공데이터 소스 레지스트리 v0.2

## Purpose / 목적

권위 있는 공공·연구 데이터 소스를 국가·지역·기관별로 관리하고, 혁신 탐색 파이프라인에서 우선 조사할 소스를 기록한다. 이 문서는 소스 수준 레지스트리이며 개별 데이터셋 승인 목록이 아니다.  
Maintain an authoritative shortlist of public/research data sources by jurisdiction and institution for the innovation-discovery pipeline. This is a source-level registry, not an approval list for individual datasets.

데이터 개수·API·접근조건·플랫폼 기능뿐 아니라 **historical snapshot retention/recoverability**도 변할 수 있으므로 각 조사·재현 Wave에서 재검증한다.  
Dataset counts, APIs, access conditions, platform capabilities, and **historical snapshot retention/recoverability** are dynamic and must be re-verified during research and reproduction waves.

**v0.2 lesson / v0.2 교훈:** `EU-STEEL-R01` showed that an official dataset ID may remain citable after the exact historical dataflow required for reproduction is no longer disseminated. Current accessibility and historical recoverability are therefore tracked separately. / 공식 dataset ID가 인용 가능하게 남아 있어도 재현에 필요한 historical dataflow가 더 이상 배포되지 않을 수 있으므로 현재 접근성과 historical 복구가능성을 분리한다.

## Wave 0 — Methodological Benchmark / 방법론 기준

| Jurisdiction / 관할 | Source / 소스 | URL | Role / 역할 | Status |
|---|---|---|---|---|
| United States / 미국 | NIST AM Bench | https://www.nist.gov/ambench | 첨단제조 실험·측정·benchmark 기준 / experimental measurement benchmark for advanced manufacturing | `ACTIVE_BENCHMARK` |
| United States / 미국 | NIST Data Catalog | https://data.nist.gov/ | NIST 연구데이터 탐색 / NIST research dataset discovery | `DISCOVERED` |

## Wave 1 — Priority Expansion / 1차 우선 확장

### United States / 미국

| Source | URL | Primary Use / 주요 용도 | Notes / 비고 | Status |
|---|---|---|---|---|
| Data.gov Catalog | https://catalog.data.gov/ | 연방·공공 데이터셋 탐색 / federal/public dataset discovery | 카탈로그·API 수집 후보 / catalog/API harvesting candidate | `PRIORITY_A` |
| Resources.data.gov | https://resources.data.gov/ | 거버넌스·메타데이터·품질·표준 / governance, metadata, quality, standards | 원시 데이터보다 방법론 참조 / methodology reference | `PRIORITY_A` |
| NIST | https://www.nist.gov/ | 제조·측정·소재·표준 / manufacturing, measurement, materials, standards | 기관 심층탐색 / agency deep search | `PRIORITY_A` |
| U.S. Department of Energy | https://www.energy.gov/data | 전력·에너지·그리드·인프라 / energy, grid, infrastructure | 제조·AI 인프라 결합 후보 / cross-domain join candidate | `PRIORITY_A` |
| NOAA | https://www.noaa.gov/ | 기상·기후·해양·환경 / weather, climate, ocean, environment | 시간·공간 조인 강점 / strong temporal-spatial joins | `PRIORITY_A` |
| EPA | https://www.epa.gov/data | 환경·배출·시설 / environment, emissions, facilities | 산업–전력–환경 조인 / industry-energy-environment joins | `PRIORITY_A` |
| USGS | https://www.usgs.gov/ | 핵심광물·지질·수자원 / critical minerals, geology, water | 자원·공급망·순환경제 / resources and supply-chain research | `PRIORITY_A` |
| NASA Open Data | https://data.nasa.gov/ | 지구관측·원격탐사 / earth observation and remote sensing | 공간·물리 측정 / spatial and physical measurements | `PRIORITY_B` |

### Korea / 한국

| Source | URL | Primary Use / 주요 용도 | Notes / 비고 | Status |
|---|---|---|---|---|
| 공공데이터포털 / Public Data Portal | https://www.data.go.kr/ | 중앙 공공데이터 검색·API / central public-data discovery and APIs | 한국 1차 카탈로그 / primary Korean catalog | `PRIORITY_A` |
| KOSIS 국가통계포털 / KOSIS | https://kosis.kr/ | 공식 통계 / official statistics | 국가·지역·산업 baseline / cross-domain baseline | `PRIORITY_A` |
| 한국전력·전력 공식 소스 / KEPCO and official electricity sources | https://home.kepco.co.kr/ | 전력수요·설비 후보 / electricity demand and infrastructure | 구체 endpoint 재검증 필요 / endpoint-specific verification required | `DISCOVERED` |
| 기상청 기상자료개방포털 / KMA Open Data | https://data.kma.go.kr/ | 기상·기후 / weather and climate | 시간·공간 조인 강점 / strong temporal-spatial joins | `PRIORITY_A` |
| 국가공간정보·VWorld / National Spatial Data & VWorld | https://www.vworld.kr/ | 토지·건축·공간정보 / land, buildings, geospatial | 공간 조인 / spatial joins | `PRIORITY_B` |

### European Union / 유럽연합

| Source | URL | Primary Use / 주요 용도 | Notes / 비고 | Status |
|---|---|---|---|---|
| data.europa.eu | https://data.europa.eu/ | 범EU 오픈데이터 탐색 / pan-European open-data discovery | DCAT-AP 기반 통합 / DCAT-AP integration | `PRIORITY_A` |
| Eurostat | https://ec.europa.eu/eurostat/ | 조화된 EU 통계 / harmonized EU statistics | 국가 간 비교 backbone; historical dataset retention must be checked per claim / 국가간 비교 backbone·historical 보존성 별도 확인 | `PRIORITY_A` |
| European Environment Agency | https://www.eea.europa.eu/ | 환경·기후 / environment and climate | 산업·에너지·환경 조인; chart/raw snapshot hashes recommended / 산업·에너지·환경 조인·snapshot hash 권고 | `PRIORITY_A` |
| ENTSO-E Transparency Platform | https://transparency.entsoe.eu/ | 발전·부하·전력망 / electricity generation, load, grid | 고가치 전력시스템 후보 / high-value power-system candidate | `PRIORITY_A` |

## Wave 2 — Secondary Expansion / 2차 확장

| Jurisdiction / 관할 | Source | URL | Research Strength / 연구 강점 | Status |
|---|---|---|---|---|
| Japan / 일본 | e-Stat | https://www.e-stat.go.jp/ | 공식 통계·지역/mesh 분석 / official statistics and regional mesh analysis | `WAVE_2` |
| Japan / 일본 | Digital Agency data resources | https://www.digital.go.jp/ | 정부 데이터 생태계 / government data ecosystem | `WAVE_2` |
| United Kingdom / 영국 | data.gov.uk | https://www.data.gov.uk/ | 경제·환경·토지·교통 / economy, environment, land, transport | `WAVE_2` |
| Singapore / 싱가포르 | data.gov.sg | https://data.gov.sg/ | 도시·교통·환경·주택 API / urban, transport, environment, housing APIs | `WAVE_2` |

## Wave 3 — Broader Expansion / 3차 확장

| Jurisdiction / 관할 | Source | URL | Research Strength / 연구 강점 | Status |
|---|---|---|---|---|
| Canada / 캐나다 | Open Government | https://open.canada.ca/ | 자원·환경·산업·공간 / resources, environment, industry, geospatial | `WAVE_3` |
| Australia / 호주 | data.gov.au | https://data.gov.au/ | 자원·환경·공간 / resources, environment, geospatial | `WAVE_3` |
| Global / 글로벌 | OECD Data | https://data.oecd.org/ | 국가 간 정규화·비교 / cross-national normalization | `WAVE_3` |
| Global / 글로벌 | World Bank Data | https://data.worldbank.org/ | 경제·개발 baseline / development and economic baseline | `WAVE_3` |
| Global / 글로벌 | WHO / GLASS | https://www.who.int/initiatives/glass | 항생제 내성·사용 감시 / antimicrobial resistance and use surveillance | `WAVE_3_DOMAIN` |

## Source Qualification Fields / 소스 적격성 필드

각 소스는 점진적으로 다음을 기록한다. / Each source should progressively capture:

### Current access / 현재 접근
- `source_id`
- jurisdiction / 관할
- operator/publisher / 운영·발행기관
- canonical URL
- API/catalog endpoint
- metadata standard (`DCAT`, `DCAT-AP`, `CKAN`, custom, etc.)
- authentication requirement / 인증
- rate/access constraints / 호출·접근 제한
- license/reuse policy / 라이선스·재사용
- update cadence / 갱신주기
- machine-readable formats / 기계판독 포맷
- domain coverage / 도메인 범위
- provenance quality / 출처 품질
- harvesting feasibility / 수집 가능성
- last verified date / 최종 검증일

### Historical reproducibility / Historical 재현성
- `historical_version_retention`: `strong / partial / none / unknown`
- `snapshot_recoverability`: `exact / current_only / archive_only / unavailable / unknown`
- snapshot/version identifier and hash when bytes are available / byte 확보 시 snapshot ID·hash
- discontinuation date if applicable / 배포중단일
- official replacement dataset, if any / 공식 replacement dataset
- `replacement_correspondence_evidence`: `authoritative / partial / weak / none`
- archive/mirror status / archive·mirror 상태
- `reproduction_risk`: `low / medium / high / blocked`

**Rule / 규칙:** a live current API does not prove historical reproducibility, and a similar successor dataset does not prove historical equivalence. / 현재 API가 살아 있다는 사실은 historical 재현성을 증명하지 않으며 유사 후속 dataset도 historical 동등성을 증명하지 않는다.

## Current Priority Logic / 현재 우선순위 논리

Wave 1 데이터셋 선별은 단순 국가 순회가 아니라 `registry/RESEARCH_MATERIAL_LANDSCAPE.md`에서 선정된 고가치 소재를 중심으로 수행한다.  
Wave 1 dataset discovery is guided by the high-value topics selected in `registry/RESEARCH_MATERIAL_LANDSCAPE.md`, rather than by indiscriminate country-by-country harvesting.

기본 순서는 / Default order:
1. United States / 미국 — Data.gov, NIST, DOE, NOAA, EPA, USGS
2. Korea / 한국 — data.go.kr, KOSIS, KMA, electricity and spatial sources
3. EU / 유럽연합 — data.europa.eu, Eurostat, EEA, ENTSO-E

Historical reproduction candidates receive an additional lineage gate before experiment promotion. / historical 재현 후보는 실험 승격 전 별도 lineage gate를 적용한다.

공식 산출물은 `LANG-001`을 따른다. / Official artifacts comply with `LANG-001`.
