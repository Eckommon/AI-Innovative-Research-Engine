---
id: US-GRID-E01-PREREG-STRUCTURAL-PREFLIGHT
type: outcome-blind-prereg-structural-preflight
created: 2026-09-04
queue_duration_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-E01 Preregistration Structural Maturity Preflight

No IR→COD elapsed duration was calculated. Only queue-entry year, source status, explicit-date availability and BA cardinality were counted.

## Completed-project structure by queue-entry year

| q_year | Unique completed project keys | # represented BAs |
|---:|---:|---:|
| 1997 | 10 | 1 |
| 1998 | 11 | 2 |
| 1999 | 37 | 4 |
| 2000 | 47 | 4 |
| 2001 | 60 | 5 |
| 2002 | 51 | 5 |
| 2003 | 78 | 7 |
| 2004 | 74 | 7 |
| 2005 | 124 | 8 |
| 2006 | 117 | 8 |
| 2007 | 200 | 9 |
| 2008 | 114 | 9 |
| 2009 | 113 | 11 |
| 2010 | 168 | 11 |
| 2011 | 133 | 10 |
| 2012 | 111 | 8 |
| 2013 | 134 | 8 |
| 2014 | 146 | 9 |
| 2015 | 198 | 11 |
| 2016 | 239 | 13 |
| 2017 | 214 | 10 |
| 2018 | 173 | 11 |
| 2019 | 193 | 11 |
| 2020 | 122 | 9 |
| 2021 | 60 | 8 |
| 2022 | 21 | 3 |
| 2023 | 37 | 5 |
| 2024 | 5 | 1 |
| 2025 | 9 | 1 |

## Candidate preregistration windows

| Window | Projects | Represented BAs | BAs with >=3 projects |
|---|---:|---:|---:|
| 2021-2022 | 81 | 8 | 4 |
| 2021-2023 | 118 | 9 | 5 |
| 2021-2024 | 123 | 9 | 5 |

## BA counts for 2021–2022 candidate

| BA | Projects |
|---|---:|
| `ERCO` | 62 |
| `IPCO` | 6 |
| `FPL` | 5 |
| `NWMT` | 4 |
| `CISO` | 1 |
| `SWPP` | 1 |
| `TEC` | 1 |
| `SRP` | 1 |

## Design implication

- A two-prior-year EIA predictor requires q_date no earlier than 2021 because the frozen EBA family begins in 2019.
- Using q_date through 2022 gives every selected project at least three calendar years between the latest queue-entry year and the 2025-12-31 outcome snapshot, while remaining a completed-project construct.
- This is a maturity heuristic chosen before any duration magnitude or EIA value is inspected; it is not an official LBNL/EIA correction window.

Incremental monetary cost remained **0 USD**.
