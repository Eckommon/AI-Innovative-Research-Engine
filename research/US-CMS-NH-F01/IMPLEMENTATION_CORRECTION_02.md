---
id: US-CMS-NH-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-10-06
issue: 194
attempt_01_run: 37338329443
scientific_threshold_changed: false
archive_window_changed: false
identity_rule_changed: false
event_rule_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NH-F01 — Attempt 02 implementation-only correction

Attempt 01 remains immutable but is **not scientifically adjudicative**.

## Demonstrated defect

Attempt 01 recorded:
- CMS archive endpoint HTTP 200;
- official CMS dictionary HTTP 200;
- `archive_ui.text == ""`;
- `archive_ui.links == []`;
- `archive_ui.dates == []`.

The official CMS archive surface is known to expose nursing-home archive releases, so an entirely empty rendered DOM does not demonstrate that all frozen months are absent. It demonstrates that the headless renderer failed to expose the SPA's loaded archive content.

Therefore Gate 4 from Attempt 01 cannot be treated as a valid scientific failure.

## Allowed correction

Attempt 02 may only change archive-discovery mechanics:

1. preserve the exact same CMS archive URL;
2. capture source-native network responses made by the official CMS page;
3. inspect official CMS JSON/text response bodies and browser performance resource URLs for archive metadata;
4. wait longer for SPA hydration and also inspect final DOM;
5. derive archive release dates only from CMS-owned responses/page state.

No third-party mirror, search cache, manually supplied archive date, changed baseline month, or relaxed lineage criterion may be used.

## Frozen boundaries retained

Unchanged:
- contract `fed9f05c7271c712881fc9b7936ca1a5f7912347`;
- frozen months September 2025 through August 2026;
- exact 6-digit CCN;
- all 18 gate thresholds;
- standard-health-survey opportunity;
- G–L serious event rule;
- anti-tautology firewall;
- September-2026-or-later row-body seal;
- cost = 0 USD.

If Attempt 02 source-native archive discovery proves any required frozen month lacks an official row-bearing archive/snapshot release, that is a valid terminal scientific HOLD. If archive discovery itself remains unresolved, the result stays implementation-blocked and does not become scientific HOLD.
