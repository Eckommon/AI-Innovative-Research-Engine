#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'research'/'US-EPA-XMEDIA-N01'
REG=ROOT/'registry'; CTX=ROOT/'context'
ISSUE=151; RUN=35167553702; STAGING_COMMIT='78f0f0f1458463c79c326c016d415dc5533af026'
DECISION='DEC-215'; CLAIM='CLM-189'
GATE='PASS_US_EPA_XMEDIA_N01_MATCHED_MONITORING_INTENSITY_DESIGN_IDENTIFIABLE'
STATE='US_EPA_XMEDIA_N01_PASS__E01_AUTHORIZATION_REQUIRED'

def append_once(path, marker, row):
    t=path.read_text(encoding='utf-8')
    if marker not in t:
        if not t.endswith('\n'): t+='\n'
        path.write_text(t+row,encoding='utf-8')

def main():
    cp=json.loads((CTX/'checkpoint.json').read_text())
    assert cp=={'checkpoint_id':'CHK-20260917-US-EPA-XMEDIA-N01-ACTIVE','active_issue':151,'active_research':'US-EPA-XMEDIA-N01','last_completed_issue':150,'last_completed_research':'US-EPA-XMEDIA-F01','last_decision':'DEC-214','updated':'2026-09-17'}
    s=json.loads((RESEARCH/'STAGING_RESULT.json').read_text())
    m=json.loads((RESEARCH/'DESIGN_MANIFEST.json').read_text())
    assert s['gate']==GATE and s['requirements_passed']==18 and s['requirements_total']==18
    assert all(r['pass'] for r in s['requirements'])
    assert m['canonical_core_sha256']==s['diagnostics']['manifest_sha256']
    assert len(m['pairs'])==s['diagnostics']['matched_pairs']==307
    assert m['outcome_membership_included'] is False
    for v in s['boundaries'].values(): assert v is False
    assert s['incremental_monetary_cost_usd']==0
    d=s['diagnostics']
    (RESEARCH/'RESULT.md').write_text(f'''---
id: US-EPA-XMEDIA-N01-RESULT
type: outcome-blind-matched-design-identifiability
created: 2026-09-17
issue: {ISSUE}
state: COMPLETED_PASS
gate: {GATE}
source_run: {RUN}
staging_commit: {STAGING_COMMIT}
future_outcome_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-N01 Result — matched monitoring-intensity design PASS

**`{GATE}`**

Immutable Run `{RUN}` executed the pre-Issue contract frozen at `12f30d5d27d7d4f27022bc355c2a0c62a76e9f0c`. All **18/18** requirements passed without opening any future NPDES or RCRA outcome.

## Frozen design support / 고정 설계 지원

- exact FRS cross-program Registry IDs: **{d['frs_exact_cross_program_registry_ids']:,}**
- exact one-to-one RCRAInfo↔NPDES Registry IDs: **{d['frs_exact_one_to_one_registry_ids']:,}**
- structurally eligible Registry IDs: **{d['eligible_registry_ids']:,}**
- all structural strata: **{d['all_structural_strata']:,}**
- strict-separation strata: **{d['strict_separation_strata']:,}**
- matched HIGH–LOW pairs: **{d['matched_pairs']:,}**
- matched states: **{d['matched_state_count']}**
- baseline-evaluation-count balance within `[1/3,3]`: **{d['baseline_ratio_within_1_3_to_3_rate']:.2%}**
- permit-age difference <=10 years: **{d['permit_age_difference_within_10y_rate']:.2%}**
- deterministic manifest SHA-256: `{d['manifest_sha256']}`

The final design contains one facility at most once and every pair satisfies `HIGH exposure_eval_count > LOW exposure_eval_count`.

## Outcome firewall / 결과 방화벽

- NPDES effluent-violation rows: **not opened**;
- DMR outcomes: **not opened**;
- RCRA violation/enforcement outcomes: **not opened**;
- 2024 future outcome membership: **not opened**;
- relationship/prediction/causality: **not computed**;
- identity repair: **not used**;
- cost: **0 USD**.

## Exact next action / 정확한 다음 행동

A separate `US-EPA-XMEDIA-E01` authorization may now bind the frozen 307-pair manifest and open only the prospectively frozen primary endpoint: calendar-2024 `E90` occurrence from official `NPDES_EFF_VIOLATIONS.csv`, with the already frozen paired risk-difference and exact McNemar/binomial gate. No endpoint, time window, pair membership or threshold may change after outcome access.
''',encoding='utf-8')
    readme=RESEARCH/'README.md'; t=readme.read_text()
    if '## Terminal N01 result / N01 최종 결과' not in t:
        readme.write_text(t+f'''\n\n## Terminal N01 result / N01 최종 결과\n\n**`{GATE}`** — Run `{RUN}` passed all 18 frozen requirements with **307 pairs across 22 states**. Future E90/DMR outcome membership remains unopened. See `RESULT.md`.\n''')
    (REG/f'{CLAIM}.md').write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-17
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_DESIGN
status: active
---

# {CLAIM} — EPA cross-media matched monitoring-intensity design is identifiable

Run `{RUN}` passes all 18 N01 requirements and freezes **307 non-reused HIGH–LOW pairs across 22 states** from 2,170 structurally eligible Registry IDs. Baseline count balance is **{d['baseline_ratio_within_1_3_to_3_rate']:.2%}** and permit-age balance is **{d['permit_age_difference_within_10y_rate']:.2%}**. This is a design-feasibility claim only; 2024 E90 outcomes and any relationship remain unopened.
''')
    (REG/f'{DECISION}.md').write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-EPA-XMEDIA-N01
status: active
---

# {DECISION} — Accept N01 PASS and require separate E01 authorization

Accept immutable staging commit `{STAGING_COMMIT}` from Run `{RUN}` as **`{GATE}`** and close Issue #{ISSUE}. The frozen 307-pair manifest is now the only authorized design for any later E01. Outcome access remains prohibited until a separate E01 contract/Issue/activation binds this exact manifest fingerprint.
''')
    append_once(REG/'CLAIM_LEDGER.md',f'`{CLAIM}`',f"| `{CLAIM}` | US-EPA-XMEDIA-N01 identifies 307 frozen matched pairs across 22 states from 2,170 eligible Registry IDs; 18/18 PASS, outcomes unopened. / EPA cross-media matched design 식별 PASS. | `DERIVED` | `V2_PRIMARY_VERIFIED_DESIGN` | Issue #151; Run {RUN}; `research/US-EPA-XMEDIA-N01/RESULT.md` | 2026-09-17 | active |\n")
    append_once(REG/'DECISION_LOG.md',f'`{DECISION}`',f"| `{DECISION}` | 2026-09-17 | Accept US-EPA-XMEDIA-N01 PASS; freeze 307-pair manifest and require separate E01 authorization. / N01 PASS 수용 및 E01 별도 승인 요구. | Staging `{STAGING_COMMIT}`; Run {RUN}; 18/18 PASS; manifest `{d['manifest_sha256']}`. | Issue #151; `{CLAIM}` | active |\n")
    (ROOT/'STATUS.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 151
last_completed_research: US-EPA-XMEDIA-N01
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-EPA-XMEDIA-N01 is terminal at **`{GATE}`**. Run `{RUN}` passed **18/18** requirements and froze **307 matched pairs across 22 states** under manifest `{d['manifest_sha256']}`. Future 2024 E90/DMR outcomes remain unopened.

## Exact next action / 정확한 다음 행동

Freeze and bind a separate `US-EPA-XMEDIA-E01` to this exact manifest before any outcome access. E01 may use only the prospectively frozen calendar-2024 `E90` occurrence endpoint and paired McNemar/RD gate.

Incremental monetary cost remains **0 USD**.
''')
    (CTX/'checkpoint.json').write_text(json.dumps({'checkpoint_id':'CHK-20260917-US-EPA-XMEDIA-N01-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':151,'last_completed_research':'US-EPA-XMEDIA-N01','last_decision':DECISION,'updated':'2026-09-17'},indent=2)+'\n')
    (CTX/'SESSION_HANDOFF.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 151
last_completed_research: US-EPA-XMEDIA-N01
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

- state: `{STATE}`
- N01 gate: `{GATE}`
- run: `{RUN}`
- immutable staging: `{STAGING_COMMIT}`
- matched pairs: 307
- states: 22
- manifest SHA-256: `{d['manifest_sha256']}`
- future E90/DMR/RCRA outcomes opened: false
- relationship/prediction/causality: false
- cost: 0 USD

## Exact restart point

Create and activate a separate E01 bound to the exact N01 manifest before any outcome access.
''')
    print(json.dumps({'gate':GATE,'decision':DECISION,'claim':CLAIM,'state':STATE},sort_keys=True))
if __name__=='__main__': main()
