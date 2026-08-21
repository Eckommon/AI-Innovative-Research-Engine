# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Baseline / 베이스라인:** `v0.5-track-aligned-experiment`  
**Date / 기준일:** 2026-08-22  
**State / 상태:** `RAW_TRACK_CONTROLLED_EXPERIMENT_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #13 `AMBENCH-E03`

## 1. Completed / 완료

### Foundation / 기반
- GitHub = persistent Source of Truth / 지속 기준 저장소.
- `LANG-001` bilingual policy mandatory / 한·영 병기 의무.
- eight-stage innovation-discovery methodology + Dataset/Combination/Project IPS / 8단계 방법론·IPS 3종.
- Obsidian MOC/tag knowledge layer and durable GitHub memory active / Obsidian 지식레이어·지속 메모리 활성.
- hallucination/drift controls `READ-001 / FACT-001 / UNKNOWN-001 / CONFLICT-001 / FRESH-001 / MEMORY-001 / WRITEBACK-001` mandatory.
- normalized metadata schema **v0.3** includes snapshot/version lineage and `reproduction_risk` gate.

### Research / 연구
- Issues #1–#4 Wave 0/1 initial queue — `COMPLETED`.
- Issue #5 `KR-GRID-F01` — `COMPLETED`, `HOLD`.
- Issue #6 `EU-IEE-E01` — `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.
- Issue #8 `EU-STEEL-R01` — `COMPLETED`, `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`.
- Issue #10 `METHOD-001` — `COMPLETED`, snapshot recoverability promoted into source qualification.
- Issue #11 `AMBENCH-F02` — **`COMPLETED — PASS`**, exact 21-track/repeat alignment with nested optical outcomes.

## 2. Issue #11 Durable Result / Issue #11 지속 결과

`AMBENCH-F02` passed its frozen feasibility gate using official NIST raw-source semantics and versioned PDR evidence. / 공식 NIST raw-source 의미·version PDR 증거로 고정 feasibility gate를 통과했다.

- thermography `/ThermalData/Line_X_Y_Z/`: `Z` = one of three repeats per line / line별 3회 반복.
- optical naming/workbook preserves matching case + track number / optical naming·workbook이 동일 case+track 번호 보존.
- 21 single tracks = seven process cases × three repeats / 7조건×3반복.
- each exact track has two optical cross-section measurements; they are nested spatial outcomes, not extra thermography repeats / track당 두 단면은 nested outcome.
- optical XLSX SHA-256 = `2cfaac96aaca3dabb77b7029f842cdcc7e75c5a2cf3577d0734823246364a931`, exact downloaded/sidecar/PDR three-way match.
- thermography HDF5 official SHA-256 = `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`.
- source `reproduction_risk = LOW`.

Detailed: `research/AMBENCH-F02/README.md`; `CLM-014..015`; `DEC-011`; Run `32535986814`.

## 3. Active — Issue #13 / 활성 — Issue #13

### `AMBENCH-E03 — Track-level Thermography → Melt-Pool Geometry Controlled Experiment`

**Objective / 목적:** test whether thermography adds material predictive value beyond process parameters for track-level melt-pool depth/width using the exact 21-track alignment. / exact 21-track 정렬에서 thermography가 process parameter 대비 depth/width 예측 추가가치를 주는지 검증.

### Preregistered design / 사전등록 설계
- canonical `n = 21` physical tracks; optical cross-sections do not inflate sample count / 표준 표본수 21.
- target = per-track mean depth/width; cross-section spread retained as uncertainty / track 평균 depth/width.
- validation = seven-fold leave-one-process-case-out; all three repeats of held-out case excluded from training / process-case LOCO.
- models = low-capacity `PROCESS_ONLY`, `THERMO_ONLY`, `PROCESS_PLUS_THERMO` / 저용량 3모델군.
- primary metric = LOCO RMSE for depth and width / 주 지표 RMSE.
- material gate = ≥10% RMSE reduction on ≥1 target with no >10% degradation on the other / 기존 AMBENCH-001 기준 계승.
- no CNN/transformer or post-hoc capacity escalation / 고용량·사후 용량확대 금지.

Detailed preregistration: `research/AMBENCH-E03/README.md`; Issue #13.

## 4. Current Execution / 현재 실행

PR #14 is an execution-only trigger for **structural inspection before feature freezing**. / PR #14는 feature 고정 전 구조검사 전용이다.

Run scope only: / 범위
1. download exact NIST `mds2-2716` PDR v1.3.1 thermography HDF5 (~550 MB);
2. verify SHA-256 against frozen NIST checksum;
3. enumerate exactly 21 `Line_*` groups;
4. record Signal shapes/dtypes/chunks/compression and source attributes;
5. use **no optical outcomes and no model fitting**.

After structural evidence, freeze a compact outcome-blind thermography feature manifest before any prediction result is computed. / 구조근거 확인 후 예측결과 계산 전 outcome-blind thermal feature manifest를 고정한다.

## 5. Persistent Holds / 지속 HOLD
- KPX localized bus mapping — `HOLD`.
- generic EU facility-level production denominator — `HOLD`.
- historical EEA steel-mercury exact legacy reproduction — `HOLD_LEGACY_VERSION_DIVERGENCE`.

## 6. Required Session Start / 세션 시작 의무
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → research object → active Issue → claim/decision records`

Apply `READ-001` before material reasoning. / 실질 추론 전 `READ-001` 적용.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
