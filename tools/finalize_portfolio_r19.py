#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-152.md"
dec152_path = ROOT / "registry" / "DEC-152.md"
dec153_path = ROOT / "registry" / "DEC-153.md"
r19_dir = ROOT / "research" / "PORTFOLIO-R19"
e02_dir = ROOT / "research" / "CA-GRAIN-E02"
r19_dir.mkdir(parents=True, exist_ok=True)
e02_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 108" in status
assert "last_decision: DEC-151" in status
for p in (claim_path, dec152_path, dec153_path, r19_dir / "RESULT.md", e02_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

(r19_dir / "RESULT.md").write_text("""---
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
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-152
type: claim
created: 2026-09-12
issue: 109
status: active
---

# CLM-152 — Official elevator semantics prospectively distinguish Primary deliveries from Process deliveries

Outcome-blind E01 identified both `Primary / Deliveries / Current Week` and `Process / Producer Deliveries / Current Week`. Official Canadian grain-sector definitions distinguish their operating roles independently of any observed magnitudes: primary elevators principally receive producer grain for storage or forwarding, whereas process elevators principally receive/store grain for direct manufacture or processing.

For a subsequent railway-origin-dwell association test, that institutional ordering supports prospectively fixing `Primary / Deliveries` as the upstream pressure family in a new descendant. This does not validate the relationship, establish causality or erase external-overlap risk. Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

dec152_path.write_text("""---
id: DEC-152
type: decision
created: 2026-09-12
issue: 109
status: accepted
---

# DEC-152 — PORTFOLIO-R19 selects CA-GRAIN-E02 at 40/45

Select the new `CA-GRAIN-E02` descendant at **40/45**. E01 remains terminal HOLD. E02 is scientifically distinct because its `Primary / Deliveries` exposure is fixed prospectively from official institutional semantics before numeric outcomes/exposures are opened.

Retain the novelty penalty arising from existing Grain Monitor / Statistics Canada operational monitoring. The purpose is a bounded preregistered cross-source association test, not a claim that grain movement and rail dwell have never previously been jointly monitored.
""", encoding="utf-8")

dec153_path.write_text("""---
id: DEC-153
type: decision
created: 2026-09-12
issue: 110
status: accepted
---

# DEC-153 — Authorize CA-GRAIN-E02 exactly as preregistered

Authorize Issue #110 without modification. Before fitting, require exact structural completeness for the frozen GSW `Primary / Deliveries / Current Week` 15-grain × 4-region component set and the frozen Transport Canada Canada-level CN/CPKC outcome. Require >=75 strictly consecutive final model observations.

If the structural gate passes, execute exactly one primary first-difference, one-week-lag OLS association with Newey-West HAC lag 2 and the preregistered +1.0 hour / +100 Ktonnes materiality floor. Carrier-specific models are diagnostic only and cannot rescue or reverse the primary gate.

No causal claim is authorized. No post-value changes to source identities, period, carriers, lag, transformation, inference or threshold are permitted. Cost remains **0 USD**.
""", encoding="utf-8")

(e02_dir / "README.md").write_text("""---
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
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E02-ACTIVE
active_issue: 110
active_research: CA-GRAIN-E02
last_completed_issue: 109
last_completed_research: PORTFOLIO-R19
last_decision: DEC-153
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R19_SELECTED_CA_GRAIN_E02__PREREGISTERED_RELATIONSHIP_TEST_ACTIVE`

PORTFOLIO-R19 selected the new CA-GRAIN-E02 descendant at 40/45. E01 remains terminal HOLD. E02 prospectively fixes `Primary / Deliveries / Current Week` from official elevator semantics, not numeric fit, and freezes the exact 15-grain × 4-region exposure, Canada-level CN/CPKC origin-dwell outcome, one-week lag, first differences, HAC inference and materiality gate.

## Exact next action / 정확한 다음 행동

Execute Issue #110 exactly as preregistered. First validate structural completeness and >=75 eligible observations; fail closed before fitting if not satisfied. If valid, compute the single primary association and preregistered non-rescuing diagnostics. No post-value tuning.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E02-ACTIVE
active_issue: 110
active_research: CA-GRAIN-E02
last_completed_issue: 109
last_completed_research: PORTFOLIO-R19
last_decision: DEC-153
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R19 selected Issue #110 `CA-GRAIN-E02` at **40/45**. E01 remains terminal HOLD; E02 is a separate descendant whose `Primary / Deliveries` exposure is justified prospectively by official Canadian elevator semantics.

Execute the exact Issue #110 preregistration: frozen 15 grains × Alberta/British Columbia/Manitoba/Saskatchewan, GSW `Primary / Deliveries / Current Week`, Transport Canada `All Western grain / Average Dwell Time at Origin / Canada`, carriers CN+CPKC equal-weight, one-week lag, first differences, >=75 observations, OLS + Newey-West HAC lag 2, materiality +1.0 hour per +100 Ktonnes.

This is associational, not causal. No post-value tuning. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-CA-GRAIN-E02-ACTIVE",
    "active_issue": 110,
    "active_research": "CA-GRAIN-E02",
    "last_completed_issue": 109,
    "last_completed_research": "PORTFOLIO-R19",
    "last_decision": "DEC-153",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-152`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-152` | Official Canadian elevator semantics distinguish Primary producer-grain storage/forwarding from Process direct manufacture/processing, prospectively supporting `Primary/Deliveries` for a new rail-origin-dwell descendant without numeric fit. / 공식 시설 의미로 새 E02의 Primary exposure를 사전 고정할 수 있다. | `OBSERVED/DERIVED` | `V2_PRIMARY_OFFICIAL_SEMANTICS` | Canada Grain Act / CGC definitions; PORTFOLIO-R19 | 2026-09-12 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-152`" not in dl and "`DEC-153`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-152` | 2026-09-12 | R19 selects new CA-GRAIN-E02 at 40/45 with `Primary/Deliveries` prospectively fixed from official semantics; E01 remains terminal. / R19에서 새 E02 선정. | Resolves semantic ambiguity without numeric feedback while preserving overlap penalty. | Issue #109; `CLM-152`; `research/PORTFOLIO-R19/RESULT.md` | active |
| `DEC-153` | 2026-09-12 | Authorize Issue #110 exactly as preregistered; structural gate first, then one frozen association test only. / E02 사전등록 그대로 승인. | Prevent post-value source/model/threshold tuning; diagnostics cannot rescue primary. | Issue #110; `research/CA-GRAIN-E02/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"CA-GRAIN-E02","score":40,"issue":110,"cost_usd":0}))
