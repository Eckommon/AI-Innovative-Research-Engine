#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "PORTFOLIO-R33"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 146
DECISION = "DEC-205"
CLAIM = "CLM-184"
SELECTION = "SELECT_US_FTA_TRANSIT_001_BREAKDOWNS_TO_MAJOR_SAFETY_F01"
STATE = "PORTFOLIO_R33_SELECTED_US_FTA_TRANSIT_001__F01_AUTHORIZATION_REQUIRED"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R33-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "PORTFOLIO-R33",
        "last_completed_issue": 145,
        "last_completed_research": "US-FMCSA-HAZ-F01",
        "last_decision": "DEC-204",
        "updated": "2026-09-16",
    }

    contract = (OUT / "README.md").read_text(encoding="utf-8")
    source = (OUT / "SOURCE_REVALIDATION.md").read_text(encoding="utf-8")
    score = (OUT / "SCORECARD.md").read_text(encoding="utf-8")

    assert "Exactly four candidates are authorized" in contract
    assert "issue: 146" in source
    assert "source_revalidation_commit: ddd37fb2ca4bfc1495009752d19a8ceff5b06b5e" in score
    assert "**US-FTA-TRANSIT-001**" in score and "**37/45**" in score
    assert "US-MSHA-001" in score and "HOLD_DIRECT_OVERLAP_TIEBREAK" in score
    assert "KR-GG-CHEM-001" in score and "**36/45**" in score
    assert "US-FRA-XING-001" in score and "**34/45**" in score
    assert "FTA **3** > MSHA **0**" in score
    assert SELECTION in score
    assert "candidate_outcomes_opened: false" in score

    (OUT / "RESULT.md").write_text(f'''---
id: PORTFOLIO-R33-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: US-FTA-TRANSIT-001
selected_gate: US-FTA-TRANSIT-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R33 Result — Select US-FTA-TRANSIT-001 F01

**`{SELECTION}`**

R33 followed the prospective order:

`candidate/rule contract → Issue #146 → current source/direct-overlap revalidation → immutable scorecard → frozen tie-break`.

No candidate-specific outcome magnitude, exposure-stratified outcome count, coefficient, predictive score or relationship direction was opened.

## Frozen final scores / 최종 고정점수

| Candidate | Total | Disposition |
|---|---:|---|
| **US-FTA-TRANSIT-001** | **37/45** | **SELECT_F01_BY_TIEBREAK** |
| US-MSHA-001 | **37/45** | HOLD_DIRECT_OVERLAP_TIEBREAK |
| KR-GG-CHEM-001 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-FRA-XING-001 | **34/45** | HOLD_HIGH_DIRECT_OVERLAP |

## Frozen tie-break / 고정 동점규칙

FTA and MSHA tie at 37/45. Next-gate information gain is also tied at 4. The next frozen criterion is low-overlap / novelty risk, where **FTA 3 > MSHA 0**. The tie resolves there; no later criterion is consulted.

## Selection meaning / 선정 의미

The selection authorizes exactly one separate **outcome-blind** `US-FTA-TRANSIT-F01`. It does not establish that mechanical breakdown structure predicts later Major Safety Events and does not establish novelty.

The F01 may verify only:

- current official zero-cost FTA/NTD Breakdowns and Safety & Security source access;
- source-native agency × mode identity semantics;
- Type of Service and Full Reporter/reporting-scope handling;
- year/time support and repeated agency-mode structure;
- aggregate structural overlap and deterministic fingerprints;
- whether a prospective agency × mode panel can be frozen without opening safety-event occurrence by breakdown profile.

F01 may **not** open or compare Major Safety Event occurrence/rates/counts conditioned on breakdown intensity, derived reliability class, agency risk profile or any downstream label. No causal or safety-rating claim is authorized.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nIssue #146 ratifies the immutable scorecard without rescoring. **`{SELECTION}`** is selected after the frozen 37/45 tie with MSHA is resolved at the second tie-break criterion, low-overlap / novelty risk (**FTA 3 > MSHA 0**). No candidate outcome was opened.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R33 selects US-FTA-TRANSIT-001 by frozen tie-break

PORTFOLIO-R33 prospectively compares four frozen candidates after current official-source/direct-overlap revalidation. The immutable scorecard is **US-FTA-TRANSIT-001 37/45**, **US-MSHA-001 37/45**, **KR-GG-CHEM-001 36/45**, and **US-FRA-XING-001 34/45**. FTA and MSHA remain tied on next-gate information gain, then FTA wins the frozen low-overlap / novelty-risk tie-break **3 > 0**. Therefore `US-FTA-TRANSIT-001` is selected for one separate outcome-blind F01.

This is a portfolio-control claim only. It does not establish a relationship between mechanical breakdowns and Major Safety Events, any effect direction, prediction, novelty, transit-agency risk ranking or causality.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R33
status: active
---

# {DECISION} — Select US-FTA-TRANSIT-001 for one outcome-blind F01

## Decision / 결정

Ratify the immutable R33 scorecard and frozen tie-break, selecting **`US-FTA-TRANSIT-001`** for exactly one separate `US-FTA-TRANSIT-F01` source/schema/agency-mode/time feasibility gate.

## Rationale / 근거

FTA and MSHA tie at **37/45** and tie again on next-gate information gain. Under the prospectively frozen tie-break, FTA then leads on low-overlap / novelty risk **3 > 0**. No later tie-break dimension is consulted and no candidate outcome is opened.

## Boundary / 경계

- no breakdown-conditioned Major Safety Event occurrence/rate/count;
- no post-hoc fuzzy agency identity repair;
- Type of Service/reporting-scope handling must be frozen prospectively;
- no novelty, causal, transit-agency safety-rating or risk-ranking claim;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | PORTFOLIO-R33 selects US-FTA-TRANSIT-001 after a frozen 37/45 tie with US-MSHA-001 is resolved at low-overlap/novelty risk 3>0; KR-GG-CHEM 36 and US-FRA-XING 34; no candidate outcomes opened. / R33에서 FTA transit 후보를 사전고정 tie-break로 선정. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #146; `research/PORTFOLIO-R33/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Select US-FTA-TRANSIT-001 for one separate outcome-blind F01. / FTA Breakdowns→Major Safety Events 후보를 별도 F01에 한해 선택. | Frozen R33 scorecard: FTA 37 = MSHA 37; tie-break next-info 4=4 then low-overlap/novelty 3>0; outcomes unopened. | Issue #146; `{CLAIM}`; `research/PORTFOLIO-R33/RESULT.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R33-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 146
last_completed_research: PORTFOLIO-R33
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R33 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. Frozen scores: FTA-TRANSIT **37/45**, MSHA **37/45**, KR-GG-CHEM **36/45**, FRA-XING **34/45**. The frozen tie-break resolves FTA over MSHA at low-overlap / novelty risk **3 > 0** after next-gate information gain remains tied. No candidate outcome magnitude or relationship was opened.

## Exact next action / 정확한 다음 행동

Open exactly one separate `US-FTA-TRANSIT-F01` outcome-blind source/schema/agency-mode/time feasibility Issue. Verify current official FTA/NTD Breakdowns and Safety & Security source bytes, exact source-native agency × mode semantics, Type of Service and reporting-scope handling, repeated time support, aggregate structural overlap and deterministic fingerprints. Do not open Major Safety Event occurrence/rates/counts conditioned on any breakdown-derived profile.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R33-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 146,
        "last_completed_research": "PORTFOLIO-R33",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R33-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 146
last_completed_research: PORTFOLIO-R33
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- selected candidate: `US-FTA-TRANSIT-001`
- selected gate: `US-FTA-TRANSIT-F01`
- frozen score: `37/45`
- tie-break: `next-info 4=4 → low-overlap/novelty 3>0`
- candidate outcomes opened: `false`
- monetary cost: `0 USD`

## Exact restart point / 정확한 재개점

Open exactly one `US-FTA-TRANSIT-F01` outcome-blind source/schema/agency-mode/time gate. Verify current official FTA/NTD Breakdowns and Safety & Security source bytes, source-native agency × mode identity, Type of Service/reporting-scope semantics, temporal support, aggregate overlap and deterministic fingerprints. Do not open Major Safety Event occurrence/rates/counts conditioned on breakdown history.
''', encoding="utf-8")

    print(json.dumps({"selection": SELECTION, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
