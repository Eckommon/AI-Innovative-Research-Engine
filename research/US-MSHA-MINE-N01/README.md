---
id: US-MSHA-MINE-N01
type: outcome-blind-prospective-design
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-MSHA-MINE-F01
parent_decision: DEC-265
parent_gate: PASS_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_READY
future_serious_fatal_event_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-MSHA-MINE-N01 — prospective labor-intensity ramp-up → future serious/fatal event design

## Mission / 목적

Prospectively test whether mines with an unusually large **Q1→Q2 2026 increase in work-hours per average employee** have higher subsequent mine-level risk of a frozen serious/fatal MSHA accident event during 2026-09-30 through 2027-03-31 than outcome-blind matched mines without extreme ramp-up.

The exposure, eligible cohort, comparator, matching, event codes, future window, support gates and inferential rule are frozen **before Issue creation and before any future event membership is opened**.

This is a prospective association test, not a causal design.

## Frozen source baseline / 고정 source baseline

N01 uses exactly the three pre-outcome source bodies fingerprinted by F01 Attempt 02:

- `Mines.zip`
  - SHA-256 `3ddec0aebbc3fd4d70feeae0e507fd0ccee4e45516768b1a932e6e185f43fcd7`
- `MinesProdQuarterly.zip`
  - SHA-256 `4fa86737661eeee1aa9eea16b39614aba961a1920abf471761424b9613b1e960`
- `Accidents.zip`
  - SHA-256 `db5ac677f235e90f6214e6f26ee2b2994e32f01e18124f5165f05b5f741420b6`

Any baseline execution must either use bytes matching these fingerprints or stop. A later refreshed file may not replace the frozen baseline.

## Frozen identity / 고정 식별자

Exact seven-digit MSHA `MINE_ID`, unchanged from F01.

No zero-padding, operator/controller/name/address/fuzzy/geospatial/manual reconciliation is allowed.

## Frozen eligibility / 고정 대상

A mine is N01-eligible only if all are true:

1. exact qualified Mine ID exists in the frozen Mines source;
2. `CURRENT_MINE_STATUS` is exactly one of:
   - `Active`
   - `Intermittent`
   - `NonProducing`
   - `Temporarily Idled`;
3. frozen 2026 Q1 and 2026 Q2 employment/production data both contain at least one row for the Mine ID;
4. after aggregation across all subunits for each quarter:
   - `EMP_Q1 >= 3`
   - `EMP_Q2 >= 3`
   - `HOURS_Q1 >= 500`
   - `HOURS_Q2 >= 500`;
5. Q1 and Q2 labor intensity values are finite and positive;
6. `STATE`, `COAL_METAL_IND`, and `CURRENT_MINE_TYPE` are nonblank.

Quarter aggregation is fixed:

- `EMP_Q = sum(AVG_EMPLOYEE_CNT)` across all source rows for Mine ID / calendar quarter;
- `HOURS_Q = sum(HOURS_WORKED)` across all source rows for Mine ID / calendar quarter;
- `INTENSITY_Q = HOURS_Q / EMP_Q`.

No subunit is selected or dropped based on accident history or future outcome.

## Frozen exposure / 고정 노출

For each eligible mine:

`RAMP = ln(INTENSITY_Q2 / INTENSITY_Q1)`.

Exposure ranks are assigned **within exact `COAL_METAL_IND × CURRENT_MINE_TYPE` strata** having at least 40 eligible mines.

Within each qualifying stratum:
1. sort by `(RAMP ascending, MINE_ID ascending)`;
2. let `n` be stratum size;
3. `q25_index = ceil(0.25*n)`;
4. `q75_index = ceil(0.75*n)`;
5. rank positions are 1-based.

Groups:
- **RAMP_UP exposed:** rank position `> q75_index`;
- **MODERATE_CHANGE comparator pool:** `q25_index < rank position <= q75_index`;
- bottom-quarter mines and boundary ranks outside those exact rules are not used in the primary comparison.

No outcome information may alter ranks, quantile boundaries or group assignment.

## Frozen historical safety covariate / 과거 안전 이력

For matching only, define:

`PRIOR_SEVERE_12M = 1`

if the frozen pre-outcome accident file contains at least one serious/fatal row for the Mine ID with `ACCIDENT_DT` in:

- 2025-09-30 through 2026-09-29 inclusive,

using exactly the F01 serious/fatal codes:
- `DEGREE_INJURY_CD in {'01','02'}` OR
- `IMMED_NOTIFY_CD in {'01','02'}`.

Otherwise `PRIOR_SEVERE_12M = 0`.

This variable is a matching covariate only and is not the exposure.

## Frozen matching / 고정 매칭

Primary matching is 1:1 without replacement.

Exact matching strata:

`STATE × COAL_METAL_IND × CURRENT_MINE_TYPE × PRIOR_SEVERE_12M`.

Continuous baseline covariates:
1. `X1 = ln(1 + HOURS_Q1)`
2. `X2 = ln(1 + EMP_Q1)`
3. `X3 = ln(INTENSITY_Q1)`

Standardize X1–X3 using mean and sample standard deviation computed across the complete eligible cohort before exposure/comparator matching.

Greedy deterministic procedure:
1. process RAMP_UP mines in ascending Mine ID;
2. among unmatched MODERATE_CHANGE controls in the same exact stratum, retain only candidates with absolute standardized difference ≤ **0.50** on each X1–X3;
3. choose the candidate minimizing squared Euclidean distance across standardized X1–X3;
4. ties are broken by ascending comparator Mine ID;
5. if no comparator passes all three calipers, leave the exposed mine unmatched.

No propensity model, outcome variable, accident date after cutoff, operator name, mine name or manual choice is allowed.

## Frozen baseline-balance gate / baseline 균형

After matching, absolute standardized mean difference must be ≤ **0.10** for each X1, X2 and X3.

Categorical exact-match variables and PRIOR_SEVERE_12M are balanced by construction.

## Frozen future endpoint / 미래 endpoint

Primary endpoint is mine-level binary:

> at least one official MSHA accident/injury row with `ACCIDENT_DT` from **2026-09-30 through 2027-03-31 inclusive** satisfying:
> - `DEGREE_INJURY_CD in {'01','02'}` OR
> - `IMMED_NOTIFY_CD in {'01','02'}`.

A mine counts once regardless of multiple qualifying rows.

Future event classes remain source-native; narratives are not used to classify the primary endpoint.

Baseline eligibility is intention-to-observe. Later mine-status changes do not remove a mine from the primary matched cohort.

## Frozen competing/secondary handling / 경쟁 사건

- Future non-severe accident rows do not count as the primary event.
- Later abandonment, sealing, operator change or production cessation does not redefine the primary binary endpoint.
- No mine is re-matched after baseline.
- Any later status-based sensitivity analysis requires a separate pre-specified descendant and is not part of N01 primary adjudication.

## Frozen prospective support rule / 미래 사건 support

When the future window is finally adjudicated, primary inference is allowed only if the matched cohort contains:

- at least **40** mines with the primary event in total; and
- at least **10** event mines in each arm.

Otherwise disposition is `HOLD_US_MSHA_MINE_N01_LOW_FUTURE_EVENT_SUPPORT` and no directional relationship claim is promoted.

## Frozen statistical test / 통계 판정

Primary estimand: mine-level 6-month risk ratio and risk difference, RAMP_UP versus matched comparator.

Primary hypothesis is directional:

`H1: Risk_RAMP_UP > Risk_COMPARATOR`.

Promotion requires all of:
1. future-event support gate passes;
2. point estimate `RR > 1.0`;
3. two-sided 95% confidence interval for RR has lower bound `> 1.0`;
4. two-sided matched-pair McNemar exact p-value `< 0.05`;
5. baseline-balance gates remain satisfied.

If support passes but any condition 2–4 fails, the hypothesis is falsified/non-promoted. No alternate threshold, subgroup or endpoint may rescue it.

No causal effect is claimed even on promotion.

## Immutable 18-gate pre-outcome design contract / 불변 18개 사전 gate

The N01 baseline/design runner must pass **18/18** before the prospective cohort is considered locked:

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | F01 terminal PASS checkpoint and `DEC-265` are canonical |
| 2 | Issue binding | runner executes only after Issue creation bound to this exact contract |
| 3 | Baseline fingerprints | all three source bodies exactly match the frozen F01 SHA-256 values |
| 4 | Required schemas | Mines, Q1/Q2 employment and historical accident columns needed above are present |
| 5 | Eligible cohort support | ≥ **5,000** eligible mines before exposure ranking |
| 6 | Exposure-stratum support | ≥ **8** qualifying `COAL_METAL_IND × CURRENT_MINE_TYPE` strata with n≥40 |
| 7 | RAMP_UP support | ≥ **1,000** exposed mines |
| 8 | Comparator support | ≥ **2,000** MODERATE_CHANGE mines |
| 9 | Prior-severe construction | PRIOR_SEVERE_12M constructed only from pre-cutoff frozen rows/codes |
| 10 | Match support | ≥ **800** accepted 1:1 matched pairs |
| 11 | Exposed match coverage | accepted pairs cover ≥ **60.00%** of RAMP_UP mines |
| 12 | X1 balance | absolute SMD ≤ **0.10** |
| 13 | X2 balance | absolute SMD ≤ **0.10** |
| 14 | X3 balance | absolute SMD ≤ **0.10** |
| 15 | Historical event plausibility | among eligible mines, ≥ **40** distinct mines have a frozen serious/fatal event dated 2026-03-30 through 2026-09-29 in the frozen pre-outcome accident file |
| 16 | Future source seal | post-2026-09-29 future serious/fatal membership opened = **false** |
| 17 | Outcome firewall | no future relationship/RR/RD/p-value/ranking/causal metric computed; no prohibited identity repair |
| 18 | Reproducibility/cost | immutable evidence records cohort/ranks/matches/balance, source fingerprints, contract/runner hash and cost = **0 USD** |

## Pre-outcome disposition / 사전 판정

If 18/18 baseline/design gates pass:

`PASS_US_MSHA_MINE_N01_PROSPECTIVE_COHORT_LOCKED`

This means the cohort/exposure/matches are sealed for later adjudication; it does **not** mean the hypothesis is supported.

Any valid pre-outcome gate failure:

`HOLD_US_MSHA_MINE_N01_PROSPECTIVE_DESIGN_NOT_READY`

No post-observation relaxation or rematching is permitted.

## Future adjudication timing / 미래 판정 시점

Primary outcome adjudication may occur only after the official MSHA accident source has enough publication lag to cover **2027-03-31**. The adjudicator must verify source freshness before opening future event membership.

## Non-claims / 비주장

N01 baseline locking makes no safety prediction, mine ranking, enforcement recommendation, employment recommendation or causal claim.

Incremental monetary cost must remain **0 USD**.
