---
id: CA-RAIL-F01-RESULT
type: source-semantic-spatial-temporal-join-feasibility-result
created: 2026-09-04
issue: 83
state: COMPLETED_PASS
final_gate: PASS_CA_RAIL_TERMINAL_WEATHER_JOIN_READY
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 Result — Transport Canada Terminal Dwell × ECCC Weather-Station Join Feasibility
# CA-RAIL-F01 결과 — Transport Canada 터미널 체류시간 × ECCC 관측소 조인 실행가능성

## Final gate / 최종 판정

**PASS_CA_RAIL_TERMINAL_WEATHER_JOIN_READY**

## What was established / 확립된 내용

A deterministic, outcome-blind official-source bridge exists for a nontrivial Canadian freight-rail panel:

`CN/CPKC carrier × terminal area × reporting week → official CGNDB city identity → prospectively selected ECCC station`

No rail-weather association was computed and no weather observation value was opened in F01.

## Frozen rail source / 고정 철도 source

- Transport Canada TDIH full ZIP:
  `https://tdih-cdit.tc.canada.ca/sites/default/files/ferroviaire-rail.zip`
- frozen ZIP SHA-256:
  `e29cd33ea9e65601b4945b7d196cef0fbd539831377a7666ce0ea65886dfd088`
- annual English schemas are identical across 2023–2026.
- the current public surface states that the data are preliminary and may be revised.
- the governing Transportation Information Regulations require weekly reporting for the period Monday through Sunday.

## Frozen future rail outcome construct / 고정 향후 rail outcome

Transport Canada source-defined measure:

**Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**

Frozen simple stratum:
- carriers: **CN and CPKC**;
- commodity: **Intermodal containers**;
- Car_Type / Dwell_Time_Range / Fleet_Status / Employee_Type: `Not Applicable`;
- Segment_Distance_km: `0.0`;
- Unit_of_Measure: **Hours**;
- Status_of_Value: **0 - Available**;
- period: **2024-01-01 through 2025-12-31**.

This avoids manufacturing a terminal-wide average across heterogeneous commodity rows. BNSF is excluded because its source dimension contract is different.

## Structural rail panel / 구조적 rail panel

Before spatial qualification:
- **20 carrier-terminal series**;
- **105 Monday reference dates**;
- **2,100 unique carrier-terminal-week keys**;
- duplicate keys: **0**;
- every one of the 20 source terminal series has **105/105** weeks.

## Official place identity / 공식 place identity

Transport Canada terminal-place tokens are admitted only when they match one pinned CGNDB record under:
- exact case-insensitive linguistic equality after Unicode diacritic folding;
- `Status = Official`;
- `Concise Term = CITY-City`;
- official CGNDB coordinate.

Result:
- **15/15 unique source place tokens qualified**;
- `Montreal` is matched only to official `Montréal`, CGNDB key `EHHUN`, under the pre-frozen diacritic-fold rule;
- no fuzzy geocoding or commercial geocoder is used.

## Frozen ECCC station rule / 고정 ECCC station 규칙

Structurally eligible station:
- one unique ECCC Climate ID row;
- parseable official coordinates;
- DLY First Year <= 2024;
- DLY Last Year >= 2025.

Spatial rule frozen before weather values:
- nearest eligible station distance **<= 20 km**;
- if nearest and second-nearest distances differ by **<= 0.01 km**, exclude fail-closed;
- no manual tie-break or post-outcome station substitution.

Outcome-blind structural support:
- 10 km: 13/15 cities;
- 20 km: 14/15;
- 30/50/75 km: still 14/15.

Therefore 20 km is retained because a larger cap adds no support.

## Final support-qualified universe / 최종 support universe

- qualified carrier-terminal series: **19 / 20**;
- qualified carrier-terminal-week keys: **1,995**;
- final support-key CSV:
  `research/CA-RAIL-F01/FINAL_SUPPORT_KEYS.csv`
- final support-key SHA-256:
  `454bce3a77510cedbe4ff0f81cdc561500ec40462396e63f6f36ef8ebaf361e7`.

Prospective exclusion:
- **CPKC terminal area, Thunder Bay** — nearest and second-nearest eligible ECCC stations are tied at the frozen precision (5.201 km vs 5.201 km); excluded rather than manually choosing a station.

## Time / revision contract / 시간·개정 계약

- rail observation unit is a source reporting week, Monday through Sunday;
- 2024–2025 are the two complete calendar years selected before weather outcomes;
- Transport Canada values are preserved as one hash-pinned preliminary snapshot;
- ECCC historical climate observations may be retrospectively quality-controlled/revised;
- any numerical descendant must pin exact ECCC response/file hashes and one extraction timestamp before analysis;
- no silent replacement of a later revised source is permitted inside one result version.

## What PASS means / PASS 의미

PASS establishes **join and experiment readiness only**.

It means a later controlled experiment can be preregistered on a prospectively qualified 19-series panel without selecting terminals after seeing weather-dwell relationships.

## Claim boundary / 주장 경계

F01 does **not** establish:
- that weather causes rail dwell;
- that any weather variable predicts dwell;
- a temperature/snow/wind threshold;
- carrier or terminal sensitivity rankings;
- exact terminal-yard meteorology;
- causal supply-chain disruption;
- policy or investment superiority.

The spatial exposure unit is an official-city-point → nearby ECCC station proxy, not an exact terminal-facility coordinate.

## Next authorization / 다음 승인 경계

F01 authorizes only one **outcome-blind CA-RAIL-E01 preregistration**.

Before any selected weather observation is opened, E01 must freeze:
1. one primary weather variable;
2. exact Monday-Sunday weekly aggregation;
3. daily completeness/quality rule;
4. outcome transformation;
5. independent-unit / fixed-effect / clustering structure;
6. one primary statistic/model and prospective PASS/NO/HOLD gate;
7. source snapshot/hash procedure.

No multi-weather-variable fishing or same-window terminal selection is authorized.

## Durable evidence / 영속 증거

- `research/CA-RAIL-F01/README.md`
- `research/CA-RAIL-F01/RAIL_SCHEMA_PROBE.md`
- `research/CA-RAIL-F01/SOURCE_PREFLIGHT.md`
- `research/CA-RAIL-F01/OUTCOME_ADJUDICATION.md`
- `research/CA-RAIL-F01/STATION_RULE.md`
- `research/CA-RAIL-F01/STRUCTURAL_SPATIAL_ADJUDICATION.md`
- `research/CA-RAIL-F01/FINAL_SUPPORT_PREFLIGHT.md`
- `research/CA-RAIL-F01/FINAL_SUPPORT_KEYS.csv`

Incremental monetary cost remained **0 USD**.
