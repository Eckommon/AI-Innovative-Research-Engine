#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "C-EU-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 139
DECISION = "DEC-192"
CLAIM = "CLM-177"
GATE = "HOLD_C_EU_F01_SOURCE_OR_IDENTITY"
STATE = "C_EU_F01_HOLD__PORTFOLIO_RETURN"
RUN_ID = os.environ.get("SOURCE_RUN_ID", "35039383396")


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
    assert cp["active_research"] == "C-EU-F01"
    assert cp["last_completed_issue"] == 138
    assert cp["last_decision"] == "DEC-191"

    staging = json.loads((OUT / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    assert staging["gate"] == GATE
    assert staging["industrial_outcome_or_thematic_magnitudes_opened"] is False
    assert staging["site_temperature_magnitudes_opened"] is False
    assert staging["relationship_computed"] is False
    assert staging["post_execution_rescue_used"] is False
    assert staging["incremental_monetary_cost_usd"] == 0
    assert staging["execution_correction"]["scientific_contract_changed"] is False
    assert staging["execution_correction"]["full_population_preserved"] is True

    eea = staging["eea"]
    era5 = staging["era5"]
    req = staging["requirements"]
    assert eea["queried_rows"] == eea["reported_layer_records"] == 854731
    assert eea["distinct_nonblank_site_ids"] == 97889
    assert eea["coordinate_qualified_site_ids"] == 59137
    assert eea["conflicting_site_ids"] == 38752
    assert eea["qualified_country_codes"] == 34
    assert req["coordinate_qualified_rate_ge_95pct"] is False
    assert req["conflicting_site_ids_zero"] is False
    assert req["distinct_site_ids_ge_10000"] is True
    assert req["qualified_country_codes_ge_25"] is True
    assert req["required_fields_and_point_geometry"] is True
    assert req["era5_semantics_confirmed"] is True
    assert era5["credential_blocked"] is True
    assert era5["unauthenticated_arco_metadata_access"] is False

    coord_pct = eea["coordinate_qualified_rate"] * 100

    result = f'''---
id: C-EU-F01-RESULT
type: outcome-blind-source-access-identity-feasibility
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_HOLD
gate: {GATE}
industrial_outcomes_opened: false
temperature_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# C-EU-F01 Result — terminal HOLD

**`{GATE}`**

Corrected Run `{RUN_ID}` executed the preregistered EEA industrial-site × ERA5-Land 2m-temperature structural/access gate after Run `35010687544` had timed out during serial deep-offset pagination. The correction changed only transport execution: the same complete EEA population and the same allowed identity/coordinate fields were retrieved by bounded concurrent OBJECTID batches. No scientific threshold, source, identity rule, hazard family or disposition changed.

## Frozen-gate evidence / 고정 게이트 근거

- EEA layer records fully retrieved: **854,731 / 854,731**
- distinct exact nonblank `InspireSiteId`: **97,889**
- coordinate-qualified exact site IDs under the frozen no-conflict rule: **59,137**
- coordinate-qualified share: **{coord_pct:.4f}% / 95% required**
- exact site IDs with >1 distinct valid coordinate pair: **38,752 / 0 required**
- coordinate-qualified country codes: **34 / 25 required**
- required fields and point geometry: **PASS**
- ERA5-Land 2m-temperature semantics: **PASS**
- unauthenticated official ARCO metadata probe: **HTTP 401 / credential blocked**

The decisive failure is not the CDS credential. Requirements 4 and 6 already fail at the EEA identity layer. Therefore the frozen PARTIAL disposition does not apply: PARTIAL was allowed only when EEA requirements 1–7 and 10 passed and the sole blocker was the free CDS credential.

## Interpretation / 해석

The current historical EEA site-map layer is not compatible with the preregistered assumption that one exact `InspireSiteId` has one invariant coordinate pair across all reporting records. Under the frozen rule, **38,752** site IDs have multiple distinct valid coordinate pairs, so only **59,137 / 97,889 = {coord_pct:.4f}%** remain coordinate-qualified. No coordinate tolerance, latest-year selection, canonical-year rule, geometry clustering or name-based repair may be introduced after observing this support.

This is a **source/identity-design HOLD**, not evidence about heat exposure, industrial vulnerability, emissions, performance, prediction or causality.

## Outcome-blind boundary / outcome 비개봉 경계

- pollutant/release/waste/energy/production magnitudes: **not opened**
- site temperature magnitudes: **not opened**
- temperature→industrial relationship: **not computed**
- fuzzy site-name repair: **not used**
- unofficial mirror/authentication bypass: **not used**
- post-execution rescue: **not used**
- incremental monetary cost: **0 USD**

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio selection. Do not rescue C-EU-F01 by adding a coordinate tolerance or choosing a reporting year post hoc. A future C-EU redesign is allowed only if independently selected by a later portfolio decision and prospectively freezes a reporting-year/coordinate-lineage rule before support is re-opened.
'''
    (OUT / "RESULT.md").write_text(result, encoding="utf-8")
    (OUT / "RESULT.json").write_text(json.dumps({
        "research_id": "C-EU-F01",
        "issue": ISSUE,
        "gate": GATE,
        "source_run": int(RUN_ID),
        "eea_records": eea["queried_rows"],
        "distinct_site_ids": eea["distinct_nonblank_site_ids"],
        "coordinate_qualified_site_ids": eea["coordinate_qualified_site_ids"],
        "coordinate_qualified_rate": eea["coordinate_qualified_rate"],
        "conflicting_site_ids": eea["conflicting_site_ids"],
        "qualified_country_codes": eea["qualified_country_codes"],
        "era5_semantic_pass": era5["semantic_pass"],
        "credential_blocked": era5["credential_blocked"],
        "industrial_outcomes_opened": False,
        "temperature_magnitudes_opened": False,
        "relationship_computed": False,
        "incremental_monetary_cost_usd": 0,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    readme_path = OUT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nCorrected Run `{RUN_ID}` terminates C-EU-F01 at **`{GATE}`**. The complete EEA population was retrieved, but **38,752** exact `InspireSiteId` values have multiple distinct valid coordinate pairs and only **{coord_pct:.4f}%** of exact site IDs satisfy the frozen invariant-coordinate rule versus **95% required**. ERA5 semantics passed and the unauthenticated ARCO probe returned 401, but credential access is not the sole blocker, so the frozen PARTIAL disposition does not apply. No industrial outcome or temperature magnitude was opened and no relationship was computed.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V3_OUTCOME_BLIND_IDENTITY_GATE
status: active
---

# {CLAIM} — C-EU-F01 exact-site identity HOLD

Corrected Run `{RUN_ID}` retrieved the full **854,731-record** EEA site-map population using only frozen identity/support fields. It found **97,889** exact nonblank `InspireSiteId` identities, of which **59,137 ({coord_pct:.4f}%)** satisfy the preregistered invariant-coordinate rule; **38,752** exact site IDs contain more than one distinct valid coordinate pair. The frozen requirements were >=95% coordinate-qualified and zero conflicts, so C-EU-F01 terminates at **`{GATE}`**.

ERA5-Land 2m-temperature semantics were confirmed and the unauthenticated ARCO metadata probe returned HTTP 401, but credential access is not the sole blocker. Industrial outcome/thematic magnitudes and site temperature magnitudes were never opened and no relationship was computed.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: C-EU-F01
status: active
---

# {DECISION} — Finalize C-EU-F01 as source/identity HOLD

## Decision / 결정

Finalize C-EU-F01 at **`{GATE}`** and return to Stage 0 portfolio selection. Do not add coordinate tolerance, latest-year selection, coordinate clustering or site-name repair inside C-EU-F01.

## Rationale / 근거

The corrected full-population execution preserves the preregistered contract and shows that **38,752** exact site IDs have multiple distinct valid coordinate pairs; only **{coord_pct:.4f}%** satisfy the invariant-coordinate rule versus the frozen **95%** requirement. Because EEA identity requirements already fail, the CDS-credential-only PARTIAL disposition is not available.

## Boundary / 경계

- This HOLD is about source/identity design only.
- It establishes no heat, vulnerability, emissions, performance, predictive or causal relationship.
- No industrial outcome or site-temperature magnitude was opened.
- A future C-EU redesign requires a new independent portfolio selection and prospective coordinate/reporting-year rule.
- Incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | C-EU-F01 full-population identity gate: 97,889 exact site IDs, 59,137 ({coord_pct:.4f}%) invariant-coordinate qualified, 38,752 coordinate conflicts; frozen 95%/zero-conflict gate fails, outcomes unopened. / C-EU-F01 exact-site identity gate HOLD. | `OBSERVED/DERIVED` | `V3_OUTCOME_BLIND_IDENTITY_GATE` | Issue #139; Run `{RUN_ID}`; `research/C-EU-F01/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Finalize C-EU-F01 as `HOLD_C_EU_F01_SOURCE_OR_IDENTITY`; no post-hoc coordinate/year rescue; return to Stage 0. / C-EU-F01을 source/identity HOLD로 종결하고 사후 좌표·연도 구제를 금지. | Frozen identity requirements 4 and 6 fail on the complete EEA population; CDS credential is not the sole blocker. | Issue #139; `{CLAIM}`; Run `{RUN_ID}` | active |\n")

    status = f'''---
checkpoint_id: CHK-20260916-C-EU-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 139
last_completed_research: C-EU-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

C-EU-F01 is terminal at **`{GATE}`** under corrected Run `{RUN_ID}`, {DECISION} and {CLAIM}. The full EEA identity population was retrieved, but the frozen invariant-coordinate identity requirements fail. Industrial outcome/thematic magnitudes and site temperature magnitudes remained closed and no relationship was computed.

## Terminal evidence / 종결 근거

- exact site IDs: **97,889**
- coordinate-qualified exact IDs: **59,137 ({coord_pct:.4f}%) / 95% required**
- conflicting exact site IDs: **38,752 / 0 required**
- coordinate-qualified countries: **34 / 25 required**
- ERA5 semantic route: **PASS**
- unauthenticated ARCO metadata: **HTTP 401**

## Exact next action / 정확한 다음 행동

Return to Stage 0 and open a new portfolio reselection only. Re-score surviving or newly discovered candidates using marginal information from terminal US-MINE-N01, US-UTIL-N01 and C-EU-F01. Do not automatically promote US-PIPE and do not redesign C-EU-F01 post hoc.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / "STATUS.md").write_text(status, encoding="utf-8")

    (CTX / "checkpoint.json").write_text(json.dumps({
        "checkpoint_id": "CHK-20260916-C-EU-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 139,
        "last_completed_research": "C-EU-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }, indent=2) + "\n", encoding="utf-8")

    handoff = f'''---
checkpoint_id: CHK-20260916-C-EU-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 139
last_completed_research: C-EU-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- terminal gate: `{GATE}`
- source run: `{RUN_ID}`
- exact site IDs: `97889`
- invariant-coordinate qualified: `59137` ({coord_pct:.4f}%)
- coordinate-conflict site IDs: `38752`
- industrial outcomes opened: `false`
- site temperature magnitudes opened: `false`
- relationship computed: `false`

## Exact restart point / 정확한 재개점

Open a new Stage-0 portfolio reselection. Incorporate the terminal information from US-MINE-N01, US-UTIL-N01 and C-EU-F01. Do not automatically promote US-PIPE and do not rescue C-EU-F01 with a post-hoc coordinate tolerance, reporting-year choice or fuzzy identity rule.

Incremental monetary cost remains **0 USD**.
'''
    (CTX / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE, "source_run": RUN_ID}, sort_keys=True))


if __name__ == "__main__":
    main()
