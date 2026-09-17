#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CTX=ROOT/'context'
REG=ROOT/'registry'
R=ROOT/'research'/'PORTFOLIO-R35'
ISSUE=153
DECISION='DEC-219'
CLAIM='CLM-191'
SELECTION='SELECT_US_FAA_AIP_001_AIRFIELD_INFRASTRUCTURE_TO_BTS_DELAY_F01'
STATE='PORTFOLIO_R35_SELECTED_US_FAA_AIP_001__F01_AUTHORIZATION_REQUIRED'
CONTRACT='4febd519dfae899897bed8d2c8ab45edb85fb33c'
REVALIDATION='127170adafcddefb66e3a9bfd33943b8fd5d53be'
SCORECARD='b41f009024b23e73d75a278e73cba950f6afd3fe'


def append_once(path: Path, marker: str, row: str) -> None:
    text=path.read_text(encoding='utf-8')
    if marker not in text:
        if not text.endswith('\n'): text+='\n'
        path.write_text(text+row,encoding='utf-8')


def main():
    cp=json.loads((CTX/'checkpoint.json').read_text())
    assert cp['active_issue']==153 and cp['active_research']=='PORTFOLIO-R35'
    assert cp['last_decision']=='DEC-218'
    score=(R/'SCORECARD.md').read_text()
    assert '**US-FAA-AIP-001**' in score and '**40**' in score
    assert 'US-EPA-DWSRF-001' in score and '**39**' in score
    assert 'US-PHMSA-LI-001' in score and '**38**' in score
    assert 'US-NRC-ROP-001' in score and '**32**' in score
    assert SELECTION in score
    assert 'Candidate outcomes opened:** false' in score

    (R/'RESULT.md').write_text(f'''---
id: PORTFOLIO-R35-RESULT
type: stage0-portfolio-selection
created: 2026-09-17
issue: {ISSUE}
state: COMPLETED_SELECTED
selection: {SELECTION}
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R35 Result / 결과

**`{SELECTION}`**

R35 executed the candidate pool and rubric frozen before Issue binding at `{CONTRACT}`, source/literature revalidation at `{REVALIDATION}`, and the one-time immutable scorecard at `{SCORECARD}`.

## Immutable ranking

| Candidate | Score /45 | Terminal portfolio disposition |
|---|---:|---|
| `US-FAA-AIP-001` | **40** | **SELECT_F01** |
| `US-EPA-DWSRF-001` | **39** | HOLD_DIRECT_PRECEDENT |
| `US-PHMSA-LI-001` | **38** | HOLD_AGENCY_INTENT_AND_OVERLAP |
| `US-NRC-ROP-001` | **32** | HOLD_INTEGRATED_FRAMEWORK_AND_SMALL_N |

No tie-break was required.

## What is authorized

Exactly one separate outcome-blind `US-FAA-AIP-F01` may be designed and executed next. F01 must first prove or reject:

1. current official FAA AIP grant source access and `Loc ID` schema;
2. current BTS airport identity semantics;
3. a deterministic official FAA↔BTS identity route, not string resemblance;
4. sufficient airport/time/cardinality overlap;
5. deterministic source fingerprints and zero-cost reproducibility.

F01 may not open grant-conditioned future delay values, direction, effect estimates or predictive metrics. If exact identity cannot be established, the branch must HOLD without fuzzy/manual/geographic repair.

## Non-claims

R35 establishes no infrastructure effectiveness, delay relationship, causal effect or novelty claim. DWSRF/PHMSA/NRC remain portfolio holds only; their outcomes were not opened.

Incremental monetary cost: **0 USD**.
''',encoding='utf-8')

    readme=R/'README.md'
    text=readme.read_text()
    if '## Final disposition / 최종 처분' not in text:
        readme.write_text(text+f'''\n\n## Final disposition / 최종 처분\n\nIssue #{ISSUE} ratifies the one-time immutable scorecard without rescoring. **`{SELECTION}`** is uniquely selected at **40/45** over DWSRF 39, PHMSA 38 and NRC 32. No candidate outcome was opened.\n''')

    (REG/f'{CLAIM}.md').write_text(f'''---
id: {CLAIM}
type: claim
created: 2026-09-17
issue: {ISSUE}
verification: V2_REVIEWED
status: active
---

# {CLAIM} — R35 selected FAA AIP for one outcome-blind F01

Under the pre-Issue frozen nine-dimension rubric and one-time scorecard, `US-FAA-AIP-001` scored 40/45, ahead of DWSRF 39, PHMSA 38 and NRC 32. This supports only portfolio selection of an identity/cardinality F01; it is not evidence that AIP grants affect later airport delays.
''',encoding='utf-8')

    (REG/f'{DECISION}.md').write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: PORTFOLIO-R35
status: active
---

# {DECISION} — close R35 and authorize one FAA-AIP outcome-blind F01

Accept immutable scorecard `{SCORECARD}` without rescoring and select **`{SELECTION}`**. Close Issue #{ISSUE}. Authorize only a separate FAA-AIP source/schema/identity/cardinality F01; no delay outcome may be opened before a later prospective design gate.
''',encoding='utf-8')

    append_once(REG/'CLAIM_LEDGER.md',f'`{CLAIM}`',f'| `{CLAIM}` | PORTFOLIO-R35 selected `US-FAA-AIP-001` at 40/45 over DWSRF 39, PHMSA 38, NRC 32 for one outcome-blind F01; no candidate outcomes opened. / R35 FAA AIP F01 선정. | `DERIVED` | `V2_REVIEWED` | Issue #153; `{SCORECARD}`; `research/PORTFOLIO-R35/RESULT.md` | 2026-09-17 | active |\n')
    append_once(REG/'DECISION_LOG.md',f'`{DECISION}`',f'| `{DECISION}` | 2026-09-17 | Close R35 and authorize one FAA-AIP outcome-blind F01. / R35 종결 및 FAA AIP F01 1개 승인. | Immutable scorecard `{SCORECARD}`; selection `{SELECTION}`. | Issue #153; `{CLAIM}` | active |\n')

    (ROOT/'STATUS.md').write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R35-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 153
last_completed_research: PORTFOLIO-R35
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R35 selected **`US-FAA-AIP-001`** at **40/45** over DWSRF 39, PHMSA 38 and NRC 32. Candidate outcomes remained unopened.

## Exact next action / 정확한 다음 행동

Freeze a separate outcome-blind `US-FAA-AIP-F01` contract before its Issue is created. F01 must determine whether official FAA AIP `Loc ID` can be bound deterministically to BTS airport identity with adequate temporal/cardinality support. No grant-conditioned delay value may be opened.

Incremental monetary cost remains **0 USD**.
''',encoding='utf-8')
    (CTX/'checkpoint.json').write_text(json.dumps({
      'checkpoint_id':'CHK-20260917-PORTFOLIO-R35-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':153,'last_completed_research':'PORTFOLIO-R35','last_decision':DECISION,'updated':'2026-09-17'},indent=2)+'\n')
    (CTX/'SESSION_HANDOFF.md').write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R35-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 153
last_completed_research: PORTFOLIO-R35
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

- state: `{STATE}`
- R35 selection: `{SELECTION}`
- immutable scorecard: `{SCORECARD}`
- candidate outcomes opened: false
- exact next: freeze FAA-AIP-F01 outcome-blind source/schema/identity/cardinality contract, then create its Issue
- fuzzy/manual/geographic identity repair: prohibited
- delay outcomes before later N01: prohibited
- cost: 0 USD
''',encoding='utf-8')
    print(json.dumps({'decision':DECISION,'claim':CLAIM,'selection':SELECTION,'state':STATE},sort_keys=True))

if __name__=='__main__': main()
