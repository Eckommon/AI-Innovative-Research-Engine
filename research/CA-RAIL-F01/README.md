---
id: CA-RAIL-F01
type: source-semantic-spatial-temporal-join-feasibility
state: PREREGISTERED_ACTIVE
created: 2026-09-04
issue: 83
candidate: C-CA-001
decision: DEC-114
mission_anchor: MEM-054
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 — Transport Canada Weekly Terminal-Dwell × ECCC Weather-Station Identity Feasibility
# CA-RAIL-F01 — 캐나다 주간 철도 터미널 체류시간 × ECCC 관측소 식별 실행가능성

## 1. Objective / 목적

Establish whether official Canadian sources support a deterministic bridge:

`carrier × terminal area × week → official populated place → ECCC station → future weekly weather exposure`

before any rail-weather relationship statistic.

## 2. Frozen rail outcome family / 고정 rail outcome

Transport Canada:
**Average Terminal Dwell Time - Loaded Cars and Intermodal Containers**

Source unit:
**Hours**

No alternative rail measure can replace the primary family because it later yields a stronger weather relation.

## 3. Frozen source families / 고정 소스

### Transport Canada TDIH
`https://tdih-cdit.tc.canada.ca/en/rail-2023`

Qualify:
- full ZIP/file download identity/hash;
- exact schema;
- reference-date semantics;
- carrier;
- geography;
- measure/value/unit/status dimensions;
- duplicate and revision behavior.

### NRCan CGNDB
`https://geonames.nrcan.gc.ca/search-place-names/search`

Use only official current populated-place identities.

### ECCC Historical Climate Data
`https://climate.weather.gc.ca/`
`https://climate.weather.gc.ca/map/index_e.html`

Qualify:
- permanent Climate ID;
- station coordinates;
- status and observation availability;
- historical download route;
- weather quality/missingness semantics needed for a future experiment.

## 4. Candidate independent unit / 독립단위

**carrier × source terminal-area geography × reference week**

A source row dimension such as car type, commodity, status or count cannot be silently treated as an independent terminal-week.

## 5. Terminal identity rule / terminal 식별 규칙

F01 may admit only source geography values that can be prospectively parsed as a carrier-specific terminal area.

Expected syntactic class:
`<carrier> terminal area, <place>`

Before any weather values:
- freeze normalization;
- require one official CGNDB populated-place identity;
- exclude ambiguous/missing place identities;
- do not use fuzzy or commercial geocoding.

## 6. Future station mapping / 향후 station mapping

A station rule may be frozen only after structural coverage is known.

It must use:
- official CGNDB place point;
- ECCC station coordinate;
- required observation-period coverage;
- one maximum-distance rule;
- deterministic tie handling;
- no post-outcome station substitution.

## 7. Time and revision / 시간·개정

F01 must freeze:
- exact weekly date interpretation;
- bounded mature period;
- current/preliminary rail revision policy;
- ECCC availability/missingness policy;
- source hash/snapshot behavior.

## 8. Gate / 게이트

PASS:
**`PASS_CA_RAIL_TERMINAL_WEATHER_JOIN_READY`**

PARTIAL:
`PARTIAL_CA_RAIL_JOIN_SEMANTICS`

HOLD:
`HOLD_CA_RAIL_PUBLIC_OR_SPATIAL_ROUTE`

REJECT:
`REJECT_CA_RAIL_TERMINAL_WEATHER_UNIT`

## 9. Exposure boundary / 노출 경계

F01 does not calculate a rail-weather relationship.

No temperature, precipitation, snowfall or wind variable is selected as a primary numerical predictor during F01.

## 10. Cost / 비용

Incremental monetary cost remains **0 USD**.
