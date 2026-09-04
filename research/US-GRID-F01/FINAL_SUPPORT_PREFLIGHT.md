---
id: US-GRID-F01-FINAL-SUPPORT-PREFLIGHT
type: outcome-blind-final-support-preflight
created: 2026-09-04
relationship_outcome_computed: false
eia_operating_values_opened: false
qualified_entities: 41
excluded_entities: 16
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Final Support & EIA-930 Bulk Snapshot Preflight

## Frozen identity universe

- qualified LBNL entities: **41**
- prospectively excluded entities: **16**
- exact mapping contract: `ALIAS_ADJUDICATION.md`.

## Frozen common cohort

- q_date: **2019-01-01 through 2025-12-31**
- completed-project candidate: `q_status=operational` + explicit `on_date<=2025-12-31`
- no elapsed-duration statistic was calculated.

- all queue rows entering 2019–2025: **19794**
- qualified-entity queue rows: **17453**
- qualified row coverage: **88.173184%**
- operational + explicit on_date rows: **447**
- invalid on_date < q_date: **0**
- completed-cohort duplicate `entity+q_id` groups: **0**
- exact duplicate groups: **0**
- semantic-conflict groups: **0**
- unique completed project keys after frozen duplicate rule: **447**

### Completed-project cardinality by EIA BA (structural only)

| EIA BA | Unique completed project keys |
|---|---:|
| `ERCO` | 229 |
| `PJM` | 102 |
| `FPL` | 38 |
| `MISO` | 24 |
| `SWPP` | 13 |
| `IPCO` | 12 |
| `NWMT` | 10 |
| `CISO` | 9 |
| `SOCO` | 6 |
| `SRP` | 2 |
| `TEC` | 2 |

## Frozen source bytes

- LBNL workbook SHA-256: `794582d3281c6a305e9615fcfec3fae9dc85be2165216d33760b677e976a08b6`
- EIA EBA final URL: `https://www.eia.gov/opendata/bulk/EBA.zip`
- EIA EBA ZIP bytes: **686684023**
- EIA EBA ZIP SHA-256: `3b80081e3720e0075ca151bd81308cd548b076a436c9136baf8656b507a50bb1`
- Content-Type: `application/x-zip-compressed`

### EBA ZIP member inventory (names/sizes only; values unopened)

| Member | Uncompressed bytes | Compressed bytes |
|---|---:|---:|
| `EBA.txt` | 4323307257 | 686683879 |

## Fail-closed rules

1. Future outcome-bearing work must use only the 41 qualified entities and their frozen BA mapping.
2. Exact duplicate rows may collapse only if all source fields used by the experiment are identical.
3. Any conflicting `entity+q_id` is excluded; no preferred row is selected.
4. A project is eligible for the IR→COD outcome only if it entered queue on/after 2019-01-01, is source-status operational, has explicit q_date/on_date, has on_date>=q_date, and on_date<=2025-12-31.
5. EIA operating values were not parsed in F01. A future experiment must preregister its EIA metric before opening relevant EBA values.

## Gate-ready structural conclusion

The source snapshots, BA identity subset, bounded common cohort, direct source-defined IR→COD date pair, and duplicate/null rules are now all frozen without computing queue durations or EIA operating relationships.

Incremental monetary cost remained **0 USD**.
