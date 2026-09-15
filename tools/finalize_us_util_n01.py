#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-UTIL-N01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 137
GATE = "HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT"
DECISION = "DEC-189"
CLAIM = "CLM-175"
STATE = "US_UTIL_N01_HOLD__PORTFOLIO_RETURN"
RUN_ID = os.environ.get("GITHUB_RUN_ID", "unknown")


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker not in current:
        if not current.endswith("\n"):
            current += "\n"
        current += text
        path.write_text(current, encoding="utf-8")


def main() -> None:
    checkpoint = json.loads((CTX / "checkpoint.json").read_text(encoding="utf-8"))
    assert checkpoint["active_issue"] == ISSUE
    assert checkpoint["active_research"] == "US-UTIL-N01"
    assert checkpoint["last_decision"] == "DEC-188"

    staging = json.loads((OUT / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    assert staging["gate"] == GATE
    assert staging["source_hash_match_f02"] is True
    assert staging["execution_correction"]["scientific_contract_changed"] is False
    assert staging["reliability_magnitudes_opened"] is False
    assert staging["relationship_computed"] is False
    assert staging["noaa_storm_magnitudes_used"] is False
    assert staging["invented_county_weights"] is False
    assert staging["post_execution_rescue_used"] is False
    assert staging["incremental_monetary_cost_usd"] == 0

    frozen = staging["frozen_issue_137_requirements"]
    assert frozen["eligible_utilities_ge_500"] is False
    assert frozen["exposed_candidates_ge_300"] is False
    assert frozen["matched_pairs_ge_150"] is False
    assert frozen["matched_states_ge_25"] is False
    assert frozen["no_conflicting_ami_duplicates"] is False

    diagnostics = staging["diagnostics"]
    candidates = staging["candidate_support"]
    matching = staging["matching"]

    terminal = dict(staging)
    terminal["terminal"] = {
        "finalized": True,
        "finalizer_run": RUN_ID,
        "decision": DECISION,
        "claim": CLAIM,
        "state": STATE,
        "issue": ISSUE,
    }
    (OUT / "RESULT.json").write_text(json.dumps(terminal, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    result_md = f"""---
id: US-UTIL-N01-RESULT
type: outcome-blind-design-identifiability-result
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_HOLD
final_gate: {GATE}
decision: {DECISION}
claim: {CLAIM}
corrected_run: 35008869612
superseded_runs: [35007853296, 35007936755]
reliability_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-N01 Result / 결과

## Final gate / 최종 판정

**`{GATE}`**

US-UTIL-N01 does not reach a separately authorized Reliability-outcome experiment. The prospectively frozen AMI-ramp matched design fails multiple support requirements before any SAIDI magnitude is opened. / US-UTIL-N01은 별도 Reliability outcome 실험 단계로 승격되지 않는다. SAIDI 값을 열기 전에 사전 고정된 AMI-ramp matched design의 여러 support 요건이 충족되지 않았다.

## Corrected outcome-blind support / 교정된 outcome-blind support

Corrected execution Run `35008869612` reused the already prospectively adjudicated F02 largest-identity worksheet rule and the primary IEEE-with-MED rule excluding LOS variants. No scientific threshold, denominator, year, state rule or caliper changed. / 교정 실행은 F02에서 이미 사전 판정된 parser 규칙만 재사용했으며 과학적 기준은 변경하지 않았다.

- eligible utility-state transitions: **{diagnostics['eligible_transitions']:,}**
- distinct eligible Utility Numbers: **{diagnostics['eligible_utilities']:,}** vs frozen minimum **500**
- exposed candidates: **{candidates['exposed']:,}** vs frozen minimum **300**
- control candidates: **{candidates['control']:,}** vs frozen minimum **300**
- conflicting exact utility-state-year AMI records: **{diagnostics['ami_duplicate_conflicts']:,}** vs frozen requirement **0**
- deterministic matched pairs: **{matching['pairs']:,}** vs frozen minimum **150**
- matched states: **{matching['states']:,}** vs frozen minimum **25**
- pairs by exposure year: **{matching['pairs_by_exposure_year']}**; represented-year minimum was **30 pairs each**
- frozen pair fingerprint: `{matching['pair_identity_sha256']}`

The control-candidate minimum and all-year exposed/control existence tests pass, but the design still terminates because multiple mandatory frozen requirements fail. / control 후보 수와 모든 exposure year의 양 역할 존재는 통과하지만, 여러 필수 고정요건이 실패하므로 design은 종료된다.

## Execution lineage / 실행 계보

- Run `35007853296`: environment dependency failure (`openpyxl` absent), before support calculation.
- Run `35007936755`: `EXECUTION_PARSER_INVALID_FOR_GATE`; wrong base F02 worksheet/header resolver and an unregistered hard condition were detected before terminalization.
- Run `35008869612`: corrected execution under unchanged Issue #137 contract; this is the terminal evidence-bearing N01 run.

## Evidence boundary / 증거 경계

This HOLD means **design/support identifiability failed**. It is not evidence that AMI does or does not improve reliability. Specifically:
- SAIDI/SAIFI/CAIDI magnitudes remain unopened;
- no AMI→Reliability relationship was computed;
- no NOAA storm magnitude was used;
- no customer-weighted county exposure was invented;
- no post-execution threshold/caliper/aggregation rescue is permitted;
- no causal or resilience claim is supported.

A future US-UTIL descendant requires a new Stage-0/portfolio authorization rather than modifying N01 after seeing support. / 후속 US-UTIL 연구는 N01 기준을 사후 변경하지 않고 Stage 0/portfolio에서 새로 승인되어야 한다.

Incremental monetary cost remained **0 USD**.
"""
    (OUT / "RESULT.md").write_text(result_md, encoding="utf-8")

    readme = (OUT / "README.md").read_text(encoding="utf-8")
    marker = "## Terminal disposition / 최종 처분"
    if marker not in readme:
        readme += f"""\n\n{marker}\n\nCorrected Run `35008869612` terminates US-UTIL-N01 at **`{GATE}`** under {DECISION} / {CLAIM}. Eligible Utility Numbers = **{diagnostics['eligible_utilities']:,}**, exposed candidates = **{candidates['exposed']:,}**, control candidates = **{candidates['control']:,}**, exact-key AMI conflicts = **{diagnostics['ami_duplicate_conflicts']:,}**, deterministic pairs = **{matching['pairs']:,}** across **{matching['states']:,} states**. Reliability magnitudes remained closed and no relationship was computed. / Reliability 값은 개봉되지 않았고 관계계산도 수행하지 않았다.\n"""
        (OUT / "README.md").write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f"""---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_DESIGN_GATE
status: active
---

# {CLAIM} — US-UTIL-N01 AMI-ramp matched design HOLD

Corrected Run `35008869612` applies the frozen Issue #137 contract without opening Reliability magnitudes. It finds **{diagnostics['eligible_utilities']:,}** eligible Utility Numbers (<500), **{candidates['exposed']:,}** exposed candidates (<300), **{matching['pairs']:,}** deterministic pairs (<150) across **{matching['states']:,} states** (<25), and **{diagnostics['ami_duplicate_conflicts']:,}** conflicting exact utility-state-year AMI records where the frozen requirement is zero. Therefore US-UTIL-N01 terminates at **`{GATE}`**.

This claim is a design-support HOLD only. It does not establish an AMI reliability effect, resilience benefit, direction of association, novelty or causality.
""", encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f"""---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-UTIL-N01
status: active
---

# {DECISION} — Finalize US-UTIL-N01 at frozen HOLD and return to portfolio

## Decision / 결정

Finalize Issue #137 / US-UTIL-N01 as **`{GATE}`** using corrected Run `35008869612`, preserve Runs `35007853296` and `35007936755` as implementation-invalid lineage, do not open Reliability magnitudes, and return the engine to Stage 0 portfolio selection. / Issue #137을 frozen HOLD로 종결하고 Reliability 값은 열지 않으며 Stage 0 포트폴리오 선택으로 복귀한다.

## Rationale / 근거

The corrected outcome-blind design fails multiple preregistered requirements: eligible Utility Numbers **{diagnostics['eligible_utilities']} < 500**, exposed candidates **{candidates['exposed']} < 300**, exact AMI-key conflicts **{diagnostics['ami_duplicate_conflicts']} > 0**, matched pairs **{matching['pairs']} < 150**, states **{matching['states']} < 25**, and represented-year pair support below 30/year. No threshold, denominator, aggregation, caliper, year or geography rescue is authorized after observing support.

## Boundary / 경계

- No US-UTIL-E01 authorization from this N01.
- SAIDI/SAIFI/CAIDI magnitudes remain closed.
- No AMI effect, reliability benefit, resilience or causal claim.
- Any descendant requires a new portfolio decision and prospective design.
- Incremental monetary cost remains 0 USD.
""", encoding="utf-8")

    append_once(
        REG / "CLAIM_LEDGER.md",
        f"`{CLAIM}`",
        f"| `{CLAIM}` | Corrected US-UTIL-N01 outcome-blind AMI-ramp design fails frozen identifiability/support requirements; no Reliability magnitude opened. / 교정된 US-UTIL-N01 설계가 고정 support 요건을 충족하지 못했으며 Reliability 값은 개봉하지 않았다. | `DERIVED` | `V3_OUTCOME_BLIND_DESIGN_GATE` | Issue #137; Run `35008869612`; `research/US-UTIL-N01/RESULT.md` | 2026-09-16 | active |\n",
    )
    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | 2026-09-16 | Finalize US-UTIL-N01 as `{GATE}` and return to Stage 0; do not open Reliability outcomes or rescue the frozen design. / US-UTIL-N01을 HOLD로 종결하고 Stage 0로 복귀하며 Reliability outcome 개봉·사후구제를 금지한다. | Corrected Run `35008869612` fails multiple frozen support thresholds under unchanged Issue #137 contract. | Issue #137; `{CLAIM}`; `research/US-UTIL-N01/RESULT.md` | active |\n",
    )

    status = f"""---
checkpoint_id: CHK-20260916-US-UTIL-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 137
last_completed_research: US-UTIL-N01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-UTIL-N01 is terminal at **`{GATE}`** under corrected Run `35008869612`, {DECISION} and {CLAIM}. Reliability magnitudes were never opened and no AMI→Reliability relationship was computed. / US-UTIL-N01은 frozen design-support HOLD로 종결됐으며 Reliability 값과 관계계산은 개봉되지 않았다.

## Terminal evidence / 종결 근거

- eligible Utility Numbers: **{diagnostics['eligible_utilities']:,} / 500 required**
- exposed candidates: **{candidates['exposed']:,} / 300 required**
- control candidates: **{candidates['control']:,} / 300 required**
- exact AMI-key conflicts: **{diagnostics['ami_duplicate_conflicts']:,} / 0 required**
- matched pairs: **{matching['pairs']:,} / 150 required**
- matched states: **{matching['states']:,} / 25 required**
- pair fingerprint: `{matching['pair_identity_sha256']}`

## Exact next action / 정확한 다음 행동

Return to Stage 0 and open a new portfolio reselection only. Re-score surviving candidates using marginal information gained from terminal US-MINE-N01 and US-UTIL-N01; do not automatically promote a prior runner-up, do not redesign US-UTIL-N01 post hoc, and do not open any Reliability outcome magnitude. / Stage 0에서 신규 portfolio reselection만 수행한다.

Incremental monetary cost remains **0 USD**.
"""
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    new_checkpoint = {
        "checkpoint_id": "CHK-20260916-US-UTIL-N01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 137,
        "last_completed_research": "US-UTIL-N01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(new_checkpoint, indent=2) + "\n", encoding="utf-8")

    handoff = f"""# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- checkpoint: `CHK-20260916-US-UTIL-N01-TERMINAL`
- active issue: `none`
- active research: `NONE`
- last completed issue: `#137`
- last completed research: `US-UTIL-N01`
- last decision: `{DECISION}`
- state: `{STATE}`

## Latest terminal result / 최신 종결 결과

Corrected Run `35008869612` finalizes **`{GATE}`**. Eligible Utility Numbers = **{diagnostics['eligible_utilities']:,}**, exposed candidates = **{candidates['exposed']:,}**, control candidates = **{candidates['control']:,}**, exact AMI-key conflicts = **{diagnostics['ami_duplicate_conflicts']:,}**, matched pairs = **{matching['pairs']:,}**, matched states = **{matching['states']:,}**. Reliability magnitudes remained unopened; no AMI→Reliability relationship was computed.

Runs `35007853296` and `35007936755` are implementation-invalid lineage and must not be treated as scientific results. / 두 선행 Run은 구현결함 이력이며 과학적 결과가 아니다.

## Exact restart point / 정확한 재개점

Open a new Stage-0 portfolio reselection. Incorporate terminal information from US-MINE-N01 and US-UTIL-N01 into marginal-information/overlap scoring, compare surviving candidates prospectively, select exactly one next branch, and only then authorize its first outcome-blind gate. Do not reopen or rescue US-UTIL-N01 and do not open Reliability magnitudes.

Incremental monetary cost remains **0 USD**.
"""
    (CTX / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

    print(json.dumps({
        "gate": GATE,
        "decision": DECISION,
        "claim": CLAIM,
        "state": STATE,
        "finalizer_run": RUN_ID,
        "eligible_utilities": diagnostics["eligible_utilities"],
        "exposed_candidates": candidates["exposed"],
        "control_candidates": candidates["control"],
        "ami_duplicate_conflicts": diagnostics["ami_duplicate_conflicts"],
        "pairs": matching["pairs"],
        "states": matching["states"],
        "reliability_magnitudes_opened": False,
        "relationship_computed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
