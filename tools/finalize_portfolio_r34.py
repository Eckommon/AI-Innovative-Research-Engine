#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "PORTFOLIO-R34"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 149
DECISION = "DEC-211"
CLAIM = "CLM-187"
SELECTION = "SELECT_US_EPA_XMEDIA_001_RCRA_TO_NPDES_F01"
STATE = "PORTFOLIO_R34_SELECTED_US_EPA_XMEDIA_001__F01_AUTHORIZATION_REQUIRED"
TODAY = "2026-09-17"
CONTRACT_COMMIT = "db56429107fc1a7054b9be0b5a78d91424f72971"
SOURCE_COMMIT = "70884f50133fdd3f786d3b3f515e303584fd77bf"
SCORE_COMMIT = "a23c00f321e565e647d53eada24e2ce17dc956fd"


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
        "checkpoint_id": "CHK-20260917-PORTFOLIO-R34-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "PORTFOLIO-R34",
        "last_completed_issue": 148,
        "last_completed_research": "US-FTA-TRANSIT-N01",
        "last_decision": "DEC-210",
        "updated": TODAY,
    }

    contract = (OUT / "README.md").read_text(encoding="utf-8")
    source = (OUT / "SOURCE_REVALIDATION.md").read_text(encoding="utf-8")
    score = (OUT / "SCORECARD.md").read_text(encoding="utf-8")

    assert "Exactly four candidates are authorized" in contract
    assert f"contract_commit: {CONTRACT_COMMIT}" in source
    assert f"source_revalidation_commit: {SOURCE_COMMIT}" in score
    for candidate in ("US-EPA-XMEDIA-001", "US-BTS-PORT-001", "US-USCG-VESSEL-001", "US-MSHA-001"):
        assert candidate in score
    assert "**US-EPA-XMEDIA-001**" in score and "**41**" in score
    assert "US-USCG-VESSEL-001" in score and "**38**" in score
    assert "US-MSHA-001" in score and "**36**" in score
    assert "US-BTS-PORT-001" in score and "**30**" in score
    assert SELECTION in score
    assert "No tie-break is required" in score
    assert "candidate_outcomes_opened: false" in score
    assert "relationship_computed: false" in score

    (OUT / "RESULT.md").write_text(f'''---
id: PORTFOLIO-R34-RESULT
type: mission-roi-portfolio-selection
created: {TODAY}
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: US-EPA-XMEDIA-001
selected_gate: US-EPA-XMEDIA-F01
candidate_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R34 Result — Select US-EPA-XMEDIA-001 F01

**`{SELECTION}`**

R34 followed the prospective order:

`candidate/rule contract → Issue #149 → canonical activation → current source/internal-history/literature revalidation → immutable scorecard → one selection`.

The candidate pool was **not rewritten** after post-contract discovery of prior RCRA, port and mine branches. Those internal overlaps were instead persisted as evidence and reflected in the one-time scorecard.

No candidate-specific outcome magnitude, exposure-stratified outcome count, coefficient, predictive score, relationship direction or downstream event membership was opened.

## Frozen final scores / 최종 고정점수

| Candidate | Total | Disposition |
|---|---:|---|
| **US-EPA-XMEDIA-001** | **41/45** | **SELECT_F01** |
| US-USCG-VESSEL-001 | **38/45** | HOLD_DIRECT_OVERLAP |
| US-MSHA-001 | **36/45** | HOLD_INTERNAL_AND_DIRECT_OVERLAP |
| US-BTS-PORT-001 | **30/45** | HOLD_IDENTITY_SUPPORT_AND_OVERLAP |

No tie-break is used.

## Why EPA cross-media leads / EPA cross-media 선정 이유

The candidate combines:

- official exact cross-program facility identity through EPA FRS / Registry ID;
- genuinely distinct RCRA and ICIS-NPDES program data;
- a direct future regulatory endpoint family (effluent-limit exceedance);
- a large national facility universe whose **exact cross-program support remains unknown and therefore informative**;
- a cheap outcome-blind next gate that can falsify source/join/time/cardinality feasibility before any relationship is opened.

Novelty is **not** established. EPA already has multi-media compliance-screening practice, and the repository has a prior RCRA disaster-compliance branch. Those adjacency risks are why low-overlap / novelty receives only 3/5 rather than full credit.

## Selection boundary / 선정 경계

The selection authorizes exactly one separate `US-EPA-XMEDIA-F01` source/schema/FRS-identity/time/cardinality feasibility gate.

F01 may verify only:

- current official zero-cost EPA RCRAInfo / RCRA Pipeline, FRS program-linkage and ICIS-NPDES source routes;
- exact official `REGISTRY_ID` / FRS cross-program identity semantics;
- RCRA `SOURCE_ID` and NPDES `NPDES_ID` structural mappings;
- longitudinal date/schema support;
- exact aggregate cross-program facility / permit cardinality and deterministic fingerprints;
- whether a future preregistered facility-time design is feasible without fuzzy identity or full-national expensive ingestion.

F01 may **not** open or report RCRA-conditioned NPDES effluent-violation occurrence, pollutant exceedance magnitude, rate, coefficient, risk ranking, predictive score or relationship direction.

No causal, facility-risk-ranking, enforcement-targeting or novelty claim is authorized.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nIssue #149 ratifies the one-time immutable scorecard without rescoring. **`{SELECTION}`** is selected uniquely at **41/45** over USCG 38, MSHA 36 and BTS-Port 30. No candidate outcome was opened.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: {TODAY}
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R34 selects EPA cross-media F01 under frozen Mission-ROI scoring

PORTFOLIO-R34 prospectively compares four frozen candidates after current official-source, internal-history and direct-overlap revalidation. The immutable scorecard is **US-EPA-XMEDIA-001 41/45**, **US-USCG-VESSEL-001 38/45**, **US-MSHA-001 36/45**, and **US-BTS-PORT-001 30/45**. EPA cross-media is therefore selected for exactly one separate outcome-blind F01 without a tie-break.

This is a portfolio-control claim only. It does not establish a RCRA→NPDES relationship, effect direction, facility risk ranking, enforcement recommendation, causal mechanism or novelty.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: {TODAY}
issue: {ISSUE}
research: PORTFOLIO-R34
status: active
---

# {DECISION} — Select US-EPA-XMEDIA-001 for one outcome-blind F01

## Decision / 결정

Ratify the immutable R34 scorecard and select **`US-EPA-XMEDIA-001`** for exactly one separate `US-EPA-XMEDIA-F01` source/schema/FRS-identity/time/cardinality feasibility gate.

## Rationale / 근거

EPA cross-media leads uniquely at **41/45**. It combines an official exact FRS cross-program identity, direct regulatory outcome family and high next-gate information gain while retaining only conservative novelty credit because multi-media compliance screening and prior internal RCRA work are adjacent precedents.

USCG and MSHA remain technically stronger in some dimensions but are materially near-identical to existing published predictive relationships. BTS-Port remains constrained by unresolved exact port identity, small independent-unit support and a prior internal identity blocker.

## Boundary / 경계

- no RCRA-conditioned NPDES effluent-violation occurrence/rate/magnitude;
- no fuzzy name/address/geospatial/manual facility repair;
- exact FRS / Registry ID linkage only;
- no causal, enforcement-targeting, facility-risk-ranking or novelty claim;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(
        REG / "CLAIM_LEDGER.md",
        f"`{CLAIM}`",
        f"| `{CLAIM}` | PORTFOLIO-R34 selects US-EPA-XMEDIA-001 at 41/45 over USCG 38, MSHA 36 and BTS-Port 30 after frozen source/internal-history/literature revalidation; no candidate outcomes opened. / R34에서 EPA RCRA→NPDES cross-media 후보를 선정. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #149; `research/PORTFOLIO-R34/RESULT.md` | {TODAY} | active |\n",
    )
    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | {TODAY} | Select US-EPA-XMEDIA-001 for one separate outcome-blind F01. / EPA RCRA compliance→NPDES effluent 후보를 별도 F01에 한해 선택. | Frozen R34 scorecard: EPA 41 > USCG 38 > MSHA 36 > BTS-Port 30; official FRS identity and high next-gate information gain; outcomes unopened. | Issue #149; `{CLAIM}`; `research/PORTFOLIO-R34/RESULT.md` | active |\n",
    )

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R34-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 149
last_completed_research: PORTFOLIO-R34
last_decision: {DECISION}
updated: {TODAY}
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R34 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. Frozen scores: EPA cross-media **41/45**, USCG vessel **38/45**, MSHA **36/45**, BTS-Port **30/45**. No tie-break was required and no candidate outcome magnitude or relationship was opened.

## Exact next action / 정확한 다음 행동

Freeze a separate `US-EPA-XMEDIA-F01` contract **before opening its Issue**. F01 must verify current official RCRAInfo / RCRA Pipeline, FRS Program Linkages and ICIS-NPDES source/schema access, exact official Registry-ID cross-program identity, structural date support, aggregate exact facility / permit overlap and deterministic fingerprints. It must not open RCRA-conditioned NPDES effluent-violation occurrence or magnitude.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-PORTFOLIO-R34-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": ISSUE,
        "last_completed_research": "PORTFOLIO-R34",
        "last_decision": DECISION,
        "updated": TODAY,
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R34-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 149
last_completed_research: PORTFOLIO-R34
last_decision: {DECISION}
updated: {TODAY}
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- selected candidate: `US-EPA-XMEDIA-001`
- selected gate: `US-EPA-XMEDIA-F01`
- frozen score: `41/45`
- other scores: `USCG 38`, `MSHA 36`, `BTS-Port 30`
- tie-break used: `false`
- candidate outcomes opened: `false`
- relationship computed: `false`
- monetary cost: `0 USD`

## Exact restart point / 정확한 재개점

Freeze the separate US-EPA-XMEDIA-F01 source/schema/identity/time/cardinality contract before Issue creation. Use exact official FRS / Registry ID linkage only. Do not open RCRA-conditioned NPDES effluent outcomes.
''', encoding="utf-8")

    print(json.dumps({"selection": SELECTION, "decision": DECISION, "claim": CLAIM, "state": STATE, "score_commit": SCORE_COMMIT}, sort_keys=True))


if __name__ == "__main__":
    main()
