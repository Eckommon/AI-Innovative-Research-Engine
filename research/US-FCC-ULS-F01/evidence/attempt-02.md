# US-FCC-ULS-F01 — Attempt 02

**Disposition:** `HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **9/18**
- Failed gates: `[3, 8, 9, 10, 11, 12, 13, 14, 15]`
- Future daily rows opened: **0**
- Future cancelled/terminated membership opened: **False**
- Daily entity-body bytes consumed: **0**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 166, "active_research": "US-FCC-ULS-F01", "checkpoint_id": "CHK-20260921-US-FCC-ULS-F01-ACTIVE", "last_completed_issue": 165, "last_completed_research": "PORTFOLIO-R40", "last_decision": "DEC-242", "updated": "2026-09-21"}` |
| 2 | PASS | `{"contract_sha": "287f0e3dfe203beee3d9ca1f21e67e51ef2db6a5", "issue": 166}` |
| 3 | FAIL | `{"https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf": {"attempted_urls": [{"result": "selected", "status": 200, "url": "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf"}], "bytes": 225341, "content_type": "application/pdf", "contract_logical_url": "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf", "final_url": "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf", "requested_url": "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf", "sha256": "df03acbcbf5c080a077d04c9a672508b9a8ec962788742731e1e1f02c401cefe", "status": 200, "transport": "curl"}, "https://wireless.fcc.gov/uls/releases/d992205c.pdf": {"attempted_urls": [{"result": "selected", "status": 200, "url": "https://wireless.fcc.gov/uls/releases/d992205c.pdf"}], "bytes": 24205, "content_type": "application/pdf", "contract_logical_url": "https://wireless.fcc.gov/uls/releases/d992205c.pdf",...` |
| 4 | PASS | `{"complete": "l_micro.zip", "daily": ["l_mw_mon.zip", "l_mw_tue.zip", "l_mw_wed.zip", "l_mw_thu.zip", "l_mw_fri.zip"], "family": "Microwave and Microwave Broadcast Auxiliary"}` |
| 5 | PASS | `{"attempted_urls": [{"result": "selected", "status": 200, "url": "https://data.fcc.gov/download/pub/uls/complete/l_micro.zip"}], "bytes": 211037826, "content_type": "application/zip", "contract_logical_url": "https://data.fcc.gov/download/pub/uls/complete/l_micro.zip", "final_url": "https://data.fcc.gov/download/pub/uls/complete/l_micro.zip", "parseable_zip": true, "requested_url": "https://data.fcc.gov/download/pub/uls/complete/l_micro.zip", "sha256": "3ade0c1fcf335fa9d50ce4ecc9bf11b53839d7a40de49baa8f8fa7877e636803", "status": 200, "transport": "curl"}` |
| 6 | PASS | `{"HD": "HD.dat", "HS": "HS.dat"}` |
| 7 | PASS | `{"positions": {"call_sign": 5, "cancellation_date": 10, "effective_date": 43, "expired_date": 9, "grant_date": 8, "last_action_date": 44, "license_status": 6, "radio_service_code": 7, "unique_system_id": 2}, "rows": 366807, "short_rows_lt_44_fields": 0}` |
| 8 | FAIL | `{"nonblank_id_rows": 366807, "rate": 0.0, "valid_9digit_id_rows": 0}` |
| 9 | FAIL | `{"distinct_valid_system_ids": 0, "threshold": 20000}` |
| 10 | FAIL | `{"distinct_active_system_ids": 0, "threshold": 10000}` |
| 11 | FAIL | `{"counts": {"A": 165713, "C": 132479, "E": 48865, "P": 503, "T": 19247}, "documented_A_C_E_T_rows": 366304, "nonblank_status_rows": 366807, "rate": 0.998628706649546}` |
| 12 | FAIL | `{"active_rows": 0, "grant_or_effective_parseable": 0, "rate": 0.0}` |
| 13 | FAIL | `{"active_ids": 0, "active_ids_with_hs": 0, "hs_rows": 4950382, "rate": 0.0, "short_hs_rows_lt_6_fields": 0}` |
| 14 | FAIL | `{"code_and_date_valid_rows": 0, "linked_hs_rows": 0, "rate": 0.0}` |
| 15 | FAIL | `{"AN.dat": {"joinable": false, "member": "AN.dat", "overlap_hd_ids": 0, "scanned_rows_cap": 200000, "valid_id_rows": 0}, "CP.dat": {"joinable": false, "member": "CP.dat", "overlap_hd_ids": 0, "scanned_rows_cap": 74239, "valid_id_rows": 0}, "FR.dat": {"joinable": false, "member": "FR.dat", "overlap_hd_ids": 0, "scanned_rows_cap": 200000, "valid_id_rows": 0}, "LO.dat": {"joinable": false, "member": "LO.dat", "overlap_hd_ids": 0, "scanned_rows_cap": 200000, "valid_id_rows": 0}, "MW.dat": {"joinable": false, "member": "MW.dat", "overlap_hd_ids": 0, "scanned_rows_cap": 200000, "valid_id_rows": 0}}` |
| 16 | PASS | `{"https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip": {"attempted_urls": [{"result": "selected", "status": 200, "url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip"}], "content_type": "application/zip", "contract_logical_url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip", "entity_body_bytes_consumed": 0, "final_url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip", "method": "HEAD", "requested_url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_fri.zip", "status": 200, "transport": "curl"}, "https://data.fcc.gov/download/pub/uls/daily/l_mw_mon.zip": {"attempted_urls": [{"result": "selected", "status": 200, "url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_mon.zip"}], "content_type": "application/zip", "contract_logical_url": "https://data.fcc.gov/download/pub/uls/daily/l_mw_mon.zip", "entity_body_bytes_consumed": 0, "final_url": ...` |
| 17 | PASS | `{"causal_claim_made": false, "daily_entity_body_bytes_consumed": 0, "future_cancelled_terminated_membership_opened": false, "future_daily_rows_opened": 0, "future_relationship_computed": false, "name_address_call_sign_only_fuzzy_geo_manual_identity_repair_used": false, "predictive_metric_computed": false, "ranking_computed": false}` |
| 18 | PASS | `{"baseline_sha256": "3ade0c1fcf335fa9d50ce4ecc9bf11b53839d7a40de49baa8f8fa7877e636803", "contract_sha": "287f0e3dfe203beee3d9ca1f21e67e51ef2db6a5", "cost_usd": 0, "runner_sha256": "33290528493ec5efa8e35501ae36c93abcc5b625a61c364465fb37a958303cf6"}` |

No future Microwave daily transaction body was opened by this attempt. Scientific thresholds were not modified.

## Attempt 02 transport-only correction

- Correction commit: `486624cf803c291217baef97b8514294691fce82`
- Base runner commit: `92bbf04d8a9786f9c62417f24fd0d16dc74828a4`
- Transport changed: Python urllib → curl with redirects/browser-compatible headers and FCC-owned endpoint variants only.
- Scientific thresholds changed: **false**
- Service family changed: **false**
- Identity rule changed: **false**
- Future window changed: **false**
- Future daily transaction bodies opened: **0**
