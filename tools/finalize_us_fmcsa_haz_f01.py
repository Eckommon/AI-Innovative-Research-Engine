#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FMCSA-HAZ-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 145
DECISION = "DEC-203"
CLAIM = "CLM-183"
GATE = "PARTIAL_US_FMCSA_HAZ_F01_SOURCE_SEMANTICS_READY__PHMSA_EXPORT_ACCESS_BLOCKED"
STATE = "US_FMCSA_HAZ_F01_PARTIAL_PHMSA_EXPORT_BLOCKED__PORTFOLIO_RETURN"
SOURCE_RUN = int(os.environ.get("SOURCE_RUN_ID", "35057953144"))


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += row
        path.write_text(text, encoding="utf-8")


def main() -> None:
    cp = json.loads((CTX / "checkpoint.json").read_text(encoding="utf-8"))
    assert cp["active_issue"] == ISSUE
    assert cp["active_research"] == "US-FMCSA-HAZ-F01"
    assert cp["last_completed_issue"] == 144
    assert cp["last_decision"] == "DEC-202"

    r = json.loads((OUT / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    a = json.loads((OUT / "STAGING_SOURCE_AUDIT.json").read_text(encoding="utf-8"))

    assert r["gate"] == GATE
    assert r["valid_execution"] is True
    assert r["corrects_run"] == 35057504925
    assert r["correction_chain"] == [35045639924, 35057504925]
    assert r["text_date_parser_correction"] is True
    assert r["implementation_error"] is None

    f = r["fmcsa"]
    assert f["schema_complete"] is True
    assert f["field_map"]["usdot"] == "dot_number"
    assert f["field_map"]["inspection_date"] == "insp_date"
    assert f["distinct_valid_usdot_carriers"] == 662705
    assert f["valid_usdot_inspection_rows"] == 8302114
    assert f["date_parse_success_rows"] == 8302114
    assert f["date_parse_rate"] == 1.0
    assert f["date_years"] == [2023, 2024, 2025, 2026]
    assert f["distinct_date_years"] == 4
    assert f["violation_linkage_ready"] is True
    assert f["violation_inspection_id_nonnull_rate"] == 1.0

    p = r["phmsa"]
    assert p["docs_reachable"] is True
    assert p["public_export_semantics_documented"] is True
    assert p["export_bytes_accessible"] is False
    assert p["required_schema_present"] is False
    partial = r["phmsa_export_access_only_partial_condition"]
    assert partial == {
        "fmcsa_empirical_requirements_pass": True,
        "phmsa_docs_reachable": True,
        "phmsa_export_bytes_accessible": False,
        "phmsa_public_export_semantics_documented": True,
    }

    assert r["hazmat_incident_occurrence_by_inspection_profile_opened"] is False
    assert r["future_incident_membership_conditioned_on_fmcsa_opened"] is False
    assert r["carrier_level_join_membership_persisted"] is False
    assert r["relationship_computed"] is False
    assert r["predictive_metric_computed"] is False
    assert r["causal_claim_made"] is False
    assert r["federal_safety_rating_claim_made"] is False
    assert r["unofficial_mirror_used"] is False
    assert r["authentication_bypass_used"] is False
    assert r["post_execution_rescue_used"] is False
    assert r["incremental_monetary_cost_usd"] == 0
    assert a["raw_source_bytes_persisted"] is False
    assert a["carrier_level_join_membership_persisted"] is False
    assert (OUT / "SUPERSEDED_RUN_35045639924.md").exists()
    assert (OUT / "SUPERSEDED_RUN_35057504925.md").exists()

    result_md = f'''---
id: US-FMCSA-HAZ-F01-RESULT
type: outcome-blind-source-schema-carrier-time-feasibility
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_PARTIAL
gate: {GATE}
source_run: {SOURCE_RUN}
hazmat_incident_occurrence_by_inspection_profile_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FMCSA-HAZ-F01 Result — PHMSA-export access-limited PARTIAL

**`{GATE}`**

Corrected Run `{SOURCE_RUN}` validly executes the frozen outcome-blind FMCSA inspection × PHMSA highway hazmat source/schema/carrier-time gate using official DOT/FMCSA/PHMSA routes only.

## FMCSA empirical support / FMCSA 실증 지원

The frozen FMCSA side passes its prospective structural requirements:

- native carrier identity: `dot_number` → exact numeric USDOT canonicalization;
- distinct valid USDOT carriers: **662,705** (threshold >=50,000);
- valid inspection rows / distinct inspection IDs: **8,302,114**;
- repeated-inspection carriers: **471,908**;
- native `insp_date` is source text, parsed deterministically by exact-value weighted parsing;
- date parseability: **100% = 8,302,114 / 8,302,114**;
- supported years: **2023–2026, 4 years** (threshold >=3);
- violation rows: **13,536,445**;
- violation rows with inspection ID: **13,536,445 = 100%**;
- distinct violation inspection IDs: **4,592,338**;
- OOS/inspection linkage is structurally available and deterministic;
- FMCSA carrier fingerprint: `{f['carrier_fingerprint']}`.

## PHMSA access-only blocker / PHMSA 접근 전용 장벽

Official PHMSA catalog/dictionary semantics are reachable and document the public detailed incident export path, but the frozen zero-cost runner cannot retrieve the Oracle detailed-export bytes. Therefore the byte-dependent PHMSA requirements remain **uncomputed rather than failed**:

- detailed export schema presence;
- >=500 distinct Highway FED DOT IDs;
- >=95% incident-date parseability and >=10 years;
- exact FMCSA USDOT ↔ PHMSA FED DOT intersection >=300;
- PHMSA and intersection identity fingerprints.

The preregistered PARTIAL explicitly applies only when all FMCSA empirical requirements pass, PHMSA semantics pass, and the sole remaining blocker is official PHMSA export-byte access. Run `{SOURCE_RUN}` satisfies exactly that condition.

## Preserved implementation history / 구현 비적합 보존

- Run `35045639924`: native `dot_number` alias was not mapped; execution invalid for gate.
- Run `35057504925`: `insp_date` was correctly identified as text, but inherited date support did not parse text values and therefore incorrectly produced zero supported years; not accepted as terminal scientific disposition.
- Run `{SOURCE_RUN}`: same source/field/thresholds, deterministic weighted text-date parsing only; valid PARTIAL.

No threshold, source identity, carrier join rule or outcome boundary was changed during these corrections.

## Outcome-blind boundary / outcome 비개봉 경계

- hazmat incident occurrence/rate/count by FMCSA inspection/violation/OOS profile: **not opened**;
- future incident membership conditioned on FMCSA profile: **not opened**;
- carrier-level FMCSA↔PHMSA joined membership: **not persisted**;
- relationship/prediction: **not computed**;
- causal or federal safety-rating claim: **not made**;
- unofficial mirror/authentication bypass: **not used**;
- incremental monetary cost: **0 USD**.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve `US-FMCSA-HAZ-001` as an access-blocked asset. Do not substitute unofficial PHMSA incident files, infer the uncomputed carrier intersection, or redesign the branch from observed outcomes. Re-entry is allowed only if the official PHMSA detailed export becomes executable at zero incremental cost or a later independent prospective portfolio decision reselects the branch.
'''
    (OUT / "RESULT.md").write_text(result_md, encoding="utf-8")

    result_json = {
        "research_id": "US-FMCSA-HAZ-F01",
        "issue": ISSUE,
        "gate": GATE,
        "source_run": SOURCE_RUN,
        "correction_chain": [35045639924, 35057504925, SOURCE_RUN],
        "fmcsa_distinct_valid_usdot_carriers": 662705,
        "fmcsa_valid_inspection_rows": 8302114,
        "fmcsa_date_parse_rate": 1.0,
        "fmcsa_date_years": [2023, 2024, 2025, 2026],
        "fmcsa_violation_linkage_ready": True,
        "phmsa_docs_reachable": True,
        "phmsa_public_export_semantics_documented": True,
        "phmsa_export_bytes_accessible": False,
        "phmsa_byte_dependent_support": "uncomputed",
        "hazmat_incident_occurrence_by_inspection_profile_opened": False,
        "carrier_level_join_membership_persisted": False,
        "relationship_computed": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "RESULT.json").write_text(json.dumps(result_json, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nCorrected Run `{SOURCE_RUN}` finalizes **`{GATE}`**. FMCSA empirical source/schema/carrier/date/violation-linkage requirements pass; the official PHMSA detailed-export bytes remain unavailable, so PHMSA cardinality/date/intersection requirements remain uncomputed. Runs `35045639924` and `35057504925` remain preserved as implementation nonconformities. No hazmat incident outcome or carrier-level joined membership was opened.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_ACCESS_GATE
status: active
---

# {CLAIM} — US-FMCSA-HAZ-F01 FMCSA-ready / PHMSA-export access blocked

Corrected Run `{SOURCE_RUN}` establishes strong outcome-blind FMCSA structural support: **662,705** distinct valid USDOT carriers, **8,302,114** valid inspections, **100%** deterministic parseability of native `insp_date` across **2023–2026**, and deterministic inspection→violation/OOS linkage across **13,536,445** violation rows. Official PHMSA catalog/dictionary export semantics are documented, but the detailed Oracle export bytes are not currently retrievable by the frozen zero-cost runner.

Therefore the frozen result is **`{GATE}`**. PHMSA carrier/date/intersection thresholds are uncomputed rather than failed. No incident occurrence by inspection profile, joined carrier membership, relationship, prediction or causal quantity was opened.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FMCSA-HAZ-F01
status: active
---

# {DECISION} — Finalize US-FMCSA-HAZ-F01 as PHMSA-export access-limited PARTIAL

## Decision / 결정

Finalize US-FMCSA-HAZ-F01 at **`{GATE}`** and return to Stage 0. Preserve the branch as an access-blocked asset; do not replace the unavailable official PHMSA detailed export with unofficial mirrors or infer the uncomputed exact-carrier overlap.

## Rationale / 근거

After two preserved implementation corrections, Run `{SOURCE_RUN}` validly demonstrates that all preregistered FMCSA empirical requirements pass. Official PHMSA export semantics are documented while the actual detailed export bytes remain inaccessible to the zero-cost official-source runner. This is exactly the prospectively frozen PARTIAL sole-blocker condition.

## Boundary / 경계

- no carrier-level joined incident membership persistence;
- no hazmat incident outcome stratified by FMCSA profile;
- no relationship/prediction/causal/federal-safety-rating claim;
- re-entry requires restored official zero-cost PHMSA export access or a later independent portfolio reselection;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | US-FMCSA-HAZ-F01 passes FMCSA structural support (662,705 carriers; 8,302,114 inspections; 100% date parsing across 2023–2026; deterministic violation/OOS linkage) but official PHMSA detailed-export bytes remain inaccessible, leaving PHMSA support uncomputed. / FMCSA-ready, PHMSA-export access-blocked PARTIAL. | `OBSERVED/DERIVED` | `V3_OUTCOME_BLIND_ACCESS_GATE` | Issue #145; Run `{SOURCE_RUN}`; `research/US-FMCSA-HAZ-F01/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Finalize US-FMCSA-HAZ-F01 as PHMSA-export access-limited PARTIAL; no unofficial substitution; return to Stage 0. / FMCSA-HAZ F01을 PHMSA export 접근제한 PARTIAL로 종결. | FMCSA empirical gate passes; PHMSA semantics documented; detailed export bytes inaccessible; outcome boundary intact. | Issue #145; `{CLAIM}`; Run `{SOURCE_RUN}` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-US-FMCSA-HAZ-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 145
last_completed_research: US-FMCSA-HAZ-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FMCSA-HAZ-F01 is terminal at **`{GATE}`** under corrected Run `{SOURCE_RUN}`, {DECISION} and {CLAIM}. FMCSA source/schema/carrier/date/violation-linkage support passes strongly; official PHMSA detailed-export semantics are documented but the export bytes remain inaccessible to the frozen zero-cost runner. PHMSA carrier/date/intersection requirements remain uncomputed. No hazmat incident outcome or joined carrier membership was opened.

## Exact next action / 정확한 다음 행동

Return to Stage 0 and open a new portfolio reselection. Preserve US-FMCSA-HAZ-001 as an access-blocked asset; do not automatically redesign it around another PHMSA source and do not use unofficial mirrors. Compare preserved and fresh candidates prospectively before authorizing exactly one next outcome-blind gate.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-US-FMCSA-HAZ-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 145,
        "last_completed_research": "US-FMCSA-HAZ-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    handoff = f'''---
checkpoint_id: CHK-20260916-US-FMCSA-HAZ-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 145
last_completed_research: US-FMCSA-HAZ-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- terminal gate: `{GATE}`
- valid source run: `{SOURCE_RUN}`
- superseded implementation runs: `35045639924`, `35057504925`
- FMCSA distinct valid USDOT carriers: `662705`
- FMCSA valid inspections: `8302114`
- FMCSA date support: `2023–2026`, parse rate `1.0`
- FMCSA violation/OOS linkage: ready
- official PHMSA export semantics: documented
- PHMSA detailed-export bytes: inaccessible
- PHMSA carrier/date/exact-intersection thresholds: uncomputed
- carrier-level joined incident membership: not persisted
- hazmat incident outcome by FMCSA profile: unopened
- relationship/prediction/causality: closed

## Exact restart point / 정확한 재개점

Open a new Stage-0 portfolio reselection. Keep US-FMCSA-HAZ-001 parked as an access-blocked asset. Do not auto-redesign the PHMSA source after observing F01, and do not use unofficial substitutes. Prospectively compare preserved and fresh candidates, then authorize exactly one next outcome-blind gate.

Incremental monetary cost remains **0 USD**.
'''
    (CTX / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE, "source_run": SOURCE_RUN}, sort_keys=True))


if __name__ == "__main__":
    main()
