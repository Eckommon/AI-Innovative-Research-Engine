---
id: US-FCC-ULS-F01-PRECONTRACT-DISCLOSURE
type: precontract-observation-boundary
created: 2026-09-18
parent: PORTFOLIO-R40
future_baseline_snapshot_opened: false
future_daily_transaction_body_opened: false
incremental_monetary_cost_usd: 0
---

# US-FCC-ULS-F01 pre-contract observation disclosure / 계약 전 관측 공개

## Purpose / 목적

Preserve research transparency before the F01 contract is frozen.

During post-R40 official-source research, web search snippets from FCC **Termination Pending Public Notices** displayed a small number of historical example rows for radio service `IG — Industrial/Business Pool, Conventional`, including notices from historical calendar years such as 2019, 2022 and 2025.

These examples were **not**:

- joined to any ULS complete-file baseline;
- counted to estimate an IG event rate;
- used to select `US-FCC-ULS-001` in R40;
- used in the R40 /45 scorecard;
- used to set a support threshold, effect threshold, matching rule or outcome horizon;
- retrieved by querying a known historical baseline license/system identifier;
- used to compute any exposure→outcome association.

R40 had already selected the ULS family from source-native identity, public-file architecture and next-gate falsifiability. The prospective F01 service family `IG` is chosen from the official FCC radio-service taxonomy and site-based Land Mobile structure, not from observed termination counts.

## Consequence for temporal firewall / 시간 방화벽 결과

To remove any possible contamination from historical examples, the descendant experiment will define a **new prospective baseline time `T0`** as the timestamp of the first valid F01 complete-file snapshot after the F01 Issue is bound to its frozen contract.

Only licenses that are exact `IG` and `License Status = A (Active)` at `T0` may enter the descendant baseline candidate universe.

A descendant future event can only occur **strictly after T0**. Historical cancellation, expiration, termination, Termination Pending notices, HS history rows, or other pre-T0 status events are not future outcomes. They may be used only for source/lineage integrity if a later frozen contract explicitly authorizes that use.

F01 itself may not download any daily transaction body. A body-free metadata request is permitted only to verify the documented future collection channel. Daily outcome collection remains unauthorized until a separate outcome-blind N01 has fixed its cohort/exposure/comparator and passed its own design gate.

## Current sealed state / 현재 봉인 상태

- ULS complete `Land Mobile - Private` baseline body opened under F01: **false**
- ULS daily transaction body opened under F01: **false**
- post-T0 cancellation/termination membership opened: **false**
- relationship computed: **false**
- predictive metric computed: **false**
- candidate ranking made: **false**
- incremental monetary cost: **0 USD**

This disclosure does not alter the R40 score or selection.
