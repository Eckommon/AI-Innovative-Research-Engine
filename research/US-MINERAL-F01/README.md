---
id: US-MINERAL-F01
type: source-semantic-join-feasibility
created: 2026-09-04
issue: 74
state: PREREGISTERED_ACTIVE
mission_anchor: MEM-054
portfolio_decision: DEC-104
incremental_monetary_cost_usd: 0
---

# US-MINERAL-F01 — USGS Critical-Mineral Trade-Code × Census Import-Node Join Feasibility
# US-MINERAL-F01 — USGS 핵심광물 trade code × Census 수입 진입노드 조인 실행가능성

## 1. Objective / 목적

Test only whether official U.S. public sources can construct a deterministic, reproducible semantic bridge:

`critical mineral → USGS trade code → Census import record identity → country of origin × U.S. customs entry/unlading district × transport mode × month`.

F01 is **not** a concentration experiment.

## 2. Frozen critical-mineral universe / 고정 핵심광물 universe

Use the **Final 2025 U.S. List of Critical Minerals**, published by the Department of the Interior through USGS on 2025-11-06.

Frozen universe size: **60 critical minerals**.

The universe identity is fixed before any concentration outcome is computed. A later experiment may not remove minerals because their observed concentration results are inconvenient or weak.

Authoritative universe reference:
- USGS `About the 2025 List of Critical Minerals` / final 2025 list.
- USGS reports 60 minerals: all 50 from the 2022 list plus 10 additions.

## 3. Frozen USGS semantic bridge / 고정 USGS semantic bridge

Primary bridge source:

`Methodology and technical input for the 2025 U.S. List of Critical Minerals—Assessing the potential effects of mineral commodity supply chain disruptions on the U.S. economy` (`OFR 2025-1047`).

Use only trade-code mappings, allocation weights, notes, inclusions/exclusions and commodity identities explicitly supported by the official USGS methodology/associated public data.

Supporting current context:
- `Mineral Commodity Summaries 2026` and its public 2021–2025 data release may be used to verify commodity identity/version/context.
- MCS 2026 tariff tables may be used as primary-source cross-checks, not as post-hoc replacements for inconsistent mapping.

No ad-hoc code assignment from web search or commercial concordance is allowed.

## 4. Frozen Census route / 고정 Census 경로

Prefer the official Census international-trade **public file/bulk data products** rather than the API.

Reason:
- current Census API documentation requires an API key;
- current Census data-product documentation states previously subscription-only international-trade products are now public at no cost;
- F01 must not create credential provisioning merely for convenience.

The required import identity fields to qualify are:
- HTSUSA commodity code;
- country of origin;
- customs district of entry and/or unlading;
- method of transportation;
- quantity and quantity unit where provided;
- shipping weight where provided;
- import value field(s);
- year/month.

F01 shall identify the exact public file(s), record layout/codebook, vintage and file naming/version semantics before any later data extraction.

## 5. Join qualification / 조인 검증

F01 must determine:

1. whether each frozen mineral can be linked to one or more official USGS trade codes;
2. whether the code level matches or can be deterministically transformed to the Census HTSUSA level for one fixed vintage;
3. whether USGS allocation weights/notes provide a reproducible rule where codes are shared or mixed;
4. whether any code maps to multiple minerals in a way that makes mineral-level attribution non-identifiable;
5. whether Census public-file fields retain country + entry/unlading district + mode at the same commodity/time grain;
6. how revisions, suppressed values, nulls, duplicate identities and quantity-unit heterogeneity are handled;
7. whether a future experiment can use:
   - all 60 minerals, or
   - a **prospectively support-qualified subset** defined solely by pre-outcome mapping/support rules.

A support-qualified subset is allowed only if exclusion rules are frozen before concentration values are calculated.

## 6. Exposure boundary / 노출 경계

Prohibited during F01:
- computing country concentration or entry-node concentration;
- HHI, entropy, top-country share, top-district share or composite chokepoint scores;
- ranking minerals, countries, customs districts, ports or transport modes;
- correlations/regressions;
- investment/policy winners and losers.

Allowed:
- source identity;
- schema/field names;
- code cardinality and mapping cardinality;
- number of minerals with/without deterministic mapping;
- file size/row-count only when required to plan bounded execution;
- hashes, version dates and non-outcome integrity diagnostics.

## 7. Stage-0 exposure disclosure / Stage-0 노출 고지

Before this README was frozen, PORTFOLIO-R03 source refresh exposed:
- examples showing that the USGS methodology contains explicit mineral→trade-code rows;
- an example MCS tariff table;
- Census documentation describing HTSUSA, country-of-origin, customs-district, transport-mode, quantity/weight and value fields.

No mineral-level concentration statistic, import-node concentration, HHI, mineral risk ranking or gateway ranking was computed or viewed as an experimental result.

These schema/mapping examples are treated as source-semantic exposure and cannot later be described as newly outcome-blind evidence.

## 8. Gate / 게이트

### PASS

**`PASS_US_MINERAL_TRADE_IMPORT_NODE_JOIN_READY`** if all are true:
- authoritative 60-mineral universe frozen;
- official USGS mapping can be represented deterministically with documented weights/caveats;
- Census zero-cost public-file route contains required code/origin/district/mode/time fields;
- fixed-vintage compatibility is defensible;
- non-identifiable mixed-code cases can be prospectively excluded by a source-semantic rule without viewing concentration outcomes;
- a reproducible snapshot/hash plan is defined.

### PARTIAL

`PARTIAL_US_MINERAL_JOIN_SEMANTICS` if most semantics are qualified but one bounded non-outcome component remains unresolved while the research unit remains identifiable.

### HOLD

`HOLD_US_MINERAL_PUBLIC_JOIN_ROUTE` if the zero-cost public-file route or vintage compatibility cannot be established without credential-heavy/paid/tooling rescue.

### REJECT

`REJECT_US_MINERAL_UNIT_NOT_IDENTIFIABLE` if official mapping semantics make mineral-level source-country × entry-node attribution invalid as framed.

## 9. Branch-stop / 중단 규칙

Do not rescue F01 through:
- paid commercial trade databases;
- dashboard/visualization scraping;
- arbitrary manual HTS substitutions;
- selecting only minerals that later show interesting concentration;
- unregistered code aggregation/disaggregation.

If those are needed, apply HOLD/REJECT and return to Stage 0.

## 10. Cost / 비용

Incremental monetary cost must remain **0 USD**. Any potentially billable work requires explicit prior user approval.
