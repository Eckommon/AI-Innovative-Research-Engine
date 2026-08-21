# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Baseline / 베이스라인:** `v0.3-knowledge-memory`  
**Date / 기준일:** 2026-08-22  
**State / 상태:** `CROSS_DATASET_REPRODUCTION_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #8 `EU-STEEL-R01`

## 1. Completed / 완료

### Foundation / 기반
- GitHub = persistent Source of Truth / 지속 기준 저장소.
- `LANG-001` bilingual policy mandatory / 한·영 병기 의무.
- eight-stage innovation-discovery methodology + Dataset/Combination/Project IPS / 8단계 방법론·IPS 3종.
- Obsidian MOC/tag knowledge layer and durable GitHub memory active / Obsidian 지식레이어·지속 메모리 활성.
- `READ-001 / FACT-001 / UNKNOWN-001 / CONFLICT-001 / FRESH-001 / MEMORY-001 / WRITEBACK-001` mandatory / 환각·드리프트 방지 규약 의무.

### Research / 연구
- Issues #1–#4 Wave 0/1 initial queue — `COMPLETED`.
- Issue #5 `KR-GRID-F01` — `COMPLETED`, research outcome `HOLD`.
- Issue #6 `EU-IEE-E01` — `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.

## 2. Active Work — Issue #8 / 활성 작업 — Issue #8

### `EU-STEEL-R01 — Independent Reproduction of Steel Mercury Intensity / 철강 수은집약도 독립 재현`

**Objective / 목적:** independently reproduce EEA's EEA-33 `2008→2017 = -36%` mercury-emissions-per-unit-steel relationship from official raw E-PRTR + Eurostat PRODCOM inputs. / 공식 raw 입력에서 EEA -36% 관계 독립 재현.

### Frozen reference / 고정 기준
- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: `2008–2017`
- EEA-33: EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia; Turkey absent from E-PRTR
- target: 2017 intensity `36% lower` than 2008
- chart unit: grams Hg / kilotonne steel

### Gate / 게이트
- `PASS`: independent percent change within `-38%` to `-34%`.
- `PARTIAL`: raw extraction reproducible but documented legacy/version differences prevent agreement.
- `FAIL/HOLD`: unsupported assumptions required.

### Newly resolved / 신규 해결
- EEA-33 membership and exact primary-report crosswalk / EEA-33 구성·공식 crosswalk.
- historical E-PRTR numerator file existence: `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` / historical 분자 파일 존재.
- current EEA Industrial Reporting v16 incorporates historical 2007–2017 E-PRTR and defines pollutant releases/transfers as `kg/year` / 현행 표준화 DB의 historical 통합·분자 단위.
- historical denominator source `DS-066342` confirmed / 과거 분모 dataset.
- official historical EUROPROMS archives `epanntotal-r2.zip`, `epanntotal.zip` confirmed / legacy bulk archive.
- current annual total-production dataset `DS-059359` confirmed; `APRODQNT` = actual production quantity, `QNTUNIT` = quantity unit / 현행 dataset·필드 의미.
- Eurostat Files API relative-path retrieval rule confirmed / Files API 규칙.

### Remaining `UNKNOWN` / 남은 미확인
1. executable byte-level read/schema of E-PRTR `F1_3` or current official equivalent / E-PRTR raw 실제 읽기·schema;
2. executable byte-level read/schema of `EUROPROMS/epanntotal-r2.zip` / historical PRODCOM ZIP 실제 읽기·schema;
3. actual physical `QNTUNIT` for the six target steel rows in 2008 and 2017 / 목표 row 실제 단위값;
4. exact raw reporter/aggregate method used to construct the EEA-33 steel denominator / EEA-33 분모 reporter/aggregate 방식;
5. raw 2008/2017 Hg and steel quantities and therefore the independently calculated intensity change / 실제 분자·분모·독립 변화율.

**Access boundary / 접근 경계:** official source existence and semantics are `V2_PRIMARY_VERIFIED`; raw numerical reproduction remains below `V3_REPRODUCED` until bytes/rows are actually extracted. / 공식 출처·의미는 V2이나 실제 raw 추출 전 V3로 승격하지 않는다.

## 3. Persistent Holds / 지속 HOLD
- `C-KR-001` localized/asset attribution — `HOLD`.
- U.S. facility-level data-center energy/cooling/water — `HOLD_DATA_GAP`.
- generic EU facility-level production denominator — `HOLD`.

## 4. Next Actions / 다음 행동
1. resolve an executable official EEA raw-download path and inspect 2008/2017 mercury rows / EEA raw 실행 접근 확보;
2. resolve an executable Eurostat historical `epanntotal-r2.zip` download and inspect six T-code rows / historical PRODCOM ZIP 확보;
3. freeze files/URLs/hashes, reporter set, product codes and units before calculation / 계산 전 provenance 고정;
4. calculate `Hg_2008`, `Hg_2017`, `Steel_2008`, `Steel_2017` separately / 분자·분모 별도 계산;
5. calculate intensity change and compare to frozen `-36%` gate without tuning / 사후조정 없이 비교;
6. write back Issue #8, research object, Claim Ledger, Memory/Handoff/STATUS/MOC as applicable / 기록 동기화.

## 5. Required Session Start / 세션 시작 의무
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → research object → active Issue → claim/decision records`

Apply `READ-001` before material reasoning. / 실질 추론 전 `READ-001` 적용.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
