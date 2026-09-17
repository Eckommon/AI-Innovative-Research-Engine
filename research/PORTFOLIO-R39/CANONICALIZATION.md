---
id: PORTFOLIO-R39-CANONICALIZATION
type: implementation-only-state-correction
created: 2026-09-18
issue: 162
scientific_selection_changed: false
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R39 terminal canonicalization correction

`PORTFOLIO-R39` scientific selection is already immutable and is **not** being rerun, rescored, or reinterpreted.

Frozen evidence chain:

- pre-Issue contract: `9d6a16975bc02638aae938f20b6591ffe02d1fa9`
- bounded revalidation: `a835ed4eb46cb6634f7c55408029651819a74748`
- immutable scorecard: `776cf5702778cfd4e994a0c668b38f1dd6cd2019`
- terminal result: `1fc531a3537e70863989002b99f858380b63f229`
- Issue #162: completed

The result selected `US-IRS-EO-001` at 41/45 and held the other three candidates. No future automatic-revocation membership or other candidate future outcome was opened.

## Why this correction exists

Issue #162 and the terminal R39 research files were completed before the canonical state mirrors (`registry/DEC-*.md`, `registry/DECISION_LOG.md`, `context/checkpoint.json`, `STATUS.md`, `context/SESSION_HANDOFF.md`) were advanced from the prior `US-FDIC-BRANCH-N01` terminal checkpoint. That is a state-plumbing omission, not a scientific failure and not authorization to alter R39.

## Allowed correction

A single terminal canonicalization decision may:

1. verify the four frozen evidence commits and completed Issue #162;
2. require the live pre-correction checkpoint to remain `CHK-20260918-US-FDIC-BRANCH-N01-TERMINAL` with `last_decision: DEC-235`;
3. append exactly one new terminal decision, `DEC-236`;
4. advance the canonical checkpoint to `CHK-20260918-PORTFOLIO-R39-TERMINAL`;
5. set `last_completed_issue: 162`, `last_completed_research: PORTFOLIO-R39`, and no active issue/research;
6. set the exact next action to freezing `US-IRS-EO-F01` **before** creating its Issue.

It may not add a retroactive activation decision, change any R39 score, reopen or replace Issue #162, access future outcome membership, or authorize an empirical N01/E01.

## Terminal selection boundary

The only authorized descendant is a separate, outcome-blind `US-IRS-EO-F01` structural contract. Prior nonfiling/missed-filing streaks remain prohibited as exposure because automatic revocation is mechanically triggered by three consecutive missed required annual filings.

Cost remains **0 USD**.
