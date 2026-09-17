---
id: US-EPA-XMEDIA-N01
type: outcome-blind-matched-design-identifiability
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EPA-XMEDIA-F01
parent_gate: PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY
outcome_rows_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-N01 — outcome-blind matched RCRA monitoring-intensity design

## Purpose / 목적

Determine, **before any ICIS-NPDES effluent-violation row is opened**, whether the exact FRS-linked RCRAInfo↔NPDES facility universe can support one deterministic matched design comparing higher vs lower recent RCRA compliance-monitoring intensity, with a prospectively frozen later E01 endpoint.

N01 is a design-identifiability gate only. It may build and persist an exposure/matching manifest. It may not open, count, infer or condition on the future NPDES outcome.

## Frozen source boundary / 고정 소스 경계

N01 may read only these official zero-cost EPA structural sources:

1. `pipeline_rcra_downloads.zip` → `PIPELINE_RCRA_01_EVALUATIONS.csv`
2. `frs_downloads.zip` → `FRS_PROGRAM_LINKS.csv`
3. `npdes_downloads.zip` → `ICIS_FACILITIES.csv`, `ICIS_PERMITS.csv`

### RCRA fields authorized in N01

- `ISN_RCR_EVAL`
- `REGISTRY_ID`
- `SOURCE_ID`
- `EVAL_TYPE`
- `EVAL_IDENTIFIER`
- `EVAL_LEAD_AGENCY`
- `EVAL_ACTIVITY_LOCATION`
- `EVAL_DATE`

`NUM_OF_VIOLS`, `NUM_OF_EA`, `PIPELINE_FLAG`, RCRA violation/enforcement files and all RCRA outcome fields are forbidden.

### FRS fields authorized in N01

- `PGM_SYS_ACRNM`
- `PGM_SYS_ID`
- `REGISTRY_ID`

Only exact source-native identity is allowed.

### ICIS-NPDES Part 1 fields authorized in N01

From `ICIS_FACILITIES.csv`:

- `NPDES_ID`
- `FACILITY_UIN`
- `STATE_CODE`
- `FACILITY_TYPE_CODE`

From `ICIS_PERMITS.csv`:

- `EXTERNAL_PERMIT_NMBR`
- `VERSION_NMBR`
- `FACILITY_TYPE_INDICATOR`
- `PERMIT_TYPE_CODE`
- `MAJOR_MINOR_STATUS_FLAG`
- `ORIGINAL_ISSUE_DATE`
- `ISSUE_DATE`
- `EFFECTIVE_DATE`
- `EXPIRATION_DATE`
- `RETIREMENT_DATE`
- `TERMINATION_DATE`

`PERMIT_COMP_STATUS_FLAG`, `DMR_NON_RECEIPT_FLAG`, `RNC_TRACKING_FLAG`, current violation/compliance fields and all outcome-proximal Part 1 fields are forbidden.

### Hard outcome firewall

N01 must not open or query:

- ICIS-NPDES Part 2 / `NPDES_EFF_VIOLATIONS.csv`;
- any DMR measurement/value/limit/exceedance file or API;
- any `NPDES_*_VIOLATIONS.csv` table;
- QNCR compliance history;
- any RCRA violation/enforcement outcome table.

Required persisted booleans:

- `npdes_effluent_violation_rows_opened: false`
- `dmr_outcome_rows_opened: false`
- `rcra_violation_outcome_rows_opened: false`
- `future_outcome_membership_opened: false`
- `relationship_computed: false`
- `predictive_metric_computed: false`
- `causal_claim_made: false`

## Exact identity / 정확한 식별

Start from FRS `REGISTRY_ID` records having both `PGM_SYS_ACRNM = RCRAINFO` and `PGM_SYS_ACRNM = NPDES`.

A Registry ID is eligible only if:

1. it maps to **exactly one** non-conflicting RCRAInfo `PGM_SYS_ID`;
2. it maps to **exactly one** non-conflicting NPDES `PGM_SYS_ID`;
3. the exact RCRAInfo program ID is present as `SOURCE_ID` with the same `REGISTRY_ID` in RCRA evaluations;
4. the exact NPDES program ID is present as `NPDES_ID` with the same `FACILITY_UIN` in ICIS facilities;
5. no name/address/geospatial/fuzzy/manual/parent-company repair is used.

Any one-to-many, conflicting or blank exact identity is excluded fail-closed.

## Fixed temporal design / 고정 시간 설계

One facility appears at most once.

- baseline window: **2018-01-01 through 2020-12-31**
- exposure window: **2021-01-01 through 2023-12-31**
- frozen future E01 outcome window: **2024-01-01 through 2024-12-31**
- index date: **2023-12-31**

A facility must have at least **one valid RCRA evaluation in the baseline window**. This prevents the LOW group from being composed solely of facilities with no demonstrated pre-exposure RCRA monitoring history.

## RCRA structural exposure / RCRA 구조적 노출

For each eligible exact RCRA `SOURCE_ID`:

- `baseline_eval_count` = number of distinct nonblank `ISN_RCR_EVAL` rows with valid `EVAL_DATE` in 2018–2020;
- `exposure_eval_count` = number of distinct nonblank `ISN_RCR_EVAL` rows with valid `EVAL_DATE` in 2021–2023;
- `baseline_last_eval_date` = latest valid RCRA `EVAL_DATE` in 2018–2020.

Duplicate `ISN_RCR_EVAL` rows with conflicting structural identity/date are fail-closed and make that facility ineligible. No RCRA violation finding, enforcement action, linked-violation count or pipeline flag may influence exposure.

The exposure interpretation is strictly **recent RCRA compliance-monitoring intensity**, not RCRA noncompliance or environmental risk.

## NPDES structural eligibility / NPDES 구조 적격성

For the exact one-to-one NPDES ID:

1. `STATE_CODE` must be a nonblank two-character state/territory code;
2. at least one permit row must exist;
3. select only current permit version `VERSION_NMBR = 0` as documented by EPA;
4. if multiple version-0 rows disagree on any frozen matching field, exclude fail-closed;
5. `PERMIT_TYPE_CODE` must be `NPD` or `GPC`;
6. `MAJOR_MINOR_STATUS_FLAG` must be `M` or `N`;
7. `FACILITY_TYPE_INDICATOR` must be nonblank;
8. a valid effective anchor date is the first nonblank valid date in this order: `EFFECTIVE_DATE`, `ISSUE_DATE`, `ORIGINAL_ISSUE_DATE`;
9. the effective anchor must be on or before **2023-12-31**;
10. `RETIREMENT_DATE`, when valid/nonblank, must be after **2024-12-31**;
11. `TERMINATION_DATE`, when valid/nonblank, must be after **2024-12-31**.

`EXPIRATION_DATE` is recorded only as structural metadata and is **not** an exclusion criterion because administratively continued permits may remain operative after nominal expiration.

## Frozen strata and quartiles / 고정 층화·사분위

Define exact stratum:

`STATE_CODE × MAJOR_MINOR_STATUS_FLAG × PERMIT_TYPE_CODE × FACILITY_TYPE_INDICATOR`

A stratum is eligible only if it contains at least **16** eligible Registry IDs.

Within each eligible stratum:

1. sort ascending by `(exposure_eval_count, REGISTRY_ID)`;
2. let `k = floor(n / 4)`;
3. LOW = first `k` units;
4. HIGH = last `k` units;
5. require `min(HIGH exposure_eval_count) > max(LOW exposure_eval_count)`; otherwise drop the entire stratum;
6. middle 50% is excluded.

No cut-point may be changed after seeing counts, and no outcome information may affect stratum eligibility.

## Frozen deterministic matching / 고정 결정론적 매칭

Match HIGH to LOW **only within the exact stratum**, without replacement.

Process HIGH units in descending `(exposure_eval_count, REGISTRY_ID)` order. For each HIGH unit choose the unused LOW unit by, in order:

1. minimum absolute difference in `baseline_eval_count`;
2. minimum absolute difference in days from `baseline_last_eval_date` to `2020-12-31`;
3. minimum absolute difference in permit age at `2023-12-31` using the frozen effective anchor;
4. lexical LOW `REGISTRY_ID`.

Every Registry ID, RCRA SOURCE_ID and NPDES ID may appear at most once in the final pair manifest.

The persisted N01 manifest may contain only exact IDs, frozen structural covariates, exposure counts, dates, stratum and pair IDs. It must contain no future outcome membership/value.

## N01 PASS requirements / N01 PASS 요건

All must pass prospectively:

1. all four authorized structural tables are readable from the three official EPA ZIPs;
2. all frozen required fields are present;
3. no forbidden outcome file/table is opened;
4. exact one-to-one FRS/RCRA/NPDES identity only; identity repair = false;
5. at least **1,000** Registry IDs remain after exact identity + baseline + NPDES structural eligibility;
6. at least **20** eligible strict-separation strata remain;
7. at least **250** matched HIGH–LOW pairs remain;
8. matched pairs span at least **20** distinct `STATE_CODE` values;
9. every pair has `HIGH exposure_eval_count > LOW exposure_eval_count`;
10. no Registry ID, RCRA SOURCE_ID or NPDES ID appears in more than one pair;
11. at least **75%** of pairs have baseline-evaluation-count ratio `HIGH/LOW` within `[1/3, 3]`;
12. at least **75%** of pairs have absolute permit-age difference <= **10 years** at the index date;
13. deterministic canonical pair-manifest SHA-256 is persisted;
14. `npdes_effluent_violation_rows_opened = false`;
15. `dmr_outcome_rows_opened = false` and `future_outcome_membership_opened = false`;
16. `rcra_violation_outcome_rows_opened = false`;
17. relationship/prediction/causality all remain false;
18. incremental monetary cost = **0 USD**.

### N01 PASS

`PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE`

### N01 HOLD

`HOLD_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_NOT_IDENTIFIABLE`

A scientific HOLD is terminal for this exact design. Thresholds, identity rules, exposure windows, strata or matching rules must not be relaxed after observing N01 counts.

Network/download/parser/implementation defects are not scientific HOLD and may be corrected transparently without changing this contract.

## Prospectively frozen future E01 / 향후 E01 사전고정

This section does **not** authorize outcome access. It freezes what a later E01 must do if and only if N01 passes and a separate E01 Issue/authorization is created.

### Outcome source

Only official ICIS-NPDES Part 2 `NPDES_EFF_VIOLATIONS.csv` may supply the primary E01 outcome.

Authorized primary-outcome fields only:

- `NPDES_ID`
- `NPDES_VIOLATION_ID`
- `VIOLATION_CODE`
- `MONITORING_PERIOD_END_DATE`

No DMR value, limit magnitude, pollutant, exceedance percentage, enforcement outcome or narrative is needed for the primary endpoint.

### Primary outcome

For each frozen N01 NPDES ID:

- retain only rows with `VIOLATION_CODE = E90`;
- retain only rows whose valid `MONITORING_PERIOD_END_DATE` falls in calendar **2024**;
- deduplicate by exact nonblank `NPDES_VIOLATION_ID`;
- `Y = 1` iff at least one such unique E90 violation exists;
- `Y = 0` iff none exists.

EPA documents `E90` as an effluent violation where a reported DMR value exceeds a maximum/average limit or is below a minimum limit. D80/D90 reporting non-receipt violations are excluded from the primary endpoint.

### Primary paired analysis

For the frozen matched pairs only:

- `risk_HIGH = mean(Y_HIGH)`
- `risk_LOW = mean(Y_LOW)`
- `RD = risk_HIGH - risk_LOW`
- `b = count(HIGH=1, LOW=0)`
- `c = count(HIGH=0, LOW=1)`
- exact two-sided McNemar/binomial test on `b+c` with `p=0.5`
- materiality floor: `RD >= +0.05`

### Frozen E01 gates

- `PASS_POSITIVE_MATERIAL_US_EPA_XMEDIA_E01_RELATIONSHIP` iff `RD >= +0.05`, exact two-sided `p < 0.05`, and `b > c`;
- `POSITIVE_BELOW_MATERIALITY_US_EPA_XMEDIA_E01_RELATIONSHIP` iff `0 < RD < +0.05`, exact two-sided `p < 0.05`, and `b > c`;
- `NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP` otherwise.

A negative estimate must not be reframed as a protective-effect claim. Any later result is observational/noncausal and must not be used as a facility risk ranking or enforcement-targeting score.

## Cost boundary / 비용 경계

Incremental monetary cost must remain **0 USD**. Any paid API/data/runner requirement requires explicit user approval before use.
