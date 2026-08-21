# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Baseline / 베이스라인:** `v0.4-reproducibility-lineage`  
**Date / 기준일:** 2026-08-22  
**State / 상태:** `RAW_ALIGNMENT_FEASIBILITY_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #11 `AMBENCH-F02`

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

## 2. Active — Issue #11 / 활성 — Issue #11

### `AMBENCH-F02 — Raw Snapshot & Replicate Alignment Feasibility / AM Bench raw snapshot·반복 정렬 검증`

**Objective / 목적:** freeze exact NIST PDR snapshots for AMB2022-03 thermography `mds2-2716` and optical microscopy `mds2-2718`, then determine the highest authoritative alignment resolution between thermography track/repeat identities and optical specimen/cross-section outcomes without speculative pairing. / exact snapshot을 고정하고 추정 없이 가능한 최고 정렬 해상도를 판정한다.

### Why selected / 선정 이유
- `AMBENCH-001` left `replicate_alignment` as its principal unresolved uncertainty.
- Wave 1 synthesis ranks `C-US-004 Registered Manufacturing Quality` as the benchmark-grade next candidate after the KR grid HOLD path.
- This is the second empirical calibration of the new snapshot/version-lineage gate after `EU-STEEL-R01`.

### Frozen sources / 고정 소스
- NIST PDR `mds2-2716` — thermography / 열화상
- NIST PDR `mds2-2718` — optical microscopy / 광학현미경
- official AMB2022-03 benchmark/challenge documentation for experiment semantics only / 실험 의미 해석용 공식 문서

### Frozen gate / 고정 게이트
- `PASS`: authoritative track/repeat-level mapping to optical target identities.
- `PARTIAL`: exact snapshots + authoritative case-level mapping, but no defensible repeat-level one-to-one pairing; downstream work restricted to validated aggregation level.
- `HOLD`: snapshot/identifier semantics unavailable or speculative pairing required.

No post-hoc relaxation after raw inspection. / raw 검사 후 게이트 완화 금지.

## 3. Issue #8 Durable Result / Issue #8 지속 결과

`EU-STEEL-R01` remains `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`:
- EEA frozen Hg numerator V3: 2008 `4,312.9 kg`, 2017 `3,327.1 kg`.
- current EEA figure CSV: `35.0 → 20.5 g/kt = -41.4286%`, conflicting with 2019 narrative `-36%`; cause `UNKNOWN`.
- exact historical `DS-066342` 2017 denominator unavailable through tested current official dissemination paths.
- current replacement data and `null→0` assumptions are not used to force agreement.

Detailed: `research/EU-STEEL-R01/REPRODUCTION_RESULT.md`.

## 4. Active Next Actions / 활성 다음 행동

1. machine-inspect PDR landing/version metadata for `mds2-2716` and `mds2-2718`;
2. retrieve README/update history and distribution manifests;
3. hash accessible metadata/manifests and record snapshot lineage;
4. inspect case/track/repeat/sample naming conventions;
5. build explicit alignment matrix;
6. apply Issue #11 PASS/PARTIAL/HOLD gate;
7. only after gate completion decide whether any raw-level controlled ML experiment is justified.

## 5. Persistent Holds / 지속 HOLD
- KPX localized bus mapping — `HOLD`.
- generic EU facility-level production denominator — `HOLD`.
- historical EEA steel-mercury exact legacy reproduction — `HOLD_LEGACY_VERSION_DIVERGENCE`.

## 6. Required Session Start / 세션 시작 의무
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant MOC → research object → active Issue → claim/decision records`

Apply `READ-001` before material reasoning. / 실질 추론 전 `READ-001` 적용.

Official artifacts comply with `LANG-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and `MEMORY-001`. / 공식 산출물은 관련 규약을 따른다.
