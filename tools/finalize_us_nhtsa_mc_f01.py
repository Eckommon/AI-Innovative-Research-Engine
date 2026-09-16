#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "US-NHTSA-MC-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 143
AUTH_DECISION = "DEC-198"
DECISION = "DEC-199"
CLAIM = "CLM-181"
GATE = "HOLD_US_NHTSA_MC_F01_SOURCE_SCHEMA_OR_IDENTITY"
STATE = "US_NHTSA_MC_F01_HOLD__PORTFOLIO_RETURN"
SOURCE_RUN = os.environ.get("SOURCE_RUN_ID", "35043099657")


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
    assert cp["active_research"] == "US-NHTSA-MC-F01"
    assert cp["last_completed_issue"] == 142
    assert cp["last_decision"] == AUTH_DECISION

    r = json.loads((OUT / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    a = json.loads((OUT / "STAGING_SOURCE_AUDIT.json").read_text(encoding="utf-8"))
    assert r["gate"] == GATE
    assert r["valid_execution"] is True
    assert r["corrects_runs"] == [35042810534, 35042957163]

    # Positive structural support that was validly measured.
    assert r["communication"]["structural_product_document_schema_readable"] is True
    assert r["communication"]["distinct_product_keys"] >= 10_000
    assert r["recall"]["distinct_product_keys"] >= 5_000
    assert r["communication"]["distinct_normalized_makes"] >= 25
    assert r["recall"]["distinct_normalized_makes"] >= 25
    assert r["aggregate_product_key_overlap"] >= 1_000
    assert r["recall"]["distinct_date_years"] >= 10
    assert r["recall"]["date_parse_rate"] >= 0.95
    assert all(r["fingerprints"].values())

    # Frozen requirements that validly fail.
    assert r["communication"]["full_frozen_required_schema_present"] is False
    assert r["communication"]["distinct_date_years"] == 0
    assert r["communication"]["date_parse_rate"] == 0.0
    assert r["requirements"]["communication_schema_verified"] is False
    assert r["requirements"]["communication_date_support_ge_5_years_and_95pct"] is False
    assert r["requirements"]["official_metadata_dictionaries_reachable_hashed"] is False
    assert a["catalog"]["http"] == 403
    archives = a["communication_archives"]
    assert len(archives) == 2
    assert all(x["structural_product_document_schema_readable"] for x in archives)
    assert all(x["communication_date_field_present"] is False for x in archives)
    assert all(x["full_frozen_required_schema_present"] is False for x in archives)

    # Outcome-blind boundary.
    assert r["recall_incidence_opened"] is False
    assert r["future_recall_membership_conditioned_on_communications_opened"] is False
    assert r["relationship_computed"] is False
    assert r["predictive_metric_computed"] is False
    assert r["causal_claim_made"] is False
    assert r["unofficial_mirror_used"] is False
    assert r["authentication_bypass_used"] is False
    assert r["post_execution_rescue_used"] is False
    assert r["incremental_monetary_cost_usd"] == 0

    result_json = {
        "research_id": "US-NHTSA-MC-F01",
        "issue": ISSUE,
        "gate": GATE,
        "source_run": int(SOURCE_RUN),
        "valid_execution": True,
        "communication_distinct_product_keys": r["communication"]["distinct_product_keys"],
        "communication_distinct_makes": r["communication"]["distinct_normalized_makes"],
        "communication_date_field_present": False,
        "communication_distinct_date_years": 0,
        "recall_distinct_product_keys": r["recall"]["distinct_product_keys"],
        "recall_distinct_makes": r["recall"]["distinct_normalized_makes"],
        "recall_distinct_date_years": r["recall"]["distinct_date_years"],
        "recall_date_parse_rate": r["recall"]["date_parse_rate"],
        "aggregate_product_key_overlap": r["aggregate_product_key_overlap"],
        "catalog_http": a["catalog"]["http"],
        "fingerprints": r["fingerprints"],
        "recall_incidence_opened": False,
        "future_recall_membership_conditioned_on_communications_opened": False,
        "relationship_computed": False,
        "unofficial_mirror_used": False,
        "incremental_monetary_cost_usd": 0,
    }
    (OUT / "RESULT.json").write_text(json.dumps(result_json, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    result_md = f'''---
id: US-NHTSA-MC-F01-RESULT
type: outcome-blind-source-schema-product-time-feasibility
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_HOLD
gate: {GATE}
recall_incidence_opened: false
future_recall_membership_conditioned_on_communications_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-NHTSA-MC-F01 Result — source/schema HOLD

**`{GATE}`**

Corrected Run `{SOURCE_RUN}` validly evaluated the frozen official NHTSA Manufacturer Communications × Safety Recall source/schema/product-time gate. The two earlier runs (`35042810534`, `35042957163`) remain preserved as implementation-invalid and do not contribute scientific dispositions.

## Strong structural support that passed / 통과한 구조적 지원

The frozen source family is large and the exact product identity itself is viable:

- Manufacturer Communications valid product rows: **{r['communication']['valid_product_rows']:,}**
- Manufacturer Communications distinct product keys: **{r['communication']['distinct_product_keys']:,}** (>=10,000 required)
- Manufacturer Communications normalized makes: **{r['communication']['distinct_normalized_makes']:,}** (>=25 required)
- distinct communication document IDs: **{r['multiplicity']['distinct_communication_document_ids']:,}**
- product keys with multiple communication documents: **{r['multiplicity']['product_keys_with_multiple_communication_documents']:,}**
- maximum communication documents on one product key: **{r['multiplicity']['max_communication_documents_per_product_key']:,}**
- Safety Recall distinct product keys: **{r['recall']['distinct_product_keys']:,}** (>=5,000 required)
- Safety Recall normalized makes: **{r['recall']['distinct_normalized_makes']:,}**
- Safety Recall date support: **{r['recall']['distinct_date_years']} years**, parse rate **{r['recall']['date_parse_rate']:.4f}**
- exact normalized aggregate product-key intersection: **{r['aggregate_product_key_overlap']:,}** (>=1,000 required)

Identity fingerprints were frozen before any descendant outcome authorization:
- communication product keys: `{r['fingerprints']['communication_product_keys']}`
- recall product keys: `{r['fingerprints']['recall_product_keys']}`
- exact intersection: `{r['fingerprints']['intersection_product_keys']}`

## Frozen requirements that fail / 실패한 사전고정 요건

### 1. Frozen Manufacturer Communications CSV lacks a communication date field

Both frozen official ZIPs are readable and each contains a CSV with exactly these observed fields:

`TSB/Document ID, Make, Model, Model Year, Concise Summary`

The files therefore support deterministic document × product identity, but they expose neither `Mfr Communication Date` nor `Date Added to File`. Under the preregistered F01 contract, communication-time support was mandatory. Consequently:

- full frozen communication schema: **FAIL**
- communication date years: **0 / >=5 required**
- communication date parse rate: **0 / >=95% required**

The broader NHTSA dictionary documents richer fields, but F01 froze the CSV ZIPs before execution. Switching post hoc to a richer TSV/flat-file source would be a source redesign and is not permitted in this branch.

### 2. NHTSA catalog HTML returns HTTP 403 to the zero-cost GitHub runner

The frozen static NHTSA dictionaries and all three frozen ZIPs return HTTP 200, but the separately frozen NHTSA catalog page returns **HTTP 403** even with an ordinary unauthenticated browser User-Agent. The F01 PASS contract required the catalog page and dictionaries to be reachable from the runner, so that requirement also fails.

## Outcome-blind boundary / outcome 비개봉 경계

- recall incidence/rate/count by communication-derived group: **not opened**
- per-product future-recall membership conditional on communication history: **not opened**
- relationship/predictive statistic: **not computed**
- causal claim: **not made**
- unofficial mirror/authentication bypass: **not used**
- incremental monetary cost: **0 USD**

The aggregate 8,263-key source intersection is an identity-support count only; it is not a communication-conditioned recall outcome.

## Interpretation / 해석

This HOLD does **not** show that Manufacturer Communications are uninformative about recalls. It means the **specific prospectively frozen F01 source package** cannot satisfy its own time/schema/access contract. The branch is therefore terminal without switching sources after support was observed.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Do not rescue this branch by replacing the frozen CSVs with richer TSV/flat files. A future communication-time design is allowed only if a new independent portfolio decision prospectively selects the richer source family before its support is inspected.

Incremental monetary cost remains **0 USD**.
'''
    (OUT / "RESULT.md").write_text(result_md, encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nCorrected Run `{SOURCE_RUN}` validly resolves **`{GATE}`**. Product-key cardinality and aggregate exact overlap are strong, but the two prospectively frozen Manufacturer Communications CSV files lack any communication/addition date field and the frozen catalog HTML returns HTTP 403 to the zero-cost runner. The branch is terminal without switching post hoc to a richer TSV source. Recall incidence and relationship remain unopened.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_SOURCE_SCHEMA_GATE
status: active
---

# {CLAIM} — NHTSA product identity is large, but frozen F01 lacks communication-time schema

Corrected Run `{SOURCE_RUN}` establishes that the frozen NHTSA Manufacturer Communications CSVs contain **{r['communication']['distinct_product_keys']:,}** valid normalized product keys across **{r['communication']['distinct_normalized_makes']:,}** makes and intersect the frozen Safety Recall source on **{r['aggregate_product_key_overlap']:,}** exact normalized product keys. The recall source contains **{r['recall']['distinct_product_keys']:,}** product keys with **{r['recall']['distinct_date_years']}** date years and full date parse support.

However, both prospectively frozen communication CSVs expose only `TSB/Document ID, Make, Model, Model Year, Concise Summary` and no communication/addition date field. The runner-side NHTSA catalog HTML also returns HTTP 403. Therefore the frozen F01 result is **`{GATE}`**. No recall outcome conditioned on communications was opened.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-NHTSA-MC-F01
status: active
---

# {DECISION} — Finalize US-NHTSA-MC-F01 as source/schema HOLD

## Decision / 결정

Finalize US-NHTSA-MC-F01 at **`{GATE}`** and return to Stage 0.

## Rationale / 근거

The valid corrected execution shows strong deterministic product cardinality and overlap, but two preregistered PASS requirements fail: the frozen Manufacturer Communications CSVs lack a source-native communication/addition date field, and the frozen NHTSA catalog HTML is not reachable from the zero-cost GitHub runner (HTTP 403). These are contract-level source/schema failures, not evidence about the communication→recall relationship.

## Boundary / 경계

- Do not switch this branch post hoc to the richer TSV/flat source.
- Do not interpret the aggregate overlap as recall incidence or predictive evidence.
- A richer-source redesign requires a new independent prospective portfolio decision.
- Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | Corrected US-NHTSA-MC-F01 finds {r['communication']['distinct_product_keys']:,} communication product keys, {r['recall']['distinct_product_keys']:,} recall keys and {r['aggregate_product_key_overlap']:,} exact overlap, but frozen communication CSVs lack date fields and catalog HTML is runner-403; no communication-conditioned recall outcome opened. / NHTSA F01 product identity strong but frozen time/schema contract fails. | `OBSERVED/DERIVED` | `V3_OUTCOME_BLIND_SOURCE_SCHEMA_GATE` | Issue #143; Run `{SOURCE_RUN}`; `research/US-NHTSA-MC-F01/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Finalize US-NHTSA-MC-F01 as source/schema HOLD; no post-hoc TSV switch; return to Stage 0. / NHTSA F01을 source/schema HOLD로 종결. | Frozen communication CSVs have no date field; catalog HTML runner-403; product cardinality/overlap otherwise strong and outcomes unopened. | Issue #143; `{CLAIM}`; Run `{SOURCE_RUN}` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-US-NHTSA-MC-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 143
last_completed_research: US-NHTSA-MC-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-NHTSA-MC-F01 is terminal at **`{GATE}`** under corrected Run `{SOURCE_RUN}`, {DECISION} and {CLAIM}. Product-key support is large and exact aggregate overlap is strong, but the prospectively frozen Manufacturer Communications CSV files contain no communication/addition date field and the frozen NHTSA catalog HTML returns HTTP 403 to the zero-cost runner. No communication-conditioned recall outcome or relationship was opened.

## Exact next action / 정확한 다음 행동

Return to Stage 0 and open a new portfolio reselection. Do not rescue US-NHTSA-MC-F01 by switching to a richer TSV/flat source after observing this result. Any future NHTSA communication-time branch must be independently reselected and freeze the richer source before support is inspected.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")
    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-US-NHTSA-MC-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 143,
        "last_completed_research": "US-NHTSA-MC-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")
    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-NHTSA-MC-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 143
last_completed_research: US-NHTSA-MC-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- terminal gate: `{GATE}`
- source run: `{SOURCE_RUN}`
- communication product keys: `{r['communication']['distinct_product_keys']}`
- recall product keys: `{r['recall']['distinct_product_keys']}`
- exact aggregate product-key overlap: `{r['aggregate_product_key_overlap']}`
- frozen communication date field: absent
- NHTSA catalog from GitHub runner: HTTP 403
- communication-conditioned recall outcome: unopened
- relationship computed: false

## Exact restart point / 정확한 재개점

Open a new Stage-0 portfolio reselection. Incorporate the NHTSA finding that exact product identity/cardinality is strong but the frozen CSV source lacks time identity. Do not post-hoc switch this branch to TSV. Compare preserved/fresh candidates prospectively and authorize exactly one next outcome-blind gate.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE, "source_run": SOURCE_RUN}, sort_keys=True))


if __name__ == "__main__":
    main()
