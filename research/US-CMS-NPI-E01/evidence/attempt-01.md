# US-CMS-NPI-E01 — Attempt 01

**Disposition:** `INCONCLUSIVE_US_CMS_NPI_E01`

- Attempt valid: `True`
- Execution gates passed: **18/18**
- Failed gates: `[]`
- Future update body opened: **True**
- Future deactivation membership opened: **True**
- Cost: **0 USD**

## Future source

- Token: `101226_101826`
- Covered: **2026-10-12..2026-10-18**

## Pair outcome table

| both | exposed only | control only | neither |
|---:|---:|---:|---:|
| 0 | 30 | 42 | 346787 |

## Frozen statistics

`{"matched_odds_ratio": 0.7142857142857143, "mor_ci95": [0.43168261444288, 1.168664599840469], "mcnemar_exact_p": 0.1945051658673991, "discordant_pairs": 72, "total_deactivated_matched_npis": 72, "exposed_events": 30, "control_events": 42, "exposed_risk": 8.649047595708919e-05, "control_risk": 0.00012108666633992487, "marginal_risk_ratio": 0.7142857142857143, "risk_difference_per_100k": -3.4596190382835683, "minimum_event_support_satisfied": true}`

## Execution gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 203, "active_research": "US-CMS-NPI-E01", "checkpoint_id": "CHK-20261013-US-CMS-NPI-E01-ACTIVE", "last_completed_issue": 202, "last_completed_research": "US-CMS-NPI-N01", "last_decision": "DEC-318", "updated": "2026-10-18"}` |
| 2 | PASS | `{"contract_sha": "48843c9979336dcd10fdff984f458277062d6f20", "issue": 203}` |
| 3 | PASS | `{"deactivation_sha256": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "expected_deactivation": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "expected_full": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "full_sha256": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e"}` |
| 4 | PASS | `{"age_smd": 0.008089949330951387, "common_strata": 31791, "control": 1568503, "eligible": 1978439, "exposed": 409936, "location_smd": 0.01358494151547246, "pairs": 346859, "unique_controls": 346859, "unique_exposed": 346859}` |
| 5 | PASS | `{"expected": 346859, "pairs": 346859, "unique_controls": 346859, "unique_exposed": 346859}` |
| 6 | PASS | `{"age_smd": 0.008089949330951387, "expected_age_smd": 0.008089949330951387, "expected_location_smd": 0.01358494151547246, "location_smd": 0.01358494151547246, "tolerance": 1e-06}` |
| 7 | PASS | `{"anchor_present": true, "anchor_token": "100526_101126", "preflight_commit": "0e81620e9cbea5dcddb558791e786d1565dfaf0f", "preflight_zip_body_opened": false}` |
| 8 | PASS | `{"chosen_token": "101226_101826", "earliest": true, "end": "2026-10-18", "qualifying_count": 1, "start": "2026-10-12"}` |
| 9 | PASS | `{"bytes": 6642415, "content_length_header": "6642415", "content_type": "application/zip", "etag": "\"d3294db5c433ee5f677bf9d4a8327084:1792393329.262554\"", "final_url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip", "last_modified": "Mon, 19 Oct 2026 07:02:09 GMT", "requested_url": "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip", "sha256": "cc5a3c9d833e4e107ae92e20f7ccb575998e6596caae60a5ffcdba1e4c763398", "status": 200, "zip_members": ["endpoint_pfile_20261012-20261018.csv", "endpoint_pfile_20261012-20261018_fileheader.csv", "othername_pfile_20261012-20261018.csv", "othername_pfile_20261012-20261018_fileheader.csv", "pl_pfile_20261012-20261018.csv", "pl_pfile_20261012-20261018_fileheader.csv", "npidata_pfile_20261012-20261018.csv", "npidata_pfile_20261012-20261018_fileheader.csv", "NPPES_Data_Dissemination_CodeValues.pdf", "NPPES_Data_Dissemination_Readme_v.2.pdf"]}` |
| 10 | PASS | `{"deactivation": "NPI Deactivation Date", "entity": "Entity Type Code", "main_member": "npidata_pfile_20261012-20261018.csv", "npi": "NPI", "reactivation": "NPI Reactivation Date"}` |
| 11 | PASS | `{"future_nonblank_npis": 32691, "rate": 1.0, "threshold": 0.99999, "valid_exact_npis": 32691}` |
| 12 | PASS | `{"all_exact_join_locked": true, "counted_event_npis": 202, "identity_repair": false}` |
| 13 | PASS | `{"counted_in_window": 202, "event_window_end": "2026-10-18", "event_window_start": "2026-10-12", "locked_candidate_deactivation_rows": 202, "outside_window_or_unparsed": 0, "parse_rate": 1.0, "parseable_dates": 202, "threshold": 0.999}` |
| 14 | PASS | `{"a_both": 0, "b_exposed_only": 30, "c_control_only": 42, "d_neither": 346787, "expected": 346859, "sum": 346859}` |
| 15 | PASS | `{"reactivation_erases_event": false, "same_update_reactivation_control": 0, "same_update_reactivation_exposed": 0}` |
| 16 | PASS | `{"control_events": 42, "control_risk": 0.00012108666633992487, "discordant_pairs": 72, "exposed_events": 30, "exposed_risk": 8.649047595708919e-05, "marginal_risk_ratio": 0.7142857142857143, "matched_odds_ratio": 0.7142857142857143, "mcnemar_exact_p": 0.1945051658673991, "minimum_event_support_satisfied": true, "mor_ci95": [0.43168261444288, 1.168664599840469], "risk_difference_per_100k": -3.4596190382835683, "total_deactivated_matched_npis": 72}` |
| 17 | PASS | `{"causal_claim": false, "closure_quality_interpretation": false, "identity_repair": false, "later_week_selected": false, "monthly_substitution": false, "provider_ranking": false}` |
| 18 | PASS | `{"baseline_deactivation_sha": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "baseline_full_sha": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "contract_sha": "48843c9979336dcd10fdff984f458277062d6f20", "cost_usd": 0, "future_weekly_sha": "cc5a3c9d833e4e107ae92e20f7ccb575998e6596caae60a5ffcdba1e4c763398", "runner_sha": "a67fdf7df8e3e48be246c239f6cd8daf52e3135e4973009a2c29e934b4fd627f"}` |

NPI deactivation is treated only as an administrative NPPES registry event. No provider ranking or causal interpretation is authorized.
