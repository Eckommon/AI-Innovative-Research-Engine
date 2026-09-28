---
id: US-HUD-MF-N01
type: outcome-blind-design-identifiability
created: 2026-09-28
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-HUD-MF-F01
parent_decision: DEC-247
parent_result: PASS_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_READY
future_terminated_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-HUD-MF-N01 — matched recent-inspection-condition design before future adverse termination

## Mission / 목적

Determine, **without opening any post-2026-09-21 terminated-mortgage membership**, whether the frozen HUD historical baseline can support a deterministic matched design comparing relatively low versus relatively high **latest pre-cutoff physical inspection score** among active FHA multifamily projects.

N01 is a design-identifiability gate only. It does not test whether inspection condition predicts or causes a later FHA claim/adverse termination.

## Frozen source lineage / 고정 소스 계보

N01 must reconstruct only the exact historical source snapshots fingerprinted in parent F01 Attempt 03:

- active FHA multifamily mortgage workbook SHA-256:
  `72ae185f05fd94a5eda54dc55cd36332153c2307b88776fdc139d41a266e5c36`
- active multifamily property workbook SHA-256:
  `6c375b2b3491d7c7931ce58a1f715a8632a6ceb05b6c10a36ff8624b9c547a01`
- physical-inspection workbook SHA-256:
  `0ff6b86e54762df917058bca832088f343dc174e78332b002dc6fbfa400cd883`

The historical terminated workbook is **not required for N01 cohort construction**. N01 may rely on the already-durable F01 termination-schema evidence but may not open any post-baseline terminated workbook body.

If any required historical fingerprint no longer resolves from the official HUD selector, N01 may use the immutable F01-recorded fingerprint only if the exact bytes are already reproducibly recoverable from an official HUD URL in the runner. No later snapshot substitution is allowed.

## Frozen unit and identity / 고정 단위·식별자

Unit = one baseline active FHA multifamily project.

Primary identity is the exact qualified 8-digit FHA project ID under the unchanged F01 normalization:

1. source value to text without invented digits;
2. trim;
3. uppercase;
4. remove literal hyphen and ASCII spaces only;
5. accept only exact 8 decimal digits.

No zero-padding, address/name matching, fuzzy matching, geospatial repair or manual repair.

## Frozen baseline cohort / 고정 cohort

Start from all exact-qualified projects in the 2026-08-31 active mortgage snapshot.

A project is eligible only if:

1. it exact-links to one official property row usable under the deterministic property rule below;
2. that property has at least one physical inspection release date on or before **2026-09-21**;
3. one deterministic latest pre-cutoff inspection score can be assigned;
4. all required baseline matching covariates are nonmissing and parseable;
5. no source-level identity conflict remains after the frozen deduplication rules.

### Property deduplication

For each FHA project:

- prefer official property rows where the FHA number is marked primary when the source field is available;
- require exactly one resulting REMS Property ID;
- if multiple distinct REMS Property IDs remain, exclude the FHA project rather than select by address/name/geography.

### Inspection deduplication

For the selected REMS Property ID:

1. consider only inspection score/date pairs with release date <= 2026-09-21;
2. select the maximum release date;
3. if multiple scores exist on that same maximum date, retain the project only if all nonblank scores are identical;
4. otherwise exclude as ambiguous.

No score averaging, max/min rescue or manual adjudication.

## Frozen exposure / 고정 exposure

Exposure is the **latest pre-cutoff inspection score** only.

Among the fully eligible baseline cohort:

1. compute empirical 25th and 75th percentiles using the deterministic linear quantile definition implemented by NumPy-compatible `method="linear"`;
2. `LOW` = score <= Q25;
3. `HIGH` = score >= Q75;
4. scores strictly between Q25 and Q75 are not used in the primary matched design;
5. if Q25 >= Q75, N01 fails the exposure-separation gate;
6. quantile thresholds may not be changed after computation.

This relative-tail definition is outcome-blind and makes no claim that Q25 is an official HUD failure threshold.

## Frozen baseline matching covariates / 고정 매칭 변수

Only baseline source fields measured before future outcome membership are allowed:

- exact **property state**;
- exact **SOA category/sub-category** from the active mortgage file;
- `log1p(UNITS)`;
- `log1p(ORIGINAL MORTGAGE AMOUNT)`;
- **balance ratio** = AMORITIZED PRINCIPAL BALANCE / ORIGINAL MORTGAGE AMOUNT;
- **months to maturity** from 2026-09-21 to MATURITY DATE;
- **interest rate**.

Projects with nonpositive original mortgage amount, impossible balance ratio (<0 or >1.25), or unparseable required fields are excluded. These exclusion bounds are fixed before empirical N01 execution.

Inspection score itself may not appear among matching covariates.

## Frozen matching algorithm / 고정 매칭 알고리즘

1. exact stratum = `PROPERTY_STATE × SOA_CATEGORY/SUB_CATEGORY`;
2. standardize the five continuous matching covariates globally over LOW+HIGH candidates using mean and population SD;
3. within each exact stratum, perform deterministic 1:1 nearest-neighbor matching **without replacement**, pairing the smaller exposure side to the nearest opposite-side project by Euclidean distance over the five standardized covariates;
4. sort source projects by FHA project ID before greedy matching;
5. distance ties are resolved by the lexicographically smallest opposite-side FHA project ID;
6. no outcome, future termination membership, project name, lender/servicer name, address or geography beyond exact state may enter matching.

No post-run rematching, alternate propensity model, caliper tuning or variable deletion is permitted.

## Frozen balance/support requirements / 고정 support 기준

N01 PASS requires all of the following:

- eligible exact-linked baseline cohort: >= **7,000** projects;
- LOW candidates: >= **1,500**;
- HIGH candidates: >= **1,500**;
- matched pairs: >= **1,200**;
- matched pairs span >= **20** distinct states;
- matched pairs span >= **8** distinct SOA category/sub-category values;
- every continuous covariate absolute standardized mean difference after matching <= **0.15**;
- LOW/HIGH exact-state distributions are identical by construction within pairs;
- LOW/HIGH exact-SOA distributions are identical by construction within pairs;
- no FHA project appears in more than one pair.

If any gate fails, N01 is terminal HOLD for this exact design; no threshold or matching rescue is allowed.

## Frozen future adverse-event hierarchy / 고정 미래 event 규칙

N01 must not open future terminated membership. It freezes the later descendant adjudication only.

For a baseline FHA project, inspect future official HUD terminated-mortgage snapshots with as-of dates after 2026-09-21 and through **2027-03-31** only after a separate E01 authorization.

The first qualifying source row by `TERM_DATE` inside the frozen window controls.

Primary adverse event:

- source field `TYPE (Claim/Non Claim)`, normalized by trim/case only, equals exact **`Claim`**.

Competing routine/non-adverse termination:

- exact `TYPE (Claim/Non Claim) = Non Claim` and source-native termination description is exactly one of **Prepayment, Maturity, Voluntary**.

Ambiguous competing termination:

- all other terminated rows, including Assignment, Acquired, Conveyance, Cancellation, correction/supersession, transfer/reinsurance, missing type, and any claim/non-claim conflict.

Ambiguous cases may not be recoded after future rows are seen. A later E01 must prospectively state whether they are censored/excluded in the primary test and may report them only as a sensitivity population.

No generic substring search is allowed for future primary event classification.

## Frozen future snapshot cadence / 고정 cadence

A later E01 may use only official monthly HUD terminated-mortgage snapshots whose landing-page as-of date is > 2026-09-21 and <= 2027-03-31.

For repeated appearance of the same FHA project:

- retain the earliest source `TERM_DATE` within the window;
- if same project/date has conflicting Claim/Non Claim values, classify as ambiguous and exclude from primary resolved-event analysis;
- do not use workbook publication order to override source `TERM_DATE`.

## Frozen event-support and later primary-test gate / 고정 향후 gate

Before any effect estimate is accepted in a later E01, the frozen matched cohort must yield:

- >= **40** primary adverse `Claim` events total;
- >= **15** primary adverse events in each exposure arm;
- >= **80%** of all observed future terminated projects in the matched cohort resolved unambiguously as adverse or routine under the frozen hierarchy.

If future support is below these thresholds, E01 must HOLD for insufficient outcome support.

If support passes, the later primary test is a two-sided exact McNemar test on matched-pair adverse-event discordance with:
- alpha = **0.05**;
- materiality gate = absolute matched risk difference >= **3 percentage points**;
- no covariate/model substitution may rescue a failed primary test.

N01 itself computes none of these future quantities.

## Immutable 18-gate N01 contract / 불변 18개 gate

Exactly **18/18 PASS** is required:

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical parent is F01 18/18 PASS / `DEC-247` |
| 2 | Issue binding | runner executes only after a new Issue is created against this exact contract commit |
| 3 | Historical source identity | all three required historical source fingerprints exactly match F01 |
| 4 | Exact FHA reconstruction | 2026-08-31 active exact-qualified project count reproduces F01 within exact source semantics |
| 5 | Deterministic property linkage | property deduplication yields no unresolved multi-property identity in retained cohort |
| 6 | Deterministic latest inspection | latest pre-cutoff score/date assignment is unique under frozen rules |
| 7 | Eligible cohort support | >= 7,000 |
| 8 | Exposure separation | Q25 < Q75 and LOW/HIGH definitions computed exactly once |
| 9 | LOW support | >= 1,500 |
| 10 | HIGH support | >= 1,500 |
| 11 | Covariate completeness | retained LOW/HIGH candidates have all frozen matching covariates |
| 12 | Matched-pair support | >= 1,200 pairs |
| 13 | Geographic support | >= 20 states |
| 14 | Program support | >= 8 SOA category/sub-category values |
| 15 | Post-match balance | all five continuous absolute SMD <= 0.15 and exact state/SOA balance preserved |
| 16 | Pair integrity | no project reused; pair IDs/fingerprint deterministic |
| 17 | Outcome firewall | future terminated rows opened = 0; future adverse membership opened = false; relationship/prediction/ranking/causal metric = false |
| 18 | Reproducibility/cost | immutable evidence records source hashes, quantiles, counts, exclusions, pair-manifest SHA-256, runner SHA-256 and cost = 0 USD |

## Terminal rule / 종결 규칙

PASS:

`PASS_US_HUD_MF_N01_MATCHED_INSPECTION_DESIGN_IDENTIFIABLE`

Any valid gate failure:

`HOLD_US_HUD_MF_N01_MATCHED_INSPECTION_DESIGN_NOT_IDENTIFIABLE`

PASS authorizes only a separate E01 contract. It does not authorize opening future membership inside N01.

## Non-claims / 비주장

N01 makes no claim that lower inspection scores predict or cause later claim termination and makes no property/lender/servicer risk ranking or recommendation.

Incremental monetary cost must remain **0 USD**.
