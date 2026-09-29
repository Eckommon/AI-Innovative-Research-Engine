# US-MSHA-MINE-N01 — Baseline Attempt 01

**Disposition:** `HOLD_US_MSHA_MINE_N01_PROSPECTIVE_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **15/18**
- Failed gates: `[6, 11, 14]`
- Future membership opened: **False**
- Locked cohort pairs: **964**
- Cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 178, "active_research": "US-MSHA-MINE-N01", "checkpoint_id": "CHK-20260929-US-MSHA-MINE-N01-ACTIVE", "last_completed_issue": 177, "last_completed_research": "US-MSHA-MINE-F01", "last_decision": "DEC-266", "updated": "2026-09-29"}` |
| 2 | PASS | `{"contract_sha": "1d5f60ac0fca0aa81fad325bfc12e716ef370fec", "issue": 178}` |
| 3 | PASS | `{"actual": {"accidents": "db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6", "employment": "4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960", "mines": "3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7"}, "expected": {"accidents": "db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6", "employment": "4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960", "mines": "3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7"}, "http": {"accidents": 200, "employment": 200, "mines": 200}}` |
| 4 | PASS | `{"accidents_delimiter": "|", "accidents_headers": ["MINE_ID", "CONTROLLER_ID", "CONTROLLER_NAME", "OPERATOR_ID", "OPERATOR_NAME", "CONTRACTOR_ID", "DOCUMENT_NO", "SUBUNIT_CD", "SUBUNIT", "ACCIDENT_DT", "CAL_YR", "CAL_QTR", "FISCAL_YR", "FISCAL_QTR", "ACCIDENT_TIME", "DEGREE_INJURY_CD", "DEGREE_INJURY", "FIPS_STATE_CD", "UG_LOCATION_CD", "UG_LOCATION", "UG_MINING_METHOD_CD", "UG_MINING_METHOD", "MINING_EQUIP_CD", "MINING_EQUIP", "EQUIP_MFR_CD", "EQUIP_MFR_NAME", "EQUIP_MODEL_NO", "SHIFT_BEGIN_TIME", "CLASSIFICATION_CD", "CLASSIFICATION", "ACCIDENT_TYPE_CD", "ACCIDENT_TYPE", "NO_INJURIES", "TOT_EXPER", "MINE_EXPER", "JOB_EXPER", "OCCUPATION_CD", "OCCUPATION", "ACTIVITY_CD", "ACTIVITY", "INJURY_SOURCE_CD", "INJURY_SOURCE", "NATURE_INJURY_CD", "NATURE_INJURY", "INJ_BODY_PART_CD", "INJ_BODY_PART", "SCHEDULE_CHARGE", "DAYS_RESTRICT", "DAYS_LOST", "TRANS_TERM", "RETURN_TO_WORK_DT", "IMMED_NOTIFY_CD", "IMMED_NOTIFY", "INVEST_BEGIN_DT", "NARRATIVE", "CLOSED_DOC_NO", "COAL_METAL_IND"], "accidents_member": "Accidents.txt", "employment_delimiter": "|", "employment_headers": ["MINE_ID", "CURR_MINE_NM", "STATE", "SUBUNIT_CD", "SUBUNIT", "CAL_YR", "CAL_QTR", "FISCAL_YR", "FISCAL_QTR", "AVG_EMP...` |
| 5 | PASS | `{"eligible_mines": 6894, "threshold": 5000}` |
| 6 | FAIL | `{"qualifying_strata": 6, "strata_sizes": {"C|Facility": 172, "C|Surface": 252, "C|Underground": 153, "M|Facility": 306, "M|Surface": 5807, "M|Underground": 204}, "threshold": 8}` |
| 7 | PASS | `{"ramp_up_mines": 1722, "threshold": 1000}` |
| 8 | PASS | `{"comparator_mines": 3447, "threshold": 2000}` |
| 9 | PASS | `{"construction": "pre-cutoff frozen rows only; Degree 01/02 or Immediate 01/02", "distinct_prior_severe_mines": 123, "prior_window_end": "2026-09-29", "prior_window_start": "2025-09-30"}` |
| 10 | PASS | `{"matched_pairs": 964, "threshold": 800}` |
| 11 | FAIL | `{"coverage": 0.5598141695702671, "exposed": 1722, "matched_pairs": 964, "threshold": 0.6}` |
| 12 | PASS | `{"abs_smd": 0.019658093317916587, "smd": -0.019658093317916587, "threshold": 0.1}` |
| 13 | PASS | `{"abs_smd": 0.01739667542281701, "smd": 0.01739667542281701, "threshold": 0.1}` |
| 14 | FAIL | `{"abs_smd": 0.1240167574812327, "smd": -0.1240167574812327, "threshold": 0.1}` |
| 15 | PASS | `{"distinct_eligible_serious_fatal_mines": 54, "historical_plausibility_window": ["2026-03-30", "2026-09-29"], "threshold": 40}` |
| 16 | PASS | `{"future_membership_opened": false, "future_rows_seen_but_severity_not_used": 0}` |
| 17 | PASS | `{"causal": false, "future_pvalue": false, "future_rd": false, "future_relationship": false, "future_rr": false, "identity_repair": false, "ranking": false}` |
| 18 | PASS | `{"contract_sha": "1d5f60ac0fca0aa81fad325bfc12e716ef370fec", "cost_usd": 0, "runner_sha256": "269220ad63bff158daa21e07e030c55db18933ed3cd6de7db288254f382d2846", "source_sha256": {"accidents": "db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6", "employment": "4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960", "mines": "3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7"}}` |

No post-2026-09-29 serious/fatal event membership or future relationship statistic was opened/computed.
