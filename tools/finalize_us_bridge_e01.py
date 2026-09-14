#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = 34796095655
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
staging_p = ROOT / "research" / "US-BRIDGE-E01" / "STAGING_RESULT.json"
audit_p = ROOT / "research" / "US-BRIDGE-E01" / "STAGING_SOURCE_AUDIT.json"
result_json_p = ROOT / "research" / "US-BRIDGE-E01" / "RESULT.json"
result_md_p = ROOT / "research" / "US-BRIDGE-E01" / "RESULT.md"
readme_p = ROOT / "research" / "US-BRIDGE-E01" / "README.md"
claim_p = ROOT / "registry" / "CLM-170.md"
dec_p = ROOT / "registry" / "DEC-181.md"

ALLOWED = {
    "PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP",
    "POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP",
    "NO_PREREGISTERED_POSITIVE_US_BRIDGE_E01_RELATIONSHIP",
}
status = status_p.read_text(encoding="utf-8")
assert "active_issue: 132" in status
assert "active_research: US-BRIDGE-E01" in status
assert "last_decision: DEC-180" in status
assert "US_BRIDGE_E01_ACTIVE__PAIR_IDENTITY_REVALIDATION_FIRST" in status

r = json.loads(staging_p.read_text(encoding="utf-8"))
a = json.loads(audit_p.read_text(encoding="utf-8"))
assert r["research_id"] == "US-BRIDGE-E01" and r["issue"] == 132
assert r["gate"] in ALLOWED
assert r["pair_identity_revalidated_before_outcome_access"] is True
assert r["n01_pair_count"] == 89800
assert r["n01_pair_identity_sha256"] == "a35d38c8219de527a72c5d4975c6f6c2fed63e92711632fd5adc4b16056269b9"
assert r["n01_pair_artifact_gzip_sha256"] == "4de3b8cbc7152725f72e4a93a0990a26e92579607cca8ecfe3390eba5d69e6e3"
assert r["condition_values_opened"] is True
assert r["condition_access_after_pair_identity_pass"] is True
assert r["nbi_source_hashes_match_n01"] is True
assert r["relationship_computed"] is True
assert r["post_value_rescue_used"] is False
assert r["negative_rd_protective_interpretation_authorized"] is False
assert r["causal_claim_authorized"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert a["pair_validation"]["passed_before_outcome_access"] is True
assert all(x["source_hash_matches_n01"] for x in a["source_audit"])
assert not claim_p.exists() and not dec_p.exists()

gate = r["gate"]
if gate == "PASS_POSITIVE_MATERIAL_US_BRIDGE_E01_RELATIONSHIP":
    state_name = "US_BRIDGE_E01_POSITIVE_MATERIAL__REPLICATION_REQUIRED"
    next_action = "Open only a separately preregistered replication/robustness mission. Do not upgrade this matched association to a causal claim."
elif gate == "POSITIVE_BELOW_MATERIALITY_US_BRIDGE_E01_RELATIONSHIP":
    state_name = "US_BRIDGE_E01_POSITIVE_BELOW_MATERIALITY__PORTFOLIO_RETURN"
    next_action = "Return to Stage 0 independent-candidate comparison; preserve the sub-material positive association without threshold rescue."
else:
    state_name = "US_BRIDGE_E01_NO_POSITIVE_RELATIONSHIP__PORTFOLIO_RETURN"
    next_action = "Return to Stage 0 independent-candidate comparison. Do not rescue US-BRIDGE post hoc and do not reinterpret the negative RD as evidence that disasters protect bridges."

canonical = dict(r)
canonical["workflow_run"] = RUN
canonical["canonical_finalized"] = True
result_json_p.write_text(json.dumps(canonical, indent=2, sort_keys=True) + "\n", encoding="utf-8")

cells = r["paired_cells"]
exact = r["exact_two_sided_mcnemar_binomial"]
classes = r["analyzable_class_counts"]
result_md_p.write_text(f"""---
id: US-BRIDGE-E01-RESULT
type: preregistered-matched-pair-outcome-test
created: 2026-09-14
issue: 132
workflow_run: {RUN}
gate: {gate}
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-E01 Result / 결과

**`{gate}`**

## Preregistered execution integrity / 사전등록 실행 무결성

- N01 pair identity was revalidated **before** condition access: **YES**.
- Frozen pair count: **{r['n01_pair_count']:,}**.
- Pair identity SHA-256: `{r['n01_pair_identity_sha256']}`.
- Compressed pair artifact SHA-256: `{r['n01_pair_artifact_gzip_sha256']}`.
- Frozen class counts: `CULVERT={r['n01_class_counts']['CULVERT']:,}`, `NON_CULVERT={r['n01_class_counts']['NON_CULVERT']:,}`.
- All NBI ZIP/member hashes matched the N01 source manifest before each source's condition fields were used.
- No post-value rescue, alternative threshold, alternative outcome, one-sided test or model substitution was used.

## Primary frozen result / 주 분석 결과

- Complete analyzable matched pairs: **{r['complete_analyzable_pairs']:,} / {r['n01_pair_count']:,} ({r['complete_pair_rate']:.4%})**.
- Analyzable `CULVERT`: **{classes.get('CULVERT', 0):,}**; `NON_CULVERT`: **{classes.get('NON_CULVERT', 0):,}**.
- Exposed deterioration: **{r['exposed_deterioration_count']:,} / {r['complete_analyzable_pairs']:,} = {r['exposed_deterioration_risk']:.6%}**.
- Control deterioration: **{r['control_deterioration_count']:,} / {r['complete_analyzable_pairs']:,} = {r['control_deterioration_risk']:.6%}**.
- Risk difference `exposed - control`: **{r['risk_difference_percentage_points']:+.4f} percentage points**.
- Paired cells `(exposed, control)`: `00={cells['neither_00']:,}`, `10={cells['exposed_only_10']:,}`, `01={cells['control_only_01']:,}`, `11={cells['both_11']:,}`.
- Discordant pairs: **{exact['discordant_n']:,}**.
- Exact two-sided McNemar/binomial p-value: **{exact['p_decimal_50']}**.
- Frozen positive materiality floor: **+5pp**; frozen significance gate: **p < 0.05**.

## Interpretation boundary / 해석 경계

The preregistered positive relationship was not established. The observed RD is negative, but this design does **not** authorize the reversed claim that disasters protect bridges. The result is an association under county-level FEMA exposure timing and matched NBI inspection intervals, not a causal effect. Maintenance/repair responses, inspection ascertainment, exposure misclassification, disaster severity, aging, traffic/environment and other unobserved interventions remain unresolved.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "## Terminal E01 result / E01 최종 결과" not in readme:
    readme += f"\n\n## Terminal E01 result / E01 최종 결과\n\n**`{gate}`** — Run `{RUN}`; complete matched pairs **{r['complete_analyzable_pairs']:,}**; RD **{r['risk_difference_percentage_points']:+.4f}pp**; exact two-sided p **{exact['p_decimal_50']}**. Negative RD is not a protective-effect claim. See `RESULT.md`.\n"
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-170
type: claim
created: 2026-09-14
issue: 132
status: active
---

# CLM-170 — US-BRIDGE-E01 terminal preregistered outcome result

Run `{RUN}` terminates US-BRIDGE-E01 at **`{gate}`** after exact pre-outcome revalidation of all **89,800** frozen N01 pairs and source hashes. Among **{r['complete_analyzable_pairs']:,}** complete matched pairs, exposed deterioration was **{r['exposed_deterioration_risk']:.6%}** versus **{r['control_deterioration_risk']:.6%}** in matched controls, yielding RD **{r['risk_difference_percentage_points']:+.4f}pp**; exact two-sided McNemar/binomial p = **{exact['p_decimal_50']}**.

This establishes only that the frozen preregistered **positive** relationship criterion was not met. The negative RD does not establish a protective causal effect of disasters. No post-value rescue was used. Cost remained **0 USD**.
""", encoding="utf-8")

dec_p.write_text(f"""---
id: DEC-181
type: decision
created: 2026-09-14
issue: 132
status: accepted
---

# DEC-181 — Finalize US-BRIDGE-E01 at {gate}

Finalize Issue #132 / US-BRIDGE-E01 at **`{gate}`** using preregistered Run `{RUN}`. The exact N01 pair identity and source hashes passed before outcome use; the frozen deterioration definition, complete-pair estimand, exact two-sided McNemar/binomial test, `p < 0.05` gate and `RD >= +5pp` materiality floor were applied without post-value modification.

Observed RD was **{r['risk_difference_percentage_points']:+.4f}pp** with exact p **{exact['p_decimal_50']}**. This may not be reversed into a claim that disasters protect bridges and may not be promoted to causality.

Exact next action: {next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-170`" not in claim_log
claim_log += f"\n\n| `CLM-170` | US-BRIDGE-E01 terminates at `{gate}`: {r['complete_analyzable_pairs']:,} complete matched pairs, exposed deterioration {r['exposed_deterioration_risk']:.4%}, control {r['control_deterioration_risk']:.4%}, RD {r['risk_difference_percentage_points']:+.4f}pp, exact two-sided p {exact['p_decimal_50']}; negative RD is not a protective claim. / E01 사전등록 결과검정 종결. | `OBSERVED/DERIVED/VALIDATED` | `V4_PREREGISTERED_MATCHED_OUTCOME` | Run `{RUN}`; `research/US-BRIDGE-E01/RESULT.json`; `RESULT.md`; `STAGING_SOURCE_AUDIT.json` | 2026-09-14 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-181`" not in dec_log
dec_log += f"\n| `DEC-181` | 2026-09-14 | Finalize US-BRIDGE-E01 at `{gate}`; preserve the frozen outcome/test/materiality contract and prohibit protective reverse interpretation. / E01 최종 판정, 역방향 보호효과 해석 금지. | Preregistered Run `{RUN}`; pair/source identity PASS; no post-value rescue. | Issue #132; `CLM-170`; `research/US-BRIDGE-E01/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260914-US-BRIDGE-E01-TERMINAL"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 132
last_completed_research: US-BRIDGE-E01
last_decision: DEC-181
updated: 2026-09-14
---
"""
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `{state_name}`

US-BRIDGE-E01 / Issue #132 is terminal at **`{gate}`** under preregistered Run `{RUN}`. Pair/source identity checks passed before outcome use. Complete matched-pair N = **{r['complete_analyzable_pairs']:,}**; exposed deterioration = **{r['exposed_deterioration_risk']:.6%}**; control = **{r['control_deterioration_risk']:.6%}**; RD = **{r['risk_difference_percentage_points']:+.4f}pp**; exact two-sided p = **{exact['p_decimal_50']}**.

A negative RD does not authorize a protective interpretation, and no causal claim is authorized.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

US-BRIDGE-E01 / Issue #132 is terminal at **`{gate}`** from preregistered Run `{RUN}`.

Before condition access, E01 reproduced all 89,800 N01 pair identities and exact hashes. Frozen NBI source hashes also matched. Primary complete matched-pair N = {r['complete_analyzable_pairs']:,}; exposed deterioration {r['exposed_deterioration_risk']:.6%}; control {r['control_deterioration_risk']:.6%}; RD {r['risk_difference_percentage_points']:+.4f}pp; exact two-sided p {exact['p_decimal_50']}.

The preregistered positive relationship was not established. The negative RD is not a protective-effect claim and no post-value rescue is allowed.

Exact restart: {next_action} Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 132,
    "last_completed_research": "US-BRIDGE-E01",
    "last_decision": "DEC-181",
    "updated": "2026-09-14"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"gate": gate, "run": RUN, "complete_pairs": r["complete_analyzable_pairs"], "rd_pp": r["risk_difference_percentage_points"], "p": exact["p_decimal_50"], "next_action": next_action}, ensure_ascii=False))
