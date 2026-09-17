#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
STAGING='bfba6b52c8b09257d3430f6661b663779c23eb63'
RUN='35250781694'
DEC='DEC-233'
GATE='PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY'
CONTRACT='6568d9bd0d897abb0bcabf8eaf04f2e54f50177f'
CORRECTION='08403a21ef34462149b3a22228c3f3a02300b50f'

base=json.loads((ROOT/'research/US-FDIC-BRANCH-F01/staging/f01_result.json').read_text(encoding='utf-8'))
x=json.loads((ROOT/'research/US-FDIC-BRANCH-F01/staging/attempt-02/f01_result.json').read_text(encoding='utf-8'))
assert base['requirements_passed']==17 and base['requirements'][7]['number']==8 and not base['requirements'][7]['pass']
assert x['gate']==GATE and x['scientific_disposition']=='PASS'
assert x['requirements_total']==18 and x['requirements_passed']==18
assert x['contract_commit']==CONTRACT
assert x['implementation_correction_commit']==CORRECTION
assert x['diagnostics']['structurally_usable_branch_year_rows']==233669
assert x['diagnostics']['distinct_uninumbr']==81218
assert x['diagnostics']['uninumbr_in_ge2_years']==77753
assert x['diagnostics']['uninumbr_in_all3_years']==74698
assert x['diagnostics']['uninumbr_with_cert_change']==2499
assert x['diagnostics']['valid_identity_rate']==1.0
assert x['requirements'][7]['evidence']['rowless_2025_sod_head']['http_status']==200
assert x['requirements'][7]['evidence']['rowless_2025_sod_head']['response_body_read'] is False
assert x['requirements'][7]['evidence']['future_2025_rows_opened'] is False
assert all(v is False for v in x['boundaries'].values())
assert x['incremental_monetary_cost_usd']==0

result=f'''---
id: US-FDIC-BRANCH-F01-RESULT
type: structural-feasibility-result
created: 2026-09-18
issue: 160
research: US-FDIC-BRANCH-F01
disposition: PASS
staging_commit: {STAGING}
workflow_run: {RUN}
contract_commit: {CONTRACT}
gate: {GATE}
---

# US-FDIC-BRANCH-F01 Result / 결과

## Terminal disposition / 최종 판정

**`{GATE}`**

The final immutable outcome-blind evidence passes **18/18** frozen requirements. Exact FDIC `UNINUMBR` provides sufficient historical physical-location continuity and ownership-change support for a separately preregistered N01 design.

최종 immutable outcome-blind evidence는 고정된 **18/18** 요구조건을 모두 통과했습니다. FDIC exact `UNINUMBR`는 별도 사전등록 N01 설계를 진행할 만큼 충분한 물리적 branch-location 종단 연속성과 소유권 변경 support를 제공합니다.

## Structural support / 구조적 support

- 2022–2024 structurally usable branch-year rows: **233,669**
- distinct valid `UNINUMBR`: **81,218**
- `UNINUMBR` observed in at least 2 of 3 years: **77,753**
- `UNINUMBR` observed in all 3 years: **74,698**
- exact `UNINUMBR` identities with historical `CERT` change: **2,499**
- historical identity-field validity: **100%**
- rows by year: 2022 **79,172** / 2023 **77,770** / 2024 **76,727**

These are structural feasibility facts only. They are not branch-closure, ownership-effect, prediction, causal, ranking, or novelty results.

## Implementation correction provenance / 구현 보정 계보

Attempt 01 preserved all historical empirical evidence but returned 17/18 because the implementation incorrectly required literal `UNINUMBR` text inside an unexpanded OpenAPI/JS transport payload for frozen requirement #8. That result remains immutable.

Correction `{CORRECTION}` changed **no scientific requirement or threshold**. Attempt 02 resolved only transport/schema evidence with an official 2025 SOD `HEAD` request requesting `YEAR,CERT,BRNUM,UNINUMBR`; the server returned HTTP 200 and **no response body was read**. Attempt 02 was committed at `{STAGING}`.

## Future-outcome firewall / 미래 outcome 방화벽

No 2025 SOD data row, future branch membership, future History/Structure Change event membership, closure/non-continuation disposition, relationship, predictive metric, causal estimate, bank/branch ranking, or novelty result was opened or computed.

## Consequence / 후속 조치

This PASS authorizes **only** a separately preregistered outcome-blind `US-FDIC-BRANCH-N01` design stage. N01 must define exposure/comparator construction and future-disposition adjudication rules before any candidate future membership is opened. E01 remains unauthorized.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/US-FDIC-BRANCH-F01/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: 160
research: US-FDIC-BRANCH-F01
status: terminal
---

# {DEC} — Finalize US-FDIC-BRANCH-F01 PASS and authorize N01 design only

Finalize `US-FDIC-BRANCH-F01` as `{GATE}` from immutable Attempt 02 commit `{STAGING}` / Run `{RUN}`.

All 18 frozen requirements pass. Historical exact-`UNINUMBR` support is 233,669 branch-years, 81,218 distinct physical-location identities, 74,698 identities in all three historical years, and 2,499 identities with historical `CERT` changes. Implementation correction `{CORRECTION}` changed no scientific threshold and consumed no 2025 response body. Future branch/event membership remains unopened.

Authorize only a separate outcome-blind `US-FDIC-BRANCH-N01` design. E01 remains unauthorized. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'; log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Finalize `US-FDIC-BRANCH-F01` as 18/18 structural PASS; authorize only separate outcome-blind N01 design. / `US-FDIC-BRANCH-F01`을 18/18 구조 PASS로 종결하고 별도 outcome-blind N01 설계만 허가. | 233,669 historical branch-years; 81,218 distinct `UNINUMBR`; 74,698 all-three-year identities; 2,499 historical ownership changes; no future row opened. / 미래 row 미개봉 상태의 강한 exact physical-branch support. | Issue #160; `{STAGING}`; `research/US-FDIC-BRANCH-F01/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-US-FDIC-BRANCH-F01-TERMINAL','active_issue':'none','active_research':'NONE','last_completed_issue':160,'last_completed_research':'US-FDIC-BRANCH-F01','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-US-FDIC-BRANCH-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 160
last_completed_research: US-FDIC-BRANCH-F01
last_decision: DEC-233
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+'''\n# Project Status / 프로젝트 상태\n\n**State / 상태:** `US_FDIC_BRANCH_F01_PASS__N01_DESIGN_AUTHORIZED`\n\nUS-FDIC-BRANCH-F01 is terminal PASS at 18/18 frozen requirements. Exact `UNINUMBR` longitudinal support is sufficient. Future branch/event membership remains unopened.\n\n## Exact next action / 정확한 다음 행동\n\nDesign and freeze a separate outcome-blind `US-FDIC-BRANCH-N01` contract **before** opening its Issue. N01 may use only already-authorized historical structural evidence while prospectively fixing exposure/comparator and future-disposition adjudication rules. E01 remains unauthorized.\n\nIncremental monetary cost remains **0 USD**.\n''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''\n# Session Handoff / 세션 인계\n\n`US_FDIC_BRANCH_F01_PASS__N01_DESIGN_AUTHORIZED`\n\n- Issue #160 completed.\n- Contract: `{CONTRACT}`.\n- Immutable PASS evidence: `{STAGING}` / Run `{RUN}`.\n- 18/18 PASS.\n- Historical support: 233,669 branch-years; 81,218 distinct UNINUMBR; 77,753 in >=2 years; 74,698 in all 3 years; 2,499 historical CERT changes.\n- 2025 SOD response body and future branch/event membership unopened.\n- N01 design only authorized; E01 not authorized.\n- Next: freeze `US-FDIC-BRANCH-N01` contract before creating its Issue.\n- Cost: 0 USD.\n''',encoding='utf-8')
print(GATE)
