---
id: US-EPA-RCRA-F01
type: outcome-blind-structural-feasibility
created: 2026-10-08
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R55
parent_decision: DEC-307
selected_candidate: US-EPA-RCRA-001
future_refresh_opened: false
future_evaluation_violation_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-EPA-RCRA-F01 — exact handler-key evaluation-conditioned violation structural gate

## Mission / 목적

Before opening any event membership from a later RCRAInfo weekly refresh, determine whether EPA ECHO's direct national RCRAInfo download supports a deterministic handler-level prospective design in which a future **evaluation opportunity** is the observation opportunity and source-native `FOUND_VIOLATION = Y` is the primary event.

F01 is structural only. It does not test whether generator/TSDF/transporter role, NAICS or any other handler attribute predicts a future violation.

## Frozen official source anchors / 공식 source

- ECHO downloads page: `https://echo.epa.gov/tools/data-downloads`
- RCRAInfo dictionary: `https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary`
- official current RCRAInfo ZIP: `https://echo.epa.gov/files/echodownloads/rcra_downloads.zip`

EPA documents six CSV files:
- `RCRA_FACILITIES.csv`
- `RCRA_ENFORCEMENTS.csv`
- `RCRA_EVALUATIONS.csv`
- `RCRA_VIOLATIONS.csv`
- `RCRA_NAICS.csv`
- `RCRA_VIOSNC_HISTORY.csv`

All six carry `ID_NUMBER` and `ACTIVITY_LOCATION` as documented key fields.

## Frozen baseline / baseline 고정

After Issue binding, Attempt 01 may download the official `rcra_downloads.zip` exactly once.

That exact body becomes the historical F01 baseline and must be fingerprinted by requested/final URL, HTTP metadata, byte size, SHA-256, ZIP member inventory, CSV schemas, row/cardinality counts, `YRMONTH` lineage summary and evaluation date/event support.

All rows in this exact body are **historical structural/support evidence only**. The raw ZIP is transient under RAW-001 and must not be committed. No later RCRAInfo weekly ZIP body may be opened in F01.

## Frozen handler identity / 고정 식별자

Primary entity identity is exact source-native composite:

**`ID_NUMBER + ACTIVITY_LOCATION`**

Allowed normalization: text conversion, ASCII trim and uppercase.

For `ID_NUMBER`, accept only 4–12 characters and require the first two characters to be uppercase alphabetic letters. `NN` is explicitly allowed for Navajo Nation handlers.

`ACTIVITY_LOCATION` must be an exact two-letter uppercase source value when nonblank.

Prohibited: facility-name matching; street/city/ZIP/geospatial repair; FRS substitution; inserting/deleting/padding ID characters; manual identity repair.

## Frozen schema-alias rule / schema alias 고정

The EPA help page itself contains two documented spellings for the same evaluation concepts:

- `EVALUATION_IDENTIFIER` / structure-table typo `EVALUATION_IDENTIFER`
- `FOUND_VIOLATION` / structure-table typo `FOUND_VOLATION`

F01 may accept either **only as the source-native header for that same EPA-documented concept**. The actual CSV header must be recorded exactly. No other alias expansion is permitted without a separately demonstrated implementation defect.

## Frozen event semantics / event 의미

Primary future event prospect:

> At a prospectively eligible future RCRA evaluation opportunity, the evaluation row records source-native `FOUND_VIOLATION = Y`.

Observation opportunity is one source-native evaluation action identified by handler key plus evaluation identifier/type/date as available in the baseline schema.

Primary event: `Y` = violation identified as a result of evaluation.
Non-event values remain distinct: `N` = no violation; `U` = undetermined.
Event onset: source-native `EVALUATION_START_DATE`.

A later N01 must condition analysis on an actual future evaluation opportunity; an unevaluated handler may not be silently coded as a non-event.

## Anti-tautology firewall / 순환성 방화벽

A descendant predictive exposure may not include prior/current `FOUND_VIOLATION`, evaluation outcome/result, violation history/counts, `VIO_FLAG` / `SNC_FLAG`, enforcement history/actions, penalty amounts, return-to-compliance fields, or any variable mechanically derived from the future observation window.

Allowed exposure family is non-outcome handler/site structure only, prospectively selected later.

## Immutable 18-gate contract / 불변 18 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is `CHK-20261008-PORTFOLIO-R55-TERMINAL`, last decision `DEC-307`, RCRA selected |
| 2 | Issue binding | runner executes only after a new Issue binds this exact pre-Issue contract commit |
| 3 | Official documentation access | ECHO downloads page and RCRAInfo dictionary return valid official bodies |
| 4 | Baseline ZIP access | official `rcra_downloads.zip` is parseable, **>=50 MB**, EPA/ECHO-hosted, SHA-256 recorded |
| 5 | Required table inventory | all six documented CSV members are present |
| 6 | Facility schema | Facility exposes `ID_NUMBER`, `ACTIVITY_LOCATION`, `FED_WASTE_GENERATOR`, `TRANSPORTER`, `ACTIVE_SITE`, `OPERATING_TSDF` |
| 7 | Exact handler-key syntax | >= **99.00%** of nonblank Facility `ID_NUMBER` values satisfy frozen 4–12-char/two-letter-prefix rule and >=99.00% of nonblank `ACTIVITY_LOCATION` values are exactly two uppercase letters |
| 8 | Handler support | Facility contains >= **500,000** distinct exact `ID_NUMBER + ACTIVITY_LOCATION` keys |
| 9 | Active structural support | >= **100,000** distinct exact handler keys have at least one usable non-outcome role/status field among active/generator/TSDF/transporter concepts |
| 10 | Monthly history lineage | `RCRA_VIOSNC_HISTORY.csv` contains >= **36** distinct valid `YRMONTH` values in `YYYYMM` form |
| 11 | History identity coverage | >= **99.00%** of distinct history composite keys exact-match a Facility composite key without repair |
| 12 | Evaluation schema | Evaluations exposes handler keys plus EPA-documented evaluation identifier, type, start date and found-violation concepts under the frozen alias rule |
| 13 | Evaluation support | >= **100,000** distinct source-native historical evaluation opportunities are present |
| 14 | Event semantic support | >= **99.00%** of nonblank found-violation values are only `Y`, `N`, or `U`, and >= **20,000** distinct historical evaluation opportunities have `Y` |
| 15 | Evaluation-date support | >= **99.00%** of distinct eligible evaluation opportunities have parseable nonblank `EVALUATION_START_DATE` |
| 16 | Evaluation identity coverage | >= **99.00%** of distinct evaluation composite handler keys exact-match a Facility composite key without repair |
| 17 | Future/outcome firewall | later RCRAInfo refresh opened=false; future evaluation membership=false; relationship/prediction/ranking/causal metric=false; prohibited compliance exposure=false; identity repair=false |
| 18 | Reproducibility/cost | immutable evidence records URLs/HTTP metadata, ZIP SHA/member inventory, exact schemas, row/cardinality/month/event counts, contract SHA, runner SHA and `incremental_monetary_cost_usd=0` |

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_READY`

Any valid empirical frozen-gate failure:

`HOLD_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. Do not lower thresholds, broaden identity, add fuzzy/geographic repair, replace the event with violation/enforcement history, or open a later refresh after observation.

Transport/parser defects may be corrected only when independently demonstrated and without changing scientific criteria.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-EPA-RCRA-N01`.

N01 must freeze before any later weekly refresh is opened: one non-tautological structural exposure, eligible handler cohort, exact identity rule, qualifying future evaluation types/opportunities, comparator/matching/stratification, state/activity-location and handler-role controls, common-support and balance gates, future weekly-refresh window, and event-support/statistical gates.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that handler role, generator class, TSDF status, transporter status, NAICS or any other structural characteristic predicts or causes a later violation.

Incremental monetary cost must remain **0 USD**.
