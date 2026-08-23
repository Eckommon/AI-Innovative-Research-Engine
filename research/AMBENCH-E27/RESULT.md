---
id: AMBENCH-E27-RESULT
type: controlled-experiment-result
state: COMPLETED_HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-E27 Result — Six-Plate Turnaround-Time → Optical Geometry Experiment
# AMBENCH-E27 결과 — 6개 plate Turnaround-Time → Optical Geometry 실험

**Frozen final gate / 고정 최종 판정:** **`HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`**

## 1. Executive result / 핵심 결과

**KO:** E27은 F26에서 확정한 `0.75 ms` 3개 plate(T72/T82/T92) 대 `5.0 ms` 3개 plate(T102/T112/T122)의 condition-level optical geometry 실험을 수치 분석 전에 사전등록했다. 그러나 frozen primary `overlap_depths_avg.csv`와 sensitivity `depths_avg.csv`는 NIST NERDm source identity·size·SHA-256은 정확히 검증되었으나, CSV schema가 physical plate identifier를 보존하지 않는다. 따라서 사전등록된 6개 독립 plate P1 값을 결정론적으로 추출할 수 없으며, E27의 numeric test는 실행하지 않는다.

**EN:** E27 preregistered a condition-level optical-geometry experiment comparing three `0.75 ms` physical plates (T72/T82/T92) against three `5.0 ms` plates (T102/T112/T122) before numerical analysis. The frozen primary `overlap_depths_avg.csv` and sensitivity `depths_avg.csv` have fully verified NIST NERDm identity, size, and SHA-256, but their CSV schemas do not preserve physical-plate identifiers. The preregistered six independent P1 plate values therefore cannot be deterministically extracted, so the E27 numerical test is not executed.

## 2. Immutable source verification / immutable source 검증

Primary:
- `Cross_Sections/Tracks_Results/overlap_depths_avg.csv`
- size `30012` bytes
- SHA-256 `e56c702fba658efd87e99e305ac61d7679d40a855cb331941679d8cdfb66373f`
- local exact size/SHA match: PASS

Sensitivity:
- `Cross_Sections/Tracks_Results/depths_avg.csv`
- size `29879` bytes
- SHA-256 `8d65caae37318ce80392324b7766c0396c004169548054e7d5fce18e090d7a9d`
- local exact size/SHA match: PASS

Correct decoding is `cp1252` for both frozen summaries.

## 3. Schema finding / schema 확인

Primary header has 53 fields and sensitivity has 50. Both begin with condition/location descriptors such as:
- `Powder_Layer_Thickness (µm)`;
- `Turnaround_Time (ms)`;
- `Pad_Width (mm)`;
- `Location (mm)`;
followed by numbered average-measurement fields.

Both contain 103 data rows.

Critically, the corrected bounded preflight found **none** of the six required physical plate identifiers (`T72`, `T82`, `T92`, `T102`, `T112`, `T122`) and therefore no deterministic six-plate P1 mapping.

Supported conclusion: the frozen summary representation is condition/location organized, not a six-physical-plate inference table usable under the preregistered E27 unit contract.

Not claimed: that the broader `mds2-4103` dataset lacks plate-specific information. F26 already established plate-specific P1/P2/P3 components elsewhere in the publication.

## 4. Frozen gate application / 고정 gate 적용

E27 preregistration required all six independent plate-level P1 values to be deterministically identifiable from the frozen source representation before numerical analysis.

That condition failed. Therefore:

**`HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY`**

No reduced-n test, endpoint switching, source substitution, P2/P3 substitution, reconstruction from a different component, or high-capacity model is allowed inside E27.

## 5. Numerical analysis / 수치 분석

Not performed:
- six-plate outcome vector construction;
- group means/medians;
- Δ effect;
- exact 20-allocation permutation test;
- rank-biserial effect;
- sensitivity comparison;
- causal/modeling claim.

## 6. Integrity incident / 무결성 사고

During schema qualification, a parser incorrectly accepted BOM-less bytes as UTF-16 and committed a malformed pseudo-header that contained numerical cells. The current branch tip was redacted without destructive history rewriting, and `AMENDMENT-02.md` records the incident.

Permanent descendant disclosure:

**`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`**

The E27 endpoint, location, directional hypothesis, statistic, and gates were frozen before this incident. No plate mapping or condition-level comparison was performed from the emitted values.

## 7. Decision consequence / 후속 결정

Do not redesign E27 around a different source after seeing schema/data exposure. Close E27 as HOLD.

The next eligible work is a **separate feasibility gate** to determine whether the already identified plate-specific P1 optical components in `mds2-4103` preserve enough non-outcome schema/provenance to reconstruct a valid per-plate geometry endpoint. That gate must be source/schema-only first and must inherit the exposure disclosure above.

## 8. v2.1 overlay / v2.1 overlay

This handling follows `DEC-055`: the affected E27 scope was fail-closed, the incident was persisted, no destructive Git rewrite was performed, and unrelated project mission continuity remains intact. No new Skill/MCP/Plugin is introduced to resolve this local source/schema problem.

## 9. Cost / 비용

Incremental monetary cost: `0 USD`. Raw external data remained transient. No paid/potentially paid route was used.