#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; CTX=ROOT/'context'; REG=ROOT/'registry'
DEC='DEC-220'; ISSUE=154; STATE='US_FAA_AIP_F01_ACTIVE__OUTCOME_BLIND_EXACT_AIRPORT_TIME_JOIN_GATE'
CONTRACT='4f9a2a3491bc00c0fd1e00a7b0d3bc0bc62d4254'

def append_once(path, marker, row):
    t=path.read_text(encoding='utf-8')
    if marker not in t:
        if not t.endswith('\n'): t+='\n'
        path.write_text(t+row,encoding='utf-8')

def main():
    cp=json.loads((CTX/'checkpoint.json').read_text())
    assert cp=={'checkpoint_id':'CHK-20260917-PORTFOLIO-R35-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':153,'last_completed_research':'PORTFOLIO-R35','last_decision':'DEC-219','updated':'2026-09-17'}
    contract=(ROOT/'research/US-FAA-AIP-F01/README.md').read_text(encoding='utf-8')
    assert 'CONTRACT_FROZEN_PRE_ISSUE' in contract
    assert 'candidate_outcomes_opened: false' in contract
    assert 'PASS_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_READY' in contract
    assert 'HOLD_US_FAA_AIP_F01_EXACT_AIRPORT_TIME_JOIN_NOT_READY' in contract
    (REG/f'{DEC}.md').write_text(f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: US-FAA-AIP-F01
status: active
---

# {DEC} — Activate outcome-blind FAA AIP ↔ BTS exact airport/time join gate

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

F01 may inspect FAA AIP identity/time/project structure, the official FAA Location IDs database, BTS Master Coordinate identity/history, and on-time schema/airport/time support only. Delay/cancellation/diversion/cause values, grant-conditioned outcome metrics, fuzzy/name/address/geospatial/manual repair, causal claims and airport rankings remain unauthorized. Cost remains 0 USD.
''')
    append_once(REG/'DECISION_LOG.md',f'`{DEC}`',f"| `{DEC}` | 2026-09-17 | Activate US-FAA-AIP-F01 under pre-Issue outcome-blind exact airport/time join contract. / FAA AIP↔BTS F01 활성화. | Contract `{CONTRACT}`; Issue #154; delay outcomes unopened. | Issue #154 | active |\n")
    (ROOT/'STATUS.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-FAA-AIP-F01-ACTIVE
active_issue: 154
active_research: US-FAA-AIP-F01
last_completed_issue: 153
last_completed_research: PORTFOLIO-R35
last_decision: {DEC}
updated: 2026-09-17
---

# Project Status / 프로젝트 상태

**State / 상태:** `{STATE}`

US-FAA-AIP-F01 is active under the frozen pre-Issue contract `{CONTRACT}`. Candidate delay outcomes remain unopened.

## Exact next action / 정확한 다음 행동

Execute one immutable structural F01 run. Do not alter identity rules, thresholds or exclusions after empirical support counts are observed.

Incremental monetary cost remains **0 USD**.
''')
    cp2={'checkpoint_id':'CHK-20260917-US-FAA-AIP-F01-ACTIVE','active_issue':154,'active_research':'US-FAA-AIP-F01','last_completed_issue':153,'last_completed_research':'PORTFOLIO-R35','last_decision':DEC,'updated':'2026-09-17'}
    (CTX/'checkpoint.json').write_text(json.dumps(cp2,indent=2)+'\n')
    (CTX/'SESSION_HANDOFF.md').write_text(f'''---
checkpoint_id: CHK-20260917-US-FAA-AIP-F01-ACTIVE
active_issue: 154
active_research: US-FAA-AIP-F01
last_completed_issue: 153
last_completed_research: PORTFOLIO-R35
last_decision: {DEC}
updated: 2026-09-17
---

# Session Handoff / 세션 인계

- state: `{STATE}`
- Issue: #154
- contract: `{CONTRACT}`
- outcome firewall: BTS delay/cancellation/diversion/cause values unopened
- cost: 0 USD

## Exact restart point
Execute the immutable FAA AIP ↔ FAA LID ↔ BTS Master Coordinate structural gate exactly as frozen.
''')
    print(json.dumps({'decision':DEC,'issue':ISSUE,'state':STATE},sort_keys=True))
if __name__=='__main__': main()
