---
id: US-CMS-NPI-N01
type: outcome-blind-prospective-design
created: 2026-10-13
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-CMS-NPI-F01
parent_decision: DEC-315
baseline_full_sha256: 45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e
baseline_deactivation_sha256: fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1
future_update_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-N01 — multi-taxonomy vs single-taxonomy prospective cohort lock

## Mission / 목적

Before opening any NPPES weekly or later monthly update body, determine whether the frozen October 12, 2026 active Type-2 organization baseline can support a balanced, adequately scaled prospective comparison of:

- **EXPOSED:** active Type-2 organization NPI with **2 or more** nonblank taxonomy codes;
- **CONTROL:** active Type-2 organization NPI with **exactly 1** nonblank taxonomy code.

The future event remains source-native NPI deactivation only.

N01 evaluates cohort scale, matching/common support and event-opportunity support. It does **not** compute deactivation rates or compare outcomes between arms.

## Frozen baseline

Use exactly the F01 monthly V2 full replacement body:

`45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e`

and F01 monthly deactivation body:

`fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1`.

No later monthly or weekly row body may be opened in N01.

## Frozen eligible cohort

A baseline NPI is eligible only if all are true:

1. exact 10-digit NPI;
2. Entity Type Code = 2;
3. NPI Deactivation Date is blank;
4. NPI Reactivation Date is blank;
5. exactly one nonblank taxonomy entry has `Healthcare Provider Primary Taxonomy Switch == 'Y'`;
6. corresponding primary taxonomy code is nonblank;
7. primary practice-location state is exactly two ASCII letters;
8. Provider Enumeration Date is parseable and no later than 2026-10-12;
9. taxonomy count is ≥1.

The blank-reactivation requirement prospectively excludes prior churn/reversal cases from the initial study.

## Frozen exposure

`MULTI_TAXONOMY = taxonomy_count >= 2`

Control:

`SINGLE_TAXONOMY = taxonomy_count == 1`

No deactivation, reactivation, last-update recency, prior registry event or any outcome-derived field may be used to define exposure.

## Frozen structural covariates

For matching/support only:

- primary taxonomy family = first **4 characters** of the source-native primary taxonomy code;
- primary practice-location state;
- enumeration-age band in completed 5-year bins as of 2026-10-12;
- Is Organization Subpart normalized to `Y / N / BLANK`;
- total practice locations = 1 primary location + number of exact-NPI rows in the official Practice Location reference file;
- practice-location bin = `1`, `2`, `3+`.

## Frozen matching algorithm

1. Construct exact stratum:
   `(state, primary_taxonomy_prefix4, age_5y_band, subpart_status, practice_location_bin)`.
2. Keep only strata containing at least one exposed and one control.
3. Within each stratum, sort exposed and controls separately by:
   `SHA256("CMS-NPI-N01|" + NPI)`.
4. Pair one-to-one in deterministic sorted order up to the smaller arm count.
5. No comparator reuse.
6. No cross-stratum matching.
7. No caliper rescue, propensity model or post-hoc stratum relaxation.

## Frozen balance metrics

After matching, compute arm-level standardized mean differences for:

- exact enumeration age in days;
- exact total practice-location count.

Absolute SMD must be ≤ **0.10** for both.

## Frozen observation-opportunity support

The baseline monthly deactivation workbook may be used only to count **global recent historical event support**, never arm-specific outcomes.

Recent analog window:
- deactivation date from **2024-10-13 through 2026-10-12 inclusive**.

No baseline deactivation NPI may be joined back to exposed/control arms in N01.

## Future event window

If N01 passes, E01 may open only the first official weekly/monthly NPPES update body published **after the N01 terminal commit** and with a covered period ending after 2026-10-12.

Primary future event:
- first source-native NPI deactivation for a locked cohort NPI.

A later reactivation does not erase the deactivation event but must be reported separately as a reversal/competing state.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | F01 terminal PASS checkpoint and `DEC-315` |
| 2 | Issue binding | runner executes only after new Issue binds this exact contract |
| 3 | Baseline identity | downloaded full/deactivation bodies exactly match both frozen F01 SHA-256s |
| 4 | Schema reproducibility | required main/practice/deactivation concepts resolve exactly as in F01 |
| 5 | Eligible cohort scale | eligible active Type-2 NPIs ≥ **1,000,000** |
| 6 | Exposed support | multi-taxonomy eligible ≥ **250,000** |
| 7 | Control support | single-taxonomy eligible ≥ **700,000** |
| 8 | Exact common strata | ≥ **1,000** strata contain both arms |
| 9 | Practice-location construction | every eligible NPI receives deterministic total-location count ≥1; secondary rows use exact NPI only |
| 10 | Exposed common-support coverage | ≥ **60.00%** of exposed eligibles are in common strata |
| 11 | Matched-pair scale | ≥ **200,000** deterministic pairs |
| 12 | Matching integrity | zero duplicate NPI within an arm, zero comparator reuse, zero cross-stratum pairs |
| 13 | Enumeration-age balance | matched absolute SMD ≤ **0.10** |
| 14 | Practice-location balance | matched absolute SMD ≤ **0.10** |
| 15 | Recent analog event support | ≥ **20,000** distinct exact deactivated NPIs dated 2024-10-13..2026-10-12; counted globally only |
| 16 | Reactivation policy | eligible cohort contains **0** NPIs with nonblank baseline reactivation date |
| 17 | Outcome/future firewall | no weekly/later monthly row body, no arm-specific deactivation lookup, no relationship/prediction/ranking/causal metric, no identity repair |
| 18 | Reproducibility/cost | immutable evidence records baseline SHAs, cohort/arm/strata/pair counts, SMDs, recent global event count, contract/runner SHA and cost=0 |

## Terminal rule

PASS:

`PASS_US_CMS_NPI_N01_MULTI_TAXONOMY_MATCHED_COHORT_READY`

Any valid failure:

`HOLD_US_CMS_NPI_N01_MULTI_TAXONOMY_MATCHED_COHORT_NOT_READY`

No threshold, exposure, eligibility, matching stratum or future window may be changed after observation inside this N01.

## PASS consequence

PASS authorizes one separately frozen E01 only after the N01 terminal commit. E01 may then open the first qualifying future update and test the locked cohort.

N01 itself authorizes no provider-risk ranking or causal claim.

Incremental monetary cost must remain **0 USD**.
