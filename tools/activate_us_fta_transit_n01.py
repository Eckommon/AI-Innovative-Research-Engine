#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 148
DECISION = "DEC-208"
CONTRACT_COMMIT = "c4a7f4ea05954fd013714ee6c891d489a6cfc82f"
STATE = "US_FTA_TRANSIT_N01_ACTIVE__OUTCOME_BLIND_MATCHED_RELIABILITY_DESIGN"


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
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 147,
        "last_completed_research": "US-FTA-TRANSIT-F01",
        "last_decision": "DEC-207",
        "updated": "2026-09-16",
    }

    cpath = ROOT / "research" / "US-FTA-TRANSIT-N01" / "README.md"
    contract = cpath.read_text(encoding="utf-8")
    assert "status: CONTRACT_FROZEN_PRE_ISSUE" in contract
    assert "parent_gate: PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY" in contract
    assert "PASS_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_IDENTIFIABLE" in contract
    assert "HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE" in contract
    assert "safety_outcome_row_values_opened: false" in contract
    assert "PASS_POSITIVE_MATERIAL_US_FTA_TRANSIT_E01_RELATIONSHIP" in contract
    assert not (cpath.parent / "STAGING_RESULT.json").exists()
    assert not (cpath.parent / "DESIGN_MANIFEST.json").exists()

    for preflight, key in [
        ("SCHEMA_PREFLIGHT.json", "outcome_values_opened"),
        ("QUALITY_FLAG_PREFLIGHT.json", "safety_outcome_values_opened"),
        ("OUTCOME_SCHEMA_PREFLIGHT.json", "outcome_row_values_opened"),
    ]:
        obj = json.loads((cpath.parent / preflight).read_text(encoding="utf-8"))
        assert obj[key] is False
        assert obj["relationship_computed"] is False

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FTA-TRANSIT-N01
status: active
---

# {DECISION} — Authorize US-FTA-TRANSIT-N01 outcome-blind matched reliability design

## Decision / 결정

Authorize Issue #{ISSUE} to execute only the preregistered N01 contract frozen at commit `{CONTRACT_COMMIT}` before Issue binding.

N01 may read only the frozen Breakdowns exposure/service/quality row fields. No Major Safety/Security Event row endpoint is authorized.

## Frozen design boundary / 고정 경계

- exposure = major mechanical failures per 1,000,000 vehicle/passenger-car revenue miles;
- source-native NTD ID × mode × TOS × year only;
- Q/W/unknown quality markers fail closed at whole agency-mode-year;
- one agency contributes at most one mode;
- deterministic HIGH/LOW quartile and VRM matching only;
- future Safety-only outcome definition and matched E01 statistic are already frozen but may not be executed in N01;
- no safety outcome occurrence/count/severity, relationship, prediction, ranking or causality;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | 2026-09-16 | Authorize US-FTA-TRANSIT-N01 outcome-blind matched reliability design. / FTA transit N01 노출측 매칭 설계 승인. | F01 PASS; N01 contract `{CONTRACT_COMMIT}` frozen before Issue #148; Major Safety/Security row values remain unopened. | Issue #148; `research/US-FTA-TRANSIT-N01/README.md`; `registry/{DECISION}.md` | active |\n",
    )

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-N01-ACTIVE
active_issue: {ISSUE}
active_research: US-FTA-TRANSIT-N01
last_completed_issue: 147
last_completed_research: US-FTA-TRANSIT-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FTA-TRANSIT-N01 is active under Issue #{ISSUE} / {DECISION}. The exposure measure, Q/W fail-closed rules, TOS aggregation, temporal eligibility, one-agency rule, strata/quartiles, deterministic VRM matching, 17 PASS requirements and future E01 Safety-only/McNemar contract were frozen before Issue binding. No Major Safety/Security Event row value has been opened.

## Exact next action / 정확한 다음 행동

Execute the frozen N01 runner against official Breakdowns `amkt-4ehs` only. Persist an outcome-blind deterministic pair manifest and its fingerprint, then apply the exact PASS/HOLD gate. Do not call the Major Safety/Security event row endpoint.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-N01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-FTA-TRANSIT-N01",
        "last_completed_issue": 147,
        "last_completed_research": "US-FTA-TRANSIT-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-N01-ACTIVE
active_issue: {ISSUE}
active_research: US-FTA-TRANSIT-N01
last_completed_issue: 147
last_completed_research: US-FTA-TRANSIT-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- active Issue: `#{ISSUE}`
- authorization: `{DECISION}`
- contract commit: `{CONTRACT_COMMIT}`
- N01 row source authorized: `amkt-4ehs` only
- Major Safety/Security row endpoint authorized: false
- safety outcome rows opened: false
- relationship/prediction/causality: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Run the frozen exposure-side matched-design construction. No outcome-driven adjustment of thresholds, strata, quality rules or matching is permitted.
''', encoding="utf-8")

    print(json.dumps({"issue": ISSUE, "decision": DECISION, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
