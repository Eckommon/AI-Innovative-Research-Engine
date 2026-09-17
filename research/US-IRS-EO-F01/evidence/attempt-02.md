# US-IRS-EO-F01 — Attempt 02

**Disposition:** `PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY`

- Attempt valid: `True`
- Gates passed: **18/18**
- Failed gates: `[]`
- Future automatic-revocation rows opened: **0**
- 2025/2026 Form-990 index rows opened: **0**
- Automatic-revocation entity-body bytes consumed: **0**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 163, "active_research": "US-IRS-EO-F01", "checkpoint_id": "CHK-20260918-US-IRS-EO-F01-ACTIVE", "last_completed_issue": 162, "last_completed_research": "PORTFOLIO-R39", "last_decision": "DEC-237", "updated": "2026-09-18"}` |
| 2 | PASS | `{"contract_sha": "689a00db411b650defcb679bef998beeb55a57da", "issue": 163}` |
| 3 | PASS | `{"2022": {"bytes": 72228246, "content_type": "text/csv", "final_url": "https://apps.irs.gov/pub/epostcard/990/xml/2022/index_2022.csv", "sha256": "5493bf8850e25dbd3d44acf53faa92faed4f50931600aadc5e4e425379b74631", "status": 200, "url": "https://apps.irs.gov/pub/epostcard/990/xml/2022/index_2022.csv"}, "2023": {"bytes": 77519435, "content_type": "text/csv", "final_url": "https://apps.irs.gov/pub/epostcard/990/xml/2023/index_2023.csv", "sha256": "3906ff84e87285f3a3cf2ba328505b1ba348d9814f5dc95864fa7d1f9575a58e", "status": 200, "url": "https://apps.irs.gov/pub/epostcard/990/xml/2023/index_2023.csv"}, "2024": {"bytes": 91056866, "content_type": "text/csv", "final_url": "https://apps.irs.gov/p...` |
| 4 | PASS | `{"2022": {"missing": [], "raw_headers": ["RETURN_ID", "FILING_TYPE", "EIN", "TAX_PERIOD", "SUB_DATE", "TAXPAYER_NAME", "RETURN_TYPE", "DLN", "OBJECT_ID"], "resolved": {"dln": "DLN", "ein": "EIN", "filing_type": "FILING_TYPE", "object_id": "OBJECT_ID", "return_id": "RETURN_ID", "submission_date": "SUB_DATE", "tax_period": "TAX_PERIOD", "taxpayer_name": "TAXPAYER_NAME"}}, "2023": {"missing": [], "raw_headers": ["RETURN_ID", "FILING_TYPE", "EIN", "TAX_PERIOD", "SUB_DATE", "TAXPAYER_NAME", "RETURN_TYPE", "DLN", "OBJECT_ID"], "resolved": {"dln": "DLN", "ein": "EIN", "filing_type": "FILING_TYPE", "object_id": "OBJECT_ID", "return_id": "RETURN_ID", "submission_date": "SUB_DATE", "tax_period": "T...` |
| 5 | PASS | `{"nonblank_rows": 2090378, "rate": 1.0, "valid_rows": 2090378}` |
| 6 | PASS | `{"combined_rows": 2090378, "threshold": 500000}` |
| 7 | PASS | `{"distinct_valid_ein": 742646, "threshold": 150000}` |
| 8 | PASS | `{"ein_in_at_least_two_indexes": 641705, "threshold": 75000}` |
| 9 | PASS | `{"parseable_tax_period": 2090378, "rate": 1.0, "valid_ein_rows": 2090378}` |
| 10 | PASS | `{"duplicate_rate": 0.0, "duplicate_rows": 0, "nonblank_rate": 1.0, "object_nonblank": 2090378, "valid_ein_rows": 2090378}` |
| 11 | PASS | `{"min_max_by_index": {"2022": {"max": "2022-01-01T00:00:00", "min": "2022-01-01T00:00:00"}, "2023": {"max": "2023-01-01T00:00:00", "min": "2023-01-01T00:00:00"}, "2024": {"max": "2024-01-01T00:00:00", "min": "2024-01-01T00:00:00"}}, "parseable_submission_dates": 2090378, "rate": 1.0, "valid_ein_rows": 2090378}` |
| 12 | PASS | `{"download_page_documented": true, "xml_zip_metadata": {"content_length": "104816571", "content_type": "application/zip", "entity_body_bytes_consumed": 0, "etag": "\"63f5fbb-62facfc2207e8\"", "final_url": "https://apps.irs.gov/pub/epostcard/990/xml/2024/2024_TEOS_XML_01A.zip", "last_modified": "Thu, 06 Mar 2025 14:04:31 GMT", "method": "HEAD", "status": 200}}` |
| 13 | PASS | `{"990ez": true, "990pf": true, "official_schema_family_990": true}` |
| 14 | PASS | `{"effective_revocation_date": true, "ein": true, "posting_date": true, "reinstatement": true}` |
| 15 | PASS | `{"third_due_date_semantics": true, "three_consecutive_years": true}` |
| 16 | PASS | `{"content_length": "47564625", "content_type": "application/zip", "entity_body_bytes_consumed": 0, "etag": "\"2d5c751-65b45a011d450\"", "final_url": "https://apps.irs.gov/pub/epostcard/data-download-revocation.zip", "last_modified": "Sat, 12 Sep 2026 09:14:16 GMT", "method": "HEAD", "status": 200}` |
| 17 | PASS | `{"automatic_revocation_entity_body_bytes_consumed": 0, "future_form990_2025_2026_rows_opened": 0, "future_outcome_rows_opened": 0, "name_address_repair_used": false, "nonfiling_streak_exposure_variables_constructed": 0}` |
| 18 | PASS | `{"contract_sha": "689a00db411b650defcb679bef998beeb55a57da", "cost_usd": 0, "runner_sha256": "5d788154e1d02e4855b96be23c8d4a5d64949d212323ea707c9c873fc713f4c8", "source_sha256": {"2022": "5493bf8850e25dbd3d44acf53faa92faed4f50931600aadc5e4e425379b74631", "2023": "3906ff84e87285f3a3cf2ba328505b1ba348d9814f5dc95864fa7d1f9575a58e", "2024": "c00051a33f65d408ea7f6d5fa008c7f82f9bc6223751f4a6e29d59f5e17f826d"}}` |

This attempt did not read any Automatic Revocation List row. Scientific thresholds and source years were not modified.

## Attempt 02 implementation-only correction

- Correction commit: `d3026031bb7e5b90e63709589e226cd99babc590`
- Base runner commit: `14b671a6f0209cc6afba2099fa42e6bc209e63f9`
- Submission-date source precision counts: `{"YYYY_year_precision": 2090378}`
- Exact `YYYY` is treated as source **year precision** only. `YYYY-01-01` is an internal ordering sentinel, not an observed month/day.
- Scientific thresholds changed: **false**
- Source years changed: **false**
- Identity rule changed: **false**
- Outcome firewall changed: **false**
