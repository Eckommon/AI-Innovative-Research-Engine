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
- geography: EEA-33
- special note: EEA reports one corrected UK point for 2009

The crosswalk is frozen before calculation. / 계산 전 crosswalk를 고정한다.

## 3. Primary Reference Verification / 1차 기준 검증

### `OBSERVED`, `V2_PRIMARY_VERIFIED` — EEA reference / EEA 기준

The EEA 2019 briefing states that mercury emissions per unit of steel produced in the EEA-33 were **36% lower in 2017 than in 2008**. Figure 1 identifies E-PRTR as the numerator source and Eurostat `DS-066342` as the total-production denominator source, and specifies the exact activity/product codes above. The figure uses mercury grams per kilotonne of steel production.  
EEA 2019 briefing은 EEA-33의 철강 생산단위당 수은 배출량이 **2017년에 2008년 대비 36% 낮았다**고 명시한다. Figure 1은 분자를 E-PRTR, 분모를 Eurostat `DS-066342` total production으로 밝히고 위 activity/product code를 명시하며 단위는 철강 생산 kilotonne당 수은 gram이다.

### EEA-33 geography resolved / EEA-33 지리범위 해결

The same EEA briefing describes E-PRTR coverage as the EU-28 Member States + Iceland + Liechtenstein + Norway + Switzerland + Serbia = 33 countries. Figure 1 explicitly notes that Turkey has no E-PRTR data and Serbia is included.  
동일 EEA briefing은 E-PRTR 범위를 EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia의 33개국으로 설명한다. Figure 1은 Turkey 자료가 없고 Serbia가 포함됨을 명시한다.

**Resolved / 해결:** EEA-33 membership is no longer an `UNKNOWN`. / EEA-33 구성 자체는 더 이상 미확인이 아니다.

## 4. Raw Access Discovery / Raw 접근 발견

### E-PRTR numerator / E-PRTR 분자
`OBSERVED`, `V2_PRIMARY_VERIFIED`

EEA historical user-friendly data package `eea_t_ied-eprtr_p_2007-2022_v11_r00` lists:
- `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` (~13 MB)
- `F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv` (~101 MB)

This establishes a raw numerator path at Annex I activity granularity. / Annex I activity 해상도의 raw 분자 경로 존재를 확인했다.

Official index / 공식 인덱스:  
`https://sdi.eea.europa.eu/webdav/datastore/public/eea_t_ied-eprtr_p_2007-2022_v11_r00/User%20friendly%20.csv%20file/`

**Access status / 접근상태:** the WebDAV index and file name are verified, but the current execution environment has not yet successfully transported/read the CSV bytes. This is an access-path limitation, not evidence of data absence. / 현재 실행환경에서는 CSV byte 직접 transport/read가 아직 성공하지 않았으며 이는 데이터 부재가 아니라 접근경로 제한이다.

### Historical PRODCOM denominator / 과거 PRODCOM 분모
`OBSERVED`, `V2_PRIMARY_VERIFIED`

EEA Figure 1 cites `DS-066342 — Total production by PRODCOM list (NACE Rev. 2) - annual data`. Eurostat's official historical EUROPROMS bulk inventory still lists:
- `EUROPROMS/epanntotal-r2.zip` (~1.10 MB)
- `EUROPROMS/epanntotal.zip` (~1.12 MB)

Eurostat's current Files API documentation states that files under `/comext` are retrieved by the base `https://ec.europa.eu/eurostat/api/dissemination/files?file=<relative-path>`. Therefore the inventory establishes an official legacy bulk route for annual total production.  
EEA Figure 1은 과거 `DS-066342`를 인용하며, Eurostat 공식 historical EUROPROMS inventory에는 `epanntotal-r2.zip`과 `epanntotal.zip`이 남아 있다. 현행 Files API 문서는 `/comext` 파일을 relative path로 가져오는 규칙을 명시한다.

**Verification boundary / 검증 경계:** the official file listing and URL-construction rule are verified; direct ZIP-byte retrieval in the current environment is **not yet reproduced**. / 공식 파일 존재·URL 규칙은 검증됐지만 현 실행환경에서 ZIP byte 직접 확보는 아직 재현되지 않았다.

### Current PRODCOM total-production access / 현행 PRODCOM total-production 접근
`OBSERVED`, `V2_PRIMARY_VERIFIED`

Eurostat's November 2025 Quick Guide identifies **`DS-059359`** as the current annual total-production dataset. It states:
- total production = sold production + production retained for further processing;
- data available from 1995 onward;
- annual frequency `A`;
- reporter dimension includes Member States, EFTA and candidate/acceding countries, with EU15/EU28/EU27_2020 aggregates where available;
- `APRODQNT` = Actual production quantity;
- `QNTUNIT` = Quantity unit;
- `APQNTFLAG` and `APQNTBASE` describe availability/rounding.

Eurostat의 2025 Quick Guide는 **`DS-059359`**를 현행 annual total-production dataset으로 설명하고, `APRODQNT`를 실제 생산수량, `QNTUNIT`를 그 수량의 단위로 정의한다.

**Important / 중요:** current `DS-059359` and historical EEA-cited `DS-066342` perform the same broad statistical role of annual total production, but a one-to-one historical migration equivalence is **not assumed without explicit correspondence**. / 현행 `DS-059359`와 과거 `DS-066342`가 annual total production이라는 같은 통계 역할을 하지만, 명시 correspondence 없이 1:1 migration 동등성을 가정하지 않는다.

## 5. Predefined Calculation / 사전 계산식

```text
Hg_t = sum(E-PRTR mercury-to-air releases for activities 1.(d), 2.(a), 2.(b))
Steel_t = sum(PRODCOM total-production quantities for 2410T121-122, 2410T131-132, 2410T141-142)
Intensity_t = Hg_t / Steel_t
Change_2008_2017 = (Intensity_2017 / Intensity_2008 - 1) * 100
```

Units must be harmonized before division. / 나눗셈 전 단위를 일치시킨다.

## 6. Frozen Gate / 고정 게이트

- `PASS`: `Change_2008_2017` within `-38%` to `-34%` and inputs/crosswalk reproducible.
- `PARTIAL`: numerator/denominator reproducible but documented legacy/version differences prevent ±2%p agreement.
- `FAIL/HOLD`: unsupported assumptions are required to recover numerator, denominator, geography, units, or legacy code semantics.

No post-hoc filter change solely to force agreement with `-36%`. / `-36%`에 맞추기 위한 사후 filter 변경 금지.

## 7. Resolved vs Unknown / 해결·미확인

### Resolved / 해결
- EEA target ratio, `-36%`, exact E-PRTR/PRODCOM crosswalk, period and chart unit. / EEA 기준 관계·코드·기간·단위.
- EEA-33 country membership. / EEA-33 구성.
- historical denominator dataset identity `DS-066342`. / 과거 분모 dataset 정체.
- official historical EUROPROMS annual-total-production archive exists (`epanntotal-r2.zip`). / legacy annual-total-production archive 존재.
- current annual total-production dataset `DS-059359` and fields `APRODQNT`, `QNTUNIT`. / 현행 dataset·필드 의미.
- `QNTUNIT` semantics = field specifying the physical quantity unit. / `QNTUNIT` 의미.

### `UNKNOWN`
1. exact directly executable E-PRTR `F1_3` CSV transport/schema in the current execution environment / 현 실행환경의 E-PRTR `F1_3` 직접 transport·schema;
2. direct extraction of the historical `epanntotal-r2.zip` contents and its exact legacy row schema / historical ZIP 내부 schema·row 직접 추출;
3. actual `QNTUNIT` value returned for the six target crude-steel product rows in 2008 and 2017 / 목표 6개 철강 row의 실제 수량 단위값;
4. exact raw reporter/aggregate construction used by EEA to form the denominator across EEA-33, despite the country membership itself now being resolved / EEA-33 구성은 해결됐으나 EEA가 실제 분모에서 사용한 reporter/aggregate 계산 방식;
5. raw 2008 and 2017 Hg and steel-production values / 실제 2008·2017 분자·분모 값.

No modern-code substitution or synthetic country/facility allocation is permitted. / 현대 code 임의대체·국가/시설 임의배분 금지.

## 8. Next Actions / 다음 행동

1. Retrieve/read `F1_3` or an official equivalent and inspect column schema. / E-PRTR 분자 파일·schema 확보.
2. Retrieve/read historical `epanntotal-r2.zip`; prefer the historical denominator before considering current `DS-059359` as a compatibility check. / historical 분모 ZIP 우선 확보.
3. Freeze exact reporter/product/year/unit filters and raw-source snapshots. / reporter·product·year·unit filter와 snapshot 고정.
4. Extract 2008 and 2017 numerator and denominator independently. / 2008·2017 분자·분모 독립 추출.
5. Compute annual intensity and percent change without post-hoc tuning. / 사후조정 없이 집약도·변화율 계산.
6. Compare to EEA `-36%`; classify `PASS/PARTIAL/FAIL-HOLD` under the frozen gate. / 기준 판정.
7. Preserve raw provenance, file hashes, query filters and any legacy-version discrepancy. / provenance·hash·filter·version 차이 보존.

## 9. Primary Sources / 1차 출처

- EEA, *A decade of industrial pollution data* (2019), Figure 1 and E-PRTR coverage.
- EEA historical Industrial Reporting WebDAV user-friendly CSV index (`2007–2022 v11`).
- Eurostat, *Quick guide on accessing annual industrial production (PRODCOM) data — DS-059359* (Nov 2025).
- Eurostat, *Statistics on the production of manufactured goods (prom)* reference metadata.
- Eurostat, *API — Migrating from Bulk Download Listing URLs to API URLs* and EUROPROMS inventory.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and `FRESH-001`. / 공식 산출물은 관련 규약을 따른다.
