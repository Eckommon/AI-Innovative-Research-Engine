---
id: MEM-029-AMBENCH-D11
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/README.md
  - registry/DEC-026.md
---

# MEM-029 — AMBENCH-D11 Temporal-Information Diagnostic / AMBENCH-D11 시간정보 진단

**KO:** F10의 `HOLD_PUBLICATION_NOT_VERIFIED` 이후 immediate fallback은 `AMBENCH-D11`이다. D11은 NIST `mds2-3842` v1.0.3의 21개 BP4 dynamic-coupling waveform에 대해 process-case 지배와 repeat-level 시간정보를 구분한다. 8개 frozen temporal descriptor, normalized-waveform variance decomposition, PCA95 effective dimension을 사용하며 physical outcome utility를 주장하지 않는다. Raw coupling은 E09에서 이미 관측됐으므로 D11은 full outcome-blind가 아니며, D11의 새로운 진단값들은 사전등록 시점에 아직 계산되지 않았다.

**EN:** After F10's `HOLD_PUBLICATION_NOT_VERIFIED`, the immediate fallback is `AMBENCH-D11`. D11 distinguishes process-case dominance from repeat-level temporal information in the 21 BP4 dynamic-coupling waveforms from NIST `mds2-3842` v1.0.3. It uses eight frozen temporal descriptors, normalized-waveform variance decomposition, and PCA95 effective dimension, without claiming physical-outcome utility. Because raw coupling was already observed in E09, D11 is not fully outcome-blind; the new D11 diagnostic values were not yet computed at preregistration.

**State:** `PREREGISTERED / EXECUTION_NOT_YET_RUN`.
