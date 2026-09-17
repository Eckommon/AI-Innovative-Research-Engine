#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-228'
CONTRACT='1c7496ad5f4f6d82900fd60f0a31d3406cf217dc'

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 158
research: US-FSIS-SAMPLE-F01
status: active
---

# {DEC} — Activate outcome-blind FSIS exact-establishment structural gate

Activate Issue #158 only under pre-Issue contract `{CONTRACT}`.

F01 may inspect official FSIS Raw Poultry Sampling FY2021–FY2023 exposure rows, official dataset metadata and the official MPI Directory under the frozen minimal establishment-number normalization rule. Candidate 2024–2025 recall/public-health-alert membership and all recall row values remain forbidden. No name/address/geospatial/fuzzy/manual identity repair. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Activate `US-FSIS-SAMPLE-F01` under pre-Issue contract `{CONTRACT}` with FY2021–FY2023 sampling exposure and sealed 2024–2025 recall membership. / 사전고정 계약 아래 FY2021–FY2023 sampling 노출과 봉인된 2024–2025 recall membership으로 F01 활성화. | Test source-native establishment identity, longitudinal support and MPI exact-link coverage before any recall outcome access. / recall outcome 접근 전 source-native establishment identity·longitudinal support·MPI exact-link coverage 검증. | Issue #158; `research/US-FSIS-SAMPLE-F01/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260917-US-FSIS-SAMPLE-F01-ACTIVE','active_issue':158,'active_research':'US-FSIS-SAMPLE-F01','last_completed_issue':157,'last_completed_research':'PORTFOLIO-R37','last_decision':DEC,'updated':'2026-09-17'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-US-FSIS-SAMPLE-F01-ACTIVE
active_issue: 158
active_research: US-FSIS-SAMPLE-F01
last_completed_issue: 157
last_completed_research: PORTFOLIO-R37
last_decision: DEC-228
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_FSIS_SAMPLE_F01_ACTIVE__OUTCOME_BLIND_EXACT_ESTABLISHMENT_GATE`\n\nUS-FSIS-SAMPLE-F01 is active under its frozen pre-Issue 18-gate contract. Candidate 2024–2025 recall/public-health-alert membership remains unopened.\n\n## Exact next action / 정확한 다음 행동\n\nExecute the immutable FY2021–FY2023 Raw Poultry Sampling + MPI Directory exact-establishment structural gate without opening candidate recall rows.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_FSIS_SAMPLE_F01_ACTIVE__OUTCOME_BLIND_EXACT_ESTABLISHMENT_GATE`\n\n- Issue #158 open.\n- Frozen contract: `{CONTRACT}`.\n- Exposure: FSIS Raw Poultry Sampling FY2021–FY2023 only.\n- Identity: official establishment number under frozen minimal normalization only.\n- Structural identity source: official MPI Directory.\n- Candidate outcome window: 2024–2025 recall/public-health-alert membership sealed.\n- 18 frozen gates; no relationship/prediction/ranking/causality/novelty.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('US_FSIS_SAMPLE_F01_ACTIVE')
