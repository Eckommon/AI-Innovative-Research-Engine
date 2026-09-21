---
id: US-HUD-MF-F01
type: outcome-blind-structural-feasibility
created: 2026-09-21
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R41
parent_decision: DEC-245
selected_candidate: US-HUD-MF-001
future_terminated_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-HUD-MF-F01 — exact FHA-project structural gate before future adverse termination

## Mission / 목적

Determine, **before opening any post-2026-09-21 terminated-mortgage membership**, whether official HUD public multifamily sources can support a deterministic project-level prospective design linking historical mortgage/property/inspection structure to a later **adverse FHA multifamily insurance termination**, while keeping routine prepayment/voluntary/maturity/refinance termination separate.

F01 is structural only. It does not test whether physical condition, leverage, unpaid principal balance, subsidy structure, project size, geography or any other characteristic predicts termination.

## Frozen historical structural baseline / 고정 historical baseline

### A. FHA insured multifamily mortgage source

Official landing page:
- `https://www.hud.gov/hud-partners/multifamily-fhasl-active`

Frozen page state observed before Issue creation:
- page reports **Current as of August 31, 2026**;
- link text **Active MF Insured Mortgages**;
- link text **Terminated MF Insured Mortgages**.

After Issue binding, F01 may retrieve the two official HUD-owned workbook bodies resolved from those exact link selectors **only if the landing page still identifies the August 31, 2026 snapshot**. If the page has rolled forward, F01 must not silently use a later snapshot; it is operational HOLD unless an official same-snapshot HUD URL/redirect is recoverable without changing the contract.

The August-31 terminated workbook is authorized only as a **historical source/schema/event-semantics support file**. Its membership may not be used to choose an exposure, fit a relationship, estimate an event rate for design tuning, rank projects, or alter thresholds.

### B. HUD active multifamily property structure

Official page:
- `https://www.hud.gov/hud-partners/multifamily-preservation`

Frozen page state observed before Issue creation:
- **Active Multifamily Portfolio-Property Level data (as of 9/2/2026)**.

Official HUD ArcGIS schema anchor:
- `https://egis.hud.gov/arcgis/rest/services/cpdmaps/HudMfProps/MapServer/1?f=pjson`

The schema anchor is structural metadata. F01 may use the official September-2 property workbook or official HUD ArcGIS features only under the same source-native fields and exact-ID rules. No address/name/geospatial matching is allowed.

### C. HUD physical inspection structure

Official page:
- `https://www.hud.gov/stat/mfh/inspection-scores`

Frozen page state observed before Issue creation:
- **Project Physical Inspection Scores as of September 2, 2026**;
- official Excel download selector **REAC Physical Inspections Scores and Release Dates**.

The historical September-2 inspection workbook may be read for project linkage/cardinality only. F01 does not define an inspection-score exposure or inspect any future termination membership.

## Frozen future outcome window / 고정 future outcome window

Prospective later terminated-mortgage membership is frozen to monthly HUD source snapshots whose as-of dates fall within:

- **start:** 2026-09-21
- **end:** 2027-03-31 inclusive.

In F01, no terminated-mortgage snapshot with an as-of date after 2026-09-21 may have entity rows opened, parsed, counted, searched or cached.

Metadata-only HEAD/page checks are allowed if they consume no future workbook entity body.

## Frozen FHA Project Number identity / 고정 식별자

Primary cross-source identity is the HUD/FHA project number.

Allowed deterministic normalization is fixed **before row access**:

1. convert source value to text without numeric coercion;
2. trim leading/trailing whitespace;
3. uppercase ASCII letters if any;
4. remove literal hyphen `-` and ASCII spaces only;
5. accept only the resulting exact **8 decimal digits** as a qualified FHA project ID.

Prohibited:
- zero-padding;
- digit insertion/deletion;
- truncation;
- name/address/ZIP matching;
- fuzzy/string similarity;
- geospatial repair;
- manual repair;
- using REMS Property ID as a substitute for FHA identity on the mortgage join.

REMS Property ID may be used only for the second exact link from the official property table to official physical-inspection data after FHA-project linkage succeeds.

## Frozen adverse-event semantics / 고정 adverse event 의미

A later descendant may not classify `Terminated MF Insured Mortgages` membership itself as adverse.

For F01 to PASS, current official historical terminated-source structure must establish all of the following before future outcome membership is opened:

1. a project-level termination date field;
2. a source-native termination reason/code field with sufficiently populated historical rows;
3. official HUD documentation or source-native textual categories that permit deterministic separation of at least:
   - **adverse** default/claim/foreclosure-equivalent termination;
   - **routine/non-adverse** prepayment/voluntary termination and/or scheduled maturity/refinance-equivalent termination;
4. no model-inferred, keyword-invented or post-observation category mapping.

If current public bytes expose only `terminated` without a defensible reason distinction, this exact F01 is scientific HOLD.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R41 selection `US-HUD-MF-001`, checkpoint `CHK-20260921-PORTFOLIO-R41-TERMINAL`, last decision `DEC-245` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official landing-page state | frozen HUD mortgage, property and inspection landing pages are reachable by the runner or official same-content HUD redirect and still identify the required 2026-08-31 / 2026-09-02 historical snapshots |
| 4 | Official workbook resolution | active, historical terminated, property-level and inspection workbook selectors resolve to HUD-owned HTTPS resources; no mirror or third-party copy |
| 5 | Active mortgage workbook | August-31 active workbook is parseable and exposes FHA Project Number plus at least units, original mortgage amount, maturity date and unpaid-principal-balance concepts |
| 6 | Historical terminated workbook | August-31 terminated workbook is parseable from the official source and its SHA-256 is recorded; historical membership is not used for association/scoring |
| 7 | Exact FHA-ID syntax | ≥ **99.00%** of nonblank active-workbook FHA Project Number values qualify under the frozen 8-digit normalization; invalid values are excluded, not repaired |
| 8 | Active-project support | ≥ **10,000** distinct qualified FHA project IDs exist in the active mortgage snapshot |
| 9 | Termination schema | historical terminated workbook exposes exact FHA Project Number plus termination date and source-native termination reason/code concepts |
| 10 | Termination field support | among qualified historical terminated rows, ≥ **95.00%** have a nonblank parseable termination date and ≥ **95.00%** have a nonblank source-native reason/code |
| 11 | Adverse/routine semantic separation | official HUD documentation or source-native reason labels deterministically distinguish at least one adverse default/claim/foreclosure-equivalent category and at least one routine prepayment/voluntary/maturity/refinance-equivalent category without invented mapping |
| 12 | Property schema | official property source exposes exact `PRIMARY_FHA_NUMBER`/equivalent FHA-number concept and exact REMS Property ID/equivalent source-native property identifier |
| 13 | Mortgage→property exact-link support | ≥ **70.00%** of distinct qualified active FHA IDs exact-match at least one official property row after only the frozen FHA normalization |
| 14 | Inspection schema | September-2 official inspection source exposes exact REMS Property ID plus at least one inspection score and associated inspection/release date |
| 15 | Property→inspection support | ≥ **5,000** distinct active-mortgage FHA IDs are linked through an exact property REMS ID to at least one inspection record dated on or before 2026-09-21 |
| 16 | Future source seal | no post-2026-09-21 terminated-workbook entity row is opened; any future-source check is body-free metadata only |
| 17 | Outcome/identity firewall | future terminated rows opened = **0**; future adverse membership opened = **false**; relationship/prediction/ranking/causal metric computed = **false**; name/address/fuzzy/geo/manual identity repair used = **false** |
| 18 | Reproducibility and cost | immutable JSON/Markdown records selectors/final URLs, HTTP metadata, workbook SHA-256 values, normalized headers, row/cardinality/join counts, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen terminal rule / 종결 규칙

PASS only if all 18 gates pass:

`PASS_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_HUD_MF_F01_EXACT_PROJECT_ADVERSE_TERMINATION_DESIGN_NOT_READY`

No post-observation threshold reduction, later-snapshot substitution, termination-category invention, address/name repair, alternate project key, broader HUD program, third-party mirror or paid source may rescue the design.

Transport/HTML/XLSX parser defects may be corrected only when every scientific criterion and frozen snapshot remains unchanged and each prior attempt is preserved immutably.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-HUD-MF-N01` design. N01 must freeze one non-tautological historical exposure, eligibility/exclusions, comparator/matching or stratification rules, future adverse-event hierarchy, routine-termination handling, snapshot cadence, minimum event support and statistical gate **before** any post-baseline terminated membership is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that inspection condition, mortgage balance, project size, subsidy structure or any other characteristic predicts or causes adverse termination; no property risk score, lender ranking, regulatory recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
