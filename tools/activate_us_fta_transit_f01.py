#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 147
DECISION = "DEC-206"
STATE = "US_FTA_TRANSIT_F01_ACTIVE__OUTCOME_BLIND_SOURCE_SCHEMA_AGENCY_MODE_TIME"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R33-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 146,
        "last_completed_research": "PORTFOLIO-R33",
        "last_decision": "DEC-205",
        "updated": "2026-09-16",
    }

    contract_path = ROOT / "research" / "US-FTA-TRANSIT-F01" / "README.md"
    contract = contract_path.read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "selected_by: PORTFOLIO-R33" in contract
    assert "selection_decision: DEC-205" in contract
    assert "amkt-4ehs" in contract
    assert "5ti2-5uiv" in contract
    assert "9ivb-8ae9" in contract
    assert "PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY" in contract
    assert "HOLD_US_FTA_TRANSIT_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY" in contract
    assert "candidate_outcome_opened: false" in contract
    assert "relationship_computed: false" in contract
    assert not (ROOT / "research" / "US-FTA-TRANSIT-F01" / "STAGING_RESULT.json").exists()

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FTA-TRANSIT-F01
status: active
---

# {DECISION} — Authorize US-FTA-TRANSIT-F01 outcome-blind source/schema/agency-mode/time feasibility

## Decision / 결정

Authorize Issue #{ISSUE} to execute only the preregistered official-source feasibility contract in `research/US-FTA-TRANSIT-F01/README.md`, frozen at commit `70c41fc8202579436ad7560118548fc1c2a34593` before Issue binding.

## Frozen sources / 고정 원천

- `amkt-4ehs` — 2022–2024 NTD Annual Data - Breakdowns
- `5ti2-5uiv` — Monthly Modal Time Series
- `9ivb-8ae9` — Major Safety and Security Events

## Boundaries / 경계

- exact source-native NTD agency ID × mode only;
- Breakdowns TOS grain must be verified before any structural projection;
- no agency-name/address/fuzzy/manual repair;
- no breakdown-conditioned safety-event count/rate/membership;
- no agency risk ranking, prediction, regression, effect or causal claim;
- no row-level Breakdowns→event joined table persistence;
- no unofficial mirror, paid source/API/runner, or authentication bypass;
- incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | 2026-09-16 | Authorize US-FTA-TRANSIT-F01 outcome-blind NTD Breakdowns × Major Safety Events agency-mode/time feasibility. / FTA Breakdowns×Major Safety Events 구조 gate 승인. | R33 selected FTA by frozen tie-break; contract commit `70c41fc...` precedes Issue #147 and freezes official source IDs, exact NTD-ID×mode identity, TOS scope and 19 PASS requirements. | Issue #147; `research/US-FTA-TRANSIT-F01/README.md`; `registry/{DECISION}.md` | active |\n",
    )

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-FTA-TRANSIT-F01
last_completed_issue: 146
last_completed_research: PORTFOLIO-R33
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FTA-TRANSIT-F01 is active under Issue #{ISSUE} / {DECISION}. The three official source IDs, source-native NTD agency × mode identity, Breakdowns TOS grain, time rules, cardinality/coverage thresholds and all 19 PASS requirements were frozen before Issue binding. No Breakdown-conditioned Major Safety Event occurrence has been opened.

## Exact next action / 정확한 다음 행동

Build and execute the official-source-only F01 runner. Verify Socrata metadata and actual bytes for `amkt-4ehs`, `5ti2-5uiv`, and `9ivb-8ae9`; resolve only source-native structural fields; compute preregistered source/key/time/cardinality/coverage diagnostics and deterministic fingerprints; persist no row-level Breakdowns→event membership and no outcome relationship.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-F01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-FTA-TRANSIT-F01",
        "last_completed_issue": 146,
        "last_completed_research": "PORTFOLIO-R33",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-FTA-TRANSIT-F01
last_completed_issue: 146
last_completed_research: PORTFOLIO-R33
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- contract commit: `70c41fc8202579436ad7560118548fc1c2a34593`
- Breakdowns source: `amkt-4ehs`
- Monthly Modal source: `5ti2-5uiv`
- Major Safety Events source: `9ivb-8ae9`
- exact identity: source-native NTD agency ID × mode only
- Breakdowns TOS grain: frozen and must be verified
- Breakdown-conditioned safety outcome opened: false
- row-level event join persisted: false
- relationship computed: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Implement and run the frozen F01 source/schema/agency-mode/time feasibility gate. Preserve implementation failures separately from scientific PASS/HOLD. Do not change source IDs, thresholds, identity rules, TOS handling or outcome boundaries after reading source bytes.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
