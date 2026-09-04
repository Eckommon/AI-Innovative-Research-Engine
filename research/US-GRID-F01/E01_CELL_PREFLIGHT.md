---
id: US-GRID-E01-CELL-PREFLIGHT
type: outcome-blind-ba-year-cell-preflight
created: 2026-09-04
queue_duration_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-E01 BA × Queue-Entry-Year Structural Preflight

Window inspected structurally: **2021–2023**. No elapsed duration or EIA operating value was calculated.

## All BA-year completed-project counts

| BA | q_year | Completed project keys | >=3? |
|---|---:|---:|---|
| `CISO` | 2021 | 1 | NO |
| `ERCO` | 2021 | 45 | YES |
| `ERCO` | 2022 | 17 | YES |
| `ERCO` | 2023 | 29 | YES |
| `FPL` | 2021 | 3 | YES |
| `FPL` | 2022 | 2 | NO |
| `IPCO` | 2021 | 4 | YES |
| `IPCO` | 2022 | 2 | NO |
| `IPCO` | 2023 | 1 | NO |
| `NWMT` | 2021 | 4 | YES |
| `NWMT` | 2023 | 2 | NO |
| `SOCO` | 2023 | 2 | NO |
| `SRP` | 2021 | 1 | NO |
| `SWPP` | 2021 | 1 | NO |
| `SWPP` | 2023 | 3 | YES |
| `TEC` | 2021 | 1 | NO |

## Frozen candidate support rule diagnostic

- BA-year cell requires **>=3** completed project keys.
- BA requires **>=2 qualifying BA-year cells** so the primary analysis can use within-BA variation rather than pure cross-BA level differences.
- qualifying cells before >=2-year BA rule: **7**
- BAs with >=2 qualifying years: **1**
- final structural candidate cells: **3**
- final structural candidate projects: **91**

### Retained BA-year cells

| BA | q_year | Projects |
|---|---:|---:|
| `ERCO` | 2021 | 45 |
| `ERCO` | 2022 | 17 |
| `ERCO` | 2023 | 29 |

## Interpretation

This is a source/cardinality gate only. The >=3-project and >=2-year rules are prospective anti-pseudoreplication rules, not result-driven filters.
If this structure is too sparse for a bounded within-BA experiment, E01 should not be forced; return to Stage 0 rather than loosen filters after outcomes.

Incremental monetary cost remained **0 USD**.
