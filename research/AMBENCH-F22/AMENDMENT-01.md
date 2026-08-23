---
id: AMBENCH-F22-AMENDMENT-01
type: preregistration-amendment
state: ACTIVE
created: 2026-08-23
source_of_truth: github
---

# AMBENCH-F22 Amendment 01 — Header Assumption Failure and Limited Numerical Exposure
# AMBENCH-F22 수정 01 — header 가정 실패 및 제한적 numerical 노출

## Trigger / 발생 원인

**KO:** Part 1 byte-verification workflow가 각 CSV의 첫 줄을 header라고 가정했다. 실제 `part01/L0001.csv`에는 textual header가 없었고 첫 줄은 40-field numerical data row였다. 그 결과 workflow sanitized result의 `canonical_header_names` 섹션에 해당 첫 row의 값들이 의도치 않게 기록됐다.

**EN:** The Part 1 byte-verification workflow assumed that the first line of each CSV was a header. `part01/L0001.csv` actually has no textual header; its first line is a 40-field numerical data row. The workflow therefore unintentionally persisted that first row as `canonical_header_names` in the sanitized result.

## Integrity consequence / 무결성 영향
- `NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = YES` is **withdrawn**.
- Replacement state: **`NEW_REGISTERED_X4_NUMERICAL_OUTCOME_BLIND = VIOLATED_LIMITED`**.
- Exposure scope known from the workflow: first line only from each CSV was read for the attempted header check; the persisted values came from the first CSV (`part01/L0001.csv`) because the workflow printed only the first parsed line as the canonical entry.
- No correlations, aggregation, feature selection, ranking, model, or process↔XCT statistic was computed.
- This does not invalidate the SHA-256 match, ZIP validity, 250-member inventory, or layer filename coverage evidence.
- It **does** mean any later numerical experiment using `mds2-3761` cannot be described as fully outcome-blind. Future preregistration must explicitly carry this limited pre-exposure.

## Frozen-gate consequence / frozen gate 영향
The original F22 full gate required a 40-column **header/schema** check. Because the archive CSVs appear headerless, F22 must not silently reinterpret the first data row as a header or weaken the gate after access.

Therefore:
- do not claim the original header check passed;
- do not read additional numerical rows for F22 schema inference;
- use NIST AMS 100-69 as the authoritative 40-column semantic schema source;
- any revised numerical usability gate must be separately preregistered after F22, not retrofitted into the original F22 PASS definition.

## Remediation / 보정
1. Current-facing `PART1_RESULT.md` will be redacted to remove the mistakenly emitted row values while preserving a durable note and the historical commit reference.
2. F22 may continue **source-integrity-only** work (hashes, ZIP validity, filenames/member counts) because those checks are independent of numerical outcome values.
3. No further CSV content lines may be opened in F22.
4. Future experiment documentation must state the exact limited pre-exposure and may not claim pristine outcome blindness.

## Cost / 비용
No monetary cost resulted from this event. Existing zero-cost restrictions remain unchanged.
