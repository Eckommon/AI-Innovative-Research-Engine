# US-EPA-SDWIS-F01 — Attempt 01

**Disposition:** `HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **15/18**
- Failed gates: `[7, 9, 13]`
- Later quarterly refresh opened: **False**
- Future health-based membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 182, "active_research": "US-EPA-SDWIS-F01", "checkpoint_id": "CHK-20260930-US-EPA-SDWIS-F01-ACTIVE", "last_completed_issue": 181, "last_completed_research": "PORTFOLIO-R47", "last_decision": "DEC-274", "updated": "2026-09-30"}` |
| 2 | PASS | `{"contract_sha": "5546edebea1c09f68eb98075b286b3f20bd69b46", "issue": 182}` |
| 3 | PASS | `{"dictionary": {"bytes": 158932, "content_type": "text/html; charset=UTF-8", "etag": null, "final_url": "https://echo.epa.gov/tools/data-downloads/sdwa-download-summary", "last_modified": null, "sha256": "27d3f3919484017742323bc62dc9ba8db6682d63c60e32ac6f27137ecaa21ce3", "status": 200}, "downloads": {"bytes": 99476, "content_type": "text/html; charset=UTF-8", "etag": null, "final_url": "https://echo.epa.gov/tools/data-downloads", "last_modified": null, "sha256": "59e962733690e75e866ff5e601114fbb1819719ddf679fe50920af3dffa3b09c", "status": 200}, "faq": {"bytes": 108288, "content_type": "text/html; charset=UTF-8", "etag": null, "final_url": "https://echo.epa.gov/help/sdwa-faqs", "last_modified": null, "sha256": "9e672124c8cbfdd9467f303e0e8eec5c2e4125702dcbb79185dab440ed066954", "status": 200}}` |
| 4 | PASS | `{"bytes": 423774232, "content_length_header": "423774232", "content_type": "application/zip", "etag": "\"19424818-65632c8ca50c2\"", "final_url": "https://echo.epa.gov/files/echodownloads/SDWA_latest_downloads.zip", "last_modified": "Thu, 09 Jul 2026 19:39:37 GMT", "requested_url": "https://echo.epa.gov/files/echodownloads/SDWA_latest_downloads.zip", "sha256": "a18a20f9091c2e0466c91c83d0bac5651473441642331d09504e447a6e2ac7a4", "status": 200, "zip_valid": true}` |
| 5 | PASS | `{"present": ["SDWA_FACILITIES.CSV", "SDWA_PUB_WATER_SYSTEMS.CSV", "SDWA_REF_CODE_VALUES.CSV", "SDWA_VIOLATIONS_ENFORCEMENT.CSV"], "required": ["SDWA_FACILITIES.CSV", "SDWA_PUB_WATER_SYSTEMS.CSV", "SDWA_REF_CODE_VALUES.CSV", "SDWA_VIOLATIONS_ENFORCEMENT.CSV"]}` |
| 6 | PASS | `{"headers": ["SUBMISSIONYEARQUARTER", "PWSID", "PWS_NAME", "PRIMACY_AGENCY_CODE", "EPA_REGION", "SEASON_BEGIN_DATE", "SEASON_END_DATE", "PWS_ACTIVITY_CODE", "PWS_DEACTIVATION_DATE", "PWS_TYPE_CODE", "DBPR_SCHEDULE_CAT_CODE", "CDS_ID", "GW_SW_CODE", "LT2_SCHEDULE_CAT_CODE", "OWNER_TYPE_CODE", "POPULATION_SERVED_COUNT", "POP_CAT_2_CODE", "POP_CAT_3_CODE", "POP_CAT_4_CODE", "POP_CAT_5_CODE", "POP_CAT_11_CODE", "PRIMACY_TYPE", "PRIMARY_SOURCE_CODE", "IS_GRANT_ELIGIBLE_IND", "IS_WHOLESALER_IND", "IS_SCHOOL_OR_DAYCARE_IND", "SERVICE_CONNECTIONS_COUNT", "SUBMISSION_STATUS_CODE", "ORG_NAME", "ADMIN_NAME", "EMAIL_ADDR", "PHONE_NUMBER", "PHONE_EXT_NUMBER", "FAX_NUMBER", "ALT_PHONE_NUMBER", "ADDRESS_LINE1", "ADDRESS_LINE2", "CITY_NAME", "ZIP_CODE", "COUNTRY_CODE", "FIRST_REPORTED_DATE", "LAST_REPORTED_DATE", "STATE_CODE", "SOURCE_WATER_PROTECTION_CODE", "SOURCE_PROTECTION_BEGIN_DATE", "OUTSTANDING_PERFORMER", "OUTSTANDING_PERFORM_BEGIN_DATE", "REDUCED_RTCR_MONITORING", "REDUCED_MONITORING_BEGIN_DATE", "REDUCED_MONITORING_END_DATE", "SEASONAL_STARTUP_SYSTEM"], "missing": []}` |
| 7 | FAIL | `{"nonblank": 434040, "rate": 0.9883559118975209, "rows": 434040, "threshold": 0.9999, "valid": 428986}` |
| 8 | PASS | `{"duplicate_quarter_pwsid_keys": 0, "rate": 1.0, "rows": 434040, "threshold": 0.9999}` |
| 9 | FAIL | `{"distinct_quarters": 1, "max_quarter": "2026Q2", "quarters": ["2026Q2"], "threshold": 8}` |
| 10 | PASS | `{"distinct_active_pwsids": 140677, "max_quarter": "2026Q2", "threshold": 140000}` |
| 11 | PASS | `{"active_rows": 140677, "complete_type_source_population": 140649, "rate": 0.9998009624885376, "threshold": 0.9}` |
| 12 | PASS | `{"headers": ["SUBMISSIONYEARQUARTER", "PWSID", "VIOLATION_ID", "FACILITY_ID", "COMPL_PER_BEGIN_DATE", "COMPL_PER_END_DATE", "NON_COMPL_PER_BEGIN_DATE", "NON_COMPL_PER_END_DATE", "PWS_DEACTIVATION_DATE", "VIOLATION_CODE", "VIOLATION_CATEGORY_CODE", "IS_HEALTH_BASED_IND", "CONTAMINANT_CODE", "VIOL_MEASURE", "UNIT_OF_MEASURE", "FEDERAL_MCL", "STATE_MCL", "IS_MAJOR_VIOL_IND", "SEVERITY_IND_CNT", "CALCULATED_RTC_DATE", "VIOLATION_STATUS", "PUBLIC_NOTIFICATION_TIER", "CALCULATED_PUB_NOTIF_TIER", "VIOL_ORIGINATOR_CODE", "SAMPLE_RESULT_ID", "CORRECTIVE_ACTION_ID", "RULE_CODE", "RULE_GROUP_CODE", "RULE_FAMILY_CODE", "VIOL_FIRST_REPORTED_DATE", "VIOL_LAST_REPORTED_DATE", "ENFORCEMENT_ID", "ENFORCEMENT_DATE", "ENFORCEMENT_ACTION_TYPE_CODE", "ENF_ACTION_CATEGORY", "ENF_ORIGINATOR_CODE", "ENF_FIRST_REPORTED_DATE", "ENF_LAST_REPORTED_DATE"], "missing": []}` |
| 13 | FAIL | `{"distinct_violation_pwsids": 258445, "join_rate": 0.9863646036874383, "matched_to_pws_table": 254921, "pwsid_nonblank": 15432737, "pwsid_valid": 15186589, "syntax_rate": 0.9840502692425848, "violation_rows": 15432737}` |
| 14 | PASS | `{"categories": {"MCL": 1634410, "MRDL": 1285, "TT": 338078}, "distinct_health_events": 557102, "event_threshold": 10000, "health_indicator_nonblank": 14430187, "recognized_YN": 14430187, "semantic_rate": 1.0}` |
| 15 | PASS | `{"health_events": 557102, "parseable_begin_dates": 557102, "rate": 1.0, "threshold": 0.99}` |
| 16 | PASS | `{"baseline_max_quarter": "2026Q2", "baseline_sha256": "a18a20f9091c2e0466c91c83d0bac5651473441642331d09504e447a6e2ac7a4", "future_membership_opened": false, "future_rows_consumed": 0, "later_refresh_opened": false}` |
| 17 | PASS | `{"causal": false, "identity_repair": false, "prediction": false, "prohibited_exposure": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"baseline_sha256": "a18a20f9091c2e0466c91c83d0bac5651473441642331d09504e447a6e2ac7a4", "contract_sha": "5546edebea1c09f68eb98075b286b3f20bd69b46", "cost_usd": 0, "runner_sha256": "89ed70b7c08bed52ff462a6dee641ac8419a2b9b845d52fca3be06d43385621a"}` |

The raw EPA ZIP was transient only. No later quarterly refresh body was opened and no predictive/outcome relation was computed.
