#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
manifest_p = ROOT / "research" / "US-RCRA-N01" / "DESIGN_MANIFEST.json"
readme_p = ROOT / "research" / "US-RCRA-N01" / "README.md"
result_p = ROOT / "research" / "US-RCRA-N01" / "RESULT.md"
claim_p = ROOT / "registry" / "CLM-164.md"
dec_p = ROOT / "registry" / "DEC-171.md"

status = status_p.read_text(encoding="utf-8")
assert "active_issue: 123" in status
assert "active_research: US-RCRA-N01" in status
assert "last_decision: DEC-170" in status

m = json.loads(manifest_p.read_text(encoding="utf-8"))
assert m["gate"] == "PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE"
assert m["boundary"]["found_violation_values_accessed_or_persisted"] is False
assert m["boundary"]["disaster_linked_violation_counts_or_rates_computed"] is False
assert m["boundary"]["relationship_computed"] is False
assert m["paired_cei_structural_support"]["paired_facilities"] >= 100
assert m["paired_cei_structural_support"]["paired_state_territory_fips_count"] >= 20
assert m["paired_cei_structural_support"]["pre_agency_identity_fraction"] >= 0.95
assert m["paired_cei_structural_support"]["post_agency_identity_fraction"] >= 0.95
assert m["cei_identity"]["cei_identity_deterministic"] is True
assert m["literature_overlap"]["near_identical_found"] is False
assert not claim_p.exists()
assert not dec_p.exists()

status_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-N01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 123
last_completed_research: US-RCRA-N01
last_decision: DEC-171
updated: 2026-09-13
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_RCRA_N01_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-RCRA-N01 completed outcome-blind at **`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`**. CEI identity is deterministic; 297 operating TSDFs satisfy the frozen same-facility last-pre/first-post CEI design across 43 state/territory FIPS, with 100% pre/post evaluation-agency identity. Selected-pair `FOUND_VIOLATION` values and disaster-linked compliance relationships remain unopened.

## Exact next action / 정확한 다음 행동

Return to Stage 0. Compare a separately preregistered US-RCRA-E01 paired-CEI experiment against independent alternatives. If US-RCRA remains selected, freeze the paired outcome test, `N/U/Y` handling, agency-change handling, materiality threshold and claim boundary before opening selected-pair `FOUND_VIOLATION` values. N01 PASS does not authorize E01.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text("""---
checkpoint_id: CHK-20260913-US-RCRA-N01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 123
last_completed_research: US-RCRA-N01
last_decision: DEC-171
updated: 2026-09-13
---

# Session Handoff / 세션 인수인계

US-RCRA-N01 / Issue #123 resolves **`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`** outcome-blind.

Frozen structural facts: CEI = `COMPLIANCE EVALUATION INSPECTION` deterministically; 459 operating TSDFs receive a frozen qualifying index disaster after the 365-day washout; after no-pre/no-post and multi-disaster exclusions, 297 same-facility CEI pairs remain across 43 state/territory FIPS. Pre/post evaluation-agency identity is 100%. Literature adjudication is adjacent/not near-identical, not proof of novelty. `FOUND_VIOLATION` values were not accessed or persisted and no disaster-linked compliance relationship was computed.

Exact restart: Stage 0 comparison before any E01. If US-RCRA-E01 is selected, preregister the exact paired statistical test/model, `FOUND_VIOLATION` N/U/Y treatment, agency-change diagnostic/handling, materiality threshold, missingness rules and non-causal claim boundary before opening selected-pair outcomes. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": "CHK-20260913-US-RCRA-N01-PASS-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 123,
    "last_completed_research": "US-RCRA-N01",
    "last_decision": "DEC-171",
    "updated": "2026-09-13"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

result_p.write_text("""---
id: US-RCRA-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-13
issue: 123
gate: PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE
found_violation_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-N01 Result

**`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`**

N01 passes as an outcome-blind paired-inspection design-identifiability gate. This does **not** establish that FEMA-declared disasters change RCRA compliance, and it does not authorize opening the selected CEI-pair `FOUND_VIOLATION` values.

## Frozen structural evidence

- Current RCRAInfo identifies `CEI` deterministically as `COMPLIANCE EVALUATION INSPECTION`; 32,094 CEI rows are present for the 640 operating-TSDF universe.
- 464 operating TSDFs have at least one qualifying 2018–2023 physical-hazard FEMA DR in their exact county; 459 receive a frozen index event after the 365-day qualifying-disaster washout.
- Under the fixed ±730-day same-facility last-pre/first-post CEI rule, 297 facilities remain after excluding 53 with no pre CEI, 32 with no post CEI, and 77 with another qualifying disaster before/on the selected post CEI.
- The 297 pairs span 43 state/territory FIPS, exceeding the preregistered minimum of 20.
- Evaluation-agency identity is present for 100% of selected pre and post CEIs, exceeding the 95% threshold.
- No ambiguous selected-date tie remains under the frozen evaluation-identifier tie-break.
- The bounded literature scan found material adjacent RCRA inspection/compliance and hazard-vulnerability work but no materially near-identical national paired-CEI FEMA-disaster design; novelty is not proven.
- `FOUND_VIOLATION` values were not accessed or persisted; no disaster-linked violation count/rate, coefficient, p-value or relationship was computed.

## Frozen descendant boundary

Any later E01 requires separate Stage-0 selection and preregistration before outcomes are opened. At minimum it must freeze:

- analysis unit = selected same-facility CEI pair;
- exact pre/post pair identities already selected outcome-blind by N01;
- handling of `FOUND_VIOLATION` values `Y`, `N`, and `U`;
- exact paired statistical test/model and inference;
- evaluation-agency-change handling/diagnostic;
- materiality threshold;
- missingness and exclusions;
- non-causal compliance-monitoring interpretation;
- no post-value alternative window, disaster set, CEI substitution or rescue threshold.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE" not in readme:
    readme += "\n## Terminal result / 최종 결과\n\n**`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`** — see `RESULT.md`. PASS is design identifiability only; selected-pair `FOUND_VIOLATION` remains unopened and E01 requires separate authorization.\n"
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text("""---
id: CLM-164
type: claim
created: 2026-09-13
issue: 123
status: active
---

# CLM-164 — Outcome-blind same-facility paired CEI disaster design has sufficient national structural support

US-RCRA-N01 identifies CEI deterministically and constructs 297 uncontaminated same-facility last-pre/first-post CEI pairs across 43 state/territory FIPS under the frozen FEMA DR, washout, ±730-day and multi-disaster rules. Pre/post evaluation-agency identity is 100%.

This supports design identifiability only. `FOUND_VIOLATION` values were not accessed or persisted, and the claim does not establish a disaster-compliance relationship, causal effect, prediction or proven novelty. Cost: **0 USD**.
""", encoding="utf-8")

dec_p.write_text("""---
id: DEC-171
type: decision
created: 2026-09-13
issue: 123
status: accepted
---

# DEC-171 — Finalize US-RCRA-N01 PASS and return to Stage 0 without opening paired outcomes

Finalize Issue #123 at **`PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`** based on 297 qualifying same-facility CEI pairs across 43 state/territory FIPS and 100% pre/post evaluation-agency identity support.

Do not open selected-pair `FOUND_VIOLATION` values under N01 and do not automatically authorize E01. Any E01 requires a separate Stage-0 selection and preregistration of outcome coding, paired test/model, agency-change handling, materiality, missingness and non-causal claim language before values are opened. Cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
claim_row = "| `CLM-164` | US-RCRA-N01 establishes sufficient outcome-blind same-facility paired-CEI disaster design support: 297 pairs across 43 state/territory FIPS with 100% agency identity; paired compliance results remain unopened. / paired CEI 재해 설계의 구조적 식별 가능성이 충분하다. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_DESIGN_GATE` | Run `34721307603`; `research/US-RCRA-N01/DESIGN_MANIFEST.json`; Issue #123 | 2026-09-13 | active |"
assert "`CLM-164`" not in claim_log
claim_log_p.write_text(claim_log.rstrip() + "\n\n" + claim_row + "\n", encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
dec_row = "| `DEC-171` | 2026-09-13 | Finalize US-RCRA-N01 at `PASS_US_RCRA_N01_PAIRED_CEI_DESIGN_IDENTIFIABLE`; keep paired `FOUND_VIOLATION` unopened and return Stage 0. / N01 PASS 종결·paired 결과 미개방·Stage 0 복귀. | 297 frozen pairs across 43 state/territory FIPS and 100% agency identity satisfy every structural gate; E01 remains separately blocked. | Issue #123; `CLM-164`; Run `34721307603` | active |"
assert "`DEC-171`" not in dec_log
dec_log_p.write_text(dec_log.rstrip() + "\n\n" + dec_row + "\n", encoding="utf-8")
