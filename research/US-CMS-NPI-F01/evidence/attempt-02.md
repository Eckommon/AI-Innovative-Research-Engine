# US-CMS-NPI-F01 — Attempt 02

**Disposition:** `PASS_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_READY`

- Attempt valid: `True`
- Gates passed: **18/18**
- Failed gates: `[]`
- Weekly body opened: **False**
- Future deactivation membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 201, "active_research": "US-CMS-NPI-F01", "checkpoint_id": "CHK-20261013-US-CMS-NPI-F01-ACTIVE", "last_completed_issue": 200, "last_completed_research": "PORTFOLIO-R56", "last_decision": "DEC-314", "updated": "2026-10-13"}` |
| 2 | PASS | `{"contract_sha": "18646fff22a499fedb058df397269281e62793b8", "issue": 201}` |
| 3 | PASS | `{"deactivation": {"text": "NPPES Data Dissemination V.2 - Monthly Deactivation Update - October 12, 2026", "url": "https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_101226_V2.zip"}, "dissemination": "https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination", "files_page": "https://download.cms.gov/nppes/NPI_Files.html", "full": {"text": "NPPES Data Dissemination V.2 (October 12, 2026)", "url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_October_2026_V2.zip"}, "weekly": {"text": "NPPES Data Dissemination V.2 - Weekly Update - 100526_101126", "url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip"}}` |
| 4 | PASS | `{"bytes": 1159720219, "content_length_header": "1159720219", "content_type": "application/zip", "etag": "\"dffc19807a2ffc7300b104b66732e994:1791790182.261161\"", "final_url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_October_2026_V2.zip", "last_modified": "Mon, 12 Oct 2026 07:31:11 GMT", "requested_url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_October_2026_V2.zip", "sha256": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "status": 200, "zip_valid": true}` |
| 5 | PASS | `{"bytes": 2679243, "content_length_header": "2679243", "content_type": "application/zip", "etag": "\"1d9e99cc49dfeebcb4a67b9b8a9f9d2c:1791788469.859903\"", "final_url": "https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_101226_V2.zip", "last_modified": "Mon, 12 Oct 2026 07:01:10 GMT", "requested_url": "https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_101226_V2.zip", "sha256": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "status": 200, "zip_valid": true}` |
| 6 | PASS | `{"headers": ["NPI", "Entity Type Code", "Replacement NPI", "Employer Identification Number (EIN)", "Provider Organization Name (Legal Business Name)", "Provider Last Name (Legal Name)", "Provider First Name", "Provider Middle Name", "Provider Name Prefix Text", "Provider Name Suffix Text", "Provider Credential Text", "Provider Other Organization Name", "Provider Other Organization Name Type Code", "Provider Other Last Name", "Provider Other First Name", "Provider Other Middle Name", "Provider Other Name Prefix Text", "Provider Other Name Suffix Text", "Provider Other Credential Text", "Provider Other Last Name Type Code", "Provider First Line Business Mailing Address", "Provider Second Line Business Mailing Address", "Provider Business Mailing Address City Name", "Provider Business Mailing Address State Name", "Provider Business Mailing Address Postal Code", "Provider Business Mailing Address Country Code (If outside U.S.)", "Provider Business Mailing Address Telephone Number", "Provider Business Mailing Address Fax Number", "Provider First Line Business Practice Location Address", "Provider Second Line Business Practice Location Address", "Provider Business Practice Location Ad...` |
| 7 | PASS | `{"nonblank": 9852180, "rate": 1.0, "threshold": 0.99999, "valid": 9852180}` |
| 8 | PASS | `{"duplicate_exact": 0, "exact_rows": 9852180, "rate": 1.0, "threshold": 0.99999}` |
| 9 | PASS | `{"active_type2": 1979717, "threshold": 500000}` |
| 10 | PASS | `{"active_type2": 1979717, "rate": 1.0, "threshold": 0.95, "with_taxonomy": 1979717}` |
| 11 | PASS | `{"multi_taxonomy": 410081, "single_taxonomy": 1569636, "threshold_each": 100000}` |
| 12 | PASS | `{"distinct_npi": 817918, "join_rate": 1.0, "matched_main": 817918, "practice_location_member": "pl_pfile_20050523-20261011.csv", "rows_nonblank_npi": 1274332, "syntax_rate": 1.0, "valid_npi": 1274332}` |
| 13 | PASS | `{"header_row": 2, "headers": ["NPI", "NPPES Deactivation Date"], "sheet": "DeactivatedNPIs", "xlsx_member": "NPPES Deactivated NPI Report 20261012.xlsx"}` |
| 14 | PASS | `{"date_nonblank": 357926, "date_parseable": 357926, "date_rate": 1.0, "npi_nonblank": 357926, "npi_rate": 1.0, "npi_valid": 357926}` |
| 15 | PASS | `{"distinct_deactivated_npis": 357926, "threshold": 50000}` |
| 16 | PASS | `{"future_membership_opened": false, "future_rows": 0, "later_monthly_body_opened": false, "weekly_body_opened": false, "weekly_metadata": {"content_length": "6705278", "content_type": "application/zip", "etag": "\"2606d1148a6fbfb4208bbe2ceeb6c431:1791788535.190815\"", "final_url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_100526_101126_Weekly_V2.zip", "last_modified": "Mon, 12 Oct 2026 07:02:15 GMT", "status": 200}}` |
| 17 | PASS | `{"causal": false, "deactivation_history_exposure": false, "identity_repair": false, "prediction": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"contract_sha": "18646fff22a499fedb058df397269281e62793b8", "cost_usd": 0, "deactivation_sha256": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "full_sha256": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "runner_sha256": "8664b6d8b77849bcdb2a29d6bc80c868eea67224cbc4290ac33ecfdc5734acf1"}` |

Attempt 01 remains immutable. Attempt 02 changes only the deactivation-body parser from CSV-only to source-native XLSX support.
