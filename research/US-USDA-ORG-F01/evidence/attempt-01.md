# US-USDA-ORG-F01 — Attempt 01

**Disposition:** `IMPLEMENTATION_BLOCKED_US_USDA_ORG_F01_ATTEMPT_01`

- Attempt valid: `False`
- Gates passed: **3/18**
- Failed gates: `[]`
- Future Suspended/Revoked membership opened: **False**
- Incremental monetary cost: **0 USD**

## Gate ledger

| Gate | PASS | Observed |
|---:|:---:|---|
| 1 | PASS | `{"active_issue": 180, "active_research": "US-USDA-ORG-F01", "checkpoint_id": "CHK-20260929-US-USDA-ORG-F01-ACTIVE", "last_completed_issue": 179, "last_completed_research": "PORTFOLIO-R46", "last_decision": "DEC-270", "updated": "2026-09-29"}` |
| 2 | PASS | `{"contract_sha": "d1ccc1e745c0881a64f8cf7e2ab481fb69215adc", "issue": 180}` |
| 3 | PASS | `{"decisions": {"bytes": 72514, "content_type": "text/html; charset=utf-8", "etag": null, "final_url": "https://www.ams.usda.gov/services/enforcement/organic/ams-decisions", "last_modified": null, "requested_url": "https://www.ams.usda.gov/services/enforcement/organic/ams-decisions", "sha256": "b880d7ad32ce47fe093ea80621ac1533bec2d794ab50d92f656d5341abcb05dd", "status": 200}, "dictionary": {"bytes": 158644, "content_type": "application/pdf", "etag": "\"26bb4-64cab3696c364\"", "final_url": "https://www.ams.usda.gov/sites/default/files/media/INTEGRITY%20Data%20Dictionary.pdf", "last_modified": "Tue, 10 Mar 2026 13:08:19 GMT", "requested_url": "https://www.ams.usda.gov/sites/default/files/media/INTEGRITY%20Data%20Dictionary.pdf", "sha256": "2700d0ae43522ed4dea941b41d4e06592c32ca04d2cb12e1cf81a3fc2d170352", "status": 200}, "enforcement": {"bytes": 52691, "content_type": "text/html; charset=utf-8", "etag": null, "final_url": "https://www.ams.usda.gov/services/enforcement/organic", "last_m...` |
| 4 | FAIL | `{"browser": {"downloaded": false, "initial_text": " United States Department of Agriculture\nAgricultural Marketing Service\nLog In\nRegister\nHome\nSearch\nReports\nTrade Partners\nContact Us   About  \nWelcome to the Organic INTEGRITY Database!\nFind a specific certified organic farm or business, or search for an operation with specific characteristics. Listings come from USDA and Trade Partner-Accredited Certifying Agents. Only certified operations can sell, label or represent products as organic, unless exempt or excluded from certification.\n\nReset Search Filters\n \nExport to Excel\nProgram\tOperation\tCertifier\tInfo\tStatus\tCity\tState/Province\tCountry\tCertified Products\n\n\t\n\t\n\t\n\t\n Certified\n\t\n\t\n\t\n\t\nUSDA-NOP\t\n\"ARATANIA\" LLC\n\t[STC] Sertifikacijas un testesanas centrs\t\tCertified\t\t\tUkraine\tHANDLING: Other Grains, Pastas and Cereals: Organic wheat, Organic corn (maize), Organic barley, Organic oats, Organic rye, Organic sunflower seed, Organic r...` |

## Implementation error

`{'type': 'RuntimeError', 'message': 'PUBLIC_EXPORT_NOT_RESOLVED_BY_OFFICIAL_UI'}`

No future adverse-status source was intentionally queried. Current baseline rows were evaluated only under the frozen cutoff/firewall rule.
