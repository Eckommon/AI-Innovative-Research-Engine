#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATE='2026-09-12'
status_path=ROOT/'STATUS.md'
handoff_path=ROOT/'context'/'SESSION_HANDOFF.md'
checkpoint_path=ROOT/'context'/'checkpoint.json'
claim_ledger_path=ROOT/'registry'/'CLAIM_LEDGER.md'
decision_log_path=ROOT/'registry'/'DECISION_LOG.md'
claim_path=ROOT/'registry'/'CLM-156.md'
dec_path=ROOT/'registry'/'DEC-159.md'
research=ROOT/'research'/'US-WW-F01'
readme_path=research/'README.md'
result_path=research/'RESULT.md'

status=status_path.read_text(encoding='utf-8')
assert 'active_issue: 114' in status
assert 'active_research: US-WW-F01' in status
assert 'last_decision: DEC-158' in status
assert not claim_path.exists() and not dec_path.exists() and not result_path.exists()

cwns=json.loads((research/'CWNS_IDENTITY_MANIFEST.json').read_text(encoding='utf-8'))
echo=json.loads((research/'ECHO_JOIN_MANIFEST.json').read_text(encoding='utf-8'))
assert cwns['probe_revision']==2
assert cwns['wastewater_with_official_npdes_linkage']>=3000
assert cwns['npdes_linked_state_count']>=30
assert cwns['pass_threshold_3000_facilities'] is True
assert cwns['pass_threshold_30_states'] is True
assert cwns['need_dollar_magnitudes_read'] is False
assert echo['exact_match']['pass_80pct_on_permit_route'] is True
assert echo['exact_match']['permit_route_coverage']>=0.80
assert echo['compliance_identity']['post_2022_date_and_type_identity_available'] is True
assert echo['no_fuzzy_matching'] is True
assert echo['candidate_outcome_magnitudes_opened'] is False

linked=cwns['wastewater_with_official_npdes_linkage']
states=cwns['npdes_linked_state_count']
ids=cwns['distinct_official_npdes_ids']
matches=echo['exact_match']['permit_route_matches']
coverage=echo['exact_match']['permit_route_coverage']

result_path.write_text(f'''---
id: US-WW-F01-RESULT
type: outcome-blind-source-join-feasibility
created: {DATE}
issue: 114
gate: PASS_US_WW_F01_CWNS_NPDES_JOIN_READY
relationship_computed: false
need_dollar_magnitudes_read: false
candidate_outcome_magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WW-F01 Result

**`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`**

The preregistered source/schema/identity/cardinality gate passes without opening infrastructure-need dollar magnitudes or candidate compliance outcomes.

## Frozen gate evidence

- EPA 2022 CWNS nationwide CSV ZIP is reproducibly downloadable through the official no-auth download UI at 0 USD.
- CWNS contains deterministic `CWNS_ID`, `FACILITY_ID`, `STATE_CODE`, infrastructure/facility-type identities, `FACILITY_PERMIT` linkage and explicit need-category identities.
- Restricting to `INFRASTRUCTURE_TYPE = Wastewater` and `PERMIT_SOURCE = NPDES` yields **{linked:,}** CWNS wastewater facilities with official NPDES linkage across **{states}** state/territory codes and **{ids:,}** distinct official NPDES permit IDs.
- The preregistered cardinality requirements (>=3,000 linked facilities; >=30 states) both pass.
- In the official ECHO/ICIS-NPDES national identity package, **{matches:,} / {echo['cwns_official_npdes_ids']:,} = {coverage*100:.4f}%** of the CWNS official NPDES IDs exact-match `ICIS_PERMITS`; the >=80% requirement passes.
- `ICIS_FACILITIES` independently supports {echo['exact_match']['facility_route_coverage']*100:.4f}% exact coverage.
- `NPDES_PS_VIOLATIONS`, `NPDES_CS_VIOLATIONS`, and `NPDES_SE_VIOLATIONS` expose deterministic `NPDES_ID`, violation type/code/description and post-2022 date identities.
- CWNS need-category semantics prospectively identify wet-weather/conveyance-relevant categories including `III-A Infiltration/Inflow (I/I) Correction`, `III-B Sewer Replacement/Rehabilitation`, and `V Combined Sewer Overflow (CSO) Correction` without reading `BASE_AMOUNT` or `OFFICIAL_AMOUNT`.
- No facility-name/address fuzzy matching was used. Raw source bytes were transient and were not persisted.

## Claim boundary

This PASS establishes **join/design feasibility only**. It is not evidence that 2022 infrastructure needs predict later NPDES violations, does not establish causality or novelty, and does not authorize any relationship/effect test.

## Exact next action

Return to Stage 0. Compare a separately preregistered US-WW descendant design against independent alternatives. If US-WW advances, first freeze exposure-category identities, future compliance identity, pre-existing-compliance leakage controls, temporal window, comparator, model and inferential gate **before opening any future compliance outcome counts/rates**.

Incremental monetary cost: **0 USD**.
''',encoding='utf-8')

claim_path.write_text(f'''---
id: CLM-156
type: claim
created: {DATE}
issue: 114
status: active
---

# CLM-156 — 2022 CWNS wastewater facilities have a high-coverage deterministic official NPDES bridge into ICIS-NPDES compliance identities

Under the outcome-blind US-WW-F01 contract, **{linked:,}** CWNS wastewater facilities carry official `PERMIT_SOURCE=NPDES` linkage across **{states}** jurisdictions, producing **{ids:,}** distinct official NPDES IDs. Of the **{echo['cwns_official_npdes_ids']:,}** frozen IDs, **{matches:,} ({coverage*100:.4f}%)** exact-match the official ECHO `ICIS_PERMITS` identity route, and post-2022 violation date/type identities are structurally available.

This is a source/schema/identity/cardinality feasibility claim only. No needs-dollar amount, candidate compliance magnitude, relationship, predictive effect, causal effect or novelty claim is established. Cost: **0 USD**.
''',encoding='utf-8')

dec_path.write_text(f'''---
id: DEC-159
type: decision
created: {DATE}
issue: 114
status: accepted
---

# DEC-159 — Finalize US-WW-F01 as PASS and return to Stage 0

Finalize Issue #114 at **`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`**. The frozen cardinality and exact-match thresholds all pass: {linked:,} officially NPDES-linked wastewater facilities, {states} jurisdictions, and {coverage*100:.4f}% exact `ICIS_PERMITS` coverage.

Do **not** authorize a relationship/effect test from this PASS. Return to Stage 0 and require a separate preregistration that explicitly controls pre-existing-compliance leakage/reverse-direction risk before any future compliance outcome magnitude is opened. Cost remains **0 USD**.
''',encoding='utf-8')

readme=readme_path.read_text(encoding='utf-8')
readme=readme.replace('state: ACTIVE_SOURCE_JOIN_FEASIBILITY','state: COMPLETED_PASS')
readme += '\n## Terminal disposition / 최종 판정\n\n**`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`** — See `RESULT.md`, `CLM-156`, and `DEC-159`. PASS is feasibility only; no effect test is authorized.\n'
readme_path.write_text(readme,encoding='utf-8')

claim_ledger=claim_ledger_path.read_text(encoding='utf-8')
assert '`CLM-156`' not in claim_ledger
claim_ledger_path.write_text(claim_ledger.rstrip()+f'''\n\n| `CLM-156` | US-WW-F01 establishes a deterministic national 2022 CWNS wastewater → official NPDES → ICIS-NPDES identity bridge: {linked:,} linked wastewater facilities across {states} jurisdictions and {matches:,}/{echo['cwns_official_npdes_ids']:,} ({coverage*100:.4f}%) exact `ICIS_PERMITS` coverage, without opening needs dollars or compliance outcomes. / CWNS→NPDES→ICIS 식별 bridge가 값 비사용으로 확립된다. | `OBSERVED/DERIVED` | `V3_REPRODUCED` | Runs `34692901199`, `34693017748`, `34693082010`; `research/US-WW-F01/` | {DATE} | active |\n''',encoding='utf-8')

decision_log=decision_log_path.read_text(encoding='utf-8')
assert '`DEC-159`' not in decision_log
decision_log_path.write_text(decision_log.rstrip()+f'''\n\n| `DEC-159` | {DATE} | Finalize US-WW-F01 at `PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`; return to Stage 0 without authorizing an effect test. / US-WW-F01 PASS 종결 후 Stage 0 복귀. | {linked:,} official-NPDES-linked wastewater facilities, {states} jurisdictions and {coverage*100:.4f}% exact ICIS permit coverage satisfy the preregistered source/join gate; predictive/causal evidence remains unopened. | Issue #114; `CLM-156`; `research/US-WW-F01/RESULT.md` | active |\n''',encoding='utf-8')

status_path.write_text(f'''---
checkpoint_id: CHK-20260912-US-WW-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 114
last_completed_research: US-WW-F01
last_decision: DEC-159
updated: {DATE}
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_WW_F01_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

US-WW-F01 completed outcome-blind at **`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`**. The official 2022 CWNS national route yields {linked:,} wastewater facilities with official NPDES linkage across {states} jurisdictions; {matches:,}/{echo['cwns_official_npdes_ids']:,} ({coverage*100:.4f}%) frozen IDs exact-match `ICIS_PERMITS`. Post-2022 violation date/type identities are structurally available. No needs-dollar or candidate compliance magnitude was opened and no relationship was computed.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio/design control. Re-evaluate a separately preregistered US-WW descendant against independent alternatives. Do not open future compliance outcomes until exposure identities, temporal window, comparator, pre-existing-compliance leakage controls, model and inferential gate are frozen in a new authorization.

Incremental monetary cost remains **0 USD**.
''',encoding='utf-8')

handoff_path.write_text(f'''---
checkpoint_id: CHK-20260912-US-WW-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 114
last_completed_research: US-WW-F01
last_decision: DEC-159
updated: {DATE}
---

# Session Handoff / 세션 인수인계

US-WW-F01 / Issue #114 is terminal **PASS** at `PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`.

Verified outcome-blind structure: {linked:,} CWNS wastewater facilities with official NPDES linkage across {states} jurisdictions, {ids:,} distinct official NPDES IDs, and {coverage*100:.4f}% exact `ICIS_PERMITS` coverage. Post-2022 compliance violation date/type identities exist. No needs-dollar/compliance outcome magnitude or relationship was opened.

Exact restart: Stage 0 portfolio/design control. A US-WW descendant, if selected, must use a new preregistration and explicitly address pre-existing-compliance leakage/reverse-direction risk before any future compliance outcome count/rate is opened. Cost: **0 USD**.
''',encoding='utf-8')

checkpoint_path.write_text(json.dumps({'checkpoint_id':'CHK-20260912-US-WW-F01-PASS-PORTFOLIO-RETURN','active_issue':None,'active_research':'NONE','last_completed_issue':114,'last_completed_research':'US-WW-F01','last_decision':'DEC-159','updated':DATE},indent=2)+'\n',encoding='utf-8')

print(json.dumps({'gate':'PASS_US_WW_F01_CWNS_NPDES_JOIN_READY','linked_facilities':linked,'jurisdictions':states,'exact_matches':matches,'coverage':coverage,'cost_usd':0}))
