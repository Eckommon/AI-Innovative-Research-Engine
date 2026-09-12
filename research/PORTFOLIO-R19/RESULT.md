---
id: PORTFOLIO-R19-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-12
issue: 109
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-CA-002-PRIMARY
selected_gate: CA-GRAIN-E02
next_issue: 110
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R19 Result — Post-E01 Ambiguity HOLD Reselection
# PORTFOLIO-R19 결과 — E01 exposure 모호성 HOLD 이후 재선정

## Final selection / 최종 선정

**`SELECT_C_CA_002_PRIMARY_DELIVERIES_CA_GRAIN_E02`**

Advance to Issue #110 `CA-GRAIN-E02` under its fully frozen preregistration. E01 remains terminal and is not repaired or rerun.

## Why the new descendant is scientifically distinct / 새 descendant 정당성

E01's outcome-blind source catalog found two semantically plausible upstream families. Subsequent official semantic verification, still without opening values, resolves their operational roles independently of model fit: under the Canada Grain Act / Canadian Grain Commission framework, a **primary elevator** principally receives grain directly from producers for storage or **forwarding**, while a **process elevator** principally receives/stores grain for direct manufacture or processing into other products.

Because the downstream outcome is railway **origin dwell**, `Primary / Deliveries / Current Week` has the stronger prospective supply-chain ordering. This is a new preregistered descendant, not post-hoc repair of E01.

The overlap penalty remains material: Statistics Canada and the Grain Monitoring Program already monitor grain movement and rail performance. E02 therefore makes no novelty claim from merely placing those variables together. Its bounded information value is the fully preregistered cross-source, one-week-lag, first-difference association test.

## Mission-ROI comparison / 목적-ROI 비교

0–5 each; /45. Portfolio-control judgment, not an empirical finding.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **CA-GRAIN-E02 — Primary deliveries × origin dwell** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 2 | **40** | **SELECT** |
| US-UTIL AMI × Storm × Reliability descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_READY_HIGH_OVERLAP |
| EU-GRID separate source-route redesign | 5 | 5 | 5 | 5 | 5 | 2 | 3 | 3 | 3 | **36** | HOLD_SOURCE_ROUTE_FRICTION |
| US freight-rail × weather | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2026_OVERLAP |
| C-SG-001 Maritime Weather | 3 | 4 | 4 | 2 | 4 | 5 | 5 | 3 | 5 | **35** | HOLD_READY_LOW_DIVERSITY |
| C-EU-004 Industrial Site Climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE_JOIN_ASSET |

## Frozen E02 contract / E02 고정 계약

Issue #110 freezes before values:
- exposure: GSW `Primary / Deliveries / Current Week`, blank grade;
- exact 15 grain identities and four western provinces;
- outcome: Transport Canada `All Western grain / Average Dwell Time at Origin / Canada`;
- carriers exactly `CN`, `CPKC`, equal-weight weekly mean;
- one-week lag and weekly first differences;
- >=75 final observations before fitting;
- OLS + Newey-West HAC lag 2, finite-sample `n/(n-2)`;
- signed beta > 0;
- materiality floor +1.0 dwell hour per +100 Ktonnes;
- no post-value carrier/grain/region/period/lag/model/threshold substitution.

The test is explicitly **associational/predictive, not causal**.

## Exact next action / 정확한 다음 행동

Execute Issue #110 exactly as preregistered. Validate all 60 GSW grain×region component identities and both carrier outcomes before fitting. If structural completeness fails, HOLD without model fitting. Otherwise compute the single frozen primary result and non-rescuing carrier diagnostics.

Incremental monetary cost remains **0 USD**.
