# UK-CQC-LOC-F01 — Attempt 02

**Disposition:** `HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **13/18**
- Failed gates: `[6, 7, 9, 11, 15]`
- Future rows opened: **0**
- Future event membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 171, "active_research": "UK-CQC-LOC-F01", "checkpoint_id": "CHK-20260929-UK-CQC-LOC-F01-ACTIVE", "last_completed_issue": 170, "last_completed_research": "PORTFOLIO-R42", "last_decision": "DEC-252", "updated": "2026-09-29"}` |
| 2 | PASS | `{"contract_sha": "99c7782cabc384ce7c4817a91b5cb1bdc105012c", "issue": 171}` |
| 3 | PASS | `{"landing": {"bytes": 76805, "content_length_header": "76805", "content_type": "text/html; charset=UTF-8", "entity_body_bytes_consumed": 76805, "etag": "\"1790598150\"", "last_modified": "Mon, 28 Sep 2026 12:22:30 GMT", "requested_url": "https://www.cqc.org.uk/about-us/transparency/using-cqc-data", "sha256": "70b08501dd51c80e031a51e7b209e586080530923af8caebc71cc57d2d87f40d", "status": 200}, "selectors_present": {"deactivated": true, "filters": true, "ratings": true}}` |
| 4 | PASS | `{"deactivated": "https://www.cqc.org.uk/system/files/2026-09/01_September_2026_Deactivated_Locations.ods", "filters": "https://www.cqc.org.uk/system/files/2026-09/01_September_2026_HSCA_Active_Locations.ods", "ratings": "https://www.cqc.org.uk/system/files/2026-09/01_September_2026_Latest_ratings.ods"}` |
| 5 | PASS | `{"distinct_qualified_location_ids": 1770, "header_row": 1, "headers": ["Location ID", "Location HSCA start date", "Dormant (Y/N)", "Care home?", "Location Name", "Location ODS Code", "Location Telephone Number", "Registered manager", "Location Web Address", "Care homes beds", "Location Type/Sector", "Location Inspection Directorate", "Location Primary Inspection Category", "Location Latest Overall Rating", "Publication Date", "Inherited Rating (Y/N)", "Location Region", "Location NHS Region", "Location Local Authority", "Location ONSPD CCG Code", "Location ONSPD CCG", "Location Commissioning CCG Code", "Location Commissioning CCG", "Location Street Address", "Location Address Line 2", "Location City", "Location County", "Location Postal Code", "Location PAF ID", "Location UPRN ID", "Location Latitude", "Location Longitude", "Location Parliamentary Constituency", "Brand ID", "Brand Name", "Provider Companies House Number", "Provider C...` |
| 6 | FAIL | `{"nonblank": 57069, "qualified": 1770, "rate": 0.03101508699994743, "threshold": 0.999}` |
| 7 | FAIL | `{"distinct_qualified_baseline_location_ids": 1770, "threshold": 20000}` |
| 8 | PASS | `{"date_field_count": 1, "distinct_qualified_location_ids": 456, "header_row": 1, "headers": ["Location ID", "Location ODS Code", "Location Name", "Care Home?", "Location Type", "Location Primary Inspection Category", "Location Street Address", "Location Address Line 2", "Location City", "Location Post Code", "Location Local Authority", "Location Region", "Location NHS Region", "Location ONSPD CCG Code", "Location ONSPD CCG", "Location Commissioning CCG Code", "Location Commissioning CCG Name", "Service / Population Group", "Domain", "Latest Rating", "Publication Date", "Report Type", "Inherited Rating (Y/N)", "URL", "Provider ID", "Provider Name", "Brand ID", "Brand Name"], "rating_field_count": 2, "rows": 323673, "sheet": "Locations"}` |
| 9 | FAIL | `{"exact_linked_baseline_location_ids": 456, "threshold": 10000}` |
| 10 | PASS | `{"date_field_count": 5, "distinct_qualified_location_ids": 3441, "header_row": 1, "headers": ["Location ID", "Location ODS Code", "Location Name", "Location Status", "Location HSCA start date", "Location HSCA End Date", "Care home?", "Care homes beds at point location de-activated", "Location Type/Sector", "Location Primary Inspection Category", "Location Inspection Directorate", "Location Region", "Location Primary NHS Region", "Location Local Authority", "Location ONSPD CCG Code", "Location ONSPD CCG", "Location Commissioning CCG Code", "Location Commissioning CCG Name", "Location Parliamentary Constituency", "Location Latitude", "Location Longitude", "Location Street Address", "Location Address Line 2", "Location City", "Location County", "Location Postal Code", "Location PAF ID", "Location UPRN ID", "Location Latest Overall Rating", "Publication Date", "Inherited Rating (Y/N)", "Brand ID", "Brand Name", "Provider Charity Number",...` |
| 11 | FAIL | `{"distinct_exact_deactivated_location_ids": 3441, "threshold": 5000}` |
| 12 | PASS | `{"parseable": 3441, "parseable_end_date_rate": 1.0, "qualified_rows": 3441, "threshold": 0.95}` |
| 13 | PASS | `{"address_change_example": true, "api_linked_organisations": true, "deactivated_not_necessarily_closed": true, "legal_structure_example": true, "registration_start_end_api": true, "reregistered_example": true}` |
| 14 | PASS | `{"conflicting_exact_location_ids": 0, "evaluable_with_provider_id": true, "examples": []}` |
| 15 | FAIL | `{"archive_pages": {"filters_archive": {"dates": [], "error": "NameError:name 'html_lib' is not defined", "url": "https://drive.google.com/drive/folders/1Y6V6r-q2l4lJYKuZL0DXw25VDUTH6L4N?usp=sharing"}, "ratings_archive": {"dates": [], "error": "NameError:name 'html_lib' is not defined", "url": "https://drive.google.com/drive/folders/1N9JH4DhoKvb5SO6I9ObqRmhPgxD_m_pS?usp=sharing"}}, "archive_urls": {"filters_archive": "https://drive.google.com/drive/folders/1Y6V6r-q2l4lJYKuZL0DXw25VDUTH6L4N?usp=sharing", "ratings_archive": "https://drive.google.com/drive/folders/1N9JH4DhoKvb5SO6I9ObqRmhPgxD_m_pS?usp=sharing"}, "count": 0, "distinct_snapshot_dates_le_2026_09_01": [], "threshold": 6}` |
| 16 | PASS | `{"future_entity_body_bytes_consumed": 0, "future_rows_opened": 0, "policy": "runner defines and requests only frozen 01-Sep-2026 files"}` |
| 17 | PASS | `{"causal_claim_made": false, "future_event_membership_opened": false, "future_rows_opened": 0, "name_address_fuzzy_geo_manual_repair_used": false, "prediction_computed": false, "ranking_computed": false, "relationship_computed": false}` |
| 18 | PASS | `{"contract_sha": "99c7782cabc384ce7c4817a91b5cb1bdc105012c", "cost_usd": 0, "runner_sha256": "2ef0cc64bce10afd6ab65ddbb17fd85938963e0ad70ddd3f89180be3e4352234", "source_sha256": {"deactivated": "682c88d44ce97264328cf4f21b63b7889ad6906907b6bbe18721bb868e16f853", "filters": "1b64024445823e2e53c329c47b44d69831170df12b42bb2a300958cc8d98aa93", "ratings": "432d8c5220572b11adec15ab53dd8db411c4f45de5c3320ca5b5abb69fdf473d"}}` |

Only frozen 01-Sep-2026 CQC entity files were authorized. No post-2026-09-28 inactive/deactivated entity body was opened.
