#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = 35006086876
ISSUE = 135
GATE = "HOLD_US_MINE_N01_SOURCE_OR_DESIGN_SUPPORT"
PAIR_SHA = "e2fde0b16457f0b50397b638c96a363a9a0dcca6d4c9ccd49cba5d744f9ba116"

status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
staging_p = ROOT / "research" / "US-MINE-N01" / "STAGING_RESULT.json"
audit_p = ROOT / "research" / "US-MINE-N01" / "STAGING_SOURCE_AUDIT.json"
readme_p = ROOT / "research" / "US-MINE-N01" / "README.md"
result_json_p = ROOT / "research" / "US-MINE-N01" / "RESULT.json"
result_md_p = ROOT / "research" / "US-MINE-N01" / "RESULT.md"
claim_p = ROOT / "registry" / "CLM-173.md"
dec_p = ROOT / "registry" / "DEC-186.md"
pair_p = ROOT / "research" / "US-MINE-N01" / "PAIR_IDENTITIES.jsonl.gz"

c = json.loads(checkpoint_p.read_text(encoding="utf-8"))
assert c["active_issue"] == ISSUE
assert c["active_research"] == "US-MINE-N01"
assert c["last_completed_issue"] == 134
assert c["last_completed_research"] == "US-MINE-F01"
assert c["last_decision"] == "DEC-185"
assert "US_MINE_N01_ACTIVE__OUTCOME_BLIND_HOURS_RAMP_DESIGN" in status_p.read_text(encoding="utf-8")
assert not claim_p.exists() and not dec_p.exists()
assert pair_p.exists()

r = json.loads(staging_p.read_text(encoding="utf-8"))
a = json.loads(audit_p.read_text(encoding="utf-8"))
assert r["research_id"] == "US-MINE-N01" and r["issue"] == ISSUE
assert r["gate"] == GATE
assert r["source_hash_match_f01"] is True
assert r["accident_source_read"] is False
assert r["injury_outcome_values_opened"] is False
assert r["production_magnitude_parsed"] is False
assert r["relationship_computed"] is False
assert r["post_execution_rescue_used"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert a["accident_source_read"] is False
assert a["injury_outcome_values_opened"] is False
assert a["production_magnitude_parsed"] is False
assert a["raw_source_bytes_persisted"] is False
assert a["pair_identity_sha256"] == PAIR_SHA
assert r["matching"]["pair_identity_sha256"] == PAIR_SHA
assert r["matching"]["pairs"] == 2084
assert r["matching"]["pairs_by_sector"] == {"C": 214, "M": 1870}
assert r["matching"]["states"] == 49
assert r["structural_diagnostics"]["eligible_mines"] == 15179
assert r["structural_diagnostics"]["sector_mine_mismatches"] == 60
assert r["requirements"]["coal_pairs_ge_300"] is False
assert r["requirements"]["sector_matches_mines"] is False
failed = sorted(k for k, v in r["requirements"].items() if not v)
assert failed == ["coal_pairs_ge_300", "sector_matches_mines"]

canonical = dict(r)
canonical["workflow_run"] = RUN
canonical["canonical_finalized"] = True
canonical["failed_requirements"] = failed
canonical["scientific_contract_changed_after_execution"] = False
result_json_p.write_text(json.dumps(canonical, indent=2, sort_keys=True) + "\n", encoding="utf-8")

m = r["matching"]
s = r["structural_diagnostics"]
cs = r["candidate_support"]["counts_by_sector_role"]
result_md_p.write_text(f"""---
id: US-MINE-N01-RESULT
type: outcome-blind-design-identifiability
created: 2026-09-16
issue: {ISSUE}
workflow_run: {RUN}
gate: {GATE}
pair_identity_sha256: {PAIR_SHA}
incremental_monetary_cost_usd: 0
---

# US-MINE-N01 Result / 결과

**`{GATE}`**

## Frozen design execution / 고정 설계 실행

The preregistered `ALL_SECTOR_OPERATOR_HOURS_RAMP_UP` design executed without opening the Accidents source or any injury outcome. F01 Mines and quarterly-employment source hashes reproduced exactly before exposure magnitudes were used.

사전등록한 `ALL_SECTOR_OPERATOR_HOURS_RAMP_UP` 설계를 사고 데이터·부상 outcome을 열지 않은 상태에서 실행했다. Exposure magnitude 사용 전 F01 Mines 및 quarterly-employment source hash가 정확히 재현됐다.

## Outcome-blind integrity / 결과 비개봉 무결성

- Accidents source read: **NO**.
- Injury outcome values opened: **NO**.
- Coal-production magnitude parsed: **NO**.
- Exposure→injury relationship computed: **NO**.
- Post-execution threshold/matching rescue: **NO**.
- Incremental monetary cost: **0 USD**.

## Exposure-only support / exposure-only 지원

- Eligible mines with >=1 positive-hours `(t-1,t,t+1)` sequence: **{s['eligible_mines']:,}**.
- Eligible three-quarter observations: **{s['eligible_three_quarter_observations']:,}**.
- First-role Coal candidates: exposed **{cs['C_EXPOSED']:,}**, control **{cs['C_CONTROL']:,}**.
- First-role Metal/Nonmetal candidates: exposed **{cs['M_EXPOSED']:,}**, control **{cs['M_CONTROL']:,}**.
- Deterministic 1:1 pairs: **{m['pairs']:,}**.
- Pair coverage: Coal **{m['pairs_by_sector']['C']:,}**, Metal/Nonmetal **{m['pairs_by_sector']['M']:,}**, **{m['states']} states**.
- Pair identity fingerprint: `{PAIR_SHA}`.

## Why the frozen gate is HOLD / HOLD 이유

Two preregistered requirements failed:

1. `coal_pairs_ge_300` — only **214** Coal pairs were identified against the frozen minimum of **300**.
2. `sector_matches_mines` — **60** mine-quarter records had a historical quarterly-employment sector that did not equal the current Mines-snapshot sector identity under the strict frozen comparison.

All other frozen requirements passed, including >=2,000 total pairs and >=30-state coverage. Nevertheless the contract is conjunctive: these two failures prevent PASS or E01 authorization.

사후에 Coal 최소쌍 기준을 낮추거나, 60개 mismatch를 결과를 본 뒤 새 규칙으로 재분류하지 않는다. Doing either would be a post-support rescue.

## Interpretation boundary / 해석 경계

This HOLD does **not** show that operator-hours ramp-up is unrelated to mine injuries. Injury outcomes were never opened. It means only that the exact N01 design, as preregistered, failed its own support/identity gate.

No positive, negative, protective, sector-specific or causal injury claim is authorized.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Do not open US-MINE-E01 from this N01 and do not rescue the branch by lowering the Coal-pair threshold or rewriting sector identity after support was observed. A future independent design may revisit historical sector semantics only as a separately selected, prospectively registered mission.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
if "## Terminal N01 result / N01 최종 결과" not in readme:
    readme += f"""\n\n## Terminal N01 result / N01 최종 결과\n\n**`{GATE}`** — Run `{RUN}`. Exposure-only design produced **{m['pairs']:,}** pairs across **{m['states']} states**, but failed frozen `coal_pairs_ge_300` (**214**) and strict `sector_matches_mines` (**60 mismatches**) requirements. Accidents/injury outcomes remained unopened and no relationship was computed. No rescue is permitted. See `RESULT.md`.\n"""
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-173
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_DESIGN_GATE
status: active
---

# CLM-173 — US-MINE-N01 frozen hours-ramp design HOLD

Run `{RUN}` executed the preregistered all-sector operator-hours ramp-up design without reading the Accidents source or any injury outcome. It identified **{m['pairs']:,}** deterministic pairs across **{m['states']} states**, but only **214** Coal pairs versus the frozen **300** minimum and **60** strict current-Mines-vs-historical-quarterly sector mismatches. Therefore the exact frozen N01 contract terminates at **`{GATE}`**.

This is a design-support/identity HOLD, not evidence for or against an injury relationship.
""", encoding="utf-8")

dec_p.write_text(f"""---
id: DEC-186
type: decision
created: 2026-09-16
issue: {ISSUE}
status: accepted
---

# DEC-186 — Finalize US-MINE-N01 at HOLD and return to portfolio control

Finalize Issue #{ISSUE} / US-MINE-N01 at **`{GATE}`** from frozen-contract Run `{RUN}`.

Do not lower the Coal-pair floor, reinterpret the 60 sector mismatches, change geography/time matching, or open injury outcomes to rescue the design. No US-MINE-E01 is authorized from this N01.

Return to Stage 0 independent-candidate comparison. A future historical-sector-semantics design would require independent portfolio selection and prospective preregistration before any outcome access.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_log = claim_log_p.read_text(encoding="utf-8")
assert "`CLM-173`" not in claim_log
claim_log += f"\n\n| `CLM-173` | US-MINE-N01 executed outcome-blind and identified {m['pairs']:,} frozen hours-ramp pairs across {m['states']} states, but the preregistered design is HOLD because Coal contributed 214 pairs (<300) and strict current-Mines-vs-historical-quarterly sector identity had 60 mismatches; injury outcomes were never opened. / US-MINE-N01 결과 비개봉 설계 HOLD. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_DESIGN_GATE` | Run `{RUN}`; `research/US-MINE-N01/RESULT.json`; `RESULT.md` | 2026-09-16 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
assert "`DEC-186`" not in dec_log
dec_log += f"\n| `DEC-186` | 2026-09-16 | Finalize US-MINE-N01 at `{GATE}`; no threshold/sector-identity rescue and no E01 authorization; return to Stage 0 portfolio control. / N01 HOLD 종결·구제 금지·포트폴리오 복귀. | Frozen Run `{RUN}` failed exactly two preregistered requirements: Coal pairs 214<300 and 60 strict sector mismatches; outcomes remained closed. | Issue #135; `CLM-173`; `research/US-MINE-N01/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

checkpoint_id = "CHK-20260916-US-MINE-N01-TERMINAL"
front = f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-MINE-N01
last_decision: DEC-186
updated: 2026-09-16
---
"""
next_action = (
    "Return to Stage 0 and open the next independent portfolio comparison. Do not open US-MINE-E01 or rescue N01 by changing the frozen Coal-pair floor, sector identity rule, matching, or thresholds after support was observed."
)
status_p.write_text(front + f"""
# Project Status / 프로젝트 상태

**State / 상태:** `US_MINE_N01_HOLD__PORTFOLIO_RETURN`

US-MINE-N01 / Issue #{ISSUE} is terminal at **`{GATE}`** from frozen-contract Run `{RUN}`.

Exposure-only evidence: **{s['eligible_mines']:,}** eligible mines; **{m['pairs']:,}** deterministic pairs across **{m['states']} states**; Coal **214** pairs and Metal/Nonmetal **1,870**. Frozen failures: Coal pair minimum **214 < 300** and **60** strict sector-identity mismatches. Accident/injury outcomes remained closed and no relationship was computed.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(front + f"""
# Session Handoff / 세션 인수인계

US-MINE-N01 / Issue #{ISSUE} is terminal at **`{GATE}`** from Run `{RUN}`. The exact outcome-blind design produced **{m['pairs']:,}** pairs across **{m['states']} states**, but the preregistered Coal minimum failed at **214 < 300** and strict current-Mines-vs-historical-quarterly sector identity showed **60 mismatches**. No outcome was opened, and no threshold/matching rescue was used.

Exact restart: {next_action}

Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": ISSUE,
    "last_completed_research": "US-MINE-N01",
    "last_decision": "DEC-186",
    "updated": "2026-09-16"
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "state": "US_MINE_N01_HOLD__PORTFOLIO_RETURN",
    "issue": ISSUE,
    "gate": GATE,
    "pairs": m["pairs"],
    "coal_pairs": m["pairs_by_sector"]["C"],
    "sector_mine_mismatches": s["sector_mine_mismatches"],
    "last_decision": "DEC-186",
    "injury_outcomes_opened": False,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False))
