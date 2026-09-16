---
id: US-EPA-XMEDIA-F01
type: outcome-blind-cross-media-source-schema-frs-identity-feasibility
created: 2026-09-17
status: CONTRACT_FROZEN_PRE_ISSUE
selected_by: PORTFOLIO-R34
selection_decision: DEC-211
candidate_outcome_opened: false
effluent_violation_rows_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-F01 — RCRAInfo / RCRA Pipeline × FRS × ICIS-NPDES exact cross-media feasibility

## Purpose / 목적

This F01 is the sole descendant authorized by `PORTFOLIO-R34 = SELECT_US_EPA_XMEDIA_001_RCRA_TO_NPDES_F01`.

F01 asks only whether current official U.S. EPA public sources support a deterministic, source-native facility bridge:

`RCRA facility / evaluation structure → exact FRS REGISTRY_ID → exact NPDES facility / permit structure`

F01 does **not** test whether RCRA compliance-monitoring or violation history predicts, precedes, causes, ranks, or is associated with later NPDES effluent-limit exceedance.

The contract is frozen before Issue binding and before opening any NPDES effluent-violation row or RCRA-conditioned NPDES outcome.

## Frozen official sources / 고정 공식 원천

Only the following current official EPA sources are authorized.

### A. RCRA Pipeline — RCRA structural/time source

- Documentation: `https://echo.epa.gov/tools/data-downloads/rcra-pipeline-download-summary`
- Official ZIP: `https://echo.epa.gov/files/echodownloads/pipeline_rcra_downloads.zip`
- Required structural table: `PIPELINE_RCRA_01_EVALUATIONS.csv`
- Required source-native fields: `REGISTRY_ID`, `SOURCE_ID`, `EVAL_DATE` plus source-grain evaluation identity fields exposed by the current file.

EPA documents `REGISTRY_ID` as the Federal Registry/FRS identifier, `SOURCE_ID` as the RCRA facility ID, and `EVAL_DATE` as the compliance-monitoring/evaluation date.

F01 may inspect evaluation structure and dates only. It may not read or persist `FOUND_VIOLATION`, violation type, violation determination, return-to-compliance, enforcement, penalty, or any exposure score.

### B. FRS Facilities and Linkages — official cross-program identity bridge

- Documentation: `https://echo.epa.gov/tools/data-downloads/frs-download-summary`
- Official ZIP: `https://echo.epa.gov/files/echodownloads/frs_downloads.zip`
- Required table: `FRS_PROGRAM_LINKS.csv`
- Required fields: `PGM_SYS_ACRNM`, `PGM_SYS_ID`, `REGISTRY_ID`.

EPA documents Program Links as the linkage from a program record (`PGM_SYS_ACRNM × PGM_SYS_ID`) to the FRS facility (`REGISTRY_ID`). Only exact official program linkages are authorized.

### C. ICIS-NPDES National Dataset Part 1 — downstream structural source

- Documentation: `https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary`
- Official Part 1 ZIP: `https://echo.epa.gov/files/echodownloads/npdes_downloads.zip`
- Required tables: `ICIS_FACILITIES.csv`, `ICIS_PERMITS.csv`.
- Required facility fields: `NPDES_ID`, `FACILITY_UIN`.
- Required permit structural/time fields: `EXTERNAL_PERMIT_NMBR`, and source-native permit date/status fields exposed by the current schema, including `ORIGINAL_ISSUE_DATE`, `ISSUE_DATE`, `EFFECTIVE_DATE`, `EXPIRATION_DATE`, `RETIREMENT_DATE`, `TERMINATION_DATE` where present.

EPA documents `NPDES_ID` / `EXTERNAL_PERMIT_NMBR` as NPDES permit identity and `FACILITY_UIN` / `REGISTRY_ID` semantics as the FRS facility identifier.

### D. Explicitly forbidden downstream outcome source

The following source is **not authorized for F01 access**:

- ICIS-NPDES National Dataset Part 2 — effluent violations (`NPDES_EFF_VIOLATIONS.csv`), currently distributed separately from Part 1.

F01 runner code must not download, query, open, stream, inspect, fingerprint, count, or infer rows from the Part 2 effluent-violation product or jurisdictional effluent-violation downloads. DMR value/limit datasets are also not authorized in F01.

## Frozen identity rules / 고정 identity 규칙

### RCRA identity

Use exact source-native `SOURCE_ID` and exact `REGISTRY_ID` from the authorized RCRA evaluation table.

Normalization is limited to:
1. decode as text;
2. trim surrounding whitespace;
3. reject blank/null;
4. preserve leading zeros and source text semantics;
5. compare exact canonical text after trimming only.

No facility-name, address, corporate parent, geographic coordinate, fuzzy, manual, inferred, or post-outcome repair is authorized.

### FRS identity

Use only exact official `FRS_PROGRAM_LINKS.csv` rows. For the two relevant program families, program-system acronyms must be resolved from the current source using exact normalized text consistent with EPA-documented `RCRAINFO` and `NPDES` semantics.

For any `(PGM_SYS_ACRNM, PGM_SYS_ID)` with more than one distinct nonblank `REGISTRY_ID`, mark that program record as identity-conflicting and exclude it from exact-link support. Do not choose a preferred Registry ID.

### NPDES identity

Use exact `NPDES_ID` / `EXTERNAL_PERMIT_NMBR` and exact `FACILITY_UIN` in Part 1 only. Permit/facility identity may be reconciled only by exact NPDES permit ID semantics documented by EPA.

### Cross-media bridge

The only authorized RCRA↔NPDES bridge is exact equality of a nonblank official FRS `REGISTRY_ID` after both sides are independently supported by FRS Program Links.

Direct agreement between the RCRA Pipeline `REGISTRY_ID`, FRS RCRAInfo linkage, ICIS-NPDES `FACILITY_UIN`, and FRS NPDES linkage may be measured. Disagreement is a structural diagnostic, never a repair invitation.

## Frozen time rules / 고정 시간 규칙

RCRA:
- use source-native `EVAL_DATE` only;
- report distinct valid evaluation calendar years;
- require at least **10 distinct calendar years** of valid RCRA evaluation support;
- require the maximum valid RCRA evaluation year to be at least **2025**.

NPDES Part 1:
- inspect only source-native permit issue/effective/expiration/retirement/termination dates;
- require at least **10 distinct calendar years** represented across valid structural permit dates;
- no effluent monitoring period, violation date, DMR value, exceedance date or outcome window may be opened.

F01 does not yet choose an exposure window, follow-up window, lag, censoring rule, or experimental cohort.

## Frozen structural measurements / 고정 구조 측정

F01 may compute and persist only:

### RCRA Pipeline
- ZIP bytes/hash and member-name fingerprint;
- evaluation row count;
- required-header presence;
- count of rows with valid `SOURCE_ID × REGISTRY_ID × EVAL_DATE`;
- distinct RCRA `SOURCE_ID` count;
- distinct RCRA `REGISTRY_ID` count;
- distinct valid evaluation years;
- count of source IDs mapping to exactly one vs conflicting Registry ID;
- deterministic SHA-256 fingerprints of sorted exact identity sets.

### FRS Program Links
- ZIP bytes/hash and member-name fingerprint;
- row count;
- required-header presence;
- distinct exact RCRAInfo program IDs and NPDES program IDs with one nonblank Registry ID;
- count of conflicting program-record→Registry mappings;
- distinct Registry IDs for each program family;
- exact cross-program Registry-ID intersection size;
- deterministic SHA-256 fingerprints of relevant sorted sets/intersections.

### ICIS-NPDES Part 1
- ZIP bytes/hash and member-name fingerprint;
- facility and permit row counts;
- required-header presence;
- distinct valid NPDES facility/permit IDs;
- distinct nonblank `FACILITY_UIN` values;
- NPDES ID→Registry cardinality/conflict diagnostics;
- valid structural permit-date years only;
- deterministic SHA-256 fingerprints of exact identity sets.

### Cross-source
- RCRA Pipeline identities exactly corroborated by FRS RCRAInfo links;
- NPDES Part 1 identities exactly corroborated by FRS NPDES links;
- distinct exact Registry IDs supported on both RCRA and NPDES sides;
- number of exact cross-program Registry IDs with at least one valid RCRA evaluation date and at least one NPDES Part 1 permit/facility record;
- agreement/coverage rates and sorted-set SHA-256 fingerprints;
- aggregate counts only; no facility-level outcome table or ranking may be persisted.

## Frozen PASS requirements / 고정 PASS 요건

All must pass:

1. Current official EPA documentation for RCRA Pipeline, FRS Download, and ICIS-NPDES Download is reachable or the corresponding official downloadable source bytes are successfully readable.
2. The three authorized official ZIPs (`pipeline_rcra_downloads.zip`, `frs_downloads.zip`, `npdes_downloads.zip`) are readable, valid ZIP archives and fingerprinted at zero incremental monetary cost.
3. RCRA Pipeline exposes `REGISTRY_ID`, `SOURCE_ID`, `EVAL_DATE` in `PIPELINE_RCRA_01_EVALUATIONS.csv`.
4. At least **5,000 distinct valid RCRA SOURCE_IDs** and **5,000 distinct valid RCRA REGISTRY_IDs** are present in the evaluation structure.
5. RCRA structural evaluation support spans at least **10 distinct calendar years** and reaches at least **2025**.
6. FRS Program Links exposes `PGM_SYS_ACRNM`, `PGM_SYS_ID`, `REGISTRY_ID` and contains exact program families corresponding to RCRAInfo and NPDES.
7. At least **90%** of distinct RCRA Pipeline `SOURCE_ID × REGISTRY_ID` exact pairs are corroborated by a non-conflicting exact FRS RCRAInfo program linkage, measured on pairs whose program IDs are represented in FRS.
8. ICIS-NPDES Part 1 exposes `NPDES_ID`, `FACILITY_UIN` in `ICIS_FACILITIES.csv` and `EXTERNAL_PERMIT_NMBR` plus structural permit dates in `ICIS_PERMITS.csv`.
9. At least **10,000 distinct valid NPDES IDs** and **10,000 distinct nonblank NPDES-side Registry IDs** are present in Part 1 facility structure.
10. At least **90%** of non-conflicting `NPDES_ID × FACILITY_UIN` exact pairs represented in FRS are corroborated by exact FRS NPDES program linkage.
11. NPDES structural permit-date support spans at least **10 distinct calendar years**.
12. At least **500 distinct exact FRS REGISTRY_IDs** occur in the RCRAInfo↔NPDES program-family intersection.
13. At least **500 distinct exact FRS REGISTRY_IDs** are simultaneously supported by: (a) a valid RCRA Pipeline evaluation identity/date, (b) a non-conflicting FRS RCRAInfo link, (c) a non-conflicting FRS NPDES link, and (d) an ICIS-NPDES Part 1 facility/permit identity.
14. No name/address/geospatial/corporate-parent/fuzzy/manual/post-outcome identity repair is used.
15. Deterministic SHA-256 fingerprints are persisted for the RCRA exact identity set, FRS RCRAInfo set, FRS NPDES set, NPDES Part 1 identity set, and exact cross-program Registry-ID intersections.
16. `effluent_violation_rows_opened = false`, `dmr_outcome_rows_opened = false`, and no Part 2 or jurisdictional effluent-violation source is accessed by the F01 runner.
17. No RCRA-conditioned NPDES occurrence, rate, magnitude, pollutant, exceedance, violation count, facility ranking, effect estimate, prediction, regression, correlation or causal quantity is computed or persisted.
18. `relationship_computed = false`, `predictive_metric_computed = false`, `causal_claim_made = false`, and incremental monetary cost = **0 USD**.

## Frozen dispositions / 고정 판정

### PASS

`PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY`

Use only if all 18 requirements pass.

### HOLD

`HOLD_US_EPA_XMEDIA_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY`

Use after a valid evaluation when any preregistered source/schema/native-identity/time/cardinality/coverage requirement fails.

### Implementation failure

A transient network error, server timeout, ZIP transfer interruption, decompression defect, filename casing variation, parser defect or GitHub Actions implementation defect that prevents a valid evaluation is **not** scientific HOLD. Preserve the failed run, correct only implementation mechanics without changing this contract, and rerun.

A source product changing in a way that removes a frozen required semantic field is a valid scientific/operability HOLD, not an invitation to substitute unofficial data.

## Outcome-blind prohibitions / 결과 비개봉 금지사항

F01 may not download/read/query/open/persist or derive:
- `NPDES_EFF_VIOLATIONS.csv` or Part 2 effluent-violation rows;
- jurisdictional effluent-violation files;
- DMR reported values, permit limits, exceedance flags or pollutant measurements;
- RCRA-conditioned NPDES violation/event membership;
- future effluent-exceedance occurrence for any RCRA facility;
- facility risk scores, ranks or risk classes;
- regression/correlation/effect/prediction/causal statistics;
- a repaired identity chosen after observing downstream outcome support.

## Exact next action / 정확한 다음 행동

Bind this already-frozen contract to one dedicated Issue. Then create a separate activation decision and canonical active-state mirrors. Only after activation may the official-source-only runner download the three authorized ZIPs and evaluate the 18 frozen structural requirements. Part 2 effluent violations and DMR outcome rows must remain unopened.

Incremental monetary cost remains **0 USD**.
