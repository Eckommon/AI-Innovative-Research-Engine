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
- selected_encoding: cp1252
- header_field_count: 53
- bounded_header_fields: ['Powder_Layer_Thickness (µm)', 'Turnaround_Time (ms)', 'Pad_Width (mm)', 'Location (mm)', '1 Avg. (µm)', '2 Avg. (µm)', '3 Avg. (µm)', '4 Avg. (µm)', '5 Avg. (µm)', '6 Avg. (µm)', '7 Avg. (µm)', '8 Avg. (µm)', '9 Avg. (µm)', '10 Avg. (µm)', '11 Avg. (µm)', '12 Avg. (µm)', '13 Avg. (µm)', '14 Avg. (µm)', '15 Avg. (µm)', '16 Avg. (µm)', '17 Avg. (µm)', '18 Avg. (µm)', '19 Avg. (µm)', '20 Avg. (µm)', '21 Avg. (µm)', '22 Avg. (µm)', '23 Avg. (µm)', '24 Avg. (µm)', '25 Avg. (µm)', '26 Avg. (µm)', '27 Avg. (µm)', '28 Avg. (µm)', '29 Avg. (µm)', '30 Avg. (µm)', '31 Avg. (µm)', '32 Avg. (µm)', '33 Avg. (µm)', '34 Avg. (µm)', '35 Avg. (µm)', '36 Avg. (µm)', '37 Avg. (µm)', '38 Avg. (µm)', '39 Avg. (µm)', '40 Avg. (µm)', '41 Avg. (µm)', '42 Avg. (µm)', '43 Avg. (µm)', '44 Avg. (µm)', '45 Avg. (µm)', '', '', '', '']
- data_row_count: 103
- six_plate_identifier_presence: {'T72': False, 'T82': False, 'T92': False, 'T102': False, 'T112': False, 'T122': False}
- six_plate_P1_identifier_presence: {'T72': False, 'T82': False, 'T92': False, 'T102': False, 'T112': False, 'T122': False}
- all_six_plate_identifiers_present: NO
- all_six_P1_identifiers_present: NO

## sensitivity / sensitivity
- exact_component: FOUND
- filepath: `Cross_Sections/Tracks_Results/depths_avg.csv`
- NERDm_size: 29879
- NERDm_SHA256: 8d65caae37318ce80392324b7766c0396c004169548054e7d5fce18e090d7a9d
- downloadURL_present: YES
- local_size_match: YES
- local_SHA256_match: YES
- selected_encoding: cp1252
- header_field_count: 50
- bounded_header_fields: ['Powder_Layer_Thickness (µm)', 'Turnaround_Time (ms)', 'Pad_Width (mm)', 'Location (mm)', '1 Avg. (µm)', '2 Avg. (µm)', '3 Avg. (µm)', '4 Avg. (µm)', '5 Avg. (µm)', '6 Avg. (µm)', '7 Avg. (µm)', '8 Avg. (µm)', '9 Avg. (µm)', '10 Avg. (µm)', '11 Avg. (µm)', '12 Avg. (µm)', '13 Avg. (µm)', '14 Avg. (µm)', '15 Avg. (µm)', '16 Avg. (µm)', '17 Avg. (µm)', '18 Avg. (µm)', '19 Avg. (µm)', '20 Avg. (µm)', '21 Avg. (µm)', '22 Avg. (µm)', '23 Avg. (µm)', '24 Avg. (µm)', '25 Avg. (µm)', '26 Avg. (µm)', '27 Avg. (µm)', '28 Avg. (µm)', '29 Avg. (µm)', '30 Avg. (µm)', '31 Avg. (µm)', '32 Avg. (µm)', '33 Avg. (µm)', '34 Avg. (µm)', '35 Avg. (µm)', '36 Avg. (µm)', '37 Avg. (µm)', '38 Avg. (µm)', '39 Avg. (µm)', '40 Avg. (µm)', '41 Avg. (µm)', '42 Avg. (µm)', '43 Avg. (µm)', '44 Avg. (µm)', '45 Avg. (µm)', '']
- data_row_count: 103
- six_plate_identifier_presence: {'T72': False, 'T82': False, 'T92': False, 'T102': False, 'T112': False, 'T122': False}
- six_plate_P1_identifier_presence: {'T72': False, 'T82': False, 'T92': False, 'T102': False, 'T112': False, 'T122': False}
- all_six_plate_identifiers_present: NO
- all_six_P1_identifiers_present: NO

## Frozen preflight gate / 고정 preflight 판정
**HOLD_E27_SOURCE_OR_SCHEMA_INTEGRITY**
- sensitivity_schema_ready: NO
- numerical outcome analysis performed: NO
- raw transient teardown: SUCCESS
