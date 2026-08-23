---
id: AMBENCH-F23-RESULT
type: feasibility-result
state: COMPLETED_PASS_HEADERLESS_40_COLUMN_MAPPING_READY
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
related:
  - research/AMBENCH-F23/README.md
  - research/AMBENCH-F23/STRUCTURE_RESULT.md
  - Issue #41
---

# AMBENCH-F23 Result — Headerless Serialization / 40-Column Semantic Mapping
# AMBENCH-F23 결과 — Headerless 직렬화 / 40열 의미 매핑

**Frozen final gate / 고정 최종 판정:** **`PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`**

## 1. Executive result / 핵심 결과

**KO:** NIST AMS 100-69 Section 3.2와 Tables 1–3에서 registered X4 CSV의 위치 기반 40-column 의미 순서를 사전 고정했다. 이후 F22에서 checksum-verified된 네 ZIP을 public standard GitHub-hosted runner에서 transient하게 다시 회수하여 모든 4 parts × 250 layers = 1000 CSV의 모든 non-empty row를 값 비노출 방식으로 검사했다. 총 4,748,352 rows 모두 정확히 40 fields였고 numeric/NaN parse failure는 0, empty row는 0이었다. 각 CSV의 첫 non-empty row 또한 1000/1000 모두 numeric/NaN으로 parse되어 textual header가 없음을 구조적으로 확인했다. 따라서 raw position `1..40` → AMS 100-69 documented semantics의 deterministic parser contract가 준비 상태다.

**EN:** The positional 40-column semantic order for the registered X4 CSVs was frozen prospectively from NIST AMS 100-69 Section 3.2 and Tables 1–3. The four F22 checksum-verified ZIPs were then transiently recovered on a public standard GitHub-hosted runner and all non-empty rows across 4 parts × 250 layers = 1000 CSVs were structurally inspected without emitting numerical values. All 4,748,352 rows contained exactly 40 fields, with zero numeric/NaN parse failures and zero empty rows. The first non-empty row in every one of the 1000 CSVs also parsed as numeric/NaN, structurally confirming there is no textual header. The deterministic parser contract from raw position `1..40` to the documented AMS 100-69 semantics is therefore ready.

## 2. Authoritative positional semantics / 권위 위치 의미론
NIST AMS 100-69 states:
- each registered CSV has 40 columns and multiple rows;
- each row is one measured point with all associated registered features;
- Tables 1–3 define positions 1..40, names, units and definitions.

The frozen mapping in `README.md` covers:
- 1–10: part/time, commanded process and DAQ-derived real process features;
- 11–19: melt-pool length/width/area at thresholds 80/100/120;
- 20–37: LWI pixel features for powder/exposure views, LEDs A/B/C and original/3×3/5×5 filtering;
- 38–40: XCT voxel original, 3×3×3 mean-filtered and 5×5×5 mean-filtered values.

## 3. Immutable-source revalidation / 불변 source 재검증
All four F22/NIST NERDm identities were revalidated before parsing:
- `part1.zip` SHA-256 `0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3` — exact local match;
- `part02.zip` SHA-256 `bf72d9e160d94094f9268fcf3f76a532c8a29fb64aff1afbec20256acaee178e` — exact local match;
- `part03.zip` SHA-256 `89e9e1afadca22b9c34177d82972272a4e73789b19388f0c83d62a9ebd53d878` — exact local match;
- `part04.zip` SHA-256 `6c3f655a1482001119c54d1f1e404a34eb401f386fffc06147628b36c7c8d7c5` — exact local match.

No raw ZIP/CSV was committed, cached or retained as an artifact.

## 4. Full structural verification / 전체 구조 검증

| Archive | CSVs | Non-empty rows | Field-count set | Rows ≠40 | Numeric parse failures | First row numeric/NaN |
|---|---:|---:|---|---:|---:|---:|
| part1 | 250 | 1,187,088 | {40} | 0 | 0 | 250/250 |
| part02 | 250 | 1,187,088 | {40} | 0 | 0 | 250/250 |
| part03 | 250 | 1,187,088 | {40} | 0 | 0 | 250/250 |
| part04 | 250 | 1,187,088 | {40} | 0 | 0 | 250/250 |
| **Total** | **1000** | **4,748,352** | **{40}** | **0** | **0** | **1000/1000** |

This verifies headerless 40-field numeric serialization at full published-dataset row coverage.

## 5. Parser contract / parser contract
The authorized parser contract is now:
1. verify source ZIP SHA-256 first;
2. parse every CSV with `header=None` / no textual header;
3. assign positions 1..40 exactly according to the frozen AMS 100-69 map;
4. preserve hierarchy `row(measured point) ⊂ layer ⊂ part`;
5. do not treat rows, layers or parts as automatically independent statistical replicates;
6. carry documented registration/measurement uncertainty into downstream design.

## 6. Exposure boundary / 사전노출 경계
F23 inherits the F22 disclosure:
**`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`**.

F23 did **not** add numerical-value exposure:
- no raw field values emitted;
- no minima/maxima/distributions;
- no correlations or rankings;
- no feature selection;
- no process↔XCT statistic;
- no model.

Structural counts only were emitted.

## 7. Frozen gate application / 고정 gate 적용
### `PASS_F23_HEADERLESS_40_COLUMN_MAPPING_READY`
- authoritative positions 1..40 frozen: PASS;
- all four immutable hashes revalidated: PASS;
- all 1000 CSVs structurally inspected: PASS;
- every non-empty row exactly 40 fields: PASS;
- all fields numeric/NaN serializable: PASS;
- all first non-empty rows numeric/NaN: PASS;
- additional numerical values emitted: NO;
- deterministic position→semantic map frozen: PASS.

Result: **PASS**.

## 8. Scientific interpretation / 과학적 해석
Supported now:
- exact registered source bytes are reproducible;
- complete headerless serialization contract is reproducible;
- every published data row conforms structurally to the documented 40-feature layout;
- raw positions can be assigned deterministic documented semantics without inspecting outcomes.

Not yet supported:
- any numerical process↔XCT association magnitude;
- prediction performance;
- causal interpretation;
- statistical independence of rows/layers/parts;
- pristine outcome blindness.

## 9. Consequence / 후속
A numerical experiment may now be **designed and preregistered**, but not improvised. The next eligible work is a low-degree-of-freedom registered process/melt-pool ↔ XCT controlled experiment that:
- explicitly inherits `VIOLATED_LIMITED`;
- freezes predictors/outcome/aggregation and split structure before numerical association analysis;
- respects the nested `row ⊂ layer ⊂ part` hierarchy;
- avoids high-capacity ML unless later justified by independent conditions;
- carries NIST registration/measurement uncertainty into interpretation.

## 10. Cost / 비용
Incremental monetary cost: `0 USD`. Public standard GitHub-hosted runners only; no paid API/source, larger runner, artifact storage or cache.