---
id: US-WW-E01-RESULT
type: preregistered-relationship-test
created: 2026-09-13
issue: 119
gate: NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP
claim_boundary: non-causal-predictive
incremental_monetary_cost_usd: 0
---

# US-WW-E01 Result

**`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**

The frozen structural gate passed, so the authorized second pass opened the 2023–2025 binary future incident outcome and fit the single preregistered state-fixed-effect HC1 linear-probability model. The positive hypothesis did **not** pass.

## Structural gate

- all-linked-permit exact facilities: **14,560**
- documented-need facilities: **7,616**
- baseline-clean documented-need facilities: **3,785**
- eligible before state-overlap restriction: **3,761**
- both-group state/territory codes: **46**
- primary model exposed: **2,503**
- primary model comparator: **1,222**
- design rank: **48 / 48**

All preregistered structural thresholds passed before future outcome membership/count/rate was derived.

## Primary preregistered result

Model: `Y ~ intercept + exposed + compliance-reason leakage stratum + state FE`, OLS LPM with HC1 covariance.

- `n = 3,725`
- exposure coefficient `beta = -0.0221841` = **−2.218 percentage points**
- HC1 SE = **0.0164862**
- 95% CI = **[−0.0544964, +0.0101283]**
- two-sided normal p = **0.178427**
- frozen positive materiality floor = **+0.03**

Because `beta` is negative and the confidence interval includes zero, the frozen gate resolves to **`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**.

## Pre-specified non-rescuing diagnostics

Raw facility outcome:
- exposed: **735 / 2,503 = 29.3648%**
- comparator: **415 / 1,222 = 33.9607%**
- unadjusted risk difference: **−4.5960pp**
- risk ratio: **0.8647**

Leakage strata:
- `L=0`: 447 exposed vs 288 comparator; risks 32.6622% vs 35.0694%, RD −2.4073pp;
- `L=1`: 2,056 exposed vs 934 comparator; risks 28.6479% vs 33.6188%, RD −4.9710pp.

The preregistered `L=0` sensitivity model was **not run** because the stratum did not retain >=500 facilities in each exposure group. This cannot rescue or change the primary disposition.

Nonexclusive future-event table contribution counts among model facilities:
- PS: 400 facilities
- CS: 131 facilities
- SE: 782 facilities

## Interpretation boundary

This result does **not** show that wet-weather/conveyance needs protect facilities, nor does it establish any causal effect. It only fails to support the preregistered positive predictive association under this specific public-data design. The point estimate is negative, but the interval spans zero.

The structural diagnostic found **578 official NPDES permit IDs linked to more than one CWNS facility** in the wider exact-linked universe. This was not a preregistered exclusion or covariance rule and therefore cannot be used post hoc to alter the primary result. It is recorded as a limitation for any future independent research question.

Material adjacent prior work remains acknowledged; no novelty is claimed for CWNS×NPDES linkage itself.

## Exact next action

Treat E01 as terminal under its frozen hypothesis. Do not rerun with a different need-category subset, date rule, threshold, model, or exclusion to seek a positive result. Return to Stage 0 and compare independent alternatives rather than rescuing this branch.

Incremental monetary cost: **0 USD**.
