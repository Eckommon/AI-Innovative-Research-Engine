# US-FCC-ULS-F01 — Attempt 01

**Disposition:** `IMPLEMENTATION_BLOCKED_US_FCC_ULS_F01_ATTEMPT_01`

- Attempt valid: `False`
- Gates passed: **3/18**
- Failed gates: `[]`
- Future daily rows opened: **0**
- Future cancelled/terminated membership opened: **False**
- Daily entity-body bytes consumed: **0**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 166, "active_research": "US-FCC-ULS-F01", "checkpoint_id": "CHK-20260921-US-FCC-ULS-F01-ACTIVE", "last_completed_issue": 165, "last_completed_research": "PORTFOLIO-R40", "last_decision": "DEC-242", "updated": "2026-09-21"}` |
| 2 | PASS | `{"contract_sha": "287f0e3dfe203beee3d9ca1f21e67e51ef2db6a5", "issue": 166}` |
| 3 | FAIL | `{"https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf": {"bytes": 225341, "content_length_header": "225341", "content_type": "application/pdf", "final_url": "https://wireless.fcc.gov/uls/documentation/pa_intro24.pdf", "last_modified": "Tue, 02 Dec 2014 21:38:00 GMT", "sha256": "df03acbcbf5c080a077d04c9a672508b9a8ec962788742731e1e1f02c401cefe", "status": 200}, "https://wireless.fcc.gov/uls/releases/d992205c.pdf": {"bytes": 24205, "content_length_header": "24205", "content_type": "application/pdf", "final_url": "https://wireless.fcc.gov/uls/releases/d992205c.pdf", "last_modified": "Thu, 01 Nov 2001 14:59:53 GMT", "sha256": "dbc63ca7015d7bc059a58b622df8b577c23cf7e20698d87c3c5cc767b320298f", "status": 200}, "https://wireless.fcc.gov/wtbfiles/pa_ddef51.pdf": {"bytes": 547619, "content_length_header": "547619", "content_type": "application/pdf", "final_url": "https://wireless.fcc.gov/...` |
| 4 | PASS | `{"complete": "l_micro.zip", "daily": ["l_mw_mon.zip", "l_mw_tue.zip", "l_mw_wed.zip", "l_mw_thu.zip", "l_mw_fri.zip"], "family": "Microwave and Microwave Broadcast Auxiliary"}` |

## Implementation error

`{'type': 'HTTPError', 'message': 'HTTP Error 403: Forbidden'}`

No future Microwave daily transaction body was opened by this attempt. Scientific thresholds were not modified.
