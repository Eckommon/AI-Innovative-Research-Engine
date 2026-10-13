---
id: US-CMS-NPI-E01
type: preregistered-future-update-experiment
created: 2026-10-13
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-CMS-NPI-N01
parent_decision: DEC-317
baseline_full_sha256: 45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e
baseline_deactivation_sha256: fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1
n01_evidence_commit: da46a24114452a1d63a16adf731aa3b51761c88b
n01_run: 38356022445
future_update_body_opened: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-E01 — preregistered matched-pair future deactivation experiment

## Mission / 목적

Test, on exactly the locked N01 matched cohort and **without changing eligibility, exposure, matching or event semantics**, whether active Type-2 organization NPIs with multiple taxonomy codes differ from matched single-taxonomy controls in their first source-native NPI deactivation observed in the first qualifying post-baseline CMS NPPES Version-2 weekly update.

This is a one-update, two-sided matched-pair experiment. It is not a provider-closure, insolvency, licensure, quality, access or causal study.

## Parent authorization / 상위 승인

Parent N01 terminal result:

`PASS_US_CMS_NPI_N01_MULTI_TAXONOMY_MATCHED_COHORT_READY`

Canonical evidence:
- contract: `29ab6cd8368801137eff94463a5b405c1fdf10ac`;
- evidence commit: `da46a24114452a1d63a16adf731aa3b51761c88b`;
- Run: `38356022445`;
- matched pairs: **346,859**;
- exposed/common-support coverage: **97.0742%**;
- age |SMD|: **0.00809**;
- practice-location |SMD|: **0.01358**.

No future update body or arm-specific deactivation membership was opened in F01/N01.

## Frozen baseline / 고정 baseline

Reconstruct the cohort only from the exact F01/N01 baseline bodies:

- monthly full V2 SHA-256:
  `45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e`
- monthly deactivation V2 SHA-256:
  `fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1`

The cohort, eligibility, taxonomy count, structural strata and deterministic SHA256 pairing algorithm remain exactly those frozen in N01.

No persisted provider list is required; the 346,859 pairs must be reconstructed deterministically from the exact baseline bodies.

## Frozen exposure / 고정 노출

- **EXPOSED:** locked N01 active Type-2 organization NPI with taxonomy_count ≥2.
- **CONTROL:** locked N01 active Type-2 organization NPI with taxonomy_count ==1.

No future update field may change exposure assignment.

## Frozen future source / 고정 미래 소스

Official family:
`https://download.cms.gov/nppes/NPI_Files.html`

At preregistration, the latest visible Version-2 weekly listing is:

`NPPES Data Dissemination V.2 - Weekly Update - 100526_101126`

This file covers 2026-10-05 through 2026-10-11 and is a **pre-baseline metadata anchor only**. Its row body must not be opened by E01.

### Primary qualifying update rule

E01 may open **exactly one** future body: the first official Version-2 **Weekly Update** appearing on the CMS NPI Files page after this E01 contract/Issue lock that satisfies all of:

1. source is the official CMS NPPES NPI Files family;
2. filename/listing exposes a parseable weekly covered-date range;
3. covered range start is **2026-10-12 or later**;
4. covered range end is later than **2026-10-12**;
5. it is the chronologically earliest qualifying weekly listing;
6. its ZIP body has not been opened before E01 Issue binding;
7. HTTP final URL, headers, bytes and SHA-256 are recorded before outcome adjudication.

No monthly-file substitution, later-week cherry-picking or second weekly update is allowed inside this E01.

If CMS skips/withdraws the next weekly family so that no qualifying weekly file can be resolved, E01 remains `WAIT_SOURCE` rather than switching to a monthly body.

## Frozen event / 고정 사건

For a locked matched-cohort NPI, primary event = first source-native **NPI deactivation** observed in the qualifying weekly file, requiring:

- exact 10-digit NPI;
- NPI belonged to the locked baseline active cohort;
- future row has a nonblank parseable `NPI Deactivation Date`;
- deactivation date is **2026-10-12 through the qualifying weekly covered end date inclusive**.

Because all locked cohort NPIs had blank baseline deactivation and blank baseline reactivation, this identifies a newly observed administrative deactivation relative to the locked baseline.

A nonblank future reactivation date does not erase a qualifying deactivation. It is counted separately as a reversal/competing-state flag.

Rows for newly enumerated NPIs, ordinary profile updates or taxonomy/location changes are not events.

## Frozen pair table / 고정 paired table

For the 346,859 reconstructed pairs define:

- `a`: both exposed and control deactivated;
- `b`: exposed deactivated, control not deactivated;
- `c`: control deactivated, exposed not deactivated;
- `d`: neither deactivated.

Primary discordant support:
`q = b + c`.

## Frozen primary inferential metric / 주 추론 지표

Primary test:
- exact two-sided McNemar/binomial test on discordant pairs;
- null: `P(exposed-only | discordant) = 0.5`;
- alpha = **0.05**, two-sided.

Primary effect:
- matched discordant odds ratio `MOR = b / c`;
- exact 95% confidence interval obtained by transforming the exact binomial confidence interval for `b / (b+c)`.

If `b=0` or `c=0`, report the source-native finite/infinite boundary and exact interval; do not add arbitrary pseudocounts to the primary metric.

## Frozen secondary descriptive metrics / 보조 지표

Report descriptively only:

- exposed risk = `(a+b) / 346,859`;
- control risk = `(a+c) / 346,859`;
- marginal risk ratio;
- risk difference per 100,000 matched NPIs;
- total future deactivations in each arm;
- same-update reactivation counts by arm.

Secondary metrics cannot override the primary classification.

## Frozen minimum event support / 최소 사건 지지

A scientific effect classification requires both:

1. total deactivated matched NPIs across both arms `(2a+b+c) >= 30`;
2. discordant pairs `q=b+c >= 20`.

If either fails:

`INSUFFICIENT_EVENT_SUPPORT_US_CMS_NPI_E01`

This is not evidence of no difference.

## Frozen material-effect band / 실질효과 구간

Material association requires primary MOR:

- **≤ 0.80**, or
- **≥ 1.25**.

The interval `0.80 < MOR < 1.25` is the predeclared practically small-effect band.

No direction is hypothesized prospectively. Direction is labeled only after observation as lower or higher exposed deactivation odds.

## Frozen outcome classification / 결과 판정

After minimum event support is satisfied:

### 1. VALIDATED_MATERIAL_DIFFERENCE

`VALIDATED_MATERIAL_DIFFERENCE_US_CMS_NPI_E01`

only if all are true:
- exact two-sided McNemar p ≤ **0.05**;
- 95% exact MOR confidence interval excludes **1.0**;
- MOR ≤ **0.80** or MOR ≥ **1.25**.

### 2. NO_MATERIAL_DIFFERENCE

`NO_MATERIAL_DIFFERENCE_US_CMS_NPI_E01`

only if the entire 95% exact MOR confidence interval lies inside **[0.80, 1.25]**.

### 3. INCONCLUSIVE

`INCONCLUSIVE_US_CMS_NPI_E01`

for every other adequately supported result, including:
- statistically significant but materially small effect;
- materially large point estimate with interval including 1;
- confidence interval spanning both negligible and material regions.

No threshold may be changed after future membership is opened.

## Immutable 18-gate execution-integrity contract

Exactly **18/18 execution-integrity gates** are required before the scientific classification above is valid.

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal N01 PASS checkpoint `CHK-20261013-US-CMS-NPI-N01-TERMINAL`, last decision `DEC-317` |
| 2 | Issue binding | runner executes only after new Issue binds this exact pre-Issue E01 contract |
| 3 | Baseline body identity | downloaded full/deactivation baseline bodies match both frozen F01 SHA-256 values |
| 4 | Cohort reconstruction | exactly **1,978,439** eligible, **409,936** exposed, **1,568,503** controls |
| 5 | Pair reconstruction | exactly **346,859** matched pairs; no reuse/cross-stratum mismatch |
| 6 | Pair-balance reproduction | age and practice-location SMD values reproduce N01 within absolute tolerance **1e-6** |
| 7 | Pre-anchor confirmation | CMS page metadata still identifies `100526_101126` as pre-baseline historical weekly anchor or preserves an official trace of that listing |
| 8 | First-qualifying-source rule | selected file is the earliest official V2 weekly with range start ≥ 2026-10-12 and end > 2026-10-12; no later file substituted |
| 9 | Future ZIP integrity | qualifying weekly ZIP is official, parseable, HTTP metadata/bytes/SHA recorded |
| 10 | Future schema | weekly main CSV exposes NPI, Entity Type Code, NPI Deactivation Date and NPI Reactivation Date concepts |
| 11 | Future exact identity | ≥ **99.999%** of nonblank future NPIs satisfy exact 10-digit syntax |
| 12 | Outcome join integrity | every counted event joins by exact NPI to one locked arm member; zero name/address/taxonomy/geographic repair |
| 13 | Event-date integrity | ≥ **99.90%** of candidate future deactivation rows for locked NPIs have parseable dates and counted events lie inside the frozen weekly window |
| 14 | Pair-table integrity | `a+b+c+d = 346,859`; each pair contributes exactly once |
| 15 | Reactivation accounting | same-update nonblank reactivation among counted deactivations is reported separately and does not erase the primary event |
| 16 | Primary-statistic determinism | exact McNemar p, MOR and exact 95% CI computed solely from frozen `b,c`; no model/threshold tuning |
| 17 | Scientific firewall | no provider ranking, causal claim, closure/insolvency/quality interpretation, alternative exposure, monthly substitution, later-week selection or identity repair |
| 18 | Reproducibility/cost | immutable evidence records baseline/future SHAs, source metadata, cohort/pair counts, event table, exact statistics, contract/runner SHA and cost = 0 USD |

If an execution-integrity gate fails because of a scientific/source property, E01 is invalid for scientific classification and terminates as `HOLD_US_CMS_NPI_E01_EXECUTION_INTEGRITY_FAILED`. Demonstrable parser/transport defects may be corrected only without changing any scientific criterion and with prior attempts immutable.

## Non-claims / 비주장

Even a validated material difference establishes only a prospective association between the locked taxonomy-plurality exposure and a source-native administrative NPI deactivation event over one CMS weekly update.

It does not establish:
- causal effect;
- provider closure;
- insolvency;
- loss of licensure;
- provider quality;
- patient access;
- clinical risk;
- a deployable provider ranking.

Incremental monetary cost must remain **0 USD**.
