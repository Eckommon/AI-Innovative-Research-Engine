---
id: PORTFOLIO-R54-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-10-08
issue: 195
contract: bc9b5b49481ea2b44a2aac842f0a255e1d0de619
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R54 — bounded direct-source / overlap revalidation

No candidate future-event membership, effect, prediction, ranking or causal result was opened.

## US-FRA-RR-001

Current FRA surfaces expose full Form 54 Rail Equipment Accident/Incident and Form 55 Operational datasets, database dictionaries, current/previous form definitions, reporting-threshold guidance and a documented `DataDownloadService`. The service exposes railroad/year operations for both Form 54 and Form 55 plus railroad reference data and XML schemas.

This directly addresses the CMS failure mode: the empirical body is a documented machine-readable service rather than an archive SPA. Railroad-level yearly operational exposure and accident outcomes are source-native and temporally separable.

Primary risks are railroad code consolidation/mergers, threshold regime changes and N01 common support across large versus small railroads. Prior accident/casualty information remains prohibited as exposure.

## US-EPA-RCRA-001

EPA ECHO directly publishes the RCRAInfo ZIP and defines six CSV tables linked by `ID_NUMBER + ACTIVITY_LOCATION`. The facility, evaluation, violation and enforcement files are source-native, while `RCRA_VIOSNC_HISTORY.csv` provides explicit monthly `YRMONTH` compliance history.

Transport and exact identity are therefore strong. The main design penalty is scientific rather than technical: future violation ascertainment must be conditioned on an evaluation/inspection opportunity, and inspection targeting is non-random. Current/prior violation, SNC, enforcement and penalty fields cannot be exposure.

## US-FAA-NTSB-AIR-001

FAA directly offers the complete Aircraft Registration Database, and the NTSB aviation dictionary exposes RegistrationNumber and aircraft characteristics. Static/direct transport is strong.

However N-number reuse, deregistration/re-registration and ownership changes make temporal aircraft identity harder than railroad or RCRA identities. Serial-number concordance must be established before an N-number-only longitudinal claim. Operational hours/exposure are also absent from the registry baseline.

## US-NHTSA-REC-001

NHTSA directly publishes static recall ZIPs with daily-updated recall data going back to 1949 plus APIs and dictionaries. Transport and event frequency are strong.

The unit is weaker: make/model/model-year is not necessarily a unique engineering platform. Complaints, investigations and manufacturer communications are precisely the signals NHTSA uses around defect discovery, so they are excluded from first-descendant exposures to avoid precursor leakage. This sharply reduces cross-table information gain for an outcome-blind first experiment.

## Canonical overlap

No prior canonical artifact was found for these exact R54 candidate identifiers. FRA was held as the R53 runner-up but never activated; it is rescored here under a new pre-Issue contract rather than promoted post hoc. RCRA was a prior portfolio alternative but no exact RCRA F01 was activated. FAA/NTSB and NHTSA exact routes are new.

## Revalidation conclusion

All four candidates remain eligible. FRA has the highest combined survivor probability because:
1. source-native direct machine-readable service;
2. explicit annual railroad operational and accident datasets;
3. stable cross-form reporting context;
4. a direct, sufficiently frequent event;
5. no inspection-opportunity conditioning comparable to RCRA.

Incremental monetary cost: **0 USD**.
