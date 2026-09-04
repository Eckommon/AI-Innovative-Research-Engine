---
id: WAVE3-GEO-D01-SOURCE-REGISTRY
type: official-source-registry
created: 2026-09-04
issue: 82
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# WAVE3-GEO-D01 Official Source Registry
# WAVE3-GEO-D01 공식 소스 레지스트리

This is a bounded discovery registry, not a national-catalog harvest.

## Canada

### Transport Canada — Weekly freight rail service and performance
Official:
https://tdih-cdit.tc.canada.ca/en/rail-2023

Current source surface exposes weekly records from 2023 through 2026 and offers a full English/French ZIP download.

Observed source dimensions include:
- reference date;
- carrier;
- geography;
- car type;
- commodity;
- measure;
- measure value;
- unit;
- value status;
- segment distance where applicable.

Direct operational measures include:
- Average Terminal Dwell Time - Loaded Cars and Intermodal Containers;
- Average Terminal Dwell Time - Empty Cars and Intermodal Containers;
- Average Dwell Time at Origin / Destination;
- Segment Transit Time;
- Average Velocity;
- loaded/intermodal units not moving at origin, destination or en route.

Named geographies include carrier-specific terminal areas and carrier-specific segments.

### Environment and Climate Change Canada — Historical Climate Data
Official:
https://climate.weather.gc.ca/

Official station map/search:
https://climate.weather.gc.ca/map/index_e.html

ECCC exposes:
- Climate ID as a permanent unique site identifier under source semantics;
- station name;
- latitude/longitude/elevation;
- status/operator;
- hourly/daily/monthly availability dates;
- downloadable historical hourly/daily/monthly data.

Weather includes temperature, precipitation, wind speed/direction and related variables.

### NRCan / Geographical Names Board of Canada — CGNDB
Official:
https://geonames.nrcan.gc.ca/search-place-names/search

CGNDB provides official populated-place identities and coordinates. It is a possible outcome-blind bridge from the city token embedded in a Transport Canada terminal-area geography label to a stable official point before selecting an ECCC station.

### Canadian Grain Commission — Grain Statistics Weekly
Official:
https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/

Weekly CSV/Excel data expose grain movement, stocks and terminal-position activity. Historical crop-year archives are available.

Potential relationship:
weekly grain-flow pressure → rail terminal dwell / corridor performance.

Limitation:
terminal/rail geography compatibility and causal direction are less clean than the weather→rail operational-stress candidate.

## Australia

### AEMO — NEM dispatch / NEMDE
Official:
https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/market-operations/dispatch-information

AEMO describes NEMDE as central dispatch subject to constraints and publishes dispatch results at five-minute frequency.

Current technical data model exposes public dispatch families including:
- DISPATCHCONSTRAINT;
- DISPATCHPRICE;
- DISPATCHREGIONSUM;
- DISPATCHINTERCONNECTORRES.

Constraint semantics include LHS, RHS and MARGINALVALUE/shadow price. Dispatch tables update every five minutes.

AEMO released Data Model 5.8 material in August 2026; source-version/report-path handling is therefore material for any F01.

### Australian Bureau of Meteorology — Weather Data Services
Official:
https://www.bom.gov.au/catalogue/data-feeds.shtml

BOM exposes station observations through automated feeds, including station-based observations in machine-readable formats such as JSON/XML.

Potential relationship:
regional weather / renewable-operating conditions → NEM constraint shadow price, interconnector flow stress or regional price separation.

Limitation:
a defensible physical weather→constraint mapping must avoid selecting constraint IDs or regions after outcome inspection, and current AEMO report/version transitions increase source-contract complexity.

### BITRE — Waterline
Official:
https://www.bitre.gov.au/statistics/freight

Current latest Waterline found in the discovery refresh:
Waterline 70, released 2 December 2024, covering terminal activity through the June quarter 2023.

It publishes downloadable throughput, container-terminal performance, VBS/TAS and cost-index tables for five major container ports.

Potential relationship:
port weather exposure → container-terminal productivity/throughput.

Limitation:
quarterly/half-year reporting and stale latest covered activity materially reduce near-term information gain versus Canada weekly rail or AEMO five-minute data.

## Cross-national

### OECD Data Explorer / ITF
Official SDMX API:
https://sdmx.oecd.org/public/rest/

Transport datasets include infrastructure, activity, traffic, economic/social and energy/environment performance indicators.

### World Bank Indicators API
Official:
https://api.worldbank.org/v2/

The V2 API is public and does not require authentication.

Potential use:
cross-national normalization or external comparator for a concrete operational candidate.

Screen-out:
do not promote a generic GDP/infrastructure/emissions correlation merely because the APIs are easy to query. Annual macro grain is not a direct enough operational bottleneck for this D01.

## Discovery source-access conclusion

The strongest immediately minimum-operable source pair is:

Transport Canada weekly rail performance
× ECCC historical weather
with NRCan CGNDB as a possible official location bridge.

Incremental monetary cost remained **0 USD**.
