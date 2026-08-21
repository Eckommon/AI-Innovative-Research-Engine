---
id: EU-STEEL-R01
type: experiment
state: EXPERIMENT
evidence_class: HYPOTHESIZED
region: eu
domain: industry
tags:
  - type/experiment
  - state/experiment
  - evidence/hypothesized
  - region/eu
  - domain/industry
  - risk/classification
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/EU-IEE-F02/README.md
---

# EU-STEEL-R01 — E-PRTR × PRODCOM 철강 수은집약도 독립 재현 / Independent Reproduction of E-PRTR × PRODCOM Steel Mercury Intensity

**Issue / 이슈:** #8  
**State / 상태:** `EXPERIMENT — RAW_INPUT_RETRIEVAL`

## 1. Reproduction Target / 재현 대상

**KO:** EEA가 발표한 EEA-33의 `mercury emissions per unit of steel production`이 2008 대비 2017년 **36% 감소**했다는 관계를 공식 raw E-PRTR + Eurostat PRODCOM 입력에서 독립 계산한다.  
**EN:** Independently calculate from official raw E-PRTR + Eurostat PRODCOM inputs the EEA-published relationship that EEA-33 `mercury emissions per unit of steel production` was **36% lower in 2017 than in 2008**.

## 2. Frozen Published Crosswalk / 고정 공식 Crosswalk

- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM products: `2410T121-122`, `2410T131-132`, `2410T141-142`
- years: `2008–2017`
- geography: EEA-33; Turkey absent from E-PRTR, Serbia included
- special note: EEA reports one corrected UK point for 2009

The crosswalk is frozen before calculation. / 계산 전 crosswalk를 고정한다.

## 3. Raw Access Discovery / Raw 접근 발견

### E-PRTR numerator / E-PRTR 분자
`OBSERVED`, `V2_PRIMARY_VERIFIED`

EEA historical user-friendly data package `eea_t_ied-eprtr_p_2007-2022_v11_r00` lists:
- `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` (~13 MB)
- `F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv` (~101 MB)

This establishes a raw numerator path at Annex I activity granularity. / Annex I activity 해상도의 raw 분자 경로 확인.

Index / 인덱스: `https://sdi.eea.europa.eu/webdav/datastore/public/eea_t_ied-eprtr_p_2007-2022_v11_r00/User%20friendly%20.csv%20file/`

Current EEA Industrial Reporting also exposes downloadable 2007–2024 tabular data. / 현행 EEA Industrial Reporting도 2007–2024 tabular download 제공.

### PRODCOM denominator / PRODCOM 분모
`OBSERVED`, `V2_PRIMARY_VERIFIED`

- Eurostat/data.europa.eu identify **`DS-066342` as Total production**. / Eurostat/data.europa.eu에서 `DS-066342 = Total production` 확인.
- Eurostat PRODCOM manuals describe `DS-066342` as annual total production broken down by PRODCOM List. / PRODCOM List별 연간 total production dataset임을 확인.
- DS-prefixed PRODCOM datasets use `https://ec.europa.eu/eurostat/api/comext/dissemination` and filtered API requests. / 전용 Comext API 사용.
- The published steel `T` codes retain explicit crude-steel semantics in current statistical code lists: non-alloy/alloy/stainless steel split by electric-furnace vs other process. / 발표된 T-code는 현재 통계 code list에서도 조강 종류·공정별 의미가 확인됨.

### Reference semantics / 기준 의미
EEA's published figure states that the ratio uses the above E-PRTR activity codes and PRODCOM product codes and reports 2017 intensity 36% below 2008. The chart unit is mercury grams per kilotonne of steel production. / EEA 공식 figure는 해당 code 조합과 2017년 -36%를 명시하며 chart 단위는 철강생산 kilotonne당 수은 grammes다.

## 4. Predefined Calculation / 사전 계산식

```text
Hg_t = sum(E-PRTR mercury-to-air releases for activities 1.(d), 2.(a), 2.(b))
Steel_t = sum(PRODCOM total-production quantities for 2410T121-122, 2410T131-132, 2410T141-142)
Intensity_t = Hg_t / Steel_t
Change_2008_2017 = (Intensity_2017 / Intensity_2008 - 1) * 100
```

Units must be harmonized before division. / 나눗셈 전 단위를 일치시킨다.

## 5. Frozen Gate / 고정 게이트

- `PASS`: `Change_2008_2017` within `-38%` to `-34%` and inputs/crosswalk reproducible.
- `PARTIAL`: numerator/denominator reproducible but documented legacy/version differences prevent ±2%p agreement.
- `FAIL/HOLD`: unsupported assumptions are required to recover numerator, denominator, geography, units, or legacy code semantics.

No post-hoc filter change solely to force agreement with `-36%`. / `-36%`에 맞추기 위한 사후 filter 변경 금지.

## 6. Resolved vs Unknown / 해결·미확인

### Resolved / 해결
- `DS-066342` identity = annual total production by PRODCOM List. / dataset 정체 확인.
- exact published steel T-code descriptions remain interpretable. / T-code 의미 확인.
- EEA target ratio/crosswalk/reference change fixed. / 기준 ratio·crosswalk·변화율 고정.

### `UNKNOWN`
- exact directly executable E-PRTR CSV transport in the current execution environment / 현재 실행환경의 E-PRTR CSV 직접 transport;
- exact Eurostat API dimension/filter syntax needed to retrieve 2008 and 2017 `DS-066342` rows for the legacy T codes / 2008·2017 legacy T-code raw row를 가져올 API dimension/filter;
- raw `QNTUNIT`/production quantity unit returned for those rows and any EU/EEA aggregate construction required / raw 수량단위와 EEA-33 aggregation 구성.

No modern-code substitution is made. / 현대 code 임의대체 금지.

## 7. Next Actions / 다음 행동

1. Resolve E-PRTR Annex I CSV access and inspect schema. / E-PRTR CSV 접근·schema 확인.
2. Resolve filtered `DS-066342` query structure and `QNTUNIT` for 2008/2017. / DS-066342 filter·단위 확인.
3. Extract 2008/2017 numerator and denominator independently. / 분자·분모 독립 추출.
4. Compute annual intensity and percent change. / 집약도·변화율 계산.
5. Compare to EEA `-36%` without post-hoc tuning. / 사후조정 없이 비교.
6. Preserve query/snapshot provenance and hashes where possible. / provenance·hash 보존.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, and `UNKNOWN-001`. / 공식 산출물은 관련 규약을 따른다.
