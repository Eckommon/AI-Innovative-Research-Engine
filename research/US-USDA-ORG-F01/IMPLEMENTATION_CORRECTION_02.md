---
id: US-USDA-ORG-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-30
issue: 180
attempt_01_commit: 3b352945fb8494cf89a0e937ae32ee5ffae48044
attempt_01_run: 36592128366
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_USDA_ORG_F01_ATTEMPT_01
scientific_threshold_changed: false
population_changed: false
identity_rule_changed: false
status_hierarchy_changed: false
historical_cutoff_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-USDA-ORG-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved. It established that all frozen USDA documentation/enforcement surfaces were reachable and that the official Organic INTEGRITY application rendered a public operation table with **Export to Excel**, USDA-NOP rows and **50,654** displayed Certified results. It did not complete a valid empirical 18-gate execution because the browser automation did not resolve the export body.

## Demonstrated implementation defect / 확인된 구현 결함

Attempt 01 searched only role-based button/link locators for `export|excel|download`. Organic INTEGRITY visibly rendered the literal text `Export to Excel`, but the control did not expose a matching accessible role to the runner. The app also loaded Telerik ReportViewer resources, indicating that the export path can involve an intermediate report-viewer control rather than an immediate browser download.

This is a transport/UI-automation defect, not evidence that the official export is absent.

## Attempt 02 correction / 보정

Attempt 02 may only:

1. click the literal `Reset Search Filters` control before export so the export is not restricted to the initial Certified-only display when the official UI permits reset;
2. locate the exact visible `Export to Excel` text regardless of accessible role and record the matched element/ancestor markup;
3. accept a browser download produced by that exact control;
4. if the control opens a Telerik report viewer, use only its official Export/Excel/XLSX controls;
5. capture an export response body from the same authenticated/anonymous browser session when the response is an Excel/CSV attachment but Playwright does not emit a download event;
6. record all discovered official response URLs and UI steps.

## Frozen scientific boundaries retained / 유지되는 과학 경계

Attempt 02 retains exactly:
- pre-Issue contract `d1ccc1e745c0881a64f8cf7e2ab481fb69215adc`;
- Issue #180;
- focal USDA-NOP operation population;
- exact 10-digit Operation ID rule with no padding/repair/substitution;
- all 18 gate thresholds;
- Suspended/Revoked adverse hierarchy and separate Surrendered status;
- historical cutoff 2026-09-29;
- future adverse membership seal from 2026-09-30;
- anti-tautology firewall;
- no relationship/prediction/ranking/causal computation;
- incremental monetary cost = 0 USD.

If Attempt 02 obtains the official export and any frozen scientific gate fails, the result is a valid terminal scientific HOLD unless a later defect is independently demonstrable as implementation-only without changing any frozen criterion.
