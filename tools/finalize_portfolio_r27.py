#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE = 133
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
result_p = ROOT / "research" / "PORTFOLIO-R27" / "RESULT.md"
claim_p = ROOT / "registry" / "CLM-171.md"
dec_p = ROOT / "registry" / "DEC-182.md"

status = status_p.read_text(encoding="utf-8")
checkpoint = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert checkpoint["active_issue"] == "none"
assert checkpoint["active_research"] == "NONE"
assert checkpoint["last_completed_issue"] == 132
assert checkpoint["last_completed_research"] == "US-BRIDGE-E01"
assert checkpoint["last_decision"] == "DEC-181"
assert "US_BRIDGE_E01_NO_POSITIVE_RELATIONSHIP__PORTFOLIO_RETURN" in status

result = result_p.read_text(encoding="utf-8")
assert "selected_candidate: US-MINE-001" in result
assert "selected_gate: US-MINE-F01" in result
assert "candidate_outcomes_opened: false" in result
assert "**39** | **SELECT_STAGE0_ONLY**" in result
assert claim_p.exists() and dec_p.exists()
assert "US-MINE-F01" in claim_p.read_text(encoding="utf-8")
assert "US-MINE-F01" in dec_p.read_text(encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
if "`CLM-171`" not in claim_log:
    claim_log += "\n\n| `CLM-171` | PORTFOLIO-R27 selects US-MINE-001 at 39/45 for one outcome-blind US-MINE-F01 structural feasibility gate; no injury or exposure magnitude was opened. / R27에서 US-MINE-001을 결과 비개봉 F01로 선정. | `DERIVED/PORTFOLIO_CONTROL` | `V2_PRIMARY_VERIFIED` | Issue #133; `research/PORTFOLIO-R27/RESULT.md`; `registry/CLM-171.md` | 2026-09-16 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-182`" not in dec_log:
    dec_log += "\n| `DEC-182` | 2026-09-16 | PORTFOLIO-R27 selects US-MINE-F01 at 39/45 for Stage-0 feasibility only. / R27에서 US-MINE-F01 결과 비개봉 feasibility만 선정. | Highest current marginal information value after durable-state reconstruction; US-UTIL is F02-consumed/high-overlap, US-PIPE direct-overlap, C-EU-004 weaker direct outcome. | Issue #133; `CLM-171`; `research/PORTFOLIO-R27/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-PORTFOLIO-R27-COMPLETE"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: PORTFOLIO-R27
last_decision: DEC-182
updated: 2026-09-16
---
"""

next_action = (
    "Open exactly one separate US-MINE-F01 outcome-blind feasibility authorization. "
    "Verify MSHA source, mine-quarter/subunit, operator/contractor and reporting-comparability semantics; "
    "do not open injury magnitudes or compute an exposure-to-injury relationship."
)

status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `PORTFOLIO_R27_SELECTED_US_MINE_F01__AUTHORIZATION_REQUIRED`

PORTFOLIO-R27 / Issue #133 is complete. **US-MINE-001** is selected at **39/45** for one outcome-blind `US-MINE-F01` structural feasibility gate. The selection is a portfolio-control decision, not an injury finding. Candidate outcome magnitudes remain unopened.

Key boundary: official MSHA documentation indicates that Metal/Nonmetal operators are not required to report production. A production-based national exposure therefore cannot be assumed; F01 must resolve sector/reporting comparability from source semantics/support before any outcome access.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

PORTFOLIO-R27 / Issue #133 is complete at **`SELECT_US_MINE_F01_OPERATIONAL_STRESS_INJURY_FEASIBILITY`**. R27 reused the R26 /45 rubric but scored current marginal information value after reconstructing durable candidate state. US-MINE-001 leads at 39/45; no injury/exposure magnitude or relationship was opened.

US-UTIL already completed F01/F02 and remains high-overlap; US-PIPE remains direct-overlap; C-EU-004 remains a preserved unexecuted join asset but has a less direct operational outcome framing.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": ISSUE,
    "last_completed_research": "PORTFOLIO-R27",
    "last_decision": "DEC-182",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "gate": "SELECT_US_MINE_F01_OPERATIONAL_STRESS_INJURY_FEASIBILITY",
    "issue": ISSUE,
    "score": 39,
    "outcomes_opened": False,
    "next_action": next_action,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
