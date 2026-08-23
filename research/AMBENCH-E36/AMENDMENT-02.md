---
id: AMBENCH-E36-AMENDMENT-02
type: post-execution-semantic-correction
state: ACTIVE
created: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-E36/RESULT.md
  - HY-RHF-DataDescription.pdf
---

# AMBENCH-E36 Amendment 02 — Analysis-Result Unit Semantic Correction
# AMBENCH-E36 수정 02 — Analysis-Result 단위 의미 보정

## Event / 사건

The frozen E36 numerical workflow correctly used documented positional columns 5–7 as melt-pool area, length, and width. The generated `RESULT.md` initially labeled the persisted part-level SD values as `px`, following the data-description statement that melt-pool dimensions are in pixels.

After execution, a semantic consistency review found that the raw CSV numerical scale is not safely reconciled with that literal unit label from documentation. The same NIST data-description also documents an 8 µm/pixel camera iFoV and synchronized displays of length/width in physical units, while the analysis CSV itself is headerless and carries no inline unit row.

Therefore the repository must not overstate the exact stored numerical unit.

## Correction / 보정

For E36 durable claims:
- columns 5–7 remain authoritatively identified as melt-pool `area`, `length`, and `width`;
- their persisted numerical values and SDs must be labeled **`source numeric unit`** (or `source-unit`) unless an authoritative file-level unit mapping is independently established;
- do not label the raw analysis CSV values as pixels, mm, µm, mm², or µm² solely by inference.

This is a unit-label semantic correction only.

## Statistical consequence / 통계 결과 영향

**No gate/statistic changes.**

The E36 primary comparison, median difference sign, label-permutation p-value, block signs, and descriptive percentage reduction are invariant to a common positive linear unit conversion within the same endpoint. No row selection, endpoint switch, re-estimation, or outcome-dependent change is introduced.

The gate remains:
`PASS_E36_EXTERNAL_RHF_VARIABILITY_REDUCTION`.

## Claim boundary / 주장 경계

E36 supports lower **source-scale melt-pool-area variability** across the frozen non-selective RHF group relative to baseline within this NIST experiment. Exact physical-unit interpretation of the stored analysis values remains `UNRESOLVED_UNIT_SEMANTICS` unless separately verified from authoritative source evidence.
