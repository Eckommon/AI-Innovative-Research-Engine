#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "US-EPA-XMEDIA-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 150
RUN = 35166942067
STAGING_COMMIT = "7a9599ae76af2e93d5806a0473ad17f6bbc1ac93"
DECISION = "DEC-213"
CLAIM = "CLM-188"
GATE = "PASS_US_EPA_XMEDIA_F01_EXACT_FRS_CROSS_PROGRAM_JOIN_READY"
STATE = "US_EPA_XMEDIA_F01_PASS__N01_AUTHORIZATION_REQUIRED"


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += row
        path.write_text(text, encoding="utf-8")


def main() -> None:
    cp = json.loads((CTX / "checkpoint.json").read_text(encoding="utf-8"))
    assert cp == {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-F01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-EPA-XMEDIA-F01",
        "last_completed_issue": 149,
        "last_completed_research": "PORTFOLIO-R34",
        "last_decision": "DEC-212",
        "updated": "2026-09-17",
    }

    s = json.loads((RESEARCH / "STAGING_RESULT_CORRECTED.json").read_text(encoding="utf-8"))
    assert s["research"] == "US-EPA-XMEDIA-F01"
    assert s["issue"] == ISSUE
    assert s["contract_commit"] == "86a7a01ba3b64160ee21a7ea821536d3d1adbb14"
    assert s["activation_decision"] == "DEC-212"
    assert s["gate"] == GATE
    assert s["scientific_disposition"] == "PASS"
    assert s["requirements_passed"] == 18 and s["requirements_total"] == 18
    assert all(r["pass"] for r in s["requirements"])
    assert s["effluent_violation_rows_opened"] is False
    assert s["dmr_outcome_rows_opened"] is False
    assert s["relationship_computed"] is False
    assert s["predictive_metric_computed"] is False
    assert s["causal_claim_made"] is False
    assert s["identity_repair_used"] is False
    assert s["incremental_monetary_cost_usd"] == 0
    corr = s["implementation_correction"]
    for k in ("contract_changed", "sources_changed", "thresholds_changed", "identity_rules_changed", "outcome_firewall_changed"):
        assert corr[k] is False

    m = s["measurements"]
    yrs = m["npdes_permit_date_years"]
    assert yrs and all(1900 <= y <= 2100 for y in yrs)

    (RESEARCH / "RESULT.md").write_text(f'''---
id: US-EPA-XMEDIA-F01-RESULT
type: outcome-blind-cross-media-source-schema-frs-identity-feasibility
created: 2026-09-17
issue: {ISSUE}
state: COMPLETED_PASS
gate: {GATE}
source_run: {RUN}
staging_commit: {STAGING_COMMIT}
effluent_violation_rows_opened: false
dmr_outcome_rows_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-F01 Result — exact FRS cross-program join-ready PASS

**`{GATE}`**

Corrected immutable Run `{RUN}` validly executed the pre-Issue contract frozen at `86a7a01ba3b64160ee21a7ea821536d3d1adbb14`. All **18/18** preregistered requirements passed. This is a structural source/schema/identity/time feasibility result only; it does not establish any RCRA→NPDES outcome relationship.

## Structural evidence / 구조적 근거

- RCRA evaluation rows: **{m['rcra_evaluation_rows']:,}**; valid identity/date rows: **{m['rcra_valid_identity_date_rows']:,}**
- distinct RCRA `SOURCE_ID`: **{m['rcra_distinct_source_ids']:,}**; distinct RCRA `REGISTRY_ID`: **{m['rcra_distinct_registry_ids']:,}**
- RCRA valid evaluation years: **{min(m['rcra_distinct_valid_years'])}–{max(m['rcra_distinct_valid_years'])}** ({len(m['rcra_distinct_valid_years'])} years)
- exact RCRA↔FRS corroboration: **{m['rcra_pairs_exactly_corroborated_by_frs']:,}/{m['rcra_pairs_represented_in_frs']:,} = {m['rcra_exact_corroboration_rate']:.6%}**
- FRS Program Link rows: **{m['frs_program_link_rows']:,}**
- exact FRS RCRAInfo↔NPDES Registry-ID intersection: **{m['frs_exact_cross_program_registry_intersection']:,}**
- NPDES facility rows / distinct IDs: **{m['npdes_facility_rows']:,} / {m['npdes_distinct_ids']:,}**
- NPDES distinct Registry IDs: **{m['npdes_distinct_registry_ids']:,}**
- exact NPDES↔FRS corroboration: **{m['npdes_pairs_exactly_corroborated_by_frs']:,}/{m['npdes_pairs_represented_in_frs']:,} = {m['npdes_exact_corroboration_rate']:.6%}**
- NPDES permit rows: **{m['npdes_permit_rows']:,}**
- valid structural permit-date years after mechanical parser correction: **{min(yrs)}–{max(yrs)}**, **{len(yrs)}** distinct years
- exact Registry IDs simultaneously supported by valid RCRA evaluation + both non-conflicting FRS program links + ICIS-NPDES Part 1 permit identity: **{m['exact_cross_program_registry_ids_with_rcra_eval_and_npdes_part1_permit']:,}**

## Deterministic fingerprints / 결정론적 지문

- RCRA exact identity pairs: `{m['fingerprints']['rcra_exact_identity_pairs_sha256']}`
- FRS RCRAInfo exact pairs: `{m['fingerprints']['frs_rcra_exact_pairs_sha256']}`
- FRS NPDES exact pairs: `{m['fingerprints']['frs_npdes_exact_pairs_sha256']}`
- NPDES Part 1 exact identity pairs: `{m['fingerprints']['npdes_part1_exact_identity_pairs_sha256']}`
- FRS cross-program Registry intersection: `{m['fingerprints']['frs_cross_program_registry_intersection_sha256']}`
- fully cross-supported Registry IDs: `{m['fingerprints']['exact_cross_supported_registry_sha256']}`

## Implementation correction / 구현 보정

The first immutable staging result is preserved. Review detected that its fallback date parser could admit malformed/out-of-range calendar years. The corrected rerun changed **only** that parser boundary to valid years `1900–2100`; the frozen contract, source set, thresholds, identity rules and outcome firewall were unchanged. The corrected run remained **18/18 PASS**, and all identity counts/fingerprints remained unchanged.

## Outcome-blind boundary / 결과 비개봉 경계

- ICIS-NPDES Part 2 / effluent-violation rows: **not opened**;
- DMR reported values, limits or exceedance rows: **not opened**;
- name/address/geospatial/fuzzy/manual/post-outcome identity repair: **not used**;
- RCRA-conditioned NPDES outcome occurrence/rate/magnitude: **not computed**;
- relationship/prediction/causality: **not computed or claimed**;
- incremental monetary cost: **0 USD**.

## Interpretation / 해석

The official EPA RCRA Pipeline, FRS and ICIS-NPDES Part 1 sources provide a large, exact, source-native cross-program identity surface suitable for a separately preregistered outcome-blind design gate. F01 alone does not authorize opening downstream effluent outcomes.

## Exact next action / 정확한 다음 행동

Freeze a separate `US-EPA-XMEDIA-N01` design-identifiability contract before Issue binding and before any Part 2/DMR outcome access. N01 must prospectively define the RCRA structural exposure, facility eligibility, time ordering, matching/stratification, missingness rules and the exact later E01 outcome/statistical contract.
''', encoding="utf-8")

    readme_path = RESEARCH / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Terminal F01 result / F01 최종 결과" not in readme:
        readme += f'''\n\n## Terminal F01 result / F01 최종 결과\n\n**`{GATE}`** — corrected immutable Run `{RUN}` passed all 18 frozen requirements. The original staging artifact is preserved; a mechanical date-parser correction changed no contract/source/threshold/identity/outcome boundary. Part 2 and DMR outcomes remain unopened. See `RESULT.md`.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-17
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_FEASIBILITY
status: active
---

# {CLAIM} — EPA RCRA×FRS×NPDES exact cross-program identity is structurally join-ready

Corrected immutable Run `{RUN}` passes all 18 preregistered F01 requirements. There are **{m['frs_exact_cross_program_registry_intersection']:,}** exact FRS Registry IDs in the RCRAInfo↔NPDES program-family intersection and **{m['exact_cross_program_registry_ids_with_rcra_eval_and_npdes_part1_permit']:,}** Registry IDs simultaneously supported by valid RCRA evaluation structure and ICIS-NPDES Part 1 permit identity. Exact corroboration is **{m['rcra_exact_corroboration_rate']:.6%}** on the RCRA side and **{m['npdes_exact_corroboration_rate']:.6%}** on the NPDES side.

This is a structural feasibility claim only. Effluent-violation/DMR outcomes, relationships, prediction, facility ranking and causal effects remain unopened/uncomputed.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-EPA-XMEDIA-F01
status: active
---

# {DECISION} — Accept corrected US-EPA-XMEDIA-F01 PASS and require separate N01

Accept corrected immutable staging commit `{STAGING_COMMIT}` from Run `{RUN}` as **`{GATE}`** and close Issue #{ISSUE} as completed.

The first staging artifact remains preserved. The correction was implementation-only: valid calendar-year range enforcement for structural NPDES permit dates. No frozen research parameter changed.

This PASS authorizes only a separately preregistered outcome-blind `US-EPA-XMEDIA-N01`. It does not authorize direct opening of ICIS-NPDES Part 2 or DMR outcomes.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | US-EPA-XMEDIA-F01 passes all 18 frozen requirements: 60,677 exact FRS RCRAInfo↔NPDES Registry IDs, 18,415 fully cross-supported Registry IDs, RCRA FRS corroboration 100%, NPDES FRS corroboration 99.9976%; outcomes unopened. / EPA cross-media 구조 join-ready PASS. | `DERIVED` | `V2_PRIMARY_VERIFIED_FEASIBILITY` | Issue #150; Run {RUN}; `research/US-EPA-XMEDIA-F01/RESULT.md` | 2026-09-17 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-17 | Accept corrected US-EPA-XMEDIA-F01 PASS; require separate outcome-blind N01. / corrected F01 PASS 수용 후 N01 별도 사전등록 요구. | Corrected immutable staging `{STAGING_COMMIT}`; Run {RUN}; 18/18 PASS; source-level Part 2/DMR firewall preserved. | Issue #150; `{CLAIM}`; `research/US-EPA-XMEDIA-F01/RESULT.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-EPA-XMEDIA-F01
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-EPA-XMEDIA-F01 is terminal at **`{GATE}`** under {DECISION} / {CLAIM}. Corrected immutable Run `{RUN}` passed **18/18** frozen requirements. Exact structural support includes **{m['frs_exact_cross_program_registry_intersection']:,}** FRS cross-program Registry IDs and **{m['exact_cross_program_registry_ids_with_rcra_eval_and_npdes_part1_permit']:,}** fully cross-supported Registry IDs. Effluent-violation and DMR outcomes remain unopened.

## Exact next action / 정확한 다음 행동

Freeze `US-EPA-XMEDIA-N01` before opening its Issue. N01 must build a deterministic outcome-blind design using only authorized structural information and prospectively freeze the later E01 outcome/statistical contract before any Part 2/DMR access.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260917-US-EPA-XMEDIA-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": ISSUE,
        "last_completed_research": "US-EPA-XMEDIA-F01",
        "last_decision": DECISION,
        "updated": "2026-09-17",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: {ISSUE}
last_completed_research: US-EPA-XMEDIA-F01
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- gate: `{GATE}`
- corrected source run: `{RUN}`
- corrected immutable staging commit: `{STAGING_COMMIT}`
- FRS cross-program Registry intersection: {m['frs_exact_cross_program_registry_intersection']:,}
- fully cross-supported Registry IDs: {m['exact_cross_program_registry_ids_with_rcra_eval_and_npdes_part1_permit']:,}
- RCRA exact FRS corroboration: {m['rcra_exact_corroboration_rate']:.6%}
- NPDES exact FRS corroboration: {m['npdes_exact_corroboration_rate']:.6%}
- Part 2/DMR outcome rows opened: false
- relationship/prediction/causality: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Freeze `US-EPA-XMEDIA-N01` before Issue binding. Preserve the F01 source-level outcome firewall until a later separately authorized E01.
''', encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
