#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-159.md"
dec163_path = ROOT / "registry" / "DEC-163.md"
dec164_path = ROOT / "registry" / "DEC-164.md"
r22_dir = ROOT / "research" / "PORTFOLIO-R22"
e01_dir = ROOT / "research" / "US-WW-E01"
r22_dir.mkdir(parents=True, exist_ok=True)
e01_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "last_completed_issue: 116" in status
assert "last_completed_research: US-WW-N01" in status
assert "last_decision: DEC-162" in status
for p in (claim_path, dec163_path, dec164_path, r22_dir / "RESULT.md", e01_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

(r22_dir / "RESULT.md").write_text("""---
id: PORTFOLIO-R22-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 118
state: COMPLETED_SELECT
selected_candidate: US-WW-E01
selected_gate: US-WW-E01
next_issue: 119
future_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R22 Result — Select US-WW-E01

**`SELECT_US_WW_E01_INCIDENT_COMPLIANCE_RELATIONSHIP`**

US-WW-E01 is selected for one separately preregistered relationship test. No 2023–2025 future compliance outcome magnitude was opened during selection.

## Mission-ROI comparison

0–5 each; /45. These are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WW-E01 incident compliance** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | **43** | **SELECT** |
| US-RCRA-001 hazard → compliance | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 2 | **39** | HOLD_READY |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |

## Why US-WW-E01 now leads

US-WW-F01 removed national source/join uncertainty and US-WW-N01 prospectively fixed exposure/comparator identities, an all-linked-permit facility unit, a 2019–2021 baseline-clean rule, and an exact-label compliance-reason leakage stratum while keeping future outcomes closed. Official ICIS-NPDES semantics also permit occurrence/start dates to be frozen before outcomes: PS/CS use `SCHEDULE_DATE`; SE uses `SINGLE_EVENT_VIOLATION_DATE`.

Material adjacent literature exists, especially Hanyi Yi's `Financing Public Goods`, so novelty receives only 3/5 and the project may not claim first use of CWNS with NPDES violations. The bounded information gain remains high because E01 asks one falsifiable, preregistered 2022 structural-need-profile → 2023–2025 incident prediction question under explicit leakage control.

## Exact next action

Execute Issue #119 exactly as preregistered plus its pre-outcome mixed-date streaming clarification. Structural support must pass before any future-window membership/count/rate is derived. No design/model/threshold tuning is allowed after future outcomes are opened.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-159
type: claim
created: 2026-09-13
issue: 118
status: active
---

# CLM-159 — N01 PASS plus official ICIS violation-start semantics make one bounded US-WW-E01 test executable

US-WW-N01 established outcome-blind structural support and leakage controls, while official ICIS-NPDES field semantics permit the primary violation-start identity to be fixed prospectively (`SCHEDULE_DATE` for PS/CS; `SINGLE_EVENT_VIOLATION_DATE` for SE). This supports one bounded preregistered E01 test without post-outcome date-rule tuning.

Material adjacent CWNS×NPDES violation literature limits novelty; this claim does not establish predictive value, causality, or novelty of the dataset linkage itself. Future outcomes remain unopened at selection. Cost: **0 USD**.
""", encoding="utf-8")

dec163_path.write_text("""---
id: DEC-163
type: decision
created: 2026-09-13
issue: 118
status: accepted
---

# DEC-163 — PORTFOLIO-R22 selects US-WW-E01 at 43/45

Select `US-WW-E01 — 2022 structural need profile × 2023–2025 incident compliance` at **43/45**. N01 materially reduced source, join, exposure, comparator and leakage-identifiability risk; the remaining highest-value question is one frozen relationship test.

Preserve the current-overlap penalty and non-causal claim boundary. Selection itself does not authorize outcome access.
""", encoding="utf-8")

dec164_path.write_text("""---
id: DEC-164
type: decision
created: 2026-09-13
issue: 119
status: accepted
---

# DEC-164 — Authorize US-WW-E01 exactly as preregistered plus pre-outcome streaming clarification

Authorize Issue #119 and its pre-outcome mixed-date execution clarification. Before the structural gate passes, the runner may stream mixed-year violation files only to identify 2019–2021 baseline events; rows outside that window must be ignored without storing or computing 2023–2025 membership, counts, rates or comparisons.

Only after the frozen structural gate passes may a second pass derive the future binary outcome. Preserve the issue's facility unit, all-linked-permit rule, exposure/comparator identities, baseline-clean rule, permit lifecycle risk rule, exact-label leakage stratum, canonical event-start dates, state-FE LPM, HC1 covariance, +0.03 materiality floor, diagnostic non-rescue rule and non-causal interpretation. No post-outcome tuning. Cost: **0 USD**.
""", encoding="utf-8")

(e01_dir / "README.md").write_text("""---
id: US-WW-E01
issue: 119
state: ACTIVE_PREREGISTERED_RELATIONSHIP
selection_decision: DEC-163
authorization_decision: DEC-164
future_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WW-E01 — Preregistered Structural-Need Profile × Incident-Compliance Test

Canonical contract is Issue #119 plus its pre-outcome mixed-date execution clarification.

The structural pass may use only CWNS identities, ICIS permit lifecycle identities, and 2019–2021 baseline violation identities. It must not store or compute 2023–2025 future-window membership/counts/rates before the structural gate passes. If structural support passes, exactly one primary state-FE HC1 linear-probability model is authorized under the frozen +3 percentage-point materiality gate.

No causal claim is allowed. Raw source bytes remain transient. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-E01-ACTIVE
active_issue: 119
active_research: US-WW-E01
last_completed_issue: 118
last_completed_research: PORTFOLIO-R22
last_decision: DEC-164
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R22_SELECTED_US_WW_E01__US_WW_E01_ACTIVE`

PORTFOLIO-R22 selected **US-WW-E01** at **43/45**. Issue #119 is the only active research gate. The test is fully preregistered, but 2023–2025 future compliance outcome membership/counts/rates remain unopened until the frozen structural gate passes.

## Exact next action / 정확한 다음 행동

Execute Issue #119 in two passes: first baseline/structural qualification only, then—only if PASS—derive the frozen future binary incident outcome and fit the single preregistered model. No post-outcome source/date/model/threshold tuning.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-E01-ACTIVE
active_issue: 119
active_research: US-WW-E01
last_completed_issue: 118
last_completed_research: PORTFOLIO-R22
last_decision: DEC-164
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R22 selected US-WW-E01 at 43/45 and authorized Issue #119 under DEC-164.

Exact restart: execute the two-pass preregistered E01. Pass 1 may derive only baseline-clean, lifecycle-at-risk, exposure/comparator/leakage and state/design support. Future-window membership/count/rate must not be stored or computed before structural PASS. If PASS, Pass 2 derives the 2023–2025 facility-level binary incident outcome and fits the one frozen state-FE HC1 LPM.

Canonical occurrence dates are PS/CS `SCHEDULE_DATE` and SE `SINGLE_EVENT_VIOLATION_DATE`. Detection/resolution/actual/report/end dates cannot rescue or shift primary event timing. Hanyi Yi's adjacent work limits novelty. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-WW-E01-ACTIVE",
    "active_issue": 119,
    "active_research": "US-WW-E01",
    "last_completed_issue": 118,
    "last_completed_research": "PORTFOLIO-R22",
    "last_decision": "DEC-164",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-159`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-159` | US-WW N01 PASS plus official ICIS violation-start semantics make one bounded preregistered E01 executable without post-outcome date-rule tuning; adjacent literature limits novelty. / N01 PASS와 공식 event-start 의미로 E01 1회 검정이 사전고정 가능하다. | `OBSERVED/DERIVED` | `V2/V3_PREREGISTERED_DESIGN_READY` | US-WW-N01; official ICIS-NPDES dictionary; PORTFOLIO-R22 | 2026-09-13 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-163`" not in dl and "`DEC-164`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-163` | 2026-09-13 | PORTFOLIO-R22 selects US-WW-E01 at 43/45. / N01 이후 incident-compliance E01 선정. | N01 removed most design-identifiability risk; one frozen relationship test now has highest marginal information value despite adjacent-literature penalty. | Issue #118; `CLM-159`; `research/PORTFOLIO-R22/RESULT.md` | active |
| `DEC-164` | 2026-09-13 | Authorize Issue #119 plus its pre-outcome mixed-date two-pass execution clarification. / E01 사전등록 및 미래 outcome firewall 승인. | Preserve structural-first outcome firewall and all frozen event/date/model/materiality rules before future outcomes. | Issue #119; `research/US-WW-E01/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"US-WW-E01","score":43,"active_issue":119,"future_outcomes_opened":False,"cost_usd":0}))
