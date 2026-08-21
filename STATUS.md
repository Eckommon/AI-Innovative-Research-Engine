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
- eight-stage innovation discovery methodology / 8단계 혁신탐색 방법론.
- Dataset / Combination / Project IPS separated / IPS 3종 분리.
- metadata schema calibrated to v0.2 / 메타데이터 스키마 v0.2.

### Research / 연구
- Issues #1–#4 Wave 0/1 initial queue — `COMPLETED`.
- Issue #5 `KR-GRID-F01` — feasibility complete, outcome `HOLD`; no localized/asset-attributed KPX model.
- Issue #6 `EU-IEE-E01` — first cross-dataset controlled experiment; empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `PARTIAL_PASS`: `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.

### Knowledge & Memory / 지식·메모리
- `KM-001` Obsidian-compatible knowledge management active / Obsidian 지식관리 활성.
- repository root = Vault; GitHub Markdown remains authoritative / 저장소 루트 Vault·GitHub Markdown 기준.
- Research/Datasets/Experiments/Decisions MOCs + controlled tag taxonomy active / MOC·통제 태그 활성.
- `READ-001 / FACT-001 / UNKNOWN-001 / CONFLICT-001 / FRESH-001 / MEMORY-001 / WRITEBACK-001` mandatory / 환각·드리프트 방지 규약 의무.
- `PROJECT_MEMORY`, `SESSION_HANDOFF`, `CLAIM_LEDGER`, `DECISION_LOG` active / 지속 메모리·인수인계·주장·결정 기록 활성.

## 2. Active Work — Issue #8 / 활성 작업 — Issue #8

### `EU-STEEL-R01 — Independent Reproduction of Steel Mercury Intensity / 철강 수은집약도 독립 재현`

**Objective / 목적:** independently reproduce EEA's EEA-33 `2008→2017 = -36%` mercury-emissions-per-unit-steel relationship from official raw E-PRTR + Eurostat PRODCOM inputs. / 공식 raw 입력에서 EEA -36% 관계 독립 재현.

### Frozen crosswalk / 고정 crosswalk
- E-PRTR: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: 2008–2017
- geography: EEA-33; Turkey absent, Serbia included
- target reference: 2017 intensity `36% lower` than 2008

### Reproduction gate / 재현 게이트
- `PASS`: independent percent change within ±2 percentage points of `-36%`.
- `PARTIAL`: inputs reproducible but documented legacy/version differences prevent exact agreement.
- `FAIL/HOLD`: unsupported assumptions required.

### Resolved / 해결
- EEA historical bulk lists Annex I activity-level air-release CSV (`F1_3`, ~13 MB); current Industrial Reporting also provides 2007–2024 tabular data. / E-PRTR raw 분자 경로 존재 확인.
- **`DS-066342` confirmed as annual Total production broken down by PRODCOM List.** / PRODCOM dataset 정체 확인.
- published T-code semantics confirmed as crude-steel categories split by alloy class and furnace process. / 철강 T-code 의미 확인.
- DS-prefixed PRODCOM uses Eurostat `api/comext/dissemination` endpoints. / 전용 API 경로 확인.
- EEA reference figure expresses mercury grams per kilotonne of steel production. / 기준 figure 단위 의미 확인.

### Current UNKNOWN / 현재 미확인
1. directly executable/readable E-PRTR Annex I CSV path in the current execution environment / 현재 실행환경의 E-PRTR raw CSV 직접 접근;
2. exact `DS-066342` API dimension/filter syntax for 2008 and 2017 T-code rows / PRODCOM filter 문법;
3. returned raw `QNTUNIT` and exact EEA-33 country aggregation needed for denominator / raw 수량단위·EEA-33 분모 국가집계.

No modern-code substitution, arbitrary facility allocation, or post-hoc tuning is allowed. / 현대코드 임의대체·시설 임의배분·사후 tuning 금지.

## 3. Persistent Holds / 지속 HOLD
- `C-KR-001` localized/asset attribution — `HOLD`.
- U.S. facility-level data-center energy/cooling/water — `HOLD_DATA_GAP`.
- generic EU facility-level production denominator — `HOLD`.

## 4. Next Actions / 다음 행동
1. obtain/read E-PRTR activity-level mercury numerator for 2008 and 2017 / E-PRTR 분자 확보;
2. resolve filtered `DS-066342` query + `QNTUNIT` / PRODCOM query·단위 확인;
3. freeze URL/filter/country/snapshot provenance / provenance 고정;
4. compute numerator and denominator separately, then intensity / 분자·분모·집약도 계산;
5. compare independently to `-36%` without tuning / 사후조정 없이 비교;
6. write back Issue #8, research record, Claim Ledger, Memory, Handoff, STATUS and MOCs / 기록 동기화.

## 5. Required Session Start / 세션 시작 의무

`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → research object → active Issue → claim/decision records`

Apply `READ-001` before material reasoning. / 실질 추론 전 `READ-001` 적용.

## 6. Safety / 안전
- no precise critical-infrastructure location/topology reconstruction / 중요 인프라 위치·토폴로지 재구성 금지;
- no unsupported classification/denominator allocation / 근거 없는 분류·분모 배분 금지;
- preserve `UNKNOWN`, `HOLD`, negative, inconclusive and non-novel results / 미확인·보류·부정적·불확정·비신규 결과 보존.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
