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

## 3. Frozen Crosswalk / 고정 Crosswalk
- E-PRTR: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: `2008–2017`
- geography: EEA-33; Turkey absent in E-PRTR, Serbia included
- reference: EEA `2017 vs 2008 = -36%`

No post-hoc crosswalk substitution. / 사후 crosswalk 대체 금지.

## 4. Access Findings / 접근 발견

### E-PRTR numerator / 분자
EEA historical 2007–2022 v11 user-friendly bulk listing includes Annex I activity-level air releases (`F1_3`, ~13 MB) and facility-level air releases (`F1_4`, ~101 MB). Current Industrial Reporting also offers 2007–2024 tabular downloads. / historical·현행 raw 분자 경로 존재 확인.

### PRODCOM denominator / 분모
- `DS-066342` is confirmed as **annual Total production broken down by PRODCOM List**. / `DS-066342` 정체 해결.
- DS-prefixed PRODCOM uses Eurostat `api/comext/dissemination` endpoints. / 전용 Comext API 사용.
- Published T-codes map to crude steel categories split by alloy class and furnace process; code meanings remain identifiable in current statistical code lists. / T-code 의미 확인.
- EEA figure unit is mercury grams per kilotonne steel production. / 기준 figure 단위 확인.

## 5. Remaining UNKNOWN / 남은 미확인

1. Directly executable E-PRTR CSV download/read path in the current execution environment. / 현 실행환경 E-PRTR CSV 직접 접근.
2. Exact Eurostat `DS-066342` API dimension/filter syntax for 2008 and 2017 legacy T-code rows. / DS-066342 filter 문법.
3. Raw PRODCOM quantity unit (`QNTUNIT`) and exact country aggregation needed to reproduce the EEA-33 denominator. / raw 수량단위·EEA-33 분모 국가 집계.

## 6. Predefined Reproduction Gate / 사전 재현 게이트

- `PASS`: independent change within ±2 percentage points of `-36%`.
- `PARTIAL`: raw extraction reproducible but documented legacy/version difference prevents exact agreement.
- `FAIL/HOLD`: unsupported assumptions required.

## 7. Exact Next Actions / 정확한 다음 행동

1. Resolve E-PRTR `F1_3` or current equivalent download and inspect schema. / E-PRTR 분자 파일 확보·schema 확인.
2. Resolve `DS-066342` filtered API query and `QNTUNIT` for target codes/years. / PRODCOM query·단위 확인.
3. Freeze raw URLs, filters, countries and snapshots. / URL·filter·국가·snapshot 고정.
4. Calculate Hg numerator and steel denominator separately for 2008 and 2017. / 분자·분모 별도 계산.
5. Compute intensity change and compare to `-36%` without tuning. / 사후 조정 없이 기준 비교.
6. Write back Issue #8, experiment result, Claim Ledger, Memory, STATUS and MOCs. / 결과 기록.

## 8. Known Holds / 알려진 보류
- KPX localized bus mapping: `HOLD`.
- Generic EU facility-level production denominator: `HOLD`.
- EEA chart CSV failed through one fetch path; treat as access-path failure, not data absence. / chart CSV 한 경로 실패는 데이터 부재가 아님.

## 9. Mandatory Read Set Next Session / 다음 세션 의무 읽기
1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. this file / 본 파일
5. `docs/HALLUCINATION_CONTROL_PROTOCOL.md`
6. `research/EU-STEEL-R01/README.md`
7. Issue #8
8. `registry/CLAIM_LEDGER.md`, `registry/DECISION_LOG.md`

Official artifacts comply with `LANG-001`, `READ-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
