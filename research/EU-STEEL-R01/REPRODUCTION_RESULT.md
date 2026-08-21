---
id: EU-STEEL-R01-RESULT
type: reproduction-result
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
---

# EU-STEEL-R01 Reproduction Result / 철강 수은집약도 독립 재현 결과

**Issue / 이슈:** #8  
**Frozen gate outcome / 고정 게이트 결과:** `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`  
**Reason / 사유:** the original 2017 legacy PRODCOM denominator (`DS-066342`) is no longer disseminated through the tested official Eurostat APIs/dataflow, while current replacement-compatible data cannot be substituted without violating the frozen no-assumption rule. / 원 연구의 2017 legacy PRODCOM 분모(`DS-066342`)가 시험한 현행 Eurostat 공식 API/dataflow에서 더 이상 배포되지 않으며, 현행 호환 데이터로의 대체는 사전 무가정 규칙을 위반하므로 독립 재현을 확정할 수 없다.

## 1. Frozen Reference / 고정 기준

- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM products: `2410T121`, `2410T122`, `2410T131`, `2410T132`, `2410T141`, `2410T142`
- years: `2008`, `2017`
- geography: EEA-33 = EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia
- published narrative target: 2017 intensity `36% lower` than 2008
- unit: grams Hg per kilotonne steel
- gate: `PASS` only for independently reproduced change within `-38%..-34%`; unsupported assumptions force `HOLD`.

No post-hoc crosswalk, country, unit, missing-value, or dataset substitution was permitted. / 사후 crosswalk·국가·단위·결측값·dataset 대체를 허용하지 않았다.

## 2. Machine-Reproduced E-PRTR Numerator / 기계 재현 E-PRTR 분자

Official historical EEA files were downloaded and hashed in GitHub Actions. / GitHub Actions에서 공식 EEA historical 파일을 직접 다운로드·해시했다.

### `F1_3` aggregate-by-activity file
SHA-256:
`b14d792fa9e7b540effaddd7182186fb01d766906ad9c7ab1a6d5325b33439c4`

Frozen activity + mercury filter produced: / 고정 activity + mercury filter 결과:

| Year | Hg to air |
|---|---:|
| 2008 | **4,312.9 kg** |
| 2017 | **3,327.1 kg** |

Change in numerator alone / 분자 단독 변화율: **-22.8570%**.

### `F1_4` facility-level detailed file
SHA-256:
`358d61ed6f718a6d5761620b7a5e4f20eb8b6ef5d7bd690ca1a7ae61e77963f3`

Applying the same frozen filter produced exactly the same totals: / 동일 고정 filter 적용 결과 합계가 정확히 일치했다.

| Year | F1_3 | F1_4 |
|---|---:|---:|
| 2008 | 4,312.9 kg | 4,312.9 kg |
| 2017 | 3,327.1 kg | 3,327.1 kg |

**Decision / 판단:** the reproduction discrepancy is not explained by choosing the aggregated `F1_3` instead of facility-level `F1_4`. / 재현 불일치는 `F1_3` 대신 facility-level `F1_4`를 사용하지 않았기 때문이 아니다.

## 3. Current EEA Figure Data Conflict / 현행 EEA Figure 데이터 내부 불일치

The current EEA chart download returned the following reference values: / 현행 EEA chart CSV가 다음 값을 반환했다.

| Year | Facilities | Hg intensity (g/kt) |
|---|---:|---:|
| 2008 | 288 | **35.0** |
| 2017 | 250 | **20.5** |

Direct arithmetic from the currently distributed figure CSV: / 현행 배포 CSV 직접 계산:

`(20.5 / 35.0 - 1) × 100 = -41.4286%`

This differs materially from the EEA briefing narrative stating `-36%`. / 이는 EEA briefing 본문의 `-36%` 서술과 유의미하게 다르다.

The project does **not** infer why the narrative and current figure CSV differ. Possible causes such as later data revision, version drift, or rounding are not promoted without evidence. / 본 프로젝트는 본문과 현행 figure CSV가 다른 원인을 추정해 확정하지 않는다. 후속 데이터 개정·버전 드리프트·반올림 등은 근거 없이 승격하지 않는다.

EEA figure CSV SHA-256:
`314cea2bf2de34b96e14e2ce47d1ac6bb0304e943abfbc9b176f5e4fb5b0875a`

## 4. Historical PRODCOM Evidence / Historical PRODCOM 증거

Official Eurostat EUROPROMS archives were machine-read. / 공식 Eurostat EUROPROMS archive를 기계 판독했다.

### `epanntotal-r2.zip`
- schema: `DECL, PERIOD, PRCCODE, QNTUNIT, PQNTFLAG, PRODQNT, PQNTBASE`
- observed period range: `199552..201452`
- six frozen T-codes are present
- target 2008 quantity unit: `kg`
- does **not** contain 2017.

### `epanntotal.zip`
- observed period range: `199552..201252`
- does **not** contain 2017.

The official Eurostat bulk inventory exposes these files, but they cannot supply the required 2017 denominator. / 공식 bulk inventory에 파일은 존재하지만 요구되는 2017 분모를 제공하지 못한다.

## 5. Current `DS-059359` Diagnostic — Not a Legacy Substitute / 현행 `DS-059359` 진단 — legacy 대체 금지

The current Eurostat total-production API was reproduced with dimensions: / 현행 Eurostat total-production API의 실제 dimension을 재현했다.

`freq / reporter / product / indicators / time`

Indicators: `APRODQNT`, `QNTUNIT`, `APQNTFLAG`, `APQNTBASE`.

The literal frozen T-codes exist in 2017 and use `KG`. / 고정 T-code는 2017에도 literal code로 존재하며 `KG` 단위를 사용한다.

For diagnostic purposes only, the six-code **EU28** sum is: / 진단 전용 6-code EU28 합계:

| Year | EU28 steel quantity |
|---|---:|
| 2008 | 168,619,860,319 kg |
| 2017 | 129,543,917,700 kg |

Using the reproduced E-PRTR numerator with this **EU28-only diagnostic** yields: / 재현 분자와 EU28-only 진단분모 계산:

| Year | Diagnostic intensity |
|---|---:|
| 2008 | 25.5777 g/kt |
| 2017 | 25.6832 g/kt |

Diagnostic change: **+0.4126%**.

This is **not** an EEA-33 reproduction result. / 이는 EEA-33 재현 결과가 아니다.

Why it cannot be promoted: / 승격 불가 이유:
- `IS` and `NO` returned explicit zero for the tested frozen products;
- `LI` and `CH` returned `null`, not explicit zero;
- `XS` returned `null` in 2008 and explicit zero in 2017;
- treating `null` as zero would be an unsupported assumption;
- no authoritative one-to-one correspondence was established allowing `DS-059359` to replace the historical `DS-066342` snapshot used by EEA.

## 6. Legacy `DS-066342` Recovery Probe / Legacy `DS-066342` 복구 탐색

GitHub Actions directly probed official Eurostat endpoints on 2026-08-22. / 2026-08-22 GitHub Actions에서 Eurostat 공식 endpoint를 직접 조회했다.

Results: / 결과:

- COMEXT Statistics API, 2008: HTTP `404`
- COMEXT Statistics API, 2017: HTTP `404`
- regular Statistics API, 2017: HTTP `404`
- SDMX dataflow: HTTP `404`

Returned Eurostat message: / Eurostat 반환 메시지:

`DS-066342 ... is not available for dissemination.`

The historical dataset identity remains verified, but the exact legacy 2017 data slice required for this reproduction is not recoverable through the tested current official dissemination interfaces. / historical dataset 정체성은 검증됐으나, 재현에 필요한 정확한 legacy 2017 slice는 시험한 현행 공식 배포 인터페이스에서 복구되지 않는다.

## 7. Frozen Gate Decision / 고정 게이트 판정

### Outcome: `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`

`PASS` is **not** granted. `PARTIAL` is also **not** granted under the original strict definition because the exact historical denominator is not reproducibly extractable. / `PASS`를 부여하지 않으며, 정확한 historical 분모 자체가 재현 추출되지 않으므로 원래의 엄격한 정의상 `PARTIAL`도 부여하지 않는다.

This outcome means: / 이 결과의 의미:
1. the EEA numerator path and frozen activity filtering are reproducible at V3 level;
2. the current EEA figure CSV itself now implies `-41.43%`, while the briefing narrative states `-36%`;
3. the historical denominator dataset used by the briefing is discontinued and not available through tested current Eurostat dissemination endpoints;
4. a current compatibility dataset cannot be silently substituted;
5. therefore the historical `-36%` claim cannot presently be independently reproduced from a complete matched legacy input pair without unsupported assumptions.

This is **not a falsification** of the historical EEA analysis. It is a reproducibility/version-lineage limitation under the evidence currently recoverable. / 이는 과거 EEA 분석의 반증이 아니다. 현재 복구 가능한 증거에서 발생한 재현성·버전 계보 한계다.

## 8. Reproduction Runs / 재현 Run

- Run 7: `32534535674` — frozen EEA-33 denominator attempt → `HOLD_UNRESOLVED_DENOMINATOR`
- Run 8: `32534683910` — current EEA figure CSV + `F1_3` vs `F1_4` numerator diagnostic
- Run 9: `32534864866` — discontinued `DS-066342` official endpoint recovery probe

## 9. Research Value / 연구 가치

This reproduction failure is retained as a positive methodological asset: / 이 재현 실패는 방법론적 자산으로 보존한다.

- published percentage claims can drift from currently distributed chart data;
- dataset identifiers may remain citable after raw dissemination is discontinued;
- a newer dataset with similar semantics is not automatically a valid historical replacement;
- missing (`null`) national values must not be silently converted to zero;
- reproducibility engines require snapshot/version provenance, not only source URLs and dataset names.

**Methodology implication / 방법론 시사점:** future source qualification should score **snapshot recoverability / historical version retention** as a first-class reproducibility field. / 향후 source qualification에는 `snapshot recoverability / historical version retention`을 1급 재현성 필드로 포함할 가치가 있다.
