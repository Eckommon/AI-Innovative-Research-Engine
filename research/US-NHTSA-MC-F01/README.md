---
id: US-NHTSA-MC-F01
type: outcome-blind-source-schema-product-identity-feasibility
created: 2026-09-16
state: CONTRACT_FROZEN_AWAITING_ISSUE_BINDING
parent: PORTFOLIO-R31
parent_decision: DEC-197
recall_incidence_opened: false
future_recall_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-NHTSA-MC-F01 — outcome-blind Manufacturer Communications × Recall source/schema/product/time feasibility

## Authorization boundary / 승인 경계

This is the only Stage-0 descendant authorized by `PORTFOLIO-R31 = SELECT_US_NHTSA_MC_001_COMMUNICATION_TO_RECALL_F01` / DEC-197.

F01 tests only:
- official source access;
- published field/schema semantics;
- deterministic product identity;
- source-native communication/recall row identity;
- repeated-row/multiplicity structure;
- date parsing/support;
- aggregate cross-source product-key overlap and SHA-256 fingerprints.

F01 must **not** compute or persist:
- recall incidence/rate/count by communication type, component, bulletin count, communication frequency, manufacturer, make, model, or any proposed exposure group;
- per-product future-recall membership conditional on communication history;
- coefficient, risk ratio, predictive score, ranking, causal estimate, or relationship direction.

## Frozen official sources / 고정 공식 source

### Manufacturer Communications

Official dataset family:
- NHTSA Manufacturer Communications / Technical Service Bulletin flat-file downloads.

Frozen execution files:
- `https://static.nhtsa.gov/odi/ffdd/tsbs/MFR_COMMS_RECEIVED_2020-2024.zip`
- `https://static.nhtsa.gov/odi/ffdd/tsbs/MFR_COMMS_RECEIVED_2025-2026.zip`
- dictionary/semantics: `https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS.txt`
- catalog page: `https://www.nhtsa.gov/nhtsa-datasets-and-apis`

NHTSA states the CSV communication file contains one record per TSB/Document ID per product (Make, Model, Model Year), while the richer TSV/flat file may repeat records across multi-valued elements. F01 may quantify this structure but may not turn component/type fields into an exposure.

### Safety Recalls

Frozen execution files:
- `https://static.nhtsa.gov/odi/ffdd/rcl/FLAT_RCL_POST_2010.zip`
- dictionary: `https://static.nhtsa.gov/odi/ffdd/rcl/RCL.txt`
- catalog/API documentation: `https://www.nhtsa.gov/nhtsa-datasets-and-apis`

Recall source is used only for schema, product identity, campaign identity, date support and aggregate product-key overlap in F01.

## Frozen deterministic product identity / 고정 product identity

Product identity is exactly:

`(Model Year, normalized Make, normalized Model)`

Normalization is fixed before source execution:
1. Unicode NFKC;
2. trim leading/trailing whitespace;
3. collapse each internal whitespace run to one ASCII space;
4. uppercase;
5. preserve punctuation, digits and all other non-whitespace characters exactly;
6. no manufacturer aliases, model aliases, token deletion, punctuation deletion, edit distance, embeddings, fuzzy matching or hand repair.

Model Year must be exactly four decimal digits and must not equal `9999`. Invalid/unknown product identities are excluded, not repaired.

## Frozen row identities / 고정 row identity

### Communication row

Use source-native communication/document identity plus product key. Prefer current source header semantics for:
- NHTSA ID Number;
- TSB/Document ID;
- Mfr Communication Date or Date Added to File;
- Make;
- Model;
- Model Year.

Exact duplicated rows may be collapsed. Conflicting source-native communication IDs are not manually repaired.

### Recall row

Use source-native NHTSA campaign identity plus product key. The runner must verify the current RCL dictionary and actual flat-file field positions/header semantics before use. It may use campaign number and report/record date only after source documentation confirms their meaning.

No recall defect/consequence text is used in F01.

## Frozen F01 PASS requirements / 고정 PASS 요건

Full PASS requires all:

1. NHTSA catalog page, Manufacturer Communications dictionary and Recall dictionary are reachable from the zero-cost runner and source metadata/content hashes are persisted.
2. Both frozen Manufacturer Communications ZIPs and `FLAT_RCL_POST_2010.zip` are downloadable from official NHTSA hosts, readable and hashed; raw source bytes are transient and not committed.
3. Communication bytes expose source-native communication/document identity, communication/addition date, Make, Model and Model Year sufficient to form the frozen product identity without inferred aliases.
4. Recall bytes/dictionary expose source-native campaign identity, documented recall date identity, Make, Model and Model Year sufficient to form the same frozen product identity.
5. After only the frozen normalization/exclusion rules, Manufacturer Communications contain >= **10,000 distinct valid product keys**.
6. Safety Recalls contain >= **5,000 distinct valid product keys**.
7. Each source contains >= **25 distinct normalized Makes** among valid product keys.
8. Exact normalized aggregate product-key intersection contains >= **1,000 distinct product keys**. This is identity support only; F01 must not derive future-recall membership conditional on communication history.
9. Communication date support spans >= **5 distinct calendar years** and >= **95%** of structurally eligible communication rows have a parseable allowed source date. Recall date support spans >= **10 distinct calendar years** and >= **95%** of structurally eligible recall rows have a parseable documented recall date.
10. Communication/document multiplicity by product and repeated product rows are quantified structurally; no communication type/component subset is selected based on recall support.
11. SHA-256 fingerprints are persisted for sorted distinct communication product keys, recall product keys and their aggregate intersection before any descendant outcome authorization.
12. No recall incidence/rate/count by any communication-derived grouping, no per-product future-recall membership conditioned on communications, no relationship/predictive statistic, no causal claim, no unofficial mirror, and no paid source/service; incremental monetary cost remains **0 USD**.

## Frozen dispositions / 고정 판정

### `PASS_US_NHTSA_MC_F01_PRODUCT_TIME_JOIN_READY`
All twelve requirements pass.

### `HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY`
Any structural/source/schema/product-identity/date/overlap requirement fails after valid execution.

A transient workflow/runtime/download implementation failure that prevents valid evaluation is **not** automatically a scientific HOLD. It must be recorded and corrected without changing the frozen source files, normalization, thresholds or outcome boundary.

## Claim boundary / 주장 경계

PASS means only that current official NHTSA public files support a deterministic, sufficiently large product/time identity bridge for a later separately preregistered non-causal design. It does **not** establish that TSBs or manufacturer communications predict recalls, that any communication category is higher risk, novelty, or causality.

NHTSA's own use of manufacturer communications in Early Warning Reporting and defect analysis remains an explicit overlap constraint.

Incremental monetary cost: **0 USD**.


## Final disposition / 최종 처분

Corrected Run `35043099657` validly resolves **`HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY`**. Product-key cardinality and aggregate exact overlap are strong, but the two prospectively frozen Manufacturer Communications CSV files lack any communication/addition date field and the frozen catalog HTML returns HTTP 403 to the zero-cost runner. The branch is terminal without switching post hoc to a richer TSV source. Recall incidence and relationship remain unopened.
