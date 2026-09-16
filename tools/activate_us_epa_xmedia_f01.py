#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 150
DECISION = "DEC-212"
STATE = "US_EPA_XMEDIA_F01_ACTIVE__OUTCOME_BLIND_EXACT_FRS_CROSS_PROGRAM_FEASIBILITY"
CONTRACT_COMMIT = "86a7a01ba3b64160ee21a7ea821536d3d1adbb14"


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
        "checkpoint_id": "CHK-20260917-PORTFOLIO-R34-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 149,
        "last_completed_research": "PORTFOLIO-R34",
        "last_decision": "DEC-211",
        "updated": "2026-09-17",
    }

    contract_path = ROOT / "research" / "US-EPA-XMEDIA-F01" / "README.md"
    contract = contract_path.read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "selected_by: PORTFOLIO-R34" in contract
    assert "selection_decision: DEC-211" in contract
    assert "pipeline_rcra_downloads.zip" in contract
    assert "frs_downloads.zip" in contract
    assert "npdes_downloads.zip" in contract
    assert "PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY" in contract
    assert "HOLD_US_EPA_XMEDIA_F01_SOURCE_SCHEMA_SCOPE_OR_IDENTITY" in contract
    assert "effluent_violation_rows_opened: false" in contract
    assert "relationship_computed: false" in contract
    assert not (ROOT / "research" / "US-EPA-XMEDIA-F01" / "STAGING_RESULT.json").exists()

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-EPA-XMEDIA-F01
status: active
---

# {DECISION} — Authorize US-EPA-XMEDIA-F01 outcome-blind exact FRS cross-program feasibility

## Decision / 결정

Authorize Issue #{ISSUE} to execute only the preregistered official-EPA-source feasibility contract in `research/US-EPA-XMEDIA-F01/README.md`, frozen at commit `{CONTRACT_COMMIT}` before Issue binding.

## Frozen sources / 고정 원천

- EPA ECHO RCRA Pipeline — `pipeline_rcra_downloads.zip`
- EPA ECHO FRS Facilities and Linkages — `frs_downloads.zip`
- EPA ECHO ICIS-NPDES National Dataset Part 1 — `npdes_downloads.zip`

## Hard outcome firewall / 결과 방화벽

- ICIS-NPDES Part 2 / `NPDES_EFF_VIOLATIONS.csv` is forbidden in F01;
- jurisdictional effluent-violation downloads are forbidden;
- DMR outcome values/limits/exceedance rows are forbidden;
- no RCRA-conditioned NPDES occurrence/rate/magnitude or facility ranking;
- exact official FRS identity only; no name/address/geospatial/fuzzy/manual repair;
- no unofficial mirror, paid source/API/runner, or authentication bypass;
- incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | 2026-09-17 | Authorize US-EPA-XMEDIA-F01 outcome-blind RCRA×FRS×NPDES exact cross-program feasibility. / EPA cross-media 구조 gate 승인. | R34 uniquely selected EPA cross-media; pre-Issue contract `{CONTRACT_COMMIT[:8]}...` freezes three official ZIPs, exact FRS identity, 18 PASS requirements and a source-level ban on NPDES Part 2/DMR outcomes. | Issue #150; `research/US-EPA-XMEDIA-F01/README.md`; `registry/{DECISION}.md` | active |\n",
    )

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-EPA-XMEDIA-F01
last_completed_issue: 149
last_completed_research: PORTFOLIO-R34
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-EPA-XMEDIA-F01 is active under Issue #{ISSUE} / {DECISION}. The official RCRA Pipeline, FRS Program Linkages and ICIS-NPDES Part 1 sources, exact FRS identity rules, structural time/cardinality thresholds and all 18 PASS requirements were frozen before Issue binding. NPDES Part 2 effluent-violation rows and DMR outcomes remain unopened and are prohibited in F01.

## Exact next action / 정확한 다음 행동

Build and execute the official-source-only F01 runner. Evaluate source ZIP integrity, required schemas, exact RCRA↔FRS and NPDES↔FRS identity corroboration, structural date support, aggregate exact cross-program Registry-ID overlap and deterministic fingerprints. Do not access Part 2 effluent violations or DMR outcomes.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-F01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-EPA-XMEDIA-F01",
        "last_completed_issue": 149,
        "last_completed_research": "PORTFOLIO-R34",
        "last_decision": DECISION,
        "updated": "2026-09-17",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-F01-ACTIVE
active_issue: {ISSUE}
active_research: US-EPA-XMEDIA-F01
last_completed_issue: 149
last_completed_research: PORTFOLIO-R34
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- pre-Issue contract commit: `{CONTRACT_COMMIT}`
- RCRA source: `pipeline_rcra_downloads.zip`
- FRS source: `frs_downloads.zip`
- NPDES source: `npdes_downloads.zip` (Part 1 only)
- exact identity: official FRS `REGISTRY_ID` bridge only
- NPDES Part 2 opened: false
- DMR outcome rows opened: false
- relationship computed: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Implement and run the frozen F01 source/schema/exact-FRS feasibility gate. Preserve implementation failures separately from scientific PASS/HOLD. Do not alter sources, thresholds, identity rules or outcome firewall after reading source bytes.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
