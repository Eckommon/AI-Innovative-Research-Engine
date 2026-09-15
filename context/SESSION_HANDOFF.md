---
checkpoint_id: CHK-20260916-US-MINE-N01-ACTIVE
active_issue: 135
active_research: US-MINE-N01
last_completed_issue: 134
last_completed_research: US-MINE-F01
last_decision: DEC-185
updated: 2026-09-16
---

# Session Handoff / 세션 인수인계

Issue #135 / US-MINE-N01 is active and outcome-blind under DEC-185. The exposure family, support window, quantile thresholds, exact matching fields and minimum support gates are frozen in `research/US-MINE-N01/README.md`.

N01 may parse operator `HOURS_WORKED` magnitudes only for the preregistered exposure design. It may not read the Accidents source, injury outcomes or production magnitude.

Exact restart: Execute US-MINE-N01 exactly as preregistered using Mines + MinesProdQuarterly only. Verify exact F01 source hashes first, then compute exposure-only three-quarter support, deterministic matching and pair fingerprint. Do not read the Accidents source or any injury field/value; no fallback/rescue.

Cost: **0 USD**.
