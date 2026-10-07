# US-EPA-RCRA-N01 — Attempt 01

**Disposition:** `HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY`

- Attempt valid: `True`
- Gates passed: **13/18**
- Failed gates: `[6, 7, 8, 11, 15]`
- Later refresh opened: **False**
- Future membership opened: **False**
- Evaluation-result values consumed: **0**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 199, "active_research": "US-EPA-RCRA-N01", "checkpoint_id": "CHK-20261008-US-EPA-RCRA-N01-ACTIVE", "last_completed_issue": 198, "last_completed_research": "US-EPA-RCRA-F01", "last_decision": "DEC-310", "updated": "2026-10-08"}` |
| 2 | PASS | `{"contract_sha": "14b9509808bcfd9a6affc694ec97531105d8ca41", "issue": 199}` |
| 3 | PASS | `{"bytes": 119521531, "expected_sha256": "ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5", "last_modified": "Sun, 04 Oct 2026 13:45:03 GMT", "observed_sha256": "ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5"}` |
| 4 | PASS | `{"evaluation_headers": ["ID_NUMBER", "ACTIVITY_LOCATION", "EVALUATION_IDENTIFIER", "EVALUATION_TYPE", "EVALUATION_DESC", "EVALUATION_AGENCY", "EVALUATION_START_DATE", "FOUND_VIOLATION"], "evaluation_missing": [], "facility_missing": [], "naics_missing": []}` |
| 5 | PASS | `{"evaluation_rows_scanned": 1169946, "forbidden_outcome_tables_opened": 0, "found_column_present": true, "found_values_consumed": 0}` |
| 6 | FAIL | `{"eligible": 23599, "threshold": 100000}` |
| 7 | FAIL | `{"multi_naics_exposed": 2418, "threshold": 20000}` |
| 8 | FAIL | `{"single_naics_controls": 21181, "threshold": 40000}` |
| 9 | PASS | `{"common_exact_strata": 691, "threshold": 200}` |
| 10 | PASS | `{"caliper_fail": 0, "duplicate_controls": 0, "exact_mismatch": 0, "pairs": 1728}` |
| 11 | FAIL | `{"matched_pairs": 1728, "threshold": 20000}` |
| 12 | PASS | `{"coverage": 0.7146401985111662, "eligible_exposed": 2418, "matched_pairs": 1728, "threshold": 0.4}` |
| 13 | PASS | `{"abs_smd_x1": 0.003119556556205712, "threshold": 0.1}` |
| 14 | PASS | `{"abs_smd_x2": 0.0019589799985277223, "threshold": 0.1}` |
| 15 | FAIL | `{"control": 355, "exposed": 348, "recent_opportunity_handlers_total": 703, "threshold_each": 1500, "threshold_total": 5000}` |
| 16 | PASS | `{"future_membership_opened": false, "future_window": "2026-10-05..2027-04-04", "later_refresh_opened": false}` |
| 17 | PASS | `{"causal": false, "found_values_consumed": 0, "identity_repair": false, "prediction": false, "prohibited_exposure": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"baseline_sha256": "ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5", "contract_sha": "14b9509808bcfd9a6affc694ec97531105d8ca41", "cost_usd": 0, "matched_manifest_sha256": "3d71d52d9e3ba05c630f24b0b3f590dd428e4be4968e2afd4b2430553e7fe5a3", "runner_sha256": "314a39bb45f07580aee9b2f5fea907a7aeac51075596b90e62aa5ec1a6a1b2a8"}` |

No later weekly refresh was opened. No evaluation-result value was accessed for N01 matching.
