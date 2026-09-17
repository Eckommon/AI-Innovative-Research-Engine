#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-234'
CONTRACT='c0f9f412b88b4ff54fd9999ff57fc3c4be40f374'
ISSUE=161

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: US-FDIC-BRANCH-N01
status: active
---

# {DEC} — Activate outcome-blind FDIC matched network-position trajectory design

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

N01 may read only official historical SOD 2022–2024 structural/exposure rows using exact `UNINUMBR`, `CERT`, `BRNUM`, `STALPBR`, and `DEPSUMBR`. It may build the prospectively frozen `CERT × STALPBR` within-network deposit-share trajectory and matching manifest. 2025 SOD rows, future branch membership, future BankFind structure-event membership, closure/non-continuation outcomes, relationship metrics, prediction, causality, ranking, and novelty claims remain unauthorized. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'; log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Activate `US-FDIC-BRANCH-N01` under pre-Issue contract `{CONTRACT}`; historical matched network-position trajectory design only. / 사전계약에 따라 과거 matched network-position trajectory 설계만 활성화. | F01 passed 18/18 with exact UNINUMBR support; N01 must prove matched-design identifiability before future membership is opened. / F01 exact identity PASS 후 미래 membership 전 matched-design 식별 가능성 검증 필요. | Issue #161; `research/US-FDIC-BRANCH-N01/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-US-FDIC-BRANCH-N01-ACTIVE','active_issue':161,'active_research':'US-FDIC-BRANCH-N01','last_completed_issue':160,'last_completed_research':'US-FDIC-BRANCH-F01','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-US-FDIC-BRANCH-N01-ACTIVE
active_issue: 161
active_research: US-FDIC-BRANCH-N01
last_completed_issue: 160
last_completed_research: US-FDIC-BRANCH-F01
last_decision: DEC-234
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_FDIC_BRANCH_N01_ACTIVE__OUTCOME_BLIND_MATCHED_NETWORK_POSITION_DESIGN`\n\nUS-FDIC-BRANCH-N01 is active under its frozen pre-Issue matched-design contract. Only historical SOD 2022–2024 structural/exposure rows are authorized. 2025 SOD and future branch/event membership remain unopened.\n\n## Exact next action / 정확한 다음 행동\n\nExecute the immutable historical `CERT × STALPBR` network-position trajectory/matching gate without opening any future closure/non-continuation membership. E01 remains unauthorized.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_FDIC_BRANCH_N01_ACTIVE__OUTCOME_BLIND_MATCHED_NETWORK_POSITION_DESIGN`\n\n- Issue #161 open.\n- Contract: `{CONTRACT}`.\n- Parent F01: 18/18 PASS.\n- Authorized rows: SOD 2022–2024 only.\n- Exposure: within exact CERT × STALPBR delta-log deposit share quartiles.\n- Future 2025 SOD and BankFind branch/event membership unopened.\n- E01 not authorized.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('US_FDIC_BRANCH_N01_ACTIVE')
