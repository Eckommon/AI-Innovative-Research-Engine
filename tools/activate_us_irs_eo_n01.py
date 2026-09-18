#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEC='DEC-239'
CONTRACT='70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8'
ISSUE=164

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: US-IRS-EO-N01
status: active
---

# {DEC} — Activate outcome-blind IRS matched governance-independence design

Activate Issue #{ISSUE} only under pre-Issue contract `{CONTRACT}`.

N01 may read only the frozen official IRS 2019 Form 990 index and nine 2019 XML ZIP bundles to construct the historical 501(c)(3), Form-990-only exact-EIN cohort, governing-body-independence quartile exposure, and deterministic matched pair manifest. Automatic Revocation rows, missed-filing/nonfiling exposure variables, relationship metrics, prediction, causality, organization ranking, and novelty claims remain unauthorized. E01 is not authorized. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'
log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Activate `US-IRS-EO-N01` under pre-Issue contract `{CONTRACT}`; 2019 Form-990-only matched governance-independence design only. / 사전계약에 따라 2019 Form 990 governance-independence matched design만 활성화. | Parent F01 passed 18/18; N01 must prove historical cohort/exposure/matching identifiability before any Automatic Revocation membership is opened. / F01 PASS 후 outcome 개봉 전 historical matched-design 식별 가능성 검증 필요. | Issue #164; `research/US-IRS-EO-N01/README.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={
    'checkpoint_id':'CHK-20260918-US-IRS-EO-N01-ACTIVE',
    'active_issue':164,
    'active_research':'US-IRS-EO-N01',
    'last_completed_issue':163,
    'last_completed_research':'US-IRS-EO-F01',
    'last_decision':DEC,
    'updated':'2026-09-18'
}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')

front='''---
checkpoint_id: CHK-20260918-US-IRS-EO-N01-ACTIVE
active_issue: 164
active_research: US-IRS-EO-N01
last_completed_issue: 163
last_completed_research: US-IRS-EO-F01
last_decision: DEC-239
updated: 2026-09-18
---
'''

(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_IRS_EO_N01_ACTIVE__OUTCOME_BLIND_MATCHED_GOVERNANCE_DESIGN`\n\nUS-IRS-EO-N01 is active under its frozen pre-Issue contract. Only the official IRS 2019 Form 990 historical index/XML sources are authorized for cohort, exposure, matching, and balance construction. Automatic Revocation membership remains unopened.\n\n## Exact next action / 정확한 다음 행동\n\nExecute the immutable 18-requirement historical Form-990 cohort / governing-body-independence exposure / matched-balance gate without opening any Automatic Revocation row. E01 remains unauthorized.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')

(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_IRS_EO_N01_ACTIVE__OUTCOME_BLIND_MATCHED_GOVERNANCE_DESIGN`\n\n- Issue #164 open.\n- Contract: `{CONTRACT}`.\n- Parent F01: 18/18 PASS under DEC-238.\n- Authorized historical source: official IRS 2019 Form 990 index + nine frozen 2019 XML ZIP bundles only.\n- Unit: exact 9-digit EIN; U.S. 501(c)(3), Form 990 only.\n- Exposure: governing-body independence ratio, bottom vs top quartile.\n- Matching: exact state × tax-period-end year × board-size bin × revenue decile; deterministic historical balance matching.\n- Automatic Revocation rows opened: 0.\n- E01 not authorized.\n- Cost: 0 USD.\n''',encoding='utf-8')

print('US_IRS_EO_N01_ACTIVE')
