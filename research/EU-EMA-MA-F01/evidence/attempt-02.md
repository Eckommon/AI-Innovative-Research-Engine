# EU-EMA-MA-F01 — Attempt 02

**Disposition:** `HOLD_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_NOT_READY`

- Attempt valid: `True`
- Gates passed: **15/18**
- Failed gates: `[9, 12, 14]`
- Future event membership opened: **False**
- Cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 175, "active_research": "EU-EMA-MA-F01", "checkpoint_id": "CHK-20260929-EU-EMA-MA-F01-ACTIVE", "last_completed_issue": 174, "last_completed_research": "PORTFOLIO-R44", "last_decision": "DEC-260", "updated": "2026-09-29"}` |
| 2 | PASS | `{"contract_sha": "215cd9dd74a358e412a86de5d41a039c2f8186cb", "issue": 175}` |
| 3 | PASS | `{"data": {"bytes": 85884, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790672113-gzip\"", "last_modified": "Tue, 29 Sep 2026 08:55:13 GMT", "sha256": "d837f354b03f4ab5e5aed891cb7b23ff303f4646d10801aa62b51306f49f6f72", "status": 200, "url": "https://www.ema.europa.eu/en/medicines/download-medicine-data"}, "json": {"bytes": 119815, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790672115-gzip\"", "last_modified": "Tue, 29 Sep 2026 08:55:15 GMT", "sha256": "229de27f5096b60a6ecb79093bc116f95c7e47366caac2c576bc5b5185777178", "status": 200, "url": "https://www.ema.europa.eu/en/about-us/about-website/download-website-data-json-data-format"}, "status": {"bytes": 143248, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790672103-gzip\"", "last_modified": "Tue, 29 Sep 2026 08:55:03 GMT", "sha256": "851da31313cfc932824fe44dd09b0dc3c3cc17067b3891b71da625811c13aea5", "status": 200, "url": "https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/...` |
| 4 | PASS | `{"download_url": "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"}` |
| 5 | PASS | `{"headers": ["Category", "Name of medicine", "EMA product number", "Medicine status", "Opinion status", "Latest procedure affecting product information", "International non-proprietary name (INN) / common name", "Active substance", "Therapeutic area (MeSH)", "Species\n(veterinary)", "Patient safety", "ATC code (human)", "ATCvet code (veterinary)", "Pharmacotherapeutic group\n(human)", "Pharmacotherapeutic group\n(veterinary)", "Therapeutic indication", "Accelerated assessment", "Additional monitoring", "Advanced therapy", "Biosimilar", "Conditional approval", "Exceptional circumstances", "Generic", "Orphan medicine", "PRIME: priority medicine", "Marketing authorisation developer / applicant / holder", "European Commission decision date", "Start of rolling review date", "Start of evaluation date", "Opinion adopted date", "Withdrawal of application date", "Marketing authorisation date", "Refusal of marketing authorisation date", "Withdrawal / expiry / revocation / lapse of marketing a...` |
| 6 | PASS | `{"nonblank": 2351, "rate": 1.0, "valid": 2351}` |
| 7 | PASS | `{"distinct_human_ids": 2351, "threshold": 1000}` |
| 8 | PASS | `{"authorised_ids": 1573, "status_counts": {"Application withdrawn": 268, "Authorised": 1573, "Expired": 17, "Lapsed": 27, "Opinion": 25, "Opinion under re-examination": 2, "Refused": 64, "Revoked": 9, "Suspended": 1, "Withdrawn": 363, "Withdrawn from rolling review": 2}, "threshold": 750}` |
| 9 | FAIL | `{"rate": 0.9204593789876648, "threshold": 0.99}` |
| 10 | PASS | `{"rate": 1.0, "threshold": 0.99}` |
| 11 | PASS | `{"candidate_pages": 120, "qualified_withdrawn_authorisations": 93, "threshold": 25}` |
| 12 | FAIL | `{"date_sane": 54, "qualified": 93, "rate": 0.5806451612903226, "threshold": 0.95}` |
| 13 | PASS | `{"classes": {"OTHER_UNKNOWN": 24, "VOLUNTARY_COMMERCIAL": 69}, "qualified": 93, "rate": 1.0, "reason_supported": 93}` |
| 14 | FAIL | `{"expiry": true, "initial_application_withdrawal": false, "post_authorisation": true, "suspension": true}` |
| 15 | PASS | `{"rate": 1.0, "threshold": 0.95}` |
| 16 | PASS | `{"future_entity_pages_consumed": 0, "future_event_membership_opened": false}` |
| 17 | PASS | `{"causal": false, "identity_repair": false, "prediction": false, "ranking": false, "relationship": false}` |
| 18 | PASS | `{"baseline_sha256": "5a9c27c2a91282b6305b7721c3458638e0d08a2618dc0b327dcec18d4002cdcf", "contract_sha": "215cd9dd74a358e412a86de5d41a039c2f8186cb", "cost_usd": 0, "runner_sha256": "85aae68a4864f92641b51521232dece8f3b2074971eea8d08ac49c184fcccddc"}` |

No post-2026-09-29 future event membership was opened.
