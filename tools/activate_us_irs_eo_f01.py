#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-237'
CONTRACT='689a00db411b650defcb679bef998beeb55a57da'
ISSUE=163

cp=json.loads((ROOT/'context/checkpoint.json').read_text(encoding='utf-8'))
assert cp['checkpoint_id']=='CHK-20260918-PORTFOLIO-R39-TERMINAL'
assert str(cp['active_issue']).lower() in {'none','null'}
assert cp['active_research']=='NONE'
assert cp['last_completed_issue']==162
assert cp['last_completed_research']=='PORTFOLIO-R39'
assert cp['last_decision']=='DEC-236'

contract=(ROOT/'research/US-IRS-EO-F01/README.md').read_text(encoding='utf-8')
assert 'status: CONTRACT_FROZEN_PRE_ISSUE' in contract
assert 'future_outcome_membership_opened: false' in contract
assert 'PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY' in contract
assert 'future_outcome_rows_opened` must equal exactly **0**' in contract

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: US-IRS-EO-F01
status: active
---

# {DEC} — Activate outcome-blind IRS exact-EIN structural gate

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

F01 may open only official Form-990-series index CSV posting years 2022–2024. The Automatic Revocation bulk ZIP may receive only a body-free HEAD or equivalent metadata-only request consuming zero entity-body bytes. Exact nine-digit EIN/TIN identity only; no name/address/fuzzy/geospatial/manual repair. Prior nonfiling/missed-filing streaks and equivalent statutory-trigger features remain prohibited as exposure. N01/E01 are not authorized. Incremental monetary cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'''\n| `{DEC}` | 2026-09-18 | Activate `US-IRS-EO-F01` under pre-Issue contract `{CONTRACT}` using 2022–2024 Form-990 indexes and a sealed Automatic Revocation outcome source. / 2022–2024 Form-990 index와 Automatic Revocation outcome 봉인 조건으로 F01 활성화. | R39 selected IRS EO 41/45; F01 must falsify exact EIN identity, historical support, documented event semantics and outcome firewall before any membership is opened. / R39 41/45 선정 후 outcome 전 exact EIN·historical support·event semantics·방화벽 검증 필요. | Issue #163; `research/US-IRS-EO-F01/README.md` | active |\n'''
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp2={'checkpoint_id':'CHK-20260918-US-IRS-EO-F01-ACTIVE','active_issue':163,'active_research':'US-IRS-EO-F01','last_completed_issue':162,'last_completed_research':'PORTFOLIO-R39','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp2,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-US-IRS-EO-F01-ACTIVE
active_issue: 163
active_research: US-IRS-EO-F01
last_completed_issue: 162
last_completed_research: PORTFOLIO-R39
last_decision: DEC-237
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_IRS_EO_F01_ACTIVE__OUTCOME_BLIND_EXACT_EIN_GATE`\n\nUS-IRS-EO-F01 is active under its frozen 18-gate contract. Only 2022–2024 Form-990 index rows are authorized. Automatic Revocation List rows, 2025/2026 Form-990 index rows, and statutory nonfiling-trigger exposures remain sealed/prohibited.\n\n## Exact next action / 정확한 다음 행동\n\nExecute the immutable 18-gate historical-index/cardinality/source-metadata runner. The automatic-revocation ZIP may receive body-free HEAD only.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_IRS_EO_F01_ACTIVE__OUTCOME_BLIND_EXACT_EIN_GATE`\n\n- Issue #163 open.\n- Contract: `{CONTRACT}`.\n- Historical row access authorized: Form-990 index posting years 2022, 2023, 2024 only.\n- Organization identity prospect: exact normalized 9-digit EIN/TIN.\n- Automatic Revocation List rows unopened; ZIP HEAD only.\n- 2025/2026 Form-990 index rows unopened.\n- Prior nonfiling/missed-filing streak exposure prohibited.\n- N01/E01 not authorized.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('US_IRS_EO_F01_ACTIVE')
