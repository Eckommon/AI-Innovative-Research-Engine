#!/usr/bin/env python3
"""Finalize PORTFOLIO-R26 selection and activate US-BRIDGE-F01."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "research/PORTFOLIO-R26/RESULT.md",
    ROOT / "research/US-BRIDGE-F01/README.md",
    ROOT / "registry/CLM-167.md",
    ROOT / "registry/DEC-175.md",
    ROOT / "registry/DEC-176.md",
]
for p in required:
    if not p.exists():
        raise SystemExit(f"missing prerequisite: {p.relative_to(ROOT)}")

claim_log = ROOT / "registry/CLAIM_LEDGER.md"
claim_text = claim_log.read_text(encoding="utf-8")
if "`CLM-167`" not in claim_text:
    claim_text = claim_text.rstrip() + "\n| `CLM-167` | PORTFOLIO-R26 outcome-blind comparison selects US-BRIDGE-F01 at 41/45 for source/identity/time feasibility; no bridge condition values were opened and static NBI hazard mapping is explicitly non-novel. / R26은 bridge condition 값을 열지 않고 US-BRIDGE-F01을 41/45로 선택하며 static NBI hazard mapping의 신규성을 주장하지 않는다. | `OBSERVED/DERIVED` | `V2_PRIMARY_VERIFIED` | Issue #126; `research/PORTFOLIO-R26/RESULT.md` | 2026-09-13 | active |\n"
    claim_log.write_text(claim_text, encoding="utf-8")

dec_log = ROOT / "registry/DECISION_LOG.md"
dec_text = dec_log.read_text(encoding="utf-8")
if "`DEC-175`" not in dec_text:
    dec_text = dec_text.rstrip() + "\n| `DEC-175` | 2026-09-13 | Select US-BRIDGE-F01 at 41/45 after terminal US-RCRA-E01; preserve overlap boundary for static bridge-hazard mapping and generic NBI deterioration. / terminal US-RCRA-E01 이후 US-BRIDGE-F01을 41/45로 선택하되 static hazard mapping·일반 NBI deterioration의 중복경계를 보존한다. | Exact national identity/time route and high next-gate information gain without opening outcomes. | Issue #126; `CLM-167`; `research/PORTFOLIO-R26/RESULT.md` | active |\n"
if "`DEC-176`" not in dec_text:
    dec_text = dec_text.rstrip() + "\n| `DEC-176` | 2026-09-13 | Authorize Issue #127 US-BRIDGE-F01 for outcome-blind 2015–2025 NBI identity/panel + FEMA county/time feasibility only; condition-rating values remain closed. / #127은 NBI identity/panel×FEMA time feasibility만 허용하고 condition 값은 닫아 둔다. | Separate feasibility from relationship testing and prevent post-value repair. | Issue #127; `research/US-BRIDGE-F01/README.md` | active |\n"
    dec_log.write_text(dec_text, encoding="utf-8")
else:
    dec_log.write_text(dec_text, encoding="utf-8")

front = """---
checkpoint_id: CHK-20260913-US-BRIDGE-F01-ACTIVE
active_issue: 127
active_research: US-BRIDGE-F01
last_completed_issue: 126
last_completed_research: PORTFOLIO-R26
last_decision: DEC-176
updated: 2026-09-13
---
"""
status = front + """
# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R26_SELECTED_US_BRIDGE_F01__US_BRIDGE_F01_ACTIVE`

PORTFOLIO-R26 selected **US-BRIDGE-F01** at **41/45** after terminal US-RCRA-E01. Issue #127 is the only active research gate.

## Exact next action / 정확한 다음 행동

Execute the frozen outcome-blind US-BRIDGE-F01 feasibility contract: prove 2015–2025 FHWA NBI bridge identity continuity, county-FIPS support, distinct inspection-date support, FEMA 2015–2024 county/time overlap, and condition-field header availability. Do **not** parse or compute bridge condition-rating values or any hazard-condition relationship.

Static bridge-hazard mapping and generic NBI deterioration modeling are not novelty claims. Incremental monetary cost remains **0 USD**.
"""
(ROOT / "STATUS.md").write_text(status, encoding="utf-8")

handoff = front + """
# Session Handoff / 세션 인수인계

PORTFOLIO-R26 selected **US-BRIDGE-F01** at **41/45** and closed Stage 0 selection. Issue #127 is active under `DEC-176`.

Frozen F01 boundary: FHWA NBI legacy archives 2015–2025 + FEMA DisasterDeclarationsSummaries v2; exact State Code + Structure Number bridge identity; exact county FIPS; actual inspection-date support; condition-field identity only. Bridge condition-rating values remain unopened and no relationship is authorized.

PASS thresholds and PASS/PARTIAL/HOLD dispositions are frozen in `research/US-BRIDGE-F01/README.md`. 2026 SNBI outcomes are outside F01. No fuzzy/post-value repair. Static hazard mapping is already established by BTS and is not a novelty claim.

Exact restart: execute US-BRIDGE-F01 outcome-blind source/identity/time probe. Cost: **0 USD**.
"""
(ROOT / "context/SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

checkpoint = {
    "checkpoint_id": "CHK-20260913-US-BRIDGE-F01-ACTIVE",
    "active_issue": 127,
    "active_research": "US-BRIDGE-F01",
    "last_completed_issue": 126,
    "last_completed_research": "PORTFOLIO-R26",
    "last_decision": "DEC-176",
    "updated": "2026-09-13",
}
(ROOT / "context/checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
print(json.dumps(checkpoint, sort_keys=True))
