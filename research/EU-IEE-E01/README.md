# EU-IEE-E01 — 산업 배출–경제활동 Decoupling 통제실험 / Industrial Emissions–Economic Activity Decoupling Controlled Experiment

**State / 상태:** `EXPERIMENT_COMPLETE`  
**Date / 기준일:** 2026-08-22  
**Parent candidate / 상위 후보:** `C-EU-002`  
**Experiment class / 실험 유형:** cross-dataset validation / 데이터셋 간 검증

## 1. Purpose / 목적

**한국어**  
Wave 1 이후 첫 cross-dataset controlled experiment로서 EEA 산업대기배출과 Eurostat 산업 GVA를 결합한 EU-27 공식 지표를 사용하여, 산업 경제활동이 증가하는 동안 주요 산업 대기오염물질이 실질적으로 감소했다는 `decoupling` 주장을 사전 기준으로 검증한다. 이 실험의 목적은 신규성을 강제하는 것이 아니라 엔진의 `source → relationship → falsifiable criterion → result` 경로를 재현 가능한 방식으로 검증하는 것이다.

**English**  
As the first post-Wave-1 cross-dataset controlled experiment, use the official EU-27 relationship between EEA industrial air-emission reporting and Eurostat industrial GVA to test, against a predefined criterion, whether major industrial air pollutants materially declined while industrial economic activity increased. The purpose is to validate the engine's `source → relationship → falsifiable criterion → result` path without forcing novelty.

## 2. Source Datasets / 원천 데이터셋

1. **EEA Industrial Reporting / INDP003** — pollutant releases from large industrial operators; indicator period 2010–2024. / 대규모 산업시설의 대기오염물질 배출; 지표 기간 2010–2024.
2. **Eurostat Gross value added and income by main industry** — industrial GVA in chain-linked volumes, used by EEA as economic-activity proxy. / 산업 GVA chain-linked volume; EEA가 산업경제활동 proxy로 사용.

### Official source references / 공식 출처
- https://www.eea.europa.eu/en/analysis/indicators/industrial-pollutant-releases-to-air
- https://www.eea.europa.eu/en/analysis/indicators/industrial-pollutant-releases-to-air/industrial-releases-of-pollutants
- EEA industrial reporting v16.0 metadata DOI family: `10.2909/657ac3cb-affa-4295-a4a9-27b4f539adab`

## 3. Evidence Before Experiment / 실험 전 관측근거

`OBSERVED`

EEA's 2026 indicator states that between 2010 and 2024 in the EU, releases of heavy metals (Cd/Hg/Pb), SOx and PM10 declined by more than 75%, NOx by almost 60%, NMVOC by 41%, and CO2 by 38%. During the same period industrial GVA increased. / EEA 2026 지표에 따르면 EU에서 2010–2024년 중 중금속(Cd/Hg/Pb), SOx, PM10 배출은 75% 이상, NOx는 약 60%, NMVOC는 41%, CO2는 38% 감소했고 같은 기간 산업 GVA는 증가했다.

## 4. Hypothesis / 가설

### `H-EU-IEE-001`

**한국어**  
2010년 대비 2024년 EU-27 산업 GVA가 증가한 상태에서, 추적하는 6개 주요 pollutant family 중 최소 5개가 20% 이상 감소하면 산업 경제활동과 주요 산업대기배출 사이에 `material decoupling`이 존재한다고 판정한다.

**English**  
Relative to 2010, classify EU-27 industry as showing `material decoupling` by 2024 if industrial GVA increased while at least five of six tracked major pollutant families declined by at least 20%.

**Evidence class before test / 검증 전 증거등급:** `HYPOTHESIZED`

## 5. Predefined Design / 사전 실험설계

- **Baseline / 기준선:** no material decoupling — fewer than 5/6 pollutant families decline ≥20%, or industrial GVA does not increase. / 6개 중 5개 미만만 20% 이상 감소하거나 GVA가 증가하지 않음.
- **Target / 결과:** binary decoupling gate / 이진 decoupling 게이트.
- **Primary metric / 주요지표:** number of pollutant families with ≥20% decline while GVA > 2010 level. / GVA가 2010보다 높은 상태에서 20% 이상 감소한 pollutant family 수.
- **Pass threshold / 통과기준:** `>=5/6` pollutant families and GVA increase. / `5/6 이상` + GVA 증가.
- **Rejection criterion / 기각기준:** `<5/6` or non-increasing GVA. / `5/6 미만` 또는 GVA 비증가.
- **Leakage note / 누수주의:** threshold is defined from the research question and should not be redefined after seeing detailed values. / 상세값 확인 후 threshold를 변경하지 않는다.

## 6. Results / 결과

| Pollutant family / 오염물질군 | EEA-reported change 2010→2024 | ≥20% decline? |
|---|---:|---|
| Heavy metals (Cd/Hg/Pb) / 중금속 | >75% decline / 75% 이상 감소 | PASS |
| SOx | >75% decline / 75% 이상 감소 | PASS |
| PM10 | >75% decline / 75% 이상 감소 | PASS |
| NOx | ~60% decline / 약 60% 감소 | PASS |
| NMVOC | 41% decline / 41% 감소 | PASS |
| CO2 | 38% decline / 38% 감소 | PASS |

**Industrial GVA / 산업 GVA:** increased over the same period / 같은 기간 증가.

### Primary result / 주요 결과

`6/6 PASS` + `GVA increased`

## 7. Decision / 판단

### Empirical state / 실증 상태: `VALIDATED`

**한국어**  
사전 기준 `>=5/6 + GVA 증가`에 대해 실제 결과는 `6/6 + GVA 증가`이므로 EU-27 집계수준의 산업 배출–경제활동 material decoupling 가설은 통과한다.

**English**  
The predefined gate required `>=5/6 + GVA increase`; the observed result is `6/6 + GVA increase`. The aggregate EU-27 industrial emissions–economic activity material-decoupling hypothesis therefore passes.

### Novelty state / 신규성 상태: `LOW / NOT NOVEL`

**한국어**  
이 실험은 EEA가 이미 공식적으로 제시하는 decoupling 관계를 독립 연구 신규성으로 주장하지 않는다. 이번 가치의 핵심은 **cross-dataset controlled-experiment 절차의 엔진 보정**이다.

**English**  
This experiment does not claim independent novelty for a decoupling relationship already reported by the EEA. Its value is **calibration of the engine's cross-dataset controlled-experiment procedure**.

## 8. Limitations / 한계

- Aggregate EU-27 results can hide country/sector/facility heterogeneity. / EU-27 집계는 국가·sector·facility 이질성을 가릴 수 있음.
- E-PRTR/industrial reporting focuses on large operators and reporting thresholds; it is not a census of all industry. / 대형 사업자·보고 threshold 중심이며 산업 전체 census가 아님.
- EEA notes gap filling for several countries in 2023–2024 in the EU-level figure. / EEA는 EU-level figure에서 일부 국가의 2023–2024 gap filling을 명시함.
- This test validates decoupling, not its causal mechanism. / decoupling 현상을 검증하지만 인과 메커니즘을 검증하지 않음.

## 9. Next Research Gate / 다음 연구 게이트

Promote a more granular extension: `EU-IEE-F02` should test whether facility/sector-level emission performance can be normalized against harmonized industry output without violating reporting-threshold, coding, and temporal-alignment constraints. / `EU-IEE-F02`에서 시설·sector 배출성과를 조화된 산업생산과 정규화할 수 있는지 보고 threshold·coding·시간정렬 제약을 검증한다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
