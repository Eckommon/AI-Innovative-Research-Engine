#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / "context"
REG = ROOT / "registry"
DECISION = "DEC-214"
ISSUE = 151
STATE = "US_EPA_XMEDIA_N01_ACTIVE__OUTCOME_BLIND_MATCHED_MONITORING_INTENSITY_DESIGN"


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
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 150,
        "last_completed_research": "US-EPA-XMEDIA-F01",
        "last_decision": "DEC-213",
        "updated": "2026-09-17",
    }

    contract = (ROOT / "research" / "US-EPA-XMEDIA-N01" / "README.md").read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE" in contract
    assert "npdes_effluent_violation_rows_opened: false" in contract
    assert "2021-01-01 through 2023-12-31" in contract
    assert "2024-01-01 through 2024-12-31" in contract

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-EPA-XMEDIA-N01
status: active
---

# {DECISION} — Activate US-EPA-XMEDIA-N01 under frozen outcome-blind contract

Activate Issue #{ISSUE} using the contract frozen before Issue creation at commit `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`.

N01 may build only the deterministic structural exposure/matching manifest. ICIS-NPDES Part 2, E90 membership, DMR values/limits/exceedance, RCRA violation/enforcement outcomes, relationship/prediction/causality and facility ranking remain unauthorized.

Incremental monetary cost remains 0 USD.
''', encoding="utf-8")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-17 | Activate US-EPA-XMEDIA-N01 under pre-Issue frozen matched monitoring-intensity contract; keep all future E90/DMR outcomes closed. / N01 outcome-blind 설계 활성화. | Contract `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`; Issue #151. | Issue #151; `research/US-EPA-XMEDIA-N01/README.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-N01-ACTIVE
active_issue: 151
active_research: US-EPA-XMEDIA-N01
last_completed_issue: 150
last_completed_research: US-EPA-XMEDIA-F01
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-EPA-XMEDIA-N01 is active under the pre-Issue contract frozen at `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`. The design uses baseline RCRA evaluations (2018–2020), recent RCRA monitoring intensity (2021–2023), exact FRS cross-program identity and NPDES Part 1 structural permit covariates only. Future 2024 E90 outcome membership remains unopened.

## Exact next action / 정확한 다음 행동

Execute one immutable structural N01 run and evaluate all 18 frozen requirements without opening any NPDES/RCRA outcome table. Do not relax thresholds or matching rules after observing counts.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-N01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-EPA-XMEDIA-N01",
        "last_completed_issue": 150,
        "last_completed_research": "US-EPA-XMEDIA-F01",
        "last_decision": DECISION,
        "updated": "2026-09-17",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-N01-ACTIVE
active_issue: 151
active_research: US-EPA-XMEDIA-N01
last_completed_issue: 150
last_completed_research: US-EPA-XMEDIA-F01
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- Issue: #151
- contract: `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`
- baseline window: 2018–2020
- exposure window: 2021–2023
- future E01 window: 2024
- E90/DMR/RCRA outcome rows opened: false
- relationship/prediction/causality: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Execute N01 exactly as frozen and persist a deterministic structural pair manifest plus PASS/HOLD staging result. Future E01 remains unauthorized.
''', encoding="utf-8")

    print(json.dumps({"decision": DECISION, "issue": ISSUE, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
