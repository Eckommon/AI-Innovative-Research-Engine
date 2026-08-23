---
id: AMBENCH-E27-SCHEMA-PREFLIGHT
type: schema-preflight
created: 2026-08-23
source_of_truth: github-actions
raw_artifacts_committed: false
numerical_outcome_values_emitted: false
exposure_state: VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION
---

# AMBENCH-E27 Corrected Schema Preflight / E27 보정 schema 사전검증

- route: official NIST NERDm + frozen summary components
- incremental monetary cost: 0 USD
- amendment: AMENDMENT-02 bounded encoding/schema parser
- raw data rows emitted: NO
- numerical outcome cells emitted by this corrected run: NO

## NERDm identity / NERDm identity
- version: 1.0.0
- component_count: 552

## primary / primary
- exact_component: FOUND
- filepath: `Cross_Sections/Tracks_Results/overlap_depths_avg.csv`
- NERDm_size: 30012
- NERDm_SHA256: e56c702fba658efd87e99e305ac61d7679d40a855cb331941679d8cdfb66373f
- downloadURL_present: YES
- local_size_match: YES
- local_SHA256_match: YES
- selected_encoding: UNRESOLVED
- schema_parse: HOLD_ENCODING_OR_HEADER_UNRESOLVED

## sensitivity / sensitivity
- exact_component: FOUND
- filepath: `Cross_Sections/Tracks_Results/depths_avg.csv`
- NERDm_size: 29879
- NERDm_SHA256: 8d65caae37318ce80392324b7766c0396c004169548054e7d5fce18e090d7a9d
- downloadURL_present: YES
- local_size_match: YES
- local_SHA256_match: YES
- selected_encoding: UNRESOLVED
- schema_parse: HOLD_ENCODING_OR_HEADER_UNRESOLVED

## Frozen preflight gate / 고정 preflight 판정
**HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY**
- sensitivity_schema_ready: NO
- numerical outcome analysis performed: NO
- raw transient teardown: SUCCESS
