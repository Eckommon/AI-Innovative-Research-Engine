---
checkpoint_id: CHK-20260822-D11-PREREG
active_issue: 27
active_research: AMBENCH-D11
last_completed_issue: 26
last_completed_research: AMBENCH-F10
last_decision: DEC-026
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline label / 최신 검증 baseline:** `v0.12-bp4-coupling-temporal-diagnostic-prereg`  
**State / 상태:** `D11_PREREGISTERED__EXECUTION_NOT_YET_RUN`  
**Active Work Queue / 활성 작업 큐:** Issue #27 `AMBENCH-D11`

## 1. Mandatory Governance / 필수 거버넌스

- GitHub = persistent Source of Truth.
- `READ-001` + `STATE-001` + `CHECKPOINT-001` mandatory before material work.
- `COST-001`: zero incremental monetary cost by default.
- `RAW-001`: authoritative external raw data are `RAW_DATA_TRANSIENT_ONLY`.
- `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.

## 2. Completed AMBENCH Chain / 완료 계보

- #11 `AMBENCH-F02` — `PASS`.
- #13 `AMBENCH-E03` — `NO_MATERIAL_GAIN`.
- #15 `AMBENCH-F04` — `PARTIAL`.
- #17 `AMBENCH-E05` — `MIXED`.
- #19 `AMBENCH-D06` — `PROCESS_CASE_PROXY_DOMINANT`.
- #21 `AMBENCH-F07` — `PARTIAL_SOURCE_READY`.
- #22 `AMBENCH-F08` — `PARTIAL_CASE_LEVEL_READY`.
- #24 `AMBENCH-E09` — `INCONCLUSIVE_CASE_LEVEL`.
- #26 `AMBENCH-F10` — `HOLD_PUBLICATION_NOT_VERIFIED`.

## 3. Active D11 / 활성 D11

**Purpose / 목적:** determine whether the 21 BP4 dynamic-coupling waveforms preserve repeat-level temporal information beyond process-case labels, without claiming physical-outcome utility. / 21개 BP4 coupling waveform이 case label을 넘어 repeat 수준 시간정보를 보존하는지 진단.

**Frozen source:** NIST `mds2-3842` v1.0.3; ZIP `93,566 B`; SHA-256 `8c4278eb621c1638465e13e87339fe0daba1dcae138f24b9c1d86c186cd74f66`; 21 authoritative tracks.

**Prior-observation boundary / 기존 관측 경계:**
- `RAW_COUPLING_PREOBSERVED = YES` — E09 already read the coupling time series.
- `NEW_D11_TEMPORAL_DIAGNOSTICS_UNCOMPUTED_AT_PREREG = YES`.
- D11 is not described as fully outcome-blind.

**Frozen diagnostics / 고정 진단:**
1. exactly eight robust temporal descriptors;
2. descriptor repeat-vs-case variance decomposition;
3. normalized waveform variance on `tau=0.050..0.950`, 901 points;
4. descriptor PCA / `PCA95_DIM`;
5. seven-case process association as descriptive-only secondary analysis.

**Frozen final gates / 고정 판정:**
- `COUPLING_PROCESS_CASE_PROXY_DOMINANT`;
- `REPEAT_LEVEL_TEMPORAL_INFORMATION_PRESENT`;
- `MIXED_TEMPORAL_INFORMATION`;
- `HOLD_DATA_INTEGRITY`.

**No-post-hoc / 사후변경 금지:** no descriptor/window/threshold changes, smoothing rescue, FFT/wavelet/neural expansion, BP1 outcome substitution, or physical-utility claim inside D11.

Records / 기록:
- `research/AMBENCH-D11/README.md`
- `research/AMBENCH-D11/WORK_QUEUE.md`
- Issue #27
- `registry/DEC-026.md`
- `registry/CLM-040.md`
- `context/MEM-029-AMBENCH-D11.md`

## 4. Exact Next Action / 정확한 다음 행동

Execute D11 under the frozen preregistration:
1. transiently download exact `mds2-3842` v1.0.3 coupling ZIP;
2. verify byte size/checksum and all 21 file identities;
3. compute the eight frozen temporal descriptors;
4. compute descriptor and normalized-waveform case-vs-repeat variance diagnostics;
5. compute descriptor `PCA95_DIM` and descriptive process associations;
6. apply exactly one frozen D11 gate;
7. write `RESULT.md`, claim/decision records, close/update Issue #27, synchronize STATUS/HANDOFF;
8. persist no raw source bytes or raw-data Actions artifact.

Execution must remain zero-cost under `COST-001`. / 실행은 추가 금전비용 0원 경로만 허용.

## 5. Persistent Holds / 지속 HOLD

- same-BP4 confocal analysis — `HOLD_PUBLICATION_NOT_VERIFIED`;
- BP1↔BP4 physical track/repeat pairing — `NOT_AUTHORIZED`;
- BP4 roughness harmonization — `ACTIVE_SOURCE_CONFLICT`;
- AMB2025-07 predictive thermal↔geometry — HOLD pending public thermography source;
- prior other project HOLDs remain unchanged.
