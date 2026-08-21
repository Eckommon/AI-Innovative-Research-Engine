---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
tags:
  - type/memory
  - state/experiment
  - region/eu
  - domain/industry
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Session Handoff / 세션 인수인계

> **Latest operational checkpoint only / 최신 운영 checkpoint 전용**  
> 다음 세션은 이 파일을 읽고 작업을 재개한다. / The next session resumes from this file.

## 1. Current State / 현재 상태

- Issues #1–#4 Wave 0/1 discovery: `COMPLETED`
- Issue #5 `KR-GRID-F01`: `COMPLETED`, research outcome `HOLD`
- Issue #6 `EU-IEE-E01`: `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`
- Issue #7 `EU-IEE-F02`: `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`
- **Active Issue / 활성 Issue:** **#8 `EU-STEEL-R01`**

## 2. Active Objective / 활성 목적

**KO:** EEA가 발표한 EEA-33 철강 생산단위당 수은배출 2008→2017 `-36%` 관계를 raw/official E-PRTR + Eurostat PRODCOM 입력에서 독립 재현한다.  
**EN:** Independently reproduce EEA's published EEA-33 2008→2017 `-36%` change in mercury emissions per unit steel production from raw/official E-PRTR + Eurostat PRODCOM inputs.

## 3. Frozen Reference / 고정 기준

- E-PRTR: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: `2008–2017`
- EEA-33 = EU-28 + Iceland + Liechtenstein + Norway + Switzerland + Serbia
- Turkey absent from E-PRTR
- reference = `2017 vs 2008 = -36%`
- display unit = grams Hg / kilotonne steel

No post-hoc crosswalk substitution or tuning. / 사후 crosswalk 대체·tuning 금지.

## 4. Resolved This Checkpoint / 이번 checkpoint 해결

### EEA numerator / 분자
- historical EEA package lists `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` (~13 MB).
- EEA Industrial Reporting v16 explicitly integrates historical E-PRTR data for 2007–2017.
- v16 metadata defines pollutant releases/transfers as **kg/year**.
- official direct-distribution directory is `https://sdi.eea.europa.eu/webdav/datastore/public/eea_t_ied-eprtr_p_2007-2024_v16_r00`.

**Still not reproduced:** current execution environment has not transported/read the raw table bytes. / 실제 byte·row 읽기는 미완료.

### PRODCOM denominator / 분모
- EEA Figure 1 historical source = `DS-066342` total production.
- Eurostat official EUROPROMS inventory lists `epanntotal-r2.zip` and `epanntotal.zip`.
- Eurostat current Files API retrieves `/comext` special files with `?file=<relative-path>`.
- current annual total-production dataset = `DS-059359` (1995 onward).
- current fields: `APRODQNT` actual production quantity; `QNTUNIT` quantity unit; `APQNTFLAG`, `APQNTBASE` availability/rounding metadata.

**Do not assume** `DS-059359` is a one-to-one migration of historical `DS-066342` without authoritative correspondence. / 현행·과거 dataset 1:1 migration 가정 금지.

## 5. Remaining UNKNOWN / 남은 미확인

1. executable/raw read of E-PRTR `F1_3` or v16 equivalent and its row schema / E-PRTR raw 직접 읽기·schema;
2. executable/raw read of historical `EUROPROMS/epanntotal-r2.zip` and legacy schema / historical PRODCOM ZIP 직접 읽기·schema;
3. actual `QNTUNIT` of the six target steel rows for 2008/2017 / 목표 철강 row 실제 단위;
4. exact reporter/aggregate procedure used by EEA for the EEA-33 steel denominator / EEA-33 분모 집계법;
5. actual 2008/2017 numerator, denominator, intensities and independent percent change / 실제 수치·독립 변화율.

`V2_PRIMARY_VERIFIED` source semantics must not be mislabeled `V3_REPRODUCED` before raw extraction succeeds. / raw 추출 전 V3 승격 금지.

## 6. Predefined Gate / 사전 게이트

- `PASS`: independent change within `-38%` to `-34%`.
- `PARTIAL`: raw extraction reproducible but documented legacy/version differences prevent exact agreement.
- `FAIL/HOLD`: unsupported assumptions required.

## 7. Exact Next Actions / 정확한 다음 행동

1. obtain raw EEA table bytes through the official direct distribution and identify fields for year, country, Annex I activity, pollutant and quantity / EEA raw 확보·필드 확인;
2. obtain `epanntotal-r2.zip` through Eurostat official Files API and inspect legacy columns / historical PRODCOM 확보;
3. select only frozen activity/product/year/geography rows and record units/flags / 고정 filter 적용;
4. freeze files/URLs/snapshot dates/hashes before computation / provenance 고정;
5. compute `Hg_2008`, `Hg_2017`, `Steel_2008`, `Steel_2017`, then intensities and percent change / 수치 계산;
6. compare to `-36%` without changing filters after seeing the result / 사후 filter 변경 금지;
7. update Issue #8 + research artifact + Claim Ledger + STATUS + Handoff, and Project Memory only if a durable decision changes / writeback.

## 8. Known Holds / 알려진 보류
- KPX localized bus mapping: `HOLD`.
- Generic EU facility-level production denominator: `HOLD`.
- raw web transport failures are access-path failures, not proof of data absence. / web transport 실패를 데이터 부재로 해석하지 않음.

## 9. Mandatory Read Set Next Session / 다음 세션 의무 읽기
1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. this file / 본 파일
5. `docs/HALLUCINATION_CONTROL_PROTOCOL.md`
6. `research/EU-STEEL-R01/README.md`
7. Issue #8
8. `registry/CLAIM_LEDGER.md`, `registry/DECISION_LOG.md`

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
