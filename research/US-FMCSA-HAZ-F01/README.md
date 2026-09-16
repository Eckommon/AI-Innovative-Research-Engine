---
id: US-FMCSA-HAZ-F01
type: outcome-blind-source-schema-carrier-time-feasibility
created: 2026-09-16
status: CONTRACT_FROZEN_PRE_ISSUE
selected_by: PORTFOLIO-R32
selection_decision: DEC-201
candidate_outcome_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FMCSA-HAZ-F01 — FMCSA inspection × PHMSA highway hazmat carrier-ID/time feasibility

## Purpose / 목적

This F01 is the only descendant authorized by `PORTFOLIO-R32 = SELECT_US_FMCSA_HAZ_001_INSPECTION_TO_PHMSA_HAZMAT_F01`.

F01 asks only whether the **current official public sources** support a deterministic, temporally usable carrier-level join:

`FMCSA public roadside inspection records → exact USDOT Number → PHMSA Form 5800.1 Highway Carrier/Reporter FED DOT ID`.

F01 does **not** test whether inspection history, violation burden, OOS status, BASICs, or any derived carrier profile predicts hazardous-material incidents.

## Frozen official FMCSA sources / 고정 FMCSA 원천

### A. Vehicle Inspection File — primary inspection source

Official catalog identity:
- DOT/Data.gov dataset: `Vehicle Inspection File`
- Socrata dataset ID: **`fx4q-ay7w`**
- landing page: `https://data.transportation.gov/d/fx4q-ay7w`
- schema metadata: `https://data.transportation.gov/api/views/fx4q-ay7w/columns.json`
- frozen CSV distribution: `https://data.transportation.gov/api/v3/views/fx4q-ay7w/export.csv?accessType=DOWNLOAD`

Official FMCSA documentation states that the Vehicle Inspection File includes inspection details, enforcement/status information, violation totals, census/entity information and vehicle markings including USDOT Number; `INSPECTION_ID` links inspection files.

### B. Vehicle Inspections and Violations — structural violation/OOS source

Official catalog identity:
- DOT/Data.gov dataset: `Vehicle Inspections and Violations`
- Socrata dataset ID: **`876r-jsdb`**
- landing page: `https://data.transportation.gov/d/876r-jsdb`
- schema metadata: `https://data.transportation.gov/api/views/876r-jsdb/columns.json`
- frozen CSV distribution: `https://data.transportation.gov/api/v3/views/876r-jsdb/export.csv?accessType=DOWNLOAD`

This source is used in F01 only to verify inspection-linked violation/OOS structure and multiplicity. No violation/OOS exposure score is computed in F01.

### FMCSA cohort boundary

FMCSA states that the current public Inspection Files:
- are updated daily from an approximately 24-hour-old database;
- contain three years of historical inspection data;
- exclude inactive USDOT Numbers, shipper-only business types, and entities with an active HMSP on file at FMCSA/PHMSA.

Therefore every downstream claim is prospectively bounded to the **publicly represented FMCSA inspection cohort**. F01 must not describe this as the universe of U.S. hazardous-material carriers.

## Frozen official PHMSA sources / 고정 PHMSA 원천

### C. Hazmat Incident Reports — Data Mining Tool

Official public catalog:
- Data.gov: `Hazmat Incident Reports - Data Mining Tool`
- catalog page: `https://catalog.data.gov/dataset/hazmat-incident-reports-data-mining-tool`
- official search/export tool: `https://portalpublic.phmsa.dot.gov/analytics/saw.dll?Portal%3FPortalPath=%2Fshared%2FPublic+Website+Pages%2F_portal%2FHazmat+Incident+Report+Search`
- PHMSA incident-statistics page: `https://www.phmsa.dot.gov/hazmat-program-management-data-and-statistics/data-operations/incident-statistics`
- data dictionary: `https://portal.phmsa.dot.gov/HIP_Help/DataDictionary.pdf`

Data.gov currently describes this as a public daily-updated search tool whose results can be exported to a text file for analysis. PHMSA's current Quick Start instructs users to open `Incident Detailed Report: All fields included in Form 5800.1` and download the report.

The PHMSA dictionary defines:
- `Report Number` as the unique incident-report identifier;
- `Date of Incident`;
- `Mode of Transportation`;
- `Carrier/Reporter FED DOT ID` as the modal carrier identifier number or code.

F01 must use the **all-fields Form 5800.1 detailed report/export**, not a summary table, if executable programmatically at 0 USD.

## Frozen identity rules / 고정 identity 규칙

### FMCSA carrier identity

Use only the source-native USDOT Number from the Vehicle Inspection File.

Normalization:
1. convert source value to text without numeric rounding;
2. trim leading/trailing whitespace;
3. require digits only;
4. remove leading zeros only for canonical comparison;
5. reject blank, zero, negative, decimal, scientific-notation or nonnumeric values;
6. no carrier-name/address/DUNS/MC-number substitution.

### PHMSA carrier identity

Use only `Carrier/Reporter FED DOT ID` from records whose source-native `Mode of Transportation` is **Highway** under the PHMSA dictionary/source vocabulary.

Apply the same digit-only canonicalization. A Highway FED DOT ID is **not assumed** to be a USDOT Number merely because it is numeric; F01 must empirically verify structural compatibility with the FMCSA carrier namespace through exact overlap and value-shape checks.

### Join

Only:

`canonical_FMCSA_USDOT == canonical_PHMSA_HIGHWAY_FED_DOT_ID`

is authorized.

Prohibited:
- carrier-name matching;
- address matching;
- fuzzy matching;
- edit distance;
- geospatial matching;
- manual repair;
- inferred alias tables.

## Frozen time rules / 고정 시간 규칙

FMCSA:
- use source-native inspection date only;
- require parseability and quantify distinct calendar years;
- do not infer dates from upload/refresh timestamps.

PHMSA:
- use source-native `Date of Incident` only;
- require parseability and quantify distinct calendar years.

F01 computes **no temporal exposure→outcome relationship**. Dates are used only to establish whether a future preregistered prospective design is structurally possible.

## Frozen structural measurements / 고정 구조 측정

F01 may compute only:

FMCSA:
- row count read/evaluated;
- distinct valid USDOT carrier count;
- distinct inspection years;
- inspection-date parseability;
- distinct `INSPECTION_ID` count;
- number of carriers with repeated inspections;
- whether violation/OOS source links deterministically through the source-native inspection identifier;
- structural multiplicity only.

PHMSA:
- row count read/evaluated;
- distinct valid Highway FED DOT IDs;
- distinct incident years;
- incident-date parseability;
- distinct report numbers;
- duplicate-report structural multiplicity caused by multi-commodity/package rows.

Cross-source:
- exact aggregate carrier-ID intersection size;
- exact-key coverage rates at aggregate level;
- SHA-256 fingerprints of sorted FMCSA carrier IDs, PHMSA Highway carrier IDs and their intersection.

F01 must **not** disclose or persist carrier-level incident membership joined to inspection characteristics.

## Frozen PASS requirements / 고정 PASS 요건

All must pass:

1. FMCSA official metadata/documentation and PHMSA official metadata/dictionary are reachable and fingerprinted.
2. Actual zero-cost machine-readable FMCSA Vehicle Inspection bytes/query results are readable from official DOT/Data.gov infrastructure.
3. Actual zero-cost machine-readable FMCSA Vehicle Inspections and Violations bytes/query results are readable from official DOT/Data.gov infrastructure.
4. FMCSA required native fields are empirically present: USDOT carrier identity, inspection identity, inspection date, and a source-native inspection linkage into violation/OOS structure.
5. FMCSA has **>= 50,000 distinct valid USDOT carriers** in the current public three-year inspection source.
6. FMCSA inspection date parseability is **>=95%** among rows with valid carrier identity and supports **>=3 distinct calendar years**.
7. PHMSA official Form 5800.1 detailed report/export is publicly executable at 0 USD and returns actual machine-readable/text-export bytes without authentication bypass.
8. PHMSA detailed bytes empirically expose Report Number, Date of Incident, Mode of Transportation, and Carrier/Reporter FED DOT ID.
9. Highway-mode PHMSA records contain **>=500 distinct valid numeric FED DOT IDs**.
10. PHMSA incident-date parseability is **>=95%** among Highway records with valid FED DOT ID and supports **>=10 distinct calendar years**.
11. Exact aggregate carrier-ID intersection is **>=300 distinct carriers**.
12. FMCSA violation/OOS linkage is structurally deterministic from source-native inspection identity; multiplicity is quantified outcome-blind.
13. SHA-256 fingerprints are persisted for the three carrier-ID sets.
14. Public-cohort exclusions are preserved explicitly.
15. `hazmat_incident_occurrence_by_inspection_profile_opened = false`.
16. `carrier_level_join_membership_persisted = false`.
17. `relationship_computed = false`, `predictive_metric_computed = false`, `causal_claim_made = false`.
18. No unofficial mirror, authentication bypass, paid source or paid API; incremental monetary cost = **0 USD**.

## Frozen dispositions / 고정 판정

### PASS

`PASS_US_FMCSA_HAZ_F01_CARRIER_TIME_JOIN_READY`

Use only if **all 18** requirements pass.

### Access-only PARTIAL

`PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED`

Use only if all of the following are true:
- FMCSA requirements 1–6 and 12 are empirically evaluable and pass;
- official PHMSA documentation/dictionary clearly confirms the required detailed-report fields and public export semantics;
- the **sole unresolved blocker** is that the current official PHMSA Oracle Analytics detailed export cannot be obtained programmatically by the zero-cost runner without authentication/circumvention;
- PHMSA byte-dependent requirements 8–11 and cross-source fingerprints therefore remain **uncomputed**, not failed;
- all outcome/relationship/cost boundaries remain closed.

This PARTIAL must not be used if an available PHMSA export is readable but required fields/identity/time/cardinality/overlap fail.

### HOLD

`HOLD_US_FMCSA_HAZ_F01_SOURCE_SCHEMA_OR_IDENTITY`

Use after a valid evaluation when any preregistered source/schema/identity/time/cardinality/linkage requirement fails and the access-only PARTIAL condition does not apply.

### Implementation failure

A transient network, parser, timeout or workflow defect that prevents valid evaluation is **not** scientific HOLD/PARTIAL. Preserve the failed run, correct only implementation mechanics without changing this contract, and rerun.

## Outcome-blind prohibitions / 결과 비개봉 금지사항

F01 may not compute or inspect:
- PHMSA incident count/rate by FMCSA inspection count;
- incident count/rate by violation/OOS/BASIC category;
- future incident membership conditional on any FMCSA exposure;
- carrier ranking or risk score;
- regression/correlation/effect/predictive metric;
- causal interpretation;
- federal safety-rating interpretation.

## Exact next action / 정확한 다음 행동

Bind this frozen contract to one dedicated Issue, create `DEC-202`, synchronize canonical mirrors, then build an official-source-only runner. The runner must first prove source/schema access and may persist only aggregate structural support/fingerprints—not joined carrier-level outcome membership.

Incremental monetary cost remains **0 USD**.


## Final disposition / 최종 처분

Corrected Run `35057953144` finalizes **`PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED`**. FMCSA empirical source/schema/carrier/date/violation-linkage requirements pass; the official PHMSA detailed-export bytes remain unavailable, so PHMSA cardinality/date/intersection requirements remain uncomputed. Runs `35045639924` and `35057504925` remain preserved as implementation nonconformities. No hazmat incident outcome or carrier-level joined membership was opened.
