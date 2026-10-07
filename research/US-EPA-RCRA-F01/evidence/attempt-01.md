# US-EPA-RCRA-F01 — Attempt 01

**Disposition:** `PASS_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_READY`

- Attempt valid: `True`
- Gates passed: **18/18**
- Failed gates: `[]`
- Later refresh opened: **False**
- Future evaluation violation membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 198, "active_research": "US-EPA-RCRA-F01", "checkpoint_id": "CHK-20261008-US-EPA-RCRA-F01-ACTIVE", "last_completed_issue": 197, "last_completed_research": "PORTFOLIO-R55", "last_decision": "DEC-308", "updated": "2026-10-08"}` |
| 2 | PASS | `{"contract_sha": "ffbb1d89ea614c4c82cc39483383ccb09e23accf", "issue": 198}` |
| 3 | PASS | `{"dictionary": {"bytes": 95310, "content_type": "text/html; charset=UTF-8", "etag": null, "final_url": "https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary", "last_modified": null, "requested_url": "https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary", "sha256": "edf0f9e759cbf883226041dca9cd169b88e4e94acc92493e803421b2471b591d", "status": 200}, "downloads": {"bytes": 99708, "content_type": "text/html; charset=UTF-8", "etag": null, "final_url": "https://echo.epa.gov/tools/data-downloads", "last_modified": null, "requested_url": "https://echo.epa.gov/tools/data-downloads", "sha256": "24fdaf2be6c6ff8a61803184f43f931cfc2cd0a4e1ef75c28478ed16953b91af", "status": 200}}` |
| 4 | PASS | `{"bytes": 119521531, "content_length_header": "119521531", "content_type": "application/zip", "etag": "\"71fc0fb-65d03f8fc7a43\"", "final_url": "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip", "last_modified": "Sun, 04 Oct 2026 13:45:03 GMT", "requested_url": "https://echo.epa.gov/files/echodownloads/rcra_downloads.zip", "sha256": "ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5", "status": 200, "zip_valid": true}` |
| 5 | PASS | `{"present": ["RCRA_ENFORCEMENTS.CSV", "RCRA_EVALUATIONS.CSV", "RCRA_FACILITIES.CSV", "RCRA_NAICS.CSV", "RCRA_VIOLATIONS.CSV", "RCRA_VIOSNC_HISTORY.CSV"], "required": ["RCRA_ENFORCEMENTS.CSV", "RCRA_EVALUATIONS.CSV", "RCRA_FACILITIES.CSV", "RCRA_NAICS.CSV", "RCRA_VIOLATIONS.CSV", "RCRA_VIOSNC_HISTORY.CSV"]}` |
| 6 | PASS | `{"headers": ["ID_NUMBER", "FACILITY_NAME", "ACTIVITY_LOCATION", "FULL_ENFORCEMENT", "HREPORT_UNIVERSE_RECORD", "STREET_ADDRESS", "CITY_NAME", "STATE_CODE", "ZIP_CODE", "LATITUDE83", "LONGITUDE83", "FED_WASTE_GENERATOR", "TRANSPORTER", "ACTIVE_SITE", "OPERATING_TSDF"], "missing": []}` |
| 7 | PASS | `{"facility_rows": 1627579, "id_nonblank": 1627579, "id_rate": 0.9999993855904997, "id_valid": 1627578, "loc_nonblank": 1627579, "loc_rate": 1.0, "loc_valid": 1627579}` |
| 8 | PASS | `{"distinct_exact_handler_keys": 1627578, "threshold": 500000}` |
| 9 | PASS | `{"distinct_structurally_usable_handler_keys": 1627578, "threshold": 100000}` |
| 10 | PASS | `{"distinct_valid_yrmonth": 322, "history_rows": 2686277, "max_yrmonth": "202610", "min_yrmonth": "200001", "threshold": 36}` |
| 11 | PASS | `{"distinct_history_keys": 146679, "matched_facility_keys": 146679, "rate": 1.0, "threshold": 0.99}` |
| 12 | PASS | `{"evaluation_identifier_header": "EVALUATION_IDENTIFIER", "found_violation_header": "FOUND_VIOLATION", "headers": ["ID_NUMBER", "ACTIVITY_LOCATION", "EVALUATION_IDENTIFIER", "EVALUATION_TYPE", "EVALUATION_DESC", "EVALUATION_AGENCY", "EVALUATION_START_DATE", "FOUND_VIOLATION"], "missing_core": []}` |
| 13 | PASS | `{"distinct_evaluation_opportunities": 1124301, "evaluation_rows": 1169946, "threshold": 100000}` |
| 14 | PASS | `{"distinct_positive_Y_opportunities": 378721, "found_nonblank": 1169946, "positive_threshold": 20000, "recognized_YNU": 1169930, "semantic_rate": 0.999986324155132}` |
| 15 | PASS | `{"distinct_evaluation_opportunities": 1124301, "parseable_date_opportunities": 1124301, "rate": 1.0, "threshold": 0.99}` |
| 16 | PASS | `{"distinct_evaluation_handler_keys": 309249, "matched_facility_keys": 307576, "rate": 0.9945901199357152, "threshold": 0.99}` |
| 17 | PASS | `{"causal": false, "future_membership_opened": false, "future_rows": 0, "identity_repair": false, "later_refresh_opened": false, "prediction": false, "prohibited_exposure": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"baseline_sha256": "ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5", "contract_sha": "ffbb1d89ea614c4c82cc39483383ccb09e23accf", "cost_usd": 0, "runner_sha256": "24be4a7a3d5b63a35dcdcbfabc553474122d18ddb801c0b1df9befe6920eb2bb"}` |

The raw EPA ZIP was transient only. No later weekly refresh was opened and no predictive/outcome relation was computed.
