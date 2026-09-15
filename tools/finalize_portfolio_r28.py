#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE = 136
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
result_p = ROOT / "research" / "PORTFOLIO-R28" / "RESULT.md"
claim_p = ROOT / "registry" / "CLM-174.md"
dec_p = ROOT / "registry" / "DEC-187.md"

c = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert c["active_issue"] == "none"
assert c["active_research"] == "NONE"
assert c["last_completed_issue"] == 135
assert c["last_completed_research"] == "US-MINE-N01"
assert c["last_decision"] == "DEC-186"
assert "US_MINE_N01_HOLD__PORTFOLIO_RETURN" in status_p.read_text(encoding="utf-8")

result = result_p.read_text(encoding="utf-8")
assert "selected_candidate: US-UTIL-post-F02" in result
assert "selected_gate: US-UTIL-N01" in result
assert "candidate_outcomes_opened: false" in result
assert "US-UTIL 1 > US-PIPE 0" in result
assert claim_p.exists() and dec_p.exists()

claim_log = claim_log_p.read_text(encoding="utf-8")
if "`CLM-174`" not in claim_log:
    claim_log += "\n\n| `CLM-174` | PORTFOLIO-R28 selects US-UTIL post-F02 for one outcome-blind US-UTIL-N01 descendant-design gate after a frozen 37=37 tie is resolved by the preregistered low-overlap tie-break; no candidate magnitude was opened. / R28에서 US-UTIL N01 결과 비개봉 설계 게이트를 선정. | `DERIVED/PORTFOLIO_CONTROL` | `V2_PRIMARY_VERIFIED` | Issue #136; `research/PORTFOLIO-R28/RESULT.md`; `registry/CLM-174.md` | 2026-09-16 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-187`" not in dec_log:
    dec_log += "\n| `DEC-187` | 2026-09-16 | PORTFOLIO-R28 selects US-UTIL post-F02 for one separate outcome-blind US-UTIL-N01 descendant-design gate. / R28에서 US-UTIL N01을 선정. | US-UTIL and US-PIPE tie at 37/45; frozen tie-break: Next-gate info 2=2, then Low overlap/novelty 1>0 selects US-UTIL. US-MINE is terminal and not rescued. | Issue #136; `CLM-174`; `research/PORTFOLIO-R28/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-PORTFOLIO-R28-COMPLETE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: PORTFOLIO-R28
last_decision: DEC-187
updated: 2026-09-16
---
"""
next_action = (
    "Open exactly one separate US-UTIL-N01 outcome-blind descendant-design authorization. "
    "Freeze one AMI/adoption exposure family, one comparable Reliability basis, timing, repeated-unit/comparator structure, materiality, panel dependence handling and non-causal claim boundary before opening Reliability or AMI magnitudes."
)
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R28_SELECTED_US_UTIL_N01__AUTHORIZATION_REQUIRED`

PORTFOLIO-R28 / Issue #136 is complete. **US-UTIL post-F02** is selected for one outcome-blind `US-UTIL-N01` descendant-design gate. US-UTIL and US-PIPE tied at 37/45; the prospectively frozen tie-break selected US-UTIL on Low overlap / novelty risk after Next-gate information gain remained tied.

No Reliability, AMI, storm-severity or candidate relationship magnitude was opened in R28. US-MINE remains terminal HOLD and is not rescued.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")
handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

PORTFOLIO-R28 / Issue #136 is complete at **`SELECT_US_UTIL_N01_OUTCOME_BLIND_DESCENDANT_DESIGN`**. The candidate pool and tie-break were frozen before scoring. US-UTIL post-F02 and US-PIPE scored 37/45; the tie resolved prospectively in favor of US-UTIL by Low overlap / novelty risk 1>0 after Next-gate information gain tied 2=2. C-EU-004 remains preserved at 36/45.

No candidate outcome magnitude was opened. US-MINE-N01 remains terminal HOLD with no rescue.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")
checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": ISSUE,
    "last_completed_research": "PORTFOLIO-R28",
    "last_decision": "DEC-187",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "gate": "SELECT_US_UTIL_N01_OUTCOME_BLIND_DESCENDANT_DESIGN",
    "issue": ISSUE,
    "selected_candidate": "US-UTIL-post-F02",
    "score": 37,
    "candidate_outcomes_opened": False,
    "last_decision": "DEC-187",
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
