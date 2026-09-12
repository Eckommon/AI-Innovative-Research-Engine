---
id: CA-GRAIN-E02
issue: 110
state: COMPLETED_HOLD_TEMPORAL_IDENTITY
mission_anchor: MEM-054
portfolio_decision: DEC-152
authorization_decision: DEC-153
parent_terminal: CA-GRAIN-E01-STAGE-A-HOLD
relationship_computed: false
magnitudes_opened: authorized_but_no_model_fitted
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E02 — Primary-Delivery Pressure × Origin-Dwell Relationship
# CA-GRAIN-E02 — Primary 유입압력 × 출발지 대기시간 관계

Canonical preregistration is Issue #110. E01 remains terminal; E02 prospectively fixes `Primary / Deliveries / Current Week` from official elevator semantics.

Primary test: weekly change in equal-weight CN/CPKC Canada-level `All Western grain` origin dwell on the **one-week-lagged weekly change** in fixed western-primary deliveries, scaled per +100 Ktonnes. OLS with Newey-West HAC lag 2; require >=75 final observations; materiality floor +1.0 hour / +100 Ktonnes.

This is an association/predictive bottleneck test, not a causal estimate. No post-value tuning is allowed. Raw source bytes remain transient. Cost: **0 USD**.

## Final disposition / 최종 판정

- gate: **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**
- corrected execution: `34689346777`
- targeted provenance audit: `34690867196`
- technical week-identity revalidation: `34690978853`
- primary relationship model: **not fitted**
- cause: frozen explicit-date normalization cannot uniquely preserve distinct GSW Week 44 and Week 48 temporal identities
- decision: `DEC-154`
- restart: **Stage 0 portfolio control**

E02 is terminal under its frozen temporal contract. Do not repair it by switching to `grain_week` after value authorization.
