---
id: CA-RAIL-F01-STATION-RULE
type: outcome-blind-spatial-support-rule
created: 2026-09-04
issue: 83
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-F01 Final Place / Station Rule
# CA-RAIL-F01 최종 place / station 규칙

## Official place identity

For each Transport Canada source token parsed from `<carrier> terminal area, <place>`:

1. require exact linguistic name equivalence after casefold + Unicode diacritic folding only;
2. require a single CGNDB record whose `Status` is `Official`;
3. require `Concise Term = CITY-City`;
4. use the CGNDB official feature coordinate;
5. no fuzzy matching, commercial geocoder, administrative guess or outcome-based repair.

`Montreal` from Transport Canada is prospectively normalized to the official CGNDB `Montréal` record only because the names are identical under diacritic folding and the official record is unique under `Official + CITY-City`; CGNDB key `EHHUN` is pinned.

## ECCC station eligibility

A station is structurally eligible only if:
- official ECCC Station Inventory contains one unique `Climate ID` row;
- latitude/longitude are parseable;
- `DLY First Year <= 2024`;
- `DLY Last Year >= 2025`.

No weather observation value is opened for this rule.

## Frozen spatial support rule

For each qualified official city point:

- calculate great-circle distance to every structurally eligible ECCC station;
- select the nearest station only if distance is **<= 20 km**;
- if the nearest and second-nearest eligible stations differ by **<= 0.01 km**, classify the city as spatially ambiguous and exclude it fail-closed;
- no manual tie-break and no station substitution.

### Why 20 km

The prior outcome-blind structural diagnostic showed support among the 14 already resolved cities:
- 10 km: 12/14;
- 20 km: 13/14;
- 30 km: 13/14;
- 50 km: 13/14;
- 75 km: 13/14.

Thus increasing the cap above 20 km provided no additional structural support. The 20 km cap is frozen before any weather observation or dwell-weather relationship.

## Rail unit

Frozen rail stratum remains:
- CN and CPKC only;
- commodity `Intermodal containers`;
- source measure `Average Terminal Dwell Time - Loaded Cars and Intermodal Containers`;
- `Status_of_Value = 0 - Available`;
- period 2024-01-01 through 2025-12-31;
- candidate independent unit `carrier × terminal area × reference week`.

Incremental monetary cost remains **0 USD**.
