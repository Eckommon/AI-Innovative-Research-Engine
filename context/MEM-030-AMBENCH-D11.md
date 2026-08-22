---
id: MEM-030-AMBENCH-D11
type: memory
state: ACTIVE
created: 2026-08-22
updated: 2026-08-22
source_of_truth: github
related:
  - research/AMBENCH-D11/RESULT.md
  - registry/DEC-027.md
---

# MEM-030 — AMBENCH-D11 Mixed Temporal Information / AMBENCH-D11 혼합 시간정보

**KO:** Issue #27 `AMBENCH-D11`은 `MIXED_TEMPORAL_INFORMATION`이다. exact NIST `mds2-3842` v1.0.3의 21개 BP4 coupling waveform에서 direct normalized waveform은 `WF_MEDIAN_WITHIN=0.0043387546`, `WF_HIGH_REPEAT_FRACTION=0.0`으로 강하게 case-structured였지만, frozen temporal descriptor는 `5/8 REPEAT_INFORMATIVE`, `2/8 CASE_DOMINATED`, `1/8 MIXED_VARIATION`이고 `PCA95_DIM=6`이었다. 이는 physical utility/predictive signal의 증거가 아니며, repeat-sensitive descriptor가 temporal morphology인지 measurement/noise/instability인지 별도 검증 전 승격하지 않는다.

**EN:** Issue #27 `AMBENCH-D11` resolves to `MIXED_TEMPORAL_INFORMATION`. Across the 21 BP4 coupling waveforms from exact NIST `mds2-3842` v1.0.3, the direct normalized waveform was strongly case-structured (`WF_MEDIAN_WITHIN=0.0043387546`, `WF_HIGH_REPEAT_FRACTION=0.0`), while frozen temporal descriptors were `5/8 REPEAT_INFORMATIVE`, `2/8 CASE_DOMINATED`, and `1/8 MIXED_VARIATION`, with `PCA95_DIM=6`. This is not evidence of physical utility or predictive signal; repeat-sensitive descriptors must not be promoted until separately tested as temporal morphology versus measurement/noise/instability.

**Source:** Run `32553063163`, Job `96982816961`; `research/AMBENCH-D11/RESULT.md`; `DEC-027`.
