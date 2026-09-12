---
id: DISCOVERY-R01-RESULT
type: fresh-opportunity-discovery
created: 2026-09-12
issue: 113
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: US-WW-001
selected_gate: US-WW-F01
next_issue: 114
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# DISCOVERY-R01 Result — Fresh Cross-Source Bottleneck Scan
# DISCOVERY-R01 결과 — 신규 cross-source bottleneck 탐색

## Final selection / 최종 선정

**`SELECT_US_WW_001_CWNS_INFRASTRUCTURE_NEED_TO_NPDES_COMPLIANCE`**

Advance only to Issue #114 `US-WW-F01`, an outcome-blind CWNS-2022 × ICIS-NPDES source/identity/join gate. No infrastructure-cost magnitude, violation count, effluent value, compliance rate or relationship is authorized.

## Selected candidate / 선정 후보

### US-WW-001 — Wastewater Infrastructure Need Profile × Subsequent Compliance Persistence

Baseline source: EPA **2022 Clean Watersheds Needs Survey (CWNS)** facility/project and need-category identities.

Future outcome source family: EPA **ICIS-NPDES / ECHO** permit/compliance identities.

Why this is structurally attractive before values:
- EPA publishes the nationwide 2022 CWNS dataset as CSV/Access files and a data dictionary;
- CWNS covers wastewater facilities and infrastructure needs over the next 20 years;
- EPA ECHO exposes CWNS IDs for wastewater facilities and uses NPDES IDs as deterministic program-system identifiers;
- EPA documentation states 2022 CWNS wastewater technical records were prepopulated from ICIS-NPDES, including NPDES permit number and facility geography;
- wet-weather/conveyance-relevant need-category semantics include infiltration/inflow correction, sewer rehabilitation/replacement and combined-sewer-overflow correction;
- the baseline survey precedes a future post-2022 compliance window, supporting prospective temporal ordering in a later separately preregistered non-causal study.

Current literature search found adjacent wastewater-compliance studies using rainfall, electronic reporting and ICIS-NPDES/CWNS treatment characteristics, but no near-identical facility-level design directly testing whether 2022 CWNS capital-need category identities prospectively stratify later NPDES compliance persistence. This is an overlap screen, not a proof of novelty.

## Fresh candidate comparison / 신규 후보 비교

0–5 each; /45. Scores are discovery/portfolio judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WW-001 CWNS need profile → later NPDES compliance** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | **43** | **SELECT** |
| US-WW-002 precipitation → NPDES compliance | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **39** | HOLD_CURRENT_OVERLAP |
| US-RCRA-001 natural-hazard exposure → hazardous-waste compliance | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 2 | **39** | HOLD_POLICY_OVERLAP |
| US-MINE-001 production pressure / operational stress → mine injuries | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_PRIOR_CONCEPTUAL_OVERLAP |
| US-PIPE-001 hydrologic stress → pipeline incidents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_CAUSE_OVERLAP |
| US-FRA-001 heat → rail accident/track failure | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2025_2026_OVERLAP |
| US-FAA-WL-001 weather regime → wildlife strikes | 3 | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 0 | **33** | HOLD_EXISTING_RESEARCH_OPERATIONAL_OVERLAP |
| US-DW-001 climate hazards → drinking-water compliance | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 1 | 0 | **36** | HOLD_NEAR_EXACT_2026_OVERLAP |

## Why the selected candidate is distinct enough for F01 / F01 가치

The discovery value is **not** the general proposition that weather can affect wastewater performance. That pathway already has substantial prior evidence. The bounded new question is whether a nationally reported **pre-existing infrastructure-need structure** can serve as a reproducible public-data signal for later compliance vulnerability/prioritization. A later experiment, if ever authorized, must explicitly handle the risk that CWNS needs may themselves reflect pre-existing compliance problems and therefore must not be interpreted causally without a much stronger design.

## Official source basis / 공식 source 근거

- EPA 2022 CWNS nationwide data download: https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download
- EPA 2022 CWNS report/data: https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data
- EPA CWNS needs categories: https://www.epa.gov/cwns/about-clean-watersheds-needs-survey-cwns
- ECHO custom-search help (CWNS ID / facility linkage): https://echo.epa.gov/help/loading-tool/custom-search/custom-search-help
- ECHO wastewater/NPDES search help: https://echo.epa.gov/help/facility-search/search-criteria-help

## Exact next action / 정확한 다음 행동

Execute Issue #114 outcome-blind. Establish the national CWNS data route, deterministic CWNS ID → NPDES ID linkage, ECHO/ICIS permit identity coverage, need-category identity route, and post-2022 compliance-record schema support. Persist no dollar needs, effluent/limit values, violation rates/counts by exposure group or relationship statistics.

Incremental monetary cost remains **0 USD**.
