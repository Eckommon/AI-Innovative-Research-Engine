---
id: US-EPA-RCRA-N01-RESULT
type: prospective-design-result
created: 2026-10-08
issue: 199
research: US-EPA-RCRA-N01
disposition: HOLD
contract_commit: 14b9509808bcfd9a6affc694ec97531105d8ca41
attempt_01_commit: 3cb5290fdce4a373a74b228059f4c913f0d1589b
attempt_01_run: 37670426503
incremental_monetary_cost_usd: 0
---

# US-EPA-RCRA-N01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_EPA_RCRA_N01_MULTI_NAICS_MATCHED_COHORT_NOT_READY`**

Attempt 01 is a valid outcome-blind prospective-design execution and passes **13/18** frozen gates. Failed gates are **6, 7, 8, 11 and 15**.

No future RCRAInfo refresh was opened. No `FOUND_VIOLATION` value was consumed.

## Frozen-cohort evidence / 고정 cohort 근거

- baseline SHA matched F01 exactly
- eligible handlers: **23,599** vs frozen minimum 100,000
- `MULTI_NAICS` exposed: **2,418** vs minimum 20,000
- `SINGLE_NAICS` controls: **21,181** vs minimum 40,000
- common exact strata: **691** vs minimum 200
- deterministic matched pairs: **1,728** vs minimum 20,000
- exposed match coverage: **71.4640%** vs minimum 40%
- X1 balance |SMD|: **0.00312**
- X2 balance |SMD|: **0.00196**
- exact-stratum mismatch: **0**
- duplicate comparator use: **0**
- caliper failures among accepted pairs: **0**
- recent evaluation-opportunity support: **703 matched handlers total** (348 exposed / 355 control), below frozen 5,000 total / 1,500 per arm

## Interpretation / 해석

The failure is **support**, not matching quality.

The multi-NAICS exposure produced excellent common-support quality among the units that could be matched, but the exposed arm and recent future-evaluation opportunity proxy are too sparse for the prospectively required study scale.

This exact N01 may not be rescued by:
- lowering cohort/arm/pair thresholds;
- redefining multi-NAICS;
- dropping the five-year evaluation-opportunity eligibility rule;
- widening future opportunity assumptions;
- relaxing exact strata or calipers;
- using historical violation/SNC/enforcement information as exposure;
- opening future refreshes.

## Firewall / 방화벽

- later weekly refresh opened: **false**
- future outcome membership opened: **false**
- `FOUND_VIOLATION` values consumed: **0**
- forbidden outcome tables opened: **0**
- relationship/prediction/ranking/causal metric: **false**
- identity repair: **false**
- cost: **0 USD**

## Consequence / 후속 조치

Do not authorize `US-EPA-RCRA-E01`.

Return to independent Stage-0 portfolio reselection. Preserve the result as reusable negative evidence:

> RCRAInfo is structurally excellent, but the exact **multi-NAICS + recently evaluated** prospective design lacks sufficient population and observation-opportunity support despite very good matching balance.

Incremental monetary cost: **0 USD**.
