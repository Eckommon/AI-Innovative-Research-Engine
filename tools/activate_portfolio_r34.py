#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 149
DECISION = "DEC-210"
STATE = "PORTFOLIO_R34_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING"
TODAY = "2026-09-17"
CONTRACT_COMMIT = "db56429107fc1a7054b9be0b5a78d91424f72971"


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
        "checkpoint_id": "CHK-20260917-US-FTA-TRANSIT-N01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 148,
        "last_completed_research": "US-FTA-TRANSIT-N01",
        "last_decision": "DEC-209",
        "updated": TODAY,
    }

    contract_path = ROOT / "research" / "PORTFOLIO-R34" / "README.md"
    contract = contract_path.read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN__ISSUE_BINDING_REQUIRED" in contract
    for c in ("US-EPA-XMEDIA-001", "US-BTS-PORT-001", "US-USCG-VESSEL-001", "US-MSHA-001"):
        assert c in contract
    assert "US-FTA-TRANSIT-001`: immediate post-HOLD rescue is prohibited" in contract
    assert not (ROOT / "research" / "PORTFOLIO-R34" / "SCORECARD.md").exists()
    assert not (ROOT / "research" / "PORTFOLIO-R34" / "SOURCE_REVALIDATION.md").exists()

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: {TODAY}
issue: {ISSUE}
research: PORTFOLIO-R34
status: active
---

# {DECISION} — Authorize PORTFOLIO-R34 frozen cross-domain reselection

## Decision / 결정

Authorize Issue #{ISSUE} to revalidate current official sources, internal portfolio overlap, and external literature overlap for exactly the four candidates frozen in `research/PORTFOLIO-R34/README.md`, then score that pool exactly once under the frozen /45 Mission-ROI rubric.

## Governance / 거버넌스

The ordering is binding:

`candidate/rule contract → Issue binding → source/internal-history/literature revalidation → immutable scorecard → at most one selection`.

The post-contract discovery that prior `US-RCRA-*`, `US-PORT-F01`, and `US-MINE-*` branches exist **must not alter the frozen candidate pool**. Instead their overlap is evidence to be recorded conservatively in `SOURCE_REVALIDATION.md` and reflected in novelty / information-gain scoring.

No candidate outcome magnitude, exposure-stratified outcome count, coefficient, predictive score, relationship direction, or downstream event membership may be opened during R34.

`US-FTA-TRANSIT-001` remains excluded from immediate post-HOLD rescue.

## Cost / 비용

Incremental monetary cost remains **0 USD**. No unofficial mirror, authentication bypass, paid source, paid API, or paid runner is authorized.
''', encoding="utf-8")

    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | {TODAY} | Authorize PORTFOLIO-R34 frozen four-candidate cross-domain source/internal-history/literature revalidation and one-time scoring. / R34 고정 4후보 source·내부이력·문헌 재검증 및 단회 scoring 승인. | Contract `{CONTRACT_COMMIT}` precedes Issue #149; post-contract discovery of prior RCRA/PORT/MINE branches may affect scores but not candidate membership. | Issue #149; `research/PORTFOLIO-R34/README.md`; `registry/{DECISION}.md` | active |\n",
    )

    status = f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R34-ACTIVE
active_issue: {ISSUE}
active_research: PORTFOLIO-R34
last_completed_issue: 148
last_completed_research: US-FTA-TRANSIT-N01
last_decision: {DECISION}
updated: {TODAY}
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R34 is active under Issue #{ISSUE} / {DECISION}. Exactly four candidates were frozen before Issue binding and before score persistence: `US-EPA-XMEDIA-001`, `US-BTS-PORT-001`, `US-USCG-VESSEL-001`, and `US-MSHA-001`. No candidate outcome magnitude or relationship has been opened.

Internal repository history discovered after contract freeze includes prior `US-RCRA-*`, `US-PORT-F01`, and `US-MINE-*` branches. The candidate pool will not be rewritten post hoc; the overlap must be explicitly evaluated in source/literature revalidation and scoring.

## Exact next action / 정확한 다음 행동

Inspect the prior internal RCRA, port and mine branches plus current official source identity/access semantics and external direct-overlap literature for all four frozen candidates. Persist `research/PORTFOLIO-R34/SOURCE_REVALIDATION.md`. Only after that file is durable may one immutable `SCORECARD.md` be created and at most one next outcome-blind F01 be selected.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-PORTFOLIO-R34-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "PORTFOLIO-R34",
        "last_completed_issue": 148,
        "last_completed_research": "US-FTA-TRANSIT-N01",
        "last_decision": DECISION,
        "updated": TODAY,
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R34-ACTIVE
active_issue: {ISSUE}
active_research: PORTFOLIO-R34
last_completed_issue: 148
last_completed_research: US-FTA-TRANSIT-N01
last_decision: {DECISION}
updated: {TODAY}
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- contract commit: `{CONTRACT_COMMIT}`
- frozen candidates: `US-EPA-XMEDIA-001`, `US-BTS-PORT-001`, `US-USCG-VESSEL-001`, `US-MSHA-001`
- internal prior-branch overlap discovered after freeze: `US-RCRA-*`, `US-PORT-F01`, `US-MINE-*`
- scorecard created: `false`
- candidate outcomes opened: `false`
- monetary cost: `0 USD`

## Exact restart point / 정확한 재개점

Perform source/internal-history/literature revalidation for all four frozen candidates, explicitly accounting for prior repository branches without altering candidate membership. Persist `SOURCE_REVALIDATION.md`, then create the immutable scorecard exactly once and select at most one separate outcome-blind F01.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
