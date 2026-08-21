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

### E-PRTR / E-PRTR
`OBSERVED`, `V2_PRIMARY_VERIFIED`

EEA historical user-friendly data package `eea_t_ied-eprtr_p_2007-2022_v11_r00` lists separate CSVs including:
- `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` (~13 MB)
- `F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv` (~101 MB)

This establishes a plausible raw numerator path at Annex I activity granularity without requiring facility-level allocation. / 시설 배분 없이 Annex I activity 해상도에서 raw 분자 추출 경로가 존재함을 확인.

Index / 인덱스: `https://sdi.eea.europa.eu/webdav/datastore/public/eea_t_ied-eprtr_p_2007-2022_v11_r00/User%20friendly%20.csv%20file/`

Current EEA Industrial Reporting also exposes downloadable 2007–2024 tabular data. / 현행 EEA Industrial Reporting도 2007–2024 tabular 다운로드를 제공한다.

### PRODCOM / PRODCOM
`OBSERVED`, `V2_PRIMARY_VERIFIED`

Eurostat documents that `DS-` prefixed PRODCOM/Comext datasets use the dedicated base endpoint:
`https://ec.europa.eu/eurostat/api/comext/dissemination`

Filtered API requests are required/appropriate for detailed data. / 상세자료는 filter된 API query를 사용한다.

## 4. Predefined Calculation / 사전 계산식

For each year `t` / 연도별:

```text
Hg_t = sum(E-PRTR mercury-to-air releases for activities 1.(d), 2.(a), 2.(b))
Steel_t = sum(PRODCOM production quantities for 2410T121-122, 2410T131-132, 2410T141-142)
Intensity_t = Hg_t / Steel_t
Change_2008_2017 = (Intensity_2017 / Intensity_2008 - 1) * 100
```

Units must be harmonized before division. / 나눗셈 전 단위를 반드시 일치시킨다.

## 5. Frozen Gate / 고정 게이트

- `PASS`: `Change_2008_2017` within `-38%` to `-34%` and inputs/crosswalk reproducible.
- `PARTIAL`: numerator/denominator reproducible but documented legacy/version differences prevent ±2%p agreement.
- `FAIL/HOLD`: unsupported assumptions are required to recover the numerator, denominator, geography, units, or legacy code semantics.

No post-hoc filter change is permitted solely to force agreement with `-36%`. / `-36%`에 맞추기 위한 사후 filter 변경 금지.

## 6. Current Unknowns / 현재 미확인

- `UNKNOWN`: exact downloadable URL/transport for the historical Annex I CSV through the current execution environment. / 현재 실행환경에서 historical Annex I CSV의 직접 download 경로.
- `UNKNOWN`: exact active/archived Eurostat dataset identifier and API dimensions corresponding to legacy `DS-066342` and the published `T` product codes. / legacy DS-066342·T code에 대응하는 현행/보관 dataset identifier·API dimension.
- `UNKNOWN`: production quantity unit returned by the relevant legacy extraction. / 해당 legacy 추출 생산수량 단위.

These remain unknown; no modern-code substitution is made. / 미확인 상태를 유지하며 현대 code로 임의 대체하지 않는다.

## 7. Next Actions / 다음 행동

1. Resolve E-PRTR Annex I CSV access and inspect schema. / E-PRTR CSV 접근·schema 확인.
2. Resolve legacy PRODCOM dataset/code access through Eurostat catalogue/API or authoritative correspondence. / legacy PRODCOM 접근 확인.
3. Extract 2008 and 2017 numerator/denominator independently. / 2008·2017 분자·분모 독립 추출.
4. Compute and compare to EEA reference. / 계산 후 EEA 기준 비교.
5. Preserve query/snapshot provenance and hashes where possible. / query·snapshot provenance·hash 보존.

Official artifacts comply with `LANG-001`, `READ-001`, and `FACT-001`. / 공식 산출물은 관련 규약을 따른다.
