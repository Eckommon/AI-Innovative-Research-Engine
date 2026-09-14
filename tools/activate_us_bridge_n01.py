#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
readme_p = ROOT / "research" / "US-BRIDGE-N01" / "README.md"
dec_p = ROOT / "registry" / "DEC-178.md"

status = status_p.read_text(encoding="utf-8")
assert "last_completed_issue: 127" in status
assert "last_completed_research: US-BRIDGE-F01" in status
assert "last_decision: DEC-177" in status
assert "active_issue: none" in status
assert readme_p.exists() and dec_p.exists()

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-178`" not in dec_log
dec_log += "\n\n| `DEC-178` | 2026-09-14 | Authorize Issue #131 / US-BRIDGE-N01 outcome-blind matched inspection-interval design gate; keep condition Items 58/59/60/62 closed. / #131 N01 결과 비개봉 매칭 점검구간 설계 gate 승인. | F01 established national panel join readiness; N01 must prospectively freeze interval exposure, reconstruction exclusion and deterministic control matching before any condition value access. | Issue #131; `research/US-BRIDGE-N01/README.md`; `registry/DEC-178.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260914-US-BRIDGE-N01-ACTIVE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: 131
active_research: US-BRIDGE-N01
last_completed_issue: 127
last_completed_research: US-BRIDGE-F01
last_decision: DEC-178
updated: 2026-09-14
---
"""
status_p.write_text(front + """
# Project Status / 프로젝트 상태

**State / 상태:** `US_BRIDGE_F01_PASS__US_BRIDGE_N01_ACTIVE`

US-BRIDGE-F01 is terminal at `PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`. Issue #131 / **US-BRIDGE-N01** is now the sole intended active research gate.

N01 is strictly outcome-blind. It may construct consecutive inspection intervals, `DR` FEMA exposure identities, reconstruction exclusions and deterministic exposed/control matching using the frozen non-outcome fields. NBI condition Items 58/59/60/62 remain closed at row-value and byte-slice level.

## Exact next action / 정확한 다음 행동

Execute the frozen US-BRIDGE-N01 design-identifiability runner and persist an exact matched-pair manifest plus fingerprint. Do not open condition-rating values or compute a disaster-linked condition relationship.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + """
# Session Handoff / 세션 인수인계

Issue #127 / US-BRIDGE-F01 closed completed at `PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`. Corrected F01 execution Run `34791209726` established 618,357 bridges with >=6/11-year support, 618,168 with >=2 distinct inspection dates, and FEMA geography overlap across 53 states/territories and 2,764 counties. Condition values were not opened.

Current active work is Issue #131 / **US-BRIDGE-N01** under `DEC-178` and `research/US-BRIDGE-N01/README.md`.

Frozen N01 design: consecutive 180–1095-day inspection intervals; stable county/class; reconstruction-year exclusion; FEMA `DR` physical-hazard exposure; one exposed interval per bridge; controls must have no exposed eligible interval; deterministic 1:1 exact-stratum matching by state × bridge class × pre-inspection year without replacement. Items 58/59/60/62 remain forbidden.

Exact restart: execute N01 outcome-blind and persist exact matched-pair identities/fingerprint. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": 131,
    "active_research": "US-BRIDGE-N01",
    "last_completed_issue": 127,
    "last_completed_research": "US-BRIDGE-F01",
    "last_decision": "DEC-178",
    "updated": "2026-09-14"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"checkpoint_id": checkpoint_id, "active_issue": 131, "last_decision": "DEC-178"}))
