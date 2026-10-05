---
id: US-CMS-NH-F01
type: outcome-blind-structural-feasibility
created: 2026-10-06
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R53
parent_decision: DEC-299
selected_candidate: US-CMS-NH-001
future_standard_survey_membership_opened: false
future_serious_deficiency_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NH-F01 — exact-CCN archived-lineage gate before future serious standard-survey deficiency

## Mission / 목적

Determine, before opening any post-August-2026 nursing-home survey outcome, whether CMS Provider Data Catalog supports a deterministic facility-level prospective design linking non-tautological baseline structure/staffing to a **serious deficiency at the next standard health survey**.

F01 is structural only. It computes no relationship, prediction, ranking or causal metric.

## Frozen official source family

Only official CMS Provider Data Catalog / CMS nursing-home documentation is authorized:

- Provider Information dataset `4pq5-n9py`;
- Inspection Dates dataset / source-native survey-date file;
- Health Deficiencies dataset `r5ix-sfxw`;
- Nursing Home consolidated data dictionary;
- official nursing-home Archived Data page and archive/snapshot resources.

No third-party archive or mirror may satisfy a gate.

## Frozen historical baseline

### Provider longitudinal window

Exactly **September 2025 through August 2026 inclusive**.

For each month, F01 must resolve one independently fingerprintable official CMS archived/snapshot **Provider Information** row body corresponding to that processing month.

Record:
- official archive page/resource URL;
- final URL/HTTP metadata;
- source filename;
- byte size/SHA-256;
- headers;
- row count;
- distinct exact CCNs;
- Processing Date distribution.

If any frozen month lacks a row-bearing official Provider Information body, the lineage gate fails.

### Historical survey/event support

F01 may open only official CMS survey/deficiency data whose source-native Processing Date is **≤ 2026-08-31**.

The August-2026 official Inspection Dates and Health Deficiencies bodies are the primary frozen historical event-support surface if available through the official archive/current source.

No September-2026-or-later row body may be opened.

## Frozen exact identity

Primary facility identity:

> **CMS Certification Number (CCN)**

Allowed:
- text conversion;
- trim ASCII whitespace;
- accept only exact `^[0-9]{6}$`.

Prohibited:
- zero-padding;
- name/address/geographic matching;
- NPI substitution;
- chain-ID substitution;
- manual/fuzzy identity repair.

## Frozen standard-survey opportunity

Primary observation opportunity is source-native:

> **Type of Survey == `Health Inspection Standard`**

in the official Inspection Dates data.

Complaint, Fire Safety and Infection Control surveys remain separate and do not define the primary opportunity.

## Frozen serious-deficiency event

A primary historical serious event requires all:

1. exact CCN;
2. parseable Survey Date;
3. `Survey Type == Health` in Health Deficiencies;
4. `Standard Deficiency == Y`;
5. source-native `Scope Severity Code ∈ {G,H,I,J,K,L}`.

CMS's scope/severity hierarchy defines G–I as actual harm that is not immediate jeopardy and J–L as immediate jeopardy. A–F are not primary serious events.

One facility-standard-survey event is positive if at least one qualifying G–L citation is linked to that exact CCN + Survey Date.

## Anti-tautology firewall

Descendant predictive exposures may not include:
- Overall/Health Inspection/QM/Staffing star ratings;
- rating-cycle deficiency counts/scores;
- Total Weighted Health Survey Score;
- current/prior Health Deficiencies rows or derived deficiency counts;
- current/prior fines/payment denials/penalties;
- Special Focus Status;
- Abuse Icon;
- complaint/enforcement/citation status;
- any field mechanically derived from a survey outcome window.

Potentially allowed future N01 exposure families are limited to non-outcome structure/staffing concepts such as ownership type, certified beds, resident census, provider type, chain structure, first-certification age, nurse staffing hours/turnover and case-mix measures, subject to N01 preregistration.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R53 selection, checkpoint `CHK-20261006-PORTFOLIO-R53-TERMINAL`, last decision `DEC-299` |
| 2 | Issue binding | empirical runner executes only after Issue binding to this exact pre-Issue contract |
| 3 | Official source access | CMS Provider Information, Health Deficiencies, data dictionary and nursing-home archive page are reachable/officially redirected |
| 4 | Twelve-month archive lineage | every month 2025-09 through 2026-08 resolves to one row-bearing official CMS Provider Information archive/snapshot body with independent fingerprint |
| 5 | Provider schema | every frozen month exposes CCN, Ownership Type, Number of Certified Beds, Average Number of Residents per Day, Provider Type, Date First Approved, Processing Date; August exposes at least three staffing/turnover/case-mix concepts |
| 6 | Exact CCN syntax | in every frozen Provider body, ≥ **99.99%** of nonblank CCNs satisfy exact 6-digit rule |
| 7 | Monthly active support | every frozen month contains ≥ **14,000** distinct exact CCNs |
| 8 | Longitudinal continuity | ≥ **90.00%** of August-2026 exact CCNs appear in at least **9 of 12** frozen monthly Provider bodies |
| 9 | Non-tautological structural support | August body has ≥ **5** authorized non-outcome structure/staffing concepts with ≥ **90.00%** usable support |
| 10 | Inspection source/schema | historical Inspection Dates body exposes exact CCN, Survey Date, Type of Survey, Survey Cycle, Processing Date |
| 11 | Standard-survey support | ≥ **30,000** distinct exact CCN + Survey Date `Health Inspection Standard` opportunities exist in allowed historical support |
| 12 | Deficiency source/schema | Health Deficiencies exposes exact CCN, Survey Date, Survey Type, Scope Severity Code, Standard Deficiency, Inspection Cycle, Processing Date |
| 13 | Exact survey↔provider join | ≥ **99.00%** of distinct exact CCNs in standard-health-survey history match at least one frozen Provider CCN |
| 14 | Serious-event semantics/support | ≥ **5,000** distinct exact CCN + Survey Date standard-survey events contain ≥1 G–L citation; G–L values remain source-native |
| 15 | Event-date support | ≥ **99.90%** of primary historical standard-survey opportunities and serious events have parseable Survey Date |
| 16 | Opportunity/event concordance | ≥ **95.00%** of serious exact CCN+Survey Date events match an Inspection Dates `Health Inspection Standard` opportunity |
| 17 | Future/outcome firewall | Sep-2026-or-later row bodies opened = 0; future standard-survey membership = false; future serious-deficiency membership = false; prediction/relationship/ranking/causal metric = false; prohibited outcome exposure = false; identity repair = false |
| 18 | Reproducibility/cost | immutable evidence records archive/resource URLs, metadata/fingerprints, schemas, monthly counts/continuity, opportunity/event counts, joins, contract SHA, runner SHA, cutoff/firewalls and cost = 0 USD |

## Frozen terminal rule

PASS only if all 18 gates pass:

`PASS_US_CMS_NH_F01_EXACT_CCN_FUTURE_STANDARD_SURVEY_SERIOUS_DEFICIENCY_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_CMS_NH_F01_EXACT_CCN_FUTURE_STANDARD_SURVEY_SERIOUS_DEFICIENCY_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01.

Do not rescue by:
- dropping missing archive months;
- replacing archives with third-party copies;
- padding/repairing CCNs;
- including complaint surveys in the primary opportunity;
- lowering G–L to D–F;
- lowering support/join thresholds;
- using current/prior deficiency/rating/penalty fields as exposure;
- opening September-2026-or-later row bodies.

Transport/parser defects may be corrected only if scientific criteria remain unchanged and prior attempts remain immutable.

## PASS consequence

PASS authorizes only a separate outcome-blind `US-CMS-NH-N01`.

N01 must freeze one non-tautological baseline exposure family, eligible active facility cohort, standard-survey follow-up definition, common-support/matching or stratification rules, survey-timing handling, balance thresholds, minimum future survey/event support and one future CMS refresh window **before** any post-August-2026 survey outcome is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims

No nursing-home quality ranking, regulatory recommendation, serious-deficiency prediction, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
