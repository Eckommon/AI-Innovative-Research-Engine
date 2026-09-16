---
id: US-FMCSA-HAZ-F01-RESULT
type: outcome-blind-source-schema-carrier-time-feasibility
created: 2026-09-16
issue: 145
state: COMPLETED_PARTIAL
gate: PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED
source_run: 35057953144
hazmat_incident_occurrence_by_inspection_profile_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FMCSA-HAZ-F01 Result — PHMSA-export access-limited PARTIAL

**`PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED`**

Corrected Run `35057953144` validly executes the frozen outcome-blind FMCSA inspection × PHMSA highway hazmat source/schema/carrier-time gate using official DOT/FMCSA/PHMSA routes only.

## FMCSA empirical support / FMCSA 실증 지원

The frozen FMCSA side passes its prospective structural requirements:

- native carrier identity: `dot_number` → exact numeric USDOT canonicalization;
- distinct valid USDOT carriers: **662,705** (threshold >=50,000);
- valid inspection rows / distinct inspection IDs: **8,302,114**;
- repeated-inspection carriers: **471,908**;
- native `insp_date` is source text, parsed deterministically by exact-value weighted parsing;
- date parseability: **100% = 8,302,114 / 8,302,114**;
- supported years: **2023–2026, 4 years** (threshold >=3);
- violation rows: **13,536,445**;
- violation rows with inspection ID: **13,536,445 = 100%**;
- distinct violation inspection IDs: **4,592,338**;
- OOS/inspection linkage is structurally available and deterministic;
- FMCSA carrier fingerprint: `3d249b6c14e182d5d1757600f67e73b1140703b85dffaa5880f490268317c0eb`.

## PHMSA access-only blocker / PHMSA 접근 전용 장벽

Official PHMSA catalog/dictionary semantics are reachable and document the public detailed incident export path, but the frozen zero-cost runner cannot retrieve the Oracle detailed-export bytes. Therefore the byte-dependent PHMSA requirements remain **uncomputed rather than failed**:

- detailed export schema presence;
- >=500 distinct Highway FED DOT IDs;
- >=95% incident-date parseability and >=10 years;
- exact FMCSA USDOT ↔ PHMSA FED DOT intersection >=300;
- PHMSA and intersection identity fingerprints.

The preregistered PARTIAL explicitly applies only when all FMCSA empirical requirements pass, PHMSA semantics pass, and the sole remaining blocker is official PHMSA export-byte access. Run `35057953144` satisfies exactly that condition.

## Preserved implementation history / 구현 비적합 보존

- Run `35045639924`: native `dot_number` alias was not mapped; execution invalid for gate.
- Run `35057504925`: `insp_date` was correctly identified as text, but inherited date support did not parse text values and therefore incorrectly produced zero supported years; not accepted as terminal scientific disposition.
- Run `35057953144`: same source/field/thresholds, deterministic weighted text-date parsing only; valid PARTIAL.

No threshold, source identity, carrier join rule or outcome boundary was changed during these corrections.

## Outcome-blind boundary / outcome 비개봉 경계

- hazmat incident occurrence/rate/count by FMCSA inspection/violation/OOS profile: **not opened**;
- future incident membership conditioned on FMCSA profile: **not opened**;
- carrier-level FMCSA↔PHMSA joined membership: **not persisted**;
- relationship/prediction: **not computed**;
- causal or federal safety-rating claim: **not made**;
- unofficial mirror/authentication bypass: **not used**;
- incremental monetary cost: **0 USD**.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve `US-FMCSA-HAZ-001` as an access-blocked asset. Do not substitute unofficial PHMSA incident files, infer the uncomputed carrier intersection, or redesign the branch from observed outcomes. Re-entry is allowed only if the official PHMSA detailed export becomes executable at zero incremental cost or a later independent prospective portfolio decision reselects the branch.
