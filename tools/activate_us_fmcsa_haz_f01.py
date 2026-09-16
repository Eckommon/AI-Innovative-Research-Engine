#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 145
DECISION = "DEC-202"
STATE = "US_FMCSA_HAZ_F01_ACTIVE__OUTCOME_BLIND_SOURCE_SCHEMA_CARRIER_TIME"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R32-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 144,
        "last_completed_research": "PORTFOLIO-R32",
        "last_decision": "DEC-201",
        "updated": "2026-09-16",
    }
    contract = (ROOT / "research" / "US-FMCSA-HAZ-F01" / "README.md").read_text(encoding="utf-8")
    assert "CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "fx4q-ay7w" in contract and "876r-jsdb" in contract
    assert "PASS_US_FMCSA_HAZ_F01_CARRIER_TIME_JOIN_READY" in contract
    assert "PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED" in contract
    assert "HOLD_US_FMCSA_HAZ_F01_SOURCE_SCHEMA_OR_IDENTITY" in contract
    assert not (ROOT / "research" / "US-FMCSA-HAZ-F01" / "STAGING_RESULT.json").exists()

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FMCSA-HAZ-F01
status: active
---

# {DECISION} — Authorize US-FMCSA-HAZ-F01 outcome-blind source/schema/carrier-time feasibility

## Decision / 결정

Authorize Issue #{ISSUE} to execute only the preregistered official-source feasibility contract in `research/US-FMCSA-HAZ-F01/README.md`.

## Boundaries / 경계

- exact FMCSA USDOT ↔ PHMSA Highway FED DOT ID only;
- no carrier-name/address/fuzzy repair;
- no incident occurrence/rate/count by inspection, violation, OOS, BASIC or derived profile;
- no carrier-level joined incident membership persistence;
- no predictive/causal/federal-safety-rating claim;
- public FMCSA inspection-cohort exclusions remain explicit;
- access-only PHMSA PARTIAL may be used only under its preregistered sole-blocker rule;
- incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Authorize US-FMCSA-HAZ-F01 outcome-blind FMCSA inspection × PHMSA Highway hazmat carrier-ID/time feasibility. / FMCSA inspection×PHMSA hazmat carrier/time 구조 gate 승인. | R32 selected FMCSA-HAZ; exact USDOT↔Highway FED DOT ID, public-cohort boundary and access-only PARTIAL were frozen before Issue #145. | Issue #145; `research/US-FMCSA-HAZ-F01/README.md`; `registry/{DECISION}.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FMCSA-HAZ-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-FMCSA-HAZ-F01
last_completed_issue: 144
last_completed_research: PORTFOLIO-R32
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FMCSA-HAZ-F01 is active under Issue #{ISSUE} / {DECISION}. The official source identities, exact carrier-ID rules, structural thresholds, public-cohort boundary and access-only PHMSA PARTIAL were frozen before Issue binding. No hazmat incident occurrence by FMCSA inspection profile has been opened.

## Exact next action / 정확한 다음 행동

Execute the official-source-only F01 runner. First verify FMCSA Socrata schema/bytes and aggregate structural support; then attempt only the official PHMSA Form 5800.1 public detailed export. Persist aggregate support/fingerprints only, never joined carrier-level incident membership.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-US-FMCSA-HAZ-F01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-FMCSA-HAZ-F01",
        "last_completed_issue": 144,
        "last_completed_research": "PORTFOLIO-R32",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FMCSA-HAZ-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-FMCSA-HAZ-F01
last_completed_issue: 144
last_completed_research: PORTFOLIO-R32
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- FMCSA source IDs: `fx4q-ay7w`, `876r-jsdb`
- PHMSA source: public Form 5800.1 Incident Detailed Report/export
- exact join: FMCSA USDOT == PHMSA Highway FED DOT ID only
- hazmat incident outcome by inspection profile: unopened
- relationship computed: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Run the frozen source/schema/carrier-time feasibility gate. Preserve any implementation failure separately from scientific HOLD/PARTIAL/PASS and do not alter thresholds or switch to unofficial sources.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
