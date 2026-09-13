---
id: PORTFOLIO-R26-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 126
state: COMPLETED_SELECT
selected_candidate: US-BRIDGE-F01
selected_gate: US-BRIDGE-F01
next_issue: 127
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R26 Result — Select US-BRIDGE-F01

**`SELECT_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_FEASIBILITY`**

After terminal US-RCRA-E01, do not rescue or reverse that branch. Select the independent US-BRIDGE branch for one outcome-blind source/identity/time feasibility gate. No bridge condition-rating value or hazard-linked bridge-condition relationship was opened during selection.

## Mission-ROI comparison

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-BRIDGE-F01 temporal hazard × bridge-condition feasibility** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **41** | **SELECT** |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **39** | HOLD_HIGH_OVERLAP |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why US-BRIDGE leads now

FHWA provides a national bridge inventory with exact bridge, county, inspection and condition identities across annual Coding-Guide-format archives through 2025. The 2015–2025 window can remain entirely inside one legacy format while actual inspection dates, rather than annual archive years, define future temporal identity. FEMA OpenFEMA provides direct county FIPS and incident dates from an independent source.

Candidate identity chain:

`NBI State Code + Structure Number → exact bridge identity → County FIPS → FEMA county/time identity → NBI inspection-date / condition-field identity`.

## Overlap boundary

The overlap penalty is material. NBI deterioration modeling is established, and the 2025 BTS `BETA - Hazard Exposure: National Highway System Bridges` product already combines NBI with FEMA/USGS/NOAA/USDA static hazard layers. Therefore this branch does **not** claim novelty for static hazard mapping, bridge deterioration modeling, or NBI × hazard integration itself.

The only potentially distinct descendant is a later, separately preregistered temporal question about observed disaster timing and subsequent inspection-condition change. F01 does not authorize or establish that relationship.

## Source semantics frozen at selection

- 2025 is the final annual NBI submission year in the legacy Coding Guide format before SNBI transition.
- FHWA validates Structure Number uniqueness within state submissions.
- County Code is a FIPS county identity; the SNBI crosswalk directly transitions legacy State Code and County Code into current location identities.
- Deck, superstructure, substructure and culvert condition ratings are inspection-derived; most routine inspections occur on roughly 24-month cycles, so later temporal pairing must use actual inspection dates.

## Exact next action

Execute Issue #127 outcome-blind. Verify 2015–2025 source access, exact bridge identity continuity, deterministic county FIPS, repeated distinct inspection-date support, FEMA county/time overlap and condition-field header availability. Do not parse, summarize, rank or compare bridge condition ratings.

Incremental monetary cost: **0 USD**.
