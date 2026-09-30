# US-SEC-IA-F01 — Attempt 01

**Disposition:** `HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **5/18**
- Failed gates: `[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- Post-cutoff ADV-W body opened: **False**
- Future ADV-W membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 187, "active_research": "US-SEC-IA-F01", "checkpoint_id": "CHK-20260930-US-SEC-IA-F01-ACTIVE", "last_completed_issue": 186, "last_completed_research": "PORTFOLIO-R49", "last_decision": "DEC-285", "updated": "2026-09-30"}` |
| 2 | PASS | `{"contract_sha": "2734008b75116779d410ffec1e3ca44343e3e1f9", "issue": 187}` |
| 3 | PASS | `{"advw_form": {"bytes": 260841, "content_length_header": "260841", "content_type": "application/pdf", "etag": null, "final_url": "https://www.sec.gov/files/formadv-w.pdf", "last_modified": "Wed, 26 Aug 2026 20:57:27 GMT", "sha256": "e7a8daf7f8547af52049900b8f518d56bcb901b6cd834b1336e08f0668887d22", "status": 200}, "faq": {"bytes": 206659, "content_length_header": null, "content_type": "text/html; charset=utf-8", "etag": "\"1790717113-gzip\"", "final_url": "https://www.sec.gov/about/divisions-offices/division-investment-management/electronic-filing-investment-advisers-iard/frequently-asked-questions-form-adv-iard", "last_modified": "Tue, 29 Sep 2026 21:25:13 GMT", "sha256": "64b47dd4922623f89537379ed21dd35320fab9cea4dad9b2dfb086af92201759", "status": 200}, "historical_adv": {"bytes": 86000, "content_length_header": "15255", "content_type": "text/html; charset=utf-8", "etag": "\"1790716903-gzip\"", "final_url": "https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data", "last_modified": "Tue, 29 Sep 2026 21:21:43 GMT", "sha256": "eda9f73bf66b162800b9bce04ed9ddfb47ba092746b81444bead961c4ce733c4", "status": 200}, "iapd_adv": {"bytes": 4160, "content_length_header": null, "content_type": "text/html", "etag": null, "final_url": "https://adviserinfo.sec.gov/adv", "last_modified": "Tue, 22 Sep 2026 22:04:44 GMT", "sha256": "1dbdc21269fff9fd3cbf485e99a585a061f300cd7033d663f9aa44d3a8e8531b", "status": 200}, "reports": {"bytes": 421662, "content_length_header": "21316", "content_type": "text/html; charset=utf-8", "etag": "\"1790730323-gzip\"", "final_url": "ht...` |
| 4 | FAIL | `{"all_external_zip": false, "expected_months": ["2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08"], "formats": {"2025-09": "XLSX", "2025-10": "PDF", "2025-11": "PDF", "2025-12": "ZIP", "2026-01": "ZIP", "2026-02": "ZIP", "2026-03": "ZIP", "2026-04": "ZIP", "2026-05": "ZIP", "2026-06": "ZIP", "2026-07": "ZIP", "2026-08": "ZIP"}, "resolved_count": 12, "urls": {"2025-09": "https://www.sec.gov/files/investment/data/information-about-registered-investment-advisers-exempt-reporting-advisers/ia09022025.xlsx", "2025-10": "https://www.sec.gov/files/investment/data/information-about-registered-investment-advisers-exempt-reporting-advisers/ia-no-data-100125.pdf", "2025-11": "https://www.sec.gov/files/investment/data/information-about-registered-investment-advisers-exempt-reporting-advisers/ia-no-data-110125.pdf", "2025-12": "https://www.sec.gov/files/investment/data/information-about-registered-investment-advisers-exempt-reporting-advisers/ia122025.zip", "2026-01": "https://www.sec.gov/files/investment/data/information-about-registered-investment-advisers-exempt-reporting-advisers/ia010226.zip", "2026-02": "https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia020226.zip", "2026-03": "https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exempt-reporting-advisers/ia030226.zip", "2026-04": "https://www.sec.gov/files/investment/data/other/information-about-registered-investment-advisers-exemp...` |
| 5 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 6 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 7 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 8 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 9 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 10 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 11 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 12 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 13 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 14 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 15 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 16 | FAIL | `{"not_evaluated_after_decisive_gate4_failure": true}` |
| 17 | PASS | `{"causal": false, "future_membership_opened": false, "identity_repair": false, "post_cutoff_advw_body_opened": false, "prediction": false, "prohibited_exposure": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"contract_sha": "2734008b75116779d410ffec1e3ca44343e3e1f9", "cost_usd": 0, "historical_advw_body_opened": false, "runner_sha256": "df09f1aa08e80cbf94646775b0875167cd1c4f2185f79e8ca16eb78e7242f889"}` |

No historical or post-cutoff ADV-W row body was opened after a decisive Gate 4 source-lineage failure. No relationship or predictive metric was computed.
