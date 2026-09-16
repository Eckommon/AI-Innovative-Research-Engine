#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "US-FTA-TRANSIT-N01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 148
RUN = 35138272269
STAGING_COMMIT = "d8d244fc2a3d8b5f7ca47a9c2dc9863b7c6a159d"
DECISION = "DEC-209"
CLAIM = "CLM-186"
GATE = "HOLD_US_FTA_TRANSIT_N01_MATCHED_RELIABILITY_DESIGN_NOT_IDENTIFIABLE"
STATE = "US_FTA_TRANSIT_N01_HOLD__PORTFOLIO_RESELECTION_REQUIRED"
TODAY = "2026-09-17"


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
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-N01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-FTA-TRANSIT-N01",
        "last_completed_issue": 147,
        "last_completed_research": "US-FTA-TRANSIT-F01",
        "last_decision": "DEC-208",
        "updated": "2026-09-16",
    }

    s = json.loads((RESEARCH / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    assert s["protocol"] == "US-FTA-TRANSIT-N01"
    assert s["issue"] == ISSUE
    assert s["contract_commit"] == "c4a7f4ea05954fd013714ee6c891d489a6cfc82f"
    assert s["valid_evaluation"] is True
    assert s["disposition"] == GATE
    assert set(s["checks"]) == {str(i) for i in range(1, 18)}
    failed = {k for k, v in s["checks"].items() if not v["pass"]}
    assert failed == {"7", "9", "10"}, failed
    b = s["boundaries"]
    for k in [
        "major_safety_event_row_values_opened",
        "future_safety_event_membership_opened",
        "row_level_breakdown_event_join_persisted",
        "relationship_computed",
        "predictive_metric_computed",
        "causal_claim_made",
        "manual_or_fuzzy_identity_repair_used",
    ]:
        assert b[k] is False, (k, b[k])
    assert s["incremental_monetary_cost_usd"] == 0

    d = s["diagnostics"]
    manifest_sha = s["manifest"]["sha256"]

    (RESEARCH / "RESULT.md").write_text(f'''---
id: US-FTA-TRANSIT-N01-RESULT
type: outcome-blind-matched-reliability-design-identifiability
created: {TODAY}
issue: {ISSUE}
state: COMPLETED_HOLD
gate: {GATE}
source_run: {RUN}
staging_commit: {STAGING_COMMIT}
major_safety_event_row_values_opened: false
future_safety_event_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-N01 Result — frozen matched-design HOLD

**`{GATE}`**

Run `{RUN}` validly executed the preregistered N01 contract against official FTA Annual Breakdowns only. The design retains substantial support, but **3 of 17 frozen PASS requirements fail**, so the branch is terminal at HOLD without threshold, stratum, mode, matching, or balance rescue.

## What passed / 통과한 지원

- actual official Breakdowns rows read: **{s['source_evidence']['rows_read']:,}**;
- canonical source-grain keys: **{d['canonical_source_grain_keys']:,}**;
- conflicting source-grain keys: **{d['conflicting_source_grain_keys']:,}**;
- quality-invalid agency-mode-years excluded fail-closed: **{d['quality_invalid_agency_mode_years']:,}**;
- unique retained agencies after temporal eligibility and one-unit-per-agency: **{d['retained_unique_agencies']:,}** (required >=400);
- deterministic matched pairs: **{d['matched_pairs']:,}** (required >=100);
- every matched HIGH intensity is strictly above its LOW counterpart: **PASS**;
- no NTD ID is reused in the final manifest: **PASS**;
- immutable outcome-blind manifest SHA-256: `{manifest_sha}`.

## Frozen requirements that fail / 실패한 사전고정 요건

1. **Design-eligible strata:** {d['design_eligible_strata']} < 8 required. Of {d['all_strata']} total strata, {d['dropped_small_strata']} were below the frozen n>=12 support floor.
2. **Matched mode diversity:** {len(d['matched_modes'])} modes `{', '.join(d['matched_modes'])}` < 5 required.
3. **VRM balance:** {d['vrm_balanced_pairs']}/{d['matched_pairs']} = **{d['vrm_balance_fraction']:.2%}** < 80% required for both exposure-year and follow-up-year HIGH:LOW VRM ratios to fall in [1/3, 3].

These failures are not implementation defects. They arise under the exact preregistered design and therefore cannot be repaired post hoc by lowering the strata threshold, pooling modes, changing quartiles, relaxing balance, or rematching after inspecting support.

## Outcome-blind boundary / 결과 비개봉 경계

- Major Safety/Security Event row values: **not opened**;
- next-year Safety-event membership: **not opened**;
- Breakdown→event row join: **not persisted**;
- relationship/predictive statistic: **not computed**;
- agency safety ranking: **not computed**;
- causal claim: **not made**;
- fuzzy/manual identity repair: **not used**;
- incremental monetary cost: **0 USD**.

The 103-pair manifest remains durable only as an audit artifact of the failed preregistered design. It does **not** authorize E01 because N01 did not pass.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve `US-FTA-TRANSIT-001` as a structurally promising but N01-insufficient asset. Do not open the prospectively defined E01 safety outcome, and do not rescue this branch by changing the frozen N01 design after observing support. A later redesign is permitted only through a new independent prospective portfolio decision.
''', encoding="utf-8")

    readme_path = RESEARCH / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    marker = "## Terminal N01 result / N01 최종 결과"
    if marker not in readme:
        readme += f'''\n\n{marker}\n\n**`{GATE}`** — Run `{RUN}` retained {d['retained_unique_agencies']} agencies and {d['matched_pairs']} deterministic pairs but failed frozen requirements 7, 9 and 10: {d['design_eligible_strata']}<8 eligible strata, {len(d['matched_modes'])}<5 matched modes, and {d['vrm_balance_fraction']:.2%}<80% VRM balance. E01 is not authorized. See `RESULT.md`. Manifest SHA-256: `{manifest_sha}`.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: {TODAY}
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_DESIGN
status: active
---

# {CLAIM} — Frozen FTA transit matched reliability design is not identifiable at its preregistered support floors

Run `{RUN}` validly retains **{d['retained_unique_agencies']}** agencies and **{d['matched_pairs']}** deterministic HIGH/LOW pairs, but only **{d['design_eligible_strata']}** design-eligible strata and **{len(d['matched_modes'])}** matched modes are available, while only **{d['vrm_balance_fraction']:.2%}** of pairs satisfy the frozen two-year VRM balance rule. Requirements 7, 9 and 10 therefore fail and N01 is terminal at HOLD.

This is an outcome-blind design-support claim only. No Major Safety/Security row value or relationship was opened.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: {TODAY}
issue: {ISSUE}
research: US-FTA-TRANSIT-N01
status: active
---

# {DECISION} — Accept US-FTA-TRANSIT-N01 HOLD and return to Stage 0

## Decision / 결정

Accept immutable staging commit `{STAGING_COMMIT}` from Run `{RUN}` as **`{GATE}`** and close Issue #{ISSUE} as completed.

Do not execute E01. Do not lower the frozen 8-strata, 5-mode, or 80%-balance thresholds; pool modes; alter quartiles; or rematch after observing N01 support. Return to Stage 0 portfolio selection.

## Preserved asset / 보존 자산

`US-FTA-TRANSIT-001` remains structurally promising: 514 retained agencies and 103 deterministic pairs were available. The failure is specifically design identifiability under the preregistered diversity/balance floors, not source absence and not a safety-outcome finding.

Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(
        REG / "CLAIM_LEDGER.md",
        f"`{CLAIM}`",
        f"| `{CLAIM}` | US-FTA-TRANSIT-N01 valid HOLD: 514 retained agencies and 103 pairs, but 6<8 eligible strata, 3<5 matched modes and 70.87%<80% two-year VRM balance; safety outcomes unopened. / 사전고정 matched design 식별성 HOLD. | `DERIVED` | `V2_PRIMARY_VERIFIED_DESIGN` | Issue #148; Run {RUN}; `research/US-FTA-TRANSIT-N01/RESULT.md` | {TODAY} | active |\n",
    )
    append_once(
        REG / "DECISION_LOG.md",
        f"`{DECISION}`",
        f"| `{DECISION}` | {TODAY} | Accept US-FTA-TRANSIT-N01 HOLD; do not execute E01; return to Stage 0 portfolio selection. / N01 HOLD 수용, E01 비승인, Stage 0 복귀. | Immutable staging `{STAGING_COMMIT}`; Run {RUN}; frozen checks 7/9/10 fail; outcome boundary preserved. | Issue #148; `{CLAIM}`; `research/US-FTA-TRANSIT-N01/RESULT.md` | active |\n",
    )

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-FTA-TRANSIT-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 148
last_completed_research: US-FTA-TRANSIT-N01
last_decision: {DECISION}
updated: {TODAY}
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FTA-TRANSIT-N01 is terminal at **`{GATE}`** under {DECISION} / {CLAIM}. Run `{RUN}` retained **514** agencies and **103** deterministic pairs, but the frozen design has only **6** eligible strata, **3** matched modes (`DR`, `MB`, `VP`), and **70.87%** two-year VRM balance. Requirements 7, 9 and 10 fail. No Major Safety/Security outcome row was opened, so E01 is not authorized.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection and create the next independent portfolio reselection mission. Preserve US-FTA-TRANSIT-001 as an N01-insufficient asset; do not rescue it by post-hoc threshold or matching changes.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-US-FTA-TRANSIT-N01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": ISSUE,
        "last_completed_research": "US-FTA-TRANSIT-N01",
        "last_decision": DECISION,
        "updated": TODAY,
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-FTA-TRANSIT-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 148
last_completed_research: US-FTA-TRANSIT-N01
last_decision: {DECISION}
updated: {TODAY}
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- terminal gate: `{GATE}`
- source run: `{RUN}`
- immutable staging commit: `{STAGING_COMMIT}`
- retained agencies: 514
- matched pairs: 103
- eligible strata: 6 / required 8
- matched modes: 3 / required 5 (`DR`, `MB`, `VP`)
- two-year VRM balance: 70.87% / required 80%
- pair manifest SHA-256: `{manifest_sha}`
- Major Safety/Security row values opened: false
- future Safety membership opened: false
- relationship/prediction/causality: false
- E01 authorized: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Begin a new Stage 0 portfolio reselection mission. Do not redesign or rescue US-FTA-TRANSIT-N01 from its observed support. Any future revisit requires a new independent prospective portfolio decision.
''', encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
