---
id: US-FDIC-BRANCH-N01
type: outcome-blind-matched-design-identifiability
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FDIC-BRANCH-F01
parent_gate: PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY
future_outcome_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FDIC-BRANCH-N01 — outcome-blind matched branch network-position trajectory design

## Purpose / 목적

Determine, **before any 2025 SOD branch membership or future BankFind structure-event membership is opened**, whether the exact-`UNINUMBR` 2022–2024 branch panel can support one deterministic matched design comparing branches with stronger versus weaker within-bank, within-state deposit-network position trajectories.

N01 is a design-identifiability gate only. It may construct and persist an exposure/matching manifest from historical SOD 2022–2024. It may not open, count, infer, or condition on future closure/non-continuation outcomes.

This design does **not** claim generic low deposits → closure novelty. R38 already records that FDIC has published branch-closure analyses and lower-deposit closure patterns. The information target here is the longitudinal **within-network position trajectory** under exact physical-branch identity.

## Authorized official sources / 허가된 공식 소스

N01 may read only zero-cost official FDIC structural sources needed for the historical design:

1. FDIC Summary of Deposits (`SOD`) for **2022, 2023, 2024 only**;
2. official FDIC BankFind/API/OpenAPI metadata needed to validate variable semantics and source lineage;
3. the already-persisted F01 source preflight and immutable F01 evidence.

### Authorized historical SOD fields

- `YEAR`
- `CERT`
- `BRNUM`
- `UNINUMBR`
- `STALPBR`
- `DEPSUMBR`

No branch name, street address, ZIP, latitude/longitude, or fuzzy/geospatial identity field is needed or authorized for matching.

## Hard future-outcome firewall / 미래 outcome 방화벽

N01 must not open or query:

- any **2025 SOD data row or branch membership**;
- any future BankFind Location row used to determine whether a candidate branch survives;
- any 2024-07-01 through 2025-06-30 Bank Structure Change / History event membership for candidate branches;
- any branch closure/non-continuation indicator;
- any future branch-opening, relocation, purchase/assumption, sale/lease, merger, or closure event membership.

Required persisted booleans:

- `future_2025_sod_rows_opened: false`
- `future_branch_membership_opened: false`
- `future_structure_event_membership_opened: false`
- `future_closure_noncontinuation_computed: false`
- `fuzzy_name_address_zip_geo_manual_identity_repair_used: false`
- `relationship_computed: false`
- `predictive_metric_computed: false`
- `causal_claim_made: false`
- `branch_or_bank_ranking_made: false`
- `novelty_claim_made: false`

## Exact historical identity / 정확한 과거 식별

The unit is one exact physical branch `UNINUMBR`.

A branch is historically eligible only if:

1. the same nonblank exact `UNINUMBR` appears in **all three** SOD years 2022, 2023, and 2024;
2. `CERT`, `BRNUM`, `STALPBR`, and `DEPSUMBR` are nonblank in each year;
3. the exact `UNINUMBR` maps to exactly one row per year after exact duplicate collapse;
4. any conflicting same-year row for `UNINUMBR × YEAR` makes the branch ineligible fail-closed;
5. `CERT` is identical in 2022, 2023, and 2024 — historical ownership changes are excluded from this matched exposure design rather than repaired;
6. `STALPBR` is identical and nonblank in 2022 and 2024;
7. `DEPSUMBR` is numeric, finite, and strictly positive in both 2022 and 2024;
8. no name/address/ZIP/geospatial/fuzzy/manual identity repair is used.

The F01 finding of historical `CERT` changes is used only to justify this explicit exclusion rule. No future ownership/event membership is opened.

## Fixed temporal design / 고정 시간 설계

- baseline SOD date: **2022-06-30**
- intermediate SOD date: **2023-06-30**
- exposure/index SOD date: **2024-06-30**
- frozen future E01 outcome window: **2024-07-01 through 2025-06-30**
- one exact `UNINUMBR` may appear at most once in the final N01 pair manifest.

## Historical bank-state network strata / 과거 은행-주 네트워크 층

Define a historical stratum as exact:

`CERT_2024 × STALPBR_2024`

A stratum is eligible only if it has at least **8** historically eligible branches.

For each eligible branch-year, define the bank-state deposit share:

`share_y = DEPSUMBR_y / sum(DEPSUMBR_y over historically eligible branches in the same CERT × STALPBR stratum)`

Only the eligible stable-identity branch universe contributes to these denominators. This is a structural within-network measure, not a depositor-residence measure or geographic market-share claim.

## Frozen exposure: within-network position trajectory / 고정 exposure

For each eligible branch:

`delta_log_share = ln(share_2024 / share_2022)`

Within each eligible `CERT × STALPBR` stratum:

1. sort ascending by `(delta_log_share, UNINUMBR)`;
2. let `k = floor(n / 4)`;
3. `DECLINE` = first `k` branches — largest relative loss of within-bank/state deposit-network share;
4. `GAIN` = last `k` branches — largest relative gain of within-bank/state deposit-network share;
5. middle 50% is excluded;
6. require `max(delta_log_share in DECLINE) < min(delta_log_share in GAIN)`; otherwise drop the whole stratum.

No absolute-dollar cut point, percentile definition, time window, or stratum definition may change after N01 counts are observed.

## Frozen deterministic matching / 고정 결정론적 매칭

Match `DECLINE` to `GAIN` **only within the same exact `CERT × STALPBR` stratum**, without replacement.

Process DECLINE branches in ascending `(delta_log_share, UNINUMBR)` order. For each DECLINE branch choose the unused GAIN branch by, in order:

1. minimum absolute difference in `ln(share_2022)`;
2. minimum absolute difference in `ln(DEPSUMBR_2022)`;
3. minimum absolute difference in `ln(DEPSUMBR_2023)` when both 2023 values are strictly positive, otherwise treat the difference as infinity;
4. lexical `UNINUMBR`.

Each `UNINUMBR` may appear in at most one pair.

Persisted N01 pair rows may contain only:

- pair ID;
- exact `UNINUMBR`;
- `CERT`;
- `STALPBR`;
- 2022–2024 `DEPSUMBR`;
- 2022 and 2024 within-stratum shares;
- `delta_log_share`;
- exposure class (`DECLINE` or `GAIN`);
- frozen baseline-balance metrics.

No future membership/event/outcome field may be persisted.

## N01 PASS requirements / N01 PASS 요건

All requirements must pass prospectively:

1. official SOD 2022, 2023, and 2024 are reproducibly machine-readable at zero incremental cost;
2. all six frozen historical fields are present in each year;
3. no 2025 SOD row or future BankFind branch/event membership is opened;
4. exact `UNINUMBR` identity only; all conflicting or ownership-changing historical branches are excluded fail-closed; identity repair = false;
5. at least **50,000** historically eligible stable-ownership branches remain;
6. at least **500** eligible `CERT × STALPBR` strata with `n >= 8` remain;
7. at least **2,000** matched DECLINE–GAIN pairs remain;
8. matched pairs span at least **30** distinct `STALPBR` values;
9. every pair satisfies `delta_log_share_DECLINE < delta_log_share_GAIN`;
10. every pair has the same exact `CERT` and `STALPBR` on both sides;
11. no `UNINUMBR` appears in more than one pair;
12. at least **75%** of pairs have 2022 deposit-share ratio `DECLINE/GAIN` within `[1/3, 3]`;
13. at least **75%** of pairs have 2022 absolute branch-deposit ratio `DECLINE/GAIN` within `[1/3, 3]`;
14. at least **75%** of pairs have 2023 absolute branch-deposit ratio `DECLINE/GAIN` within `[1/3, 3]` among pairs with positive 2023 values on both sides;
15. deterministic canonical pair-manifest SHA-256 is persisted;
16. all future-outcome/firewall booleans remain false;
17. relationship/prediction/causality/ranking/novelty all remain false;
18. incremental monetary cost is exactly **0 USD**.

### N01 PASS

`PASS_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_IDENTIFIABLE`

### N01 HOLD

`HOLD_US_FDIC_BRANCH_N01_MATCHED_NETWORK_POSITION_TRAJECTORY_DESIGN_NOT_IDENTIFIABLE`

A valid scientific HOLD is terminal for this exact N01 design. Historical eligibility rules, `CERT × STALPBR` strata, quartiles, matching order, balance thresholds, and minimum pair/state counts must not be relaxed after observed N01 counts.

Network/API/parser/implementation defects before a valid N01 structural run are not scientific HOLD and may be corrected transparently without changing this contract.

## Prospectively frozen future E01 adjudication / 향후 E01 사전고정

This section does **not** authorize future outcome access. It freezes the adjudication and primary paired analysis that a later E01 must use **if and only if N01 passes and a separate E01 contract/Issue/authorization is created**.

### Exact future physical-branch survival hierarchy

For each frozen N01 `UNINUMBR`:

1. if the exact `UNINUMBR` appears in official 2025 SOD under any `CERT`, classify `SURVIVED` (`Y = 0`); ownership change does not equal physical closure;
2. if exact `UNINUMBR` is absent from 2025 SOD and official FDIC Bank Structure Change/History records identify an exact branch **closing** event with effective date in **2024-07-01 through 2025-06-30**, classify `CLOSED` (`Y = 1`);
3. if exact `UNINUMBR` is absent but the official event evidence indicates purchase/assumption, sale/lease, merger/ownership transfer, or relocation without a qualifying closing event, classify `TRANSFER_OR_RELOCATION_UNKNOWN` and exclude from the primary endpoint;
4. if exact `UNINUMBR` is absent and no exact official closing/transfer/relocation adjudication is available, classify `UNRESOLVED` and exclude from the primary endpoint;
5. if 2025 SOD presence conflicts with a qualifying closing event in the frozen window, classify `CONFLICT` and exclude fail-closed;
6. no name/address/geospatial/fuzzy/manual repair may resolve any future identity conflict.

### Frozen E01 eligibility gate after outcome opening

The primary paired analysis may proceed only if:

- at least **1,500** N01 pairs have both sides resolved to `SURVIVED` or `CLOSED`;
- resolved-pair coverage is at least **75%** of the frozen N01 pair manifest;
- at least **50** total `CLOSED` branches occur across resolved pairs.

If any of these fails, E01 terminates as insufficient outcome ascertainment without changing the endpoint or adjudication hierarchy.

### Primary paired outcome

For resolved frozen pairs only:

- `Y_DECLINE = 1` iff DECLINE branch is `CLOSED`, else 0;
- `Y_GAIN = 1` iff GAIN branch is `CLOSED`, else 0;
- `risk_DECLINE = mean(Y_DECLINE)`;
- `risk_GAIN = mean(Y_GAIN)`;
- `RD = risk_DECLINE - risk_GAIN`;
- `b = count(DECLINE=1, GAIN=0)`;
- `c = count(DECLINE=0, GAIN=1)`;
- exact two-sided McNemar/binomial test on `b+c` with `p=0.5`.

### Frozen E01 gates

- `PASS_POSITIVE_MATERIAL_US_FDIC_BRANCH_E01_RELATIONSHIP` iff `RD >= +0.02`, exact two-sided `p < 0.05`, and `b > c`;
- `POSITIVE_BELOW_MATERIALITY_US_FDIC_BRANCH_E01_RELATIONSHIP` iff `0 < RD < +0.02`, exact two-sided `p < 0.05`, and `b > c`;
- `NO_PREREGISTERED_POSITIVE_US_FDIC_BRANCH_E01_RELATIONSHIP` otherwise.

Any later result is observational/noncausal. A negative estimate must not be reframed as a protective-effect claim, and no result may be used as a branch closure ranking, bank score, depositor targeting system, or causal effectiveness estimate.

## Cost boundary / 비용 경계

Incremental monetary cost must remain **0 USD**. Any paid source/API/runner requirement needs explicit user approval before execution.
