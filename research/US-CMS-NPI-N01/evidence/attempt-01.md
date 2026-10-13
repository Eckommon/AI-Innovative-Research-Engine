# US-CMS-NPI-N01 — Attempt 01

**Disposition:** `PASS_US_CMS_NPI_N01_MULTI_TAXONOMY_MATCHED_COHORT_READY`

- Attempt valid: `True`
- Gates passed: **18/18**
- Failed gates: `[]`
- Future update membership opened: **False**
- Arm-specific deactivation lookup: **False**
- Cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 202, "active_research": "US-CMS-NPI-N01", "checkpoint_id": "CHK-20261013-US-CMS-NPI-N01-ACTIVE", "last_completed_issue": 201, "last_completed_research": "US-CMS-NPI-F01", "last_decision": "DEC-316", "updated": "2026-10-13"}` |
| 2 | PASS | `{"contract_sha": "29ab6cd8368801137eff94463a5b405c1fdf10ac", "issue": 202}` |
| 3 | PASS | `{"deactivation_sha256": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "expected_deactivation": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "expected_full": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "full_sha256": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e"}` |
| 4 | PASS | `{"main_member": "npidata_pfile_20050523-20261011.csv", "practice_member": "pl_pfile_20050523-20261011.csv", "resolved": {"deactivation": "NPI Deactivation Date", "entity": "Entity Type Code", "enumeration": "Provider Enumeration Date", "npi": "NPI", "primary_switch_columns": 15, "reactivation": "NPI Reactivation Date", "state": "Provider Business Practice Location Address State Name", "subpart": "Is Organization Subpart", "taxonomy_columns": 15}}` |
| 5 | PASS | `{"bad_enumeration": 0, "bad_primary": 0, "bad_state": 1278, "eligible": 1978439, "excluded_reactivated": 0, "threshold": 1000000}` |
| 6 | PASS | `{"exposed_multi_taxonomy": 409936, "threshold": 250000}` |
| 7 | PASS | `{"control_single_taxonomy": 1568503, "threshold": 700000}` |
| 8 | PASS | `{"all_strata": 68801, "common_strata": 31791, "threshold": 1000}` |
| 9 | PASS | `{"all_total_locations_ge_1": true, "eligible": 1978439, "practice_secondary_rows": 1274332, "secondary_rows_joined_to_eligible": 135144}` |
| 10 | PASS | `{"coverage": 0.9707417743257484, "exposed": 409936, "exposed_in_common_strata": 397942, "threshold": 0.6}` |
| 11 | PASS | `{"matched_pairs": 346859, "threshold": 200000}` |
| 12 | PASS | `{"comparator_reuse": 0, "cross_stratum_pairs": 0, "pairs": 346859, "unique_controls": 346859, "unique_exposed": 346859}` |
| 13 | PASS | `{"abs": 0.008089949330951387, "age_days_smd": 0.008089949330951387, "threshold": 0.1}` |
| 14 | PASS | `{"abs": 0.01358494151547246, "practice_location_count_smd": 0.01358494151547246, "threshold": 0.1}` |
| 15 | PASS | `{"arm_join_performed": false, "recent_global_deactivated_npis": 69550, "threshold": 20000, "window": "2024-10-13..2026-10-12"}` |
| 16 | PASS | `{"excluded_reactivated": 0, "included_with_nonblank_reactivation": 0}` |
| 17 | PASS | `{"arm_specific_deactivation_lookup": false, "causal": false, "future_membership_opened": false, "identity_repair": false, "later_monthly_body_opened": false, "prediction": false, "ranking": false, "relationship": false, "weekly_body_opened": false}` |
| 18 | PASS | `{"contract_sha": "29ab6cd8368801137eff94463a5b405c1fdf10ac", "cost_usd": 0, "deactivation_sha256": "fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1", "full_sha256": "45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e", "runner_sha256": "56d744745dc7309b5f7b3fa45c96692eb8c25a58fba31b3dee35d6228c792bbe"}` |

No weekly/later monthly row body was opened. Historical deactivation support was counted globally only and never joined to study arms.
