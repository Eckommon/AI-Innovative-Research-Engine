---
id: US-CMS-NPI-F01
type: outcome-blind-structural-feasibility
created: 2026-10-13
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R56
parent_decision: DEC-313
selected_candidate: US-CMS-NPI-002
future_deactivation_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-F01 — exact-NPI Type-2 structural gate before future deactivation

## Mission / 목적

Determine, **before opening any later NPPES update membership**, whether the official CMS NPPES Version-2 dissemination files support a deterministic prospective study of active Type-2 organization structure and subsequent source-native NPI deactivation.

F01 is structural only. It does not test whether taxonomy plurality, practice-location plurality, provider age, organization form or any other characteristic predicts deactivation.

## Frozen official source family

- NPI files page: `https://download.cms.gov/nppes/NPI_Files.html`
- CMS Data Dissemination: `https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination`
- current Version-2 monthly full replacement ZIP resolved from the NPI files page after Issue binding;
- current Version-2 monthly deactivation ZIP resolved from the same page after Issue binding;
- current Version-2 weekly incremental link may receive metadata/HEAD only in F01; its row body is sealed.

CMS states that:
- Version 2 is the supported monthly/weekly layout from 2026;
- the monthly full replacement contains deactivated NPIs and deactivation dates;
- a separate monthly deactivation file is available;
- weekly files include newly assigned, updated and newly deactivated NPIs;
- each full ZIP includes Other Name, Practice Location and Endpoint reference files.

## Frozen baseline

After Issue binding, Attempt 01 may download exactly:
1. the currently listed Version-2 monthly full replacement ZIP;
2. the currently listed Version-2 monthly deactivation ZIP.

Those exact bodies become the F01 historical/structural baseline and must be fingerprinted by final URL, HTTP metadata, byte size, SHA-256 and ZIP inventory.

The raw bodies are transient under RAW-001 and must not be committed.

The current weekly incremental file and every later monthly/weekly file remain **body-sealed** in F01. Metadata/HEAD may be recorded without consuming row membership.

## Frozen identity

Primary identity is exact NPI.

Allowed normalization:
1. text conversion;
2. ASCII trim;
3. accept only `^[0-9]{10}$`.

No padding, truncation, name/address/taxonomy/geographic matching, legacy-ID substitution or manual repair.

The project does not require an external NPI checksum algorithm; the frozen identity criterion is source-native exact 10-digit NPI syntax plus uniqueness/linkage.

## Frozen population

The prospective population candidate is **active Type-2 organization NPIs** only.

F01 operational definition:
- `Entity Type Code == 2`;
- exact NPI;
- `NPI Deactivation Date` blank at the baseline;
- if a source-native reactivation date exists, it is recorded for semantics but does not convert a currently deactivated NPI into active unless the baseline record itself represents it as active under CMS fields.

Type-1 individual NPIs are excluded from the initial descendant design.

## Frozen structural exposure family

F01 may compute structural support only, not outcome relationships.

Allowed candidate structural variables:
- count of nonblank Healthcare Provider Taxonomy Codes;
- practice-location count from the official Practice Location reference file;
- enumeration age from Provider Enumeration Date;
- organization/provider taxonomy family;
- non-outcome endpoint/location structure.

Primary N01 candidate exposure family, if F01 passes:
- **multi-taxonomy vs single-taxonomy active Type-2 organizations**, subject to separate N01 preregistration and common-support validation.

F01 may count these arms only to assess support. It may not compare historical or future deactivation rates across them.

## Frozen event semantics

Primary descendant event is exactly:

> a source-native **NPI deactivation** first appearing after the N01 lock in an official later CMS deactivation/full/weekly update.

This is an **administrative NPPES registry event only**.

It must not be described as:
- provider closure;
- insolvency;
- death;
- loss of licensure;
- quality failure;
- patient-access loss.

Reactivation is a competing/reversal state and must be handled separately in N01.

## Future-update firewall

A future descendant may open an update body only after N01 freezes its cohort/exposure/comparator/event window.

F01 must not consume rows from:
- the current weekly incremental file;
- any monthly full/deactivation file newer than the two baseline bodies first resolved after Issue binding.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R56 CMS selection, checkpoint `CHK-20261013-PORTFOLIO-R56-TERMINAL`, last decision `DEC-313` |
| 2 | Issue binding | empirical runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official current source page | NPI Files and CMS Data Dissemination pages reachable; Version-2 monthly full/deactivation and weekly families documented |
| 4 | Monthly full ZIP | currently listed V2 monthly full ZIP resolves from official page, is parseable, ≥ **500 MB**, SHA-256 recorded |
| 5 | Monthly deactivation ZIP | currently listed V2 deactivation ZIP resolves, is parseable, ≥ **1 MB**, SHA-256 recorded |
| 6 | Full-file schema | main dissemination CSV exposes NPI, Entity Type Code, Provider Enumeration Date, Last Update Date, NPI Deactivation Date, NPI Reactivation Date and ≥1 taxonomy-code column |
| 7 | Exact NPI syntax | ≥ **99.999%** of nonblank main-file NPIs satisfy exact 10-digit syntax |
| 8 | NPI uniqueness | ≥ **99.999%** of exact main-file NPIs are unique |
| 9 | Active Type-2 support | ≥ **500,000** exact Type-2 NPIs have blank baseline deactivation date |
| 10 | Structural taxonomy support | among active Type-2 NPIs, ≥ **95.00%** have ≥1 nonblank taxonomy code |
| 11 | Candidate arm scale | among active Type-2 NPIs with taxonomy support: single-taxonomy ≥ **100,000** and multi-taxonomy ≥ **100,000** |
| 12 | Practice-location reference | official Practice Location reference file is present; ≥ **99.90%** of its nonblank NPIs satisfy exact syntax and ≥ **99.00%** exact-match a main-file NPI |
| 13 | Deactivation schema | separate monthly deactivation body exposes exact NPI and deactivation-date concepts |
| 14 | Deactivation identity/date quality | ≥ **99.99%** exact NPI syntax and ≥ **99.90%** parseable nonblank deactivation dates |
| 15 | Historical event support | separate monthly deactivation body contains ≥ **50,000** distinct exact NPIs |
| 16 | Update-family/future seal | official weekly update family is discoverable by metadata only; weekly row body opened = false; later monthly body opened = false; future membership opened = false |
| 17 | Outcome/identity firewall | no relationship/prediction/ranking/causal metric; no deactivation/reactivation/history exposure; no repaired identity |
| 18 | Reproducibility/cost | immutable evidence records URLs/metadata, both baseline SHA-256s, ZIP inventories, schemas, counts/arm support, contract/runner SHA, firewall values and cost = 0 USD |

## Frozen terminal rule

PASS only if all gates pass:

`PASS_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_NOT_READY`

A valid HOLD is terminal for this exact F01. Do not lower thresholds, mix Type-1 units, redefine deactivation, or open future update bodies after observation.

Transport/parser corrections are permitted only if scientific criteria remain unchanged and prior attempts remain immutable.

## PASS consequence

PASS authorizes only a separate outcome-blind `US-CMS-NPI-N01`.

N01 must freeze:
- exact active Type-2 cohort;
- one structural exposure;
- comparator/common-support design;
- reactivation handling;
- minimum future deactivation opportunity;
- update window;
- balance/support thresholds;
before any later update body is opened.

E01 remains unauthorized.

## Non-claims

F01 makes no claim that organizational complexity predicts provider exit or health-care quality. Deactivation remains only a CMS/NPPES administrative state.

Incremental monetary cost must remain **0 USD**.
