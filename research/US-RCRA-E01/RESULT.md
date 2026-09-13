---
id: US-RCRA-E01-RESULT
type: preregistered-paired-relationship
created: 2026-09-13
issue: 125
gate: NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP
relationship_computed: true
incremental_monetary_cost_usd: 0
---

# US-RCRA-E01 Result

**`NO_PREREGISTERED_POSITIVE_US_RCRA_E01_RELATIONSHIP`**

The frozen same-facility paired-CEI test does **not** support the preregistered positive monitoring/compliance association. This is a non-causal result and must not be reframed as evidence that disasters improve compliance.

## Frozen primary result

- Frozen pair structure: **297** facilities across **43** state/territory FIPS; pair fingerprint `d648d242e6adcddcac44dba7a61cab0ac9da2c4a5aa80e9d123d725aa7dfed73`.
- Primary analyzable complete Y/N pairs: **284**; discordant pairs: **92**.
- Contingency: `NN=123`, `N→Y=42`, `Y→N=50`, `YY=69`.
- Pre inspection violation-found risk: **41.901408%**.
- Post inspection violation-found risk: **39.084507%**.
- Paired absolute risk difference: **-2.816901%** (-2.817 percentage points).
- Exact two-sided McNemar/binomial p-value: **0.465707445773**.
- Frozen positive materiality floor: **+5 percentage points**.

Because the point estimate is negative and the exact test is not significant, the positive preregistered gate fails. No reversed or alternative post-hoc hypothesis is opened.

## Duplicate-row integrity handling

The committed pair manifest reproduced the N01 structure outcome-blind at 297/43 before the primary outcome pass. A subsequent source audit found **32** of 594 selected CEI identities represented by multiple source rows; all differed only in `EVALUATION_AGENCY` on non-outcome fields.

Before the successful primary calculation, the resolution rule was frozen: all duplicate source rows must agree under the original Y/N/U/missing coding to supply a selected CEI outcome; otherwise the selected CEI is missing. Under that rule, **25** duplicate identities agreed and **7** conflicted and were treated as missing. No row or agency was selected based on the outcome.

Execution-integrity note: an earlier failed Pass-2 implementation technically projected selected `FOUND_VIOLATION` fields into memory before halting on duplicate identity, but surfaced, persisted and aggregated no outcome values or statistics and did not change the scientific pair/window/test/materiality contract. The durable Issue #125 record preserves this limitation; therefore the final record does not claim uninterrupted value non-access after that failed run.

## Non-rescuing diagnostics

- Agency status across 297 pairs: {"MULTI_OR_MISSING_AGENCY_AMBIGUOUS": 29, "SINGLE_AGENCY_CHANGED": 38, "SINGLE_AGENCY_SAME": 230}.
- Same-single-agency sensitivity: **229** analyzable / **74** discordant; RD **-3.493pp**, exact p **0.415985**.
- Diagnostics are descriptive/non-rescuing and do not alter the primary disposition.

## Claim boundary

`FOUND_VIOLATION` is an inspection-result field. This test is a same-facility monitoring/compliance association around FEMA-declared physical hazards, not a causal estimate of underlying hazardous-waste compliance. Surveillance, agency, response timing, disaster severity, inspection selection and concurrent policy remain potential explanations. No claim is made that disasters cause violations or reduce violations.

## Terminal decision

US-RCRA-E01 is terminal under this preregistration. Do **not** rescue it by changing the disaster set, 365-day washout, ±730-day CEI window, pair identities, Y/N/U coding, duplicate handling, inspection type, statistical test, direction or +5pp materiality threshold. Return to Stage 0 for independent-candidate comparison.

Incremental monetary cost: **0 USD**.
