---
id: US-MINE-F01-RESULT
type: outcome-blind-structural-feasibility
created: 2026-09-16
issue: 134
workflow_run: 35003865979
superseded_implementation_run: 35003705306
gate: PASS_US_MINE_F01_STRUCTURAL_JOIN_READY__PRODUCTION_SCOPE_RESTRICTED
incremental_monetary_cost_usd: 0
---

# US-MINE-F01 Result / 결과

**`PASS_US_MINE_F01_STRUCTURAL_JOIN_READY__PRODUCTION_SCOPE_RESTRICTED`**

## Outcome-blind integrity / 결과 비개봉 무결성

- Frozen support window: **2019–2025**.
- Injury outcome values opened: **NO**.
- Prohibited accident outcome fields selected/accessed: **NO**.
- Exposure→injury relationship computed: **NO**.
- Hours-worked magnitude parsed: **NO**.
- Coal-production magnitude parsed: **NO**.
- Raw source bytes persisted: **NO**.
- Post-execution threshold/source/window rescue: **NO**.
- Incremental monetary cost: **0 USD**.

## Frozen structural result / 고정 구조 결과

- Mines snapshot: **92,007** distinct `MINE_ID`; duplicate/conflicting IDs **0 / 0**.
- 2019–2025 operator employment: **663,020** exact `(MINE_ID, CAL_YR, CAL_QTR, SUBUNIT_CD)` keys; conflicting duplicates **0**.
- Mines with >=2 distinct quarters: **17,060**.
- `HOURS_WORKED` nonblank support: Coal **100.000000%**, Metal/Nonmetal **99.999342%**.
- Operator-attributed accident structural keys: **21,491**.
- Exact employment-key overlap: **21,426 / 21,491 = 99.6975%**.
- Overlapping mine IDs: **4,882** across **53 states**.
- Duplicate accident `DOCUMENT_NO`: **0**.

## Production-scope boundary / 생산량 범위 경계

PASS does **not** establish a nationally comparable Coal+Metal/Nonmetal production-pressure exposure. The preregistered MSHA semantic restriction remains binding: Metal/Nonmetal operators are not required to report production. The observed nonblank support does not override that reporting-rule asymmetry. `PRODUCTION_SCOPE_RESTRICTED` is therefore part of the PASS state.

## Superseded implementation run / 대체된 구현 실행

Run `35003705306` is preserved as an implementation nonconformity. It produced the same substantive source/support evidence but mislabeled the gate as PARTIAL because two correctly false diagnostics (`prohibited_outcome_fields_accessed=false`, `relationship_computed=false`) were passed into `all()`. Run `35003865979` changed only those predicates to positive compliance form and re-executed the **same preregistered contract** with exact source-manifest stability. No scientific threshold, source, window or identity rule changed.

## Interpretation boundary / 해석 경계

This PASS establishes only deterministic source/schema/time/key structural readiness. It does **not** show that operational stress predicts or causes mine injuries and does not authorize any injury-rate, injury-severity or exposure-effect claim.

## Exact next action / 정확한 다음 행동

Open only a separately preregistered **US-MINE-N01 outcome-blind design gate**. N01 must choose exactly one exposure family from source semantics/support before any injury outcome is opened, while preserving `PRODUCTION_SCOPE_RESTRICTED`. Do not auto-select coal-only production or all-sector employee-hours from accident outcomes.

Incremental monetary cost remains **0 USD**.
