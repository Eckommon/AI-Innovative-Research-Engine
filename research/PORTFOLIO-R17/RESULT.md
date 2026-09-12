---
id: PORTFOLIO-R17-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 105
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-002
selected_gate: CA-GRAIN-F01
next_issue: 106
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R17 Result — Post-EU-GRID-F01 HOLD Reselection
# PORTFOLIO-R17 결과 — EU-GRID-F01 HOLD 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_CA_002_GRAIN_PRESSURE_RAIL_DWELL_SOURCE_JOIN_FEASIBILITY`**

Selected next gate: **Issue #106 `CA-GRAIN-F01` — outcome-blind weekly grain-pressure × rail-dwell source/join feasibility.**

No grain-volume, dwell-time, utility-reliability, weather or relationship magnitude was opened during R17.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not an empirical finding.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-CA-002 Grain Pressure × Rail Dwell redesign** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 3 | **40** | **SELECT** |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| US-FREIGHT-RAIL Weather × Terminal Dwell | 4 | 5 | 5 | 4 | 5 | 5 | 3 | 4 | 1 | **36** | HOLD_HIGH_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |
| EU-GRID source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SEPARATE_REDESIGN_ONLY |

## Current source / overlap refresh / 최신 source·중복 확인

- Transport Canada / Statistics Canada continue to expose weekly rail performance data with full-table CSV/SDMX downloads and commodity/terminal/origin-dwell identities. The post-2023 Transportation Data and Information Hub exposes a full-data download and expanded geography/commodity dimensions.
- Canadian Grain Commission Grain Statistics Weekly exposes open current and archived crop-year CSVs; the frozen 2023-24 and 2024-25 crop years are available.
- External-overlap risk is real: Canada's Grain Monitoring Program already monitors the prairie grain handling and transportation system. Therefore R17 does not claim novelty or open an effect test; the next question is narrower — whether an independent, deterministic weekly cross-source panel exists under a preregistered source/join contract.
- The fresh U.S. freight-rail weather alternative is technically attractive, but 2026 literature already studies weather effects on U.S. railway performance and delay propagation, sharply reducing marginal novelty.
- EU-GRID-F01 remains terminal under its frozen no-login public-page route; no post hoc repair is allowed inside F01.

## Exact next gate / 정확한 다음 gate

Execute **CA-GRAIN-F01 only**. Verify source download, schema/category identity, frozen crop-year support, weekly calendar semantics, carrier identity and prospective weekly join cardinality. Reduce any numeric field encountered for support checking immediately to booleans/counts; persist no grain-volume or dwell-time magnitudes and compute no relationship.

Incremental monetary cost remains **0 USD**.
