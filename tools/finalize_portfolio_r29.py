#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / 'registry'
CTX = ROOT / 'context'
OUT = ROOT / 'research' / 'PORTFOLIO-R29'
ISSUE = 138
DECISION = 'DEC-190'
CLAIM = 'CLM-176'
SELECTION = 'SELECT_C_EU_004_INDUSTRIAL_SITE_CLIMATE_F01'
STATE = 'PORTFOLIO_R29_SELECTED_C_EU_004__F01_AUTHORIZATION_REQUIRED'
RUN_ID = os.environ.get('GITHUB_RUN_ID', 'unknown')


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding='utf-8')
    if marker not in text:
        if not text.endswith('\n'):
            text += '\n'
        text += row
        path.write_text(text, encoding='utf-8')


def main() -> None:
    cp = json.loads((CTX / 'checkpoint.json').read_text(encoding='utf-8'))
    assert cp['active_issue'] == ISSUE
    assert cp['active_research'] == 'PORTFOLIO-R29'
    assert cp['last_completed_issue'] == 137
    assert cp['last_decision'] == 'DEC-189'

    readme_path = OUT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    assert 'US-PIPE-001 = 36/45' in readme
    assert 'C-EU-004 = 36/45' in readme
    assert 'No candidate outcome magnitude or relationship is opened' in readme

    result = f'''---
id: PORTFOLIO-R29-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-16
issue: {ISSUE}
state: COMPLETED_SELECT
selected_candidate: C-EU-004
selected_gate: C-EU-F01
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R29 Result — Select C-EU-004 F01

**`{SELECTION}`**

R29 compares only the two surviving R28 alternatives after terminal US-UTIL-N01. No candidate outcome magnitude or relationship was opened.

## Final scoring / 최종 점수

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | Total | R29 disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| US-PIPE-001 hydrologic stress → incident | 5 | 5 | 5 | 5 | 5 | 5 | **3** | **3** | 0 | **36** | HOLD_RESTRICTED_GEOMETRY_AND_OVERLAP |
| **C-EU-004 industrial-site climate** | 4 | 5 | 3 | 4 | 4 | 5 | **5** | **3** | **3** | **36** | **SELECT_STAGE0_F01_ONLY** |

US-PIPE changes from R28 only in the two dimensions prospectively authorized for update: Join defensibility `5→3` and Next-gate information gain `2→3`. PHMSA incident and annual mileage data remain public, but unrestricted national NPMS line GIS cannot be assumed for the general public. This weakens the original line-resolved hydrologic exposure design without proving the candidate impossible.

C-EU retains its R28 score. EEA still exposes downloadable industrial site/facility location identities and ERA5-Land remains a free CC-BY climate source; programmatic CDS-key friction must be tested in F01 but is not itself a monetary-cost penalty.

## Frozen tie-break / 고정 동점판정

1. Total: **36 = 36**.
2. Next-gate information gain: **3 = 3**.
3. Low overlap / novelty risk: **C-EU 3 > US-PIPE 0**.

Therefore the tie-break stops at criterion 3 and selects `C-EU-004`. No score was changed after observing the tie.

## Authorization boundary / 승인 경계

R29 authorizes only a separate `C-EU-F01` outcome-blind source/access/identity feasibility gate. F01 must establish:
- a reproducible zero-cost EEA Industrial Reporting site/facility location route;
- exact site/facility identity and coordinate support without fuzzy repair;
- a reproducible zero-cost Copernicus/ERA5-Land access route;
- exactly one prospectively selected physical-hazard variable family from source semantics/support only;
- deterministic point-to-grid/time identity and coverage;
- no industrial outcome, emissions effect, climate coefficient, vulnerability score, or causal claim.

R29 does not authorize opening an industrial outcome or climate-effect relationship.

## Preserved alternative / 보존 후보

`US-PIPE-001` remains unexecuted and is not declared impossible. Any later return requires a new portfolio decision and a prospective public-denominator/access design; restricted NPMS GIS may not be assumed or bypassed.

Incremental monetary cost remains **0 USD**.
'''
    (OUT / 'RESULT.md').write_text(result, encoding='utf-8')

    if '## Final disposition / 최종 처분' not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nR29 mechanically selects **`{SELECTION}`** under {DECISION} / {CLAIM}. Total scores tie 36=36 and information gain ties 3=3; Low-overlap/novelty risk selects C-EU at 3>0. No candidate outcome magnitude was opened.\n'''
        readme_path.write_text(readme, encoding='utf-8')

    (REG / f'{DECISION}.md').write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-16
issue: {ISSUE}
research: PORTFOLIO-R29
status: active
---

# {DECISION} — Select C-EU-004 for one outcome-blind F01

## Decision / 결정

Select `C-EU-004` and authorize only a separate `C-EU-F01` source/access/identity feasibility gate. / C-EU-004를 선택하되 별도의 outcome-blind F01만 승인한다.

## Rationale / 근거

Under the frozen R29 update rule, US-PIPE and C-EU both score 36/45. Next-gate information gain ties 3=3. The unchanged R28 tie-break therefore reaches Low overlap / novelty risk, where **C-EU 3 > US-PIPE 0**. Official source revalidation also shows that unrestricted national NPMS line geometry cannot be assumed for US-PIPE, while EEA site locations remain directly downloadable and ERA5-Land remains a free licensed source subject to access-route verification.

## Boundary / 경계

- No climate-effect or industrial-outcome test is authorized by R29.
- No automatic promotion beyond C-EU-F01.
- US-PIPE is preserved, not falsified.
- Incremental monetary cost remains 0 USD.
''', encoding='utf-8')

    (REG / f'{CLAIM}.md').write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-16
issue: {ISSUE}
verification: V2_PRIMARY_VERIFIED_PORTFOLIO
status: active
---

# {CLAIM} — PORTFOLIO-R29 selects C-EU-004

PORTFOLIO-R29 compares only US-PIPE-001 and C-EU-004 without opening candidate outcomes. Both score **36/45** after the prospectively allowed source-access update. The frozen tie-break reaches Low overlap / novelty risk and selects **C-EU-004, 3 > 0** after Total and Next-gate information gain both tie.

This is a portfolio-control claim only. It establishes no climate effect, industrial vulnerability, emissions relationship, novelty proof or causality.
''', encoding='utf-8')

    append_once(REG / 'CLAIM_LEDGER.md', f'`{CLAIM}`', f'| `{CLAIM}` | PORTFOLIO-R29 selects C-EU-004 after a 36=36 total and 3=3 information-gain tie because Low-overlap/novelty risk is 3>0; no candidate outcomes opened. / R29은 outcome 비개봉 상태에서 C-EU-004를 선택했다. | `DERIVED` | `V2_PRIMARY_VERIFIED_PORTFOLIO` | Issue #138; `research/PORTFOLIO-R29/RESULT.md` | 2026-09-16 | active |\n')
    append_once(REG / 'DECISION_LOG.md', f'`{DECISION}`', f'| `{DECISION}` | 2026-09-16 | Select C-EU-004 for one separate outcome-blind F01 only. / C-EU-004를 별도 outcome-blind F01에 한해 선택. | Frozen R29 tie-break: total 36=36, info gain 3=3, low-overlap/novelty C-EU 3 > US-PIPE 0. | Issue #138; `{CLAIM}`; `research/PORTFOLIO-R29/RESULT.md` | active |\n')

    status = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R29-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 138
last_completed_research: PORTFOLIO-R29
last_decision: {DECISION}
updated: 2026-09-16
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R29 is completed with **`{SELECTION}`** under {DECISION} / {CLAIM}. No candidate outcome magnitude was opened.

## Exact next action / 정확한 다음 행동

Open exactly one separate `C-EU-F01` outcome-blind source/access/identity feasibility issue. Establish EEA industrial-site identities/coordinates, zero-cost ERA5-Land access, one prospectively selected physical-hazard variable family, and deterministic point-to-grid/time support. Do not open industrial outcomes or compute a climate-effect relationship.

Incremental monetary cost remains **0 USD**.
'''
    (ROOT / 'STATUS.md').write_text(status, encoding='utf-8')
    cp2 = {
        'checkpoint_id': 'CHK-20260916-PORTFOLIO-R29-TERMINAL',
        'active_issue': 'none',
        'active_research': 'NONE',
        'last_completed_issue': 138,
        'last_completed_research': 'PORTFOLIO-R29',
        'last_decision': DECISION,
        'updated': '2026-09-16',
    }
    (CTX / 'checkpoint.json').write_text(json.dumps(cp2, indent=2) + '\n', encoding='utf-8')
    handoff = f'''---
checkpoint_id: CHK-20260916-PORTFOLIO-R29-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 138
last_completed_research: PORTFOLIO-R29
last_decision: {DECISION}
updated: 2026-09-16
---

# Session Handoff / 세션 인계

## Canonical state / 정본 상태

- state: `{STATE}`
- R29 selection: `{SELECTION}`
- selected candidate: `C-EU-004`
- candidate outcomes opened: `false`

## Exact restart point / 정확한 재개점

Open exactly one `C-EU-F01` outcome-blind source/access/identity feasibility gate. Verify the EEA site/facility identity and coordinate route, establish a zero-cost ERA5-Land access route, choose exactly one physical-hazard family from source semantics/support before any industrial outcome access, and freeze deterministic point-to-grid/time identity. No effect test is authorized.

Incremental monetary cost remains **0 USD**.
'''
    (CTX / 'SESSION_HANDOFF.md').write_text(handoff, encoding='utf-8')

    print(json.dumps({'selection': SELECTION, 'decision': DECISION, 'claim': CLAIM, 'state': STATE, 'finalizer_run': RUN_ID}, sort_keys=True))


if __name__ == '__main__':
    main()
