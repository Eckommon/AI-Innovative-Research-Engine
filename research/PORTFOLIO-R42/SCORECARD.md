---
id: PORTFOLIO-R42-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-28
issue: 170
contract: 3defb5494bee758cf671ef358599a4e50c60161c
revalidation: b74d267ab7c006062004e470abcb18cc7fef6c0f
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R42 — immutable /45 scorecard

This is the single scorecard authorized by the frozen R42 contract. Scores may not be changed after this commit.

| Dimension / 기준 | UK-CQC-LOC-001 | US-BSEE-OCS-001 | US-SAM-ENTITY-001 | UK-OFSTED-URN-001 |
|---|---:|---:|---:|---:|
| 1. Mission bottleneck fit | 5 | 5 | 4 | 4 |
| 2. Cross-dataset / cross-table information gain | 4 | 4 | 4 | 4 |
| 3. Direct future-event quality | 3 | 5 | 5 | 4 |
| 4. Independent-unit prospect | 5 | 4 | 5 | 5 |
| 5. Practical decision value | 5 | 5 | 5 | 5 |
| 6. Zero-cost operability | 5 | 5 | 3 | 5 |
| 7. Source-native/deterministic join defensibility | 5 | 3 | 5 | 5 |
| 8. Next-gate information gain | 5 | 5 | 4 | 4 |
| 9. Low overlap / novelty risk | 3 | 4 | 3 | 1 |
| **Total /45** | **40** | **40** | **38** | **37** |

## Frozen tie-break / 고정 동점규칙 적용

CQC and BSEE tie at **40/45**.

Frozen tie-break #1 is source-native/deterministic join defensibility:

- `UK-CQC-LOC-001`: **5**
- `US-BSEE-OCS-001`: **3**

Therefore the tie resolves immediately in favor of CQC.

## Candidate rationales / 후보별 근거

### UK-CQC-LOC-001 — 40/45 — SELECT_F01

- Exact CQC Location ID and public active/inactive location architecture are strong.
- Monthly care-directory/rating and deactivated-location files make zero-cost historical/current structural testing practical.
- Future-event quality is capped at 3 because CQC explicitly states that deactivation/archive does not necessarily mean service closure.
- That ambiguity raises rather than lowers next-gate information value: one F01 can sharply determine whether registration-end/deactivation mechanisms are separable enough for a later prospective design.
- No closure or quality-risk novelty claim is made.

### US-BSEE-OCS-001 — 40/45 — HOLD_TIEBREAK_INCIDENT_IDENTITY_UNCERTAINTY

- Public-safety value and direct physical incident quality are high.
- BSEE Complex ID is strong on the platform side, but exact incident-side Complex-ID/structure continuity is not yet established across the public annual incident files.
- The frozen tie-break therefore places BSEE behind CQC despite equal total score.

### US-SAM-ENTITY-001 — 38/45 — HOLD_OPERATIONAL_ACCESS_AND_SNAPSHOT_RISK

- Exact UEI and direct exclusion semantics are excellent.
- Current API/data-service handling may involve API-key/sign-in requirements; historical entity snapshot lineage and exclusion-event support are still uncertain.
- Operational-access risk reduces zero-cost operability and next-gate value relative to CQC/BSEE.

### UK-OFSTED-URN-001 — 37/45 — HOLD_MATURE_CLOSURE_AND_HIGH_OVERLAP

- Exact URN and GIAS closure fields are structurally strong.
- Generic inspection/closure research is mature, and academy conversion/reorganization complicates closure interpretation.
- Prior NCES school-closure candidate creates additional conceptual overlap, so novelty credit is minimal.

## Frozen selection / 고정 선정

**`SELECT_UK_CQC_LOC_001_RATING_SERVICE_STRUCTURE_TO_REGISTRATION_END_F01`**

## Authorized next gate / 허가되는 다음 gate

Exactly one separate outcome-blind `UK-CQC-LOC-F01` may be designed next. Before any post-baseline inactive/deactivated membership is opened, F01 must prove or reject:

1. exact CQC Location ID syntax and continuity across historical rating/directory and inactive/deactivated sources;
2. current zero-cost downloadable source access without paid subscription;
3. historical snapshot lineage and deterministic fingerprints;
4. registration start/end and active/inactive semantics;
5. whether deactivation/archiving reason or linked-organization metadata can prospectively separate true service cessation from re-registration/legal-structure/address changes;
6. sufficient independent active-location and historical deactivated-location support;
7. mechanically sealed future inactive/deactivated membership.

If reason semantics cannot distinguish closure-like cessation from administrative re-registration/change, F01 must HOLD rather than label all deactivations as closures.

## Non-claims / 비주장

The scorecard establishes no CQC closure relationship, BSEE incident relationship, SAM exclusion relationship, school-closure relationship, prediction, ranking, causal effect or novelty claim.

Incremental monetary cost: **0 USD**.
