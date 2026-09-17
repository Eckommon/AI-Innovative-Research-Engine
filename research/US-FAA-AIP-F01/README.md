---
id: US-FAA-AIP-F01
type: outcome-blind-structural-feasibility-gate
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R35
parent_selection: SELECT_US_FAA_AIP_001_AIRFIELD_INFRASTRUCTURE_TO_BTS_DELAY_F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-FAA-AIP-F01 — outcome-blind FAA AIP ↔ BTS airport identity and temporal-support gate

## Mission / 목적

Determine, **before any grant-conditioned airport delay value is opened**, whether current official FAA and U.S. DOT/BTS public data support a deterministic, zero-cost airport/time join sufficient for a later preregistered design.

F01 is a structural feasibility gate only. It establishes neither an AIP→delay relationship nor infrastructure effectiveness.

## Frozen official source family / 고정 공식 소스군

### FAA AIP grant history

Primary exposure-side files are the official FAA AIP annual grant-history summaries for fiscal years **2021–2025** linked from:

- `https://www.faa.gov/airports/aip/grant_histories`

Recent annual files are official FAA downloadable workbooks. F01 may read only identity, fiscal-year and grant/project structural fields required to establish airport-year support. No BTS delay outcome value may be joined to these rows.

### FAA Location ID bridge

The only FAA identity bridge authorized is the official FAA Location IDs database:

- `https://www.fly.faa.gov/rmt/data_file/locid_db.csv`

The FAA source defines `LOC_ID` as the location identifier. F01 must restrict bridge candidates to airport-facility records and may use state/facility metadata only for deterministic validation/exclusion, not fuzzy repair.

### BTS airport master identity

The only BTS identity source authorized for F01 is the official TranStats **Aviation Support Tables — Master Coordinate** table, whose documented fields include:

- `AirportID` — DOT identifier for a unique airport across years;
- `AirportSeqID` — time-specific airport sequence identifier;
- `Airport` — three-character DOT airport code;
- `AirportStateCode`;
- `AirportStartDate`;
- `AirportEndDate`;
- `AirportIsClosed`;
- `AirportIsLatest`.

Official documentation:

- `https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FLL`
- `https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=N8vn6v10+f722146+gnoyr5&gnoyr_VQ=FLL`

### BTS delay-side schema boundary

F01 may inspect only **schema/airport-identity/time support** for the BTS on-time performance family. It may not read, aggregate or condition on delay values, cancellation values, diversion values, delay-cause fields, or any grant-conditioned outcome metric.

BTS documents `OriginAirportID` / `DestAirportID` as U.S. DOT airport identifiers and recommends AirportID for analysis across years.

## Frozen bounded exact identity route / 고정 exact identity 경로

F01 does **not** assume universal semantic equivalence between FAA `Loc ID` and BTS `Airport` merely because the strings look alike.

A record is admitted to the bounded bridge only when all conditions below hold:

1. AIP airport row has a nonblank normalized FAA `Loc ID` of exactly three ASCII alphanumeric characters;
2. the same code exists as an FAA Location IDs database `LOC_ID` record classified as an airport facility;
3. the same code exists in BTS Master Coordinate as `Airport`;
4. BTS rows for that code map to exactly **one longitudinal `AirportID`** over the F01 study-support horizon;
5. FAA/AIP state and BTS `AirportStateCode` agree exactly when both are nonblank;
6. no code maps to multiple competing FAA airport facilities or multiple BTS `AirportID`s;
7. no name, address, latitude/longitude, distance, fuzzy string, manual review or human-picked exception is used to repair an identity failure.

This route is a **bounded deterministic analysis bridge**, not a claim that FAA Loc ID and BTS Airport are universally interchangeable identifiers.

## Frozen structural time horizon / 고정 시간 범위

- FAA AIP grant-history support years: **FY 2021–2025**.
- BTS airport-master support must cover the corresponding airport identities through at least **calendar 2025**.
- F01 may inspect BTS on-time table availability/schema for **calendar 2021–2026** only to establish that a later exposure→future-outcome design could be temporally separated.
- No delay values may be opened in F01.

## Frozen exclusions / 고정 제외

Exclude without repair:

- AIP aggregate/state/program rows that do not represent an individual airport (`*GAB`, `*PAB`, state-block or analogous non-airport rows);
- blank or malformed Loc IDs;
- FAA LID records not classified as airport facilities;
- FAA/BTS state conflict;
- code→multiple `AirportID` ambiguity;
- airport identities not present in the BTS delay-side airport universe at schema/identity level;
- any row requiring name/address/geospatial/fuzzy/manual reconciliation.

## Frozen F01 requirements / 고정 게이트

All requirements must pass for F01 PASS.

1. **FAA source access:** at least four of FY 2021–2025 official AIP annual grant-history files are machine-readable at zero incremental monetary cost.
2. **AIP required structure:** readable files expose a deterministic airport identifier interpretable as FAA `Loc ID`, a fiscal/grant year, and airport/project structural content.
3. **FAA LID access:** official `locid_db.csv` is machine-readable and exposes `LOC_ID` plus facility classification/state metadata sufficient for airport-only validation.
4. **BTS Master Coordinate access:** official BTS Master Coordinate data are machine-readable or reproducibly downloadable at zero incremental cost.
5. **BTS required structure:** `AirportID`, `Airport`, `AirportStateCode`, and longitudinal/latest-status fields required by the bridge are present.
6. **Outcome firewall:** no BTS delay/cancellation/diversion/cause numeric outcome value is opened or aggregated.
7. **No repair:** no fuzzy/name/address/geospatial/manual identity repair is used.
8. **Exact bounded bridge count:** at least **300 distinct AIP Loc IDs** across FY 2021–2025 satisfy the frozen bounded exact bridge.
9. **Commercial-delay universe support:** at least **100 distinct bridged airports** are present in the BTS on-time airport identity universe without opening delay values.
10. **Multi-year AIP support:** at least **75 bridged airports** appear in AIP grant histories in at least two distinct fiscal years during FY 2021–2025.
11. **Recent AIP support:** at least **100 bridged airports** have at least one AIP grant-history row in FY 2023–2025.
12. **Longitudinal BTS identity stability:** at least **95%** of admitted bridge codes map to exactly one `AirportID` across the inspected Master Coordinate history; ambiguous codes are excluded before the rate is computed.
13. **State concordance:** at least **99%** of admitted nonblank-state bridge rows have exact FAA/AIP↔BTS state agreement; conflicts are excluded and counted.
14. **Future temporal support:** at least **80 bridged airports** have schema/identity presence sufficient for a potential grant-year plus at least one subsequent calendar-year on-time outcome window within 2021–2026.
15. **Determinism:** source fingerprints, normalization rules and admitted/excluded counts are persisted so a rerun can reproduce the same bridge from the same source bytes.
16. **Claim boundary:** relationship, prediction, causal effect, airport ranking, project effectiveness and grant-conditioned delay statistics remain unopened/uncomputed.
17. **Cost:** incremental monetary cost remains **0 USD**.

### PASS

`PASS_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_READY`

iff all 17 requirements pass.

### HOLD

`HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY`

if a valid scientific run fails any requirement.

Parser/network/transient download failures are implementation defects and must be corrected transparently without changing this contract. Once empirical support counts are observed, thresholds, identity rules and exclusions must not be loosened.

## Future-design boundary / 후속 설계 경계

A PASS authorizes only a separate outcome-blind `US-FAA-AIP-N01` design stage. N01 must prospectively freeze:

- eligible project/exposure definition;
- airport-level independence rule;
- grant timing/index date;
- comparison/matching rule;
- future BTS delay endpoint and window;
- materiality/statistical gate;

**before any grant-conditioned delay outcome is opened.**

A HOLD terminates this branch without fuzzy/manual/geographic rescue and returns to independent portfolio reselection.

## Cost boundary / 비용 경계

Only free official public sources and standard public-repository GitHub-hosted execution are authorized. Any paid API, paid data, larger/GPU runner or other incremental monetary cost requires explicit user approval first.