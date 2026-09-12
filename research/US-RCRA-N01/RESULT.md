---
id: US-RCRA-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-13
issue: 123
gate: PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE
found_violation_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-N01 Result

**`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`**

N01 passes as an outcome-blind paired-inspection design-identifiability gate. This does **not** establish that FEMA-declared disasters change RCRA compliance, and it does not authorize opening the selected CEI-pair `FOUND_VIOLATION` values.

## Frozen structural evidence

- Current RCRAInfo identifies `CEI` deterministically as `COMPLIANCE EVALUATION INSPECTION`; 32,094 CEI rows are present for the 640 operating-TSDF universe.
- 464 operating TSDFs have at least one qualifying 2018–2023 physical-hazard FEMA DR in their exact county; 459 receive a frozen index event after the 365-day qualifying-disaster washout.
- Under the fixed ±730-day same-facility last-pre/first-post CEI rule, 297 facilities remain after excluding 53 with no pre CEI, 32 with no post CEI, and 77 with another qualifying disaster before/on the selected post CEI.
- The 297 pairs span 43 state/territory FIPS, exceeding the preregistered minimum of 20.
- Evaluation-agency identity is present for 100% of selected pre and post CEIs, exceeding the 95% threshold.
- No ambiguous selected-date tie remains under the frozen evaluation-identifier tie-break.
- The bounded literature scan found material adjacent RCRA inspection/compliance and hazard-vulnerability work but no materially near-identical national paired-CEI FEMA-disaster design; novelty is not proven.
- `FOUND_VIOLATION` values were not accessed or persisted; no disaster-linked violation count/rate, coefficient, p-value or relationship was computed.

## Frozen descendant boundary

Any later E01 requires separate Stage-0 selection and preregistration before outcomes are opened. At minimum it must freeze:

- analysis unit = selected same-facility CEI pair;
- exact pre/post pair identities already selected outcome-blind by N01;
- handling of `FOUND_VIOLATION` values `Y`, `N`, and `U`;
- exact paired statistical test/model and inference;
- evaluation-agency-change handling/diagnostic;
- materiality threshold;
- missingness and exclusions;
- non-causal compliance-monitoring interpretation;
- no post-value alternative window, disaster set, CEI substitution or rescue threshold.

Incremental monetary cost: **0 USD**.
