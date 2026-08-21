---
id: EU-IEE-F02
type: feasibility
state: HOLD
evidence_class: derived
region: eu
domain: industry
tags:
  - type/experiment
  - state/hold
  - evidence/derived
  - region/eu
  - domain/industry
  - risk/classification
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/EU-IEE-E01/README.md
---

# EU-IEE-F02 — 시설·Sector 배출–산업생산 정규화 가능성 / Facility–Sector Emissions-to-Output Normalization Feasibility

**Issue / 이슈:** #7  
**Overall decision / 종합 판단:** `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`

## 1. Question / 질문

**한국어**  
EEA 산업시설 배출과 Eurostat 산업생산을 결합해 `emissions / production` 지표를 만들 때, 어느 수준까지 의미적·통계적으로 방어 가능한가?

**English**  
At what granularity can EEA industrial emissions and Eurostat industrial production be defensibly combined into an `emissions / production` indicator?

## 2. Observed Evidence / 관측 근거

### `OBSERVED-1` — E-PRTR includes economic-activity semantics / E-PRTR 경제활동 의미
Historical official E-PRTR dataset structure includes `NACEMainEconomicActivityCode` and `NACEMainEconomicActivityName`, in addition to NUTS fields. / 과거 공식 E-PRTR 데이터 구조에는 NUTS와 함께 `NACEMainEconomicActivityCode`, `NACEMainEconomicActivityName`이 존재한다.

Source / 출처: https://www.eea.europa.eu/data-and-maps/data/member-states-reporting-art-7-under-the-european-pollutant-release-and-transfer-register-e-prtr-regulation-3/e-prtr-dataset-structure/eprtr_database_structure.pdf/file

### `OBSERVED-2` — Current portal uses E-PRTR activity/sector / 현행 포털 activity·sector
The current Industrial Emissions Portal exposes E-PRTR Annex I activity and sector groupings and notes that releases are reported when pollutant-specific thresholds are exceeded. / 현행 포털은 E-PRTR Annex I activity·sector를 제공하며 pollutant별 threshold 초과 시 배출을 보고한다.

Source / 출처: https://industry.eea.europa.eu/industrial-emissions/dashboards/summary-releases

### `OBSERVED-3` — PRODCOM output denominator / PRODCOM 생산 분모
Eurostat PRODCOM provides annual production value/quantity by reporting country and product code, with industrial coverage linked to NACE. / Eurostat PRODCOM은 국가·제품코드별 연간 생산가치·수량을 제공하며 NACE 산업분류와 연결된다.

Sources / 출처:
- https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Industrial_production_statistics
- Eurostat annual PRODCOM dataset documentation `DS-056120`.

### `OBSERVED-4` — EEA published cross-dataset precedent / EEA 공식 결합 선례
EEA published a steel example combining E-PRTR mercury emissions with Eurostat PRODCOM steel production. The figure uses E-PRTR activity codes `1.(d), 2.(a), 2.(b)` and PRODCOM codes `2410T121-122`, `2410T131-132`, `2410T141-142`. EEA reports mercury emissions per unit of steel produced were **36% lower in 2017 than in 2008**. / EEA는 E-PRTR 수은배출과 Eurostat PRODCOM 철강생산을 결합한 사례를 공식 발표했으며, 해당 생산단위당 수은배출은 2008 대비 2017년 **36% 감소**했다고 보고한다.

Sources / 출처:
- https://www.eea.europa.eu/en/analysis/maps-and-charts/mercury-emissions-per-unit-of-1
- https://www.eea.europa.eu/en/analysis/publications/a-decade-of-industrial-pollution-data/a-decade-of-industrial-pollution-data/@@download/file

## 3. Derived Feasibility / 파생 feasibility

### Sector/Product Aggregate / Sector·제품 집계
`PASS_SECTOR_AGGREGATE`

**한국어**  
EEA가 activity code와 PRODCOM product code를 명시적으로 결합한 공식 선례가 있으므로, 정의가 명확한 특정 sector/product에 대해 국가·지역 aggregate 수준 `emissions / production` 지표는 재현 가능한 연구대상으로 승격할 수 있다.

**English**  
Because EEA has an explicit official precedent mapping E-PRTR activity codes to PRODCOM steel product codes, selected well-defined sector/product combinations can be promoted to reproducible country/region aggregate `emissions / production` research.

### Generic Facility Level / 일반 시설수준
`HOLD_FACILITY_DENOMINATOR`

**한국어**  
시설별 배출은 존재하지만 일반적인 plant-level 생산량 denominator가 동일 해상도로 존재한다고 확인되지 않았다. 국가·sector 생산량을 시설별로 임의 배분하면 허위 정밀도(false precision)가 생기므로 시설단위 효율지표로 승격하지 않는다.

**English**  
Facility-level emissions exist, but a general plant-level production denominator at matching granularity has not been established. Arbitrarily allocating country/sector production to facilities would create false precision, so generic facility-level efficiency metrics are not promoted.

## 4. Classification Caveat / 분류 주의

Current portal E-PRTR activity semantics, historical NACE fields, and PRODCOM/NACE product semantics must be connected through an explicit documented mapping for each experiment. / 현행 E-PRTR activity, 과거 NACE field, PRODCOM/NACE 제품 의미는 각 실험에서 명시적 mapping으로 연결해야 한다.

For 2008–2024 statistics, NACE Rev.2 semantics apply; NACE Rev.2.1 becomes the newer framework from 2025 onward, so longitudinal work must control classification-version changes. / 2008–2024 통계에는 NACE Rev.2를 적용하며 2025 이후 NACE Rev.2.1 전환을 장기시계열에서 통제해야 한다.

## 5. Decision / 판단

**Feasibility result / 실행가능성 결과:** `PARTIAL_PASS`

- sector/product aggregate normalization: `PASS` / sector·제품 집계: 통과
- generic facility-level normalization: `HOLD` / 일반 시설단위: 보류

This is a granularity decision, not a contradiction. / 이는 해상도별 판정이며 모순이 아니다.

## 6. Next Work Queue / 다음 Work Queue

Create `EU-STEEL-R01` to independently reproduce the documented EEA steel-mercury relationship from raw/official E-PRTR and PRODCOM data, preserving the exact activity/product crosswalk and aggregation rules. / raw·공식 E-PRTR와 PRODCOM 자료로 EEA 철강-수은 관계를 독립 재현하는 `EU-STEEL-R01`을 생성한다.

Do not claim successful reproduction until the raw numerator and denominator extraction is actually reproduced. / 실제 raw 분자·분모 추출을 재현하기 전에는 재현 성공을 주장하지 않는다.

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
