---
id: EU-STEEL-R01
type: experiment
state: INCONCLUSIVE
evidence_class: DERIVED
region: eu
domain: industry
tags:
  - type/experiment
  - state/inconclusive
  - evidence/reproduced
  - region/eu
  - domain/industry
  - risk/version-drift
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/EU-IEE-F02/README.md
  - research/EU-STEEL-R01/REPRODUCTION_RESULT.md
---

# EU-STEEL-R01 — E-PRTR × PRODCOM 철강 수은집약도 독립 재현 / Independent Reproduction of E-PRTR × PRODCOM Steel Mercury Intensity

**Issue / 이슈:** #8  
**State / 상태:** `COMPLETED — HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`  
**Detailed result / 상세 결과:** [REPRODUCTION_RESULT.md](./REPRODUCTION_RESULT.md)  
**Reproduction harness / 재현 하네스:** `src/reproduce_eu_steel_mercury.py`

## 1. Reproduction Target / 재현 대상

**KO:** EEA가 2019 briefing에서 서술한 EEA-33 `mercury emissions per unit of steel production`의 2008→2017 **-36%** 관계를 공식 E-PRTR + Eurostat PRODCOM 입력에서 독립 재현한다.  
**EN:** Independently reproduce from official E-PRTR + Eurostat PRODCOM inputs the EEA 2019 briefing narrative that EEA-33 `mercury emissions per unit of steel production` was **36% lower in 2017 than in 2008**.

## 2. Frozen Published Crosswalk / 고정 공식 Crosswalk

- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM products: `2410T121`, `2410T122`, `2410T131`, `2410T132`, `2410T141`, `2410T142`
- years: `2008`, `2017`
- geography: EEA-33 = EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia
- Turkey absent from E-PRTR
- chart unit: grams Hg / kilotonne steel

The crosswalk and gate were frozen before calculation. No post-hoc tuning was permitted. / 계산 전 crosswalk·게이트를 고정했으며 사후 조정을 허용하지 않았다.

## 3. V3 Reproduced Numerator / V3 재현 분자

Official EEA historical files were machine-read in GitHub Actions. / 공식 EEA historical 파일을 GitHub Actions에서 기계 판독했다.

| Source | 2008 Hg | 2017 Hg | Result |
|---|---:|---:|---|
| `F1_3` activity aggregate | 4,312.9 kg | 3,327.1 kg | reproduced |
| `F1_4` facility detail | 4,312.9 kg | 3,327.1 kg | reproduced |

The exact equality of the two totals rules out aggregate-vs-facility resolution as the cause of the reproduction mismatch. / 두 합계가 정확히 일치하므로 aggregate/facility 해상도 차이는 불일치 원인이 아니다.

## 4. Primary-Source Version Conflict / 1차 출처 버전 불일치

The EEA briefing narrative states `-36%`. The **currently distributed EEA chart CSV** contains: / EEA briefing 본문은 `-36%`를 서술하지만 현행 배포 chart CSV는 다음 값을 포함한다.

- 2008: `35.0 g/kt`
- 2017: `20.5 g/kt`
- direct change: **`-41.4286%`**

Therefore the narrative percentage and current chart-data values are internally inconsistent. The cause is not inferred without evidence. / 따라서 본문 퍼센트와 현행 chart 데이터가 내부적으로 불일치하며 원인은 근거 없이 추정하지 않는다.

## 5. PRODCOM Denominator / PRODCOM 분모

### Historical / 과거
EEA cites `DS-066342` (`Total production by PRODCOM list`). The dataset is now discontinued. Direct probes of current official Eurostat interfaces returned `404` / `not available for dissemination` for: / EEA가 사용한 `DS-066342`는 현재 폐지됐고 현행 공식 인터페이스 직접 조회에서 다음 모두 404를 반환했다.

- COMEXT Statistics API, 2008/2017
- regular Statistics API
- SDMX dataflow

Official EUROPROMS legacy archives remain downloadable, but observed ranges are insufficient: / 공식 legacy archive는 다운로드 가능하지만 기간이 부족하다.

- `epanntotal-r2.zip`: through 2014
- `epanntotal.zip`: through 2012

Thus the exact legacy 2017 denominator used by the historical EEA analysis cannot presently be recovered through the tested official dissemination paths. / 원 EEA 분석의 정확한 legacy 2017 분모를 시험한 공식 배포경로에서 현재 복구할 수 없다.

### Current compatibility diagnostic / 현행 호환 진단
Current `DS-059359` was successfully queried with actual dimensions `freq / reporter / product / indicators / time`; the six literal T-codes exist and use `KG`. / 현행 `DS-059359`의 실제 구조와 T-code·KG 단위를 재현했다.

However, EEA-33 extra reporters contain `null` for `LI`, `CH`, and 2008 `XS` on the tested products. `null` was not converted to zero. / EEA-33 추가 reporter의 일부가 `null`이며 이를 0으로 변환하지 않았다.

For diagnosis only, the six-code EU28 sums were: / 진단 전용 EU28 합계:
- 2008: `168,619,860,319 kg`
- 2017: `129,543,917,700 kg`

Combining those EU28-only values with the reproduced numerator gives `+0.4126%`, **not** an EEA-33 reproduction result. / 해당 EU28-only 계산은 `+0.4126%`이나 EEA-33 재현값으로 승격하지 않는다.

## 6. Frozen Gate / 고정 게이트

Predefined gate: / 사전 게이트:
- `PASS`: independent change within `-38%..-34%` with reproducible matched inputs.
- `PARTIAL`: numerator and denominator reproducible, but documented legacy/version differences prevent exact agreement.
- `FAIL/HOLD`: unsupported assumptions are required to recover numerator, denominator, geography, units, or code semantics.

### Final / 최종

**`HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`**

`PASS` is not granted. `PARTIAL` is also not granted under the original definition because the exact historical 2017 denominator is not reproducibly extractable. / 정확한 historical 2017 분모가 재현 추출되지 않으므로 `PASS`뿐 아니라 원 정의상의 `PARTIAL`도 부여하지 않는다.

This is **not a falsification** of the historical EEA analysis. It is a reproducibility and data-lineage limitation. / 과거 EEA 분석의 반증이 아니라 재현성·데이터 계보 한계다.

## 7. Evidence Runs / 증거 Run

- GitHub Actions Run `32534535674` — frozen EEA-33 denominator attempt → `HOLD_UNRESOLVED_DENOMINATOR`
- Run `32534683910` — EEA figure CSV + `F1_3`/`F1_4` numerator diagnostic
- Run `32534864866` — discontinued `DS-066342` endpoint recovery probe

## 8. Research Lesson / 연구 교훈

**KO:** URL·dataset ID뿐 아니라 과거 snapshot의 실제 복구 가능성까지 재현성 메타데이터로 관리해야 한다. 후속 방법론에는 `snapshot recoverability / historical version retention`을 명시적 평가필드로 추가할 가치가 있다.  
**EN:** Reproducibility metadata must track not only URLs and dataset IDs but whether historical snapshots remain recoverable. `Snapshot recoverability / historical version retention` should be considered as an explicit future qualification field.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and `WRITEBACK-001`. / 공식 산출물은 관련 규약을 따른다.
