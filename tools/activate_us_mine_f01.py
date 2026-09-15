#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE = 134
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
r27_p = ROOT / "research" / "PORTFOLIO-R27" / "RESULT.md"
readme_p = ROOT / "research" / "US-MINE-F01" / "README.md"
dec_p = ROOT / "registry" / "DEC-183.md"

c = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert c["active_issue"] == "none"
assert c["active_research"] == "NONE"
assert c["last_completed_issue"] == 133
assert c["last_completed_research"] == "PORTFOLIO-R27"
assert c["last_decision"] == "DEC-182"
assert "PORTFOLIO_R27_SELECTED_US_MINE_F01__AUTHORIZATION_REQUIRED" in status_p.read_text(encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
assert "state: AUTHORIZED_OUTCOME_BLIND_FEASIBILITY" in readme
assert "injury_outcome_values_opened: false" in readme
assert "2019-2025" in readme
assert dec_p.exists() and "DEC-183" in dec_p.read_text(encoding="utf-8")

r27 = r27_p.read_text(encoding="utf-8")
if "next_issue: PENDING_STAGE0_AUTHORIZATION" in r27:
    r27 = r27.replace("next_issue: PENDING_STAGE0_AUTHORIZATION", "next_issue: 134")
r27_p.write_text(r27, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-183`" not in dec_log:
    dec_log += "\n| `DEC-183` | 2026-09-16 | Authorize Issue #134 / US-MINE-F01 for outcome-blind source/schema/identity/time/join-support feasibility only. / #134 US-MINE-F01 결과 비개봉 구조 feasibility만 승인. | R27 selected US-MINE; MSHA production reporting is not nationally comparable across Coal+MNM, so F01 must preserve PRODUCTION_SCOPE_RESTRICTED and keep injury outcomes closed. | Issue #134; `research/US-MINE-F01/README.md`; `registry/DEC-183.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-US-MINE-F01-ACTIVE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: 134
active_research: US-MINE-F01
last_completed_issue: 133
last_completed_research: PORTFOLIO-R27
last_decision: DEC-183
updated: 2026-09-16
---
"""
next_action = (
    "Execute US-MINE-F01 exactly as preregistered: source/hash/schema/cardinality/exact structural join support only. "
    "Keep all prohibited injury outcome fields and exposure magnitudes unopened; no threshold/window/source rescue."
)
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `US_MINE_F01_ACTIVE__OUTCOME_BLIND_STRUCTURAL_FEASIBILITY`

Issue #134 / US-MINE-F01 is authorized under DEC-183. Frozen support window: **2019–2025**. Exact structural identity: `MINE_ID + CAL_YR + CAL_QTR + SUBUNIT_CD`. Operator/contractor separation uses only `CONTRACTOR_ID` blank/nonblank.

The MSHA semantic restriction is frozen: Metal/Nonmetal production is not required, so national Coal+MNM production-pressure comparability is not assumed. Injury outcome values remain closed.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")
handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

Issue #134 / US-MINE-F01 is active and outcome-blind under DEC-183. The 2019–2025 window and exact mine-quarter-subunit structural keys are frozen. Do not use injury degree, lost/restricted days, injury magnitude/rate/severity, production-per-hour, or any exposure→injury statistic.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")
checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": ISSUE,
    "active_research": "US-MINE-F01",
    "last_completed_issue": 133,
    "last_completed_research": "PORTFOLIO-R27",
    "last_decision": "DEC-183",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "state": "US_MINE_F01_ACTIVE__OUTCOME_BLIND_STRUCTURAL_FEASIBILITY",
    "issue": ISSUE,
    "last_decision": "DEC-183",
    "injury_outcomes_opened": False,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
