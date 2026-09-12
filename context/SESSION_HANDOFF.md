---
checkpoint_id: CHK-20260913-US-RCRA-E01-ACTIVE
active_issue: 125
active_research: US-RCRA-E01
last_completed_issue: 124
last_completed_research: PORTFOLIO-R25
last_decision: DEC-173
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R25 selected US-RCRA-E01 at 42/45 and authorized Issue #125 under DEC-173. N01 fixed 297 same-facility CEI pairs across 43 state/territory FIPS; selected-pair `FOUND_VIOLATION` remains unopened at authorization.

Exact restart: two-pass E01. Pass 1 reconstructs the frozen N01 pair identities and must reproduce exactly 297 pairs / 43 state-territory FIPS, then persists a pair fingerprint. Pass 2 may read only those selected rows' `FOUND_VIOLATION`: Y=1, N=0, U/blank/other missing; require >=100 analyzable and >=20 discordant pairs; exact two-sided McNemar; RD materiality +5pp. Diagnostics cannot rescue. Cost: **0 USD**.
