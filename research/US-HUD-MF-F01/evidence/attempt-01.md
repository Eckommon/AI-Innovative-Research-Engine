# US-HUD-MF-F01 — Attempt 01

**Disposition:** `IMPLEMENTATION_BLOCKED_US_HUD_MF_F01_ATTEMPT_01`

- Attempt valid: `False`
- Gates passed: **6/18**
- Failed gates: `[]`
- Future terminated rows opened: **0**
- Future adverse membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 168, "active_research": "US-HUD-MF-F01", "checkpoint_id": "CHK-20260921-US-HUD-MF-F01-ACTIVE", "last_completed_issue": 167, "last_completed_research": "PORTFOLIO-R41", "last_decision": "DEC-246", "updated": "2026-09-21"}` |
| 2 | PASS | `{"contract_sha": "73eec2f714f3e1c89d0441ffb9f746721bda3443", "issue": 168}` |
| 3 | PASS | `{"inspection": {"bytes": 150045, "content_length_header": null, "content_type": "text/html; charset=UTF-8", "entity_body_bytes_consumed": 150045, "etag": null, "last_modified": "Wed, 16 Sep 2026 19:36:44 GMT", "requested_url": "https://www.hud.gov/stat/mfh/inspection-scores", "sha256": "4bce1d7e86b706c267d02345a48d3d5d6c9991489b723b01bae600a273861312", "status": 200}, "mortgage": {"bytes": 151305, "content_length_header": null, "content_type": "text/html; charset=UTF-8", "entity_body_bytes_consumed": 151305, "etag": null, "last_modified": "Mon, 21 Sep 2026 14:25:36 GMT", "requested_url": "https://www.hud.gov/hud-partners/multifamily-fhasl-active", "sha256": "864dc61bbd9148a5c6389348c146cf267dfae4c2eb7972cf6e0be9dbe2f1f002", "status": 200}, "property": {"bytes": 152860, "content_length_header": null, "content_type": "text/html; charset=UTF-8", "entity_body_bytes_consumed": 152860, "eta...` |
| 4 | PASS | `{"active": "https://www.hud.gov/sites/default/files/Housing/documents/FHA-BF90-RM-A.xlsx", "inspection": "https://www.hud.gov/sites/default/files/Housing/documents/MF-Inspection-Report.xls", "property": "https://www.hud.gov/sites/dfiles/Housing/documents/activeportfoliopropdata.xlsx", "terminated": "https://www.hud.gov/sites/default/files/Housing/documents/FHA-BF90-RM-T.xlsx"}` |
| 5 | FAIL | `{"distinct_valid_fha": 0, "header_row": 3, "headers": ["HUD PROJECT NUMBER", "PROPERTY NAME", "PROPERTY CITY", "PROPERTY STATE", "PROPERTY ZIP", "UNITS", "INITIAL ENDORSEMENT DATE", "FINAL ENDORSEMENT DATE", "ORIGINAL MORTGAGE AMOUNT", "FIRST PAYMENT DATE", "MATURITY DATE", "TERM IN MONTHS", "INTEREST RATE", "CURRENT PRINCIPAL AND INTEREST", "AMORITIZED PRINCIPAL BALANCE", "HOLDER NAME", "HOLDER CITY", "HOLDER STATE", "SERVICER NAME", "SERVICER CITY", "SERVICER STATE", "SECTION OF ACT CODE", "SOA CATEGORY/SUB CATEGORY", "TE", "TC", "BUSINESS_TYPE", "SA_TYPE_CODE"], "nonblank_fha": 0, "rows": 0, "sheet": "08312026", "syntax_rate": 0.0, "valid_fha": 0}` |
| 6 | PASS | `{"bytes": 9283051, "content_length_header": "9283051", "content_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "entity_body_bytes_consumed": 9283051, "etag": "\"8da5eb-65a70a216b786\"", "final_url": "https://www.hud.gov/sites/default/files/Housing/documents/FHA-BF90-RM-T.xlsx", "last_modified": "Tue, 01 Sep 2026 19:07:42 GMT", "requested_url": "https://www.hud.gov/sites/default/files/Housing/documents/FHA-BF90-RM-T.xlsx", "sha256": "2faaeb67e03e54a9a176a63ea34abe863e35c4db9309a278606a98ff0530de71", "status": 200}` |
| 7 | FAIL | `{"nonblank": 0, "rate": 0.0, "valid": 0}` |
| 8 | FAIL | `{"distinct_qualified_active_fha": 0, "threshold": 10000}` |
| 9 | FAIL | `{"header_row": 2, "headers": ["FHA_BF90_RM_T", " 58780", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], "qualified_fha_rows": 0, "reason_top50": [], "rows": 0, "sheet": "08312026", "termination_date_parseable": 0, "termination_reason_nonblank": 0}` |
| 10 | FAIL | `{"date_rate": 0.0, "qualified_rows": 0, "reason_rate": 0.0}` |
| 11 | FAIL | `{"adverse_source_labels": [], "routine_source_labels": [], "semantic_rule": "source-native labels only; adverse tokens frozen={default,claim,foreclos}; routine tokens frozen={prepay,voluntary,matur,refinan}"}` |
| 12 | PASS | `{"distinct_property_ids": 17734, "header_row": 1, "headers": ["property_name_text", "property_id", "fha_number", "soa_code", "soa_numeric_name", "soa_description_text", "is_primary_fha_ind", "is_insured_ind", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], "qualified_fha": 17734, "rows": 36815, "sheet": "All active Properties with FHA "}` |
| 13 | FAIL | `{"active_ids": 0, "matched_active_fha": 0, "rate": 0.0, "threshold": 0.7}` |

## Implementation error

`{'type': 'RuntimeError', 'message': 'XLSX_PARSE_ERROR:inspection.xlsx:BadZipFile:File is not a zip file'}`

Historical terminated rows, if retrieved, were used only for structural schema/reason/date support. No post-2026-09-21 terminated snapshot body was opened.
