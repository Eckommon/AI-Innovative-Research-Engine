---
id: PORTFOLIO-R25-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 124
state: COMPLETED_SELECT
selected_candidate: US-RCRA-E01
selected_gate: US-RCRA-E01
next_issue: 125
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R25 Result — Select US-RCRA-E01

**`SELECT_US_RCRA_E01_PAIRED_CEI_RELATIONSHIP_TEST`**

US-RCRA-E01 is selected outcome-blind after N01 fixed 297 same-facility CEI pairs across 43 state/territory FIPS with selected-pair `FOUND_VIOLATION` still unopened.

## Mission-ROI comparison

0–5 each; /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-RCRA-E01 paired CEI test** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | **42** | **SELECT** |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial-site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why E01 leads now

F01 removed source/join/time uncertainty and N01 removed pair-identifiability/surveillance-type uncertainty. The remaining bounded question is a single preregistered paired inspection-result comparison. Its information gain is therefore higher than opening a new source-feasibility branch now.

Overlap remains material: RCRA inspection/compliance and hazardous-site hazard vulnerability are established research areas. The only bounded contribution is the preregistered national same-facility paired-CEI FEMA-disaster monitoring/compliance test. Novelty is not proven.

## Exact authorization boundary

Issue #125 is authorized exactly as preregistered. Before outcome access, it must reconstruct N01's 297 pairs and persist a deterministic pair fingerprint. Only then may it read selected rows' `FOUND_VIOLATION` values. Primary coding is Y=1, N=0, U/blank/other=missing; >=100 analyzable pairs and >=20 discordant pairs are required. Primary inference is an exact two-sided McNemar/binomial test with a +5 percentage-point materiality floor. Diagnostics are non-rescuing.

Incremental monetary cost: **0 USD**.
