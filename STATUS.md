# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Baseline / 베이스라인:** `v0.4-reproducibility-lineage`  
**Date / 기준일:** 2026-08-22  
**State / 상태:** `READY_FOR_NEXT_CANDIDATE`  
**Active Work Queue / 활성 작업 큐:** none after Issue #10 methodology promotion / Issue #10 방법론 승격 완료 후 다음 후보 선정 대기

## 1. Completed / 완료

### Foundation / 기반
- GitHub = persistent Source of Truth / 지속 기준 저장소.
- `LANG-001` bilingual policy mandatory / 한·영 병기 의무.
- eight-stage innovation-discovery methodology + Dataset/Combination/Project IPS / 8단계 방법론·IPS 3종.
- Obsidian MOC/tag knowledge layer and durable GitHub memory active / Obsidian 지식레이어·지속 메모리 활성.
- `READ-001 / FACT-001 / UNKNOWN-001 / CONFLICT-001 / FRESH-001 / MEMORY-001 / WRITEBACK-001` mandatory / 환각·드리프트 방지 규약 의무.
- normalized metadata schema promoted to **v0.3**, adding snapshot/version lineage and reproduction-risk gates / snapshot·버전 계보·재현위험 게이트 추가.

### Research / 연구
- Issues #1–#4 Wave 0/1 initial queue — `COMPLETED`.
- Issue #5 `KR-GRID-F01` — `COMPLETED`, research outcome `HOLD`.
- Issue #6 `EU-IEE-E01` — `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.
- Issue #8 `EU-STEEL-R01` — `COMPLETED`, **`HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`**.
- Issue #10 `METHOD-001` — methodology hardening from #8; snapshot recoverability promoted to source qualification / #8 교훈을 source qualification으로 승격.

## 2. Issue #8 Final Result / Issue #8 최종 결과

### `EU-STEEL-R01 — Independent Reproduction of Steel Mercury Intensity / 철강 수은집약도 독립 재현`

**Frozen gate outcome / 고정 게이트:** `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`

### V3 reproduced / V3 재현
- official EEA `F1_3` Hg: **2008 = 4,312.9 kg; 2017 = 3,327.1 kg**.
- official facility-level `F1_4` gives exactly the same frozen-filter totals / facility-level 합계도 정확히 일치.
- historical PRODCOM archive schema and six target T-codes reproduced; 2008 unit = `kg` / historical archive schema·T-code·단위 재현.
- current `DS-059359` dimensions/reporters/indicators/T-codes reproduced / 현행 API 구조 재현.

### Primary-source conflict / 1차 출처 충돌
Current EEA figure CSV distributes: / 현행 EEA figure CSV:
- 2008 = `35.0 g/kt`
- 2017 = `20.5 g/kt`
- direct change = **`-41.4286%`**

The 2019 EEA briefing narrative states **`-36%`**. Cause remains `UNKNOWN`; do not infer revision/rounding without evidence. / 2019 본문 -36%와 충돌하며 원인은 근거 없이 추정하지 않는다.

### Legacy denominator boundary / legacy 분모 경계
- EEA historical denominator source `DS-066342` is discontinued.
- tested current Eurostat COMEXT Statistics API, regular Statistics API and SDMX dataflow return `404 / not available for dissemination`.
- surviving EUROPROMS archives do not contain the required 2017 denominator (`epanntotal-r2` through 2014; `epanntotal` through 2012).
- current `DS-059359` is not silently substituted for historical `DS-066342`.
- `null` reporter values are not treated as zero.

**Interpretation / 해석:** historical `-36%` is not independently reproducible from a complete matched legacy input pair through the currently tested official dissemination paths. This is a reproducibility/data-lineage limitation, **not a falsification** of the historical EEA analysis. / historical matched input 복구 한계이며 과거 EEA 분석의 반증이 아니다.

Detailed result / 상세: `research/EU-STEEL-R01/REPRODUCTION_RESULT.md`

## 3. Methodology Promotion / 방법론 승격

### Metadata Schema v0.3
New first-class lineage fields include: / 신규 1급 계보 필드:
- `snapshot_identifier`
- `snapshot_hash`
- `historical_version_retention`
- `snapshot_recoverability`
- `discontinued_at`
- `replacement_dataset_id`
- `replacement_correspondence_evidence`
- `archive_or_mirror_status`
- `reproduction_risk`

### Gate / 게이트
A live current API/landing page does not prove historical reproducibility. Historical claims require an exact/official archived snapshot or authoritative replacement correspondence before strong validation. / 현재 접근 가능성이 historical 재현성을 증명하지 않으며 exact/official archive 또는 권위 있는 replacement correspondence가 필요하다.

`reproduction_risk` is initially a **gate/modifier**, not a reweighting of the 100-point IPS. / 우선 IPS 재가중이 아닌 게이트·modifier로 운용.

## 4. Persistent Holds / 지속 HOLD
- `C-KR-001` localized/asset attribution — `HOLD`.
- U.S. facility-level data-center energy/cooling/water — `HOLD_DATA_GAP`.
- generic EU facility-level production denominator — `HOLD`.
- historical EEA steel-mercury exact legacy reproduction — `HOLD_LEGACY_VERSION_DIVERGENCE`.

## 5. Next Actions / 다음 행동

1. select the next controlled/reproduction candidate from `registry/RESEARCH_MATERIAL_LANDSCAPE.md` using IPS **plus** the new lineage gate / IPS+lineage gate로 다음 후보 선정;
2. prefer a case with recoverable exact snapshots so the new `reproduction_risk` vocabulary can be calibrated against a second empirical case / exact snapshot 복구 가능한 2차 사례로 보정;
3. do **not** change IPS weights until multiple reproduction cases justify recalibration / 복수 사례 전 IPS 가중치 유지;
4. create the next issue only after freezing target, source crosswalk, snapshot/version provenance, metric and rejection/HOLD criterion / target·crosswalk·snapshot·metric·gate 사전고정 후 다음 Issue 생성.

## 6. Required Session Start / 세션 시작 의무
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → research object → active Issue → claim/decision records`

Apply `READ-001` before material reasoning. / 실질 추론 전 `READ-001` 적용.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
