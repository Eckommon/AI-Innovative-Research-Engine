---
id: PORTFOLIO-R49
type: stage0-cross-domain-reselection
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EIA-RET-N01
parent_disposition: HOLD_US_EIA_RET_N01_REDUNDANCY_MATCHED_COHORT_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R49 — common-support-aware reselection after EIA N01 HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `US-EIA-RET-N01` terminated at frozen 16/18 prospective-design HOLD.

R49 explicitly incorporates two recent lessons:

1. **SDWIS:** update frequency does not prove longitudinal history.
2. **EIA retirement N01:** large exposed/control arms do not prove prospective common support; exact matching can collapse to a very small overlap region.

No candidate future-event membership, effect, prediction, ranking or causal metric may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `US-SEC-IA-001` — investment-adviser structure → subsequent full Form ADV-W withdrawal

Unit: one SEC-registered investment adviser keyed by exact **Organization CRD Number**, subject to F01 proving exact ADV↔ADV-W identity coverage.

Official source prospect:
- historical Form ADV Part 1 data from 2000/2001 onward;
- current/post-2025 ADV data through IAPD;
- historical Form ADV-W files;
- Investment Adviser Information Reports from July 2006 onward.

Future event prospect:
- source-native **full withdrawal** on Form ADV-W after a prospectively frozen cutoff;
- partial withdrawal remains distinct.

Baseline exposure prospect:
- organization form, client/business mix, regulatory assets, account/client structure and other non-withdrawal Form ADV characteristics.

Anti-tautology:
- ADV-W filing/intention;
- cessation/withdrawal fields;
- direct SEC-registration ineligibility or termination markers;
- any field mechanically equivalent to future withdrawal.

Critical limitation:
- full withdrawal is a regulatory registration event, not automatically firm failure or business cessation;
- F01 must resolve full-vs-partial withdrawal and SEC↔state transition semantics;
- N01 must prove exposed/control support before any future filing is opened.

### 2. `US-CMS-NPI-001` — provider/organization structure → subsequent NPI deactivation

Unit: one NPPES provider keyed by exact **10-digit NPI**.

Official source prospect:
- monthly full replacement NPPES file;
- monthly deactivation update;
- weekly incremental updates;
- source-native deactivation reason/date and reactivation date.

Future event prospect:
- new source-native NPI deactivation after a prospectively frozen cutoff, with reason strata preserved.

Baseline exposure prospect:
- entity type, taxonomy, organization/subpart structure, practice-location multiplicity and other non-outcome NPPES characteristics.

Anti-tautology:
- prior deactivation/reactivation;
- deactivation reason/date;
- direct status-transition fields;
- any field mechanically equivalent to the future deactivation.

Critical limitation:
- deactivation may reflect death, disbandment, fraud, retirement or other causes and can be followed by reactivation;
- an NPI is not licensure/credentialing and deactivation is not automatically provider closure;
- current monthly files replace prior files, so longitudinal credit requires either archived official bodies or source-native event-date history rather than assumed snapshots.

### 3. `US-EPA-RCRA-001` — hazardous-waste-handler structure → subsequent formal enforcement action

Unit: one RCRA hazardous-waste handler keyed by exact **ID_NUMBER + ACTIVITY_LOCATION**.

Official source prospect:
- ECHO RCRAInfo facility, enforcement, evaluation, violation, NAICS and VIO/SNC-history CSVs;
- source-native enforcement identifiers and dates;
- exact keys documented across all tables.

Future event prospect:
- first new source-native **formal enforcement action** after a prospectively frozen cutoff.

Baseline exposure prospect:
- non-outcome facility structure such as handler universe/type, generator class, transporter/TSDF role, NAICS and stable site characteristics.

Anti-tautology:
- violation/SNC flags or history;
- enforcement history/count;
- evaluation findings;
- penalties;
- unresolved compliance;
- any direct enforcement precursor.

Critical limitation:
- enforcement is conditional on inspection/evaluation and regulatory attention;
- N01 must address inspection-selection/common-support before any outcome access;
- causal interpretation is prohibited unless separately supported.

### 4. `US-FDA-DEV-001` — medical-device establishment/listing structure → subsequent device recall

Unit: one medical-device establishment keyed prospectively by exact **FEI / registration identifier**, only if F01 proves deterministic registration-listing↔recall harmonization.

Official source prospect:
- FDA weekly registration/listing downloadable files;
- openFDA registration-listing endpoint/download;
- openFDA device-recall endpoint covering records since 2002 and updated weekly/monthly;
- harmonized device identifiers including FEI/registration fields where available.

Future event prospect:
- new source-native device recall associated with an eligible baseline establishment after a prospectively frozen cutoff.

Baseline exposure prospect:
- establishment role/type, listing breadth, product-code/class composition and other non-recall structural fields.

Anti-tautology:
- prior recall count/history;
- enforcement history;
- adverse-event history;
- known correction/removal action;
- direct recall precursor.

Critical limitation:
- FEI/registration harmonization may be incomplete;
- recalls are product-level actions while registration is establishment-level, creating many-to-many exposure/outcome structure;
- F01 must prove exact establishment attribution before N01.

## Frozen official source anchors / 공식 소스

### SEC
- `https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data`
- `https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers`
- `https://www.sec.gov/about/forms/formadv-w.pdf`

### CMS NPPES
- `https://download.cms.gov/nppes/NPI_Files.html`
- `https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination`

### EPA RCRAInfo
- `https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary`
- `https://echo.epa.gov/tools/data-downloads`

### FDA / openFDA
- `https://www.fda.gov/medical-devices/device-registration-and-listing/establishment-registration-and-medical-device-listing-files-download`
- `https://open.fda.gov/data/device-recall/`
- `https://open.fda.gov/apis/device/recall/`
- `https://open.fda.gov/data/downloads/`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-dataset / cross-table information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. Longitudinal + prospective common-support information gain
9. Low overlap / novelty risk

Dimension 7 remains the first interpretive priority. Dimension 8 now explicitly asks both:
- does source-native historical/event lineage exist prospectively; and
- is there a credible path to sizable comparable arms without outcome-driven rematching?

## Frozen tie-break / 동점 규칙

If totals tie, apply in order:
1. source-native/deterministic join defensibility;
2. longitudinal + prospective common-support information gain;
3. low overlap / novelty risk;
4. direct future-event quality;
5. independent-unit prospect;
6. zero-cost operability;
7. cross-dataset information gain.

If still tied, no selection until an outcome-blind discriminator is documented.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:
1. current official source/schema/access revalidation;
2. explicit event/history-lineage verification;
3. prospective unit/exposure/control support-risk assessment without opening candidate future membership;
4. canonical internal-history overlap check;
5. bounded external literature/framework overlap review;
6. exactly one immutable `/45` scorecard;
7. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- EIA retirement redundancy design may not be rescued by rematching, caliper widening, stratum merging, threshold reduction or outcome access.
- Current/latest-only update language cannot earn longitudinal credit without archived official bodies or source-native event history.
- SEC withdrawal may not be called business failure without separate evidence.
- NPI deactivation may not be called provider closure without separate evidence.
- RCRA violation/enforcement/evaluation history is prohibited as descendant predictive exposure.
- FDA recall/adverse-event/enforcement history is prohibited as descendant predictive exposure.
- Paid/private/commercial sources remain excluded under COST-001.

## Non-claims / 비주장

R49 establishes no adviser-withdrawal relationship, NPI-deactivation relationship, RCRA-enforcement relationship, device-recall relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
