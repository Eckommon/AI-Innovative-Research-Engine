#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "US-FTA-TRANSIT-F01"
REG = ROOT / "registry"
CTX = ROOT / "context"
ISSUE = 147
RUN = 35063556654
STAGING_COMMIT = "de03e3e01b8b516e17ebb4baa1ef047a707d1a9c"
DECISION = "DEC-207"
CLAIM = "CLM-185"
GATE = "PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY"
STATE = "US_FTA_TRANSIT_F01_PASS__N01_AUTHORIZATION_REQUIRED"


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
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-F01-ACTIVE",
        "active_issue": ISSUE,
        "active_research": "US-FTA-TRANSIT-F01",
        "last_completed_issue": 146,
        "last_completed_research": "PORTFOLIO-R33",
        "last_decision": "DEC-206",
        "updated": "2026-09-16",
    }

    s = json.loads((RESEARCH / "STAGING_RESULT.json").read_text(encoding="utf-8"))
    assert s["protocol"] == "US-FTA-TRANSIT-F01"
    assert s["issue"] == ISSUE
    assert s["contract_commit"] == "70c41fc8202579436ad7560118548fc1c2a34593"
    assert s["valid_evaluation"] is True
    assert s["disposition"] == GATE
    assert all(v["pass"] for v in s["checks"].values())
    assert set(s["checks"]) == {str(i) for i in range(1, 20)}
    b = s["boundaries"]
    for k in [
        "agency_name_repair_used",
        "manual_or_fuzzy_identity_repair_used",
        "breakdown_conditioned_major_safety_event_occurrence_opened",
        "row_level_breakdown_event_join_persisted",
        "relationship_computed",
        "predictive_metric_computed",
        "causal_claim_made",
    ]:
        assert b[k] is False, (k, b[k])
    assert s["incremental_monetary_cost_usd"] == 0

    d = s["structural_diagnostics"]
    bd = d["breakdowns"]
    mm = d["monthly_modal"]
    me = d["major_safety_events"]
    cross = d["cross_source"]

    (RESEARCH / "RESULT.md").write_text(f'''---
id: US-FTA-TRANSIT-F01-RESULT
type: outcome-blind-source-schema-agency-mode-time-feasibility
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_PASS
gate: {GATE}
source_run: {RUN}
staging_commit: {STAGING_COMMIT}
breakdown_conditioned_major_safety_event_occurrence_opened: false
row_level_breakdown_event_join_persisted: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-FTA-TRANSIT-F01 Result — agency-mode/time join-ready PASS

**`{GATE}`**

Run `{RUN}` validly executed the frozen official-source FTA/NTD feasibility contract. All **19/19** preregistered requirements passed. This establishes source/schema/identity/time feasibility only; it does not establish that mechanical breakdowns predict or are associated with Major Safety Events.

## Empirical structural support / 구조적 실증 지원

### Breakdowns (`amkt-4ehs`)

- rows read: **{s['source_evidence']['breakdowns']['rows_read']:,}**
- supported report years: **{', '.join(map(str, bd['distinct_years']))}**
- valid exact `NTD ID × mode × TOS × year` keys: **{bd['valid_source_grain_keys']:,}**
- duplicate source-grain rows: **{bd['duplicate_source_grain_rows']:,}**
- conflicting duplicate keys: **{bd['conflicting_duplicate_source_grain_keys']:,}**
- nonnumeric mechanical rows: **{bd['non_numeric_mechanical_rows']:,}**
- distinct `NTD ID × mode` pairs: **{bd['distinct_ntd_id_mode_pairs']:,}**
- pairs represented in >=2 Breakdown years: **{bd['pairs_in_at_least_two_breakdown_years']:,}**

### Monthly Modal (`5ti2-5uiv`)

- rows read: **{s['source_evidence']['monthly_modal']['rows_read']:,}**
- supported years: **{mm['year_min']}–{mm['year_max']}**
- distinct calendar periods: **{mm['distinct_calendar_periods']:,}**
- distinct `NTD ID × mode` pairs: **{mm['distinct_ntd_id_mode_pairs']:,}**
- Breakdowns pairs represented in Monthly: **{cross['breakdowns_pairs_in_monthly']:,} / {bd['distinct_ntd_id_mode_pairs']:,} = {cross['breakdowns_pair_monthly_coverage']:.4%}**

Monthly duplicate structural rows are expected to be non-unique at the reduced `NTD ID × mode × year × month` projection because the source can contain additional scope dimensions. N01 must prospectively freeze the exact service-denominator aggregation semantics before using any service measure; F01 does not infer those semantics post hoc.

### Major Safety Events (`9ivb-8ae9`)

- structural-only rows read: **{s['source_evidence']['major_safety_events']['rows_read']:,}**
- supported years: **{me['year_min']}–{me['year_max']}** across **{me['distinct_years']}** distinct years
- distinct calendar periods: **{me['distinct_calendar_periods']:,}**
- distinct `NTD ID × mode` pairs: **{me['distinct_ntd_id_mode_pairs']:,}**
- exact aggregate Breakdowns∩Major pair overlap: **{cross['breakdowns_pairs_in_major_events']:,}**

Only `NTD ID`, mode and incident-time structural fields were requested from the Major Safety Events source. Event type, severity, casualty, agency-mode event count/rate and Breakdown-conditioned occurrence were not used for F01.

## Deterministic identity fingerprints / identity 지문

- Breakdowns pairs: `{s['fingerprints']['breakdowns_ntd_id_mode_pairs_sha256']}`
- Monthly pairs: `{s['fingerprints']['monthly_modal_ntd_id_mode_pairs_sha256']}`
- Major-event pairs: `{s['fingerprints']['major_safety_events_ntd_id_mode_pairs_sha256']}`
- Breakdowns∩Monthly: `{s['fingerprints']['breakdowns_intersect_monthly_pairs_sha256']}`
- Breakdowns∩Major: `{s['fingerprints']['breakdowns_intersect_major_events_pairs_sha256']}`

## Outcome-blind boundary / 결과 비개봉 경계

- agency-name/address/manual/fuzzy identity repair: **not used**;
- Breakdown-conditioned Major Safety Event occurrence/rate/count: **not opened**;
- row-level Breakdown→event membership: **not persisted**;
- relationship/predictive statistic: **not computed**;
- causal or transit-agency safety-rating claim: **not made**;
- unofficial mirror/authentication bypass: **not used**;
- incremental monetary cost: **0 USD**.

## Interpretation / 해석

This PASS establishes that the selected official FTA/NTD source family is sufficiently large, repeated, source-native and structurally overlapping to support a **separate outcome-blind design-identifiability gate**. It does not authorize opening Major Safety Event outcome values directly from F01.

## Exact next action / 정확한 다음 행동

Open and preregister a separate `US-FTA-TRANSIT-N01` before any Breakdown-conditioned Major Safety Event outcome is opened. N01 must prospectively freeze the exposure measure, service-denominator aggregation, time ordering, eligible agency-mode-year units, missingness/exclusion rules and the exact future E01 statistical contract while keeping safety-event outcome values closed.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    readme_path = RESEARCH / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "## Terminal F01 result / F01 최종 결과" not in readme:
        readme += f'''\n\n## Terminal F01 result / F01 최종 결과\n\n**`{GATE}`** — all 19 frozen requirements passed in Run `{RUN}`. See `RESULT.md`. Breakdown-conditioned Major Safety Event outcomes remain unopened. A separate N01 is required before any outcome gate.\n'''
        readme_path.write_text(readme, encoding="utf-8")

    (REG / f"{CLAIM}.md").write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_FEASIBILITY
status: active
---

# {CLAIM} — FTA/NTD Breakdown × Major Safety agency-mode/time panel is structurally join-ready

Run `{RUN}` passes all 19 preregistered `US-FTA-TRANSIT-F01` requirements using only the frozen official DOT/FTA datasets. Breakdowns contains **{bd['distinct_ntd_id_mode_pairs']:,}** distinct source-native `NTD ID × mode` pairs and **{bd['pairs_in_at_least_two_breakdown_years']:,}** pairs represented in at least two Breakdown years. **{cross['breakdowns_pairs_in_monthly']:,}/{bd['distinct_ntd_id_mode_pairs']:,} ({cross['breakdowns_pair_monthly_coverage']:.4%})** are represented in Monthly Modal and **{cross['breakdowns_pairs_in_major_events']:,}** occur in the exact aggregate Breakdowns∩Major-event pair intersection.

This is a structural feasibility claim only. Breakdown-conditioned safety occurrence, relationship, prediction, agency ranking and causality remain untested and unopened.
''', encoding="utf-8")

    (REG / f"{DECISION}.md").write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: US-FTA-TRANSIT-F01
status: active
---

# {DECISION} — Accept US-FTA-TRANSIT-F01 PASS and require separate N01

## Decision / 결정

Accept immutable staging commit `{STAGING_COMMIT}` from Run `{RUN}` as `PASS_US_FTA_TRANSIT_F01_AGENCY_MODE_TIME_JOIN_READY` and close Issue #{ISSUE} as completed.

The PASS authorizes only a separately preregistered outcome-blind `US-FTA-TRANSIT-N01` design-identifiability gate. It does not authorize direct opening of Breakdown-conditioned Major Safety Event outcomes.

## Boundary / 경계

- no post-hoc source/identity/TOS/time rescue;
- no agency-name/fuzzy/manual join repair;
- no safety-event count/rate/severity conditioned on Breakdowns;
- no relationship, prediction, safety ranking or causal claim;
- incremental monetary cost remains 0 USD.
''', encoding="utf-8")

    append_once(REG / "CLAIM_LEDGER.md", f"`{CLAIM}`", f"| `{CLAIM}` | US-FTA-TRANSIT-F01 passes all 19 frozen requirements: 1,199 Breakdowns agency-mode pairs, 1,131 repeated >=2 years, 97.3311% Monthly structural coverage, 968 exact Breakdowns∩Major pair overlap; outcomes unopened. / FTA/NTD 구조 join-ready PASS. | `DERIVED` | `V2_PRIMARY_VERIFIED_FEASIBILITY` | Issue #147; Run {RUN}; `research/US-FTA-TRANSIT-F01/RESULT.md` | 2026-09-16 | active |\n")
    append_once(REG / "DECISION_LOG.md", f"`{DECISION}`", f"| `{DECISION}` | 2026-09-16 | Accept US-FTA-TRANSIT-F01 PASS; require separate outcome-blind N01 before opening safety outcomes. / F01 PASS 수용 후 N01 별도 사전등록 요구. | Immutable staging `{STAGING_COMMIT}`; Run {RUN}; 19/19 PASS; outcome boundary preserved. | Issue #147; `{CLAIM}`; `research/US-FTA-TRANSIT-F01/RESULT.md` | active |\n")

    (ROOT / "STATUS.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 147
last_completed_research: US-FTA-TRANSIT-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FTA-TRANSIT-F01 is terminal at **`{GATE}`** under {DECISION} / {CLAIM}. All 19 frozen requirements passed in Run `{RUN}`. Structural support: **1,199** Breakdowns agency-mode pairs; **1,131** repeated in >=2 years; **97.3311%** represented in Monthly Modal; **968** exact Breakdowns∩Major-event pair overlap. Breakdown-conditioned Major Safety Event outcomes remain unopened.

## Exact next action / 정확한 다음 행동

Freeze a separate `US-FTA-TRANSIT-N01` design-identifiability contract **before opening its Issue and before reading any Breakdown-conditioned Major Safety Event outcome**. Prospectively define exposure normalization, service-denominator aggregation, time ordering, eligibility/missingness rules and the exact future E01 analysis contract.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    checkpoint = {
        "checkpoint_id": "CHK-20260916-US-FTA-TRANSIT-F01-TERMINAL",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": ISSUE,
        "last_completed_research": "US-FTA-TRANSIT-F01",
        "last_decision": DECISION,
        "updated": "2026-09-16",
    }
    (CTX / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

    (CTX / "SESSION_HANDOFF.md").write_text(f'''---
checkpoint_id: CHK-20260916-US-FTA-TRANSIT-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 147
last_completed_research: US-FTA-TRANSIT-F01
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- F01 gate: `{GATE}`
- source run: `{RUN}`
- immutable staging commit: `{STAGING_COMMIT}`
- Breakdowns pairs: 1,199
- repeated >=2 years: 1,131
- Monthly coverage: 97.3311%
- Breakdowns∩Major pair overlap: 968
- Breakdown-conditioned Major Safety outcome opened: false
- row-level Breakdown→event join persisted: false
- relationship/prediction/causality: false
- cost: 0 USD

## Exact restart point / 정확한 재개점

Freeze `US-FTA-TRANSIT-N01` before Issue binding. N01 must establish a deterministic exposure/design manifest without reading safety-event outcome values, and must prospectively freeze any later E01 contract.
''', encoding="utf-8")

    print(json.dumps({"gate": GATE, "decision": DECISION, "claim": CLAIM, "state": STATE}, sort_keys=True))


if __name__ == "__main__":
    main()
