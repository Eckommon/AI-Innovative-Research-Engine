#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = 35003865979
SUPERSEDED_RUN = 35003705306
ISSUE = 134
GATE = "PASS_US_MINE_F01_STRUCTURAL_JOIN_READY__PRODUCTION_SCOPE_RESTRICTED"

status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
staging_p = ROOT / "research" / "US-MINE-F01" / "STAGING_RESULT.json"
audit_p = ROOT / "research" / "US-MINE-F01" / "STAGING_SOURCE_AUDIT.json"
readme_p = ROOT / "research" / "US-MINE-F01" / "README.md"
result_json_p = ROOT / "research" / "US-MINE-F01" / "RESULT.json"
result_md_p = ROOT / "research" / "US-MINE-F01" / "RESULT.md"
claim_p = ROOT / "registry" / "CLM-172.md"
dec_p = ROOT / "registry" / "DEC-184.md"
superseded_p = ROOT / "research" / "US-MINE-F01" / "SUPERSEDED_RUN_35003705306.md"

# Canonical active-state precondition.
c = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert c["active_issue"] == ISSUE
assert c["active_research"] == "US-MINE-F01"
assert c["last_completed_issue"] == 133
assert c["last_completed_research"] == "PORTFOLIO-R27"
assert c["last_decision"] == "DEC-183"
assert "US_MINE_F01_ACTIVE__OUTCOME_BLIND_STRUCTURAL_FEASIBILITY" in status_p.read_text(encoding="utf-8")
assert not claim_p.exists() and not dec_p.exists()
assert superseded_p.exists()

r = json.loads(staging_p.read_text(encoding="utf-8"))
a = json.loads(audit_p.read_text(encoding="utf-8"))
assert r["research_id"] == "US-MINE-F01" and r["issue"] == ISSUE
assert r["gate"] == GATE
assert r["support_window"] == {"start_year": 2019, "end_year": 2025}
assert all(r["requirements"].values())
assert r["production_scope_restricted"] is True
assert r["injury_outcome_values_opened"] is False
assert r["prohibited_outcome_fields_accessed"] is False
assert r["relationship_computed"] is False
assert r["post_execution_rescue_used"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert a["forbidden_fields_selected"] == []
assert a["injury_outcome_values_opened"] is False
assert a["relationship_computed"] is False
assert a["raw_source_bytes_persisted"] is False
assert a["incremental_monetary_cost_usd"] == 0
assert a["source_manifest"] == r["source_manifest"]

m = r["mine_identity"]
e = r["employment_structural_support"]
x = r["accident_structural_support"]
assert m["distinct_mine_ids"] == 92007
assert m["duplicate_mine_id_rows"] == 0 and m["conflicting_mine_ids"] == 0
assert e["distinct_keys"] == 663020
assert e["conflicting_duplicate_keys"] == 0
assert e["mines_with_ge_2_distinct_quarters"] == 17060
assert e["hours_worked_magnitude_parsed"] is False
assert e["coal_production_magnitude_parsed"] is False
assert x["distinct_operator_mine_quarter_subunit_keys"] == 21491
assert x["exact_employment_overlap_keys"] == 21426
assert x["exact_employment_overlap_rate"] > 0.9969
assert x["overlapping_states"] == 53

canonical = dict(r)
canonical["workflow_run"] = RUN
canonical["superseded_implementation_run"] = SUPERSEDED_RUN
canonical["canonical_finalized"] = True
canonical["scientific_contract_changed_after_execution"] = False
result_json_p.write_text(json.dumps(canonical, indent=2, sort_keys=True) + "\n", encoding="utf-8")

overlap_pct = x["exact_employment_overlap_rate"] * 100
result_md_p.write_text(f"""---
id: US-MINE-F01-RESULT
type: outcome-blind-structural-feasibility
created: 2026-09-16
issue: {ISSUE}
workflow_run: {RUN}
superseded_implementation_run: {SUPERSEDED_RUN}
gate: {GATE}
incremental_monetary_cost_usd: 0
---

# US-MINE-F01 Result / 결과

**`{GATE}`**

## Outcome-blind integrity / 결과 비개봉 무결성

- Frozen support window: **2019–2025**.
- Injury outcome values opened: **NO**.
- Prohibited accident outcome fields selected/accessed: **NO**.
- Exposure→injury relationship computed: **NO**.
- Hours-worked magnitude parsed: **NO**.
- Coal-production magnitude parsed: **NO**.
- Raw source bytes persisted: **NO**.
- Post-execution threshold/source/window rescue: **NO**.
- Incremental monetary cost: **0 USD**.

## Frozen structural result / 고정 구조 결과

- Mines snapshot: **{m['distinct_mine_ids']:,}** distinct `MINE_ID`; duplicate/conflicting IDs **0 / 0**.
- 2019–2025 operator employment: **{e['distinct_keys']:,}** exact `(MINE_ID, CAL_YR, CAL_QTR, SUBUNIT_CD)` keys; conflicting duplicates **0**.
- Mines with >=2 distinct quarters: **{e['mines_with_ge_2_distinct_quarters']:,}**.
- `HOURS_WORKED` nonblank support: Coal **{e['hours_worked_nonblank_rate_by_sector']['C']:.6%}**, Metal/Nonmetal **{e['hours_worked_nonblank_rate_by_sector']['M']:.6%}**.
- Operator-attributed accident structural keys: **{x['distinct_operator_mine_quarter_subunit_keys']:,}**.
- Exact employment-key overlap: **{x['exact_employment_overlap_keys']:,} / {x['distinct_operator_mine_quarter_subunit_keys']:,} = {overlap_pct:.4f}%**.
- Overlapping mine IDs: **{x['overlapping_mine_ids']:,}** across **{x['overlapping_states']} states**.
- Duplicate accident `DOCUMENT_NO`: **{x['duplicate_document_ids']}**.

## Production-scope boundary / 생산량 범위 경계

PASS does **not** establish a nationally comparable Coal+Metal/Nonmetal production-pressure exposure. The preregistered MSHA semantic restriction remains binding: Metal/Nonmetal operators are not required to report production. The observed nonblank support does not override that reporting-rule asymmetry. `PRODUCTION_SCOPE_RESTRICTED` is therefore part of the PASS state.

## Superseded implementation run / 대체된 구현 실행

Run `{SUPERSEDED_RUN}` is preserved as an implementation nonconformity. It produced the same substantive source/support evidence but mislabeled the gate as PARTIAL because two correctly false diagnostics (`prohibited_outcome_fields_accessed=false`, `relationship_computed=false`) were passed into `all()`. Run `{RUN}` changed only those predicates to positive compliance form and re-executed the **same preregistered contract** with exact source-manifest stability. No scientific threshold, source, window or identity rule changed.

## Interpretation boundary / 해석 경계

This PASS establishes only deterministic source/schema/time/key structural readiness. It does **not** show that operational stress predicts or causes mine injuries and does not authorize any injury-rate, injury-severity or exposure-effect claim.

## Exact next action / 정확한 다음 행동

Open only a separately preregistered **US-MINE-N01 outcome-blind design gate**. N01 must choose exactly one exposure family from source semantics/support before any injury outcome is opened, while preserving `PRODUCTION_SCOPE_RESTRICTED`. Do not auto-select coal-only production or all-sector employee-hours from accident outcomes.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "## Terminal F01 result / F01 최종 결과" not in readme:
    readme += f"""\n\n## Terminal F01 result / F01 최종 결과\n\n**`{GATE}`** — corrected frozen-contract Run `{RUN}`. Superseded Run `{SUPERSEDED_RUN}` is retained as a boolean-polarity implementation nonconformity, not a scientific failure. Exact employment overlap: **{x['exact_employment_overlap_keys']:,}/{x['distinct_operator_mine_quarter_subunit_keys']:,} ({overlap_pct:.4f}%)** across **{x['overlapping_states']} states**. Injury outcome values remained unopened and no relationship was computed. See `RESULT.md`.\n"""
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-172
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_STRUCTURAL_GATE
status: active
---

# CLM-172 — US-MINE-F01 structural feasibility PASS

Corrected frozen-contract Run `{RUN}` terminates US-MINE-F01 at **`{GATE}`**. The 2019–2025 MSHA operator-employment structure contains **{e['distinct_keys']:,}** exact mine-quarter-subunit keys and **{e['mines_with_ge_2_distinct_quarters']:,}** mines with at least two quarters. Of **{x['distinct_operator_mine_quarter_subunit_keys']:,}** operator-attributed accident structural keys, **{x['exact_employment_overlap_keys']:,} ({overlap_pct:.4f}%)** exactly match an employment key; overlapping mines span **{x['overlapping_states']} states**.

No injury outcome value or prohibited accident outcome field was opened, no hours/production magnitude was parsed, and no exposure→injury relationship was computed. `PRODUCTION_SCOPE_RESTRICTED` remains mandatory because MSHA reporting semantics do not require Metal/Nonmetal production reporting.

Run `{SUPERSEDED_RUN}` is retained as a superseded boolean-polarity implementation nonconformity; the corrected run changed no scientific threshold/source/window/identity rule.
""", encoding="utf-8")

dec_p.write_text(f"""---
id: DEC-184
type: decision
created: 2026-09-16
issue: {ISSUE}
status: accepted
---

# DEC-184 — Finalize US-MINE-F01 at structural PASS with production-scope restriction

Finalize Issue #{ISSUE} / US-MINE-F01 at **`{GATE}`** using corrected frozen-contract Run `{RUN}`. Preserve Run `{SUPERSEDED_RUN}` as an implementation-polarity nonconformity only; no scientific contract was changed during correction.

F01 establishes deterministic source/schema/time/key readiness but does not establish an injury relationship. `PRODUCTION_SCOPE_RESTRICTED` remains binding: a national Coal+Metal/Nonmetal production-pressure exposure is not authorized from F01.

Exact next action: open only a separately preregistered US-MINE-N01 outcome-blind design gate that chooses exactly one exposure family from source semantics/support before any injury outcome is opened. Do not select the exposure using accident outcomes and do not open an injury relationship test from F01.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-172`" not in claim_log
claim_log += f"\n\n| `CLM-172` | US-MINE-F01 passes the frozen outcome-blind structural gate: {e['distinct_keys']:,} exact employment keys, {e['mines_with_ge_2_distinct_quarters']:,} repeat-support mines, {x['exact_employment_overlap_keys']:,}/{x['distinct_operator_mine_quarter_subunit_keys']:,} ({overlap_pct:.4f}%) exact operator-accident structural overlap across {x['overlapping_states']} states; injury outcomes remain closed and production scope remains restricted. / US-MINE-F01 구조 feasibility PASS. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_STRUCTURAL_GATE` | Run `{RUN}`; superseded Run `{SUPERSEDED_RUN}`; `research/US-MINE-F01/RESULT.json`; `RESULT.md` | 2026-09-16 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-184`" not in dec_log
dec_log += f"\n| `DEC-184` | 2026-09-16 | Finalize US-MINE-F01 at `{GATE}`; preserve production-scope restriction and require separate outcome-blind N01 before injury access. / F01 구조 PASS 종결·생산범위 제한 보존·N01 별도 승인 요구. | Corrected Run `{RUN}` preserves the frozen contract and exact source manifest; Run `{SUPERSEDED_RUN}` was implementation-polarity only. | Issue #134; `CLM-172`; `research/US-MINE-F01/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-US-MINE-F01-TERMINAL"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-MINE-F01
last_decision: DEC-184
updated: 2026-09-16
---
"""
next_action = (
    "Open only a separately preregistered US-MINE-N01 outcome-blind design gate. Choose exactly one exposure family from source semantics/support before any injury outcome access, preserve PRODUCTION_SCOPE_RESTRICTED, and do not choose exposure using accident outcomes."
)
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `US_MINE_F01_PASS__N01_AUTHORIZATION_REQUIRED`

US-MINE-F01 / Issue #{ISSUE} is terminal at **`{GATE}`** under corrected frozen-contract Run `{RUN}`. Run `{SUPERSEDED_RUN}` is preserved as a superseded boolean-polarity implementation nonconformity only.

Structural evidence: **{e['distinct_keys']:,}** exact employment keys; **{e['mines_with_ge_2_distinct_quarters']:,}** repeat-support mines; **{x['exact_employment_overlap_keys']:,}/{x['distinct_operator_mine_quarter_subunit_keys']:,} ({overlap_pct:.4f}%)** exact operator-accident structural overlap; **{x['overlapping_states']} states**. Injury outcomes remained closed and no exposure relationship was computed.

`PRODUCTION_SCOPE_RESTRICTED` remains binding.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

US-MINE-F01 / Issue #{ISSUE} is terminal at **`{GATE}`** from corrected frozen-contract Run `{RUN}`. Superseded Run `{SUPERSEDED_RUN}` is retained as an implementation-polarity nonconformity; exact source manifest and the scientific contract were unchanged.

F01 established **{e['distinct_keys']:,}** exact 2019–2025 employment keys, **{e['mines_with_ge_2_distinct_quarters']:,}** repeat-support mines, and **{x['exact_employment_overlap_keys']:,}/{x['distinct_operator_mine_quarter_subunit_keys']:,} ({overlap_pct:.4f}%)** exact operator-accident structural key overlap across **{x['overlapping_states']} states**. Injury outcomes and exposure magnitudes remained unopened; no relationship was computed.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": ISSUE,
    "last_completed_research": "US-MINE-F01",
    "last_decision": "DEC-184",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "gate": GATE,
    "workflow_run": RUN,
    "superseded_run": SUPERSEDED_RUN,
    "employment_keys": e["distinct_keys"],
    "repeat_mines": e["mines_with_ge_2_distinct_quarters"],
    "accident_structural_keys": x["distinct_operator_mine_quarter_subunit_keys"],
    "exact_overlap_keys": x["exact_employment_overlap_keys"],
    "overlap_rate": x["exact_employment_overlap_rate"],
    "overlap_states": x["overlapping_states"],
    "injury_outcomes_opened": False,
    "relationship_computed": False,
    "next_action": next_action,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
