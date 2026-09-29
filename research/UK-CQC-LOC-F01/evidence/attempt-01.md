# UK-CQC-LOC-F01 — Attempt 01

**Disposition:** `HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **11/18**
- Failed gates: `[5, 6, 7, 9, 11, 14, 15]`
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
| 5 | FAIL | `{"distinct_qualified_location_ids": 0, "header_row": 8, "headers": ["Issues with our care directory files We are currently moving to a new digital system to manage and publish our care directory. This has caused delays in generating files in their usual format, and some updates - such as provider registration cancellations - are taking longer than normal to appear. We are working to resolve these issues and will publish an update on our website once the system changes are complete. As part of our new assessment approach, adult social care, independent health and primary care locations that provide more than one type of service no longer receive a single location-level rating. This most commonly affects locations offering services such as homecare and supported living, or GP and out-of-hours services. These locations will show as ‘Not Rated’ in this file; ratings for individual services are available in the Care directory with ratings...` |
| 6 | FAIL | `{"nonblank": 0, "qualified": 0, "rate": 0.0, "threshold": 0.999}` |
| 7 | FAIL | `{"distinct_qualified_baseline_location_ids": 0, "threshold": 20000}` |
| 8 | PASS | `{"date_field_count": 1, "distinct_qualified_location_ids": 456, "header_row": 1, "headers": ["Location ID", "Location ODS Code", "Location Name", "Care Home?", "Location Type", "Location Primary Inspection Category", "Location Street Address", "Location Address Line 2", "Location City", "Location Post Code", "Location Local Authority", "Location Region", "Location NHS Region", "Location ONSPD CCG Code", "Location ONSPD CCG", "Location Commissioning CCG Code", "Location Commissioning CCG Name", "Service / Population Group", "Domain", "Latest Rating", "Publication Date", "Report Type", "Inherited Rating (Y/N)", "URL", "Provider ID", "Provider Name", "Brand ID", "Brand Name"], "rating_field_count": 2, "rows": 323673, "sheet": "Locations"}` |
| 9 | FAIL | `{"exact_linked_baseline_location_ids": 0, "threshold": 10000}` |
| 10 | PASS | `{"date_field_count": 5, "distinct_qualified_location_ids": 3441, "header_row": 1, "headers": ["Location ID", "Location ODS Code", "Location Name", "Location Status", "Location HSCA start date", "Location HSCA End Date", "Care home?", "Care homes beds at point location de-activated", "Location Type/Sector", "Location Primary Inspection Category", "Location Inspection Directorate", "Location Region", "Location Primary NHS Region", "Location Local Authority", "Location ONSPD CCG Code", "Location ONSPD CCG", "Location Commissioning CCG Code", "Location Commissioning CCG Name", "Location Parliamentary Constituency", "Location Latitude", "Location Longitude", "Location Street Address", "Location Address Line 2", "Location City", "Location County", "Location Postal Code", "Location PAF ID", "Location UPRN ID", "Location Latest Overall Rating", "Publication Date", "Inherited Rating (Y/N)", "Brand ID", "Brand Name", "Provider Charity Number",...` |
| 11 | FAIL | `{"distinct_exact_deactivated_location_ids": 3441, "threshold": 5000}` |
| 12 | PASS | `{"parseable": 3441, "parseable_end_date_rate": 1.0, "qualified_rows": 3441, "threshold": 0.95}` |
| 13 | PASS | `{"address_change_example": true, "api_linked_organisations": true, "deactivated_not_necessarily_closed": true, "legal_structure_example": true, "registration_start_end_api": true, "reregistered_example": true}` |
| 14 | FAIL | `{"conflicting_exact_location_ids": 0, "evaluable_with_provider_id": false, "examples": []}` |
| 15 | FAIL | `{"archive_pages": {"filters_archive": {"dates": [], "meta": {"bytes": 439035, "content_length_header": null, "content_type": "text/html; charset=utf-8", "entity_body_bytes_consumed": 439035, "etag": null, "last_modified": null, "requested_url": "https://drive.google.com/drive/folders/1Y6V6r-q2l4lJYKuZL0DXw25VDUTH6L4N?usp=sharing", "sha256": "767b5b9667a1969cd5c2d5a15d99f51af55164b134672818b5635c67d82d4041", "status": 200}, "url": "https://drive.google.com/drive/folders/1Y6V6r-q2l4lJYKuZL0DXw25VDUTH6L4N?usp=sharing"}, "ratings_archive": {"dates": [], "meta": {"bytes": 403180, "content_length_header": null, "content_type": "text/html; charset=utf-8", "entity_body_bytes_consumed": 403180, "etag": null, "last_modified": null, "requested_url": "https://drive.google.com/drive/folders/1N9JH4DhoKvb5SO6I9ObqRmhPgxD_m_pS?usp=sharing", "sha256": "fb517bd798e5faba7059588881b265d1fa76c13afab372aaef1cc607d5f9d6ef", "status": 200}, "url": "https://...` |
| 16 | PASS | `{"future_entity_body_bytes_consumed": 0, "future_rows_opened": 0, "policy": "runner defines and requests only frozen 01-Sep-2026 files"}` |
| 17 | PASS | `{"causal_claim_made": false, "future_event_membership_opened": false, "future_rows_opened": 0, "name_address_fuzzy_geo_manual_repair_used": false, "prediction_computed": false, "ranking_computed": false, "relationship_computed": false}` |
| 18 | PASS | `{"contract_sha": "99c7782cabc384ce7c4817a91b5cb1bdc105012c", "cost_usd": 0, "runner_sha256": "dba8d9d6d9a69ece7625b5e9d4fe4460efafe7e3d568e9e348e349eb6ac1a4b3", "source_sha256": {"deactivated": "682c88d44ce97264328cf4f21b63b7889ad6906907b6bbe18721bb868e16f853", "filters": "1b64024445823e2e53c329c47b44d69831170df12b42bb2a300958cc8d98aa93", "ratings": "432d8c5220572b11adec15ab53dd8db411c4f45de5c3320ca5b5abb69fdf473d"}}` |

Only frozen 01-Sep-2026 CQC entity files were authorized. No post-2026-09-28 inactive/deactivated entity body was opened.
