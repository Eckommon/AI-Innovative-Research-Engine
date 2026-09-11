#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-WATERWAY-E02"
REG = ROOT / "registry"

primary = json.loads((OUT / "STAGE_B_PRIMARY_RESULT.json").read_text(encoding="utf-8"))
expected = "NO_PREREGISTERED_POSITIVE_US_WATERWAY_E02_RELATIONSHIP"
if primary.get("gate") != expected:
    raise RuntimeError(f"unexpected E02 primary gate: {primary.get('gate')!r}")
if primary.get("status") != "PRIMARY_GATE_FIXED_BEFORE_SENSITIVITIES":
    raise RuntimeError("primary gate was not durably fixed before sensitivities")

result = f'''---
id: US-WATERWAY-E02-RESULT
issue: 102
state: COMPLETED_NO_PREREGISTERED_POSITIVE_RELATIONSHIP
final_gate: {expected}
claim: CLM-145
decision: DEC-142
relationship_computed: true
incremental_monetary_cost_usd: 0
---

# US-WATERWAY-E02 Result / 결과

## Final gate / 최종 판정

**`{expected}`**

Under the prospectively frozen signed-flow contract, the realized panel contained **{primary['N']} gage-year observations**, **{primary['G_gage']} gages**, and **{primary['G_year']} calendar years**.

Primary coefficient:
- beta = **{primary['beta_minutes_per_share_1_0']:.12g} minutes per 1.0 extreme-day share**;
- two-way CR1 SE = **{primary['se_two_way_cr1']:.12g}**;
- df = **{primary['df']}**;
- 95% CI = **[{primary['ci95_lower']:.12g}, {primary['ci95_upper']:.12g}]**;
- two-sided p = **{primary['p_two_sided']:.12g}**;
- model-implied +10 percentage-point difference = **{primary['delta_minutes_per_plus_10pp']:.12g} minutes**.

The point estimate is positive and exceeds the +5 minute materiality floor, but the preregistered 95% CI lower bound is not above zero. Therefore E02 does **not** establish the preregistered positive relationship.

This is not evidence that the true relationship is zero. It is a failure to satisfy the frozen positive-detection gate under this panel/model/inference contract.

Prespecified high-flow-only, low-flow-only, and leave-one-gage-out analyses were run only after the primary gate was fixed; none may rescue or reverse the primary classification.

No causal effect, advance prediction, propagation mechanism, novelty, lock ranking, or decision utility is claimed.

Incremental monetary cost: **0 USD**.
'''
(OUT / "RESULT.md").write_text(result, encoding="utf-8")

readme = (OUT / "README.md").read_text(encoding="utf-8")
readme = readme.replace("state: ACTIVE_PREREGISTERED", "state: COMPLETED_NO_PREREGISTERED_POSITIVE_RELATIONSHIP")
readme = readme.replace("relationship_computed: false", "relationship_computed: true")
if "## Final disposition / 최종 처분" not in readme:
    readme = readme.rstrip() + f'''\n\n## Final disposition / 최종 처분\n\nRun `34577544880` resolves E02 as **`{expected}`**. Realized panel: {primary['N']} gage-years / {primary['G_gage']} gages / {primary['G_year']} years. beta={primary['beta_minutes_per_share_1_0']:.12g}, 95% CI=[{primary['ci95_lower']:.12g}, {primary['ci95_upper']:.12g}], p={primary['p_two_sided']:.12g}, +10pp={primary['delta_minutes_per_plus_10pp']:.12g} minutes. The positive point estimate does not pass the preregistered CI gate. No automatic descendant is authorized; return to Stage 0.\n'''
(OUT / "README.md").write_text(readme, encoding="utf-8")

claim = f'''---
id: CLM-145
type: claim
created: 2026-09-11
issue: 102
status: active
---

# CLM-145 — US-WATERWAY-E02 does not establish the preregistered positive signed-flow relationship

Under the frozen signed-flow E02 panel and inference contract, the primary annual association fit used **{primary['N']} gage-year observations across {primary['G_gage']} gages and {primary['G_year']} years**. The extreme-flow-share coefficient was **{primary['beta_minutes_per_share_1_0']:.12g} minutes per 1.0 share** (two-way CR1 SE **{primary['se_two_way_cr1']:.12g}**, df **{primary['df']}**, 95% CI **[{primary['ci95_lower']:.12g}, {primary['ci95_upper']:.12g}]**, two-sided p **{primary['p_two_sided']:.12g}**). The implied +10pp difference was **{primary['delta_minutes_per_plus_10pp']:.12g} minutes**.

Although the point estimate is positive and above the screening materiality floor, the 95% CI lower bound is not above zero. The preregistered terminal classification is therefore **`{expected}`**.

This claim means the positive relationship was not established under the frozen design; it does not claim a zero effect or causality. Sensitivities cannot rescue the primary classification. Source: Run `34577544880`, output commit `5d65482dbdb07d5254e6c7674ff300e78a5ba374`. Incremental monetary cost: **0 USD**.
'''
(REG / "CLM-145.md").write_text(claim, encoding="utf-8")

decision = f'''---
id: DEC-142
type: decision
created: 2026-09-11
issue: 102
status: accepted
---

# DEC-142 — Finalize US-WATERWAY-E02 as NO preregistered positive relationship and return to Stage 0

Accept the primary E02 classification **`{expected}`** from Run `34577544880`.

The signed-flow redesign successfully resolved the E01 source-semantics blocker and produced a valid frozen-panel relationship test, but the primary 95% CI includes zero. Preserve the positive point estimate and materiality calculation together with the uncertainty; do not tune percentiles, drop gages, change outcomes, change covariance estimators, or promote a sensitivity to primary.

E02 is complete. No `US-WATERWAY-E03` is automatically authorized. Return to Stage 0 portfolio control and compare marginal information value against independent alternatives before any descendant.
'''
(REG / "DEC-142.md").write_text(decision, encoding="utf-8")

claim_ledger = REG / "CLAIM_LEDGER.md"
cl = claim_ledger.read_text(encoding="utf-8")
line = f'| `CLM-145` | E02 signed-flow primary beta={primary["beta_minutes_per_share_1_0"]:.6f}, +10pp={primary["delta_minutes_per_plus_10pp"]:.6f} min, but 95% CI [{primary["ci95_lower"]:.6f}, {primary["ci95_upper"]:.6f}] includes zero; gate = NO preregistered positive relationship. / 양(+) 점추정이나 CI gate 미통과. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_REPRODUCED` | Run `34577544880`; `research/US-WATERWAY-E02/STAGE_B_PRIMARY_RESULT.json` | 2026-09-11 | active |'
if "`CLM-145`" not in cl:
    claim_ledger.write_text(cl.rstrip() + "\n" + line + "\n", encoding="utf-8")

dlog = REG / "DECISION_LOG.md"
dl = dlog.read_text(encoding="utf-8")
line = f'| `DEC-142` | 2026-09-11 | Finalize US-WATERWAY-E02 as `{expected}` and return to Stage 0; no automatic descendant. / E02 NO 판정·Stage 0 복귀. | Positive point estimate fails frozen CI gate; sensitivities cannot rescue primary. | Issue #102; `CLM-145`; Run `34577544880` | active |'
if "`DEC-142`" not in dl:
    dlog.write_text(dl.rstrip() + "\n" + line + "\n", encoding="utf-8")

status = f'''---
checkpoint_id: CHK-20260911-US-WATERWAY-E02-NO-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 102
last_completed_research: US-WATERWAY-E02
last_decision: DEC-142
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WATERWAY_E02_NO_PREREGISTERED_POSITIVE_RELATIONSHIP__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-WATERWAY-E02 completed a valid preregistered signed-flow relationship test. The primary point estimate was positive and above the materiality floor, but its two-way-CR1 95% CI included zero, so the preregistered positive relationship was not established.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Compare the marginal value of any waterway follow-up against independent ready alternatives; do not tune E02 or automatically open E03.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / "STATUS.md").write_text(status, encoding="utf-8")

handoff = f'''---
checkpoint_id: CHK-20260911-US-WATERWAY-E02-NO-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 102
last_completed_research: US-WATERWAY-E02
last_decision: DEC-142
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-WATERWAY-E02 / Issue #102 is complete at **`{expected}`**.

Primary Run `34577544880`: N={primary['N']}, G={primary['G_gage']}, T={primary['G_year']}, beta={primary['beta_minutes_per_share_1_0']:.12g}, SE={primary['se_two_way_cr1']:.12g}, 95% CI=[{primary['ci95_lower']:.12g}, {primary['ci95_upper']:.12g}], p={primary['p_two_sided']:.12g}, +10pp={primary['delta_minutes_per_plus_10pp']:.12g} minutes.

The signed-flow source-semantic problem is resolved, but the preregistered positive relationship is not established. Do not tune/re-run E02. Next work begins at **Stage 0 portfolio control** with no active research issue.

Incremental monetary cost: **0 USD**.
'''
(ROOT / "context" / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

checkpoint = {
    "checkpoint_id": "CHK-20260911-US-WATERWAY-E02-NO-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 102,
    "last_completed_research": "US-WATERWAY-E02",
    "last_decision": "DEC-142",
    "updated": "2026-09-11",
}
(ROOT / "context" / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
