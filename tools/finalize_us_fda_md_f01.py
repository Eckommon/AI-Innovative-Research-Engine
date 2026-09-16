#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-FDA-MD-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 141
DECISION = "DEC-195"
CLAIM = "CLM-179"
GATE = "PARTIAL_US_FDA_MD_F01_SOURCE_SEMANTICS_READY__INSPECTION_BYTES_ACCESS_BLOCKED"
STATE = "US_FDA_MD_F01_PARTIAL_ACCESS_BLOCKED__PORTFOLIO_RETURN"
SOURCE_RUN = os.environ.get("SOURCE_RUN_ID", "35040935495")


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
    assert cp["active_research"] == "US-FDA-MD-F01"
    assert cp["last_completed_issue"] == 140
    assert cp["last_decision"] == "DEC-194"

    r = json.loads((OUT / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    a = json.loads((OUT / "STAGING_SOURCE_AUDIT.json").read_text(encoding="utf-8"))
    assert r["gate"] == GATE
    assert r["inspection_bytes_accessible"] is False
    assert r["recall_public_route"] is True
    assert all(r["semantics"].values())
    assert r["recall_incidence_by_class_opened"] is False
    assert r["class_specific_recall_membership_opened"] is False
    assert r["relationship_computed"] is False
    assert r["unofficial_mirror_used"] is False
    assert r["authentication_bypass_used"] is False
    assert r["post_execution_rescue_used"] is False
    assert r["incremental_monetary_cost_usd"] == 0
    probes = a["advertised_inspection_download_probes"]
    assert probes and all(p["http"] == 404 for p in probes)
    assert a["openfda_recall_partition_count"] >= 1

    result_md = f'''---
id: US-FDA-MD-F01-RESULT
type: outcome-blind-source-schema-identity-feasibility
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_PARTIAL
gate: {GATE}
recall_incidence_by_class_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FDA-MD-F01 Result — access-limited PARTIAL

**`{GATE}`**

Run `{SOURCE_RUN}` executed the preregistered FDA inspection × Device Recall source/schema/FEI gate using official FDA/openFDA routes only.

## What is established / 확립된 것

Official source semantics are structurally coherent for a future bounded FEI design:

- FDA FEI is documented as the unique establishment/facility identifier;
- final inspection classifications are `NAI`, `VAI`, `OAI`;
- one inspection may produce multiple Project Area rows;
- current CDRH guidance explicitly supports searching medical-device manufacturing facilities by FEI and filtering to medical-device inspection type;
- FDA explicitly states the public inspection database is not comprehensive;
- openFDA Device Recall documents native `firm_fei_number` plus initiated/created/posted event-date fields;
- the official openFDA bulk-download manifest is publicly executable and currently exposes the Device Recall source.

## Exact access blocker / 정확한 접근 장벽

The current FDA Inspections Dashboard itself is reachable, but both official inspection dataset links found/probed by the frozen runner return **HTTP 404**:

- `https://datadashboard.fda.gov/InspectionsDataset.xlsx`
- `https://datadashboard.fda.gov/oii/cd/InspectionsData-filtered.xlsx`

The Dashboard simultaneously documents that API credentials require **OII Unified Logon** authorization. No unofficial mirror, cached replica, alternate scraped dataset or authentication bypass was used.

Because actual inspection bytes are unavailable, the preregistered empirical byte-dependent requirements were **not calculable**, not scientifically failed:

- exact FEI/date/classification/native-device field presence in current bytes;
- structural-key classification conflicts;
- >=500 device-inspection FEIs;
- >=5 inspection years;
- repeated-inspection multiplicity;
- >=100 aggregate exact inspection-FEI ↔ recall-FEI overlap;
- FEI/intersection fingerprints.

The frozen PARTIAL disposition was specifically defined for this condition, so these unavailable checks must not be converted into a HOLD or rescued with nonofficial data.

## Outcome-blind boundary / outcome 비개봉 경계

- recall incidence/rate/count by NAI/VAI/OAI: **not opened**
- class-specific future-recall membership: **not opened**
- inspection→recall relationship/model: **not computed**
- population-wide manufacturer risk: **not claimed**
- unofficial mirror: **not used**
- authentication bypass: **not used**
- incremental monetary cost: **0 USD**

## Interpretation / 해석

This result means **source semantics are ready, but current official inspection bytes are access-blocked**. It does not establish that NAI/VAI/OAI predicts recall risk, and it does not justify any inspection-class ranking or causal interpretation.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Preserve US-FDA-MD-001 as an access-blocked asset rather than redesigning it. It may be reconsidered only if the official public inspection download becomes functional, an authorized zero-cost official API credential becomes available, or a later independent portfolio decision prospectively reactivates the branch. Do not use unofficial substitutes.
'''
    (OUT / "RESULT.md").write_text(result_md, encoding="utf-8")
    (OUT / "RESULT.json").write_text(json.dumps({
        "research_id": "US-FDA-MD-F01", "issue": ISSUE, "gate": GATE,
        "source_run": int(SOURCE_RUN),
        "inspection_bytes_accessible": False,
        "official_inspection_download_http": sorted({p["http"] for p in probes}),
        "semantics_all_confirmed": True,
        "recall_public_route": True,
        "recall_incidence_by_class_opened": False,
        "class_specific_recall_membership_opened": False,
        "relationship_computed": False,
        "unofficial_mirror_used": False,
        "authentication_bypass_used": False,
        "incremental_monetary_cost_usd": 0,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nRun `{SOURCE_RUN}` finalizes **`{GATE}`**. FDA/openFDA semantics and the public Device Recall route pass, while the official advertised inspection XLSX routes return 404 and the remaining Dashboard API requires OII Unified Logon credentials. Byte-dependent FEI/schema/overlap thresholds remain uncomputed. No recall outcome was opened by inspection class.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_ACCESS_GATE
status: active
---

# {CLAIM} — US-FDA-MD-F01 semantics-ready / inspection-bytes access blocked

Run `{SOURCE_RUN}` confirms official FDA semantics for exact FEI identity, NAI/VAI/OAI final classification, repeated Project Area rows, CDRH medical-device FEI filtering, public-database incompleteness, and openFDA Device Recall `firm_fei_number`/event-date identities. The official openFDA route is available, but the current advertised inspection dataset links return HTTP 404 while the Dashboard states API credentials require OII Unified Logon authorization.

Therefore the frozen result is **`{GATE}`**. Byte-dependent cohort cardinality, conflict and FEI-overlap thresholds are uncomputed rather than failed. No recall incidence or membership by inspection class was opened.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FDA-MD-F01
status: active
---

# {DECISION} — Finalize US-FDA-MD-F01 as access-limited PARTIAL

## Decision / 결정

Finalize US-FDA-MD-F01 at **`{GATE}`** and return to Stage 0. Do not replace the unavailable official inspection bytes with unofficial mirrors or infer the uncomputed FEI/schema/overlap thresholds.

## Rationale / 근거

The exact access-only PARTIAL condition frozen in Issue #141 is met: FDA documentation confirms the required identity/classification/project-area/device semantics; openFDA Device Recall FEI/date source is public; the advertised official inspection download routes return 404; and the Dashboard documents credentialed API access. No deeper schema or identity failure can be assessed without the bytes.

## Boundary / 경계

- This is not evidence for inspection-class recall risk.
- No NAI/VAI/OAI-specific recall occurrence was opened.
- No population-wide manufacturer inference.
- Re-entry requires restored official public bytes, an authorized zero-cost official credential, or a new independent prospective portfolio decision.
- Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | US-FDA-MD-F01 confirms FDA/openFDA FEI/classification/project-area/device/recall semantics but official inspection XLSX routes return 404 and API is credentialed; byte-dependent support remains uncomputed and class-stratified recall outcomes unopened. / FDA inspection source semantics-ready, bytes access-blocked PARTIAL. | `OBSERVED/DERIVED` | `V3_OUTCOME_BLIND_ACCESS_GATE` | Issue #141; Run `{SOURCE_RUN}`; `research/US-FDA-MD-F01/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Finalize US-FDA-MD-F01 as access-limited PARTIAL; no unofficial substitution; return to Stage 0. / FDA F01을 공식 inspection bytes 접근제한 PARTIAL로 종결. | Required semantics/openFDA route pass; advertised inspection files 404 and Dashboard API credentialed; byte-dependent thresholds uncomputed. | Issue #141; `{CLAIM}`; Run `{SOURCE_RUN}` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-US-FDA-MD-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 141
last_completed_research: US-FDA-MD-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FDA-MD-F01 is terminal at **`{GATE}`** under Run `{SOURCE_RUN}`, {DECISION} and {CLAIM}. FDA/openFDA source semantics are structurally ready, but current official inspection dataset bytes are unavailable through the advertised public links; the remaining Dashboard API is credentialed. No recall incidence/membership by inspection class was opened and no relationship was computed.

## Exact next action / 정확한 다음 행동

Return to Stage 0 and perform a new portfolio reselection. Preserve US-FDA-MD-001 as an access-blocked asset; do not automatically promote a prior runner-up and do not use unofficial inspection mirrors. Re-score preserved/fresh candidates using the new access information before selecting one next branch.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")
    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-US-FDA-MD-F01-TERMINAL",
        "active_issue": "none", "active_research": "NONE",
        "last_completed_issue": 141, "last_completed_research": "US-FDA-MD-F01",
        "last_decision": DECISION, "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")
    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FDA-MD-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 141
last_completed_research: US-FDA-MD-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- terminal gate: `{GATE}`
- source run: `{SOURCE_RUN}`
- FDA/openFDA semantics: ready
- official inspection bytes: access blocked (advertised XLSX routes HTTP 404; Dashboard API credentialed)
- byte-dependent FEI/cardinality/overlap thresholds: uncomputed
- recall incidence/membership by inspection class: unopened
- relationship computed: false

## Exact restart point / 정확한 재개점

Open a new Stage-0 portfolio reselection. Keep US-FDA-MD-001 parked as an access-blocked asset. Do not use unofficial inspection data or auto-promote a runner-up. Compare preserved and fresh candidates prospectively, then authorize exactly one next outcome-blind gate.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")
    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE, "source_run": SOURCE_RUN}, sort_keys=True))

if __name__ == "__main__":
    main()
