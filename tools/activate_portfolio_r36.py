#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-222'
CONTRACT='6550f4cfbde9df2702c793b902d7676f05700d61'

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-17
issue: 155
research: PORTFOLIO-R36
status: active
---

# {DEC} — Activate independent PORTFOLIO-R36 reselection

Activate Issue #155 only under pre-Issue contract `{CONTRACT}`.

R36 evaluates exactly four frozen candidates (`US-EIA-GEN-001`, `US-EDU-FIN-001`, `US-FDIC-BANK-001`, `US-CMS-HOSP-001`) under the frozen nine-dimension `/45` rubric. Candidate outcomes remain unopened. FAA-AIP threshold/conflict rescue is prohibited. Source-native join defensibility is the first tie-break. Incremental monetary cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-17 | Activate `PORTFOLIO-R36` under pre-Issue contract `{CONTRACT}` with exactly four cross-domain candidates and frozen `/45` rubric. / 사전고정 계약 아래 4개 cross-domain 후보와 고정 `/45` rubric으로 R36 활성화. | FAA-AIP F01 terminated at frozen HOLD; independent reselection required and FAA rescue prohibited. / FAA-AIP F01 고정 HOLD 후 독립 재선정 필요, FAA 구제 금지. | Issue #155; `research/PORTFOLIO-R36/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={
  'checkpoint_id':'CHK-20260917-PORTFOLIO-R36-ACTIVE',
  'active_issue':155,
  'active_research':'PORTFOLIO-R36',
  'last_completed_issue':154,
  'last_completed_research':'US-FAA-AIP-F01',
  'last_decision':DEC,
  'updated':'2026-09-17'
}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260917-PORTFOLIO-R36-ACTIVE
active_issue: 155
active_research: PORTFOLIO-R36
last_completed_issue: 154
last_completed_research: US-FAA-AIP-F01
last_decision: DEC-222
updated: 2026-09-17
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R36_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\nR36 is active under the frozen pre-Issue four-candidate contract. Candidate outcomes remain unopened.\n\n## Exact next action / 정확한 다음 행동\n\nRevalidate official sources, internal overlap and external literature/agency-framework overlap; then write exactly one immutable scorecard and select at most one outcome-blind F01.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R36_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\n- Issue #155 open.\n- Frozen contract: `{CONTRACT}`.\n- Candidates: EIA generator commissioning, education finance→operating status, FDIC financial structure→failure, CMS process measures→unplanned visits.\n- Outcomes unopened.\n- FAA-AIP rescue prohibited.\n- Next: source/internal-history/literature revalidation → one immutable scorecard.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('PORTFOLIO_R36_ACTIVE')
