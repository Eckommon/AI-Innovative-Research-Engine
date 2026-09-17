#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-226'
CONTRACT='7ad2e9bf392d3e8fdf41982d7e1a800eca377f5a'
ISSUE=157

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: {ISSUE}
research: PORTFOLIO-R37
status: active
---

# {DEC} — Activate independent PORTFOLIO-R37 reselection

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

R37 evaluates exactly four frozen candidates (`US-FSIS-SAMPLE-001`, `US-USASPEND-VENDOR-001`, `US-EPA-SDWIS-001`, `US-CMS-NH-001`) under the frozen nine-dimension `/45` rubric. Candidate outcome rows remain unopened. EIA generator threshold/window rescue is prohibited. Source-native join defensibility is the first tie-break. Incremental monetary cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Activate `PORTFOLIO-R37` under pre-Issue contract `{CONTRACT}` with four frozen cross-domain candidates and the `/45` rubric. / 사전고정 계약 아래 4개 cross-domain 후보와 `/45` rubric으로 R37 활성화. | EIA generator F01 terminated at its frozen cohort-size HOLD; independent reselection is required and post-hoc EIA rescue is prohibited. / EIA generator F01 고정 표본수 HOLD 후 독립 재선정 필요, 사후 EIA 구제 금지. | Issue #157; `research/PORTFOLIO-R37/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={
  'checkpoint_id':'CHK-20260917-PORTFOLIO-R37-ACTIVE',
  'active_issue':157,
  'active_research':'PORTFOLIO-R37',
  'last_completed_issue':156,
  'last_completed_research':'US-EIA-GEN-F01',
  'last_decision':DEC,
  'updated':'2026-09-17'
}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-PORTFOLIO-R37-ACTIVE
active_issue: 157
active_research: PORTFOLIO-R37
last_completed_issue: 156
last_completed_research: US-EIA-GEN-F01
last_decision: DEC-226
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R37_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\nR37 is active under the frozen pre-Issue four-candidate contract. Candidate outcomes remain unopened. EIA generator F01 remains terminal HOLD and is not being rescued.\n\n## Exact next action / 정확한 다음 행동\n\nRevalidate official sources, internal overlap and bounded external literature/agency-framework overlap; then write exactly one immutable scorecard and select at most one outcome-blind F01.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R37_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\n- Issue #157 open.\n- Frozen contract: `{CONTRACT}`.\n- Candidates: FSIS sampling→recall, USAspending vendor dependence→award interruption, SDWIS compliance→health-based violation, CMS nursing-home staffing→severe deficiency.\n- Candidate outcome rows unopened.\n- EIA generator threshold/window rescue prohibited.\n- Next: source/internal-history/literature revalidation → one immutable scorecard.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('PORTFOLIO_R37_ACTIVE')
