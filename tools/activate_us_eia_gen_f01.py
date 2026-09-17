#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-224'
CONTRACT='140715aecd58bf5371f7c0a6a46feccf761d9457'

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 156
research: US-EIA-GEN-F01
status: active
---

# {DEC} — Activate outcome-blind EIA generator structural gate

Activate Issue #156 only under pre-Issue contract `{CONTRACT}`.

F01 may inspect January-2024 EIA-860M Planned exposure rows and may inspect December-2025 workbook file/sheet/header structure only. December-2025 row membership, status, operation dates, schedule changes and all generator-specific future outcomes remain forbidden. Exact identity is EIA Plant ID + Generator ID only; no fuzzy/name/address/geospatial/manual repair. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Activate `US-EIA-GEN-F01` under pre-Issue contract `{CONTRACT}` with January-2024 exposure rows and December-2025 header-only firewall. / 사전고정 계약 아래 2024-01 노출행과 2025-12 header-only 방화벽으로 F01 활성화. | Test exact Plant ID + Generator ID co-located solar+storage structural feasibility before any future commissioning outcome access. / future commissioning outcome 접근 전 exact ID 구조 가능성 검증. | Issue #156; `research/US-EIA-GEN-F01/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260917-US-EIA-GEN-F01-ACTIVE','active_issue':156,'active_research':'US-EIA-GEN-F01','last_completed_issue':155,'last_completed_research':'PORTFOLIO-R36','last_decision':DEC,'updated':'2026-09-17'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-US-EIA-GEN-F01-ACTIVE
active_issue: 156
active_research: US-EIA-GEN-F01
last_completed_issue: 155
last_completed_research: PORTFOLIO-R36
last_decision: DEC-224
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_EIA_GEN_F01_ACTIVE__OUTCOME_BLIND_STRUCTURAL_GATE`\n\nUS-EIA-GEN-F01 is active under its frozen pre-Issue 18-gate contract. Future December-2025 generator rows remain unopened.\n\n## Exact next action / 정확한 다음 행동\n\nExecute the immutable January-2024 Planned-snapshot structural gate and December-2025 header-only source check.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_EIA_GEN_F01_ACTIVE__OUTCOME_BLIND_STRUCTURAL_GATE`\n\n- Issue #156 open.\n- Frozen contract: `{CONTRACT}`.\n- Exposure: January-2024 EIA-860M Planned rows.\n- Future source: December-2025 file/sheet/header only; no data rows.\n- Exact identity: Plant ID + Generator ID.\n- Exposure: focal 2024-2025 planned solar units; COLOCATED iff same Plant ID has planned BATTERIES row.\n- 18 frozen gates; no outcome/slippage/prediction/ranking/causality.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('US_EIA_GEN_F01_ACTIVE')
