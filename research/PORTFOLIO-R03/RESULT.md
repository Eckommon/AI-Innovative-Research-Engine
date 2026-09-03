---
id: PORTFOLIO-R03-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-04
issue: 73
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-003R
selected_gate: US-MINERAL-F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R03 Result — Post-U.S.-Port Mission-ROI Reselection
# PORTFOLIO-R03 결과 — 미국 항만 HOLD 이후 목적-ROI 재선정

## Final selection / 최종 선정

**`SELECT_C_US_003R_CRITICAL_MINERAL_ENTRY_NODE_CONCENTRATION`**

Promote the existing `C-US-003 Critical Mineral Resilience` family with a sharper, source-grounded framing:

**`C-US-003R — Critical Mineral Import-Source × U.S. Entry-Node Concentration Intelligence`**  
**`C-US-003R — 핵심광물 공급국 × 미국 진입노드 집중도 지능화`**

Exact next bounded gate:

**`US-MINERAL-F01 — USGS Critical-Mineral Trade-Code × Census Import-Node Join Feasibility`**.

## Why the framing was refined / 왜 framing을 보정했는가

The original Wave 1 `C-US-003` proposed `USGS MCS + trade + prices + recycling capacity + technology demand proxies` with targets including import-reliance stress, supply concentration and recycling leverage.

PORTFOLIO-R03 preserves that family but selects a lower-DOF first relationship that has a clearer public-data bridge and a more operational bottleneck meaning:

`USGS critical-mineral identity / import-reliance context`
`+ official USGS mineral→HTS trade-code mapping`
`+ Census monthly imports by HTS, country, customs district and transport mode`
`→ source-country concentration × U.S. entry-node concentration`

This can reveal whether a mineral is exposed not only to foreign-source concentration but also to a small number of U.S. import gateways. The latter is a distinct logistics/infrastructure chokepoint dimension that is not represented by net-import-reliance alone.

## Current official-source refresh / 현행 공식 소스 갱신

### USGS / 미국 지질조사국

Current official evidence confirms:

- `Mineral Commodity Summaries 2026`, first posted 2026-02-06 and revised to version 1.3 in May 2026, covers more than 90 minerals/materials.
- MCS chapters include domestic industry structure, government programs, **tariffs**, five-year salient statistics, world production/reserves/resources, import sources and net-import-reliance context.
- The 2026 USGS Science Data Catalog release is public and contains data extracted from the commodity chapters for 2021–2025.
- USGS's methodology/technical input for the 2025 U.S. List of Critical Minerals publishes explicit mineral→trade-code mappings, including HTS/HS code rows and, where necessary, allocation weights/notes.

Official sources used for Stage 0 refresh:
- https://pubs.usgs.gov/publication/mcs2026
- https://data.usgs.gov/datacatalog/data/USGS%3A69837e43b66b01367d7ec7c7
- https://pubs.usgs.gov/publication/ofr20251047/full

### U.S. Census international trade / 미국 Census 국제무역

Current official evidence confirms:

- Census states that international-trade data products previously available by subscription are now public at no cost.
- 2026 merchandise-import products include HTSUSA commodity code, country of origin, customs district of entry/unlading, quantity, shipping weight, method of transportation and value fields.
- Census publishes 2010-present concordance files.
- The Census International Trade API is current but now requires an API key; therefore the next gate shall prefer the public no-cost file/bulk route and shall not require API-key provisioning merely for convenience.

Official sources used for Stage 0 refresh:
- https://www.census.gov/foreign-trade/data/dataproducts.html
- https://api.census.gov/data/timeseries/intltrade/imports/hs.html

## Candidate comparison / 후보 비교

Stage 0 uses a transparent 0–5 qualitative score. These are **portfolio decision scores, not empirical findings**. Equal weighting is used only to expose the selection logic; no scientific effect is inferred from the score.

| Candidate | Direct bottleneck | Cross-source value | Falsifiability / reproducibility | Practical intervention value | Current source access | Low rescue/mapping friction | Next-gate information gain | Total /35 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **`C-US-003R Critical Mineral Entry-Node Concentration`** | 5 | 5 | 5 | 5 | 5 | 4 | 5 | **34** | **SELECT** |
| `C-US-001 U.S. Grid Bottleneck Intelligence` | 5 | 5 | 5 | 5 | 4 | 3 | 5 | **32** | `HOLD_READY_SECONDARY` |
| `C-EU-001 Cross-National Grid Stress` | 5 | 5 | 5 | 5 | 3 | 2 | 4 | **29** | `HOLD_READY_SECONDARY` |
| `C-EU-004 Industrial Site Climate Risk` | 4 | 5 | 3 | 4 | 5 | 5 | 2 | **28** | `PRESERVE_JOIN_ASSET` |
| `C-JP-001 Port Weather–Throughput Stress` | 3 | 4 | 3 | 4 | 5 | 4 | 3 | **26** | `HOLD_READY` |
| `C-SG-001 Maritime Activity × Weather Regime` | 3 | 4 | 3 | 4 | 5 | 5 | 2 | **26** | `HOLD_READY` |

## Candidate-specific rationale / 후보별 근거

### 1. `C-US-003R` — SELECT

Strengths:
- strategic supply-chain bottleneck with direct relevance to electronics, energy, manufacturing and infrastructure;
- official bridge from mineral identity to trade codes is already published by USGS, reducing arbitrary semantic mapping;
- Census trade files add country-of-origin and U.S. customs-district/transport-mode structure unavailable in MCS alone;
- a future experiment can be explicitly falsifiable across many mapped minerals rather than relying on one anecdotal commodity;
- public file routes allow 0 USD execution without paid data or dashboard scraping;
- entry-node concentration is a distinct intervention surface: diversification of gateways, stockpiling/logistics planning, alternate transport modes, domestic processing/recycling prioritization.

Risk:
- one mineral can map to multiple trade codes and some codes can mix products/material states; the USGS methodology's weights/notes and Census quantity-unit semantics must therefore be qualified before any concentration calculation.

### 2. `C-US-001` — strong secondary

EIA-930 still provides hourly balancing-authority demand, forecast, generation and interchange; LBNL Queued Up 2026 provides project-level queue data and a codebook through end-2025 for all seven ISOs/RTOs plus 50 non-ISO utilities (~98% of installed U.S. capacity represented by covered operators).

However:
- the EIA API requires an API key, although EIA bulk downloads remain keyless;
- LBNL queue regions/operators do not automatically equal EIA balancing-authority geography;
- the next defensible relationship still needs an explicit geography/operator bridge and a carefully chosen interconnection-delay/stress outcome.

This remains a high-value next fallback, not a rejected branch.

### 3. `C-EU-001` — high scientific value, higher access/mapping burden

ENTSO-E + ERA5 + Eurostat remains attractive and harmonized, but the repo already records the bidding-zone/control-area ≠ NUTS mapping risk and account/token handling for some automated ENTSO-E access. It therefore loses to a candidate with a cleaner official identity bridge at the next gate.

### 4. `C-EU-004` — preserve existing PASS asset

`EU-ISR-F01` already passed deterministic facility-coordinate × meteorological-point join feasibility. The durable result correctly warns that immediate climate→emissions/energy regression would have weak construct validity because annual facility outcomes are strongly confounded by capacity, fuel, dispatch, regulation and technology. The join asset is retained; it is not forced into an under-specified experiment.

### 5–6. Japan / Singapore maritime-weather

Both remain genuinely accessible official-public-data candidates. Japan currently publishes port survey monthly results including vessel arrivals, cargo and container counts. Singapore MPA public datasets provide monthly vessel arrivals/tonnage and type breakdown through 2026 with keyless sample OpenAPI access.

Their common weakness for the present mission is outcome grain: monthly aggregates are much coarser than the weather layer and weaker for identifying short-lived disruption/recovery bottlenecks.

## Exact next gate / 정확한 다음 게이트

Open only:

### `US-MINERAL-F01 — USGS Critical-Mineral Trade-Code × Census Import-Node Join Feasibility`

F01 shall remain source-semantic and outcome-blind with respect to concentration results. It may verify:

1. exact authoritative critical-mineral universe/version;
2. exact USGS mineral→HTS/HS mapping fields, weights and caveats;
3. exact Census import-file fields for HTS code, origin country, customs district, transport mode, value/quantity and time;
4. whether code granularity/version/year can be reconciled without unsupported many-to-many interpretation;
5. bounded overlap, duplicate/revision/suppression rules and unit semantics;
6. a deterministic join key and frozen snapshot/hash plan;
7. whether a later all/minimum-support-minerals concentration experiment can be preregistered without choosing commodities after seeing concentration outcomes.

F01 shall **not** calculate country concentration, entry-node concentration, HHI, chokepoint rankings, correlations or policy winners/losers.

## Branch-stop rule / 중단 규칙

HOLD/REJECT and return to Stage 0 if:
- official USGS trade-code mapping cannot be reconciled to the public Census import product at a defined vintage;
- a substantial fraction of the critical-mineral universe requires arbitrary manual code assignment;
- Census no-cost public files cannot provide the required country/district/mode structure without paid or credential-heavy access;
- mixed-product codes make the intended mineral-level unit non-identifiable without unsupported allocation.

Do not scrape visualization tools or substitute private commercial trade data to rescue the branch.

## Cost / 비용

Incremental monetary cost remained **0 USD**. Any potentially billable work requires explicit prior user approval.
