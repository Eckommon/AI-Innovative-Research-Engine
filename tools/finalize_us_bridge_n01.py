#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = 34791950311
status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
result_json_p = ROOT / "research" / "US-BRIDGE-N01" / "DESIGN_RESULT.json"
pair_manifest_p = ROOT / "research" / "US-BRIDGE-N01" / "PAIR_MANIFEST.json"
result_md_p = ROOT / "research" / "US-BRIDGE-N01" / "RESULT.md"
readme_p = ROOT / "research" / "US-BRIDGE-N01" / "README.md"
claim_p = ROOT / "registry" / "CLM-169.md"
dec_p = ROOT / "registry" / "DEC-179.md"

ALLOWED = {
    "PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE",
    "PARTIAL_US_BRIDGE_N01_INTERVAL_DESIGN_READY_MATCH_SUPPORT_PENDING",
    "HOLD_US_BRIDGE_N01_DESIGN_NOT_IDENTIFIABLE",
}
status = status_p.read_text(encoding="utf-8")
assert "active_issue: 131" in status
assert "active_research: US-BRIDGE-N01" in status
assert "last_decision: DEC-178" in status
r = json.loads(result_json_p.read_text(encoding="utf-8"))
p = json.loads(pair_manifest_p.read_text(encoding="utf-8"))
assert r["research_id"] == "US-BRIDGE-N01" and r["issue"] == 131
assert r["gate"] in ALLOWED
assert r["condition_rating_values_opened"] is False
assert r["condition_rating_row_bytes_sliced"] is False
assert r["relationship_computed"] is False
assert r["fuzzy_repair_used"] is False
assert r["outcome_dependent_inclusion_used"] is False
assert r["raw_source_bytes_persisted"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert p["pair_count"] == r["matched_pairs"]
assert p["pair_identity_sha256"] == r["pair_identity_sha256"]
assert not claim_p.exists() and not dec_p.exists()

gate = r["gate"]
pass_gate = gate == "PASS_US_BRIDGE_N01_MATCHED_INTERVAL_DESIGN_IDENTIFIABLE"
partial_gate = gate == "PARTIAL_US_BRIDGE_N01_INTERVAL_DESIGN_READY_MATCH_SUPPORT_PENDING"
if pass_gate:
    next_action = "Open a separate US-BRIDGE-E01 authorization that reproduces the exact N01 pair fingerprint before opening condition values; then execute only the prospectively frozen deterioration/McNemar contract."
    state_name = "US_BRIDGE_N01_PASS__E01_AUTHORIZATION_REQUIRED"
elif partial_gate:
    next_action = "Return to Stage 0 or open only a new prospectively bounded matching-support investigation; do not change N01 rules or open condition values."
    state_name = "US_BRIDGE_N01_PARTIAL__NO_E01_AUTHORIZATION"
else:
    next_action = "Return to Stage 0 independent-candidate comparison; do not rescue US-BRIDGE-N01 post hoc and do not open condition values."
    state_name = "US_BRIDGE_N01_HOLD__PORTFOLIO_RETURN"

classes = r.get("matched_class_counts", {})
result_md_p.write_text(f"""---
id: US-BRIDGE-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-14
issue: 131
gate: {gate}
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-N01 Result / 결과

**`{gate}`**

## Frozen design support / 고정 설계 지원

- Unique bridges with >=1 eligible consecutive interval: **{r['unique_bridges_with_eligible_interval']:,}**.
- Unique exposed bridges under FEMA `DR` physical-hazard timing: **{r['unique_exposed_bridges']:,}**.
- Unique control-candidate bridges with no exposed eligible interval: **{r['unique_control_candidate_bridges']:,}**.
- Deterministic matched exposed-control pairs: **{r['matched_pairs']:,}**.
- Matched state/territory FIPS: **{r['matched_state_fips_count']}**.
- Matched `CULVERT` pairs: **{classes.get('CULVERT', 0):,}**.
- Matched `NON_CULVERT` pairs: **{classes.get('NON_CULVERT', 0):,}**.
- Matched pairs with interval-length difference <=365 days: **{r['pairs_interval_diff_le_365_rate']:.4%}**.
- Exact pair-identity fingerprint: `{r['pair_identity_sha256']}`.
- Pair identities: `{p['pair_file']}` using canonical JSONL compressed after fingerprinting.

## Outcome-blind integrity / 결과 비개봉 무결성

Condition Items 58/59/60/62 were not opened and their fixed-width row bytes were not sliced. No bridge-condition deterioration indicator, rate, change, p-value or disaster-linked relationship was calculated. Matching used only the preregistered bridge/county/date/class/reconstruction/cadence design fields and FEMA `DR` event identity. No fuzzy repair or outcome-dependent inclusion was used. Raw source bytes remained transient.

## Interpretation boundary / 해석 경계

This result establishes only whether the preregistered temporal exposed/control design is identifiable. It is not evidence that disasters worsen or improve bridge condition. Static hazard mapping and generic NBI deterioration prediction remain outside any novelty claim.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "## Terminal N01 result / N01 최종 결과" not in readme:
    readme += f"\n\n## Terminal N01 result / N01 최종 결과\n\n**`{gate}`** — see `RESULT.md`. Exact pair fingerprint: `{r['pair_identity_sha256']}`. Condition Items 58/59/60/62 remained unopened.\n"
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-169
type: claim
created: 2026-09-14
issue: 131
status: active
---

# CLM-169 — US-BRIDGE-N01 terminal outcome-blind design result

Run `{RUN}` terminates US-BRIDGE-N01 at **`{gate}`** with **{r['matched_pairs']:,}** deterministic matched exposed-control bridge pairs across **{r['matched_state_fips_count']}** state/territory FIPS (`CULVERT={classes.get('CULVERT',0):,}`, `NON_CULVERT={classes.get('NON_CULVERT',0):,}`). Exact pair fingerprint: `{r['pair_identity_sha256']}`.

This is design-identifiability evidence only. Condition Items 58/59/60/62 and their row bytes remained unopened, no bridge-condition relationship was computed, and cost remained **0 USD**.
""", encoding="utf-8")

dec_p.write_text(f"""---
id: DEC-179
type: decision
created: 2026-09-14
issue: 131
status: accepted
---

# DEC-179 — Finalize US-BRIDGE-N01 at {gate}

Finalize Issue #131 / US-BRIDGE-N01 at **`{gate}`** using outcome-blind Run `{RUN}` and exact pair fingerprint `{r['pair_identity_sha256']}`.

No N01 source/window/exposure/matching/threshold change is authorized after execution. Condition Items 58/59/60/62 remain closed unless a separate E01 is authorized after a PASS. A negative later E01 estimate may not be reversed into a protective-effect claim.

Exact next action: {next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-169`" not in claim_log
claim_log += f"\n\n| `CLM-169` | US-BRIDGE-N01 terminates at `{gate}` with {r['matched_pairs']:,} outcome-blind deterministic matched pairs and fingerprint `{r['pair_identity_sha256']}`. / 결과 비개봉 매칭 설계 종결. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_DESIGN_GATE` | Run `{RUN}`; `research/US-BRIDGE-N01/DESIGN_RESULT.json`; `PAIR_MANIFEST.json`; `RESULT.md` | 2026-09-14 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-179`" not in dec_log
dec_log += f"\n| `DEC-179` | 2026-09-14 | Finalize US-BRIDGE-N01 at `{gate}` and preserve exact pair fingerprint; no post-execution rescue. / N01 최종 판정 및 pair fingerprint 고정. | Frozen outcome-blind design Run `{RUN}`; condition values remain closed. | Issue #131; `CLM-169`; `research/US-BRIDGE-N01/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260914-US-BRIDGE-N01-TERMINAL"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 131
last_completed_research: US-BRIDGE-N01
last_decision: DEC-179
updated: 2026-09-14
---
"""
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `{state_name}`

US-BRIDGE-N01 / Issue #131 is terminal at **`{gate}`**. Exact matched-pair identity fingerprint: `{r['pair_identity_sha256']}`.

Condition Items 58/59/60/62 remained unopened and no disaster-linked bridge-condition relationship was computed.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

US-BRIDGE-N01 / Issue #131 is terminal at **`{gate}`** under Run `{RUN}`.

Outcome-blind design support: {r['unique_bridges_with_eligible_interval']:,} bridges with eligible intervals; {r['unique_exposed_bridges']:,} exposed bridges; {r['unique_control_candidate_bridges']:,} control-candidate bridges; {r['matched_pairs']:,} deterministic matched pairs across {r['matched_state_fips_count']} states/territories. Pair fingerprint `{r['pair_identity_sha256']}`.

Condition Items 58/59/60/62 remained unopened; no relationship statistic was computed.

Exact restart: {next_action} Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 131,
    "last_completed_research": "US-BRIDGE-N01",
    "last_decision": "DEC-179",
    "updated": "2026-09-14"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"gate": gate, "pair_count": r["matched_pairs"], "pair_sha256": r["pair_identity_sha256"], "next_action": next_action}, ensure_ascii=False))
