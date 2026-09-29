# EU-EMA-MA-F01 — Attempt 01

**Disposition:** `IMPLEMENTATION_BLOCKED_EU_EMA_MA_F01_ATTEMPT_01`

- Attempt valid: `False`
- Gates passed: **4/18**
- Failed gates: `[]`
- Future event membership opened: **False**
- Cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 175, "active_research": "EU-EMA-MA-F01", "checkpoint_id": "CHK-20260929-EU-EMA-MA-F01-ACTIVE", "last_completed_issue": 174, "last_completed_research": "PORTFOLIO-R44", "last_decision": "DEC-260", "updated": "2026-09-29"}` |
| 2 | PASS | `{"contract_sha": "215cd9dd74a358e412a86de5d41a039c2f8186cb", "issue": 175}` |
| 3 | PASS | `{"data": {"bytes": 85294, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790631277-gzip\"", "last_modified": "Mon, 28 Sep 2026 21:34:37 GMT", "sha256": "f858cb5537810a56bbc616bae61e239207e643b8815d8250cc8dcfbf76345c16", "status": 200, "url": "https://www.ema.europa.eu/en/medicines/download-medicine-data"}, "json": {"bytes": 120776, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790655103-gzip\"", "last_modified": "Tue, 29 Sep 2026 04:11:43 GMT", "sha256": "0919eff15fafdcb01212d5277b9b40610c44109bdcd636cb13314d29b92d77fa", "status": 200, "url": "https://www.ema.europa.eu/en/about-us/about-website/download-website-data-json-data-format"}, "status": {"bytes": 142915, "content_type": "text/html; charset=UTF-8", "etag": "W/\"1790633671-gzip\"", "last_modified": "Mon, 28 Sep 2026 22:14:31 GMT", "sha256": "08b3866de2aaf1b9d6bfeb698edb5fdc38ba09996bed08bda7123e4c34d53f03", "status": 200, "url": "https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/...` |
| 4 | PASS | `{"download_url": "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"}` |

## Implementation error

`{'type': 'InvalidFileException', 'message': 'openpyxl does not support .bin file format, please check you can open it with Excel first. Supported formats are: .xlsx,.xlsm,.xltx,.xltm'}`

No post-2026-09-29 future event membership was opened.
