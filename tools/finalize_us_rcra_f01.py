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
claim_path = ROOT / "registry" / "CLM-162.md"
dec_path = ROOT / "registry" / "DEC-168.md"
research = ROOT / "research" / "US-RCRA-F01"
readme_path = research / "README.md"
result_path = research / "RESULT.md"
manifest_path = research / "FEASIBILITY_MANIFEST.json"

status = status_path.read_text(encoding="utf-8")
assert "active_issue: 121" in status
assert "active_research: US-RCRA-F01" in status
assert "last_decision: DEC-167" in status
assert not claim_path.exists() and not dec_path.exists() and not result_path.exists()

m = json.loads(manifest_path.read_text(encoding="utf-8"))
assert m["gate"] == "PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY"
assert m["relationship_computed"] is False
assert m["disaster_linked_compliance_outcomes_opened"] is False
assert m["disaster_linked_violation_or_evaluation_counts_computed"] is False
assert m["raw_source_bytes_persisted"] is False
assert m["incremental_monetary_cost_usd"] == 0

op = m["rcra_operating_tsdf"]
join = m["exact_gis_join"]
fema = m["fema_modern_identity"]
temp = m["rcra_compliance_temporal_identity"]

assert op["unique_ids"] >= 500
assert op["pass_min_500"] is True
assert join["coverage_fraction"] >= 0.80
assert join["pass_80pct"] is True
assert join["qualified_state_fips_count"] >= 30
assert join["pass_30_states"] is True
assert join["no_fuzzy_matching"] is True
assert fema["overlap_state_fips_count_with_qualified_tsdf"] >= 30
assert fema["pass_30_overlap_states"] is True
assert temp["pass_temporal_identity"] is True
assert temp["evaluation_2015_2025_complete"] is True
assert temp["violation_2015_2025_complete"] is True
assert temp["viosnc_spans_2015_2025"] is True

operating = op["unique_ids"]
qualified = join["qualified_unique_id_with_one_fips"]
coverage = join["coverage_fraction"]
states = join["qualified_state_fips_count"]
counties = join["qualified_county_fips_count"]
fema_states = fema["overlap_state_fips_count_with_qualified_tsdf"]
fema_counties = fema["overlap_county_fips_count_with_qualified_tsdf"]
fema_facilities = fema["qualified_tsdf_facilities_in_any_modern_fema_county"]

result_path.write_text(f'''---
id: US-RCRA-F01-RESULT
type: outcome-blind-source-join-time-feasibility
created: {DATE}
issue: 121
gate: PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY
relationship_computed: false
disaster_linked_compliance_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# US-RCRA-F01 Result

**`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`**

US-RCRA-F01 passes the preregistered outcome-blind source/schema/identity/cardinality gate. This result does **not** show that disasters change RCRA compliance outcomes and does not authorize an effect test.

## Frozen feasibility evidence

- The current EPA RCRAInfo national export exposes **{operating:,}** unique facilities in the documented operating-TSDF universe, exceeding the >=500 threshold.
- The exact route `RCRAInfo.ID_NUMBER == ECHO RCRA SOURCE_ID` yields one valid 5-digit county FIPS for **{qualified:,}/{operating:,} = {coverage*100:.1f}%** of the operating-TSDF universe.
- Exact county-qualified operating TSDFs span **{states}** state/territory FIPS codes and **{counties}** county FIPS codes; no fuzzy facility or county matching was used.
- FEMA OpenFEMA 2015-01-01 through 2024-12-31 exposes county-coded disaster/time identities. The exact TSDF geography overlaps FEMA disaster-coded counties in **{fema_states}** state/territory FIPS codes, **{fema_counties}** counties, and **{fema_facilities:,}** of the county-qualified operating TSDF facilities.
- RCRA evaluations and violations structurally cover every year 2015-2025; monthly violation/SNC history spans at least 2015-2025.
- No disaster-linked facility violation/evaluation count, rate, coefficient, ranking, or relationship statistic was computed. Raw source bytes were transient only.

## Technical audit boundary

Three implementation-only corrections were made outcome-blind before terminal disposition: the live evaluation header is `FOUND_VIOLATION`; `OPERATING_TSDF` uses six-position codes with `-` placeholders; and exact ECHO ArcGIS ID queries required smaller batches with bounded retry after a read timeout. None changed the scientific thresholds, selected facility universe semantics, exact identifiers, geography rules, or outcome boundary.

## Claim boundary

This PASS establishes **source/join/time feasibility only**. EPA/GAO already study natural-hazard vulnerability/exposure of RCRA facilities, so no novelty is claimed for static hazard mapping. No predictive or causal disaster-compliance claim is established.

## Exact next action

Return to Stage 0. If US-RCRA remains the highest-value branch, authorize a separate outcome-blind N01 design-identifiability gate before any disaster-linked compliance outcome is opened. N01 must prospectively freeze disaster incident/declaration semantics, baseline compliance, evaluation/inspection surveillance handling, multi-disaster rules, exposure window, comparator, outcome identity, model, overlap boundary, and non-causal claim language.

Incremental monetary cost: **0 USD**.
''', encoding="utf-8")

claim_path.write_text(f'''---
id: CLM-162
type: claim
created: {DATE}
issue: 121
status: active
---

# CLM-162 — Operating RCRA TSDFs have a deterministic national county-disaster/compliance identity bridge

US-RCRA-F01 verifies **{operating:,}** current operating-TSDF IDs, with **{qualified:,}/{operating:,} ({coverage*100:.1f}%)** exact `ID_NUMBER == SOURCE_ID` county-FIPS qualification across **{states}** state/territory FIPS codes. FEMA 2015-2024 county/time identities overlap this geography across **{fema_states}** states/territories, and RCRA evaluation/violation identities structurally cover 2015-2025.

This is a source/schema/identity/cardinality feasibility claim only. No disaster-linked compliance magnitude or relationship was computed; static hazard-map novelty, prediction, and causality are not established. Cost: **0 USD**.
''', encoding="utf-8")

dec_path.write_text(f'''---
id: DEC-168
type: decision
created: {DATE}
issue: 121
status: accepted
---

# DEC-168 — Finalize US-RCRA-F01 as PASS and return to Stage 0

Finalize Issue #121 at **`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`**. The frozen feasibility thresholds pass with {operating:,} operating TSDFs, {coverage*100:.1f}% exact county-FIPS coverage, {states} county-qualified state/territory FIPS codes, {fema_states} FEMA-overlap states/territories, and complete 2015-2025 RCRA temporal identity support.

Do **not** authorize a disaster-compliance effect test from this PASS. Return to Stage 0; any US-RCRA descendant requires a separate outcome-blind design gate that freezes exposure timing, baseline compliance, surveillance/evaluation controls, comparator and model before opening disaster-linked outcomes. Cost remains **0 USD**.
''', encoding="utf-8")

readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace("state: ACTIVE_SOURCE_JOIN_FEASIBILITY", "state: COMPLETED_PASS")
readme += "\n## Terminal disposition / 최종 판정\n\n**`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`** — See `RESULT.md`, `CLM-162`, and `DEC-168`. PASS is source/join/time feasibility only; no disaster-compliance relationship test is authorized.\n"
readme_path.write_text(readme, encoding="utf-8")

claim_ledger = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-162`" not in claim_ledger
claim_ledger_path.write_text(
    claim_ledger.rstrip()
    + f'''\n\n| `CLM-162` | US-RCRA-F01 verifies a deterministic national operating-TSDF → exact ECHO county-FIPS → FEMA county/time → RCRA compliance-identity bridge: {operating:,} operating TSDFs, {qualified:,}/{operating:,} ({coverage*100:.1f}%) exact county qualification across {states} state/territory FIPS codes, with 2015-2025 compliance temporal support and no disaster-linked outcome opened. / RCRA 운영 TSDF→재해·규제 식별 bridge가 값 비사용으로 확립된다. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_FEASIBILITY_GATE` | Run `34719898788`; `research/US-RCRA-F01/FEASIBILITY_MANIFEST.json`; `RESULT.md` | {DATE} | active |\n''',
    encoding="utf-8",
)

decision_log = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-168`" not in decision_log
decision_log_path.write_text(
    decision_log.rstrip()
    + f'''\n\n| `DEC-168` | {DATE} | Finalize US-RCRA-F01 at `PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`; return to Stage 0 without authorizing a relationship test. / US-RCRA-F01 PASS 종결 후 Stage 0 복귀. | {operating:,} operating TSDFs, {coverage*100:.1f}% exact county-FIPS coverage, {states} qualified states/territories, {fema_states} FEMA-overlap states/territories and complete 2015-2025 RCRA temporal support satisfy the frozen gate; disaster-linked outcomes remain unopened. | Issue #121; `CLM-162`; Run `34719898788`; `research/US-RCRA-F01/RESULT.md` | active |\n''',
    encoding="utf-8",
)

status_path.write_text(f'''---
checkpoint_id: CHK-20260913-US-RCRA-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 121
last_completed_research: US-RCRA-F01
last_decision: DEC-168
updated: {DATE}
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_RCRA_F01_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-RCRA-F01 completed outcome-blind at **`PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`**. The current source route identifies {operating:,} operating TSDFs with {qualified:,}/{operating:,} ({coverage*100:.1f}%) exact ECHO county-FIPS qualification across {states} state/territory FIPS codes; FEMA county/time and RCRA 2015-2025 compliance temporal identities are structurally ready. No disaster-linked compliance outcome or relationship was opened.

## Exact next action / 정확한 다음 행동

Return to Stage 0. Compare an outcome-blind US-RCRA N01 design gate against independent alternatives. Do not open disaster-linked compliance outcomes until disaster timing, baseline compliance, evaluation/inspection surveillance handling, multi-disaster rules, comparator, outcome identity and model are frozen in a new authorization.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

handoff_path.write_text(f'''---
checkpoint_id: CHK-20260913-US-RCRA-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 121
last_completed_research: US-RCRA-F01
last_decision: DEC-168
updated: {DATE}
---

# Session Handoff / 세션 인수인계

US-RCRA-F01 / Issue #121 is terminal **PASS** at `PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY`.

Outcome-blind evidence: {operating:,} current operating TSDFs; {qualified:,}/{operating:,} ({coverage*100:.1f}%) exact `ID_NUMBER == SOURCE_ID` county-FIPS qualification; {states} qualified state/territory FIPS codes; {fema_states} FEMA-overlap states/territories; RCRA evaluation/violation temporal identity complete for 2015-2025. No disaster-linked compliance outcome or relationship was computed.

Exact restart: Stage 0. If US-RCRA remains selected, next work is N01 design identifiability only. Freeze disaster incident/declaration semantics, baseline compliance, surveillance/evaluation handling, multi-disaster rules, comparator, outcome and model before opening outcomes. Cost: **0 USD**.
''', encoding="utf-8")

checkpoint_path.write_text(
    json.dumps(
        {
            "checkpoint_id": "CHK-20260913-US-RCRA-F01-PASS-PORTFOLIO-RETURN",
            "active_issue": "none",
            "active_research": "NONE",
            "last_completed_issue": 121,
            "last_completed_research": "US-RCRA-F01",
            "last_decision": "DEC-168",
            "updated": DATE,
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)

print(
    json.dumps(
        {
            "gate": "PASS_US_RCRA_F01_DISASTER_COMPLIANCE_JOIN_READY",
            "operating_tsdf": operating,
            "exact_county_qualified": qualified,
            "coverage": coverage,
            "qualified_states": states,
            "fema_overlap_states": fema_states,
            "relationship_computed": False,
            "cost_usd": 0,
        }
    )
)
