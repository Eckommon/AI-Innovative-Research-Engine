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
claim_path = ROOT / "registry" / "CLM-158.md"
decision_path = ROOT / "registry" / "DEC-162.md"
research_dir = ROOT / "research" / "US-WW-N01"
result_path = research_dir / "RESULT.md"
readme_path = research_dir / "README.md"
manifest_path = research_dir / "DESIGN_MANIFEST.json"
semantic_path = research_dir / "SEMANTIC_ADJUDICATION.md"
literature_path = research_dir / "LITERATURE_OVERLAP.md"

status = status_path.read_text(encoding="utf-8")
assert "active_issue: 116" in status
assert "active_research: US-WW-N01" in status
assert "last_completed_issue: 115" in status
assert "last_decision: DEC-161" in status
for p in (manifest_path, semantic_path, literature_path):
    assert p.exists(), f"missing prerequisite: {p}"
for p in (claim_path, decision_path, result_path):
    assert not p.exists(), f"already exists: {p}"

manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
assert manifest["boundary"]["future_2023_2025_outcome_counts_read_or_persisted"] is False
assert manifest["boundary"]["future_outcome_rates_computed"] is False
assert manifest["boundary"]["relationship_computed"] is False
assert manifest["boundary"]["need_dollar_magnitudes_read"] is False
assert manifest["population"]["exact_link_support_fraction_of_linked"] >= 0.80
assert manifest["exposure"]["pass_500_each"] is True
assert manifest["baseline_identity"]["pass_80pct_identity_route"] is True
assert manifest["baseline_identity"]["baseline_clean_exposed_facilities"] >= 500
assert manifest["baseline_identity"]["baseline_clean_comparator_facilities"] >= 500

result_path.write_text("""---
id: US-WW-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-13
issue: 116
gate: PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE
future_outcome_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WW-N01 Result

**`PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`**

N01 passes as an outcome-blind design-identifiability gate. This is **not** evidence that 2022 CWNS need profiles predict later NPDES compliance events, and it does not authorize opening the 2023–2025 future outcome window.

## Frozen structural evidence

- 14,578 CWNS wastewater facilities have official NPDES linkage; requiring **all** linked permits for a facility to exact-match `ICIS_PERMITS` retains 14,560 facilities (99.8765%).
- Among exact-linked facilities with at least one documented CWNS need category, 5,018 satisfy the frozen wet-weather/conveyance exposure identity (`III-A`, `III-B`, or `V`) and 2,598 satisfy the documented-need comparator identity; both exceed the preregistered >=500 threshold.
- PS/CS/SE violation tables expose baseline 2019–2021 date/type identities. Under the frozen all-linked-permits baseline-clean rule, 2,437 exposed facilities and 1,189 comparator facilities remain, again exceeding >=500 each.
- `REASON_FOR_NEEDS` exposes deterministic exact text identities. The initial regex candidate list produced one semantic false positive because `unregulated` contains `regulat`; this was corrected outcome-blind before final disposition.
- The frozen explicit compliance-driven leakage stratum consists only of four exact labels concerning new permit requirements, maintenance of NPDES permit compliance, TMDL compliance, and anticipated new permit requirements. The broader resiliency and unregulated-impact labels are not classified as explicit compliance-driven reasons.
- The 2023–2025 future-window compliance count/rate remains unopened; no future outcome prevalence, coefficient, p-value or relationship was computed.

## Literature-overlap boundary

Hanyi (Livia) Yi's `Financing Public Goods` is material adjacent prior work: it merges NPDES violation data with CWNS infrastructure-upgrade information and studies annual wastewater violations in a municipal-credit-shock design. This prevents any claim that CWNS×NPDES linkage or infrastructure-needs/violation analysis is itself novel.

The bounded proposed descendant remains distinguishable: 2022 structural need-category profile, all-linked-permit facility identity, 2019–2021 baseline-clean history, pre-frozen explicit compliance-reason leakage stratum, and a first post-baseline incident identity in 2023–2025 under a non-causal predictive claim boundary. Current search therefore resolves the N01 novelty check as **adjacent, not materially near-identical**.

## Frozen descendant contract carried forward

Any later E01 must preserve, before future outcomes are opened:

- facility as the analysis unit;
- every official linked NPDES permit travels with its CWNS facility;
- exposure = at least one of `III-A`, `III-B`, `V`;
- comparator = documented need category present, but none of `III-A`, `III-B`, `V`;
- baseline-clean = no recorded PS/CS/SE violation identity across all linked permits during 2019-01-01 through 2021-12-31;
- future window = 2023-01-01 through 2025-12-31;
- explicit compliance-reason exact-label indicator as a pre-specified leakage stratum;
- missingness/drop rules fixed without future outcomes;
- non-causal predictive interpretation only.

A separate Stage-0 selection and E01 preregistration are required before any future compliance outcome magnitude is opened.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-158
type: claim
created: 2026-09-13
issue: 116
status: active
---

# CLM-158 — US-WW-N01 supports a leakage-controlled incident-compliance predictive design without opening future outcomes

The outcome-blind N01 probe retains 14,560 facilities when all officially linked NPDES permits must exact-match ICIS, identifies 5,018 exposed and 2,598 documented-need comparator facilities, and leaves 2,437 exposed versus 1,189 comparator facilities under the frozen 2019–2021 baseline-clean rule. CWNS `REASON_FOR_NEEDS` exact labels allow an explicit compliance-driven leakage stratum to be fixed before outcomes.

Current literature includes material adjacent CWNS×NPDES violation work, so novelty is bounded to the 2022 structural-need-profile → post-baseline incident predictive design with baseline-clean and explicit leakage control. No 2023–2025 future outcome count/rate or relationship has been opened. Cost: **0 USD**.
""", encoding="utf-8")

decision_path.write_text("""---
id: DEC-162
type: decision
created: 2026-09-13
issue: 116
status: accepted
---

# DEC-162 — Finalize US-WW-N01 as PASS and return to Stage 0

Finalize Issue #116 at **`PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`**.

Freeze the exact-label compliance-reason leakage stratum documented in `SEMANTIC_ADJUDICATION.md`; do not use the initial permissive regex candidate list as the scientific rule. Treat Hanyi Yi's `Financing Public Goods` as material adjacent prior work and prohibit claims that CWNS×NPDES merging or infrastructure-needs/violation analysis is itself novel.

Do **not** authorize opening 2023–2025 future compliance outcomes from this PASS. Return to Stage 0 and require a separate E01 selection/preregistration before any future outcome magnitude is read or computed. Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

readme_path.write_text("""---
id: US-WW-N01
issue: 116
state: COMPLETED_PASS_DESIGN_IDENTIFIABLE
selection_decision: DEC-160
authorization_decision: DEC-161
final_decision: DEC-162
future_outcome_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-WW-N01 — Leakage-Controlled Incident Compliance Design Identifiability

**Final disposition:** `PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`

The branch proves only that a bounded facility-level incident-compliance predictive design can be preregistered with exact CWNS→NPDES→ICIS identities, documented exposure/comparator support, 2019–2021 baseline-clean handling, and an exact-label compliance-reason leakage stratum. It does not establish predictive value or causality and does not authorize 2023–2025 future outcome magnitudes.

See `RESULT.md`, `DESIGN_MANIFEST.json`, `SEMANTIC_ADJUDICATION.md`, and `LITERATURE_OVERLAP.md`. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-N01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 116
last_completed_research: US-WW-N01
last_decision: DEC-162
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WW_N01_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-WW-N01 completed outcome-blind at **`PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`**. The frozen design has strong exact-link, exposed/comparator and baseline-clean structural support, and explicit compliance-driven CWNS reasons can be handled as a pre-specified leakage stratum. Material adjacent CWNS×NPDES violation literature exists, so novelty claims remain bounded. No 2023–2025 future compliance outcome magnitude or relationship was opened.

## Exact next action / 정확한 다음 행동

Return to Stage 0. Compare a separately preregistered US-WW-E01 incident-prediction experiment against independent alternatives. Future compliance outcomes remain blocked until exact outcome event semantics, model, inferential gate, leakage-stratum treatment and missingness rules are frozen in a new authorization.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260913-US-WW-N01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 116
last_completed_research: US-WW-N01
last_decision: DEC-162
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

US-WW-N01 / Issue #116 resolves **`PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`** with no future outcome magnitude opened.

Durable design facts: 14,560 all-linked-permit exact-match facilities; 5,018 exposed vs 2,598 documented-need comparator; baseline-clean 2,437 vs 1,189. Explicit compliance-driven `REASON_FOR_NEEDS` handling is frozen to four exact labels as a leakage stratum; `unregulated water quality or human health impacts` is explicitly not treated as a compliance-driven label. Hanyi Yi's `Financing Public Goods` is material adjacent prior work, so the project must not claim novelty for CWNS×NPDES merging itself.

Exact restart: Stage 0 comparison before any E01. If US-WW remains selected, preregister exact 2023–2025 first-incident outcome semantics, model, inferential/materiality gate, leakage-stratum treatment and missingness rules before opening future outcomes. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-WW-N01-PASS-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 116,
    "last_completed_research": "US-WW-N01",
    "last_decision": "DEC-162",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-158`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-158` | US-WW-N01 supports a leakage-controlled 2022 CWNS structural-need-profile → post-baseline NPDES incident predictive design: 14,560 all-permit exact-linked facilities, 5,018 exposed vs 2,598 comparator, and baseline-clean 2,437 vs 1,189, with future outcomes unopened. / leakage 통제 incident-compliance 설계가 값 비사용으로 식별 가능하다. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_DESIGN_GATE` | Run `34693662600`; `research/US-WW-N01/DESIGN_MANIFEST.json`; semantic and literature adjudications | 2026-09-13 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-162`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-162` | 2026-09-13 | Finalize US-WW-N01 as `PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE`; freeze four exact compliance-reason labels as leakage stratum; return Stage 0 without opening future outcomes. / N01 PASS·leakage 규칙 고정·Stage 0 복귀. | Exact-link/exposure/comparator/baseline-clean support passes; adjacent literature is material but not near-identical under the bounded design. | Issue #116; `CLM-158`; Run `34693662600`; `research/US-WW-N01/RESULT.md` | active |
""", encoding="utf-8")

print(json.dumps({
    "gate": "PASS_US_WW_N01_INCIDENT_DESIGN_IDENTIFIABLE",
    "issue": 116,
    "future_outcomes_opened": False,
    "cost_usd": 0,
}))
