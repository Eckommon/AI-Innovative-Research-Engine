---
id: US-WW-N01-SEMANTIC-ADJUDICATION
type: outcome-blind-semantic-adjudication
created: 2026-09-13
issue: 116
future_outcome_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WW-N01 Semantic Adjudication — Compliance-Reason Leakage Rule

## Technical observation

The first N01 runner used a permissive regex (`permit|compliance|regulat|enforcement|violation|consent|order|standard`) only to surface candidate `REASON_FOR_NEEDS` labels for human semantic adjudication. That candidate list is **not** itself the frozen leakage rule.

The regex over-included:

- `The project(s) will prevent unregulated water quality or human health impacts.`

because the substring `regulat` occurs inside `unregulated`. This is a technical semantic false positive and was identified without opening any 2023–2025 future outcome magnitude.

## Frozen exact-label leakage rule

For any later descendant, define `COMPLIANCE_REASON_STRATUM = 1` if and only if a facility has at least one of these exact CWNS `REASON_FOR_NEEDS.NEED_REASON` identities:

1. `The project(s) is necessary to obtain compliance with a new permit requirement.`
2. `The project(s) is required to maintain compliance with a NPDES permit.`
3. `The project(s) is to achieve or maintain compliance with a TMDL.`
4. `The project(s) is to increase capacity or improve treatment in advance of anticipated new permit requirements.`

The following observed labels are **not** classified as explicit compliance-driven reasons:

- `The project(s) improves water efficiency, improves energy efficiency, improves water conservation, addresses climate change, or improves resiliency.`
- `The project(s) will prevent unregulated water quality or human health impacts.`

No later result may add/remove labels from this rule based on future compliance outcomes.

## Frozen handling

Use the exact-label indicator as a **pre-specified leakage stratum** in any later authorized experiment. It may additionally be used for a pre-specified exclusion sensitivity analysis, but the primary leakage handling may not be chosen after outcome inspection.

The baseline-clean rule remains: across **all** officially linked NPDES permits for a facility, no recorded PS/CS/SE violation identity in 2019-01-01 through 2021-12-31.

No 2023–2025 future violation count/rate, group prevalence, coefficient, p-value or relationship statistic was opened to make this adjudication.
