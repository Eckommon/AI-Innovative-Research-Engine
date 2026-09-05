---
id: PORTFOLIO-R07-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-05
issue: 85
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-AU-001
selected_gate: AU-NEM-F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R07 Result — Post-Canada-Rail HOLD Mission-ROI Reselection
# PORTFOLIO-R07 결과 — 캐나다 철도 HOLD 이후 목적-ROI 재선정

## Final selection / 최종 선정

**SELECT_C_AU_001_NEM_WEATHER_CONSTRAINT_INTELLIGENCE**

Selected candidate:

**C-AU-001 — Australian NEM Weather × Constraint/Congestion Intelligence**
**C-AU-001 — 호주 NEM 기상 × 제약/혼잡 지능화**

Exact next bounded gate:

**AU-NEM-F01 — AEMO Dispatch Constraint/Interconnector × BOM Gridded-Weather Region Identity & Zero-Cost Source Feasibility**

## Why the selection changed / 선정 변화 이유

CA-RAIL-F01 remains a valuable deterministic bridge, but its first preregistered descendant stopped before Stage B because the frozen ECCC Minimum Temperature source-completeness contract failed.

That makes an immediate Canada-rail rescue a new design with both redesign risk and diminishing marginal information value.

R07 therefore re-compares preserved candidates rather than replacing Min Temp or remapping stations.

## Current official-source refresh / 현행 공식 source 갱신

### Australia — AEMO

AEMO currently publishes public five-minute NEM Dispatch files in comma-delimited flat-file form.

Current and archive routes are directly browsable under NEMWeb:
- https://www.nemweb.com.au/Reports/CURRENT/DispatchIS_Reports/
- https://www.nemweb.com.au/Reports/ARCHIVE/DispatchIS_Reports/

AEMO states that the dispatch family covers:
- interconnector flows;
- constraints;
- regional reference price;
- demand;
- dispatchable generation/load;
- ancillary-service data.

AEMO constraint documentation states that in DispatchConstraint:
- non-zero MarginalValue identifies a binding constraint equation;
- non-zero ViolationDegree identifies a violating constraint equation;
- MarginalValue is the marginal cost of a 1 MW RHS change in the NEMDE objective.

AEMO's current NEM region documentation defines five price regions:
- Queensland;
- New South Wales including ACT;
- South Australia;
- Victoria;
- Tasmania.

### Australia — BOM / AWO

BOM currently exposes Climate Data Online for historical station observations and publishes Australian gridded climate products.

Australian Water Outlook official data-access documentation states that:
- AWO product pages provide NetCDF / time-series CSV downloads;
- AWDS provides web-service access;
- NCI Data Collection provides underlying daily gridded climate input data;
- climate input families include rainfall, wind, solar radiation and temperature.

R07 does not assume that every BOM climate product is free. AU-NEM-F01 must prove one reproducible zero-cost weather route and reject any path that requires paid extraction.

### Canada grain × rail

Canadian Grain Commission continues to publish Grain Statistics Weekly in open CSV format, with current 2026–2027 data and historical archives.

The source is operationally rich, but a new grain→rail-dwell experiment would require a new rail commodity/outcome stratum and a defensible terminal/geography mapping. The earlier intermodal rail construct is not automatically interchangeable with grain flow.

### ENTSO-E

Cross-national EU grid remains high-value, but current official guidance still requires Transparency Platform registration plus a separately granted Web API security token.

### Singapore

MPA vessel-arrival monthly data and NEA Changi monthly climate data remain directly downloadable and keyless at normal public limits.

However the candidate is primarily one national port-system time series at monthly grain, limiting independent-unit strength relative to the Australia NEM candidate.

### EU industrial-site climate

The EEA facility-coordinate × NASA POWER join remains technically PASS and reusable, but a low-DOF direct operational outcome remains under-specified. R07 preserves it rather than forcing a weak regression.

## Mission-ROI scoring / 목적-ROI 점수

0–5 per dimension; total /45. Scores are portfolio aids, not empirical results.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent unit | Practical value | Current access | Join defensibility | Next-gate info gain | Low diminishing-return risk | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-AU-001 NEM Weather–Constraint/Congestion** | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | **42** | **SELECT** |
| C-EU-001 Cross-National Grid Stress | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 4 | 4 | **38** | HOLD_HIGH_VALUE_CREDENTIAL |
| C-CA-002 Grain-Flow × Rail Dwell | 5 | 5 | 5 | 3 | 5 | 5 | 3 | 3 | 2 | **36** | HOLD_REDESIGN_REQUIRED |
| C-SG-001 Maritime Activity × Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 3 | 4 | 5 | 5 | 2 | 4 | **35** | PRESERVE_JOIN_ASSET |
| Canada rail weather redesign | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 2 | 1 | **35** | NO_AUTO_RESCUE |
| Japan port-weather continuation | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 2 | 1 | **33** | VALIDATED_NO_AUTO_TUNING |

## Why C-AU-001 wins / 왜 C-AU-001인가

C-AU-001 combines:
- a source-defined direct operational congestion surface;
- high-frequency public data;
- multiple regions / interconnectors rather than one national time series;
- a new national operating regime;
- official public weather data routes;
- a meaningful unresolved question: can physical constraint/interconnector identity be mapped prospectively to a defensible regional weather exposure without outcome-driven geographic inference?

The unresolved identity problem itself is high-value information. A bounded F01 can reject the candidate before any relationship statistic if region/constraint semantics are not defensible.

## Exact next gate / 정확한 다음 gate

Open exactly:

### AU-NEM-F01 — AEMO Dispatch Constraint/Interconnector × BOM Gridded-Weather Region Identity & Zero-Cost Source Feasibility

F01 must:
1. freeze exact AEMO public current/archive file families and current schema/version evidence;
2. verify DispatchConstraint / DispatchInterconnectorRes / DispatchRegionSum identities without computing weather relationships;
3. establish the source-defined NEM region and interconnector vocabulary;
4. determine whether binding-constraint identity can be assigned prospectively to one region or one region-pair using official AEMO semantics;
5. if generic constraints are not deterministically regionalizable, test the predeclared interconnector-outcome fallback rather than fuzzy classification;
6. qualify one zero-cost BOM/AWO daily gridded-weather access route;
7. establish a deterministic NEM-region geometry route, using official region/state semantics and official machine geometry if required;
8. test only source/schema/cardinality/time identity and no weather-congestion relationship;
9. freeze a single future operational outcome family or return HOLD/REJECT.

## Outcome priority / outcome 우선순위

Prospective priority entering F01:
1. source-defined binding-constraint burden if constraint→region/region-pair identity is deterministic;
2. otherwise source-defined interconnector congestion/transfer-stress outcome if the public fields support a direct construct;
3. otherwise HOLD; do not invent a generic stress score.

## Stop rule / 중단 규칙

Return to Stage 0 if:
- the AEMO constraint identity requires post-hoc text interpretation;
- region weather exposure requires a paid BOM product;
- only a tiny hand-selected constraint subset can be mapped;
- current data-model transitions make one reproducible schema contract impossible;
- a direct congestion outcome cannot be frozen without observed-effect selection.

Incremental monetary cost remained **0 USD**. Any potentially billable action requires explicit prior approval.
