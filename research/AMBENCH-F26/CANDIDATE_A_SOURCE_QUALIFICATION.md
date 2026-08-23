---
id: AMBENCH-F26-CANDIDATE-A-SOURCE-QUALIFICATION
type: sanitized-source-qualification
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
numerical_outcome_values_emitted: false
---

# F26 Candidate A — `mds2-3662` source qualification

- route: official NIST public components only
- incremental monetary cost: `0 USD`
- large `Image Data.zip` downloaded: `NO`

- `README.txt`: size_match=YES; SHA256_match=YES; SHA256=e9c33b0b31f7d1548b68041f469e84c6342c974c00e54c387952a24569835918
- `Measurements.xlsx`: size_match=YES; SHA256_match=YES; SHA256=9e21a77f0c526aa0a913a3f14e2bba7b36640b0fd319febcf8ebfdc9dd5d0edf
- `Scan Strategy Data.zip`: size_match=YES; SHA256_match=YES; SHA256=f442f9734a57f59ed33f0ab5e240bb266164740287a184d7ebd7fedece9c2bee

## README semantic-presence checks / README 의미 존재 검증
- term `converging` present: YES
- term `diverging` present: YES
- term `repeat` present: YES
- term `set 2` present: NO
- term `operator` present: YES
- term `outlier` present: NO
- term `width` present: YES
- term `area` present: YES
- term `scan strategy` present: YES

## Workbook schema-only inspection / workbook schema-only 검증
- sheet_count: 1
- sheet_names: ['Sheet1']
- `Sheet1`: max_row=49; max_column=21; first_row_string_schema=['<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>', '<EMPTY>']

## Scan-strategy archive inventory / scan-strategy archive inventory
- zip_test: PASS
- member_count: 3
- member_names: ['Scan Strategy Data/scanStrategyConverging.csv', 'Scan Strategy Data/scanStrategyDiverging.csv', 'Scan Strategy Data/singleTrack.csv']

## Source gate / source 판정
- all_small_component_integrity_pass: YES
- numerical outcome values emitted: `NO`
- raw transient teardown: `SUCCESS`
