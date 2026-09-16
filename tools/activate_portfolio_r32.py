#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 144
DECISION = "DEC-200"
STATE = "PORTFOLIO_R32_ACTIVE__SOURCE_REVALIDATION_PENDING"


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += row
        path.write_text(text, encoding="utf-8")


def main() -> None:
    cp = json.loads((CTX / "checkpoint.json").read_text(encoding="utf-8"))
    assert cp == {
        "checkpoint_id": "CHK-20260916-US-NHTSA-MC-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 143,
        "last_completed_research": "US-NHTSA-MC-F01",
        "last_decision": "DEC-199",
        "updated": "2026-09-16",
    }

    contract = (ROOT / "research" / "PORTFOLIO-R32" / "README.md").read_text(encoding="utf-8")
    assert "candidate_count: 4" in contract
    assert "CONTRACT_FROZEN_PRE_SCORE" in contract
    for c in ("US-FMCSA-HAZ-001", "US-FTA-TRANSIT-001", "KR-GG-CHEM-001", "US-PIPE-001"):
        assert c in contract
    assert not (ROOT / "research" / "PORTFOLIO-R32" / "SCORECARD.md").exists()

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R32
status: active
---

# {DECISION} — Authorize PORTFOLIO-R32 frozen four-candidate reselection

## Decision / 결정

Authorize Issue #{ISSUE} to revalidate current official sources and score exactly the four candidates frozen in `research/PORTFOLIO-R32/README.md` under the existing /45 Mission-ROI rubric.

## Governance / 거버넌스

The corrected ordering is binding:

`candidate/rule contract → Issue binding → source revalidation → immutable scorecard`.

No candidate may be inserted after Issue binding. No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score, or relationship direction may be opened in R32.

## Cost / 비용

Incremental monetary cost remains **0 USD**. No unofficial mirror, authentication bypass, paid source or paid API is authorized.
''', encoding="utf-8")

    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Authorize PORTFOLIO-R32 frozen four-candidate source revalidation and one-time Mission-ROI scoring. / R32 고정 4후보 source 재검증·단회 scoring 승인. | Contract commit precedes Issue #144; outcomes remain closed and R30 ordering correction is preserved. | Issue #144; `research/PORTFOLIO-R32/README.md`; `registry/{DECISION}.md` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R32-ACTIVE
active_issue: {ISSUE}
active_research: PORTFOLIO-R32
last_completed_issue: 143
last_completed_research: US-NHTSA-MC-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R32 is active under Issue #{ISSUE} / {DECISION}. Exactly four candidates are frozen before scoring: `US-FMCSA-HAZ-001`, `US-FTA-TRANSIT-001`, `KR-GG-CHEM-001`, and `US-PIPE-001`. The candidate/rubric contract commit precedes Issue binding. No candidate outcome magnitude or relationship has been opened.

## Exact next action / 정확한 다음 행동

Revalidate current official sources for the four frozen candidates and persist `research/PORTFOLIO-R32/SOURCE_REVALIDATION.md`. Only after that file is durable may one immutable `SCORECARD.md` be created. Select at most one separate outcome-blind F01.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R32-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "PORTFOLIO-R32",
        "last_completed_issue": 143,
        "last_completed_research": "US-NHTSA-MC-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R32-ACTIVE
active_issue: {ISSUE}
active_research: PORTFOLIO-R32
last_completed_issue: 143
last_completed_research: US-NHTSA-MC-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- frozen candidates: `US-FMCSA-HAZ-001`, `US-FTA-TRANSIT-001`, `KR-GG-CHEM-001`, `US-PIPE-001`
- scorecard created: `false`
- candidate outcomes opened: `false`
- monetary cost: `0 USD`

## Exact restart point / 정확한 재개점

Persist current official-source revalidation for all four candidates. Then score the frozen pool exactly once under the /45 Mission-ROI rubric and select at most one separate outcome-blind F01. Do not rescue terminal NHTSA by switching sources post hoc.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
