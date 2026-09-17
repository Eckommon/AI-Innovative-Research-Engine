---
id: US-EIA-GEN-F01
type: outcome-blind-structural-feasibility
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R36
parent_selection: SELECT_US_EIA_GEN_001_GENERATOR_COMMISSIONING_SLIPPAGE_F01
future_outcome_rows_opened: false
incremental_monetary_cost_usd: 0
---

# US-EIA-GEN-F01 — co-located solar+storage longitudinal design feasibility

## Mission / 목적

Determine, **without opening any future generator outcome row**, whether the official EIA-860M archive supports a deterministic longitudinal design for a narrower infrastructure-bottleneck question:

> Among planned solar photovoltaic generators, is there enough source-native support to later compare generators at a **co-located solar+storage plant configuration** against otherwise standalone-solar plant configurations with respect to subsequent commissioning slippage?

F01 is structural only. It does not estimate slippage, compare technologies, rank plants/developers, or claim that co-location causes delay.

## Terminology boundary / 용어 경계

`co-located solar+storage` means only:

- the same exact EIA `Plant ID` in the frozen exposure snapshot contains at least one planned solar-photovoltaic generator and at least one planned battery-storage generator.

It does **not** mean EIA has certified that the units are technically integrated, share an interconnection request, share a developer, or constitute one formal hybrid project. No such inference is permitted.

## Frozen official sources / 고정 공식 소스

### Exposure snapshot — row access authorized

Official January 2024 EIA-860M workbook:

`https://www.eia.gov/electricity/data/eia860m/archive/xls/january_generator2024.xlsx`

Only the `Planned` generator table (or source-equivalent planned-generator sheet if capitalization differs) may be read at row level.

Authorized exposure fields are limited to the source-equivalent forms of:

- `Plant ID`
- `Generator ID`
- `Plant State`
- `Technology`
- `Energy Source Code`
- `Prime Mover Code`
- `Nameplate Capacity (MW)`
- `Status`
- `Planned Operation Month`
- `Planned Operation Year`

The runner may use sheet/header discovery to resolve harmless punctuation/spacing changes, but may not substitute names, addresses or coordinates for generator identity.

### Reserved future source — header/schema access only

Official December 2025 EIA-860M workbook:

`https://www.eia.gov/electricity/data/eia860m/archive/xls/december_generator2025.xlsx`

F01 may verify only:

- file accessibility and source fingerprint;
- workbook sheet names;
- the header row / column names needed by a later outcome stage.

F01 must **not iterate, inspect, sample, count or classify any December-2025 data row**. Future generator membership, operating/retired/canceled status, actual operation dates, schedule changes and generator-specific outcome values remain unopened.

## Frozen exposure cohort / 고정 노출 코호트

From January 2024 `Planned` rows only:

1. normalize `Plant ID` to an integer-like decimal string only when lossless;
2. normalize `Generator ID` by Unicode-safe trim and uppercase only;
3. require nonblank exact `(Plant ID, Generator ID)`;
4. restrict focal units to rows whose planned operation year is **2024 or 2025**;
5. identify solar photovoltaic generators by exact normalized `Technology = SOLAR PHOTOVOLTAIC`;
6. identify battery-storage generators by exact normalized `Technology = BATTERIES`;
7. define a focal solar generator as **COLOCATED** iff its exact Plant ID also has >=1 planned `BATTERIES` row in the same January-2024 Planned snapshot;
8. define a focal solar generator as **STANDALONE** iff its exact Plant ID has no planned `BATTERIES` row in that same snapshot.

Rows with conflicting duplicate values for the same exact `(Plant ID, Generator ID)` on any frozen exposure field are ambiguous and excluded fail-closed. Exact duplicate rows with identical frozen fields may be deduplicated.

No plant/generator may be rescued by plant name, utility name, county, address, latitude/longitude, fuzzy matching or manual judgment.

## Frozen structural diagnostics / 고정 구조 진단

F01 may compute only exposure-snapshot and schema diagnostics:

- number of valid planned rows;
- distinct exact generator keys;
- number of focal 2024–2025 solar generator keys;
- COLOCATED and STANDALONE focal solar counts;
- distinct COLOCATED Plant IDs;
- state coverage by exposure class;
- exact-key duplicate/conflict rates;
- planned-operation month/year completeness;
- positive nameplate-capacity completeness;
- within-Plant-ID state consistency;
- simple exposure-only covariate support counts by state, planned-operation year and baseline status;
- source SHA-256 fingerprints and deterministic exposure-manifest SHA-256.

The exposure manifest may contain only source-native key and exposure/baseline fields. It must contain **no future outcome membership or labels**.

## Frozen 18 requirements / 고정 18개 게이트

All 18 must pass for F01 PASS:

1. January-2024 official EIA-860M workbook is readable and fingerprinted.
2. January-2024 planned-generator sheet is located deterministically.
3. All frozen exposure identity/technology/timing/capacity/status fields are present by source-equivalent normalized header.
4. December-2025 official workbook is readable and fingerprinted **without opening any data row**.
5. December-2025 workbook exposes at header level the source-native plant/generator identity plus status/operation-timing fields needed for a later separately authorized outcome design.
6. No December-2025 data row, future membership, future status, actual operation date or schedule-change value is opened.
7. No name/address/geospatial/fuzzy/manual identity repair is used.
8. >= **1,000** distinct valid January-2024 planned solar generator keys with planned operation year 2024–2025 exist.
9. >= **50** focal solar generators are COLOCATED.
10. >= **300** focal solar generators are STANDALONE.
11. >= **25** distinct COLOCATED Plant IDs exist.
12. >= **15** states contain at least one COLOCATED focal solar generator and at least one STANDALONE focal solar generator.
13. >= **99%** of focal solar exact generator keys are unambiguous after exact-identical duplicate collapse.
14. >= **95%** of focal solar generators have valid planned-operation month and year.
15. >= **95%** of focal solar generators have positive finite nameplate capacity.
16. >= **99%** of focal solar generators belong to Plant IDs with internally consistent state values in the January-2024 exposure snapshot.
17. deterministic source fingerprints and exposure-manifest SHA-256 are persisted; no relationship/prediction/causality/ranking/slippage metric is computed.
18. incremental monetary cost is **0 USD**.

## Frozen disposition / 고정 판정

PASS only if all 18 requirements pass:

`PASS_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_READY`

Otherwise a valid scientific run terminates as:

`HOLD_US_EIA_GEN_F01_COLOCATED_SOLAR_STORAGE_LONGITUDINAL_DESIGN_NOT_READY`

A network/download/parser defect before valid scientific evaluation is an implementation failure, not scientific HOLD, and may be transparently corrected **without changing this contract**.

## Future-stage firewall / 후속단계 방화벽

Even if F01 passes, it authorizes only a separate **outcome-blind N01 design stage**. N01 must prospectively freeze matching/strata, exact follow-up snapshot(s), commissioning-slippage endpoint, temporal windows, balance requirements and statistical gates before any future generator row is opened.

F01 does not authorize:

- December-2025 row-level access;
- generator-level slippage calculation;
- technology/developer/plant ranking;
- project cancellation or success rates;
- causal claims;
- novelty claims.

## Rationale / 근거

EIA states that EIA-860M monthly data monitor current status of existing and proposed generating units and publishes a complete monthly archive; EIA also warns that monthly estimates are preliminary and can be corrected in later inventories. That version behavior makes exact snapshot fingerprinting and pre-outcome temporal freezing necessary. Existing EIA analyses already establish that generator/project delays occur, so this branch does not treat generic delay existence as novel.

Incremental monetary cost remains **0 USD**.
