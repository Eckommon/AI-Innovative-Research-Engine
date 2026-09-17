#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT / 'context'
REG = ROOT / 'registry'
ISSUE = 153
DECISION = 'DEC-218'
CONTRACT_COMMIT = '4febd519dfae899897bed8d2c8ab45edb85fb33c'
STATE = 'PORTFOLIO_R35_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING'


def append_once(path: Path, marker: str, row: str) -> None:
    text = path.read_text(encoding='utf-8')
    if marker not in text:
        if not text.endswith('\n'):
            text += '\n'
        path.write_text(text + row, encoding='utf-8')


def main() -> None:
    checkpoint = json.loads((CTX / 'checkpoint.json').read_text(encoding='utf-8'))
    assert checkpoint == {
        'checkpoint_id': 'CHK-20260917-US-EPA-XMEDIA-E01-TERMINAL',
        'active_issue': 'none',
        'active_research': 'NONE',
        'last_completed_issue': 152,
        'last_completed_research': 'US-EPA-XMEDIA-E01',
        'last_decision': 'DEC-217',
        'updated': '2026-09-17',
    }
    contract = (ROOT / 'research' / 'PORTFOLIO-R35' / 'README.md').read_text(encoding='utf-8')
    assert 'candidate_outcomes_opened: false' in contract
    assert 'Exactly four candidates are authorized' in contract
    assert 'US-FAA-AIP-001' in contract and 'US-EPA-DWSRF-001' in contract
    assert 'US-PHMSA-LI-001' in contract and 'US-NRC-ROP-001' in contract

    (REG / f'{DECISION}.md').write_text(f'''---
id: {DECISION}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: PORTFOLIO-R35
status: active
---

# {DECISION} — activate PORTFOLIO-R35 under the frozen pre-Issue contract

Activate Issue #{ISSUE} only after the candidate contract was frozen at `{CONTRACT_COMMIT}`. R35 may perform source/literature revalidation and then persist exactly one immutable scorecard across the four frozen candidates. Candidate outcomes remain unopened and incremental monetary cost remains 0 USD.
''', encoding='utf-8')

    append_once(
        REG / 'DECISION_LOG.md',
        f'`{DECISION}`',
        f'| `{DECISION}` | 2026-09-17 | Activate PORTFOLIO-R35 under pre-Issue frozen four-candidate contract. / 사전고정 4개 후보 계약에 따라 R35 활성화. | Contract `{CONTRACT_COMMIT}`; candidate outcomes unopened; cost 0 USD. | Issue #153 | active |\n',
    )

    (ROOT / 'STATUS.md').write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R35-ACTIVE
active_issue: 153
active_research: PORTFOLIO-R35
last_completed_issue: 152
last_completed_research: US-EPA-XMEDIA-E01
last_decision: {DECISION}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

PORTFOLIO-R35 is active under pre-Issue contract `{CONTRACT_COMMIT}`. Exactly four candidates are frozen: `US-FAA-AIP-001`, `US-EPA-DWSRF-001`, `US-PHMSA-LI-001`, and `US-NRC-ROP-001`.

## Exact next action / 정확한 다음 행동

Persist `research/PORTFOLIO-R35/SOURCE_REVALIDATION.md` for all four candidates without opening candidate outcomes, then persist exactly one immutable scorecard and select at most one next outcome-blind F01.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

    (CTX / 'checkpoint.json').write_text(json.dumps({
        'checkpoint_id': 'CHK-20260917-PORTFOLIO-R35-ACTIVE',
        'active_issue': 153,
        'active_research': 'PORTFOLIO-R35',
        'last_completed_issue': 152,
        'last_completed_research': 'US-EPA-XMEDIA-E01',
        'last_decision': DECISION,
        'updated': '2026-09-17',
    }, indent=2) + '\n', encoding='utf-8')

    (CTX / 'SESSION_HANDOFF.md').write_text(f'''---
checkpoint_id: CHK-20260917-PORTFOLIO-R35-ACTIVE
active_issue: 153
active_research: PORTFOLIO-R35
last_completed_issue: 152
last_completed_research: US-EPA-XMEDIA-E01
last_decision: {DECISION}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

- state: `{STATE}`
- Issue: #153 open
- frozen contract: `{CONTRACT_COMMIT}`
- candidate outcomes opened: false
- next: source/literature revalidation → exactly one immutable scorecard → at most one F01 selection
- EPA cross-media descendant rescue: prohibited
- incremental cost: 0 USD
''', encoding='utf-8')

    print(json.dumps({'decision': DECISION, 'issue': ISSUE, 'state': STATE}, sort_keys=True))


if __name__ == '__main__':
    main()
