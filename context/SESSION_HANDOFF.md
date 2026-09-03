---
id: SESSION-HANDOFF
type: memory
state: ACTIVE
checkpoint_id: CHK-20260904-US-MINERAL-F01-ACTIVE
active_issue: 74
active_research: US-MINERAL-F01
last_completed_issue: 73
last_completed_research: PORTFOLIO-R03
last_decision: DEC-104
created: 2026-08-22
updated: 2026-09-04
source_of_truth: github
---

# Session Handoff / 세션 인수인계

## Mandatory first read / 의무 선읽기

Read README, STATUS, PROJECT_MEMORY, `MEM-054`, this handoff, live Issues, `DEC-093`, `DEC-103`, `DEC-104`, and relevant result/claim records before material work.

Mission priority:
`mission innovation/bottleneck value → cross-dataset/cross-agency/cross-national value → falsifiability/reproducibility → practical utility/scalability → efficient route → branch completion`.

## Last completed work — PORTFOLIO-R03

Issue #73 completed.

Final selection:
**`SELECT_C_US_003R_CRITICAL_MINERAL_ENTRY_NODE_CONCENTRATION`**.

Selected branch:
**`C-US-003R — Critical Mineral Import-Source × U.S. Entry-Node Concentration Intelligence`**.

Rationale:
- USGS provides current critical-mineral/MCS context plus explicit official mineral→trade-code methodology mappings;
- Census public merchandise-import products expose HTSUSA, country of origin, customs district of entry/unlading, transport mode, quantity/weight and value;
- this allows a prospective dual-chokepoint question: foreign-source concentration + domestic U.S. gateway concentration;
- the semantic bridge is cleaner than the current U.S./EU grid mapping alternatives;
- public file routes preserve 0 USD and avoid scraping/commercial data.

Durable records:
- `research/PORTFOLIO-R03/RESULT.md`;
- `registry/DEC-104.md`.

## Active Issue #74 — US-MINERAL-F01

Preregistered at:
`research/US-MINERAL-F01/README.md`.

Frozen universe:
- Final 2025 U.S. List of Critical Minerals;
- 60 minerals;
- no post-outcome mineral selection.

Primary mapping source:
- USGS OFR 2025-1047 methodology/technical input;
- MCS 2026 / data release may cross-check identity/context only.

Preferred Census route:
- official public file/bulk trade products;
- Census API requires a key, so do not create credential work merely for convenience.

Allowed F01 work:
- source identity/version;
- trade-code mapping fields/weights/caveats;
- Census record layout/schema;
- mapping/cardinality compatibility;
- suppression/null/duplicate/unit rules;
- bounded common vintage and snapshot/hash plan;
- prospective support-qualified universe definition.

Prohibited F01 work:
- country or entry-node concentration;
- HHI/entropy/top-share;
- rankings of minerals/countries/districts/gateways;
- correlation/regression;
- policy/investment ranking.

Stage-0 exposure already disclosed in README: examples of USGS trade-code rows and Census schema fields were visible before preregistration, but no concentration outcome was computed/viewed as an experiment result.

## Exact next action / 정확한 다음 행동

1. Confirm State Integrity PASS for `CHK-20260904-US-MINERAL-F01-ACTIVE`.
2. Qualify final-2025 critical-mineral universe and USGS mapping source/version.
3. Qualify exact Census public import file/bulk schema and vintage.
4. Define deterministic mapping/support/snapshot rules.
5. Apply frozen F01 gate without concentration calculations.

Incremental monetary cost remains **0 USD**. Any potentially billable work requires explicit prior user approval.
