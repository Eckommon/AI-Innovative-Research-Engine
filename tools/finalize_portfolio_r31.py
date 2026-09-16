#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "PORTFOLIO-R31"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 142
AUTH_DECISION = "DEC-196"
DECISION = "DEC-197"
CLAIM = "CLM-180"
SELECTION = "SELECT_US_NHTSA_MC_001_COMMUNICATION_TO_RECALL_F01"
STATE = "PORTFOLIO_R31_SELECTED_US_NHTSA_MC_001__F01_AUTHORIZATION_REQUIRED"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R31-ACTIVE",
        "active_issue": 142,
        "active_research": "PORTFOLIO-R31",
        "last_completed_issue": 141,
        "last_completed_research": "US-FDA-MD-F01",
        "last_decision": AUTH_DECISION,
        "updated": "2026-09-16",
    }

    readme = (OUT / "README.md").read_text(encoding="utf-8")
    score = (OUT / "SCORECARD.md").read_text(encoding="utf-8")
    assert "US-NHTSA-MC-001" in readme and "KR-GG-CHEM-001" in readme and "US-PIPE-001" in readme
    assert "**39/45**" in score and score.count("**36/45**") >= 2
    assert SELECTION in score
    assert "candidate_outcomes_opened: false" in score

    result = f'''---
id: PORTFOLIO-R31-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: US-NHTSA-MC-001
selected_gate: US-NHTSA-MC-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R31 Result — Select US-NHTSA-MC-001 F01

**`{SELECTION}`**

R31 returns to Stage 0 after terminal FDA access-limited PARTIAL and does not retry the blocked source or automatically promote US-PIPE. The candidate/rubric contract and Issue #142 were both fixed before score persistence. No candidate outcome magnitude or relationship was opened.

## Frozen scorecard / 최종 고정점수

| Candidate | Mission | Cross-source | Direct outcome | Independent-unit | Practical | Zero-cost | Join defensibility | Info gain | Low overlap | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-NHTSA-MC-001** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 2 | **39** | **SELECT_STAGE0_F01_ONLY** |
| KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

NHTSA leads outright, so no tie-break is required.

## Selection basis / 선정 근거

NHTSA publishes current zero-cost Manufacturer Communications/TSB flat files and Safety Recall flat files. The communication dictionary exposes source-native communication ID/date plus Make, Model and Model Year, while recall data support the same product dimensions plus campaign identity. One outcome-blind F01 can therefore test exact normalization, multiplicity, time ordering, cardinality and aggregate source overlap before any recall incidence is opened.

This is not a novelty claim that service bulletins are safety signals. NHTSA itself uses manufacturer communications in Early Warning Reporting and defect analysis. Any descendant must remain a bounded non-causal public-data design and must explicitly handle repeated communications, shared product/platform structure and source-driven model-name normalization.

## Preserved alternatives / 보존 후보

- `KR-GG-CHEM-001` remains useful as a Korea Wave-1 source candidate, but exact accident-to-facility identity is not yet established and prior Korean research already links facility risk factors to accident history.
- `US-PIPE-001` remains unexecuted, but the national line-geometry restriction and direct overlap continue to reduce marginal information value.
- `US-FDA-MD-001` remains parked as an access-blocked asset and is not discarded; it may be reconsidered only after new official inspection-byte access evidence.

## Authorization boundary / 승인 경계

R31 authorizes only a separate `US-NHTSA-MC-F01` outcome-blind source/schema/product-identity/time feasibility gate. F01 may verify source bytes, dictionaries, deterministic product identity, multiplicity, date support and aggregate identity overlap only. It must not compute recall incidence by communication profile, bulletin type, component, manufacturer, model, or any proposed exposure group.

Incremental monetary cost remains **0 USD**.
'''
    (OUT / "RESULT.md").write_text(result, encoding="utf-8")

    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nIssue #142 ratifies the immutable scorecard without rescoring. **`{SELECTION}`** is selected at **39/45**, ahead of KR-GG-CHEM-001 and US-PIPE-001 at **36/45** each. No candidate outcome was opened.\n'''
        (OUT / "README.md").write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R31 selects US-NHTSA-MC-001

PORTFOLIO-R31 compares exactly three prospectively frozen candidates without opening candidate outcomes. The immutable scores are **US-NHTSA-MC-001 39/45**, **KR-GG-CHEM-001 36/45**, and **US-PIPE-001 36/45**. Therefore `US-NHTSA-MC-001` is selected for one separate outcome-blind F01.

This is a portfolio-control claim only. It does not establish that manufacturer communications predict recalls, any direction of association, novelty, or causality.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R31
status: active
---

# {DECISION} — Select US-NHTSA-MC-001 for one outcome-blind F01

## Decision / 결정

Select **`US-NHTSA-MC-001`** for exactly one separate `US-NHTSA-MC-F01` source/schema/product-identity/time feasibility gate.

## Rationale / 근거

The prospectively frozen scorecard gives NHTSA **39/45**, ahead of both alternatives at **36/45**. Public NHTSA manufacturer-communication and recall flat files provide a strong zero-cost source path and a high-information next gate, while the overlap penalty remains explicit because NHTSA already uses manufacturer communications in defect analysis.

## Boundary / 경계

- No recall incidence, future-recall membership, coefficient or relationship may be opened in R31.
- F01 must resolve exact product normalization, repeated-row structure and temporal support without outcome-driven filtering.
- No novelty or causal claim.
- Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "DECISION_LOG.md", f"`{AUTH_DECISION}`", f"| `{AUTH_DECISION}` | 2026-09-16 | Authorize PORTFOLIO-R31 frozen three-candidate reselection. / R31 고정 후보 3개 재선정 승인. | Candidate/rubric contract and Issue #142 precede score persistence; outcomes closed. | Issue #142; `research/PORTFOLIO-R31/README.md` | completed |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Select US-NHTSA-MC-001 for one separate outcome-blind F01. / NHTSA manufacturer communications→recall 후보를 별도 F01에 한해 선택. | Frozen R31 scorecard: NHTSA 39 > KR-GG-CHEM 36 = US-PIPE 36; no candidate outcomes opened. | Issue #142; `{CLAIM}`; `research/PORTFOLIO-R31/RESULT.md` | active |\n")
    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | PORTFOLIO-R31 selects US-NHTSA-MC-001 at 39/45 over KR-GG-CHEM and US-PIPE at 36/45 without opening candidate outcomes. / R31은 outcome 비개봉 상태에서 NHTSA 후보를 선택. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #142; `research/PORTFOLIO-R31/RESULT.md` | 2026-09-16 | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R31-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 142
last_completed_research: PORTFOLIO-R31
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R31 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. Frozen scores: NHTSA **39/45**, KR-GG-CHEM **36/45**, US-PIPE **36/45**. No candidate outcome magnitude was opened.

## Exact next action / 정확한 다음 행동

Open exactly one separate `US-NHTSA-MC-F01` outcome-blind source/schema/product-identity/time feasibility Issue. Verify current NHTSA communication and recall flat-file routes, exact field schemas, deterministic Model Year × Make × Model normalization, repeated communication/component structure, temporal support and aggregate identity overlap. Do not count or compare recall incidence by any communication-derived exposure.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R31-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 142,
        "last_completed_research": "PORTFOLIO-R31",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    handoff = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R31-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 142
last_completed_research: PORTFOLIO-R31
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- selected candidate: `US-NHTSA-MC-001`
- selected gate: `US-NHTSA-MC-F01`
- frozen score: `39/45`
- alternatives: `KR-GG-CHEM-001 = 36/45`; `US-PIPE-001 = 36/45`
- candidate outcomes opened: `false`

## Exact restart point / 정확한 재개점

Open exactly one `US-NHTSA-MC-F01` outcome-blind source/schema/product-identity/time gate. Verify current official communication and recall files, dictionaries, exact product normalization, repeated row structure and temporal/aggregate overlap support. Do not open recall incidence or any relationship by communication profile.

Incremental monetary cost remains **0 USD**.
'''
    (CTX / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

    print(json.dumps({"selection": SELECTION, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
