#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RID = "US-BRIDGE-F01"
ISSUE = 127
RUN = 34791209726
ALLOWED = {
    "PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY",
    "PARTIAL_US_BRIDGE_F01_PANEL_READY_INSPECTION_IDENTITY_PENDING",
    "HOLD_US_BRIDGE_F01_SOURCE_OR_IDENTITY_SUPPORT",
}

status_p = ROOT / "STATUS.md"
handoff_p = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_p = ROOT / "context" / "checkpoint.json"
claim_log_p = ROOT / "registry" / "CLAIM_LEDGER.md"
dec_log_p = ROOT / "registry" / "DECISION_LOG.md"
result_json_p = ROOT / "research" / RID / "EXECUTION_RESULT.json"
result_md_p = ROOT / "research" / RID / "RESULT.md"
readme_p = ROOT / "research" / RID / "README.md"
note_p = ROOT / "research" / RID / "IMPLEMENTATION_NOTE.md"
claim_p = ROOT / "registry" / "CLM-168.md"
dec_p = ROOT / "registry" / "DEC-177.md"

status = status_p.read_text(encoding="utf-8")
assert "active_issue: 127" in status
assert "active_research: US-BRIDGE-F01" in status
assert note_p.exists()
r = json.loads(result_json_p.read_text(encoding="utf-8"))
assert r["research_id"] == RID and r["issue"] == ISSUE
assert r["gate"] in ALLOWED
assert r["condition_rating_values_opened"] is False
assert r["condition_rating_row_bytes_sliced"] is False
assert r["relationship_computed"] is False
assert r["fuzzy_repair_used"] is False
assert r["raw_source_bytes_persisted"] is False
assert r["incremental_monetary_cost_usd"] == 0
assert r["duplicate_key_fail_closed_at_key_year_level"] is True
assert r["supersedes_technical_run"] == 34790222911
assert not claim_p.exists() and not dec_p.exists()

gate = r["gate"]
pass_gate = gate == "PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY"
partial_gate = gate == "PARTIAL_US_BRIDGE_F01_PANEL_READY_INSPECTION_IDENTITY_PENDING"
if pass_gate:
    disposition = "The frozen outcome-blind source/identity/time gate is satisfied. This authorizes only a separate N01 design-identifiability gate; it does not authorize opening bridge condition-rating values or computing a disaster-linked condition relationship."
    next_action = "Open a separately preregistered US-BRIDGE-N01 design-identifiability gate before any bridge condition-rating value is opened."
elif partial_gate:
    disposition = "The panel/source route is supported but the frozen inspection-identity threshold is not fully satisfied. No relationship test is authorized."
    next_action = "Return to Stage 0 or open only a separately preregistered identity-resolution gate; do not open bridge condition-rating values."
else:
    disposition = "The frozen source/identity support requirements are not satisfied. No relationship test is authorized and this F01 must not be rescued by changing the frozen source/window/thresholds."
    next_action = "Return to Stage 0 independent-candidate comparison; do not rescue US-BRIDGE-F01 post hoc."

result_md_p.write_text(f"""---
id: US-BRIDGE-F01-RESULT
type: outcome-blind-feasibility
created: 2026-09-14
issue: 127
gate: {gate}
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-F01 Result

**`{gate}`**

{disposition}

## Frozen support result

- Official NBI annual sources processed: **{r['annual_sources']}** (2015–2025).
- Canonical bridge identities present in >=6/11 archives: **{r['canonical_bridges_ge_6_of_11']:,}**.
- Repeated-support bridges with >=2 distinct parseable inspection dates: **{r['repeated_bridges_ge_2_distinct_inspection_dates']:,}**.
- County-qualified repeated-support bridges: **{r['county_qualified_repeated_bridges']:,}** (**{r['county_qualification_rate']:.4%}**).
- Repeated-support state/territory FIPS: **{r['repeated_support_state_fips_count']}**.
- Qualified NBI counties: **{r['qualified_nbi_counties']:,}**.
- FEMA-overlap states/territories: **{r['fema_overlap_state_fips_count']}**.
- FEMA-overlap counties: **{r['fema_overlap_counties']:,}**.
- Duplicate canonical key rows observed: **{r['duplicate_canonical_key_rows_seen']}**; ambiguous canonical key-years excluded: **{r['duplicate_canonical_keys_excluded']}**.
- All annual fixed-width identity/schema checks supported: **{r['all_years_schema_supported']}**.

## Implementation-integrity record

Run `34790222911` is preserved as a superseded implementation-nonconformity run. It discarded an entire annual source when any duplicate bridge key existed, despite only 1–4 duplicate keys among roughly 612k–624k rows per year. Before the corrected rerun, Issue #127 and `IMPLEMENTATION_NOTE.md` recorded the correction: duplicate ambiguity fails closed at the canonical key-year level, while unrelated unique keys in the same official annual source remain eligible.

The corrected Run `{RUN}` changes no source, time window, threshold, FEMA hazard set, outcome definition, or gate. It is an identity-scope correction only.

## Outcome-blind boundary

Bridge condition-rating values were **not opened**. Legacy condition-item row bytes were **not sliced**. No disaster-linked bridge-condition rate/change/association was computed. No fuzzy repair was used. Raw source bytes remained transient. Therefore this result is a feasibility/identity finding only, not an infrastructure-condition effect finding.

## Next action

{next_action}

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

readme = readme_p.read_text(encoding="utf-8")
marker = "## Terminal F01 result / F01 최종 결과"
if marker not in readme:
    readme += f"\n\n{marker}\n\n**`{gate}`** — see `RESULT.md`. Run `{RUN}` is the corrected outcome-blind terminal F01 execution; Run `34790222911` is retained as a superseded implementation-nonconformity run. Bridge condition-rating values remained unopened.\n"
readme_p.write_text(readme, encoding="utf-8")

claim_p.write_text(f"""---
id: CLM-168
type: claim
created: 2026-09-14
issue: 127
status: active
---

# CLM-168 — US-BRIDGE-F01 terminal outcome-blind feasibility result

Corrected outcome-blind Run `{RUN}` terminates US-BRIDGE-F01 at **`{gate}`**. It identifies **{r['canonical_bridges_ge_6_of_11']:,}** canonical bridges present in at least 6/11 annual archives, **{r['repeated_bridges_ge_2_distinct_inspection_dates']:,}** with at least two distinct inspection dates, and FEMA geography overlap across **{r['fema_overlap_state_fips_count']}** state/territory FIPS and **{r['fema_overlap_counties']:,}** counties.

The result is strictly feasibility/identity evidence. Condition-rating values and their fixed-width row bytes were not accessed, and no hazard-linked bridge-condition relationship was computed. Run `34790222911` is superseded only because it applied duplicate fail-closed at whole-year rather than ambiguous key-year scope. Cost: **0 USD**.
""", encoding="utf-8")

dec_p.write_text(f"""---
id: DEC-177
type: decision
created: 2026-09-14
issue: 127
status: accepted
---

# DEC-177 — Finalize US-BRIDGE-F01 at {gate}

Finalize Issue #127 / US-BRIDGE-F01 at **`{gate}`** using corrected outcome-blind Run `{RUN}`. Preserve Run `34790222911` as a superseded implementation-integrity record; do not use its whole-year duplicate discard as the scientific terminal gate.

{next_action}

Do not open bridge condition-rating values except under a separately authorized downstream design/experiment contract. No post-execution changes to the frozen F01 source/window/thresholds are authorized. Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

# Synchronize the previously materialized R26/F01 authorization records into the large ledgers,
# then append the terminal F01 records. This repairs the temporary indexing lag recorded in STATUS.
claim_log = claim_log_p.read_text(encoding="utf-8")
if "`CLM-167`" not in claim_log:
    claim_log += "\n\n| `CLM-167` | PORTFOLIO-R26 selects US-BRIDGE-F01 at 41/45 as the next independent outcome-blind feasibility branch; no condition value opened. / R26에서 US-BRIDGE-F01을 41/45로 선정. | `DERIVED/VALIDATED` | `V2_PRIMARY_VERIFIED` | Issue #126; `research/PORTFOLIO-R26/RESULT.md`; `registry/CLM-167.md` | 2026-09-13 | active |\n"
assert "`CLM-168`" not in claim_log
claim_log += f"\n| `CLM-168` | US-BRIDGE-F01 terminates at `{gate}` under corrected key-year duplicate fail-closed semantics; condition values remain unopened. / 수정된 key-year fail-closed 규칙으로 F01 종결. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_FEASIBILITY_GATE` | Run `{RUN}`; `research/US-BRIDGE-F01/EXECUTION_RESULT.json`; `RESULT.md` | 2026-09-14 | active |\n"
claim_log_p.write_text(claim_log, encoding="utf-8")

dec_log = dec_log_p.read_text(encoding="utf-8")
if "`DEC-175`" not in dec_log:
    dec_log += "\n\n| `DEC-175` | 2026-09-13 | PORTFOLIO-R26 selects US-BRIDGE-F01 at 41/45. / R26에서 US-BRIDGE-F01 선정. | Highest next-gate information gain among preserved independent candidates while retaining overlap penalty. | Issue #126; `CLM-167`; `research/PORTFOLIO-R26/RESULT.md` | active |\n"
if "`DEC-176`" not in dec_log:
    dec_log += "| `DEC-176` | 2026-09-13 | Authorize Issue #127 / US-BRIDGE-F01 outcome-blind feasibility only. / F01 outcome-blind feasibility만 승인. | Prove source/bridge/county/inspection identity without opening condition-rating values. | Issue #127; `research/US-BRIDGE-F01/README.md` | active |\n"
assert "`DEC-177`" not in dec_log
dec_log += f"| `DEC-177` | 2026-09-14 | Finalize US-BRIDGE-F01 at `{gate}` using corrected key-year duplicate fail-closed semantics. / 수정된 key-year 규칙으로 F01 종결. | Run `{RUN}` satisfies outcome-blind integrity; Run `34790222911` is preserved as superseded implementation nonconformity. | Issue #127; `CLM-168`; `research/US-BRIDGE-F01/RESULT.md` | active |\n"
dec_log_p.write_text(dec_log, encoding="utf-8")

state_name = (
    "US_BRIDGE_F01_PASS__N01_DESIGN_GATE_REQUIRED" if pass_gate else
    "US_BRIDGE_F01_PARTIAL__NO_RELATIONSHIP_TEST" if partial_gate else
    "US_BRIDGE_F01_HOLD__PORTFOLIO_RETURN"
)
checkpoint_id = "CHK-20260914-US-BRIDGE-F01-TERMINAL"
status_p.write_text(f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 127
last_completed_research: US-BRIDGE-F01
last_decision: DEC-177
updated: 2026-09-14
---

# Project Status / 프로젝트 상태

**State / 상태:** `{state_name}`

US-BRIDGE-F01 / Issue #127 is terminal at **`{gate}`** under corrected key-year duplicate fail-closed semantics. The corrected execution is Run `{RUN}`; Run `34790222911` remains a superseded implementation-integrity record.

Bridge condition-rating values remained unopened and no disaster-linked condition relationship was computed.

## Exact next action / 정확한 다음 행동

{next_action}

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_p.write_text(f"""---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 127
last_completed_research: US-BRIDGE-F01
last_decision: DEC-177
updated: 2026-09-14
---

# Session Handoff / 세션 인수인계

US-BRIDGE-F01 / Issue #127 is terminal at **`{gate}`**.

Corrected Run `{RUN}` used the frozen FHWA NBI 2015–2025 and FEMA 2015–2024 outcome-blind contract. Support: {r['canonical_bridges_ge_6_of_11']:,} bridge identities in >=6/11 annual archives; {r['repeated_bridges_ge_2_distinct_inspection_dates']:,} with >=2 distinct inspection dates; county qualification {r['county_qualification_rate']:.4%}; FEMA overlap {r['fema_overlap_state_fips_count']} states/territories and {r['fema_overlap_counties']:,} counties.

Run `34790222911` is retained as superseded because it discarded whole annual files when 1–4 duplicate bridge keys existed. The correction was recorded before rerun and excludes only ambiguous duplicate key-years. No threshold/source/window/hazard change occurred.

Condition-rating values were never opened for F01 and no relationship was computed.

Exact restart: {next_action} Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_p.write_text(json.dumps({
    "checkpoint_id": checkpoint_id,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 127,
    "last_completed_research": "US-BRIDGE-F01",
    "last_decision": "DEC-177",
    "updated": "2026-09-14",
    "terminal_gate": gate,
    "execution_run": RUN,
    "superseded_technical_run": 34790222911,
    "incremental_monetary_cost_usd": 0,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"gate": gate, "checkpoint_id": checkpoint_id, "next_action": next_action}, ensure_ascii=False))
