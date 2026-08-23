---
id: AMBENCH-F22-PART1-RESULT
type: sanitized-byte-inventory-result
state: AMENDED_LIMITED_NUMERICAL_EXPOSURE
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
numerical_outcomes_emitted: true
related:
  - research/AMBENCH-F22/AMENDMENT-01.md
---

# AMBENCH-F22 Part 1 Immutable Byte Result / F22 Part 1 불변 byte 결과

## Integrity / 무결성
- component: `part1.zip`
- NERDm size_bytes: `87041995`
- expected SHA-256: `0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3`
- actual local SHA-256: `0bf229f5a04d181f4c79549fa6357a1bfe3095437b26bb660de5e86b35bb2ec3`
- SHA-256 match: **YES**
- route: public standard GitHub-hosted `ubuntu-latest`
- incremental monetary cost: `0 USD`
- artifact/cache: `NONE`

## Archive inventory / archive inventory
- zip_test: `PASS`
- total_file_members: `250`
- csv_member_count: `250`
- first_csv_member: `part01/L0001.csv`
- last_csv_member: `part01/L0250.csv`
- parsed_unique_layer_count: `250`
- exact_layer_1_250_coverage: `YES`

## Schema-check correction / schema 검사 정정
The workflow assumed the first line of each CSV was a textual header. The files are headerless, so the attempted header check read numerical data instead. The current-facing file intentionally does **not** reproduce those values.

- textual CSV header: **NOT PRESENT / NOT VERIFIED AS HEADER**
- documented schema width from NIST AMS 100-69: `40` columns
- observed attempted first-line field width: `40`, but this is a numerical data row and **must not be reported as a header check PASS**
- all-CSV header identity claim: **WITHDRAWN**
- numerical exposure state: `VIOLATED_LIMITED`
- historical accidental-value exposure occurred in the earlier workflow result commit; see `AMBENCH-F22/AMENDMENT-01.md` for scope and consequences.

## Preserved evidence / 보존 증거
The accidental schema assumption does **not** alter the independently valid evidence for:
- authoritative NERDm component identity;
- exact SHA-256 match;
- valid ZIP structure;
- exactly 250 CSV members;
- exact layer filename coverage `L0001.csv` through `L0250.csv`.

## Boundary / 경계
- No additional CSV content lines are authorized in F22.
- No numerical aggregation, association, feature selection, or modeling was performed.
- raw transient teardown: `SUCCESS`.
