#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-13"
status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-160.md"
decision_path = ROOT / "registry" / "DEC-165.md"
research_dir = ROOT / "research" / "US-WW-E01"
raw_path = research_dir / "EXECUTION_RESULT.json"
result_path = research_dir / "RESULT.md"
readme_path = research_dir / "README.md"

status = status_path.read_text(encoding="utf-8")
assert "active_issue: 119" in status
assert "active_research: US-WW-E01" in status
assert "last_completed_issue: 118" in status
assert "last_decision: DEC-164" in status
assert raw_path.exists()
for p in (claim_path, decision_path, result_path):
    assert not p.exists(), f"already exists: {p}"

r = json.loads(raw_path.read_text(encoding="utf-8"))
assert r["gate"] == "NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP"
assert r["structural_gate"]["pass_group_threshold"] is True
assert r["structural_gate"]["pass_state_threshold"] is True
assert r["structural_gate"]["pass_rank"] is True
assert r["future_outcomes_opened_before_structural_gate"] is False
assert r["relationship_computed"] is True

result_path.write_text("""---
id: US-WW-E01-RESULT
type: preregistered-relationship-test
created: 2026-09-13
issue: 119
gate: NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP
claim_boundary: non-causal-predictive
incremental_monetary_cost_usd: 0
---

# US-WW-E01 Result

**`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**

The frozen structural gate passed, so the authorized second pass opened the 2023–2025 binary future incident outcome and fit the single preregistered state-fixed-effect HC1 linear-probability model. The positive hypothesis did **not** pass.

## Structural gate

- all-linked-permit exact facilities: **14,560**
- documented-need facilities: **7,616**
- baseline-clean documented-need facilities: **3,785**
- eligible before state-overlap restriction: **3,761**
- both-group state/territory codes: **46**
- primary model exposed: **2,503**
- primary model comparator: **1,222**
- design rank: **48 / 48**

All preregistered structural thresholds passed before future outcome membership/count/rate was derived.

## Primary preregistered result

Model: `Y ~ intercept + exposed + compliance-reason leakage stratum + state FE`, OLS LPM with HC1 covariance.

- `n = 3,725`
- exposure coefficient `beta = -0.0221841` = **−2.218 percentage points**
- HC1 SE = **0.0164862**
- 95% CI = **[−0.0544964, +0.0101283]**
- two-sided normal p = **0.178427**
- frozen positive materiality floor = **+0.03**

Because `beta` is negative and the confidence interval includes zero, the frozen gate resolves to **`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**.

## Pre-specified non-rescuing diagnostics

Raw facility outcome:
- exposed: **735 / 2,503 = 29.3648%**
- comparator: **415 / 1,222 = 33.9607%**
- unadjusted risk difference: **−4.5960pp**
- risk ratio: **0.8647**

Leakage strata:
- `L=0`: 447 exposed vs 288 comparator; risks 32.6622% vs 35.0694%, RD −2.4073pp;
- `L=1`: 2,056 exposed vs 934 comparator; risks 28.6479% vs 33.6188%, RD −4.9710pp.

The preregistered `L=0` sensitivity model was **not run** because the stratum did not retain >=500 facilities in each exposure group. This cannot rescue or change the primary disposition.

Nonexclusive future-event table contribution counts among model facilities:
- PS: 400 facilities
- CS: 131 facilities
- SE: 782 facilities

## Interpretation boundary

This result does **not** show that wet-weather/conveyance needs protect facilities, nor does it establish any causal effect. It only fails to support the preregistered positive predictive association under this specific public-data design. The point estimate is negative, but the interval spans zero.

The structural diagnostic found **578 official NPDES permit IDs linked to more than one CWNS facility** in the wider exact-linked universe. This was not a preregistered exclusion or covariance rule and therefore cannot be used post hoc to alter the primary result. It is recorded as a limitation for any future independent research question.

Material adjacent prior work remains acknowledged; no novelty is claimed for CWNS×NPDES linkage itself.

## Exact next action

Treat E01 as terminal under its frozen hypothesis. Do not rerun with a different need-category subset, date rule, threshold, model, or exclusion to seek a positive result. Return to Stage 0 and compare independent alternatives rather than rescuing this branch.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-160
type: claim
created: 2026-09-13
issue: 119
status: active
---

# CLM-160 — US-WW-E01 does not support the preregistered positive incident-compliance prediction

After the frozen structural gate passed, the single preregistered facility-level state-FE HC1 LPM produced `beta = -0.0221841` (95% CI `[-0.0544964, +0.0101283]`, p=`0.178427`) for the 2022 III-A/III-B/V structural-need profile. Raw risks were 29.3648% exposed versus 33.9607% comparator.

The result is `NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`. It is non-causal and does not prove a protective effect. No post-hoc model/date/threshold/exposure rescue is authorized. Cost: **0 USD**.
""", encoding="utf-8")

decision_path.write_text("""---
id: DEC-165
type: decision
created: 2026-09-13
issue: 119
status: accepted
---

# DEC-165 — Finalize US-WW-E01 as no preregistered positive relationship and return Stage 0

Finalize Issue #119 at **`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**. The structural gate passed and future outcomes were opened only afterward; the frozen primary beta was negative and its 95% CI included zero.

Treat this E01 hypothesis as terminal. Do not rescue it by changing need categories, violation-date semantics, permit selection, baseline/future windows, leakage handling, model, covariance rule or +3pp materiality threshold after observing outcomes. Preserve the shared-permit diagnostic only as a limitation, not as a post-hoc exclusion or inferential change.

Return to Stage 0 and prioritize independent alternatives. Cost remains **0 USD**.
""", encoding="utf-8")

readme_path.write_text("""---
id: US-WW-E01
issue: 119
state: COMPLETED_TERMINAL_NO_POSITIVE
selection_decision: DEC-163
authorization_decision: DEC-164
final_decision: DEC-165
relationship_computed: true
incremental_monetary_cost_usd: 0
---

# US-WW-E01 — Preregistered Structural-Need Profile × Incident-Compliance Test

**Final disposition:** `NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`

The frozen structural gate passed and the one authorized future-outcome test was executed. The primary state-FE HC1 LPM estimated `beta=-0.0221841`, 95% CI `[-0.0544964,+0.0101283]`, p=`0.178427`; therefore the preregistered positive/material gate did not pass.

This branch is terminal under the tested hypothesis. No causal or protective-effect claim is supported. See `RESULT.md` and `EXECUTION_RESULT.json`. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-E01-TERMINAL-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 119
last_completed_research: US-WW-E01
last_decision: DEC-165
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WW_E01_NO_POSITIVE__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-WW-E01 completed at **`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**. Structural support passed, but the frozen primary exposure coefficient was −2.218pp (95% CI −5.450pp to +1.013pp; p=0.1784), so the positive hypothesis failed. This is non-causal and does not establish a protective effect.

## Exact next action / 정확한 다음 행동

Return to Stage 0 and compare independent alternatives. Do not rescue US-WW-E01 with post-outcome category/date/model/threshold changes.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-E01-TERMINAL-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 119
last_completed_research: US-WW-E01
last_decision: DEC-165
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

US-WW-E01 / Issue #119 is terminal at **`NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`**.

Primary: n=3,725; beta=−0.0221841; HC1 95% CI [−0.0544964,+0.0101283]; p=0.178427. Raw risks: 29.3648% exposed vs 33.9607% comparator. The result is non-causal and does not establish a protective effect. The preregistered L=0 sensitivity did not run because it failed the >=500-each diagnostic threshold. A shared-permit structural limitation was recorded but cannot alter the primary result post hoc.

Exact restart: Stage 0 independent-candidate comparison. Do not rerun/rescue E01 with modified categories, date semantics, windows, leakage handling, model, covariance or materiality threshold. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-WW-E01-TERMINAL-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 119,
    "last_completed_research": "US-WW-E01",
    "last_decision": "DEC-165",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-160`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-160` | US-WW-E01 does not support the preregistered positive 2022 structural-need-profile → 2023–2025 incident-compliance relationship: beta −0.0221841, 95% CI [−0.0544964,+0.0101283], p=0.178427; raw risk 29.3648% vs 33.9607%. / 사전등록 positive 관계는 지지되지 않는다. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_RELATIONSHIP_GATE` | Run `34708498104`; `research/US-WW-E01/EXECUTION_RESULT.json`; `RESULT.md` | 2026-09-13 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-165`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-165` | 2026-09-13 | Finalize US-WW-E01 as `NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP`; prohibit post-outcome rescue and return Stage 0. / E01 positive 관계 미지지·사후 구제 금지·Stage 0 복귀. | Structural gate passed, but frozen beta was negative and CI included zero; diagnostics cannot rescue primary. | Issue #119; `CLM-160`; Run `34708498104`; `research/US-WW-E01/RESULT.md` | active |
""", encoding="utf-8")

print(json.dumps({"gate":"NO_PREREGISTERED_POSITIVE_US_WW_E01_RELATIONSHIP","issue":119,"beta":r["primary"]["beta"],"cost_usd":0}))
