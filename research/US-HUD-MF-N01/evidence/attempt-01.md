# US-HUD-MF-N01 — Attempt 01

**Disposition:** `HOLD_US_HUD_MF_N01_MATCHED_INSPECTION_DESIGN_NOT_IDENTIFIABLE`

- Attempt valid: `True`
- Gates passed: **17/18**
- Failed gates: `[15]`
- Future terminated rows opened: **0**
- Future adverse membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 169, "active_research": "US-HUD-MF-N01", "checkpoint_id": "CHK-20260928-US-HUD-MF-N01-ACTIVE", "last_completed_issue": 168, "last_completed_research": "US-HUD-MF-F01", "last_decision": "DEC-248", "updated": "2026-09-28"}` |
| 2 | PASS | `{"contract_sha": "01c5a19215a30572c74309cd5b1dbe9851880224", "issue": 169}` |
| 3 | PASS | `{"expected": {"active": "72ae185f05fd94a5eda54dc55cd36332153c2307b88776fdc139d41a266e5c36", "inspection": "0ff6b86e54762df917058bca832088f343dc174e78332b002dc6fbfa400cd883", "property": "6c375b2b3491d7c7931ce58a1f715a8632a6ceb05b6c10a36ff8624b9c547a01"}, "observed": {"active": "72ae185f05fd94a5eda54dc55cd36332153c2307b88776fdc139d41a266e5c36", "inspection": "0ff6b86e54762df917058bca832088f343dc174e78332b002dc6fbfa400cd883", "property": "6c375b2b3491d7c7931ce58a1f715a8632a6ceb05b6c10a36ff8624b9c547a01"}}` |
| 4 | PASS | `{"distinct": 15632, "expected": 15632, "nonblank": 15632, "valid": 15632}` |
| 5 | PASS | `{"excluded_multi_property": 0, "mapped": 15425}` |
| 6 | PASS | `{"deterministic_latest_property_ids": 23865, "excluded_same_date_score_conflicts": 0}` |
| 7 | PASS | `{"eligible": 8247, "exclusions": {"balance_ratio": 1, "inspection": 7177, "property": 207}, "threshold": 7000}` |
| 8 | PASS | `{"method": "linear", "q25": 87.0, "q75": 97.0}` |
| 9 | PASS | `{"low": 2151, "threshold": 1500}` |
| 10 | PASS | `{"high": 2116, "threshold": 1500}` |
| 11 | PASS | `{"candidate_rows": 4267, "complete": true}` |
| 12 | PASS | `{"pairs": 1438, "threshold": 1200}` |
| 13 | PASS | `{"states": 50, "threshold": 20}` |
| 14 | PASS | `{"soa_categories": 16, "threshold": 8}` |
| 15 | FAIL | `{"abs_smd": {"balance_ratio": 0.056564840910815053, "interest_rate": 0.017181695221286302, "log1p_original_mortgage": 0.08707915650410197, "log1p_units": 0.1780490313988611, "months_to_maturity": 0.05605747716327263}, "exact_soa": true, "exact_state": true, "threshold": 0.15}` |
| 16 | PASS | `{"pair_manifest_sha256": "65426aa525f0caab7544aefa8ba3259d087ea5eb5db35a27989b440d80ad812b", "projects_in_pairs": 2876, "unique_projects": 2876}` |
| 17 | PASS | `{"causal_claim_made": false, "future_adverse_membership_opened": false, "future_entity_body_bytes_consumed": 0, "future_terminated_rows_opened": 0, "prediction_computed": false, "ranking_computed": false, "relationship_computed": false}` |
| 18 | PASS | `{"cost_usd": 0, "pair_manifest_sha256": "65426aa525f0caab7544aefa8ba3259d087ea5eb5db35a27989b440d80ad812b", "runner_sha256": "18419686c25cf2df39eabd0d70f8cb78909eeda0613a974259265419f724d69f", "source_sha256": {"active": "72ae185f05fd94a5eda54dc55cd36332153c2307b88776fdc139d41a266e5c36", "inspection": "0ff6b86e54762df917058bca832088f343dc174e78332b002dc6fbfa400cd883", "property": "6c375b2b3491d7c7931ce58a1f715a8632a6ceb05b6c10a36ff8624b9c547a01"}}` |

No post-2026-09-21 terminated-mortgage body or membership was opened. N01 computed historical design support only.
