#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
readme_p = ROOT / "research" / "US-BRIDGE-E01" / "README.md"
dec_p = ROOT / "registry" / "DEC-180.md"

status = status_p.read_text(encoding="utf-8")
assert "last_completed_issue: 131" in status
assert "last_completed_research: US-BRIDGE-N01" in status
assert "last_decision: DEC-179" in status
assert "active_issue: none" in status
assert "US_BRIDGE_N01_PASS__E01_AUTHORIZATION_REQUIRED" in status
assert readme_p.exists() and dec_p.exists()

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-180`" not in dec_log:
    dec_log += "\n\n| `DEC-180` | 2026-09-14 | Authorize Issue #132 / US-BRIDGE-E01 single preregistered matched-pair outcome test after exact N01 pair identity revalidation. / #132 E01 단일 사전등록 결과검정 승인. | N01 fixed 89,800 outcome-blind pairs; E01 may open Items 58/59/60/62 only after exact pair fingerprint and artifact-hash PASS, with frozen deterioration/McNemar/+5pp gates and no post-value rescue. | Issue #132; `research/US-BRIDGE-E01/README.md`; `registry/DEC-180.md` | active |\n"
    dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260914-US-BRIDGE-E01-ACTIVE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: 132
active_research: US-BRIDGE-E01
last_completed_issue: 131
last_completed_research: US-BRIDGE-N01
last_decision: DEC-180
updated: 2026-09-14
---
"""
status_p.write_text(front + """
# Project Status / 프로젝트 상태

**State / 상태:** `US_BRIDGE_E01_ACTIVE__PAIR_IDENTITY_REVALIDATION_FIRST`

US-BRIDGE-N01 / Issue #131 is terminal at `PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE`. Issue #132 / **US-BRIDGE-E01** is the sole intended active research experiment under DEC-180.

The E01 runner MUST validate the frozen N01 artifact before any NBI condition byte is sliced or decoded: 89,800 pairs, pair identity SHA-256 `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`, compressed artifact SHA-256 `4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3`, 15,245 CULVERT and 74,555 NON_CULVERT. Any mismatch is a pre-outcome fail-closed HOLD.

## Exact next action / 정확한 다음 행동

Execute the single frozen E01 runner. Only after identity PASS may it open Items 58/59/60/62, construct the preregistered deterioration indicators, retain complete matched pairs, run the exact two-sided McNemar/binomial test once, and apply the frozen +5pp / p<0.05 dispositions without rescue.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + """
# Session Handoff / 세션 인수인계

US-BRIDGE-N01 / Issue #131 is terminal at `PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE` from Run `34791950311`. State Integrity after closure also passed. N01 froze 89,800 deterministic outcome-blind matched pairs: 15,245 CULVERT and 74,555 NON_CULVERT; pair identity SHA-256 `a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9`; compressed pair artifact SHA-256 `4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3`.

Issue #132 / **US-BRIDGE-E01** is active under DEC-180. E01 must first reproduce the exact N01 pair artifact. Only after PASS may it open the frozen condition fields. CULVERT uses Item 62. NON_CULVERT uses the same common numeric component set from Items 58/59/60 at both endpoints, requires >=2 components, and scores the minimum. Deterioration is a decline of >=1 grade. Primary analysis is complete matched pairs, RD = exposed minus control risk, exact two-sided McNemar/binomial, p<0.05, +5pp positive-materiality floor. No post-value rescue; negative RD is not a protective-effect claim.

Exact restart: execute E01 once, persist staging evidence, then finalize canonical state. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": 132,
    "active_research": "US-BRIDGE-E01",
    "last_completed_issue": 131,
    "last_completed_research": "US-BRIDGE-N01",
    "last_decision": "DEC-180",
    "updated": "2026-09-14"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"checkpoint_id": checkpoint_id, "active_issue": 132, "last_decision": "DEC-180"}))
