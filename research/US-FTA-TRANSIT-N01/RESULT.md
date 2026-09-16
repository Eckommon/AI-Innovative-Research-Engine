---
id: US-FTA-TRANSIT-N01-RESULT
type: outcome-blind-matched-reliability-design-identifiability
created: 2026-09-17
issue: 148
state: COMPLETED_HOLD
gate: HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE
source_run: 35138272269
staging_commit: d8d244fc2a3d8b5f7ca47a9c2dc9863b7c6a159d
major_safety_event_row_values_opened: false
future_safety_event_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-N01 Result — frozen matched-design HOLD

**`HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE`**

Run `35138272269` validly executed the preregistered N01 contract against official FTA Annual Breakdowns only. The design retains substantial support, but **3 of 17 frozen PASS requirements fail**, so the branch is terminal at HOLD without threshold, stratum, mode, matching, or balance rescue.

## What passed / 통과한 지원

- actual official Breakdowns rows read: **3,731**;
- canonical source-grain keys: **3,731**;
- conflicting source-grain keys: **0**;
- quality-invalid agency-mode-years excluded fail-closed: **93**;
- unique retained agencies after temporal eligibility and one-unit-per-agency: **514** (required >=400);
- deterministic matched pairs: **103** (required >=100);
- every matched HIGH intensity is strictly above its LOW counterpart: **PASS**;
- no NTD ID is reused in the final manifest: **PASS**;
- immutable outcome-blind manifest SHA-256: `7968b839b5b00bc9bdc3df2cf541c13205c66301967d77c54343575d297f2ef1`.

## Frozen requirements that fail / 실패한 사전고정 요건

1. **Design-eligible strata:** 6 < 8 required. Of 34 total strata, 28 were below the frozen n>=12 support floor.
2. **Matched mode diversity:** 3 modes `DR, MB, VP` < 5 required.
3. **VRM balance:** 73/103 = **70.87%** < 80% required for both exposure-year and follow-up-year HIGH:LOW VRM ratios to fall in [1/3, 3].

These failures are not implementation defects. They arise under the exact preregistered design and therefore cannot be repaired post hoc by lowering the strata threshold, pooling modes, changing quartiles, relaxing balance, or rematching after inspecting support.

## Outcome-blind boundary / 결과 비개봉 경계

- Major Safety/Security Event row values: **not opened**;
- next-year Safety-event membership: **not opened**;
- Breakdown→event row join: **not persisted**;
- relationship/predictive statistic: **not computed**;
- agency safety ranking: **not computed**;
- causal claim: **not made**;
- fuzzy/manual identity repair: **not used**;
- incremental monetary cost: **0 USD**.

The 103-pair manifest remains durable only as an audit artifact of the failed preregistered design. It does **not** authorize E01 because N01 did not pass.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve `US-FTA-TRANSIT-001` as a structurally promising but N01-insufficient asset. Do not open the prospectively defined E01 safety outcome, and do not rescue this branch by changing the frozen N01 design after observing support. A later redesign is permitted only through a new independent prospective portfolio decision.
