# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Baseline / 베이스라인:** `v0.7-thermal-dynamics-feasibility`  
**Date / 기준일:** 2026-08-22  
**State / 상태:** `CALIBRATED_THERMAL_DYNAMICS_FEASIBILITY_ACTIVE`  
**Active Work Queue / 활성 작업 큐:** Issue #15 `AMBENCH-F04`

## 1. Mandatory Governance / 필수 거버넌스

- GitHub = persistent Source of Truth / 지속 기준 저장소.
- `COST-001` = **zero incremental monetary cost by default** / 추가 금전비용 0원 기본.
- Any action that incurs or may reasonably incur monetary cost requires explicit user approval **before execution**. / 비용 발생·발생 가능 작업은 실행 전 사용자 명시승인 필수.
- Unknown billing state = `HOLD_COST_APPROVAL`; no silent paid substitution. / 비용상태 불명확 시 HOLD.
- Prefer existing artifacts, official public sources, repository evidence, and zero-cost analysis over new metered automation. / 기존 artifact·공식 공개자료·무비용 분석 우선.
- `LANG-001`, `READ-001`, evidence/provenance and hallucination-control rules remain mandatory.

Detailed: `docs/NO_COST_POLICY.md`; `DEC-013`.

## 2. Completed / 완료

- Issues #1–#4 Wave 0/1 initial queue — `COMPLETED`.
- Issue #5 `KR-GRID-F01` — `COMPLETED`, `HOLD`.
- Issue #6 `EU-IEE-E01` — `COMPLETED`, empirical `VALIDATED`, novelty `LOW / NOT NOVEL`.
- Issue #7 `EU-IEE-F02` — `COMPLETED`, `PASS_SECTOR_AGGREGATE / HOLD_FACILITY_DENOMINATOR`.
- Issue #8 `EU-STEEL-R01` — `COMPLETED`, `HOLD / INCONCLUSIVE_LEGACY_VERSION_DIVERGENCE`.
- Issue #10 `METHOD-001` — `COMPLETED`, snapshot recoverability promoted into source qualification.
- Issue #11 `AMBENCH-F02` — `COMPLETED — PASS`, exact 21-track/repeat alignment.
- Issue #13 `AMBENCH-E03` — `COMPLETED — NO_MATERIAL_GAIN`.

## 3. E03 Negative Calibration / E03 음성 보정

Frozen 21-track process-case LOCO result: / 고정 21-track LOCO
- depth: Process RMSE `19.6406 µm` vs Combined `23.4295 µm` → `-19.2914%`
- width: Process RMSE `14.1639 µm` vs Combined `17.1620 µm` → `-21.1668%`
- gate: `NO_MATERIAL_GAIN`

Do not tune E03 post hoc. / E03 사후 tuning 금지.

## 4. Active Issue #15 — AMBENCH-F04 / 활성 Issue #15

**Objective / 목적:** determine whether the frozen AMB2022-03 thermography can support a deterministic, physically calibrated track-level temporal representation without optical-outcome tuning. / optical outcome tuning 없이 물리 보정된 track-level 시간표현 재현 가능성 검증.

Validated official/raw facts: / 검증 사실
- exact frozen HDF5 SHA-256: `f6fe21ec911707f72e7efda2932c77eae2b75d84765848878fe5beb6b728cd43`;
- 21 track groups, each `700 × 640 × 304`, 30,000 fps;
- source threshold metadata `100 DL`, zeroed below threshold;
- NIST HDF5 `/Calibration/ThermalCal` explicitly stores `Model`, `Model_input`, `Model_output`, coefficients and calibration quality;
- v1.3.1 metadata note states the calibration `Model` equation was corrected on 2024-09-12;
- `Coeff_a=0.9655`, `Coeff_b=197.2`, `Coeff_c=43920000`, `R-square=0.9988`, `RMSE=4.923`;
- `Model_input = Signal [DL]`, `Model_output = Emissivity-Corrected Temperature [°C]`;
- TSCR/TLCR/TTAM official result table is seven case-level averages over three tracks, not 21 repeat-level labels.

Current unresolved gate item / 현재 미확인:
- exact full `Model` expression semantics, especially the emissivity term `e`, its source/rule/domain, and whether the official 21-track transformation can be implemented without unsupported assumptions.

## 5. F04 Frozen Gate / F04 고정 게이트

- `PASS`: exact equation/units/domain + deterministic all-21-track implementation + outcome-blind calibrated temporal feature manifest.
- `PARTIAL`: calibration works but cooling-rate/transition quantities retain documented-but-incomplete algorithm/emissivity/aggregation ambiguity.
- `HOLD`: required semantics cannot be implemented without unsupported assumptions.

## 6. Exact Next Action / 정확한 다음 행동

Under `COST-001`, do **not** trigger additional metered CI merely for convenience. / 편의를 위한 추가 metered CI 금지.

1. recover exact emissivity/calibration semantics from already-existing NIST metadata, prior workflow artifacts/logs, and official public NIST documents;
2. determine whether `e` is globally defined, derived per case/track, or dependent on apparent solidification temperature;
3. reconstruct only those calibrated temporal quantities whose rules are fully authoritative;
4. compare correct case-level aggregates against official TTAM/TSCR/TLCR where methodologically permissible;
5. assign `PASS / PARTIAL / HOLD` without optical-outcome tuning.

Detailed: Issue #15; `research/AMBENCH-F04/README.md`; `research/AMBENCH-NEXT-TRIAGE.md`.

## 7. Persistent Holds / 지속 HOLD
- KPX localized bus mapping — `HOLD`.
- generic EU facility-level production denominator — `HOLD`.
- historical EEA steel-mercury exact legacy reproduction — `HOLD_LEGACY_VERSION_DIVERGENCE`.

## 8. Required Session Start / 세션 시작 의무
`README.md → STATUS.md → context/PROJECT_MEMORY.md → context/SESSION_HANDOFF.md → relevant research object → active Issue → claim/decision records`

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `FACT-001`, `UNKNOWN-001`, `FRESH-001`, and `MEMORY-001`. / 관련 규약 준수.
