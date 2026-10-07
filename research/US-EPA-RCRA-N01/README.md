---
id: US-EPA-RCRA-N01
type: outcome-blind-prospective-design
created: 2026-10-08
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EPA-RCRA-F01
parent_decision: DEC-309
parent_evidence_commit: 4994dd3e0614d0c91e04b757d8e3dbe1fca6c335
baseline_sha256: ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5
future_refresh_opened: false
future_found_violation_membership_opened: false
found_violation_values_consumed_in_n01: 0
incremental_monetary_cost_usd: 0
---

# US-EPA-RCRA-N01 — multi-NAICS structural breadth prospective cohort lock

## Mission / 목적

Before opening any post-baseline RCRAInfo weekly refresh, determine whether the frozen October-2026 RCRAInfo baseline can support a balanced prospective comparison of handlers with broader versus narrower source-native industrial activity breadth.

Hypothesis to be tested later, not in N01:

> Among otherwise comparable historically evaluated RCRA handlers that receive a future qualifying evaluation, violation incidence may differ between handlers listing multiple valid NAICS codes and handlers listing exactly one valid NAICS code.

N01 computes no violation outcome and reads no `FOUND_VIOLATION` value.

## Frozen baseline source

N01 must use the same official `rcra_downloads.zip` body fingerprinted by F01:

- SHA-256: `ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5`
- last modified: 2026-10-04 13:45:03 GMT

Any re-downloaded body with a different SHA is source-version drift and cannot silently replace the frozen baseline.

Only Facility, NAICS and Evaluation row bodies needed for eligibility/matching may be consumed. Enforcement, Violations and VIO/SNC History rows are prohibited in N01.

## Frozen identity

Exact `ID_NUMBER + ACTIVITY_LOCATION`, unchanged from F01.

No name/address/geography/FRS/manual repair.

## Frozen baseline cutoff

Baseline cutoff date:

**2026-10-04**

Historical evaluation-opportunity covariates may use only `EVALUATION_START_DATE <= 2026-10-04`.

Five-year observation-propensity window:

**2021-10-05 through 2026-10-04 inclusive**.

No evaluation result/value may be read.

## Frozen eligibility

A handler is eligible only if all are true:

1. exact qualified handler key appears in frozen Facility;
2. `ACTIVE_SITE` is nonblank;
3. at least one source-native regulated role is active:
   - generator: `FED_WASTE_GENERATOR in {1,2,3}`;
   - transporter: `TRANSPORTER == Y`;
   - operating TSDF: `OPERATING_TSDF` is nonblank;
4. exact handler key has at least one valid six-digit numeric NAICS code in frozen NAICS;
5. exact handler key has at least one historical evaluation with parseable date in the five-year propensity window;
6. `ACTIVITY_LOCATION` is exact two-letter code;
7. generator class, transporter flag, operating-TSDF binary and primary NAICS two-digit sector are constructible.

No compliance outcome is used for eligibility.

## Frozen NAICS exposure

For every eligible handler, collect distinct source-native six-digit numeric NAICS codes.

- `NAICS_COUNT` = number of distinct valid six-digit NAICS codes.
- `PRIMARY_NAICS2` = first two digits of the lexicographically smallest valid six-digit NAICS code.

Groups:

### Exposed — `MULTI_NAICS`
`NAICS_COUNT >= 2`

### Comparator — `SINGLE_NAICS`
`NAICS_COUNT == 1`

No threshold tuning after observation.

## Frozen historical evaluation-opportunity covariates

Using Evaluation rows only and never `FOUND_VIOLATION`:

- `EVAL_COUNT_5Y` = count of distinct source-native evaluation opportunities dated 2021-10-05..2026-10-04.
- `LAST_EVAL_DATE` = latest such evaluation date.
- `DAYS_SINCE_LAST_EVAL` = days from 2026-10-04 to LAST_EVAL_DATE.
- `X1 = ln(1 + EVAL_COUNT_5Y)`
- `X2 = ln(1 + DAYS_SINCE_LAST_EVAL)`

An evaluation opportunity is identified by exact handler key + evaluation identifier + evaluation type + evaluation date. Duplicate source rows of the same opportunity count once.

## Frozen exact matching strata

Match only within exact:

> `ACTIVITY_LOCATION × FED_WASTE_GENERATOR × TRANSPORTER × OPERATING_TSDF_BINARY × PRIMARY_NAICS2`

Generator class preserves source values `1/2/3/N/blank`, but eligibility requires at least one active role overall.

`OPERATING_TSDF_BINARY` = 1 when source-native OPERATING_TSDF is nonblank, otherwise 0.

## Frozen standardization and matching

Standardize X1 and X2 using mean and sample standard deviation across the complete eligible cohort before matching.

Primary matching is 1:1 without replacement.

Deterministic greedy procedure:
1. sort exposed handlers by exact stratum then handler key;
2. candidate controls must be unused and in the same exact stratum;
3. retain only candidates with absolute standardized difference <= **0.50** on X1 and <= **0.50** on X2;
4. choose candidate minimizing squared Euclidean distance across standardized X1/X2;
5. ties resolve by exact comparator handler key;
6. no candidate => exposed remains unmatched.

No propensity model, rematching, caliper widening, stratum merging or outcome-guided adjustment.

## Frozen balance

After matching:
- `|SMD(X1)| <= 0.10`
- `|SMD(X2)| <= 0.10`

Exact categorical variables must match pairwise by construction.

## Frozen historical opportunity plausibility

For support estimation only, and still without reading `FOUND_VIOLATION`:

analog recent opportunity window = **2025-10-05 through 2026-10-04 inclusive**.

Count matched handlers in each arm with at least one source-native evaluation opportunity in this window.

This is an observation-opportunity support check, not an outcome.

## Frozen future observation/event prospect

N01 opens no later refresh.

If N01 passes, a separately preregistered E01 protocol may later use:

future evaluation window:
**2026-10-05 through 2027-04-04 inclusive**.

A primary event may count only when:
1. handler is in the locked matched cohort;
2. a source-native evaluation row has `EVALUATION_START_DATE` in the future window;
3. event value is source-native `FOUND_VIOLATION = Y`.

`N` and `U` remain distinct. An unevaluated handler is not coded as `N`.

E01 must separately freeze the estimand and handling of handlers without future evaluation opportunity before opening any later refresh.

## Immutable 18-gate N01 contract

Exactly **18/18 PASS** is required.

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | F01 terminal checkpoint and `DEC-309` canonical |
| 2 | Issue binding | runner executes only after Issue binds this exact pre-Issue contract |
| 3 | Baseline fingerprint | re-downloaded RCRAInfo ZIP SHA exactly equals F01 baseline SHA |
| 4 | Required baseline schemas | Facility, NAICS and Evaluations contain all identity/exposure/matching concepts |
| 5 | Outcome-read firewall | `FOUND_VIOLATION` values consumed by N01 = **0**; Enforcement/Violations/VIO-SNC row bodies opened = **0** |
| 6 | Eligible cohort | >= **100,000** eligible handlers |
| 7 | Exposed support | `MULTI_NAICS >= 20,000` |
| 8 | Comparator support | `SINGLE_NAICS >= 40,000` |
| 9 | Common exact strata | >= **200** exact strata contain at least one exposed and one comparator |
| 10 | Matching integrity | 1:1 without replacement; exact-stratum mismatch=0; duplicate comparator use=0; all pairs satisfy both 0.50 calipers |
| 11 | Matched cohort | >= **20,000** matched pairs |
| 12 | Exposed match coverage | matched exposed / eligible exposed >= **40.00%** |
| 13 | X1 balance | `|SMD(X1)| <= 0.10` |
| 14 | X2 balance | `|SMD(X2)| <= 0.10` |
| 15 | Recent opportunity support | >= **5,000** matched handlers total and >= **1,500 in each arm** have >=1 evaluation in 2025-10-05..2026-10-04 |
| 16 | Future protocol seal | future window fixed to 2026-10-05..2027-04-04; later refresh opened=false; future membership opened=false |
| 17 | Outcome/identity firewall | relationship/prediction/ranking/causal metric=false; `FOUND_VIOLATION` consumed=0; prohibited compliance/enforcement exposure=false; identity repair=false |
| 18 | Reproducibility/cost | immutable evidence records eligibility/arm/strata/matches/balance/recent-opportunity counts, matched-manifest SHA, baseline/contract/runner SHA and cost=0 |

## Pre-outcome disposition

PASS:

`PASS_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_LOCKED`

Any valid failure:

`HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY`

A valid HOLD is terminal. No threshold, eligibility, exposure, exact strata, caliper or matching rule may be changed after observing N01 results.

## PASS consequence

PASS authorizes only a **separately preregistered, still outcome-sealed E01 protocol**. E01 must freeze the estimand, opportunity-conditioning rule, minimum evaluated-handler/event support, matched/cluster handling, statistical test and materiality criteria before any later RCRAInfo refresh is opened.

## Non-claims

N01 makes no claim that NAICS breadth predicts or causes violations. It makes no facility ranking or enforcement recommendation.

Incremental monetary cost must remain **0 USD**.
