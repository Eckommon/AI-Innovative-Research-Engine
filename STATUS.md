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
- eight-stage innovation discovery methodology established / 8단계 혁신탐색 방법론 확립.
- Dataset / Combination / Project IPS separated / IPS 3종 분리.
- metadata schema calibrated to v0.2 / 메타데이터 스키마 v0.2 보정.

### Research Material & Wave 1 / 소재·Wave 1
- frontier + persistent-bottleneck research-material landscape completed / 유망영역+잔존병목 소재지형 완료.
- Issue #1 `AMBENCH-001` — `COMPLETED`
- Issue #2 U.S. / 미국 — `COMPLETED`
- Issue #3 Korea / 한국 — `COMPLETED`
- Issue #4 EU — `COMPLETED`
- Wave 1 synthesis and feasibility tournament — `COMPLETED`

### Post-Wave 1 / Wave 1 이후
- Issue #5 `KR-GRID-F01` — completed feasibility, outcome `HOLD`; no localized/asset-attributed KPX model. / 지역·설비 귀속 모델 승격 없음.
- Issue #6 `EU-IEE-E01` — first cross-dataset controlled experiment; empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `PARTIAL_PASS`: `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.

### Knowledge & Memory / 지식·메모리
- `KM-001` Obsidian-compatible knowledge management activated. / Obsidian 지식관리 도입.
- repository root designated as Vault; GitHub Markdown remains authoritative. / 저장소 루트 Vault, GitHub Markdown 기준.
- MOCs added for research, datasets, experiments, decisions. / 연구·데이터·실험·결정 MOC 추가.
- controlled tag taxonomy added. / 통제 태그체계 추가.
- `READ-001 / FACT-001 / UNKNOWN-001 / CONFLICT-001 / FRESH-001 / MEMORY-001 / WRITEBACK-001` made mandatory. / 환각·드리프트 방지 규약군 도입.
- durable `context/PROJECT_MEMORY.md`, `context/SESSION_HANDOFF.md`, `registry/CLAIM_LEDGER.md`, `registry/DECISION_LOG.md` established. / 지속 메모리·인수인계·주장·결정 기록 확립.

## 2. Active Work — Issue #8 / 활성 작업 — Issue #8

### `EU-STEEL-R01 — Independent Reproduction of Steel Mercury Intensity / 철강 수은집약도 독립 재현`

**Objective / 목적:** independently reproduce EEA's published EEA-33 `2008→2017 = -36%` mercury-emissions-per-unit-steel relationship from raw/official E-PRTR + Eurostat PRODCOM inputs. / raw 공식 입력으로 EEA -36% 관계 독립 재현.

### Frozen crosswalk / 고정 crosswalk
- E-PRTR: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM: `2410T121-122`, `2410T131-132`, `2410T141-142`
- period: 2008–2017
- geography: EEA-33; Turkey absent, Serbia included

### Reproduction gate / 재현 게이트
- `PASS`: independent change within ±2 percentage points of `-36%`.
- `PARTIAL`: inputs reproducible but documented legacy/version differences prevent exact agreement.
- `FAIL/HOLD`: unsupported assumptions required.

### Current verified access findings / 현재 검증 접근
- EEA historical bulk package lists Annex I activity-level air release CSV (~13 MB) and facility-level air release CSV (~101 MB). / EEA historical bulk 분자 후보 확인.
- Current EEA Industrial Reporting provides downloadable 2007–2024 tabular data. / 현행 2007–2024 tabular 데이터 제공.
- Eurostat DS-prefixed PRODCOM uses dedicated `api/comext/dissemination` endpoints with filtered queries. / PRODCOM 전용 API 경로 확인.

### Current UNKNOWN / 현재 미확인
- exact executable download path/schema for the historical numerator in the current environment / 현재 환경에서 historical 분자 직접 추출 경로·schema;
- active/archive dataset mapping for legacy `DS-066342` and published `T` steel codes / legacy PRODCOM dataset·T code 현행/보관 mapping;
- relevant production quantity units / 생산수량 단위.

No modern-code substitution or post-hoc filter tuning is allowed without authoritative correspondence. / 권위 correspondence 없는 현대코드 대체·사후 filter 조정 금지.

## 3. Comparative Strategic Finding / 비교 전략 결론

- Korea / 한국: high-frequency operational/grid data / 고빈도 운영·계통 데이터.
- U.S. / 미국: cross-agency diversity + benchmark research data / 기관간 다양성+benchmark.
- EU: harmonized classification + cross-national semantics / 조화 분류+국가간 의미체계.

Use jurisdiction-specific comparative data advantages under a common research schema rather than forcing identical source structures. / 동일 데이터 구조를 강제하지 않고 각 지역 비교우위를 공통 연구 schema에서 연결한다.

## 4. Persistent Holds / 지속 HOLD

- `C-KR-001` localized/asset attribution — `HOLD`
- U.S. facility-level data-center energy/cooling/water — `HOLD_DATA_GAP`
- generic EU facility-level production denominator — `HOLD`

## 5. Next Actions / 다음 행동

1. Continue Issue #8 raw numerator/denominator retrieval. / #8 raw 분자·분모 확보.
2. Freeze query URLs/filters/snapshot metadata before calculation. / 계산 전 query·filter·snapshot 고정.
3. Compute yearly inputs separately and reproduce 2008→2017 intensity change. / 연도별 분자·분모 및 변화율 재현.
4. Compare against `-36%` without post-hoc tuning. / 사후 조정 없이 비교.
5. Update Issue #8 + research artifact + Claim Ledger + Project Memory + Session Handoff. / 기록 동기화.
6. After Issue #8, promote the next highest-information-gain experiment rather than automatically following highest IPS. / #8 이후 최고 IPS보다 정보이득이 큰 다음 실험 선정.

## 6. Required Session Start / 세션 시작 의무

Apply `READ-001`: / `READ-001` 적용:
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → relevant research object → active Issue → claims/decisions as needed`.

## 7. Safety / 안전

- no precise critical-infrastructure location/topology reconstruction from indirect identifiers / 중요 인프라 간접 식별자 기반 위치·토폴로지 재구성 금지;
- no unsupported classification or denominator allocation / 근거 없는 분류·분모 배분 금지;
- preserve `UNKNOWN`, `HOLD`, negative and non-novel results / 미확인·보류·부정적·비신규 결과 보존.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
