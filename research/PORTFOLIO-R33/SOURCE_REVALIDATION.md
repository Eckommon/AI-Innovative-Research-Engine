---
id: PORTFOLIO-R33-SOURCE-REVALIDATION
type: official-source-and-overlap-revalidation
created: 2026-09-16
issue: 146
contract_decision: DEC-204
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R33 Source Revalidation / 공식 source 재검증

This record is frozen after Issue #146 binding and before score persistence. It records only current official-source accessibility/identity facts and direct-overlap evidence. No candidate outcome magnitude or relationship direction was opened.

## 1. US-FTA-TRANSIT-001

### Current official access

FTA's current NTD product catalog continues to publish both reliability and safety products at zero incremental cost:

- `2024 Breakdowns` provides vehicle mechanical failures / breakdowns by **Agency, Mode, Type of Service (TOS)**, with direct CSV downloads and metadata/data dictionary through the DOT Open Data Portal.
- The federal data catalog currently describes a `2022–2024 NTD Annual Data - Breakdowns` product and exposes machine-readable resources, confirming current annual breakdown continuity across 2022, 2023 and 2024.
- `Monthly Modal Time Series (Safety and Service)` contains monthly NTD safety/service data by **transit agency × mode × year × month**, from calendar year 2014 to present, and is updated monthly.
- FTA's current Safety and Security access guidance states that Major Safety Events are available at individual-event level from 2014 to present, while Major-Only and threshold-adjusted safety time series are available by agency/mode over longer periods.

Current official source pages:
- https://www.transit.dot.gov/ntd/data-product/2024-breakdowns
- https://catalog.data.gov/dataset/2022-2024-ntd-annual-data-breakdowns
- https://www.transit.dot.gov/ntd/data-product/monthly-modal-time-series-safety-and-service
- https://www.transit.dot.gov/ntd/accessing-national-transit-database-ntd-safety-and-security-event-data
- https://www.transit.dot.gov/ntd/data-product/safety-security-major-only-time-series-data

### Identity / prospective uncertainty

Source-native agency and mode fields make an exact join prospect strong. The remaining high-value uncertainty is not whether a plausible key exists, but whether annual Breakdown reporting scope (Full Reporters, Mode, TOS, year) can be prospectively reconciled with the exact agency/mode reporter scope of the subsequent Major Safety Event products without post-hoc aggregation or denominator drift.

### Direct-overlap boundary

Transit reliability and safety are already jointly recognized performance domains. Current search does not establish novelty and does not justify a novelty claim. However, this revalidation did not find a clearly identical nationwide preregistered design using annual source-native **Breakdowns by agency/mode/TOS** as an exposure structure and **subsequent** Major Safety Events as a separately frozen downstream outcome. Search absence is not novelty proof.

## 2. US-MSHA-001

### Current official access

MSHA's Open Government Initiative Portal remains unusually strong for direct machine-readable access:

- files are described as updated every Friday unless otherwise noted;
- downloadable data are complete-replacement ZIP files containing pipe-delimited text with a header row;
- `Inspections Data Set` lists every mine inspection from 1/1/2000 and identifies **Event Number** as the unique inspection key plus **Mine ID** for linkage to Mines;
- `Violations Data Set` contains violations from 1/1/2000 and explicitly states that Event Number directly links violations to Inspections;
- `Accident Injuries Data Set` contains reported accidents, injuries and illnesses from 1/1/2000;
- `Mines Data Set` uses **Mine ID** as its unique key;
- Employment/Production is also keyed by mine ID/quarter for prospective denominator support if independently authorized later.

Official source:
- https://arlweb.msha.gov/opengovernmentdata/ogimsha.asp
- https://arlweb.msha.gov/opengovernmentdata/ogimsha-instructions.asp

### Direct-overlap boundary

Direct overlap is substantial and prospectively disqualifying for a high novelty score:

- Gernand (2016), summarized by the U.S. Department of Labor CLEAR study profile, explicitly examined MSHA inspection violations as predictors of non-fatal or severe disabling injuries in the following 12 months at underground coal mines.
- A later longitudinal study covering underground coal mines during 2000–2019 used MSHA mine-level violations, dust/noise sampling, mine characteristics and Part 50 injuries and reported that poor regulatory adherence measures predict injury rates.
- MSHA itself uses poor compliance history, previous accidents/injuries/illnesses and other compliance concerns in targeting impact inspections.

Therefore R33 may credit the excellent source structure and exact identity, but it must score low-overlap/novelty at the floor. A descendant would mainly reproduce/extend an established relationship family rather than open a clearly fresh discovery branch.

## 3. US-FRA-XING-001

### Current official access

FRA's safety-data platform currently publishes full datasets for:

- Highway-Rail Grade Crossing Accident/Incident Data (Form 57);
- Crossing Inventory Data — Current (Form 71);
- Crossing Inventory Data — Historical (Form 71).

The National Highway-Rail Crossing Inventory is the national database of crossings, and the FRA crossing system uses the native **U.S. DOT Crossing ID** as the prospective crossing identity. The official data site released in December 2024 and remains linked from FRA's current safety pages.

Official source:
- https://railroads.dot.gov/safety-data/new-safety-data-site
- https://railroads.dot.gov/railroad-safety/divisions/crossing-safety-and-trespass-prevention/crossing-inventory
- https://railroads.dot.gov/safety-data/forms-guides-publications/forms/618071-us-dot-crossing-inventory-form

### Direct-overlap boundary

The domain is already heavily studied with FRA inventory/incident combinations, including recent nationwide accident-risk and severity prediction work using current/historical Form 71 and accident data. Therefore exact-ID feasibility is excellent, but marginal discovery value is low for the frozen inventory-profile → later crossing-incident concept.

R33 must not reinterpret ease of joining as novelty.

## 4. KR-GG-CHEM-001

Carry the R31/R32 source facts without relaxation:

- Gyeonggi public facility metadata and separate chemical-accident records remain publicly available;
- the accident source has not established a stable common source-native business identifier shared with the facility table;
- fuzzy business-name, address-tolerance or geospatial repair is not authorized;
- Korean facility chemical-risk/accident literature creates material direct overlap.

No new source fact removes the previously recorded identity bottleneck.

## Revalidation consequence / 재검증 결론

All four candidates remain scoreable. Current source evidence creates four distinct profiles:

- FTA: current direct downloads, strong native agency/mode identity, moderate within-program dependence and moderate novelty risk;
- MSHA: strongest source/key execution profile but severe direct-overlap penalty;
- FRA: strongest crossing exact-ID execution profile but severe direct-overlap penalty;
- KR-GG-CHEM: meaningful mission/cross-source value but unresolved exact-identity support and high overlap.

No candidate outcome was opened. Proceed to exactly one immutable scorecard under the already-frozen R33 rubric.
