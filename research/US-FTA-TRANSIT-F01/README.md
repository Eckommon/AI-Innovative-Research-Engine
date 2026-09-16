---
id: US-FTA-TRANSIT-F01
type: outcome-blind-source-schema-agency-mode-time-feasibility
created: 2026-09-16
status: CONTRACT_FROZEN_PRE_ISSUE
selected_by: PORTFOLIO-R33
selection_decision: DEC-205
candidate_outcome_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-F01 — NTD Breakdowns × Major Safety Events agency-mode/time feasibility

## Purpose / 목적

This F01 is the sole descendant authorized by `PORTFOLIO-R33 = SELECT_US_FTA_TRANSIT_001_BREAKDOWNS_TO_MAJOR_SAFETY_F01`.

F01 asks only whether current official Federal Transit Administration / National Transit Database sources support a deterministic and prospectively reconcilable structural panel:

`annual Breakdowns by NTD agency × mode × TOS → exact NTD agency × mode scope → later Major Safety Events`

F01 does **not** test whether mechanical breakdown burden predicts, precedes, causes, ranks, or is associated with Major Safety Event occurrence.

The contract is frozen before Issue binding and before reading any breakdown-conditioned safety outcome.

## Frozen official sources / 고정 공식 원천

### A. Annual Breakdowns — exposure-structure source

Official identities:
- FTA product: `2024 Breakdowns`
- Data.gov product: `2022 - 2024 NTD Annual Data - Breakdowns`
- DOT Open Data / Socrata dataset ID: **`amkt-4ehs`**
- landing page: `https://data.transportation.gov/d/amkt-4ehs`
- schema metadata: `https://data.transportation.gov/api/views/amkt-4ehs/columns.json`
- frozen CSV distribution: `https://data.transportation.gov/api/v3/views/amkt-4ehs/export.csv?accessType=DOWNLOAD`
- official FTA page: `https://www.transit.dot.gov/ntd/data-product/2024-breakdowns`

Current official catalog semantics state that the product contains mechanical-failure data for applicable agency/mode/Type-of-Service reporting in **2022, 2023 and 2024**. The FTA product page exposes Breakdowns by Agency, Mode and TOS. Only Full Reporters report breakdowns under this product family.

### B. Monthly Modal Time Series — reporter-scope/time bridge

Official identities:
- DOT Open Data / Socrata dataset ID: **`5ti2-5uiv`**
- landing page: `https://data.transportation.gov/d/5ti2-5uiv`
- schema metadata: `https://data.transportation.gov/api/views/5ti2-5uiv/columns.json`
- frozen CSV distribution: `https://data.transportation.gov/api/v3/views/5ti2-5uiv/export.csv?accessType=DOWNLOAD`
- official FTA page: `https://www.transit.dot.gov/ntd/data-product/monthly-modal-time-series-safety-and-service`

Current official metadata defines this as monthly service and Safety & Security time series by **transit agency × mode × year × month** for Full Reporters, spanning calendar year **2014 to present**. Safety events in the most recent validation window are withheld from corresponding monthly rows while under review. This source is used in F01 only to verify common agency/mode/reporting-scope/time semantics; no safety count or rate is used as a candidate outcome.

### C. Major Safety and Security Events — downstream-event schema source

Official identities:
- DOT Open Data / Socrata dataset ID: **`9ivb-8ae9`**
- landing page: `https://data.transportation.gov/d/9ivb-8ae9`
- schema metadata: `https://data.transportation.gov/api/views/9ivb-8ae9/columns.json`
- frozen CSV distribution: `https://data.transportation.gov/api/v3/views/9ivb-8ae9/export.csv?accessType=DOWNLOAD`
- official FTA major-only time-series context: `https://www.transit.dot.gov/ntd/data-product/safety-security-major-only-time-series-data`

Current official metadata describes this as Major Safety and Security Events from January 2014 to the most recently published validated data, with a normal publication lag of roughly three months.

## Frozen identity rules / 고정 identity 규칙

### Agency identity

Use only a source-native **NTD agency identifier** exposed by official schema metadata/bytes. `NTD ID` / its source field name is the required semantic identity.

Normalization:
1. convert to UTF-8 text without numeric rounding;
2. trim leading/trailing whitespace;
3. reject blank/null values;
4. preserve the source textual identifier for audit;
5. canonical comparison may remove surrounding whitespace only;
6. no agency-name, city, address, fuzzy, geospatial, manual or inferred alias repair.

If either downstream official source does not expose a source-native NTD agency identifier that can be matched exactly to Breakdowns, F01 is HOLD. Agency names may be inspected only as descriptive schema fields, never as a repair key.

### Mode identity

Use only the source-native NTD **mode code**. Trim whitespace and compare exact uppercase code. No mode-name fuzzy mapping is authorized.

### Type of Service (TOS)

Breakdowns is source-native at `NTD agency × mode × TOS × report year` grain. TOS must remain explicit during F01.

The only prospective collapse permitted for **structural key support** is:

`agency × mode × TOS × year → agency × mode × year`

by set projection after verifying the source key grain. F01 may verify that failure/service numeric fields are arithmetically aggregable, but it may not construct a breakdown-risk class or inspect safety outcomes conditioned on any such aggregation.

No later F01 repair may add an unregistered dimension to rescue duplicate or incompatible keys.

## Frozen time rules / 고정 시간 규칙

Breakdowns:
- use source-native report year only;
- require all **2022, 2023, 2024** years to be present;
- do not substitute publication/update dates.

Monthly Modal:
- use source-native calendar year/month only;
- require support beginning no later than 2014 and continuing into 2026 or the latest officially published period available to the runner;
- the most recent **three months are never treated as fully validated safety support** when official metadata says they are withheld/under validation.

Major Safety Events:
- use source-native event date or source-native event year/month semantics exposed by the official schema;
- require structural temporal support from 2014 onward;
- F01 may count distinct supported calendar years/months only. It may not compute event incidence by any Breakdown-derived unit.

## Frozen structural measurements / 고정 구조 측정

F01 may compute/persist only the following.

### Breakdowns
- bytes read / row count for ingestion integrity;
- official schema fingerprint;
- exact field names used for NTD ID, mode, TOS and report year;
- distinct report years;
- distinct `NTD ID × mode × TOS × year` keys;
- duplicate count at that exact grain;
- distinct `NTD ID × mode` pairs overall and by year;
- number of `NTD ID × mode` pairs represented in at least two Breakdown years;
- null/parseability diagnostics for structural keys;
- whether published mechanical-failure fields are numeric/arithmetically aggregable, without deriving an exposure class.

### Monthly Modal
- bytes read / row count for ingestion integrity;
- official schema fingerprint;
- exact field names used for NTD ID, mode, year and month;
- distinct supported calendar periods;
- exact source-native `NTD ID × mode` key set;
- structural duplicate/null diagnostics only;
- no persisted safety-event count/rate/metric.

### Major Safety Events
- bytes read / row count only as ingestion integrity metadata;
- official schema fingerprint;
- exact field names used for NTD ID, mode and event time;
- distinct supported calendar years/months;
- exact source-native `NTD ID × mode` key set;
- structural duplicate/null diagnostics only;
- no event-type stratification, agency-mode event count, rate, severity total or exposure-conditioned occurrence.

### Cross-source
- exact aggregate `NTD ID × mode` set intersection sizes;
- Breakdowns-pair coverage in Monthly Modal;
- Breakdowns-pair structural overlap with Major Safety Events;
- SHA-256 fingerprints of sorted key sets and intersections;
- no row-level Breakdowns→event joined table may be persisted.

## Frozen PASS requirements / 고정 PASS 요건

All must pass:

1. Official FTA/Data.gov metadata for `amkt-4ehs`, `5ti2-5uiv`, and `9ivb-8ae9` is reachable and fingerprinted.
2. Actual zero-cost machine-readable bytes/query results for all three frozen DOT datasets are readable without authentication bypass.
3. Breakdowns empirically exposes source-native NTD agency ID, mode, TOS and report-year semantics plus mechanical-failure fields.
4. Breakdowns contains all three preregistered report years **2022, 2023, 2024**.
5. At least **150 distinct valid `NTD ID × mode` pairs** exist in Breakdowns across the frozen years.
6. At least **100 distinct `NTD ID × mode` pairs** are represented in **>=2 distinct Breakdown years**.
7. The exact `NTD ID × mode × TOS × report year` grain is deterministic: no unresolved conflicting duplicate key may remain after exact text normalization.
8. Monthly Modal empirically exposes source-native NTD agency ID, mode, year and month semantics and supports calendar periods from **2014 through at least 2026** or the current official latest year when the source is evaluated.
9. At least **90%** of distinct Breakdowns `NTD ID × mode` pairs are represented in Monthly Modal at least once; this is reporter-scope compatibility only.
10. Major Safety Events empirically exposes source-native NTD agency ID, mode and event-time semantics and supports **>=10 distinct calendar years** beginning no later than 2014.
11. At least **75 distinct `NTD ID × mode` pairs** occur in the exact aggregate intersection of Breakdowns and Major Safety Events.
12. The cross-source join uses only exact source-native `NTD ID × mode`; agency-name/address/manual/fuzzy repair remains unused.
13. TOS is retained through source-grain verification; any structural projection to agency × mode is performed only after the exact TOS grain passes.
14. The official recent-safety validation lag is recorded, and no most-recent under-validation period is treated as complete support for a later experiment.
15. SHA-256 fingerprints are persisted for the three source key sets plus relevant exact intersections.
16. `breakdown_conditioned_major_safety_event_occurrence_opened = false`.
17. `row_level_breakdown_event_join_persisted = false`.
18. `relationship_computed = false`, `predictive_metric_computed = false`, `causal_claim_made = false`.
19. No unofficial mirror, paid source, paid API, paid runner, or authentication bypass; incremental monetary cost = **0 USD**.

## Frozen dispositions / 고정 판정

### PASS

`PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY`

Use only if all 19 requirements pass.

### HOLD

`HOLD_US_FTA_TRANSIT_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY`

Use after a valid evaluation when any preregistered source-access/schema/native-ID/TOS/time/cardinality/coverage requirement fails.

### Implementation failure

A transient network, parser, timeout, Socrata export defect, or workflow implementation defect that prevents a valid evaluation is **not** scientific HOLD. Preserve the failed run, fix only implementation mechanics without altering this contract, and rerun.

There is no access-only PARTIAL disposition preregistered for this F01. R33 selected FTA specifically because current official sources were directly machine-readable; if a frozen source ceases to be executable, F01 fails closed unless the failure is demonstrably transient implementation mechanics.

## Outcome-blind prohibitions / 결과 비개봉 금지사항

F01 may not compute, inspect, persist or report:
- Major Safety Event count/rate by breakdown count or breakdown intensity;
- safety-event membership for a particular Breakdowns agency-mode row;
- event severity/fatality/injury totals conditioned on Breakdowns;
- breakdown-derived risk bins/classes/rankings;
- agency safety ranking;
- correlation, regression, effect estimate, predictive score/AUC, or causal quantity;
- post-hoc source substitution or identity repair chosen because it improves downstream outcome support.

## Exact next action / 정확한 다음 행동

Bind this already-frozen contract to one dedicated Issue, create the next authorization decision, synchronize canonical mirrors, and only then build the official-source-only F01 runner. The runner must persist source/schema/cardinality/key-overlap/fingerprint evidence only and must keep all breakdown-conditioned Major Safety Event outcomes closed.

Incremental monetary cost remains **0 USD**.
