---
id: PORTFOLIO-R48
type: stage0-cross-domain-reselection
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-EPA-SDWIS-F01
parent_disposition: HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R48 — longitudinal-first reselection after SDWIS single-snapshot HOLD

## Mission / 목적

Select at most one next **outcome-blind F01** after `US-EPA-SDWIS-F01` terminated at frozen 15/18 scientific HOLD.

R48 explicitly incorporates the SDWIS lesson:

> A source described as monthly/quarterly updated is **not** presumed longitudinal. Candidate scoring must distinguish a replace-in-place current snapshot from a reproducible historical file/event lineage.

No candidate future-event membership, relationship, prediction, ranking or causal metric may be opened during portfolio scoring.

## Frozen candidates / 고정 후보

### 1. `US-EIA-GEN-001` — generator structure/performance → subsequent generator retirement

Unit: one U.S. utility-scale generator keyed by exact **Plant ID + Generator ID**.

Official source prospect:
- EIA-860M monthly generator inventory, with historical monthly files available from 2015 onward;
- EIA-860 annual generator files with annual history back to 1990;
- EIA-923 monthly/annual generation and fuel data for cross-dataset baseline structure/performance;
- EIA-860M retired inventory, comprehensive for generators retired since 2002 from March 2017 onward.

Future event prospect:
- first source-native transition of an eligible baseline generator to the official retired inventory after a prospectively frozen N01 cutoff.

Anti-tautology:
- planned retirement date/month/year;
- planned-retirement status;
- announced retirement/cancellation flag;
- any field mechanically encoding the future retirement event

may not be a predictive exposure.

Candidate F01 must prove exact Plant ID + Generator ID stability, multi-month historical file availability, retired-event date semantics, active/retired separation, 860↔923 joinability and future monthly-refresh sealing.

### 2. `US-SEC-IA-001` — investment-adviser business structure → subsequent full Form ADV-W withdrawal

Unit: one investment-adviser firm keyed prospectively by exact **Organization CRD number**, if that identifier is demonstrated in both baseline ADV and ADV-W sources.

Official source prospect:
- historical Form ADV Part 1 filing data for SEC-registered advisers from January 2001 through the most recent quarter;
- SEC/IAPD quarterly/current Form ADV data;
- historical Form ADV-W data;
- SEC monthly/quarterly adviser information reports.

Future event prospect:
- source-native **full withdrawal** on Form ADV-W after an N01 cutoff;
- partial withdrawals remain a separate administrative event and are not the primary outcome.

Anti-tautology:
- filed ADV-W;
- stated intent to withdraw;
- direct SEC-registration ineligibility/withdrawal fields;
- cessation dates or fields mechanically equivalent to the future withdrawal

may not be predictive exposures.

F01 must prove exact CRD identity across ADV↔ADV-W, full-vs-partial semantics, historical filing lineage, active SEC-adviser population and future filing seal. Full withdrawal is a regulatory event and must not be labeled business failure without separate evidence.

### 3. `US-EPA-RCRA-001` — hazardous-waste-handler structure → subsequent formal enforcement action

Unit: one RCRA hazardous-waste handler keyed by exact **ID_NUMBER + ACTIVITY_LOCATION** under official RCRAInfo join semantics.

Official source prospect:
- ECHO RCRAInfo national facility, enforcement, evaluation, violation, NAICS and VIO/SNC-history files;
- source-native enforcement and violation dates;
- official ID_NUMBER semantics and direct cross-table keys.

Future event prospect:
- first new source-native formal enforcement action in a later official RCRAInfo refresh after N01 design lock.

Anti-tautology:
- prior/current violation/SNC flag;
- enforcement history/count;
- evaluation finding;
- penalty amount;
- unresolved-compliance status or direct enforcement precursor

may not be predictive exposures.

Baseline exposure prospect is limited to non-outcome facility structure such as regulated universe/type, generator class, transporter/TSDF status, NAICS and stable site characteristics. Inspection-selection bias must be treated explicitly before any causal language.

### 4. `US-FMCSA-CAR-001` — motor-carrier registration structure → subsequent reportable crash

Unit: one active motor carrier keyed by exact **USDOT Number**.

Official source prospect:
- FMCSA Safety Measurement System monthly census/crash/inspection/violation input files;
- monthly carrier-history runs;
- publicly documented monthly snapshot schedule.

Future event prospect:
- a new source-native reportable crash for an eligible carrier after a prospectively locked N01 cutoff.

Anti-tautology:
- prior crash count/history;
- Crash Indicator/BASIC values;
- inspection or violation history;
- safety intervention flags;
- enforcement history

may not be predictive exposures.

Baseline exposure prospect is limited to registration/operational structure such as carrier type, power units, drivers, operation/classification, passenger/HazMat flags and properly dated mileage. F01 must prove accessible multi-month bulk snapshot history rather than assuming that monthly refreshes are archived.

## Frozen official source anchors / 공식 소스

### EIA
- `https://www.eia.gov/electricity/data/eia860m/index.php`
- `https://www.eia.gov/electricity/data/eia860/index.php`
- `https://www.eia.gov/electricity/data/eia923/index.php`
- `https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_6_04`

### SEC / IAPD
- `https://adviserinfo.sec.gov/adv`
- `https://www.sec.gov/foia-services/frequently-requested-documents/form-adv-data`
- `https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers`
- `https://www.sec.gov/files/formadv-w.pdf`

### EPA RCRAInfo
- `https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary`
- `https://echo.epa.gov/tools/data-downloads`

### FMCSA
- `https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program`
- `https://ai.fmcsa.dot.gov/SMS/HelpCenter/`

## Frozen score rubric / 고정 평가표

Each candidate receives exactly one immutable 0–5 score on nine dimensions, total `/45`:

1. Mission bottleneck fit
2. Cross-dataset / cross-table information gain
3. Direct future-event quality
4. Independent-unit prospect
5. Practical decision value
6. Zero-cost operability
7. Source-native/deterministic join defensibility
8. Longitudinal/next-gate information gain
9. Low overlap / novelty risk

Dimension 7 remains first interpretive priority; after SDWIS, Dimension 8 explicitly penalizes replace-in-place current snapshots whose historical lineage is not already evidenced prospectively.

## Frozen tie-break / 동점 규칙

If totals tie:
1. source-native/deterministic join defensibility;
2. longitudinal/next-gate information gain;
3. low overlap / novelty risk;
4. direct future-event quality;
5. independent-unit prospect;
6. zero-cost operability;
7. cross-dataset information gain.

If still tied, no selection until an outcome-blind discriminator is documented.

## Required revalidation order / 재검증 순서

After this contract commit and Issue binding:
1. current official source/schema/access revalidation;
2. explicit historical-file/event-lineage verification;
3. canonical internal-history overlap check;
4. bounded external literature/framework overlap review;
5. exactly one immutable `/45` scorecard;
6. select at most one separate outcome-blind F01.

## Frozen exclusions / 고정 제외

- SDWIS exact design may not be rescued through historical archives, relaxed PWSID thresholds or later quarterly refreshes.
- USDA Organic remains transport-terminal for the current route.
- Current/latest-only refresh language cannot earn longitudinal credit without identifiable historical files or source-native dated event history.
- EIA planned-retirement fields are prohibited future-outcome precursors.
- SEC direct withdrawal/ineligibility fields are prohibited future-outcome precursors.
- RCRA compliance/enforcement history is prohibited as descendant predictive exposure.
- FMCSA crash/SMS/inspection/violation history is prohibited as descendant predictive exposure.
- Paid/private/commercial sources remain excluded under COST-001.

## Non-claims / 비주장

R48 establishes no generator-retirement relationship, adviser-withdrawal relationship, RCRA-enforcement relationship, carrier-crash relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost must remain **0 USD**.
