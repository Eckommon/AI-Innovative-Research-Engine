---
id: US-BRIDGE-F01
issue: 127
state: AUTHORIZED_OUTCOME_BLIND_FEASIBILITY
created: 2026-09-13
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-F01 — Outcome-blind bridge × county disaster × inspection-condition feasibility

## Objective
Prove a reproducible zero-cost bridge identity / county hazard / inspection-time bridge-condition route **without opening bridge condition-rating values**. F01 is a feasibility gate only, not an effect test.

## Frozen sources
1. FHWA National Bridge Inventory annual Coding-Guide-format archives, **2015–2025 inclusive**.
2. FEMA OpenFEMA `DisasterDeclarationsSummaries` v2.
3. FHWA Coding Guide, data checks, and SNBI crosswalk for field semantics.

The 2015–2025 window is frozen to remain entirely inside the legacy Coding Guide format. 2026 SNBI outcomes must not be substituted into F01.

## Frozen bridge identity
- normalized two-digit `STATE_CODE_001`;
- trimmed `STRUCTURE_NUMBER_008`;
- canonical bridge key `(state_fips, structure_number)`;
- county key `state_fips + zero-padded COUNTY_CODE_003`.

Duplicate canonical bridge keys within a state-year fail closed. No fuzzy bridge, road, place or coordinate repair.

## Frozen inspection / condition identity
F01 may inspect headers, blank/nonblank support, and parse inspection dates, but must not parse, convert, summarize, rank, persist or compare condition-rating values.

Required legacy fields:
- `DATE_OF_INSPECT_090`
- `DECK_COND_058`
- `SUPERSTRUCTURE_COND_059`
- `SUBSTRUCTURE_COND_060`
- `CULVERT_COND_062`

Actual inspection date, not archive year, controls future temporal identity. Repeated annual records carrying the same inspection date are not independent inspections.

## Frozen FEMA window
- `incidentBeginDate`: 2015-01-01 through 2024-12-31 inclusive.
- exact county key: `fipsStateCode + fipsCountyCode`.
- exclude county code `000`.
- physical candidate types: Coastal Storm; Dam/Levee Break; Earthquake; Fire; Flood; Hurricane; Mud/Landslide; Severe Ice Storm; Severe Storm; Snowstorm; Straight-Line Winds; Tornado; Tropical Storm; Typhoon; Volcanic Eruption; Winter Storm.

F01 may count disaster identities and geography overlap only. No disaster-linked condition value/rate/change/association.

## Frozen PASS requirements
1. All sources accessible at incremental cost 0 USD.
2. Every 2015–2025 annual NBI source exposes frozen bridge/county/inspection/condition identity fields or a documented deterministic equivalent; condition values remain unopened.
3. >=300,000 canonical bridge identities appear in >=6/11 annual archives.
4. >=250,000 repeated-support bridge identities expose >=2 distinct parseable inspection dates.
5. >=90% of repeated-support bridge identities have deterministic valid 5-digit county FIPS in every retained observation used for later pairing.
6. Repeated-support bridges span >=45 state/territory FIPS.
7. FEMA physical-hazard county/time identities overlap qualified NBI geography in >=30 state/territory FIPS and >=500 counties.
8. Condition-field header identity is available in all 11 archive years; condition values remain unopened.
9. No fuzzy/outcome-dependent repair or paid source.
10. Raw bytes transient under RAW-001; durable artifacts contain only hashes, schema/support counts, identity diagnostics and outcome-blind join metadata.

## Frozen dispositions
- `PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`
- `PARTIAL_US_BRIDGE_F01_PANEL_READY_INSPECTION_IDENTITY_PENDING`
- `HOLD_US_BRIDGE_F01_SOURCE_OR_IDENTITY_SUPPORT`

No threshold/source/window rescue after execution.

## If PASS
PASS means `PANEL_JOIN_READY` only. A later N01 must prospectively resolve disaster-index selection, repeated disasters, pre/post inspection selection and variable cadence, post-disaster inspection ascertainment, repair/reconstruction confounding, county-level exposure error, culvert/component comparability, baseline eligibility, outcome/materiality, comparator, covariance/state/time controls, static-hazard overlap, and non-causal claim boundaries **before any condition rating is opened for a relationship test**.

## Known overlap
BTS already publishes static natural-hazard exposure for NHS bridges by combining NBI with FEMA/USGS/NOAA/USDA, and NBI deterioration modeling with environmental covariates is established. Static mapping and generic deterioration prediction are not novelty claims.

Incremental monetary cost: **0 USD**.


## Terminal F01 result / F01 최종 결과

**`PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`** — see `RESULT.md`. Run `34791209726` is the corrected outcome-blind terminal F01 execution; Run `34790222911` is retained as a superseded implementation-nonconformity run. Bridge condition-rating values remained unopened.
