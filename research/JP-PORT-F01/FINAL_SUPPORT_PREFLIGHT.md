---
id: JP-PORT-F01-FINAL-SUPPORT-PREFLIGHT
type: outcome-blind-final-support-preflight
created: 2026-09-04
issue: 79
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 Final Support Preflight
# JP-PORT-F01 최종 지원 사전검증

## Frozen mature MLIT period

Use only the six mature annual Port Survey port-aggregate workbooks for 2019–2024.

Frozen SHA-256:
- 2019: c9b52effc6939080290f9cd2d1eaad894769d5a0af8f5c268bd18dce5218bebf
- 2020: 9ee04b6f968fa475f004c7e397cb74303d6bd3498972ef040c12f3414b1fbe46
- 2021: de510a1510a178a9dc3d3d0dce9ed5ea8da165929ccb0d381458f2005571dd68
- 2022: f5e1402c0fba0afa2b8a74f8e463638c9dc6ef141ed9c08355f39125b6fa61c4
- 2023: 4670b2ac230cae5b2bdc6a50ae03c72001137ca24b9c023a6f90e28e77156d04
- 2024: 830c2173b19f9ea106596e043730bd93616dafe93ef0c6a385d633335cef0200

The mature common port identity is extracted only from the 海上出入貨物 sheet, port total row 種別=計.

Structural result:
- stable exact port-name intersection across all six years: 160
- prefecture-consistent stable ports: 160

Current/preliminary 2025–2026 partial products are excluded from the immediate descendant.

## Frozen port-location bridge

Official MLIT National Land Numerical Information:
https://nlftp.mlit.go.jp/ksj/gml/data/C02/C02-14/C02-14_GML.zip

SHA-256:
5dfda41a2b1b622f328312c437e0d3c4f9bda7bbf276572631e128af70d0af0b

C02 contains official port code/name and point geometry.

Prospective normalization:
- e-Stat keeps names such as 稚内;
- C02 keeps names such as 稚内港;
- remove exactly one terminal 港 from C02 name only;
- no other fuzzy alias or manual name repair.

Result:
- 149 stable ports have exactly one C02 point;
- 10 names are ambiguous and excluded;
- 1 stable e-Stat port is unmatched and excluded.

## Frozen JMA station-history universe

Official JMA station-history file:
https://www.data.jma.go.jp/stats/data/mdrr/chiten/meta/amdmaster.index4

SHA-256:
5e8c212c433fd0322bc1045f4995c24b13949d4d438f902cdf930a6c3b86a9e9

A station is eligible only when:
1. station-history coverage spans all of 2019-01-01 through 2024-12-31;
2. precipitation statistic exists throughout;
3. wind statistic exists throughout;
4. no precipitation statistical disconnection occurs during the window;
5. no wind statistical disconnection occurs during the window;
6. representative latitude/longitude do not change at 0.001 degree precision during the window.

Eligible station IDs: 883.

## Frozen port-to-station rule

Maximum geodesic distance: 30 km.

The cap was selected before any throughput-weather relationship. JMA documents approximate 21 km spacing for the roughly 840 four-element AMeDAS stations.

Rules:
- nearest eligible station by geodesic distance;
- distance must be <=30 km;
- nearest-station tie within 0.01 km => exclude port;
- never replace with a farther station after observing results.

Structural support:
- <=10 km: 118 ports
- <=20 km: 146 ports
- <=30 km: 149 ports
- all 149 one-to-one C02 ports pass the 30 km rule.

Final prospective support-qualified port universe:
149 ports.

## Shared-weather pseudoreplication

The 149 port mappings use:
- 131 unique JMA station IDs;
- 16 station IDs are shared by more than one port;
- those shared stations account for 34 port mappings.

Therefore a later numerical experiment must not treat every port-month as an independent weather observation.

At minimum:
- shared station-month exposure must be recognized explicitly;
- inference must cluster or otherwise account for JMA-station dependence;
- no port may be remapped merely to obtain a unique station.

## Frozen future throughput outcome

Primary future throughput outcome:
monthly total maritime cargo at the port level.

MLIT schema:
- sheet: 海上出入貨物
- row: port 種別=計
- month subcolumn: 合計
- source unit label: トン数

Interpretation boundary:
the Port Survey freight-ton convention must be preserved; it must not be silently described as pure physical mass tonnage.

## JMA observation access and quality contract

Official historical CSV download route:
https://www.data.jma.go.jp/risk/obsdl/

JMA explicitly provides historical AMeDAS observations as downloadable CSV without user registration.

Future primary weather values may be opened only after a descendant preregistration freezes exact elements and aggregation.

Quality rule for the future primary weather aggregation:
- use only JMA quality code 8, normal value;
- quality 5, 4, 2, 1 or 0 is not used in the primary aggregation;
- a month must meet a preregistered completeness rule before analysis;
- if downloaded data show multiple homogeneity numbers for a selected station/element during the frozen period, that station is excluded from that descendant rather than remapped.

## Revision policy

MLIT:
- use only the frozen mature annual workbooks above;
- do not mix current preliminary/partially revised monthly values into the 2019–2024 snapshot.

JMA:
- E01 Stage A must download the preregistered bounded CSV batches and pin every raw CSV SHA-256 before any throughput-weather statistic;
- JMA notes that historical observations may be corrected retrospectively, so an intentional refresh requires a new source manifest before numerical execution.

## Gate-ready conclusion

The exact mature MLIT source snapshots, direct monthly throughput outcome semantics, deterministic port location identity, deterministic stable-station mapping rule, common period, station-quality semantics and pseudoreplication rules are all established without computing a weather-throughput relationship.

Incremental monetary cost remained 0 USD.
