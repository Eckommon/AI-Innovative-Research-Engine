---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
tags:
  - type/memory
  - state/candidate
  - domain/governance
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
---

# Session Handoff / 세션 인수인계

> **Latest operational checkpoint only / 최신 운영 checkpoint 전용**  
> 다음 세션은 이 파일을 읽고 작업을 재개한다. / The next session resumes from this file.

## 1. Current State / 현재 상태

- Issues #1–#4 Wave 0/1 discovery: `COMPLETED`
- Issue #5 `KR-GRID-F01`: `COMPLETED`, `HOLD`
- Issue #6 `EU-IEE-E01`: `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`
- Issue #7 `EU-IEE-F02`: `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`
- Issue #8 `EU-STEEL-R01`: `COMPLETED`, **`HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`**
- Issue #10 `METHOD-001`: methodology hardening completed in this checkpoint / 방법론 보강 완료
- **Project state / 프로젝트 상태:** `READY_FOR_NEXT_CANDIDATE`

## 2. Issue #8 Final Checkpoint / Issue #8 최종 checkpoint

### Frozen result / 고정 결과
- E-PRTR activities: `1.(d)`, `2.(a)`, `2.(b)`
- PRODCOM products: `2410T121-122`, `2410T131-132`, `2410T141-142`
- 2008→2017; EEA-33
- frozen narrative target: `-36%`
- final gate: **`HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`**

### V3 reproduced / V3 재현
- `F1_3` Hg 2008 = **4,312.9 kg**
- `F1_3` Hg 2017 = **3,327.1 kg**
- facility-level `F1_4` yields exactly the same totals
- `epanntotal-r2` schema/T-codes reproduced; 2008 target unit = `kg`
- current `DS-059359` actual dimensions = `freq / reporter / product / indicators / time`
- indicators = `APRODQNT / QNTUNIT / APQNTFLAG / APQNTBASE`

### Material conflict / 핵심 충돌
Current EEA figure CSV: / 현행 EEA figure CSV:
- 2008 = `35.0 g/kt`
- 2017 = `20.5 g/kt`
- direct change = **`-41.4286%`**

EEA 2019 briefing narrative states `-36%`. Cause remains `UNKNOWN`; do not infer revision/rounding. / 본문 -36%와 충돌하며 원인은 추정 금지.

### Legacy boundary / legacy 경계
- historical denominator source = `DS-066342`
- tested current Eurostat COMEXT API, Statistics API and SDMX dataflow all return `404 / not available for dissemination`
- surviving official EUROPROMS `epanntotal-r2` ends 2014; `epanntotal` ends 2012
- current `DS-059359` must not be silently substituted
- `null` must not be converted to zero

Detailed result: `research/EU-STEEL-R01/REPRODUCTION_RESULT.md`
Evidence runs: `32534535674`, `32534683910`, `32534864866`.

## 3. Methodology Promotion / 방법론 승격

Issue #10 `METHOD-001` introduced snapshot/version lineage into source qualification. / source qualification에 snapshot/version 계보를 추가했다.

### New schema / 신규 스키마
`docs/METADATA_SCHEMA.md` = **v0.3**.

Key fields: / 핵심 필드:
- `snapshot_identifier`
- `snapshot_hash`
- `historical_version_retention`
- `snapshot_recoverability`
- `discontinued_at`
- `replacement_dataset_id`
- `replacement_correspondence_evidence`
- `archive_or_mirror_status`
- `reproduction_risk`

`reproduction_risk` is a **gate/modifier**, not yet an IPS reweight. / 아직 IPS 재가중이 아닌 별도 게이트·modifier.

### Controlled rule / 통제 규칙
A current accessible source does not establish historical reproducibility. Require exact/official archive recovery or authoritative replacement correspondence. / 현행 접근 가능성만으로 historical 재현성 인정 금지.

## 4. Exact Next Actions / 정확한 다음 행동

1. read `registry/RESEARCH_MATERIAL_LANDSCAPE.md` and relevant synthesis/MOCs / 연구소재 landscape 재읽기;
2. select the next controlled or reproduction candidate using **IPS + reproduction lineage gate** / IPS+lineage gate로 후보 선정;
3. prefer a case with exact recoverable official snapshots to calibrate `reproduction_risk` against a second case / exact snapshot 가능한 2차 사례 우선;
4. freeze target, crosswalk, snapshots/hashes, metric, tolerance and HOLD criterion before opening the next experiment / 다음 실험 전 사전고정;
5. do not alter IPS weights until multiple lineage/reproduction cases justify recalibration / 복수 사례 전 IPS 재가중 금지.

## 5. Known Holds / 알려진 보류
- KPX localized bus mapping: `HOLD`.
- generic EU facility-level production denominator: `HOLD`.
- EEA steel-mercury exact historical legacy reproduction: `HOLD_LEGACY_VERSION_DIVERGENCE`.

## 6. Mandatory Read Set Next Session / 다음 세션 의무 읽기
1. `README.md`
2. `STATUS.md`
3. `context/PROJECT_MEMORY.md`
4. this file / 본 파일
5. `docs/HALLUCINATION_CONTROL_PROTOCOL.md`
6. `docs/METADATA_SCHEMA.md`
7. `registry/RESEARCH_MATERIAL_LANDSCAPE.md`
8. `registry/CLAIM_LEDGER.md`, `registry/DECISION_LOG.md`
9. `research/EU-STEEL-R01/REPRODUCTION_RESULT.md` when Issue #8 history is material / #8 이력이 필요할 때

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
