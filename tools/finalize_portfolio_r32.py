#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "PORTFOLIO-R32"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 144
DECISION = "DEC-201"
CLAIM = "CLM-182"
SELECTION = "SELECT_US_FMCSA_HAZ_001_INSPECTION_TO_PHMSA_HAZMAT_F01"
STATE = "PORTFOLIO_R32_SELECTED_US_FMCSA_HAZ_001__F01_AUTHORIZATION_REQUIRED"


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
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R32-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "PORTFOLIO-R32",
        "last_completed_issue": 143,
        "last_completed_research": "US-NHTSA-MC-F01",
        "last_decision": "DEC-200",
        "updated": "2026-09-16",
    }

    contract = (OUT / "README.md").read_text(encoding="utf-8")
    source = (OUT / "SOURCE_REVALIDATION.md").read_text(encoding="utf-8")
    score = (OUT / "SCORECARD.md").read_text(encoding="utf-8")

    assert "candidate_count: 4" in contract
    assert "issue: 144" in source
    assert "source_revalidation_commit: 0523fa3cb3c00564a034df6879c3b765b9c4f1da" in score
    assert "**US-FMCSA-HAZ-001** | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | **42/45**" in score
    assert "US-FTA-TRANSIT-001 | 4 | 3 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | **37/45**" in score
    assert "KR-GG-CHEM-001 | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 5 | 1 | **36/45**" in score
    assert "US-PIPE-001 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 3 | 0 | **36/45**" in score
    assert SELECTION in score
    assert "candidate_outcomes_opened: false" in score

    (OUT / "RESULT.md").write_text(f'''---
id: PORTFOLIO-R32-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: US-FMCSA-HAZ-001
selected_gate: US-FMCSA-HAZ-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R32 Result — Select US-FMCSA-HAZ-001 F01

**`{SELECTION}`**

R32 was executed under the corrected prospective order:

`candidate/rule contract → Issue #144 → source revalidation → immutable scorecard`.

No candidate-specific outcome magnitude, exposure-stratified outcome count, coefficient, predictive score or relationship direction was opened.

## Frozen final scores / 최종 고정점수

| Candidate | Total | Disposition |
|---|---:|---|
| **US-FMCSA-HAZ-001** | **42/45** | **SELECT_F01_ONLY** |
| US-FTA-TRANSIT-001 | **37/45** | HOLD_RUNNER_UP |
| KR-GG-CHEM-001 | **36/45** | HOLD_IDENTITY_AND_OVERLAP |
| US-PIPE-001 | **36/45** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |

No tie-break is required.

## Why FMCSA × PHMSA leads / 선정 근거

The branch combines two separate federal safety systems with a prospectively exact identity path:

`FMCSA roadside inspection / violation / OOS → native USDOT Number → PHMSA Form 5800.1 Highway Carrier/Reporter FED DOT ID → later hazmat incident`.

Current official documentation supports public zero-cost inspection/violation files with USDOT Number and inspection date, while PHMSA documents carrier/reporter FED DOT ID and incident date. One F01 can remove the remaining high-value uncertainty: whether the Highway-mode PHMSA identifier behaves as an exact USDOT carrier key in current downloadable bytes, whether the represented cohorts overlap at useful scale, and whether the frozen time window is sufficient.

The branch is bounded to the publicly represented source cohorts. FMCSA's general public Inspection Files have explicit exclusions, including inactive USDOT numbers and active-HMSP entities, so R32 does not authorize a population-wide hazmat-carrier claim.

## F01 authorization boundary / 승인 경계

A separate `US-FMCSA-HAZ-F01` may verify only:

- current official zero-cost FMCSA inspection/violation source access;
- current official zero-cost PHMSA 5800.1 incident source access;
- native USDOT / FED DOT ID field semantics and parseability;
- exact Highway-mode carrier-ID overlap, without name/address/fuzzy repair;
- inspection-date and incident-date support;
- public-cohort scope/exclusions;
- repeated carrier/inspection structure;
- aggregate exact-ID overlap and deterministic identity fingerprints.

F01 may **not** open or compare hazmat incident occurrence/rates/counts by inspection, violation, OOS, BASIC or any derived carrier-risk profile. No causal or federal-safety-rating claim is authorized.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nIssue #144 ratifies the immutable scorecard without rescoring. **`{SELECTION}`** is selected at **42/45**, ahead of FTA 37/45 and the two preserved 36/45 candidates. No candidate outcome was opened.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R32 selects US-FMCSA-HAZ-001

PORTFOLIO-R32 prospectively compares four frozen candidates after current official-source revalidation. The immutable scorecard is **US-FMCSA-HAZ-001 42/45**, **US-FTA-TRANSIT-001 37/45**, **KR-GG-CHEM-001 36/45**, and **US-PIPE-001 36/45**. Therefore `US-FMCSA-HAZ-001` is selected for one separate outcome-blind F01.

This is a portfolio-control claim only. It does not establish that FMCSA inspection/violation/OOS history predicts PHMSA hazmat incidents, any direction of association, carrier risk ranking, novelty, or causality.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R32
status: active
---

# {DECISION} — Select US-FMCSA-HAZ-001 for one outcome-blind F01

## Decision / 결정

Ratify the immutable R32 scorecard and select **`US-FMCSA-HAZ-001`** for exactly one separate `US-FMCSA-HAZ-F01` source/schema/carrier-identity/time feasibility gate.

## Rationale / 근거

US-FMCSA-HAZ-001 leads at **42/45**. Official public documentation prospectively supports USDOT-numbered FMCSA inspection records and PHMSA Form 5800.1 carrier/reporter FED DOT ID plus incident dates. The remaining uncertainty can be tested outcome-blind in one bounded F01.

## Boundary / 경계

- no inspection-profile-conditioned hazmat incident occurrence/rate/count;
- no fuzzy carrier-name/address matching;
- no population-wide inference beyond represented public-source cohorts;
- no causal or federal safety-rating interpretation;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | PORTFOLIO-R32 selects US-FMCSA-HAZ-001 at 42/45 over FTA 37, KR-GG-CHEM 36 and US-PIPE 36 after prospective official-source revalidation; no candidate outcomes opened. / R32에서 FMCSA×PHMSA hazmat 후보 선정. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #144; `research/PORTFOLIO-R32/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Select US-FMCSA-HAZ-001 for one separate outcome-blind F01. / FMCSA inspection→PHMSA hazmat incident 후보를 별도 F01에 한해 선택. | Frozen R32 scorecard: FMCSA-HAZ 42 > FTA 37 > KR-GG-CHEM 36 = US-PIPE 36; outcomes unopened. | Issue #144; `{CLAIM}`; `research/PORTFOLIO-R32/RESULT.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R32-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 144
last_completed_research: PORTFOLIO-R32
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R32 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. Frozen scores: FMCSA-HAZ **42/45**, FTA-TRANSIT **37/45**, KR-GG-CHEM **36/45**, US-PIPE **36/45**. No candidate outcome magnitude or relationship was opened.

## Exact next action / 정확한 다음 행동

Open exactly one separate `US-FMCSA-HAZ-F01` outcome-blind source/schema/carrier-identity/time feasibility Issue. Verify official FMCSA public inspection/violation bytes, official PHMSA Form 5800.1 incident bytes, exact Highway-mode USDOT↔FED-DOT-ID semantics, time support, public-cohort exclusions, aggregate exact carrier overlap and fingerprints. Do not open incident occurrence/rates/counts by any inspection-derived profile.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-PORTFOLIO-R32-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 144,
        "last_completed_research": "PORTFOLIO-R32",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R32-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 144
last_completed_research: PORTFOLIO-R32
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- selected candidate: `US-FMCSA-HAZ-001`
- selected gate: `US-FMCSA-HAZ-F01`
- frozen score: `42/45`
- candidate outcomes opened: `false`
- monetary cost: `0 USD`

## Exact restart point / 정확한 재개점

Open exactly one `US-FMCSA-HAZ-F01` outcome-blind source/schema/carrier-identity/time gate. Verify current official FMCSA inspection/violation and PHMSA incident source bytes, exact Highway-mode USDOT↔FED-DOT-ID semantics, temporal support, public-cohort scope, aggregate overlap and fingerprints. Do not open hazmat incident occurrence/rates/counts conditioned on inspection history.
''', encoding="utf-8")

    print(json.dumps({"selection": SELECTION, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
