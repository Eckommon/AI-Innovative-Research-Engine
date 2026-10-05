---
id: PORTFOLIO-R53-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-10-06
issue: 193
contract: 0015791279ada44f79201c155acdc03a21da96ac
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R53 — bounded survivor-first revalidation

## Outcome firewall

No candidate-specific future event membership, relationship, prediction, ranking or causal result was opened. Revalidation used current official source/documentation surfaces, canonical project history and bounded literature/framework context only.

## 1. US-CMS-NH-001

Current CMS Provider Data Catalog establishes:
- Provider Information: one row per active nursing home with exact CMS Certification Number (CCN), ownership, certified beds, census, chain, staffing and case-mix/turnover concepts;
- Inspection Dates: health/fire/complaint/infection-control inspection dates over the recent three cycles;
- Health Deficiencies: one citation per row with CCN, associated inspection date, citation/tag, scope and severity, status and correction date;
- Penalties: fines/payment denials with CCN and penalty/inspection date;
- recurring planned monthly updates and explicit Archived Data surfaces.

Current Health Deficiencies resource exposes >400k rows, giving materially stronger event support than recent rare-event branches.

Survivor advantage:
- exact native facility key across provider/inspection/deficiency/penalty tables;
- event frequency high enough for prospective support;
- standard-survey opportunity can be frozen to control event ascertainment;
- baseline staffing/ownership/size variables are abundant, supporting stratification/matching.

Mandatory anti-tautology:
current/prior ratings, deficiency counts/scores, fines, penalties, Special Focus status, abuse icon, survey-outcome fields and direct enforcement variables are prohibited baseline exposures.

Literature overlap is substantial: staffing, ownership and deficiencies are mature research themes. Therefore novelty credit is deliberately low. Selection value, if any, comes from prospective outcome sealing and reproducible monthly/archived design rather than a claim of novel domain discovery.

## 2. US-FRA-RR-001

FRA Safety Data Portal currently provides reports/full datasets for Train Accidents, Casualties and Operational Data. The official DataDownloadService exposes annual railroad-level Form 54 accident data and Form 55 operational data plus a railroad reference file and XML schemas.

Survivor advantage:
- direct accident event family with long historical depth;
- operational denominator/exposure source separated from accident reports;
- full datasets and source-native railroad reporting level;
- events are sufficiently frequent.

Primary risks:
- railroad mergers, consolidations and code changes;
- reporting-threshold changes across time;
- exact railroad-reference identity continuity must be empirically established;
- exposure and outcome forms can contain overlapping safety information that must be firewalled.

FRA remains a strong second candidate but needs more identity/regime adjudication than CMS CCN.

## 3. UK-FHRS-EST-001

The Food Standards Agency Ratings API exposes exact FHRSID, business type, Local Authority, RatingDate, RatingValue and hygiene/structural/confidence-in-management score concepts.

Strengths:
- exact native FHRSID;
- API/machine readability;
- direct inspection-derived rating date/value.

Weaknesses:
- the reviewed current API primarily exposes latest/current establishment rating state;
- a reproducible row-bearing longitudinal historical rating ledger was not established during R53 revalidation;
- inspection timing varies by Local Authority/risk;
- prior/current rating and component scores would be tautological predictors and are excluded.

Therefore F01 survivor probability is materially lower than CMS/FRA.

## 4. AU-ACQSC-CARE-001

The Aged Care Quality and Safety Commission current Provider Register exposes Provider ID (PRV-*), registration status/end date and an Excel register. The Commission also publishes compliance/enforcement information and a machine-readable current/former banning-order register.

Strengths:
- explicit native Provider ID;
- current registered-provider universe;
- material public-safety/regulatory value.

Weaknesses:
- the Aged Care Act 2024 transition materially changed provider registration and enforcement;
- comparable pre-transition longitudinal provider/event lineage has not been established;
- banning orders may target workers/responsible persons and cannot substitute for provider-level outcome identity;
- direct provider suspension/revocation events are likely rarer than CMS deficiency events.

## Canonical overlap and recent-failure adjustment

Repository search found no prior exact branches for the four R53 candidate IDs.

Recent reusable negatives modify expected survivor value:
- SEC F01: row-bearing monthly lineage gap;
- FCC F01: exact-ID representation mismatch;
- PHMSA F01: source-host transport block;
- CRA F01: historical event support too small;
- EIA N01: strong F01 but inadequate common support after matching.

R53 therefore gives explicit priority to source families with dense event ledgers and broad baseline cohorts.

## Revalidation conclusion

All four frozen candidates remain eligible for one immutable scorecard.

**CMS Nursing Home has the strongest survivor-first architecture** because exact CCN links a large active provider universe to recurring inspection opportunities and a dense source-native deficiency/penalty ledger, while archived/monthly source surfaces offer a direct F01 test of historical snapshot continuity.

No future survey/deficiency/penalty membership was opened.

Incremental monetary cost: **0 USD**.
