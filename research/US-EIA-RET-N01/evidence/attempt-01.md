# US-EIA-RET-N01 — Attempt 01

**Disposition:** `HOLD_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_NOT_READY`

- Attempt valid: `True`
- Gates passed: **16/18**
- Failed gates: `[10, 11]`
- Future retirement membership opened: **False**
- Post-August-2026 860M body opened: **False**
- Planned-retirement exposure used: **False**
- EIA-923 row bodies opened: **0**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"checkpoint": {"active_issue": 185, "active_research": "US-EIA-RET-N01", "checkpoint_id": "CHK-20260930-US-EIA-RET-N01-ACTIVE", "last_completed_issue": 184, "last_completed_research": "US-EIA-RET-F01", "last_decision": "DEC-281", "updated": "2026-09-30"}, "f01_disposition": "PASS_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_READY", "f01_evidence_commit": "d96ccc4346484cb39f719f98eeaca75b142d1301", "f01_pass_count": 18}` |
| 2 | PASS | `{"contract_sha": "21f28f1cefe65043493a8b3e7c55f0b9e033b212", "issue": 185}` |
| 3 | PASS | `{"all_12_match": true, "expected_sha256": {"2025-09": "069de3bee5de7c560297a814a3e90beeb6b5e10642c5c83bf4a49c4ef74da08b", "2025-10": "cf560a5e9f3b4438bf5a1e485e07f6eee50fe16b52e224480c61e7fcb060a308", "2025-11": "5dc458f278b68504830b048b8728539f104057de100f8eae6ed301d3d603ea12", "2025-12": "1264f1c37cf51ef41319067c4c0915f951535851df93c97d02e2e823e337ea2b", "2026-01": "a02a0262c98e6b4fc8451e3f88c3983c2edd015b1bff2c5174df91e331ae9cf8", "2026-02": "9f76e3a186ba0814ea836a357213bab0ea8e18955d862a92e877dc028af755e8", "2026-03": "93f2b2501cd42ba1290136ec04fd616346d974e0dfd6020cd8ec5e532ef7cec6", "2026-04": "ec15bae939cc7cf8ee7e3f0dcb9a06d0f91d5fbab3714f0f36ecaeef3bde82b6", "2026-05": "46ff71d90723e4dfe766f6fe191160d92ff28cb17d5d5f5a55eeed562067995d", "2026-06": "47d28a1e5599135b619d249971f35f03fef8a5b3062c2d66c436b55e8f8c3072", "2026-07": "9f348be6d6609b7e0c49a8c3cf872354a3bd2370051d0d4720246dc81bbe540d", "2026-08": "b4b70abb4c217e8e2658c3bde7608a3d530e86a81279ccc572ced82a200e9f1c"}, "match_by_month": {"2025-09": true, "2025-10": true, "2025-11": true, "2025-12": true, "2026-01": true, "2026-02": true, "2026-03": true, "2026-04": true, "2026-05": true, "2026-06": true, "2026-07": true, "2026-08": true}, "observed_sha256": {"2025-09": "069de3bee5de7c560297a814a3e90beeb6b5e10642c5c83bf4a49c4ef74da08b", "2025-10": "cf560a5e9f3b4438bf5a1e485e07f6eee50fe16b52e224480c61e7fcb060a308", "2025-11": "5dc458f278b68504830b048b8728539f104057de100f8eae6ed301d3d603ea12", "2025-12": "1264f1c37cf5...` |
| 4 | PASS | `{"duplicate_exact_pairs": 0, "header_row_1based": 3, "headers": ["ENTITY ID", "ENTITY NAME", "PLANT ID", "PLANT NAME", "GOOGLE MAP", "BING MAP", "PLANT STATE", "COUNTY", "BALANCING AUTHORITY CODE", "SECTOR", "GENERATOR ID", "UNIT CODE", "NAMEPLATE CAPACITY MW", "NET SUMMER CAPACITY MW", "NET WINTER CAPACITY MW", "TECHNOLOGY", "ENERGY SOURCE CODE", "PRIME MOVER CODE", "OPERATING MONTH", "OPERATING YEAR", "PLANNED RETIREMENT MONTH", "PLANNED RETIREMENT YEAR", "STATUS", "NAMEPLATE ENERGY CAPACITY MWH", "DC NET CAPACITY MW", "PLANNED DERATE YEAR", "PLANNED DERATE MONTH", "PLANNED DERATE OF SUMMER CAPACITY MW", "PLANNED UPRATE YEAR", "PLANNED UPRATE MONTH", "PLANNED UPRATE OF SUMMER CAPACITY MW", "PLANNED REPOWER YEAR", "PLANNED REPOWER MONTH", "OTHER MODIFICATION YEAR", "OTHER MODIFICATION MONTH", "LATITUDE", "LONGITUDE"], "missing": []}` |
| 5 | PASS | `{"appear_in_6plus_months": 27757, "august_exact_pairs": 28377, "rate": 0.9781513197307679, "threshold": 0.9}` |
| 6 | PASS | `{"eligible_generators": 27756, "excluded_reasons": {"continuity_lt6": 620, "missing_category": 1}, "threshold": 15000}` |
| 7 | PASS | `{"PURE_SINGLETON": 10793, "REDUNDANT_3PLUS": 12323, "excluded": {"group_size_2": 3936, "singleton_at_mixed_or_multi_plant": 704}, "threshold_each": 3000}` |
| 8 | PASS | `{"common_exact_strata": 389, "control_strata": 1558, "exposed_strata": 1660, "threshold": 50}` |
| 9 | PASS | `{"caliper_failures": 0, "duplicate_control_use": 0, "exact_stratum_mismatch": 0, "matched_pairs": 881}` |
| 10 | FAIL | `{"matched_pairs": 881, "threshold": 2000}` |
| 11 | FAIL | `{"coverage": 0.07149233141280532, "eligible_exposed": 12323, "matched_exposed": 881, "threshold": 0.4}` |
| 12 | PASS | `{"distinct_exposed_plants": 397, "threshold": 300}` |
| 13 | PASS | `{"distinct_control_plants": 873, "threshold": 300}` |
| 14 | PASS | `{"cross_arm_plant_overlap_count": 0, "examples": []}` |
| 15 | PASS | `{"abs_smd": 0.0033221173612753025, "smd_log_capacity": -0.0033221173612753025, "threshold": 0.1}` |
| 16 | PASS | `{"abs_smd": 0.0018628286749489966, "smd_operating_age": 0.0018628286749489966, "threshold": 0.1}` |
| 17 | PASS | `{"causal": false, "eia923_row_bodies_opened": 0, "exact_category_mismatch": 0, "future_retirement_membership_opened": false, "identity_repair": false, "max_single_plant_share_control": 0.0022701475595913734, "max_single_plant_share_exposed": 0.011350737797956867, "planned_proposed_row_bodies_opened": 0, "planned_retirement_used_as_exposure": false, "post_august_2026_860m_body_opened": false, "prediction": false, "ranking": false, "relationship": false, "retired_row_bodies_opened": 0, "threshold": 0.02}` |
| 18 | PASS | `{"contract_sha": "21f28f1cefe65043493a8b3e7c55f0b9e033b212", "cost_usd": 0, "f01_evidence_commit": "d96ccc4346484cb39f719f98eeaca75b142d1301", "matched_manifest_rows": 881, "matched_manifest_sha256": "1f38b2f9b028aed41c7ae431f81606a41943a8ef56e8f16357db9549e6908f39", "runner_sha256": "e6cc3f6f803259a9f3600fdc6ebbeb176eb2c593262da273f024c5c3dacd24b9", "source_sha256": {"2025-09": "069de3bee5de7c560297a814a3e90beeb6b5e10642c5c83bf4a49c4ef74da08b", "2025-10": "cf560a5e9f3b4438bf5a1e485e07f6eee50fe16b52e224480c61e7fcb060a308", "2025-11": "5dc458f278b68504830b048b8728539f104057de100f8eae6ed301d3d603ea12", "2025-12": "1264f1c37cf51ef41319067c4c0915f951535851df93c97d02e2e823e337ea2b", "2026-01": "a02a0262c98e6b4fc8451e3f88c3983c2edd015b1bff2c5174df91e331ae9cf8", "2026-02": "9f76e3a186ba0814ea836a357213bab0ea8e18955d862a92e877dc028af755e8", "2026-03": "93f2b2501cd42ba1290136ec04fd616346d974e0dfd6020cd8ec5e532ef7cec6", "2026-04": "ec15bae939cc7cf8ee7e3f0dcb9a06d0f91d5fbab3714f0f36ecaeef3bde82b6", "2026-05": "46ff71d90723e4dfe766f6fe191160d92ff28cb17d5d5f5a55eeed562067995d", "2026-06": "47d28a1e5599135b619d249971f35f03fef8a5b3062c2d66c436b55e8f8c3072", "2026-07": "9f348be6d6609b7e0c49a8c3cf872354a3bd2370051d0d4720246dc81bbe540d", "2026-08": "b4b70abb4c217e8e2658c3bde7608a3d530e86a81279ccc572ced82a200e9f1c"}}` |

No Retired, Planned/Proposed, EIA-923, or post-August-2026 row body was opened. No retirement outcome, relationship, prediction, ranking, or causal metric was computed.
