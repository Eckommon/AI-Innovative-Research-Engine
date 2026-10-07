# US-FRA-RR-F01 — Attempt 02

**Disposition:** `IMPLEMENTATION_BLOCKED_US_FRA_RR_F01_ATTEMPT_02`

- Attempt valid: `False`
- Gates passed: **5/18**
- Failed gates: `[]`
- Future 2026+ accident membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 196, "active_research": "US-FRA-RR-F01", "checkpoint_id": "CHK-20261008-US-FRA-RR-F01-ACTIVE", "last_completed_issue": 195, "last_completed_research": "PORTFOLIO-R54", "last_decision": "DEC-304", "updated": "2026-10-08"}` |
| 2 | PASS | `{"contract_sha": "492e2a29261e786fe115fa9eaf2f89a8862fa5a6", "issue": 196}` |
| 3 | PASS | `{"landing_status": 200, "operations_present": ["GetAccident54DataByRailroad", "GetAccident55DataByRailroad", "GetF54Schema", "GetF55Schema", "GetRailroadData"], "signatures": {"GetAccident54DataByRailroad": ["year"], "GetAccident55DataByRailroad": ["year"], "GetF54Schema": [], "GetF55Schema": [], "GetRailroadData": []}, "wsdl_status": 200}` |
| 4 | PASS | `{"meta": {"bytes": 304821, "content_type": "text/xml; charset=utf-8", "sha256": "c663b75904dd35e71f85280430e5583c1660c143ce0172e08ae447fbde8b478f", "status": 200, "url": "https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx"}, "row_candidates": 2981, "sample_fields": ["Name", "Railroad"]}` |
| 5 | PASS | `{"f54_bytes": 19652, "f54_has_railroad": true, "f55_bytes": 3924, "f55_has_railroad": true}` |

## Implementation error

`{'type': 'HTTPError', 'message': '500 Server Error: Internal Server Error for url: https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx'}`

Only 2020–2025 historical service calls were authorized. No 2026+ Form54 accident membership was opened.
