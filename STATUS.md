---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-F01-ACTIVE
active_issue: 147
active_research: US-FTA-TRANSIT-F01
last_completed_issue: 146
last_completed_research: PORTFOLIO-R33
last_decision: DEC-206
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_FTA_TRANSIT_F01_ACTIVE__OUTCOME_BLIND_SOURCE_SCHEMA_AGENCY_MODE_TIME`

US-FTA-TRANSIT-F01 is active under Issue #147 / DEC-206. The three official source IDs, source-native NTD agency × mode identity, Breakdowns TOS grain, time rules, cardinality/coverage thresholds and all 19 PASS requirements were frozen before Issue binding. No Breakdown-conditioned Major Safety Event occurrence has been opened.

## Exact next action / 정확한 다음 행동

Build and execute the official-source-only F01 runner. Verify Socrata metadata and actual bytes for `amkt-4ehs`, `5ti2-5uiv`, and `9ivb-8ae9`; resolve only source-native structural fields; compute preregistered source/key/time/cardinality/coverage diagnostics and deterministic fingerprints; persist no row-level Breakdowns→event membership and no outcome relationship.

Incremental monetary cost remains **0 USD**.
