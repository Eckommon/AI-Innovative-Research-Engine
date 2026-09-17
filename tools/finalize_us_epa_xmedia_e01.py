#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research' / 'US-EPA-XMEDIA-E01'
REG = ROOT / 'registry'
CTX = ROOT / 'context'

ISSUE = 152
RUN = 35168068999
STAGING_COMMIT = '3852773636146fb48414c98a825d6bedb8cfd6c1'
DECISION = 'DEC-217'
CLAIM = 'CLM-190'
GATE = 'NO_PREREGISTERED_POSITIVE_US_EPA_XMEDIA_E01_RELATIONSHIP'
STATE = 'US_EPA_XMEDIA_E01_TERMINAL_NO_PREREGISTERED_POSITIVE__PORTFOLIO_RESELECTION_REQUIRED'


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding='utf-8')
    if marker not in text:
        if not text.endswith('\n'):
            text += '\n'
        path.write_text(text + row, encoding='utf-8')


def main() -> None:
    checkpoint = json.loads((CTX / 'checkpoint.json').read_text(encoding='utf-8'))
    assert checkpoint == {
        'checkpoint_id': 'CHK-20260917-US-EPA-XMEDIA-E01-ACTIVE',
        'active_issue': 152,
        'active_research': 'US-EPA-XMEDIA-E01',
        'last_completed_issue': 151,
        'last_completed_research': 'US-EPA-XMEDIA-N01',
        'last_decision': 'DEC-216',
        'updated': '2026-09-17',
    }

    result = json.loads((RESEARCH / 'STAGING_RESULT.json').read_text(encoding='utf-8'))
    assert result['gate'] == GATE
    assert result['contract_commit'] == '46938afda3fbeaf9349a3c508502f8d4a3c973a3'
    assert result['n01_staging_commit'] == '78f0f0f1458463c79c326c016d415dc5533af026'
    assert result['n01_manifest_sha256'] == '19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf'
    assert result['integrity']['frozen_pairs'] == 307
    assert result['integrity']['frozen_npdes_ids'] == 614
    assert result['integrity']['pair_membership_changed'] is False
    assert result['integrity']['endpoint_changed'] is False
    assert result['integrity']['window_changed'] is False
    assert result['integrity']['threshold_changed'] is False
    assert result['integrity']['facility_level_outcome_labels_persisted'] is False
    assert result['interpretation_boundary']['dmr_values_or_limits_opened'] is False
    assert result['interpretation_boundary']['rcra_outcomes_opened'] is False
    assert result['interpretation_boundary']['secondary_endpoint_computed'] is False
    assert result['interpretation_boundary']['facility_ranking_computed'] is False
    assert result['interpretation_boundary']['enforcement_targeting_score_computed'] is False
    assert result['incremental_monetary_cost_usd'] == 0

    p = result['primary']
    assert p['b_high1_low0'] == 12
    assert p['c_high0_low1'] == 6
    assert p['discordant_pairs'] == 18
    assert p['risk_difference'] < p['materiality_floor']
    assert p['exact_two_sided_mcnemar_binomial_p'] >= 0.05

    (RESEARCH / 'RESULT.md').write_text(f'''---
id: US-EPA-XMEDIA-E01-RESULT
type: preregistered-paired-outcome-experiment
created: 2026-09-17
issue: {ISSUE}
state: COMPLETED_NO_PREREGISTERED_POSITIVE
gate: {GATE}
source_run: {RUN}
staging_commit: {STAGING_COMMIT}
incremental_monetary_cost_usd: 0
---

# US-EPA-XMEDIA-E01 Result — no preregistered positive relationship established

**`{GATE}`**

Immutable Run `{RUN}` executed the outcome contract frozen before Issue creation at `46938afda3fbeaf9349a3c508502f8d4a3c973a3`, bound to the N01 307-pair manifest `19e1b3a1963fe008811aa230336e12ec69a348b03cf37bd656ea9d3fba8e5aaf`.

## Primary preregistered result / 사전등록 1차 결과

- frozen matched pairs: **307**
- HIGH 2024 E90 events: **{p['high_event_facilities']} / 307 ({p['risk_high']:.2%})**
- LOW 2024 E90 events: **{p['low_event_facilities']} / 307 ({p['risk_low']:.2%})**
- paired risk difference, HIGH − LOW: **{p['risk_difference']:+.4f} ({p['risk_difference']*100:+.2f} percentage points)**
- discordant HIGH=1 / LOW=0 (`b`): **{p['b_high1_low0']}**
- discordant HIGH=0 / LOW=1 (`c`): **{p['c_high0_low1']}**
- discordant pairs: **{p['discordant_pairs']}**
- exact two-sided McNemar/binomial p-value: **{p['exact_two_sided_mcnemar_binomial_p']:.6f}**
- preregistered materiality floor: **+{p['materiality_floor']*100:.0f} percentage points**

The point estimate is positive, but it is below the frozen +5 percentage-point materiality floor and the exact paired test is not statistically significant at p<0.05. Therefore the preregistered positive gate is not met.

This result does **not** establish that no association exists in every population or endpoint. It establishes only that this frozen 307-pair, calendar-2024 E90 experiment did not establish the preregistered positive relationship.

## Execution integrity / 실행 무결성

- exact pair membership changed: **false**
- endpoint/window/threshold changed: **false**
- facility-level outcome labels persisted: **false**
- official matched-state source rows scanned: **{result['integrity']['total_source_rows_scanned']:,}**
- rows for frozen NPDES IDs encountered: **{result['integrity']['rows_for_frozen_ids']:,}**
- malformed nonblank candidate E90 dates excluded: **{result['integrity']['malformed_nonblank_candidate_e90_dates_excluded']}**
- DMR values/limits opened: **false**
- RCRA violation/enforcement outcomes opened: **false**
- secondary endpoint computed: **false**
- facility ranking / enforcement-targeting score: **not computed**
- incremental monetary cost: **0 USD**

## Interpretation boundary / 해석 경계

The result is observational and noncausal. The positive point estimate must not be described as a confirmed cross-media relationship, and the non-significant result must not be reframed as evidence of a protective effect. No named facility inference or enforcement recommendation is authorized.

## Exact next action / 정확한 다음 행동

Terminate this EPA descendant chain without rescue. Do **not** change E90 to another violation code, widen the outcome window, lower materiality/significance thresholds, rematch facilities, or mine secondary endpoints. Return to an independent `PORTFOLIO-R35` Stage-0 reselection under the standing mission rubric and zero-cost rule.
''', encoding='utf-8')

    readme = RESEARCH / 'README.md'
    text = readme.read_text(encoding='utf-8')
    if '## Terminal E01 result / E01 최종 결과' not in text:
        readme.write_text(text + f'''\n\n## Terminal E01 result / E01 최종 결과\n\n**`{GATE}`** — Run `{RUN}`: HIGH **{p['risk_high']:.2%}**, LOW **{p['risk_low']:.2%}**, RD **{p['risk_difference']*100:+.2f}pp**, `b/c={p['b_high1_low0']}/{p['c_high0_low1']}`, exact p **{p['exact_two_sided_mcnemar_binomial_p']:.6f}**. The frozen positive/material gate was not met. No rescue or secondary-endpoint mining is authorized. See `RESULT.md`.\n''', encoding='utf-8')

    (REG / f'{CLAIM}.md').write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-17
issue: {ISSUE}
verification: V3_REPRODUCED
status: active
---

# {CLAIM} — EPA cross-media E01 did not establish the preregistered positive relationship

Under the frozen 307-pair design and calendar-2024 E90 endpoint, Run `{RUN}` observed HIGH **{p['risk_high']:.2%}** vs LOW **{p['risk_low']:.2%}**, RD **{p['risk_difference']*100:+.2f} percentage points**, `b/c={p['b_high1_low0']}/{p['c_high0_low1']}`, and exact two-sided p **{p['exact_two_sided_mcnemar_binomial_p']:.6f}**. The point estimate is positive but below the +5pp materiality floor and statistically non-significant. This is a bounded observational result, not proof of no association generally and not a causal claim.
''', encoding='utf-8')

    (REG / f'{DECISION}.md').write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-EPA-XMEDIA-E01
status: active
---

# {DECISION} — Accept E01 terminal no-positive gate and prohibit descendant rescue

Accept immutable staging commit `{STAGING_COMMIT}` from Run `{RUN}` as **`{GATE}`** and close Issue #{ISSUE}. No alternate violation code, expanded window, relaxed threshold, rematching, secondary endpoint mining or post-hoc EPA rescue is authorized. Return to independent `PORTFOLIO-R35` Stage-0 reselection.
''', encoding='utf-8')

    append_once(
        REG / 'CLAIM_LEDGER.md',
        f'`{CLAIM}`',
        f"| `{CLAIM}` | US-EPA-XMEDIA-E01: frozen 307-pair 2024 E90 experiment observed HIGH {p['risk_high']:.2%} vs LOW {p['risk_low']:.2%}, RD {p['risk_difference']*100:+.2f}pp, b/c={p['b_high1_low0']}/{p['c_high0_low1']}, exact p={p['exact_two_sided_mcnemar_binomial_p']:.6f}; preregistered positive gate not established. / EPA cross-media E01 사전등록 양의 관계 미확립. | `OBSERVED/DERIVED` | `V3_REPRODUCED` | Issue #152; Run {RUN}; `research/US-EPA-XMEDIA-E01/RESULT.md` | 2026-09-17 | active |\n",
    )
    append_once(
        REG / 'DECISION_LOG.md',
        f'`{DECISION}`',
        f"| `{DECISION}` | 2026-09-17 | Accept US-EPA-XMEDIA-E01 no-preregistered-positive terminal; prohibit rescue and return to PORTFOLIO-R35. / E01 무양성 종결 수용, 구조 변경 구제 금지, R35 재선정. | Staging `{STAGING_COMMIT}`; Run {RUN}; RD {p['risk_difference']*100:+.2f}pp; p={p['exact_two_sided_mcnemar_binomial_p']:.6f}. | Issue #152; `{CLAIM}` | active |\n",
    )

    (ROOT / 'STATUS.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-E01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 152
last_completed_research: US-EPA-XMEDIA-E01
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-EPA-XMEDIA-E01 is terminal at **`{GATE}`**. Frozen 307-pair calendar-2024 E90 outcome: HIGH **{p['risk_high']:.2%}**, LOW **{p['risk_low']:.2%}**, RD **{p['risk_difference']*100:+.2f}pp**, exact p **{p['exact_two_sided_mcnemar_binomial_p']:.6f}**. The preregistered positive/material gate was not met.

## Exact next action / 정확한 다음 행동

Start independent `PORTFOLIO-R35` Stage-0 reselection. Do not rescue the EPA branch by changing endpoint, window, threshold, matching or secondary outcomes.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

    (CTX / 'checkpoint.json').write_text(json.dumps({
        'checkpoint_id': 'CHK-20260917-US-EPA-XMEDIA-E01-TERMINAL',
        'active_issue': 'none',
        'active_research': 'NONE',
        'last_completed_issue': 152,
        'last_completed_research': 'US-EPA-XMEDIA-E01',
        'last_decision': DECISION,
        'updated': '2026-09-17',
    }, indent=2) + '\n', encoding='utf-8')

    (CTX / 'SESSION_HANDOFF.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-EPA-XMEDIA-E01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 152
last_completed_research: US-EPA-XMEDIA-E01
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

- state: `{STATE}`
- E01 gate: `{GATE}`
- source Run: `{RUN}`
- immutable staging: `{STAGING_COMMIT}`
- frozen pairs: 307
- HIGH risk: {p['risk_high']:.8f}
- LOW risk: {p['risk_low']:.8f}
- RD: {p['risk_difference']:.8f}
- b/c: {p['b_high1_low0']}/{p['c_high0_low1']}
- exact paired p: {p['exact_two_sided_mcnemar_binomial_p']:.12f}
- branch rescue authorized: false
- facility ranking / enforcement targeting: false
- cost: 0 USD

## Exact restart point

Start `PORTFOLIO-R35` as an independent Stage-0 reselection. Do not alter or reinterpret the completed EPA E01 design.
''', encoding='utf-8')

    print(json.dumps({'gate': GATE, 'decision': DECISION, 'claim': CLAIM, 'state': STATE}, sort_keys=True))


if __name__ == '__main__':
    main()
