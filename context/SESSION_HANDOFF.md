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

- Wave 1 initial discovery (#1–#4): `COMPLETED`
- Issue #5 `KR-GRID-F01`: `COMPLETED` with research outcome `HOLD`
- Issue #6 `EU-IEE-E01`: `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`
- Issue #7 `EU-IEE-F02`: `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`
- **Active Issue / 활성 Issue:** **#8 `EU-STEEL-R01`**

## 2. Active Objective / 활성 목적

**KO:** EEA가 발표한 EEA-33 철강 생산단위당 수은배출 2008→2017 `-36%` 관계를 raw/official E-PRTR + Eurostat PRODCOM 입력에서 독립 재현한다.  
**EN:** Independently reproduce EEA's published EEA-33 2008→2017 `-36%` change in mercury emissions per unit steel production from raw/official E-PRTR + Eurostat PRODCOM inputs.

## 3. Fixed Crosswalk / 고정 Crosswalk

- E-PRTR activity: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: `2008–2017`
- geography: EEA-33; Turkey absent in E-PRTR, Serbia included
- reference: EEA reports `-36%` 2017 vs 2008

Do not replace these legacy codes with modern codes unless an authoritative correspondence is documented. / 권위 correspondence 없이 legacy code를 현대 코드로 대체하지 않는다.

## 4. Access Findings / 접근 발견

### E-PRTR numerator / 분자
EEA historical user-friendly bulk data list includes:
- `F1_3_Total Release at E-PRTR Annex I Activity into Air.csv` (~13 MB)
- `F1_4_Detailed releases at facility level ... into Air.csv` (~101 MB)
for the 2007–2022 v11 data package. / 2007–2022 v11 package에 Annex I activity 및 시설별 대기배출 CSV가 존재.

Current EEA Industrial Reporting also exposes downloadable 2007–2024 tabular data. / 현행 EEA Industrial Reporting도 2007–2024 tabular download 제공.

### PRODCOM denominator / 분모
DS-prefixed PRODCOM datasets use the Eurostat `https://ec.europa.eu/eurostat/api/comext/dissemination` endpoint and require filtered requests. / DS-prefix PRODCOM은 전용 Comext endpoint 사용.

## 5. Predefined Reproduction Gate / 사전 재현 게이트

- `PASS`: independent 2008→2017 percent change within ±2 percentage points of EEA `-36%`.
- `PARTIAL`: raw extraction reproducible but documented legacy/version difference prevents exact agreement.
- `FAIL/HOLD`: cannot reproduce inputs/semantics without unsupported assumptions.

## 6. Exact Next Actions / 정확한 다음 행동

1. Resolve a directly downloadable/readable E-PRTR numerator file for 2008–2017 mercury + the three activity codes. / E-PRTR 분자 파일 확보.
2. Query/discover the legacy PRODCOM dataset containing the published steel product codes and determine units. / legacy PRODCOM dataset·단위 확인.
3. Preserve raw query URLs/filters and snapshot dates. / raw query·filter·snapshot 보존.
4. Compute annual numerator and denominator separately before computing intensity. / 집약도 전 분자·분모 별도 계산.
5. Compare independent result with EEA `-36%`; do not adjust filters post hoc merely to match. / -36%에 맞추기 위한 사후 filter 변경 금지.
6. Update Issue #8, research artifact, Claim Ledger, Project Memory, STATUS, and relevant MOCs. / 관련 기록 동기화.

## 7. Known Holds / 알려진 보류

- KPX localized bus mapping remains `HOLD`; do not reopen without new authoritative public evidence. / KPX 지역귀속은 새 권위근거 없이는 재개하지 않음.
- Generic EU facility-level production denominator remains `HOLD`. / 일반 EU 시설단위 생산분모 HOLD.
- EEA chart CSV direct download failed through current web fetch path; this is an access-path issue, not evidence that data do not exist. / EEA chart CSV 직접 fetch 실패는 접근경로 문제이며 데이터 부재를 의미하지 않음.

## 8. Mandatory Read Set Next Session / 다음 세션 의무 읽기

1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. this file / 본 파일
5. `docs/HALLUCINATION_CONTROL_PROTOCOL.md`
6. `research/EU-IEE-F02/README.md`
7. Issue #8
8. `registry/CLAIM_LEDGER.md` and `registry/DECISION_LOG.md`

Official artifacts comply with `LANG-001`. / 공식 산출물은 `LANG-001`을 따른다.
