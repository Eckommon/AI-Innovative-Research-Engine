---
id: WAVE3-GEO-D01-RESULT
type: geographic-relationship-discovery-result
created: 2026-09-04
issue: 82
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-001
selected_gate: CA-RAIL-F01
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# WAVE3-GEO-D01 Result — Canada / Australia / OECD-World Bank Candidate Discovery
# WAVE3-GEO-D01 결과 — 캐나다 / 호주 / OECD-World Bank 후보 탐색

## Final selection / 최종 선정

**SELECT_C_CA_001_FREIGHT_RAIL_WEATHER_DELAY_INTELLIGENCE**

Selected candidate:

**C-CA-001 — Canadian Freight Rail Weather–Delay Intelligence**  
**C-CA-001 — 캐나다 화물철도 기상–지연 병목 지능화**

Exact next bounded gate:

**CA-RAIL-F01 — Transport Canada Weekly Terminal-Dwell × ECCC Weather-Station Identity & Join Feasibility**

No rail-weather relationship statistic was calculated during D01.

## Shortlisted relationships / 후보 관계

### 1. C-CA-001 — Freight Rail Weather–Delay Intelligence — SELECT

Relationship surface:

Transport Canada carrier-specific terminal area × week operational performance
+ official terminal-city identity/location
+ ECCC station weather
→ weekly rail terminal dwell / throughput-friction regime

Primary direct outcome family for F01 qualification:
**Average Terminal Dwell Time - Loaded Cars and Intermodal Containers (hours)**.

Why strong:
- weekly direct operational bottleneck outcome;
- carrier-specific named terminal-area units;
- current observations spanning 2023–2026;
- full dataset download;
- ECCC provides source-defined station IDs, coordinates and historical weather;
- Transport Canada's 2025 national report explicitly treats winter conditions, wildfire/flood exposure and congestion as material rail-corridor operating risks;
- completely new branch relative to prior project validated results.

Critical F01 uncertainty:
Can a carrier-specific named terminal area be mapped prospectively to one official location and one eligible ECCC station without manual post-outcome geocoding, while preserving weekly/revision semantics?

### 2. C-CA-002 — Grain-Flow Pressure × Rail Dwell

Source pair:
Canadian Grain Commission Grain Statistics Weekly
× Transport Canada weekly rail performance.

Candidate relationship:
weekly grain receipts/shipments/export pressure
→ western rail terminal dwell / loaded-car immobility.

Strength:
both source families are weekly and the demand-pressure mechanism is operationally plausible.

Limitation:
grain terminal positions and carrier terminal/segment geographies are not yet shown to be the same independent unit; grain flow can also be jointly determined with rail capacity, creating a less clean first construct than weather exposure.

Disposition:
HOLD_READY_SECONDARY.

### 3. C-AU-001 — NEM Weather × Constraint/Congestion Intelligence

Source pair:
AEMO NEM dispatch/constraint results
× BOM weather observations.

Candidate relationship:
predefined regional/weather state
→ five-minute constraint shadow-price / regional price-separation / interconnector-stress outcome.

Strength:
very high temporal resolution and direct operational electricity-market/grid constraint semantics.

Limitations:
- the project already has substantial grid-domain evidence from UK/U.S. branches;
- constraint-ID/region/weather identity needs a disciplined prospective mapping;
- current AEMO report/data-model transitions add version-contract complexity.

Disposition:
HOLD_READY_HIGH_VALUE.

### 4. C-AU-002 — Container-Port Weather × Productivity

Source pair:
BITRE Waterline
× BOM weather.

Candidate relationship:
port-quarter weather exposure
→ container-terminal productivity / throughput.

Strength:
five named major ports and direct productivity measures.

Limitation:
latest identified Waterline publication covers only through June quarter 2023, with coarse reporting grain. Lower marginal information than C-CA-001.

Disposition:
HOLD_SECONDARY.

### 5. C-XN-001 — OECD/World Bank Transport-System Stress Normalization

Source pair:
OECD ITF transport indicators
× World Bank national indicators.

Candidate relationship:
transport infrastructure/activity normalization
→ cross-national transport stress/resilience indicator.

Disposition:
NO_PROMOTION_IN_D01.

Reason:
the available relationship is primarily annual/macroeconomic and risks becoming a generic correlation rather than a direct operational bottleneck. OECD/World Bank remain useful future normalization layers, not the primary experiment source here.

## Mission-ROI scoring / 목적-ROI 점수

0–5 per dimension; total /45. Scores are selection aids, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent unit | Practical value | Current access | Join defensibility | F01 info gain | Low diminishing return | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **C-CA-001 Rail Weather–Delay** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | **43** | **SELECT** |
| C-AU-001 NEM Weather–Constraint | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 4 | 3 | **40** | HOLD_READY_HIGH_VALUE |
| C-CA-002 Grain Pressure–Rail Dwell | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 4 | 5 | **41** | HOLD_READY_SECONDARY |
| C-AU-002 Port Weather–Productivity | 4 | 4 | 4 | 3 | 4 | 5 | 4 | 3 | 4 | **35** | HOLD_SECONDARY |
| C-XN-001 OECD/WB Transport Stress | 3 | 4 | 2 | 4 | 3 | 5 | 5 | 2 | 5 | **33** | NO_PROMOTION |

C-CA-001 wins because it combines a direct weekly operational outcome, a distinct new domain/geography, strong public access and a high-value source-semantic uncertainty that can be resolved before any relationship statistic.

## Current source facts supporting selection / 현행 소스 근거

### Transport Canada
The public weekly rail surface currently exposes 2023, 2024, 2025 and 2026 reference-date records and a downloadable full dataset.

Measures include:
- Average Terminal Dwell Time - Loaded Cars and Intermodal Containers;
- Segment Transit Time;
- Average Velocity;
- multiple not-moving car/container measures.

The 2025 Transportation in Canada report states that:
- grain demand put pressure on western export corridors;
- winter conditions posed challenges;
- wildfire/flood exposure adds rail-corridor risk;
- congestion at west-coast ports can propagate inland.

These statements motivate the bottleneck question but do not count as the D01 experiment result.

### ECCC
Historical Climate Data supports hourly, daily and monthly data, station identifiers and coordinates. The station-search layer exposes Climate ID, TC ID where available, WMO ID, latitude/longitude, station status and availability periods.

### NRCan CGNDB
CGNDB supplies official place-name identities and supports exact populated-place searches. It is a prospective bridge for terminal-area city tokens, not a post-outcome geocoder.

## Exact next gate / 정확한 다음 게이트

Open:

### CA-RAIL-F01 — Transport Canada Weekly Terminal-Dwell × ECCC Weather-Station Identity & Join Feasibility

F01 is source-semantic / spatial-temporal feasibility only.

It must:
1. freeze exact Transport Canada full-dataset URL/snapshot/hash and schema;
2. freeze the source-defined weekly reference-date semantics and preliminary/revision/status rules;
3. isolate only carrier-specific named terminal-area records;
4. qualify exactly one future terminal-dwell outcome family before any weather relationship;
5. test whether terminal-area labels yield a deterministic official populated-place identity using source text + CGNDB without fuzzy repair;
6. freeze ECCC station identity, coordinates and observation-availability metadata;
7. define a prospective terminal-place→weather-station rule and maximum distance before weather/dwell outcomes;
8. determine common weekly coverage and weather aggregation boundary;
9. freeze duplicate/missing/value-status/revision rules;
10. determine whether a nontrivial multi-terminal future experiment is supportable without choosing terminals after outcomes.

F01 shall not calculate:
- weather vs dwell correlations;
- terminal sensitivity;
- weather thresholds;
- carrier rankings;
- causal delay;
- investment/policy rankings.

## Stop rule / 중단 규칙

HOLD/REJECT and return to Stage 0 if:
- terminal-area city identity cannot be extracted deterministically;
- official-place → station mapping requires subjective manual choices;
- only a tiny terminal subset survives;
- weekly rail revision/status semantics cannot be made reproducible;
- weather data require paid/custom service;
- an alternative rail measure is selected after seeing weather relationships.

## Cost / 비용

Incremental monetary cost remained **0 USD**. Any potentially billable work requires explicit prior approval.
