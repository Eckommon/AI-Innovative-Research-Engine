#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-230'
CONTRACT='81216245922df756667295a4ffeb89fb41bd274f'
ISSUE=159

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: PORTFOLIO-R38
status: active
---

# {DEC} — Activate independent PORTFOLIO-R38 reselection

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

R38 evaluates exactly four frozen candidates (`US-FRA-XING-001`, `US-FDIC-BRANCH-001`, `US-FCC-BDC-001`, `US-CMS-DIALYSIS-001`) under the frozen nine-dimension `/45` rubric. Candidate future outcome rows remain unopened. FSIS transport failure remains operational, not scientific. No paid/proxy/third-party workaround is authorized. Incremental monetary cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Activate `PORTFOLIO-R38` under pre-Issue contract `{CONTRACT}` with four frozen cross-domain candidates and the `/45` rubric. / 사전고정 계약 아래 4개 cross-domain 후보와 `/45` rubric으로 R38 활성화. | FSIS F01 terminated operationally before scientific execution because official source access was WAF-blocked; independent reselection is required. / FSIS F01이 공식 원본 WAF 차단으로 scientific 실행 전 운영 종결되어 독립 재선정 필요. | Issue #159; `research/PORTFOLIO-R38/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-PORTFOLIO-R38-ACTIVE','active_issue':159,'active_research':'PORTFOLIO-R38','last_completed_issue':158,'last_completed_research':'US-FSIS-SAMPLE-F01','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-PORTFOLIO-R38-ACTIVE
active_issue: 159
active_research: PORTFOLIO-R38
last_completed_issue: 158
last_completed_research: US-FSIS-SAMPLE-F01
last_decision: DEC-230
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `PORTFOLIO_R38_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\nR38 is active under its frozen four-candidate pre-Issue contract. Candidate future outcomes remain unopened. FSIS remains transport-blocked with no scientific PASS/HOLD result.\n\n## Exact next action / 정확한 다음 행동\n\nComplete source/internal-history/literature revalidation, freeze exactly one `/45` scorecard, and select at most one outcome-blind F01.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`PORTFOLIO_R38_ACTIVE__SOURCE_LITERATURE_REVALIDATION_PENDING`\n\n- Issue #159 open.\n- Frozen contract: `{CONTRACT}`.\n- Candidates: FRA crossing, FDIC branch, FCC BDC provider, CMS dialysis.\n- Candidate outcome rows unopened.\n- FSIS remains transport-blocked; scientific gate not executed.\n- Next: revalidation -> one immutable scorecard -> at most one F01.\n- Cost: 0 USD.\n''',encoding='utf-8')
print('PORTFOLIO_R38_ACTIVE')
