#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "PORTFOLIO-R30"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 140
DECISION = "DEC-193"
CLAIM = "CLM-178"
SELECTION = "SELECT_US_FDA_MD_001_INSPECTION_TO_RECALL_F01"
STATE = "PORTFOLIO_R30_SELECTED_US_FDA_MD_001__F01_AUTHORIZATION_REQUIRED"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R30-ACTIVE",
        "active_issue": 140,
        "active_research": "PORTFOLIO-R30",
        "last_completed_issue": 139,
        "last_completed_research": "C-EU-F01",
        "last_decision": "DEC-192",
        "updated": "2026-09-16",
    }

    readme = (OUT / "README.md").read_text(encoding="utf-8")
    score = (OUT / "SCORECARD.md").read_text(encoding="utf-8")
    nc = (OUT / "PROCESS_NONCONFORMITY.md").read_text(encoding="utf-8")
    bind = (OUT / "ISSUE_BINDING.md").read_text(encoding="utf-8")

    # Ratify; do not recompute or modify the frozen scorecard.
    assert "issue: 140" in readme
    assert "US-FDA-MD-001: 41/45" in bind
    assert "US-CMS-NH-001: 37/45" in bind
    assert "US-PIPE-001: 36/45" in bind
    assert SELECTION in bind
    assert "e848a6c77920aa7e31eb1e1038e4f9914cbc6b7e" in nc
    assert "no candidate outcome" in nc.lower()
    assert "**41**" in score and "**37**" in score and "**36**" in score

    result = f'''---
id: PORTFOLIO-R30-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: US-FDA-MD-001
selected_gate: US-FDA-MD-F01
candidate_outcomes_opened: false
process_nonconformity_recorded: true
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R30 Result — Select US-FDA-MD-001 F01

**`{SELECTION}`**

R30 returns to Stage 0 after terminal C-EU-F01 and deliberately avoids automatic promotion of US-PIPE. It compares one preserved unexecuted candidate with two fresh-domain candidates. No candidate outcome magnitude or candidate-specific relationship was opened.

## Frozen final scorecard / 최종 고정 점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-FDA-MD-001 inspection classification → later device recall** | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | **41** | **SELECT_STAGE0_F01_ONLY** |
| US-CMS-NH-001 staffing instability → later health deficiencies | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_HIGH_DIRECT_OVERLAP |
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

US-FDA-MD-001 leads outright at **41/45**; no tie-break is required.

## Why FDA leads / FDA 선정 근거

FDA's current public architecture supports a potentially exact establishment-level path that remains outcome-blind at the next gate:

`publicly disclosed CDRH/device inspection → exact FEI → later device-recall FEI identity`.

The value is not a claim that OAI/VAI causes recalls. The next information question is whether the public inspection download actually exposes a stable FEI/project-area/date/classification schema and whether that exact FEI has sufficient structural overlap with Device Recall `firm_fei_number` before any recall incidence by inspection class is opened.

The public Inspection Classification Database is explicitly non-comprehensive, so a descendant is bounded to the publicly disclosed inspected-facility cohort only. It may not estimate population-wide manufacturer recall risk or interpret inspection selection causally.

## Preserved alternatives / 보존 후보

- `US-CMS-NH-001` remains technically executable, but current peer-reviewed work already directly analyzes PBJ staffing instability against deficiency citations, so marginal information/novelty value is low.
- `US-PIPE-001` remains unexecuted, but unrestricted national line geometry still cannot be assumed and direct domain overlap remains high.

## Process nonconformity / 절차 비적합

The candidate pool, rubric, tie-break and source revalidation were durably frozen before scoring, but the scorecard commit `e848a6c77920aa7e31eb1e1038e4f9914cbc6b7e` preceded Issue #140 binding. This is recorded in `PROCESS_NONCONFORMITY.md` and Issue #140.

No candidate outcome magnitude was opened, no score was outcome-driven, and R30 does **not** rescore after Issue binding. Future portfolio rounds must bind the Issue after the candidate/rule contract and before scorecard persistence.

## Authorization boundary / 승인 경계

R30 authorizes only a separate `US-FDA-MD-F01` outcome-blind source/schema/identity feasibility gate. F01 must prospectively verify, before recall incidence by inspection class is opened:

- actual current zero-cost FDA entire-inspections dataset download route;
- FEI field presence/type and exact identity cardinality;
- inspection end date and final NAI/VAI/OAI classification route;
- a defensible CDRH/device manufacturing/project-area filter using source semantics only;
- duplicate project-area / repeated-inspection structure;
- openFDA Device Recall `firm_fei_number` and event-date identity support;
- exact FEI overlap and temporal support only, without counting or comparing recall incidence by classification;
- explicit bounded-cohort and non-causal claim boundary.

No effect test is authorized.

Incremental monetary cost remains **0 USD**.
'''
    (OUT / "RESULT.md").write_text(result, encoding="utf-8")

    # Append ratification to README without changing scorecard.
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nIssue #140 ratifies the immutable scorecard without rescoring. **`{SELECTION}`** is selected at **41/45**, ahead of US-CMS-NH-001 at 37/45 and US-PIPE-001 at 36/45. The pre-Issue scorecard ordering nonconformity remains durably recorded; no candidate outcome was opened.\n'''
        (OUT / "README.md").write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R30 selects US-FDA-MD-001

PORTFOLIO-R30 compares exactly three frozen candidates without opening candidate outcomes. The immutable scorecard is **US-FDA-MD-001 41/45**, **US-CMS-NH-001 37/45**, and **US-PIPE-001 36/45**. Therefore `US-FDA-MD-001` is selected for one separate outcome-blind F01.

The candidate/rule/source contract preceded scoring, but scorecard persistence preceded Issue #140 binding. This ordering nonconformity is explicitly recorded and did not expose outcomes or trigger rescoring.

This is a portfolio-control claim only. It does not establish that inspection classification predicts recalls, any direction of association, population-wide manufacturer risk, novelty, or causality.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R30
status: active
---

# {DECISION} — Select US-FDA-MD-001 for one outcome-blind F01

## Decision / 결정

Ratify the immutable R30 scorecard and select **`US-FDA-MD-001`** for exactly one separate `US-FDA-MD-F01` source/schema/identity feasibility gate.

## Rationale / 근거

US-FDA-MD-001 leads the frozen scorecard at **41/45**, versus CMS 37 and US-PIPE 36. Exact FEI identity is prospectively available across the FDA inspection/reliance architecture and Device Recall `firm_fei_number`, while one F01 can remove substantial uncertainty about the current downloadable inspection schema and exact structural overlap. The inspection database's explicit non-comprehensiveness requires a bounded inspected-cohort interpretation.

## Governance / 거버넌스

The scorecard-before-Issue ordering defect is preserved, not erased. Because candidate pool/rules/source facts were frozen first and no outcomes opened, the scorecard is ratified without rescoring. Future rounds must bind the Issue before scorecard persistence.

## Boundary / 경계

- No recall incidence by inspection classification may be opened in R30.
- No population-wide manufacturer denominator claim.
- No causal interpretation of inspection selection/classification.
- F01 must fail closed if FEI/schema/source access does not support the bounded design.
- Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | PORTFOLIO-R30 selects US-FDA-MD-001 at 41/45 over CMS 37 and US-PIPE 36 without opening candidate outcomes; scorecard-before-Issue ordering nonconformity recorded. / R30은 outcome 비개봉 상태에서 FDA 의료기기 후보를 선택. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #140; `research/PORTFOLIO-R30/RESULT.md`; `PROCESS_NONCONFORMITY.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Select US-FDA-MD-001 for one separate outcome-blind F01; preserve process nonconformity and bounded inspected-cohort interpretation. / FDA 의료기기 inspection→recall 후보를 별도 F01에 한해 선택. | Frozen R30 scorecard: FDA 41 > CMS 37 > US-PIPE 36; no candidate outcomes opened. | Issue #140; `{CLAIM}`; `research/PORTFOLIO-R30/RESULT.md` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R30-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 140
last_completed_research: PORTFOLIO-R30
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R30 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. Frozen scores: FDA **41/45**, CMS **37/45**, US-PIPE **36/45**. No candidate outcome magnitude was opened. The scorecard-before-Issue binding nonconformity remains durably recorded.

## Exact next action / 정확한 다음 행동

Open exactly one separate `US-FDA-MD-F01` outcome-blind source/schema/identity feasibility Issue. Verify current zero-cost inspection dataset access, exact FEI/date/classification/project-area schema, CDRH/device manufacturing filter, repeated-inspection structure and exact Device Recall FEI/date support. Do not count or compare recall incidence by inspection class.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R30-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 140,
        "last_completed_research": "PORTFOLIO-R30",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    handoff = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R30-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 140
last_completed_research: PORTFOLIO-R30
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- selected candidate: `US-FDA-MD-001`
- selected gate: `US-FDA-MD-F01`
- frozen score: `41/45`
- candidate outcomes opened: `false`
- process nonconformity: candidate/rules/source facts frozen before score; scorecard persisted before Issue #140 binding; no outcome leakage; no rescoring.

## Exact restart point / 정확한 재개점

Open exactly one `US-FDA-MD-F01` outcome-blind source/schema/identity gate. Verify the current public FDA inspection dataset route, FEI and inspection classification/date/project-area schema, source-semantic CDRH/device-manufacturing filter, repeated inspection/project-area identity, and Device Recall exact `firm_fei_number`/event-date support. Do not open recall incidence by inspection class or compute a relationship.

Incremental monetary cost remains **0 USD**.
'''
    (CTX / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

    print(json.dumps({"selection": SELECTION, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
