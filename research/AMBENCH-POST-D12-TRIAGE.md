---
id: AMBENCH-POST-D12-TRIAGE
type: research-triage
state: COMPLETED
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D12/RESULT.md
  - registry/DEC-031.md
---

# Post-D12 External Validation Triage / D12 이후 외부검증 후보 선별

## 1. Decision question / 의사결정 질문

**KO:** D12의 `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION`을 같은 21개 BP4 tracks에서 더 복잡한 feature/model로 확대하지 않고, 가장 직접적으로 외부 검증할 수 있는 authoritative public asset은 무엇인가?

**EN:** Which authoritative public asset most directly enables external validation of D12's `ROBUST_CONDITION_SPECIFIC_REPEAT_VARIATION` without further feature/model escalation on the same 21 BP4 tracks?

## 2. Triage candidates / 후보

### A. NIST A-AMB2022-01 / `mds2-2525` — SELECT
- Public NIST PDR DOI `10.18434/mds2-2525`.
- Current release history reports `v1.3.2` (2026-01-07) as a collection-metadata update; checksum-rich data-bearing `v1.3.1` remains directly documented.
- Integrating-sphere radiometry and high-speed X-ray imaging were acquired simultaneously.
- Ti-6Al-4V training experiments and Al 5182 blind experiments provide material/context independence from BP4 IN718.
- Stationary Al challenge exposes time-dependent absorption and time-dependent melt-pool width result files.
- Scanned Al measurements were repeated three times under identical conditions in the 2024 benchmark publication, but the public PDR component inventory does not clearly expose repeat-resolved Al files as separate authoritative records.
- Therefore this asset is strongest for **external same-experiment physical validation**, but is not yet established as a repeat-resolved replication of D12.

### B. NIST FLaMI reflected-laser metrology — HOLD_PUBLIC_DATASET_NOT_IDENTIFIED
- NIST publicly documents ≥1 MHz total reflected-power / dynamic-coupling capability and high-speed directionally-resolved reflected-power imaging.
- Targeted official search did not establish an exact public PDR dataset/version/manifest suitable for immediate external validation.

### C. BP4 confocal topography — HOLD_PUBLICATION_NOT_VERIFIED
- F10 already established measurement existence but not an exact public publication/version/manifest.

### D. AMB2025 independent-condition coupling — HOLD_PUBLIC_COUPLING_ASSET_NOT_IDENTIFIED
- AMB2025-06/07 public calibration data are available, but targeted official search did not establish a comparable time-resolved dynamic-coupling PDR for those independent conditions.

## 3. Triage conclusion / 결론

**Selected / 선택:** `mds2-2525`.

Why / 이유:
1. different material and experimental context from BP4;
2. time-resolved absorptance is the closest independent analogue to dynamic coupling;
3. simultaneous X-ray provides a qualified physical outcome in the same experiment;
4. public PDR files have explicit checksums and result-file semantics;
5. zero-incremental-cost public access.

Limitation / 한계:
- do not claim D12 repeat-level replication unless repeat-resolved public measurement identity is independently established;
- do not equate integrating-sphere absorptance with BP4 hemispherical-reflectometer coupling as identical measurands;
- do not use numerical Al/Ti64 outcomes before a separate experiment is preregistered.

## 4. Next gate / 다음 gate

Activate `AMBENCH-F13`: source/identity/time-alignment feasibility for `mds2-2525` as an external physical-validation asset.
