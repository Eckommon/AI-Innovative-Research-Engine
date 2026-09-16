---
id: US-NHTSA-MC-F01-RESULT
type: outcome-blind-source-schema-product-time-feasibility
created: 2026-09-16
issue: 143
state: COMPLETED_HOLD
gate: HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY
recall_incidence_opened: false
future_recall_membership_conditioned_on_communications_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-NHTSA-MC-F01 Result — source/schema HOLD

**`HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY`**

Corrected Run `35043099657` validly evaluated the frozen official NHTSA Manufacturer Communications × Safety Recall source/schema/product-time gate. The two earlier runs (`35042810534`, `35042957163`) remain preserved as implementation-invalid and do not contribute scientific dispositions.

## Strong structural support that passed / 통과한 구조적 지원

The frozen source family is large and the exact product identity itself is viable:

- Manufacturer Communications valid product rows: **182,795**
- Manufacturer Communications distinct product keys: **13,729** (>=10,000 required)
- Manufacturer Communications normalized makes: **347** (>=25 required)
- distinct communication document IDs: **49,044**
- product keys with multiple communication documents: **9,640**
- maximum communication documents on one product key: **817**
- Safety Recall distinct product keys: **40,700** (>=5,000 required)
- Safety Recall normalized makes: **1,007**
- Safety Recall date support: **17 years**, parse rate **1.0000**
- exact normalized aggregate product-key intersection: **8,263** (>=1,000 required)

Identity fingerprints were frozen before any descendant outcome authorization:
- communication product keys: `6f6644d254ffa1e180769032fde60a369e01f3acf46a0fcf849f0abf0947b6a6`
- recall product keys: `c32673c583c1eed32b432b007dcbddf05fc7bdb2203197c43b4a0a976d4272fa`
- exact intersection: `1f69c366390c6b5be331bee725c786c1c7d24ce54cf5ba127286f45290d12649`

## Frozen requirements that fail / 실패한 사전고정 요건

### 1. Frozen Manufacturer Communications CSV lacks a communication date field

Both frozen official ZIPs are readable and each contains a CSV with exactly these observed fields:

`TSB/Document ID, Make, Model, Model Year, Concise Summary`

The files therefore support deterministic document × product identity, but they expose neither `Mfr Communication Date` nor `Date Added to File`. Under the preregistered F01 contract, communication-time support was mandatory. Consequently:

- full frozen communication schema: **FAIL**
- communication date years: **0 / >=5 required**
- communication date parse rate: **0 / >=95% required**

The broader NHTSA dictionary documents richer fields, but F01 froze the CSV ZIPs before execution. Switching post hoc to a richer TSV/flat-file source would be a source redesign and is not permitted in this branch.

### 2. NHTSA catalog HTML returns HTTP 403 to the zero-cost GitHub runner

The frozen static NHTSA dictionaries and all three frozen ZIPs return HTTP 200, but the separately frozen NHTSA catalog page returns **HTTP 403** even with an ordinary unauthenticated browser User-Agent. The F01 PASS contract required the catalog page and dictionaries to be reachable from the runner, so that requirement also fails.

## Outcome-blind boundary / outcome 비개봉 경계

- recall incidence/rate/count by communication-derived group: **not opened**
- per-product future-recall membership conditional on communication history: **not opened**
- relationship/predictive statistic: **not computed**
- causal claim: **not made**
- unofficial mirror/authentication bypass: **not used**
- incremental monetary cost: **0 USD**

The aggregate 8,263-key source intersection is an identity-support count only; it is not a communication-conditioned recall outcome.

## Interpretation / 해석

This HOLD does **not** show that Manufacturer Communications are uninformative about recalls. It means the **specific prospectively frozen F01 source package** cannot satisfy its own time/schema/access contract. The branch is therefore terminal without switching sources after support was observed.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Do not rescue this branch by replacing the frozen CSVs with richer TSV/flat files. A future communication-time design is allowed only if a new independent portfolio decision prospectively selects the richer source family before its support is inspected.

Incremental monetary cost remains **0 USD**.
