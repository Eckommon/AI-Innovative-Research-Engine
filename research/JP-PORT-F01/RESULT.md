---
id: JP-PORT-F01-RESULT
type: source-semantic-spatial-temporal-join-feasibility-result
created: 2026-09-04
issue: 79
state: COMPLETED_PASS
final_gate: PASS_JP_PORT_WEATHER_JOIN_READY
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 Result
# JP-PORT-F01 결과

## Final gate / 최종 판정

PASS_JP_PORT_WEATHER_JOIN_READY

## Summary / 요약

Official zero-cost Japanese public sources support a deterministic prospective bridge:

MLIT port-month identity
→ official C02 port point
→ stable JMA AMeDAS station
→ later daily-weather CSV aggregation

without selecting ports or stations after viewing weather-throughput outcomes.

Key structural findings:
- 160 port identities are stable across the mature 2019–2024 MLIT cargo workbooks;
- 149 have one-to-one official C02 port points;
- JMA detailed history yields 883 stations satisfying full-period precipitation+wind and location-continuity rules;
- all 149 one-to-one ports have a deterministic eligible station within the prospectively frozen 30 km maximum;
- the 149 mappings use 131 unique JMA stations;
- future primary throughput is frozen as monthly total maritime cargo from the port total row and monthly total column.

No weather observation value was opened and no throughput-weather relationship was computed in F01.

## Why PASS rather than PARTIAL/HOLD

1. Exact mature MLIT source files are downloadable, hashed and structurally reproducible.
2. Port identity and monthly cargo outcome semantics are explicit.
3. Official C02 supplies port code/name and point location.
4. Exact/fail-closed port-name normalization is defined.
5. JMA station identity, coordinates, measurement availability and history continuity are directly available.
6. A prospective 30 km nearest-station rule gives broad support without post-outcome rescue.
7. JMA provides official historical observation CSV downloads and explicit quality/homogeneity semantics.
8. Revision, missingness and shared-station pseudoreplication rules are frozen.

## Prospective exclusions

Excluded before outcomes:
- 10 stable port names with ambiguous C02 stem matches;
- 1 stable port unmatched to C02;
- any future station/element that fails the frozen JMA CSV quality/homogeneity rules.

No excluded port may be restored because its later weather relationship is interesting.

## Evidence

- research/JP-PORT-F01/URL_PROBE.md
- research/JP-PORT-F01/SOURCE_PREFLIGHT.md
- research/JP-PORT-F01/SCHEMA_DIAGNOSTIC.md
- research/JP-PORT-F01/SUPPORT_ADJUDICATION.md
- research/JP-PORT-F01/FINAL_SUPPORT_PREFLIGHT.md
- research/JP-PORT-F01/EXECUTION_CONTRACT.md

## Downstream authorization boundary

A PASS authorizes only a separately preregistered JP-PORT-E01.

Before any weather-throughput statistic, E01 must freeze:
- one primary JMA weather construct;
- exact daily element;
- monthly aggregation;
- completeness rule;
- treatment of shared JMA stations;
- throughput transform;
- temporal/seasonal controls;
- primary statistic/model;
- materiality/inference gate;
- Stage A raw CSV snapshot/hash procedure.

If a low-degree-of-freedom design cannot be frozen before weather values, return to Stage 0 rather than searching multiple weather metrics.

Incremental monetary cost remained 0 USD.
