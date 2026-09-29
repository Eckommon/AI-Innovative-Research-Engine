---
id: US-MSHA-MINE-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-29
issue: 177
attempt_01_commit: 41ba21671503757516a7528477b1deb9fbea9ec8
attempt_01_disposition: HOLD_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_NOT_READY
scientific_threshold_changed: false
population_changed: false
identity_rule_changed: false
event_rule_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-MSHA-MINE-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved. It passed 17/18 gates and failed only Gate 3 because the runner implemented the contract phrase **"reachable or officially redirected"** as an exact HTTP-200 predicate for every documentation anchor.

The MSHA Mine Data Retrieval System anchor returned **HTTP 202** to the GitHub-hosted curl client while:
- the Open Government portal returned 200;
- all three frozen definition files returned 200;
- all three official entity ZIPs returned 200 and were fully parsed;
- the official MSHA web surface independently resolves/redirects the MDRS route to the current Data & Reports / Mine Data Retrieval System page.

This is an implementation predicate mismatch, not a scientific support failure.

## Authorized correction / 허가된 보정

Attempt 02 may only change Gate 3's reachability predicate from:
- exact `status == 200`

to:
- any HTTP **2xx** response for the frozen official documentation anchors.

No URL, source body, population, Mine-ID rule, operating-status set, Q1/Q2 baseline, support threshold, serious/fatal code, event date rule, future firewall or cost rule may change.

Attempt 02 must write separate immutable `attempt-02.json/.md` evidence.

If any empirical gate other than this corrected reachability predicate fails, the result is scientific evidence under the unchanged contract.
