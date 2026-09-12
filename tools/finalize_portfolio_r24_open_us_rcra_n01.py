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
claim_path = ROOT / "registry" / "CLM-163.md"
dec_select_path = ROOT / "registry" / "DEC-169.md"
dec_auth_path = ROOT / "registry" / "DEC-170.md"
r24_dir = ROOT / "research" / "PORTFOLIO-R24"
n01_dir = ROOT / "research" / "US-RCRA-N01"
r24_result = r24_dir / "RESULT.md"
n01_readme = n01_dir / "README.md"

status = status_path.read_text(encoding="utf-8")
assert "active_issue: none" in status
assert "active_research: NONE" in status
assert "last_completed_issue: 121" in status
assert "last_decision: DEC-168" in status
for p in [claim_path, dec_select_path, dec_auth_path, r24_result, n01_readme]:
    assert not p.exists(), p

r24_dir.mkdir(parents=True, exist_ok=True)
n01_dir.mkdir(parents=True, exist_ok=True)

r24_result.write_text('''---
id: PORTFOLIO-R24-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-13
issue: 122
state: COMPLETED_SELECT
selected_candidate: US-RCRA-N01
selected_gate: US-RCRA-N01
next_issue: 123
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R24 Result — Select US-RCRA-N01

**`SELECT_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABILITY`**

After `US-RCRA-F01` passed source/join/time feasibility, select one outcome-blind design-identifiability gate before any disaster-linked compliance outcome is opened.

## Mission-ROI comparison

0–5 each; /45. Scores are portfolio-control judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-RCRA-N01 paired CEI design gate** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 3 | **41** | **SELECT** |
| US-MINE-001 operational stress → injury | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_OVERLAP |
| US-UTIL post-F02 descendant | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 2 | **38** | HOLD_HIGH_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_OVERLAP |
| C-EU-004 industrial-site climate | 4 | 5 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | **35** | PRESERVE |

## Why N01 leads now

F01 removed the main source, identifier, county-join and temporal-support uncertainty: 640 operating TSDFs are exact county-FIPS-qualified with full coverage and broad FEMA overlap. The remaining scientific bottleneck is **surveillance/detection opportunity**.

EPA identifies the Compliance Evaluation Inspection (CEI) as the primary compliance-monitoring mechanism and standard comprehensive inspection for operating TSDFs. Existing RCRA empirical work also shows that inspection intensity materially changes interpretation of detected violations. Therefore a naive post-disaster violation-rate analysis has lower evidentiary value than an outcome-blind gate testing whether the same facility can be paired on the same CEI type before and after a prospectively defined disaster.

Current bounded literature searches found substantial static natural-hazard/TSDF vulnerability work and general RCRA inspection/compliance research, but did not surface a materially near-identical national paired pre/post-CEI natural-disaster design. This is not a proof of novelty; overlap remains penalized at 3/5.

## Exact next action

Execute Issue #123 outcome-blind. Enumerate CEI type/date/agency identities; assign frozen qualifying FEMA major-disaster events; construct last-pre/first-post CEI pairs under the fixed ±730-day and multi-disaster rules; and test only structural support. `FOUND_VIOLATION` and all disaster-linked compliance outcomes remain unopened.

Incremental monetary cost: **0 USD**.
''', encoding="utf-8")

n01_readme.write_text('''---
id: US-RCRA-N01
issue: 123
state: ACTIVE_OUTCOME_BLIND_DESIGN_IDENTIFIABILITY
selection_decision: DEC-169
authorization_decision: DEC-170
found_violation_values_opened: false
disaster_linked_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-N01 — Paired-CEI Disaster Design Identifiability

Canonical contract is Issue #123.

N01 may inspect operating-TSDF identity, exact county-FIPS, qualifying FEMA `DR` incident type/date identity, and RCRA evaluation type/description/date/agency identities. It may construct pre/post CEI pair membership and structural cardinalities under the frozen rules.

N01 must **not** read, aggregate, persist, rank or compare `FOUND_VIOLATION` values for the selected CEI pairs and must not compute any post-disaster violation outcome or relationship.

PASS does not authorize E01. Cost: **0 USD**.
''', encoding="utf-8")

claim_path.write_text('''---
id: CLM-163
type: claim
created: 2026-09-13
issue: 122
status: active
---

# CLM-163 — F01 source readiness plus standardized CEI semantics support an outcome-blind surveillance-control design gate

US-RCRA-F01 establishes a deterministic operating-TSDF→county-disaster/time→RCRA evaluation identity route. EPA defines CEI as the primary/standard comprehensive compliance inspection for operating TSDFs, and RCRAInfo exposes evaluation type, description, agency and start-date identities separately from `FOUND_VIOLATION`.

These facts make a paired pre/post CEI **design-identifiability** gate testable without opening the compliance-result field. This claim does not establish sufficient pair cardinality, a disaster-compliance relationship, novelty, prediction, or causality. Cost: **0 USD**.
''', encoding="utf-8")

dec_select_path.write_text('''---
id: DEC-169
type: decision
created: 2026-09-13
issue: 122
status: accepted
---

# DEC-169 — PORTFOLIO-R24 selects US-RCRA-N01 at 41/45

Select `US-RCRA-N01` at **41/45**. F01 eliminated most source/join risk, while inspection/evaluation surveillance remains the decisive unresolved threat to a credible RCRA disaster-compliance experiment. A same-facility, same-CEI paired design gate has higher current marginal information value than opening outcomes or switching immediately to a lower-ranked independent branch.

The overlap/novelty score remains bounded because EPA/GAO already study TSDF natural-hazard vulnerability and RCRA inspection/compliance is established literature. No `FOUND_VIOLATION` value or disaster-linked outcome is opened by this decision.
''', encoding="utf-8")

dec_auth_path.write_text('''---
id: DEC-170
type: decision
created: 2026-09-13
issue: 123
status: accepted
---

# DEC-170 — Authorize only outcome-blind US-RCRA-N01 paired-CEI design identifiability

Authorize Issue #123 exactly as preregistered: frozen FEMA `DR` physical-hazard identity, 2018–2023 index period, 365-day washout, ±730-day last-pre/first-post CEI pairing, multi-disaster contamination exclusion, >=100 paired facilities, >=20 states/territories and >=95% evaluation-agency identity support.

N01 may inspect CEI type/date/agency identities and pairing cardinalities only. It must not open selected-pair `FOUND_VIOLATION`, post-disaster violation counts/rates, coefficients, p-values or relationships. PASS does not authorize E01. Cost remains **0 USD**.
''', encoding="utf-8")

claim_ledger = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-163`" not in claim_ledger
claim_ledger_path.write_text(claim_ledger.rstrip() + '''\n\n| `CLM-163` | US-RCRA-F01 exact source readiness plus EPA standardized CEI type/date/agency semantics support an outcome-blind paired-CEI surveillance-control design gate without opening `FOUND_VIOLATION`. / F01과 CEI 표준 의미로 감시편향 통제 설계 gate가 값 비사용으로 가능하다. | `OBSERVED/DERIVED` | `V2/V3_DESIGN_GATE_READY` | US-RCRA-F01; EPA RCRA compliance-monitoring semantics; PORTFOLIO-R24 | 2026-09-13 | active |\n''', encoding="utf-8")

decision_log = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-169`" not in decision_log and "`DEC-170`" not in decision_log
decision_log_path.write_text(decision_log.rstrip() + '''\n\n| `DEC-169` | 2026-09-13 | PORTFOLIO-R24 selects US-RCRA-N01 at 41/45. / F01 PASS 후 paired-CEI surveillance-control 설계 gate 선정. | F01 removed source/join risk; surveillance remains the highest-value unresolved validity threat. | Issue #122; `CLM-163`; `research/PORTFOLIO-R24/RESULT.md` | active |\n| `DEC-170` | 2026-09-13 | Authorize Issue #123 outcome-blind paired-CEI design-identifiability only. / `FOUND_VIOLATION` 비개방 N01 승인. | Must prove frozen disaster identity and same-facility pre/post CEI structural support before any compliance result is opened. | Issue #123; `research/US-RCRA-N01/README.md` | active |\n''', encoding="utf-8")

status_path.write_text('''---
checkpoint_id: CHK-20260913-US-RCRA-N01-ACTIVE
active_issue: 123
active_research: US-RCRA-N01
last_completed_issue: 122
last_completed_research: PORTFOLIO-R24
last_decision: DEC-170
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R24_SELECTED_US_RCRA_N01__US_RCRA_N01_ACTIVE`

PORTFOLIO-R24 selected **US-RCRA-N01** at **41/45**. Issue #123 is the only active research gate. F01 source/join/time feasibility is already PASS; N01 now tests whether a same-facility paired pre/post CEI design has sufficient structural support while `FOUND_VIOLATION` and all disaster-linked compliance outcomes remain unopened.

## Exact next action / 정확한 다음 행동

Execute Issue #123 outcome-blind. Enumerate deterministic CEI identity; assign frozen qualifying FEMA DR events; construct last-pre/first-post CEI pairs with the fixed washout, ±730-day and multi-disaster rules; then adjudicate structural thresholds only. Do not open selected-pair compliance results.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

handoff_path.write_text('''---
checkpoint_id: CHK-20260913-US-RCRA-N01-ACTIVE
active_issue: 123
active_research: US-RCRA-N01
last_completed_issue: 122
last_completed_research: PORTFOLIO-R24
last_decision: DEC-170
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

PORTFOLIO-R24 selected US-RCRA-N01 at 41/45 and authorized Issue #123 outcome-blind only.

F01 durable facts: 640 operating TSDFs; 640/640 exact county-FIPS qualification across 52 state/territory FIPS codes; broad FEMA overlap; RCRA evaluation/violation temporal support through 2025. No disaster-linked outcome was opened.

Exact restart: execute N01 using only facility, FEMA disaster and RCRA evaluation type/date/agency identities. Frozen exposure is FEMA `DR` acute physical hazards, index 2018-2023 after 365-day washout. Pair last CEI in prior 730 days with first CEI in next 730 days; exclude a pair if another qualifying disaster occurs before the selected post CEI. PASS requires >=100 pairs, >=20 states/territories and >=95% agency identity. `FOUND_VIOLATION` must remain unopened. Cost: **0 USD**.
''', encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-RCRA-N01-ACTIVE",
    "active_issue": 123,
    "active_research": "US-RCRA-N01",
    "last_completed_issue": 122,
    "last_completed_research": "PORTFOLIO-R24",
    "last_decision": "DEC-170",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"selected": "US-RCRA-N01", "score": 41, "active_issue": 123, "cost_usd": 0}))
