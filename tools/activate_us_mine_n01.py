#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE = 135
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
readme_p = ROOT / "research" / "US-MINE-N01" / "README.md"
dec_p = ROOT / "registry" / "DEC-185.md"

c = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert c["active_issue"] == "none"
assert c["active_research"] == "NONE"
assert c["last_completed_issue"] == 134
assert c["last_completed_research"] == "US-MINE-F01"
assert c["last_decision"] == "DEC-184"
assert "US_MINE_F01_PASS__N01_AUTHORIZATION_REQUIRED" in status_p.read_text(encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
assert "state: AUTHORIZED_OUTCOME_BLIND_DESIGN" in readme
assert "injury_outcome_values_opened: false" in readme
assert "accident_source_read: false" in readme
assert "ALL_SECTOR_OPERATOR_HOURS_RAMP_UP" in readme
assert dec_p.exists() and "DEC-185" in dec_p.read_text(encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-185`" not in dec_log:
    dec_log += "\n| `DEC-185` | 2026-09-16 | Authorize Issue #135 / US-MINE-N01 and freeze the all-sector operator-hours ramp-up exposure family before any accident/injury outcome access. / #135 US-MINE-N01에서 사고·부상 결과 개봉 전 전-sector operator-hours ramp-up exposure를 고정. | F01 established near-complete HOURS_WORKED support in both sectors while production remains non-comparable across Coal+MNM; N01 therefore uses employment exposure only and reads no accident source. | Issue #135; `research/US-MINE-N01/README.md`; `registry/DEC-185.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-US-MINE-N01-ACTIVE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: 135
active_research: US-MINE-N01
last_completed_issue: 134
last_completed_research: US-MINE-F01
last_decision: DEC-185
updated: 2026-09-16
---
"""
next_action = (
    "Execute US-MINE-N01 exactly as preregistered using Mines + MinesProdQuarterly only. "
    "Verify exact F01 source hashes first, then compute exposure-only three-quarter support, deterministic matching and pair fingerprint. "
    "Do not read the Accidents source or any injury field/value; no fallback/rescue."
)
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `US_MINE_N01_ACTIVE__OUTCOME_BLIND_HOURS_RAMP_DESIGN`

Issue #135 / US-MINE-N01 is active under DEC-185. Exactly one exposure family is frozen: **`ALL_SECTOR_OPERATOR_HOURS_RAMP_UP`**, using operator `HOURS_WORKED` across Coal + Metal/Nonmetal with exact sector stratification.

`PRODUCTION_SCOPE_RESTRICTED` remains binding. N01 must not read the Accidents source and must not access injury outcomes.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")
handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

Issue #135 / US-MINE-N01 is active and outcome-blind under DEC-185. The exposure family, support window, quantile thresholds, exact matching fields and minimum support gates are frozen in `research/US-MINE-N01/README.md`.

N01 may parse operator `HOURS_WORKED` magnitudes only for the preregistered exposure design. It may not read the Accidents source, injury outcomes or production magnitude.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")
checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": ISSUE,
    "active_research": "US-MINE-N01",
    "last_completed_issue": 134,
    "last_completed_research": "US-MINE-F01",
    "last_decision": "DEC-185",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "state": "US_MINE_N01_ACTIVE__OUTCOME_BLIND_HOURS_RAMP_DESIGN",
    "issue": ISSUE,
    "last_decision": "DEC-185",
    "accident_source_read": False,
    "injury_outcomes_opened": False,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
