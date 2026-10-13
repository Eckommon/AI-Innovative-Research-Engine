---
id: US-CMS-NPI-N01-RESULT
type: prospective-design-result
created: 2026-10-13
issue: 202
research: US-CMS-NPI-N01
disposition: PASS
contract_commit: 29ab6cd8368801137eff94463a5b405c1fdf10ac
attempt_01_commit: da46a24114452a1d63a16adf731aa3b51761c88b
attempt_01_run: 38356022445
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-N01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_CMS_NPI_N01_MULTI_TAXONOMY_MATCHED_COHORT_READY`**

Attempt 01 validly passed **18/18** frozen prospective-design gates. No future NPPES weekly/later monthly row body was opened and no arm-specific deactivation lookup occurred.

## Locked cohort evidence

- eligible active Type-2 NPIs: **1,978,439**
- exposed multi-taxonomy: **409,936**
- control single-taxonomy: **1,568,503**
- exact common strata: **31,791**
- exposed common-support coverage: **97.0742%**
- deterministic matched pairs: **346,859**
- comparator reuse: **0**
- cross-stratum pairs: **0**
- enumeration-age |SMD|: **0.00809**
- practice-location-count |SMD|: **0.01358**
- recent global deactivated NPIs, 2024-10-13..2026-10-12: **69,550**
- arm-specific historical outcome lookup: **false**

## Locked matching design

Exact stratum:
`state × primary-taxonomy-prefix4 × 5-year enumeration-age band × subpart status × practice-location bin`.

Within each stratum, exposed and controls are deterministically ordered by SHA256 of the exact NPI under the frozen namespace and paired one-to-one to the smaller arm.

The locked cohort can therefore be reconstructed exactly from the frozen baseline SHA and runner/contract without persisting millions of raw provider identifiers.

## Firewall

- weekly body opened: **false**
- later monthly body opened: **false**
- future deactivation membership opened: **false**
- relationship/prediction/ranking/causal metric: **false**
- identity repair: **false**
- cost: **0 USD**

## Interpretation

The N01 result establishes unusually strong prospective support and balance. It does not establish that taxonomy plurality predicts deactivation.

Deactivation remains an administrative NPPES registry event only.

## Consequence

Authorize one separately preregistered `US-CMS-NPI-E01` controlled future-update experiment.

E01 must select the future source without looking at cohort outcomes and must reconstruct the cohort using the exact frozen baseline and N01 algorithm before opening the first qualifying future update.

Incremental monetary cost: **0 USD**.
