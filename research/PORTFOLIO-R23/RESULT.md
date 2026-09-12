---
id: PORTFOLIO-R23-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 120
state: COMPLETED_SELECT
selected_candidate: US-RCRA-F01
selected_gate: US-RCRA-F01
next_issue: 121
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R23 Result — Select US-RCRA-F01

**`SELECT_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_FEASIBILITY`**

After terminal US-WW-E01, do not rescue that branch. Select the independent US-RCRA branch for one outcome-blind source/join/time feasibility gate. No disaster-linked compliance outcome was opened during selection.

## Mission-ROI comparison

0–5 each; /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-RCRA-F01 hazard × compliance feasibility** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 3 | **40** | **SELECT** |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why US-RCRA leads now

Current EPA data expose a prospectively deterministic identity chain before values:

`RCRAInfo.ID_NUMBER` → ECHO RCRA facility `SOURCE_ID` → `RCR_FIPS_CODE` (5-digit county FIPS) → FEMA county disaster/time identity → RCRA evaluation/violation temporal identity.

This avoids fuzzy facility names and avoids post-hoc spatial repair. RCRAInfo is a national program system with facility, evaluation, violation and monthly violation/SNC identities; FEMA OpenFEMA publishes official county-coded disaster declarations with incident dates.

The overlap penalty is material: EPA and GAO already evaluate natural-hazard vulnerability/exposure of RCRA facilities. Therefore this project does **not** claim novelty for static hazard mapping. The only potentially distinct descendant is a later, separately preregistered temporal relationship to subsequent compliance identity, and F01 does not authorize it.

## Exact next action

Execute Issue #121 outcome-blind. Verify source access, exact RCRA-ID→ECHO county-FIPS linkage, operating-TSDF cardinality/geographic support, FEMA county/time coverage, and RCRA evaluation/violation temporal identity. Do not compute disaster-linked facility violation rates/counts or any relationship.

Incremental monetary cost: **0 USD**.
