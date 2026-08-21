# Research Material Landscape v0.1 / 연구 소재 탐색 지형 v0.1

**Date / 기준일:** 2026-08-21  
**State / 상태:** `SCREENING_BASELINE`  
**Evidence rule / 증거 규칙:** 소재 선별 점수는 IPS가 아니며 실제 데이터셋 검토 전에는 `HYPOTHESIZED`/screening 판단이다. / Topic-screening scores are not IPS and remain screening judgments until actual datasets are inspected.

## 1. Objective / 목적

**한국어**  
`AMBENCH-001`을 본격 보정하기 전에 엔진이 어떤 문제영역을 장기적으로 탐색할지 넓게 스캔한다. 범위는 (A) 현대사회에서 성장성과 파급력이 큰 유망 분야와 (B) 이미 산업화·보급되었지만 구조적 병목이 남은 분야를 모두 포함한다.

**English**  
Before full `AMBENCH-001` calibration, scan the broader problem space that the engine should explore over time. The scope includes both (A) high-growth, high-impact frontier domains and (B) mature systems where persistent structural bottlenecks remain.

## 2. Topic Screening Criteria / 소재 선별 기준

이 점수는 `Research Material Screening Score (RMSS)`이며 Dataset/Combination/Project IPS와 분리한다. / This is a `Research Material Screening Score (RMSS)`, separate from Dataset/Combination/Project IPS.

| Criterion / 기준 | Max |
|---|---:|
| Societal & industrial impact / 사회·산업 파급력 | 20 |
| Bottleneck or opportunity strength / 병목·기회 강도 | 20 |
| Public/research data availability / 공공·연구데이터 확보 가능성 | 20 |
| Cross-dataset join potential / 데이터 결합 가능성 | 15 |
| Falsifiability & measurable outcomes / 반증·측정 가능성 | 15 |
| Cross-region scalability / 국가·지역 확장성 | 10 |
| **Total / 합계** | **100** |

`RMSS`는 정밀 통계점수가 아니라 연구 우선순위용 전문가 선별값이다. / `RMSS` is an expert screening value for research prioritization, not a statistically calibrated score.

## 3. Frontier Opportunity Track / 현대 유망 영역

| Rank | Research Material / 연구 소재 | RMSS | Why Now / 현재성 | Candidate Data Relationships / 잠재 데이터 관계 | Priority |
|---:|---|---:|---|---|---|
| 1 | **AI data centers × grid × cooling × water / AI 데이터센터 × 전력망 × 냉각 × 물** | 96 | AI 컴퓨팅 전력밀도와 전력수요가 빠르게 증가하고 지역 전력망 영향이 집중됨 / rapidly rising compute density and locally concentrated electricity demand | data-center capacity + utility load + transmission congestion + weather + water stress + generation + land | `P0` |
| 2 | **AI-enabled smart manufacturing & digital twins / AI 스마트제조·디지털트윈** | 94 | 산업 AI는 빠르게 확대되지만 데이터 통합, 신뢰성, 센서 이질성, 설명가능성이 병목 / deployment constrained by data integration, heterogeneous sensing, trust and reliability | machine/sensor + quality + maintenance + production + energy + supply chain | `P0` |
| 3 | **Critical minerals × industrial demand × recycling / 핵심광물 × 산업수요 × 재활용** | 92 | 전력·반도체·배터리·AI 인프라가 광물 의존도를 높이고 공급집중·수입의존 문제가 지속 / growing strategic demand and concentrated supply | production/reserves + trade + prices + recycling + technology demand + geopolitical events | `P0` |
| 4 | **Climate-resilient infrastructure / 기후 회복력 인프라** | 91 | 극한기상 손실과 인프라 취약성이 운영·경제 데이터에 관측 가능 / extreme-weather losses and infrastructure vulnerability are measurable | weather hazards + outages + asset age + insurance/loss + transport/water/grid performance | `P0` |
| 5 | **Advanced semiconductor packaging & metrology / 첨단 반도체 패키징·계측** | 87 | heterogeneous integration이 확대되며 열·응력·warpage·소재특성 계측이 설계·신뢰성 병목 / heterogeneous integration raises thermal, stress, warpage and materials-metrology challenges | material properties + process + inline metrology + thermal/mechanical outcomes + reliability | `P1` |
| 6 | **Antimicrobial resistance intelligence / 항생제 내성 지능형 감시** | 86 | 다국가 표준 감시가 확대되고 임상·사용량·환경 데이터를 결합할 여지가 큼 / standardized surveillance is expanding and can be linked to use, clinical and environmental data | resistance + antibiotic use + population + hospital + wastewater/environment + mobility | `P1` |

## 4. Persistent Bottleneck Track / 기존 혁신의 잔존 병목

| Rank | Research Material / 연구 소재 | RMSS | Persistent Bottleneck / 잔존 병목 | Candidate Data Relationships / 잠재 데이터 관계 | Priority |
|---:|---|---:|---|---|---|
| 1 | **Transmission congestion & transformer supply / 송전혼잡·변압기 공급망** | 97 | 오래된 전력망에 신규 대규모 부하가 연결되며 송전 확충, 장비 리드타임, 과도한 사양 다양성이 병목 / grid expansion, equipment lead times and excessive specification variety constrain new load | congestion + interconnection queues + transformer specs/lead times + load growth + weather + prices | `P0` |
| 2 | **Additive-manufacturing quality, qualification & interoperability / 적층제조 품질·인증·상호운용성** | 95 | 공정변동성, 품질 불일치, 소재특성, 인증, 데이터 통합 문제가 광범위 채택을 제한 / variability, quality, material properties, qualification and data integration constrain adoption | process parameters + in-situ sensing + microscopy + geometry + material properties + qualification results | `P0` |
| 3 | **Port & logistics weakest-link resilience / 항만·물류 최약고리 회복력** | 93 | 항만·환적·국경 지점의 지연과 예측불확실성이 공급망 성과를 좌우 / delays and unpredictability at ports, transshipment hubs and borders dominate system performance | vessel calls + dwell time + weather + congestion + customs + trade flows + inland transport | `P0` |
| 4 | **Water leakage / non-revenue water / 상수도 누수·무수수량** | 90 | 성숙한 상수도망에서도 물리 누수·계량오차·비수익수가 재정과 물안보를 악화 / leakage, metering and non-revenue water undermine financial and resource sustainability | pipe age + pressure + repair events + meter data + drought + utility finance + terrain | `P1` |
| 5 | **Building retrofit & peak-load efficiency / 건물 리트로핏·피크부하 효율** | 89 | 기존 건축물이 장기간 존속하며 초기비용·개보수율·기후·난방/냉방 피크가 병목 / legacy building stock, upfront cost and retrofit rates constrain efficiency | building age/type + energy use + weather + retrofit + tariffs + socioeconomic data | `P1` |
| 6 | **Critical-material recovery / 핵심소재 회수·재활용** | 89 | 광물 수요 증가에도 폐제품·스크랩에서의 회수율, 경제성, 지역 처리능력에 병목 / recovery rates, economics and regional processing capacity lag strategic demand | scrap generation + commodity prices + trade + recycling capacity + product stock + policy | `P1` |

## 5. Evidence Supporting the Landscape / 지형 판단의 주요 근거

### AI, electricity, and grid / AI·전력·그리드
- IEA, *Electricity 2026*: https://www.iea.org/reports/electricity-2026
- IEA, *Key Questions on Energy and AI* (2026): https://www.iea.org/reports/key-questions-on-energy-and-ai
- U.S. DOE, *2026 Draft National Transmission Needs Study*: https://www.energy.gov/oe/national-transmission-needs-study
- U.S. DOE, *Supply Chain and Market Analysis*: https://www.energy.gov/oe/supply-chain-and-market-analysis

**Observed / 관측:** IEA projects strong electricity-demand growth through 2030 and identifies data centers as a major driver, particularly in the United States. DOE's 2026 draft transmission study identifies pressing transmission needs under new load growth; DOE also documents transformer supply-chain and specification challenges.  
**관측:** IEA는 2030년까지 강한 전력수요 증가와 미국에서 데이터센터의 큰 기여를 전망하며, DOE 2026 초안은 신규 부하 성장에 따른 송전 확충 필요와 변압기 공급망·사양 문제를 명시한다.

### Manufacturing, AM, semiconductor / 제조·AM·반도체
- NIST, *2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing*: https://www.nist.gov/publications/2026-roadmap-artificial-intelligence-and-machine-learning-smart-manufacturing
- NIST, *Advanced Manufacturing Data Infrastructure and Analytics Program*: https://www.nist.gov/programs-projects/advanced-manufacturing-data-infrastructure-and-analytics-program-0
- NIST, *Advanced Machines, Monitoring, and Control for Additive Manufacturing*: https://www.nist.gov/programs-projects/advanced-machines-monitoring-and-control-additive-manufacturing
- NIST, *CHIPS Metrology Program*: https://www.nist.gov/chips/research-development-programs/metrology-program

**Observed / 관측:** NIST's 2026 smart-manufacturing roadmap highlights industrial data complexity, heterogeneous sensing/control integration, trustworthy AI, digital twins, robotics, and advanced manufacturing as active challenges. NIST AM programs continue to identify inconsistent quality, production efficiency, qualification and data interoperability as barriers. Semiconductor metrology work highlights thermal/mechanical and advanced-packaging measurement challenges.  
**관측:** NIST의 2026 스마트제조 로드맵과 관련 프로그램은 산업 데이터 복잡성, 이질 센서·제어 통합, 신뢰가능 AI, AM 품질·효율·인증·상호운용성 및 첨단 패키징 계측 문제를 지속적 과제로 제시한다.

### Critical minerals / 핵심광물
- USGS, *Mineral Commodity Summaries 2026*: https://pubs.usgs.gov/publication/mcs2026
- USGS Data Release: https://data.usgs.gov/datacatalog/data/USGS%3A69837e43b66b01367d7ec7c7

**Observed / 관측:** The 2026 USGS release provides production, reserves/resources, trade-related and import-reliance information across more than 90 minerals/materials and an explicit critical-minerals list, creating a strong cross-dataset backbone.  
**관측:** USGS 2026 자료는 90개 이상의 광물·소재에 대해 생산·매장량·무역·수입의존 관련 데이터를 제공해 산업수요·무역·가격·재활용 데이터와 결합하기 좋은 backbone을 제공한다.

### Logistics / 물류
- World Bank, *Container Port Performance Index 2025*: https://www.worldbank.org/en/topic/transport/publication/cppi
- World Bank, *Logistics Performance Indicators 2.0*: https://lpi.worldbank.org/en/home

**Observed / 관측:** CPPI provides observed port-time performance, while LPI 2.0 moves toward shipment-level operational evidence and identifies persistent unpredictability at ports, transshipment hubs and inland checkpoints.  
**관측:** CPPI는 실제 항만 체류시간 기반 지표를 제공하고, LPI 2.0은 shipment-level 운영데이터를 활용하며 항만·환적·내륙 검문 지점의 지속적 불확실성을 포착한다.

### Water and buildings / 물·건물
- World Bank, water utility leakage/creditworthiness (2026): https://blogs.worldbank.org/en/water/water-utility-creditworthiness--reduce-leaks--secure-future
- World Bank, global freshwater losses (2025): https://www.worldbank.org/en/news/press-release/2025/11/04/world-annual-fresh-water-losses-could-supply-280-million-people
- IEA, *Energy Efficiency 2025 — Buildings*: https://www.iea.org/reports/energy-efficiency-2025/buildings
- IEA, *Breakthrough Agenda Report 2025 — Building*: https://www.iea.org/reports/breakthrough-agenda-report-2025/building

**Observed / 관측:** non-revenue water remains a major operational and financial issue for water utilities; legacy building stock and slow/deep retrofit economics remain important efficiency constraints.  
**관측:** 상수도 비수익수는 운영·재정의 지속적 병목이며, 기존 건축물 stock과 심층 리트로핏의 속도·경제성도 에너지 효율의 핵심 제약으로 남아 있다.

### Antimicrobial resistance / 항생제 내성
- WHO, *Global antibiotic resistance surveillance report 2025*: https://www.who.int/publications/i/item/9789240116337
- WHO GLASS: https://www.who.int/initiatives/glass

**Observed / 관측:** WHO GLASS provides standardized multi-country resistance surveillance and is designed to incorporate epidemiological, clinical, antimicrobial-use, food-chain and environmental dimensions, making it intrinsically suitable for relationship discovery.  
**관측:** WHO GLASS는 다국가 표준화 내성 감시를 제공하며 역학·임상·항생제 사용·식품사슬·환경 데이터까지 확장하도록 설계되어 데이터 관계 탐색에 적합하다.

## 6. Engine Priority Set v0.1 / 엔진 우선 소재군 v0.1

`P0` 소재는 향후 Wave 1 dataset discovery에서 우선 검색한다. / `P0` topics guide Wave 1 dataset discovery.

1. **Grid bottleneck intelligence / 전력망 병목 지능화** — transmission + transformers + new load + weather + prices.
2. **AI infrastructure siting & resource stress / AI 인프라 입지·자원 스트레스** — data centers + grid + water + climate + land.
3. **Advanced manufacturing quality intelligence / 첨단제조 품질 지능화** — AM/smart manufacturing + sensors + metrology + outcomes.
4. **Supply-chain weakest-link intelligence / 공급망 최약고리 지능화** — ports + shipment-level logistics + weather + trade.
5. **Critical-mineral resilience & recovery / 핵심광물 회복력·회수** — production + trade + prices + technology demand + recycling.
6. **Climate–infrastructure failure risk / 기후–인프라 고장위험** — hazards + grid/water/transport assets + outages/losses.

## 7. Strategic Interpretation / 전략적 해석

**한국어**  
`AMBENCH-001`은 여전히 가장 적절한 Wave 0 calibration case다. 다만 엔진의 장기 가치를 제조업에 한정해서는 안 된다. 소재 탐색 결과, 가장 강한 공통 패턴은 **수요 또는 외부충격 → 물리·운영 시스템 상태 → 측정 가능한 병목/결과 → 의사결정 또는 최적화** 구조다. 이는 AM Bench의 `process → measurement → outcome` 패턴을 전력망·물류·물·건물·공중보건까지 일반화할 수 있음을 시사한다.

**English**  
`AMBENCH-001` remains the most appropriate Wave 0 calibration case, but the engine should not be confined to manufacturing. The strongest cross-domain pattern is **demand or external shock → physical/operational system state → measurable bottleneck/outcome → decision or optimization**. This suggests that the AM Bench `process → measurement → outcome` pattern can be generalized to grids, logistics, water, buildings, and public health.

## 8. Next Gate / 다음 게이트

소재 탐색은 완료된 선별 baseline이며, 다음 공식 작업은 `AMBENCH-001` calibration이다. 이후 Issue #2–#4의 Wave 1 dataset discovery에서 `P0` 소재를 우선 사용하고, 실제 데이터셋 확인 후에만 IPS를 부여한다.  
This landscape is a completed screening baseline. The next official task is `AMBENCH-001` calibration. Issues #2–#4 should prioritize `P0` topics, and IPS is assigned only after real dataset inspection.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
