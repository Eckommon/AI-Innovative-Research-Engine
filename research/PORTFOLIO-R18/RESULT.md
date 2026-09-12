---
id: PORTFOLIO-R18-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 107
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-002
selected_gate: CA-GRAIN-E01-STAGE-A
next_issue: 108
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R18 Result — Post-CA-GRAIN-F01 PASS Effect-Stage Reselection
# PORTFOLIO-R18 결과 — CA-GRAIN-F01 PASS 이후 효과단계 재선정

## Final selection / 최종 선정

**`SELECT_C_CA_002_CA_GRAIN_E01_STAGE_A_DESIGN_IDENTIFIABILITY`**

Advance only to Issue #108 `CA-GRAIN-E01 Stage A`. Do **not** open grain-volume or dwell-time magnitudes.

## Current external-overlap refresh / 최신 중복 위험

Current official and monitoring products materially reduce novelty for any naive grain-volume → dwell analysis:

- Statistics Canada/Transport Canada publish weekly grain-transport and rail-system performance indicators, including grain service and dwell-related measures.
- Statistics Canada's Grain Supply Chain Dashboard already brings grain movement and 48-hour dwell information into one operational monitoring surface using multiple data sources.
- The federal Grain Monitoring Program (Quorum) publishes current weekly/monthly operational measures and long-run open-data/reporting assets; its research program also studies rail performance effects.
- The 2025 Transportation in Canada annual report explicitly discusses record grain shipments as rail-demand pressure alongside origin-dwell performance.

Therefore C-CA-002 does **not** receive novelty credit merely for combining grain and dwell data. Its remaining bounded information value is narrower: whether a prospectively fixed **upstream producer-delivery pressure**, one-week lag, and first-difference carrier-panel design can be identified and later tested without post-value choices.

US freight-rail × weather is further penalized because a 2026 Journal of Public Economics study already estimates weather effects on U.S. railway safety/performance and delay propagation at scale. US-UTIL remains technically strong but also has mature AMI/reliability overlap, including prior causal work linking AMI rollouts to SAIDI/SAIFI.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not an empirical finding.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-CA-002 CA-GRAIN-E01 Stage A** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 2 | **41** | **SELECT** |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| EU-GRID separate source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SOURCE_ROUTE_FRICTION |
| US freight-rail × weather | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2026_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |

## Why Stage A, not Stage B / 왜 효과값이 아닌 Stage A인가

F01 established 104 Transport Canada weekly keys, 2 carriers and 81 common explicit-date GSW week keys. It did not establish which GSW textual metric is the scientifically preferred **upstream pressure** exposure. Opening values before fixing that identity would create a material researcher-degree-of-freedom problem.

Issue #108 therefore freezes causal ordering and the Stage B skeleton prospectively, then permits only textual/schema/nonblank support inspection. The preferred exposure family is current-week producer/primary-elevator deliveries, lagged one week into Canada-level `All Western grain` origin dwell for exactly `CN` and `CPKC`. If exact source identities are ambiguous, Stage A fails closed rather than selecting by numeric fit.

## Exact next gate / 정확한 다음 gate

Execute Issue #108 Stage A only. Inspect GSW worksheet/metric/period/grain/region identities and Transport Canada frozen outcome identity/support without reading magnitudes. Classify PASS or HOLD. Stage A PASS still requires a separate adjudication before any Stage B values are opened.

Incremental monetary cost remains **0 USD**.
