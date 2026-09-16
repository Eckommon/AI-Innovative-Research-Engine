---
id: PORTFOLIO-R31-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: 142
state: COMPLETED_SELECT
selected_candidate: US-NHTSA-MC-001
selected_gate: US-NHTSA-MC-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R31 Result — Select US-NHTSA-MC-001 F01

**`SELECT_US_NHTSA_MC_001_COMMUNICATION_TO_RECALL_F01`**

R31 returns to Stage 0 after terminal FDA access-limited PARTIAL and does not retry the blocked source or automatically promote US-PIPE. The candidate/rubric contract and Issue #142 were both fixed before score persistence. No candidate outcome magnitude or relationship was opened.

## Frozen scorecard / 최종 고정점수

| Candidate | Mission | Cross-source | Direct outcome | Independent-unit | Practical | Zero-cost | Join defensibility | Info gain | Low overlap | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-NHTSA-MC-001** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 2 | **39** | **SELECT_STAGE0_F01_ONLY** |
| KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

NHTSA leads outright, so no tie-break is required.

## Selection basis / 선정 근거

NHTSA publishes current zero-cost Manufacturer Communications/TSB flat files and Safety Recall flat files. The communication dictionary exposes source-native communication ID/date plus Make, Model and Model Year, while recall data support the same product dimensions plus campaign identity. One outcome-blind F01 can therefore test exact normalization, multiplicity, time ordering, cardinality and aggregate source overlap before any recall incidence is opened.

This is not a novelty claim that service bulletins are safety signals. NHTSA itself uses manufacturer communications in Early Warning Reporting and defect analysis. Any descendant must remain a bounded non-causal public-data design and must explicitly handle repeated communications, shared product/platform structure and source-driven model-name normalization.

## Preserved alternatives / 보존 후보

- `KR-GG-CHEM-001` remains useful as a Korea Wave-1 source candidate, but exact accident-to-facility identity is not yet established and prior Korean research already links facility risk factors to accident history.
- `US-PIPE-001` remains unexecuted, but the national line-geometry restriction and direct overlap continue to reduce marginal information value.
- `US-FDA-MD-001` remains parked as an access-blocked asset and is not discarded; it may be reconsidered only after new official inspection-byte access evidence.

## Authorization boundary / 승인 경계

R31 authorizes only a separate `US-NHTSA-MC-F01` outcome-blind source/schema/product-identity/time feasibility gate. F01 may verify source bytes, dictionaries, deterministic product identity, multiplicity, date support and aggregate identity overlap only. It must not compute recall incidence by communication profile, bulletin type, component, manufacturer, model, or any proposed exposure group.

Incremental monetary cost remains **0 USD**.
