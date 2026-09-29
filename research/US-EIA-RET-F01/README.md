---
id: US-EIA-RET-F01
type: outcome-blind-structural-feasibility
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R48
parent_decision: DEC-278
selected_candidate: US-EIA-RET-001
selection_score: 43
future_retirement_membership_opened: false
post_august_2026_860m_body_opened: false
planned_proposed_row_bodies_opened: 0
eia923_row_bodies_opened: 0
incremental_monetary_cost_usd: 0
---

# US-EIA-RET-F01 — exact generator monthly-lineage gate before future retirement

## Mission / 목적

Determine, **before opening any retirement membership from September 2026 or later EIA-860M data months**, whether the official EIA monthly generator inventory supports a deterministic prospective retirement design using exact Plant ID + Generator ID and twelve explicitly archived historical monthly files.

This is the corrected non-colliding descendant of the R48-selected **generator structure/performance → subsequent retirement** concept. It is distinct from and does not reopen the terminal R36 `US-EIA-GEN-F01` commissioning-slippage branch.

F01 is structural only. It does not test whether generator age, fuel, technology, capacity, ownership, operation, utilization, performance or any other characteristic predicts retirement.

## Frozen official source family / 공식 소스

Primary source index:

`https://www.eia.gov/electricity/data/eia860m/index.php`

Supporting source/documentation:

- annual EIA-860: `https://www.eia.gov/electricity/data/eia860/index.php`
- EIA-923: `https://www.eia.gov/electricity/data/eia923/index.php`

EIA documents that:
- EIA-860M monitors current existing and proposed generating units monthly;
- identifiable historical monthly files are published on the 860M index;
- starting with March 2017 data, each monthly inventory includes a comprehensive Retired tab for generators retired since 2002;
- monthly inventory values are preliminary and may be revised in subsequent inventories.

## Frozen historical window / 고정 역사 window

Attempt 01 may open exactly these **twelve data-month workbooks**:

1. September 2025
2. October 2025
3. November 2025
4. December 2025
5. January 2026
6. February 2026
7. March 2026
8. April 2026
9. May 2026
10. June 2026
11. July 2026
12. August 2026

The scientific month list is immutable.

### URL resolution rule / URL 해석 규칙

The runner must resolve each workbook from the official 860M index using the exact source-visible month/year entry and its adjacent XLS link.

- Only `eia.gov` / `www.eia.gov` official HTTPS targets are accepted.
- The runner may follow official redirects.
- It may not substitute a different month, annual EIA-860 file, mirror, cache, commercial source or manually guessed non-index source to rescue access.
- Differences between EIA's current `/xls/` and historical `/archive/xls/` path organization are transport representation only; the exact twelve source-visible month labels remain the scientific contract.

Each workbook must be fingerprinted with resolved URL, HTTP metadata, byte size and SHA-256. Raw files remain transient under RAW-001.

## Future file seal / 미래 파일 봉인

No September 2026 or later EIA-860M workbook body may be opened in F01.

A future descendant may classify retirement only from an official EIA-860M data month **strictly later than August 2026**, first opened after N01 is prospectively frozen.

## Sheet firewall / sheet 방화벽

For each frozen monthly workbook, F01 may:

- enumerate workbook sheet names;
- inspect header rows needed to identify the allowed sheets;
- read row bodies only from:
  - the source-native **Operable** / source-equivalent currently-operable generator sheet;
  - the source-native **Retired** generator sheet.

F01 must not read row bodies from:
- Planned;
- Proposed;
- Planned Additions;
- planned-retirement or planned-operation tables;
- canceled/proposed-only sheets used as future-retirement precursors.

Sheet/header discovery may normalize harmless punctuation, whitespace and capitalization only.

## Frozen generator identity / 고정 식별자

Primary generator identity is exact pair:

> **(Plant ID, Generator ID)**

Allowed representation normalization:

### Plant ID
- numeric integer or integer-equivalent cell → base-10 positive integer string;
- text containing only decimal digits → canonical positive integer string after removing only mathematically redundant leading zeros;
- no nonnumeric reconstruction.

### Generator ID
- convert source cell to text;
- trim leading/trailing ASCII/Unicode whitespace;
- otherwise preserve leading zeros, internal whitespace, punctuation and case exactly.

Prohibited:
- plant-name matching;
- utility/entity/owner matching;
- location/address/county/state repair;
- geospatial matching;
- Generator ID case folding, zero-padding, truncation or punctuation removal;
- Entity ID substitution for Plant ID;
- fuzzy/manual identity repair.

Generator ID is meaningful only within Plant ID.

## Frozen retirement semantics / 고정 은퇴 의미

Historical support may use the twelve frozen Retired sheets.

A future retirement prospect is defined only as:

> an N01-eligible exact (Plant ID, Generator ID) that was in the August-2026 operable cohort and later appears in an official post-August-2026 source-native Retired inventory with a parseable retirement month/year consistent with that transition.

F01 does not open such future membership.

Retirement is an administrative generator-status event. It is not automatically plant closure, financial distress, policy failure or reliability failure.

## EIA-923 boundary / EIA-923 경계

F01 may verify only:
- official EIA-923 page accessibility;
- documentation that EIA-923 contains monthly/annual generation and fuel data;
- documented data level (plant / prime mover / limited generator schedules where applicable).

F01 may not open any EIA-923 row body, construct a 860/923 join, or assert generator-level performance availability.

Any N01 using EIA-923 must separately preregister the exact permitted join level and aggregation rule before future retirement membership is opened.

## Anti-tautology firewall / 순환성 방화벽

No descendant predictive exposure may include:
- planned retirement date/month/year;
- planned-retirement status;
- announced retirement;
- cancellation/retirement intention;
- any field mechanically encoding a future retirement;
- post-cutoff retirement status.

F01 does not read planned/proposed row bodies at all.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical checkpoint is `CHK-20260930-PORTFOLIO-R48-TERMINAL-ID-CORRECTED`; last decision `DEC-278`; corrected selection `US-EIA-RET-001` |
| 2 | Issue binding | runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official source semantics | EIA-860M, EIA-860 and EIA-923 official pages are reachable; 860M page documents identifiable monthly files and comprehensive Retired tab semantics from March 2017 |
| 4 | Exact twelve-month source resolution | all twelve frozen month/year entries resolve from the official 860M index to official EIA XLSX links; no month substituted |
| 5 | Twelve-workbook integrity | all twelve resolved bodies are parseable XLSX workbooks; URL, HTTP metadata, bytes and SHA-256 are recorded |
| 6 | Allowed sheet inventory | every workbook exposes one identifiable Operable/source-equivalent sheet and one Retired sheet; planned/proposed row bodies opened = 0 |
| 7 | Required identity/date schema | allowed sheets expose Plant ID + Generator ID in every month; Retired sheet exposes retirement month + retirement year in every month |
| 8 | Exact identity support | ≥ **99.99%** of nonblank allowed-sheet rows have a valid exact Plant ID and nonblank exact Generator ID under the frozen rule |
| 9 | Within-month identity uniqueness | ≥ **99.99%** of allowed-sheet rows are unique on exact Plant ID + Generator ID within each month/sheet |
| 10 | Historical lineage | all **12/12** expected data months are fingerprinted, chronologically ordered, with distinct workbook SHA-256 values for at least **10/12** months |
| 11 | Latest operable support | August 2026 Operable sheet contains ≥ **20,000** distinct exact generator pairs |
| 12 | Identity continuity | ≥ **85.00%** of August-2026 operable pairs appear in Operable sheets in at least **6 of the 12** frozen months |
| 13 | Historical retired support | union of the twelve Retired sheets contains ≥ **3,000** distinct exact generator pairs |
| 14 | Retirement-date support | ≥ **98.00%** of distinct retired pairs have a parseable source-native retirement month (1–12) and retirement year (2002–2026) |
| 15 | Retirement-date stability | among retired pairs observed in ≥2 frozen workbooks, ≥ **99.50%** retain one identical retirement year-month |
| 16 | Latest lifecycle exclusivity | exact pair overlap between August-2026 Operable and August-2026 Retired is ≤ **0.10%** of August operable pairs |
| 17 | Future/source firewall | September-2026-or-later 860M body opened = false; future retirement membership = false; planned/proposed row bodies opened = 0; EIA-923 row bodies opened = 0; relationship/prediction/ranking/causal metric = false; identity repair = false |
| 18 | Reproducibility/cost | immutable evidence records index/source URLs, twelve resolved workbook fingerprints, sheet/header inventories, row/cardinality/continuity/retirement counts, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_EIA_RET_F01_EXACT_GENERATOR_FUTURE_RETIREMENT_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01.

Do not rescue a failure by:
- lowering any threshold;
- substituting months;
- opening post-August-2026 files;
- reading planned/proposed rows;
- changing generator identity;
- name/geographic/manual repair;
- introducing EIA-923 row data after observing a support failure.

Transport/parser/schema-representation corrections are allowed only when every scientific criterion remains unchanged and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-EIA-RET-N01`.

Before any post-August retirement membership is opened, N01 must freeze:
- one non-tautological baseline exposure family;
- August-2026 operable eligible cohort;
- comparator/stratification/matching design;
- handling of generator ID change, re-powering, reactivation and plant reconfiguration;
- minimum follow-up horizon and retirement support;
- any EIA-923 join/aggregation level;
- balance/statistical gates.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that generator age, technology, fuel, capacity, owner, utilization, generation or any other characteristic predicts or causes retirement. No investment, grid-reliability, policy, environmental, asset-quality or operator recommendation is authorized.

Incremental monetary cost must remain **0 USD**.
