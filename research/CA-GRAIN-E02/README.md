---
id: CA-GRAIN-E02
issue: 110
state: ACTIVE_PREREGISTERED_RELATIONSHIP_TEST
mission_anchor: MEM-054
portfolio_decision: DEC-152
authorization_decision: DEC-153
parent_terminal: CA-GRAIN-E01-STAGE-A-HOLD
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E02 — Primary-Delivery Pressure × Origin-Dwell Relationship
# CA-GRAIN-E02 — Primary 유입압력 × 출발지 대기시간 관계

Canonical preregistration is Issue #110. E01 remains terminal; E02 prospectively fixes `Primary / Deliveries / Current Week` from official elevator semantics.

Primary test: weekly change in equal-weight CN/CPKC Canada-level `All Western grain` origin dwell on the **one-week-lagged weekly change** in fixed western-primary deliveries, scaled per +100 Ktonnes. OLS with Newey-West HAC lag 2; require >=75 final observations; materiality floor +1.0 hour / +100 Ktonnes.

This is an association/predictive bottleneck test, not a causal estimate. No post-value tuning is allowed. Raw source bytes remain transient. Cost: **0 USD**.
