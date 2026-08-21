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
**Reproduction harness / 재현 하네스:** `src/reproduce_eu_steel_mercury.py`  
**GitHub Actions / 자동 재현:** `.github/workflows/eu-steel-r01-reproduce.yml`, `.github/workflows/eu-steel-r01-issue-trigger.yml`

## 1. Reproduction Target / 재현 대상

**KO:** EEA가 발표한 EEA-33의 `mercury emissions per unit of steel production`이 2008 대비 2017년 **36% 감소**했다는 관계를 공식 raw E-PRTR + Eurostat PRODCOM 입력에서 독립 계산한다.  
**EN:** Independently calculate from official raw E-PRTR + Eurostat PRODCOM inputs the EEA-published relationship that EEA-33 `mercury emissions per unit of steel production` was **36% lower in 2017 than in 2008**.

## 2. Frozen Published Crosswalk / 고정 공식 Crosswalk

- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM products: `2410T121-122`, `2410T131-132`, `2410T141-142`
- years: `2008–2017`
- geography: EEA-33 = EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia; Turkey absent from E-PRTR
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

Current EEA Industrial Reporting also exposes downloadable 2007–2024 tabular data and standardizes pollutant-release quantities in `kg/year`. / 현행 EEA Industrial Reporting도 2007–2024 tabular 다운로드를 제공하고 pollutant release 단위를 `kg/year`로 표준화한다.

### PRODCOM denominator / PRODCOM 분모
`OBSERVED`, `V2_PRIMARY_VERIFIED`

- Eurostat/data.europa.eu identify **`DS-066342` as Total production**. / `DS-066342 = Total production` 확인.
- Official EUROPROMS bulk inventory lists `epanntotal-r2.zip` and `epanntotal.zip`. / 공식 historical bulk archive 확인.
- Current Eurostat Quick Guide identifies **`DS-059359`** as annual total production from 1995 onward. / 현행 annual total-production dataset 확인.
- Current field semantics: `APRODQNT` = Actual production quantity; `QNTUNIT` = Quantity unit. / 현행 필드 의미 확인.
- The published steel `T` codes retain explicit crude-steel semantics in statistical code lists. / 발표된 T-code의 조강 종류·공정 의미 확인.

**Compatibility caution / 호환 주의:** `DS-059359` is a current compatibility reference and is **not assumed to be a one-to-one migration** of historical `DS-066342` without authoritative correspondence. / 현행 dataset을 historical dataset과 임의 동일시하지 않는다.

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

## 6. Reproducibility Harness / 재현 하네스

`src/reproduce_eu_steel_mercury.py` enforces: / 다음을 코드 수준에서 강제한다.
- fixed years, activity codes, product codes, and EEA-33 scope / 고정 연도·활동·제품·지역범위;
- SHA-256 fingerprints before analysis / 분석 전 SHA-256;
- schema and delimiter inspection / schema·delimiter 검사;
- fail-closed behavior for ambiguous columns/units/reporters / 열·단위·reporter가 모호하면 추정하지 않고 실패;
- separate numerator/denominator calculation before intensity / 집약도 전 분자·분모 분리계산;
- frozen `-38%..-34%` reproduction gate / 고정 재현 게이트.

GitHub Actions runners are used as the network-capable reproducibility environment because the current chat execution container cannot resolve the official EEA/Eurostat hosts. / 현재 채팅 실행 컨테이너의 외부 DNS 제한을 피하기 위해 GitHub-hosted runner를 공식 raw 재현환경으로 사용한다.

## 7. Resolved vs Unknown / 해결·미확인

### Resolved / 해결
- EEA target ratio/crosswalk/reference change / 기준 ratio·crosswalk·변화율;
- EEA-33 membership / EEA-33 구성;
- E-PRTR historical raw filename and official directory / historical raw 파일명·공식 경로;
- E-PRTR pollutant-release unit semantics = `kg/year` / 배출 단위 의미;
- historical `DS-066342` and EUROPROMS annual-total-production archive identity / historical 분모 source;
- current `DS-059359`, `APRODQNT`, `QNTUNIT` semantics / 현행 호환 참조 의미.

### `UNKNOWN` pending GitHub Actions raw inspection / Actions raw 검사 대기
- exact E-PRTR CSV column schema and target 2008/2017 Hg rows / E-PRTR 실제 열·목표 행;
- `epanntotal-r2.zip` internal member/schema and six target-code rows / historical ZIP 내부 schema·목표 행;
- actual target-row quantity unit and defensible EEA-33 denominator aggregation / 실제 수량단위·분모 집계;
- independent 2008/2017 numerator, denominator, intensity and percent change / 독립 계산값.

These remain unknown until machine-generated raw inspection or an equivalent V3 extraction is reviewed. / 기계 raw 검사 또는 동등한 V3 추출 전까지 미확인으로 유지한다.

## 8. Next Actions / 다음 행동

1. Trigger GitHub Actions raw inspection through Issue #8 edit. / Issue #8 edit로 Actions 검사 실행.
2. Review `research/EU-STEEL-R01/action_inspection.md` if generated. / 생성된 raw 검사파일 검토.
3. Adapt parser only to observed official schema, without changing the frozen crosswalk. / 관측 schema에만 parser 보정.
4. Execute full numerator/denominator calculation and preserve result JSON. / 분자·분모 계산 및 JSON 보존.
5. Compare to EEA `-36%` under the frozen gate. / 고정 게이트 비교.
6. Update Claim Ledger, Decision Log if needed, Memory, Handoff, STATUS, MOCs, and Issue #8. / 기록 동기화.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and `WRITEBACK-001`. / 공식 산출물은 관련 규약을 따른다.
