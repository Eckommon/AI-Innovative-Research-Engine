---
checkpoint_id: CHK-20260822-E09-PREREG
active_issue: 24
active_research: AMBENCH-E09
last_completed_issue: 22
last_completed_research: AMBENCH-F08
last_decision: DEC-021
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline label / 최신 검증 baseline:** `v0.8-unpaired-coupling-preregistration`  
**State / 상태:** `E09_PREREGISTERED__COUPLING_OUTCOME_NOT_ACCESSED`  
**Active Work Queue / 활성 작업 큐:** Issue #24 `AMBENCH-E09`

## 1. Governance / 거버넌스

- GitHub = persistent Source of Truth.
- `READ-001` + `STATE-001` + synchronized checkpoint remain mandatory.
- `COST-001`: zero incremental monetary cost only unless the user explicitly approves otherwise.
- `UNKNOWN-001` / `CONFLICT-001`: unresolved identifiers and provenance are not silently repaired.
- `WRITEBACK-001`: material work requires durable research/Issue/decision/status/handoff persistence.

## 2. Completed Chain / 완료 계보

- #11 `AMBENCH-F02` — `PASS` track/repeat alignment inside BP1 thermography↔optical.
- #13 `AMBENCH-E03` — `NO_MATERIAL_GAIN`.
- #15 `AMBENCH-F04` — `PARTIAL`.
- #17 `AMBENCH-E05` — `MIXED`.
- #19 `AMBENCH-D06` — `PROCESS_CASE_PROXY_DOMINANT`.
- #21 `AMBENCH-F07` — `PARTIAL_SOURCE_READY`.
- #22 `AMBENCH-F08` — `PARTIAL_CASE_LEVEL_READY`.

## 3. Active E09 / 활성 E09

**Scientific question / 과학적 질문:** Does BP4 dynamic coupling alter BP4 process-energy case ordering so that it corresponds to BP1 thermal-response ordering better than BP4 process-only VED ordering, while preserving the fact that BP1 and BP4 are separate specimens? / BP1·BP4가 별도 specimen이라는 경계를 유지한 채 coupling 정보가 process-only ordering보다 BP1 thermal case ordering과 더 잘 대응하는지 검증.

**Cross-BP unit / 비교 단위:** `UNPAIRED_NOMINAL_CASE_FAMILY / AGGREGATE_ONLY`.  
No physical-track/repeat pairing is authorized. / track·repeat pairing 금지.

### Outcome-blindness / outcome 비사용
- `NEW_MODALITY_OUTCOME_BLIND = YES`: BP4 coupling values have not been accessed before preregistration.
- `FULL_OUTCOME_BLIND = NO — BP1_PREOBSERVED`: BP1 outcomes were previously observed in E03/E05/D06 and this is explicitly recorded.

### Frozen predictor / 고정 predictor
- `X_process(case) = official BP4 VEDσ/VED0`.
- BP4 track coupling `C_track` = median instantaneous coupling over normalized record time `τ ∈ [0.20,0.80]`, no smoothing/manual crop.
- `C_case` = median across unique authoritative BP4 track files.
- `X_coupled(case) = X_process(case) × [C_case/C_case0]`.
- Coupling remains an approximation of absorption, not exact absorbed energy.

### Frozen BP1 endpoints / 고정 BP1 endpoint
- primary: case median of existing E05 `hot_pixel_time_integral_1298C_px_s`;
- sensitivity: `any_hot_duration_1298C_s`;
- secondary geometry: both track-level mean width and mean depth, case-median aggregated; width/depth always reported together.

### Frozen primary statistic / 고정 1차 통계
- `rho_process = Spearman(X_process,Y_thermal)`;
- `rho_coupled = Spearman(X_coupled,Y_thermal)`;
- `delta_rho_thermal = rho_coupled - rho_process`.

Factor-axis sign checks / 공정축 부호검사:
- spot `1.1 - 1.2`;
- speed `2.2 - 2.1`;
- power `3.1 - 3.2`.

### Full positive gate / full 양성 gate
`CROSS_MODAL_ORDERING_SIGNAL` requires all:
1. 7 analyzable case families;
2. `rho_coupled >= 0.70`;
3. `delta_rho_thermal >= +0.20`;
4. thermal axis concordance `3/3`;
5. no integrity failure.

Other frozen final outcomes:
- `PARTIAL_CROSS_MODAL_SIGNAL`;
- `PROCESS_ONLY_OR_REDUNDANT_AT_CASE_LEVEL`;
- `NO_COHERENT_CROSS_MODAL_RELATIONSHIP`;
- `MIXED_ENDPOINT_SPECIFIC`;
- `HOLD_DATA_INTEGRITY`.

Detailed preregistration: `research/AMBENCH-E09/README.md`.  
Direction decision: `registry/DEC-021.md`.  
Supplemental durable memory: `context/MEM-024-AMBENCH-E09.md`.

## 4. Integrity Constraints / 무결성 제약

- same case label ≠ identical BP1/BP4 process condition;
- official NIST parameter vectors remain explicit: BP1 spot family `67/49/82 µm`; BP4 `110/76/131 µm`;
- case `3.2` third-repeat filename is not silently corrected;
- after outcome download, filename-only archive preflight occurs before numeric coupling read;
- if `3.2` remains partial, use verified unique files only and run mandatory sensitivity excluding `3.2`;
- fewer than 6 analyzable case families => `HOLD_DATA_INTEGRITY`;
- unresolved `Ra=0.15 µm` vs `5.8 µm` conflict means surface roughness is excluded from harmonized covariates;
- no causal mediation, paired-sensor, high-capacity model, or deployable prediction claim is authorized in E09.

## 5. Exact Next Action / 정확한 다음 행동

E09 is preregistered; scientific execution has **not** started. / 과학적 실행 전 상태.

Next execution order:
1. reverify exact frozen PDR versions/checksums;
2. confirm `COST-001` zero-cost path;
3. download the ~94 kB `mds2-3842` ZIP;
4. perform filename-only `3.2` identity preflight before numeric values;
5. extract frozen coupling descriptors;
6. recover frozen BP1 case-level endpoints without changing definitions;
7. calculate rank statistics, axis concordance and exact permutation reference;
8. apply exactly one frozen gate;
9. write `RESULT.md`, evidence/decision records, close or continue Issue #24, and synchronize checkpoint.

## 6. Persistent Holds / 지속 HOLD

- BP1↔BP4 direct track/repeat join — `NOT_AUTHORIZED`.
- case `3.2` BP4 third-repeat identity — `CONFLICT / UNKNOWN` until direct archive evidence.
- harmonized BP4 surface roughness — `ACTIVE_SOURCE_CONFLICT`.
- AMB2025-07 predictive thermal↔geometry experiment — `HOLD` pending version-identifiable thermography publication.
- historical 2022 exact TTAM/TSCR/TLCR reproduction — `PARTIAL`.

## 7. Required Session Start / 세션 시작 의무

`live GitHub state → README → STATUS → PROJECT_MEMORY → SESSION_HANDOFF → research/AMBENCH-E09/README.md → Issue #24 → DEC-021 → F08 RESULT → claim/decision records → governance/cost files → STATE-001 reconciliation`

Official artifacts comply with `LANG-001`, `COST-001`, `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `MEMORY-001`, and `WRITEBACK-001`. / 관련 규약 준수.