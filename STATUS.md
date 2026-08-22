---
checkpoint_id: CHK-20260822-F13-PARTIAL-EXTERNAL-VALIDATION
active_issue: none
active_research: none
last_completed_issue: 31
last_completed_research: AMBENCH-F13
last_decision: DEC-032
updated: 2026-08-22
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**Latest verified baseline label / 최신 검증 baseline:** `v0.16-aamb-external-validation-source-ready-partial`  
**State / 상태:** `F13_COMPLETED__PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`  
**Active Work Queue / 활성 작업 큐:** `none` — next experiment requires a new preregistration before numerical `mds2-2525` result access.

## Mandatory Governance / 필수 거버넌스
- GitHub = persistent Source of Truth.
- `COST-001` + `DEC-028`: any potentially billable action requires explicit user approval **before execution**; post-hoc reporting is not authorization; unknown billing = `HOLD_COST_APPROVAL`.
- `RAW-001`: authoritative external raw bytes are transient-only.
- `READ-001`, `STATE-001`, `CHECKPOINT-001`, `FACT-001`, `UNKNOWN-001`, `CONFLICT-001`, `FRESH-001`, `MEMORY-001`, `WRITEBACK-001` remain mandatory.

## Completed AMBENCH Chain / 완료 계보
- #11 F02 — `PASS`
- #13 E03 — `NO_MATERIAL_GAIN`
- #15 F04 — `PARTIAL`
- #17 E05 — `MIXED`
- #19 D06 — `PROCESS_CASE_PROXY_DOMINANT`
- #21 F07 — `PARTIAL_SOURCE_READY`
- #22 F08 — `PARTIAL_CASE_LEVEL_READY`
- #24 E09 — `INCONCLUSIVE_CASE_LEVEL`
- #26 F10 — `HOLD_PUBLICATION_NOT_VERIFIED`
- #27 D11 — `MIXED_TEMPORAL_INFORMATION`
- #29 D12 — `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`
- #31 F13 — **`PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`**

## F13 Final / F13 최종
**Result:** `research/AMBENCH-F13/RESULT.md`.  
**Amendment:** `research/AMBENCH-F13/AMENDMENT-01.md`.  
**Claims:** `CLM-048..050`.  
**Decisions:** `DEC-031..032`.  
**Memory:** `MEM-033-AMBENCH-F13-RESULT`.

### Source-readiness result / source 준비도
- NIST A-AMB2022-01 DOI `10.18434/mds2-2525` selected as strongest post-D12 external-validation asset.
- Checksum-rich data-bearing snapshot `v1.3.1`; release history reports `v1.3.2` (2026-01-07) as an `additiveman` collection metadata update.
- Material/experiment context is independent of BP4 IN718.
- Official documentation establishes simultaneous integrating-sphere absorptance + high-speed X-ray melt-pool acquisition.
- Public stationary-Al components include time-dependent absorption and time-dependent melt-pool width with explicit checksums.
- 2024 benchmark publication reports repeated measurements, including three repeated scanned-Al experiments under identical conditions.
- Public PDR component inventory does **not** establish >=3 separately identifiable repeat-level absorptance + geometry event pairs for direct D12 replication.

### Outcome-blindness integrity / outcome-blindness 무결성
F13 `AMENDMENT-01` corrects the original statement to:
`NEW_EXTERNAL_OUTCOME_BLIND = NO — PUBLICATION_LEVEL_AGGREGATES_PREOBSERVED`.
Publication-level aggregate scanned-Al geometry values were visible during triage before preregistration. No numerical PDR CSV outcome was downloaded/analyzed and those aggregates were not used in the F13 gate.

### Frozen gate / 고정 판정
**`PARTIAL_SAME_EXPERIMENT_EXTERNAL_VALIDATION_READY`**.

## Exact Next Action / 정확한 다음 행동
No experiment is active.

The next eligible research step is a **new separately preregistered low-degree-of-freedom A-AMB aluminum stationary-spot time-resolved absorptance ↔ time-dependent melt-pool-width external physical-validation experiment**.

Before any numerical PDR result access, freeze:
1. exact source snapshot/checksums;
2. time-zero and alignment rules;
3. resampling resolution;
4. absorptance normalization;
5. a very small descriptor-transfer set derived from D11/D12 without tuning;
6. geometry endpoint transform;
7. exact statistics/null/gates;
8. protections against preobserved publication-level aggregate scan values.

This future experiment is **same-experiment external physical validation**, not repeat-level D12 generalization. No high-capacity model is authorized.

## Persistent Holds / 지속 HOLD
- same-BP4 confocal: `HOLD_PUBLICATION_NOT_VERIFIED`;
- BP1↔BP4 physical repeat pairing: prohibited;
- AMB2025-07 predictive thermal↔geometry: HOLD pending public thermography source;
- independent-condition FLaMI dynamic-coupling PDR: exact public dataset not yet verified.
