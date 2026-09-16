---
id: US-FDA-MD-F01
issue: 141
state: ACTIVE_FROZEN_CONTRACT
created: 2026-09-16
inspection_outcomes_opened: true
recall_incidence_by_class_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FDA-MD-F01 — FDA inspection × device-recall source/schema/FEI feasibility

## Mission / 미션

Test whether the **publicly disclosed FDA medical-device inspection cohort** can be structurally linked to the FDA Device Recall identity source by exact FEI without opening recall incidence by inspection classification.

This is a source/schema/identity gate only. Inspection final classification (`NAI`/`VAI`/`OAI`) is an authorized baseline/exposure identity and is therefore open by design. The forbidden future outcome is recall incidence/membership **stratified by inspection classification** or any derived relationship.

## Frozen inspection semantics / 고정 inspection semantics

- exact establishment key: `FEI` / FDA Establishment Identifier;
- allowed final classifications: `NAI`, `VAI`, `OAI` only;
- one inspection may contain multiple Project Areas;
- structural row key: exact `(FEI, inspection end date, FDA-native Project Area-or-equivalent inspection-area field)`;
- same exact structural key with different final classifications = conflict;
- FEI duplicates across inspections/project areas are expected and are not conflicts;
- medical-device cohort must be defined only from an FDA-native inspection field/label exposed by the inspection source, never from recall/product evidence or fuzzy firm text;
- public inspection database is explicitly non-comprehensive, so any future descendant is bounded to the disclosed inspected-facility cohort and cannot estimate population-wide manufacturer risk.

## Frozen recall-source boundary / 고정 recall source 경계

Allowed openFDA Device Recall structural fields:
- `firm_fei_number`;
- `event_date_initiated`;
- `event_date_created`;
- `event_date_posted`;
- stable recall/event identity fields only as needed to deduplicate source identities.

F01 may persist aggregate counts of exact inspection FEIs, exact recall FEIs and their intersection, plus fingerprints. It must not persist intersection/recall counts by NAI/VAI/OAI or derive class-specific future-recall membership.

## Current preregistered access state / 사전등록 접근 상태

Before execution:
- FDA Dashboard visibly offers `Entire Inspections Dataset`;
- its linked `https://datadashboard.fda.gov/InspectionsDataset.xlsx` currently returns HTTP 404;
- Dashboard API access currently requires OII Unified Logon credentials;
- no unofficial mirror, cached replica, authentication bypass or paid substitute is allowed.

## Frozen full-PASS requirements / 고정 PASS 요건

All must pass:
1. official FDA inspection metadata/dashboard reachable and source metadata hashed;
2. actual official zero-cost machine-readable inspection bytes readable without auth bypass;
3. inspection bytes contain exact FEI, inspection end date, final classification and deterministic FDA-native medical-device cohort field;
4. eligible final classifications resolve exactly to NAI/VAI/OAI only;
5. exact structural-key classification conflicts = 0;
6. device inspection cohort has >=500 distinct FEIs and >=5 inspection-end calendar years;
7. repeated-inspection/project-area structure is quantifiable outcome-blind;
8. openFDA Device Recall confirms/serves native `firm_fei_number` and event-date identities over a public zero-cost route;
9. aggregate exact FEI overlap between inspection cohort and recall source >=100 distinct FEIs, with **no class-stratified overlap counts**;
10. inspection-FEI, recall-FEI and intersection identity fingerprints are frozen before any descendant outcome authorization;
11. no recall incidence/rate/count by inspection class, class-specific future-outcome comparison, model metric or causal estimate is computed; non-comprehensiveness preserved; cost 0 USD.

## Frozen dispositions / 고정 판정

- `PASS_US_FDA_MD_F01_FEI_JOIN_READY` — all 11 requirements pass.
- `PARTIAL_US_FDA_MD_F01_SOURCE_SEMANTICS_READY__INSPECTION_BYTES_ACCESS_BLOCKED` — official documentation confirms FEI/classification/project-area/device semantics, openFDA recall FEI/date route passes, and the **sole** blocker is official inspection bytes unavailable through the advertised public route while remaining official programmatic access requires credentials. Requirements dependent on those bytes remain uncomputed; no mirror/auth bypass.
- `HOLD_US_FDA_MD_F01_SOURCE_SCHEMA_OR_IDENTITY` — any failure not limited to that access-only boundary, including inability to establish FEI/schema/device cohort semantics or inadequate exact identity support once bytes are available.

No threshold, filter, identity key, source, access rule or disposition may change after support is observed.

## Official source basis / 공식 출처

- FDA Inspection Classification Database: https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-classification-database
- FDA Inspections Dashboard: https://datadashboard.fda.gov/oii/cd/inspections.htm
- FDA Dashboard Glossary: https://www.fda.gov/about-fda/fda-data-dashboard/glossary-fda-data-dashboard
- CDRH Regulatory Reliance Portal: https://www.fda.gov/medical-devices/cdrh-international-affairs/cdrh-regulatory-reliance-portal-medical-devices
- openFDA Device Recall fields: https://open.fda.gov/apis/device/recall/searchable-fields/

## Claim boundary / 주장 경계

PASS or PARTIAL establishes only structural/source readiness within the disclosed inspection cohort. It is not evidence that NAI/VAI/OAI predicts recalls, not a ranking of inspection classes, not population-wide manufacturer risk, and not a causal claim.
