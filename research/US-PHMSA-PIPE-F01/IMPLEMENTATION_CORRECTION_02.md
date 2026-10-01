---
id: US-PHMSA-PIPE-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-10-02
issue: 190
attempt_01_run: 36886491100
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_PHMSA_PIPE_F01_ATTEMPT_01
scientific_threshold_changed: false
facility_family_changed: false
annual_years_changed: false
identity_rule_changed: false
event_rule_changed: false
future_source_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-PHMSA-PIPE-F01 — Attempt 02 implementation-only transport correction

Attempt 01 is immutable. It failed before empirical row access because GitHub-hosted Python `requests` received HTTP 403 from every frozen PHMSA page and both official ZIP routes.

The same official pages and direct ZIP links are publicly resolvable outside that transport path. This demonstrates a runner/network transport defect, not a scientific gate failure.

## Allowed correction

Attempt 02 may only:
1. replace Python `requests` retrieval with command-line `curl`;
2. use a mainstream browser User-Agent, Accept headers, HTTPS redirect following, HTTP/1.1 and source-page Referer;
3. preserve the exact official PHMSA URLs and files frozen in the contract;
4. record effective URL, HTTP status, content type, size and SHA-256;
5. reuse the identical row parser and all 18 scientific gates after bytes are obtained.

No alternate mirror, VPN, proxy, paid source, service family, annual window, threshold, identity repair or event redefinition is authorized.

If Attempt 02 is again blocked before scientific row access, apply the mandatory branch-stop rule rather than opening a third transport descendant.
