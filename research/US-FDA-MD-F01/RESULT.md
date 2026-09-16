---
id: US-FDA-MD-F01-RESULT
type: outcome-blind-source-schema-identity-feasibility
created: 2026-09-16
issue: 141
state: COMPLETED_PARTIAL
gate: PARTIAL_US_FDA_MD_F01_SOURCE_SEMANTICS_READY__INSPECTION_BYTES_ACCESS_BLOCKED
recall_incidence_by_class_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FDA-MD-F01 Result — access-limited PARTIAL

**`PARTIAL_US_FDA_MD_F01_SOURCE_SEMANTICS_READY__INSPECTION_BYTES_ACCESS_BLOCKED`**

Run `35040935495` executed the preregistered FDA inspection × Device Recall source/schema/FEI gate using official FDA/openFDA routes only.

## What is established / 확립된 것

Official source semantics are structurally coherent for a future bounded FEI design:

- FDA FEI is documented as the unique establishment/facility identifier;
- final inspection classifications are `NAI`, `VAI`, `OAI`;
- one inspection may produce multiple Project Area rows;
- current CDRH guidance explicitly supports searching medical-device manufacturing facilities by FEI and filtering to medical-device inspection type;
- FDA explicitly states the public inspection database is not comprehensive;
- openFDA Device Recall documents native `firm_fei_number` plus initiated/created/posted event-date fields;
- the official openFDA bulk-download manifest is publicly executable and currently exposes the Device Recall source.

## Exact access blocker / 정확한 접근 장벽

The current FDA Inspections Dashboard itself is reachable, but both official inspection dataset links found/probed by the frozen runner return **HTTP 404**:

- `https://datadashboard.fda.gov/InspectionsDataset.xlsx`
- `https://datadashboard.fda.gov/oii/cd/InspectionsData-filtered.xlsx`

The Dashboard simultaneously documents that API credentials require **OII Unified Logon** authorization. No unofficial mirror, cached replica, alternate scraped dataset or authentication bypass was used.

Because actual inspection bytes are unavailable, the preregistered empirical byte-dependent requirements were **not calculable**, not scientifically failed:

- exact FEI/date/classification/native-device field presence in current bytes;
- structural-key classification conflicts;
- >=500 device-inspection FEIs;
- >=5 inspection years;
- repeated-inspection multiplicity;
- >=100 aggregate exact inspection-FEI ↔ recall-FEI overlap;
- FEI/intersection fingerprints.

The frozen PARTIAL disposition was specifically defined for this condition, so these unavailable checks must not be converted into a HOLD or rescued with nonofficial data.

## Outcome-blind boundary / outcome 비개봉 경계

- recall incidence/rate/count by NAI/VAI/OAI: **not opened**
- class-specific future-recall membership: **not opened**
- inspection→recall relationship/model: **not computed**
- population-wide manufacturer risk: **not claimed**
- unofficial mirror: **not used**
- authentication bypass: **not used**
- incremental monetary cost: **0 USD**

## Interpretation / 해석

This result means **source semantics are ready, but current official inspection bytes are access-blocked**. It does not establish that NAI/VAI/OAI predicts recall risk, and it does not justify any inspection-class ranking or causal interpretation.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve US-FDA-MD-001 as an access-blocked asset rather than redesigning it. It may be reconsidered only if the official public inspection download becomes functional, an authorized zero-cost official API credential becomes available, or a later independent portfolio decision prospectively reactivates the branch. Do not use unofficial substitutes.
