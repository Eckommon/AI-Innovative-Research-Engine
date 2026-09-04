---
id: US-GRID-F01-COHORT-DIAGNOSTIC
type: outcome-blind-prospective-cohort-diagnostic
created: 2026-09-04
relationship_outcome_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Prospective 2019–2025 Cohort Diagnostic

## Frozen structural cohort candidate

- queue-entry date: **2019-01-01 through 2025-12-31**
- completion status candidate: source `q_status = operational` with explicit `on_date <= 2025-12-31`
- reason: entire project interval must begin no earlier than the frozen EIA-930 2019-present bulk family.
- no elapsed-duration statistic was computed.

## Cardinality

- all LBNL rows with q_date in 2019–2025: **19794**
- rows in conservative BA-attribution candidate set: **17783**
- operational rows with explicit on_date by 2025-12-31: **447**
- invalid on_date < q_date rows: **0**
- duplicate composite-key groups inside completed cohort: **0**
- exact duplicate groups: **0**
- semantic-conflict groups: **0**
- unique completed project keys after exact-collapse/conflict-exclusion: **447**

## Prospective BA project cardinality

| EIA BA code | Unique completed project keys |
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

## Prospective LBNL entity project cardinality

| LBNL entity | EIA BA candidate | Unique completed project keys |
|---|---|---:|
| `CAISO` | `CISO` | 9 |
| `ERCOT` | `ERCO` | 229 |
| `FPL` | `FPL` | 38 |
| `IP` | `IPCO` | 12 |
| `MISO` | `MISO` | 24 |
| `NWMT` | `NWMT` | 10 |
| `PJM` | `PJM` | 102 |
| `SOCO` | `SOCO` | 6 |
| `SRP` | `SRP` | 1 |
| `SRP_ANPP` | `SRP` | 1 |
| `SPP` | `SWPP` | 13 |
| `TEC` | `TEC` | 2 |

## Excluded identity candidates at this stage

`BHCT`, `BHP`, `CLPT`, `CSU`, `Duke`, `GTC`, `MPC`, `N-C`, `OUC`, `PRPA`, `PacifiCorp`, `TSGT`, `WAPA-MPP`

These exclusions are identity-semantic, not result-based. They may not be reintroduced after relationship outcomes without a new mission-level authorization.

## Duplicate rule candidate

1. Exact duplicate rows with identical source fields may collapse to one source record.
2. Any `entity+q_id` key with conflicting `q_status/q_date/on_date/wd_date/ia_date` is excluded prospectively; no preferred row is chosen.
3. If conflicts remain material inside the frozen cohort, F01 must HOLD rather than select a favorable record.

Incremental monetary cost remained **0 USD**.
