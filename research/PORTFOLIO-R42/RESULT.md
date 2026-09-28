---
id: PORTFOLIO-R42-RESULT
type: stage0-portfolio-selection
created: 2026-09-28
issue: 170
state: COMPLETED_SELECTED
selection: SELECT_UK_CQC_LOC_001_RATING_SERVICE_STRUCTURE_TO_REGISTRATION_END_F01
scorecard_commit: ed09c81b9c744ad1f7038a7dc9848447fd9c1bff
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R42 Result / 결과

**`SELECT_UK_CQC_LOC_001_RATING_SERVICE_STRUCTURE_TO_REGISTRATION_END_F01`**

R42 executed the candidate universe frozen before Issue binding at `3defb5494bee758cf671ef358599a4e50c60161c`, bounded revalidation at `b74d267ab7c006062004e470abcb18cc7fef6c0f`, and the single immutable scorecard at `ed09c81b9c744ad1f7038a7dc9848447fd9c1bff`.

## Immutable ranking / 불변 순위

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `UK-CQC-LOC-001` | **40** | **SELECT_F01 via tie-break #1** |
| `US-BSEE-OCS-001` | **40** | HOLD_TIEBREAK_INCIDENT_IDENTITY_UNCERTAINTY |
| `US-SAM-ENTITY-001` | **38** | HOLD_OPERATIONAL_ACCESS_AND_SNAPSHOT_RISK |
| `UK-OFSTED-URN-001` | **37** | HOLD_MATURE_CLOSURE_AND_HIGH_OVERLAP |

CQC and BSEE tied on total score. Frozen tie-break #1, source-native/deterministic join defensibility, selected CQC **5 > 3**.

## Why CQC / 선정 이유

CQC combines an explicit source-native Location ID with public active/inactive location information, registration start/end dates, monthly rating/directory files and deactivated-location data. Its decisive uncertainty is semantic rather than identity-based: CQC explicitly notes that archived/deactivated locations do not necessarily represent actual service closure.

That ambiguity is exactly the next F01 falsification target. F01 must determine whether current public source structure can separate true cessation-like registration ending from re-registration, legal-structure change or address change before any prospective outcome membership is opened.

## Authorized next work / 허가 범위

Exactly one separate outcome-blind `UK-CQC-LOC-F01` may be frozen next. It must prove or reject:

1. exact CQC Location ID syntax/coverage across current directory/rating/deactivated sources;
2. current zero-cost official downloadable source access;
3. historical snapshot/archive lineage;
4. active/inactive and registration start/end semantics;
5. source-native evidence sufficient to separate closure-like cessation from administrative re-registration/change;
6. independent location/cardinality support;
7. future inactive/deactivated membership firewall.

If source-native semantics do not permit defensible cessation/re-registration separation, F01 must HOLD rather than call all deactivations closures.

## Non-claims / 비주장

R42 establishes no CQC closure relationship, BSEE incident relationship, SAM exclusion relationship, school-closure relationship, prediction, ranking, causal effect or novelty claim. Candidate future-event membership remained unopened.

Incremental monetary cost: **0 USD**.
