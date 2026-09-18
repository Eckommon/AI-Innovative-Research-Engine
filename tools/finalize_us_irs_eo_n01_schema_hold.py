#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
CONTRACT='70898f12e1b1fb2ad233aaf0a1cb13ff49d73fe8'
ISSUE=164
DEC='DEC-240'
DISP='HOLD_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_NOT_IDENTIFIABLE'
PRE1='e5ef1b4e6415a4fcd59a692da5d6d37e8a10b00d'
PRE2='75fc78558e2911b970a23db9e2da754f7c90434f'
MAP='114c673aa2ddce5feeefdd5d24efa308c7bad783'

p1=json.loads((ROOT/'research/US-IRS-EO-N01/schema-preflight.json').read_text())
p2=json.loads((ROOT/'research/US-IRS-EO-N01/schema-preflight-02.json').read_text())
pm=json.loads((ROOT/'research/US-IRS-EO-N01/schema-application-pending-map.json').read_text())

assert p1['contract_sha']==CONTRACT and p2['contract_sha']==CONTRACT and pm['contract_sha']==CONTRACT
assert p1['historical_index_rows_opened']==0 and p1['historical_xml_return_rows_opened']==0
assert p2['historical_index_rows_opened']==0 and p2['historical_xml_return_rows_opened']==0
assert pm['historical_return_rows_opened']==0
assert p1['future_outcome_rows_opened']==0 and p2['future_outcome_rows_opened']==0 and pm['future_outcome_rows_opened']==0
assert p1['automatic_revocation_entity_body_bytes_consumed']==0
assert p2['candidate_resolved']['ApplicationPendingInd'] is False
assert all(x['status']==200 for x in p1['historical_xml_zip_heads'])
assert p1['index_head']['status']==200
assert all(x['file'].endswith(('IRS990EZ/IRS990EZ.xsd','IRS990PF/IRS990PF.xsd')) for x in pm['hits'])
assert all(x['tag']=='ApplicationPending' for x in pm['hits'])
assert not any('TEGE990/IRS990/IRS990.xsd' in x['file'] for x in pm['hits'])

result=f'''---
id: US-IRS-EO-N01-RESULT
type: outcome-blind-design-identifiability-result
created: 2026-09-18
issue: {ISSUE}
research: US-IRS-EO-N01
disposition: HOLD
failed_gate: 5
contract_commit: {CONTRACT}
gate: {DISP}
---

# US-IRS-EO-N01 Result / 결과

## Terminal disposition / 최종 판정

**`{DISP}`**

N01 terminates outcome-blind at **Gate 5** before any historical organization-return row or Automatic Revocation membership is opened.

N01은 historical organization-return row나 Automatic Revocation membership을 열기 전에 **Gate 5**에서 outcome-blind terminal HOLD로 종료됩니다.

## Why Gate 5 fails / Gate 5 실패 이유

The frozen contract requires every baseline eligibility concept to have one deterministic official-IRS 2019 XML mapping. In particular, the selected Form 990 baseline return requires `ApplicationPendingInd` not to be true.

Official IRS 2019v5.1 redacted-schema inspection establishes:

- `ApplicationPendingInd`: **no declaration/reference anywhere in the scanned 2019v5.1 package**;
- `ApplicationPending`: declared as `CheckboxType` for **IRS990EZ** and **IRS990PF** only;
- no `ApplicationPending` declaration was found in `TEGE/TEGE990/IRS990/IRS990.xsd`;
- the 2019 paper Form 990 itself includes an “Application pending” checkbox, so silently treating the missing XML concept as false would be an unsupported semantic inference.

Therefore the frozen Form-990-only cohort cannot deterministically enforce all of its own eligibility criteria from the authorized 2019 XML source. Dropping the criterion, substituting a proxy, changing the source year, admitting 990-EZ/PF, or treating schema absence as false would alter the frozen design after Issue binding and is prohibited.

## Preserved evidence / 보존 증거

- contract: `{CONTRACT}`
- source/schema preflight: `{PRE1}`
- name/ref schema preflight: `{PRE2}`
- exact application-pending schema map: `{MAP}`
- official 2019 schema SHA-256: `{p1['schema_sha256']}`
- 2019 index endpoint HEAD: HTTP **{p1['index_head']['status']}**
- nine historical XML ZIP endpoints HEAD: **9/9 HTTP 200**

## Firewall / 방화벽

- historical 2019 index data rows opened by N01: **0**
- historical organization XML return rows opened by N01: **0**
- Automatic Revocation data rows opened: **0**
- Automatic Revocation entity-body bytes consumed: **0**
- relationship computed: **false**
- predictive metric computed: **false**
- exposure/matching thresholds changed: **false**
- source year changed: **false**
- incremental monetary cost: **0 USD**

Because one valid frozen requirement already fails, gates requiring full historical row ingestion, cohort cardinality, quartiles, matching, balance, and pair-manifest construction are **not run**. This is terminal early-stop, not missing evidence to be rescued inside N01.

## Consequence / 후속 조치

No E01 is authorized. The 2019 Form-990 governance-independence design is not rescued. The next authorized project action is an independent **PORTFOLIO-R40** outcome-blind reselection that treats this N01 HOLD as negative evidence.

E01은 허가되지 않습니다. 본 2019 Form-990 governance-independence 설계는 구조 변경으로 구제하지 않습니다. 다음 허가 작업은 이 HOLD를 negative evidence로 보존한 독립 **PORTFOLIO-R40** reselection입니다.
'''
(ROOT/'research/US-IRS-EO-N01/RESULT.md').write_text(result,encoding='utf-8')

dec=f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: {ISSUE}
research: US-IRS-EO-N01
status: terminal
---

# {DEC} — Terminate US-IRS-EO-N01 at frozen schema-mapping Gate 5

Finalize `US-IRS-EO-N01` as `{DISP}`.

The frozen Form-990-only 2019 design requires deterministic XML enforcement of the application-pending exclusion. Official 2019v5.1 schema inspection finds neither `ApplicationPendingInd` nor a Form-990 `ApplicationPending` element; the latter exists only for 990-EZ and 990-PF. Treating absence as false, dropping the criterion, substituting a proxy, changing source year, or admitting other form families would alter the frozen design.

No historical organization-return rows or Automatic Revocation rows were opened. E01 is not authorized. Proceed to independent PORTFOLIO-R40 reselection. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec,encoding='utf-8')

logp=ROOT/'registry/DECISION_LOG.md'; log=logp.read_text(encoding='utf-8')
if DEC not in log:
    row=f'\n| `{DEC}` | 2026-09-18 | Terminate `US-IRS-EO-N01` at frozen Gate 5; no Form-990 2019 XML mapping exists for the required application-pending exclusion. / 고정 Gate 5에서 N01 종결; 2019 Form-990 XML에 필수 application-pending mapping 부재. | Official 2019v5.1 schema has no `ApplicationPendingInd`; `ApplicationPending` is declared only for 990-EZ/PF. No historical return or future outcome row opened. / historical·outcome row 미개봉. | Issue #164; `{MAP}`; `research/US-IRS-EO-N01/RESULT.md` | active |\n'
    logp.write_text(log.rstrip()+row,encoding='utf-8')

cp={'checkpoint_id':'CHK-20260918-US-IRS-EO-N01-TERMINAL','active_issue':'none','active_research':'NONE',
    'last_completed_issue':164,'last_completed_research':'US-IRS-EO-N01','last_decision':DEC,'updated':'2026-09-18'}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n',encoding='utf-8')
front='''---
checkpoint_id: CHK-20260918-US-IRS-EO-N01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 164
last_completed_research: US-IRS-EO-N01
last_decision: DEC-240
updated: 2026-09-18
---
'''
(ROOT/'STATUS.md').write_text(front+f'''
# Project Status / 프로젝트 상태

**State / 상태:** `US_IRS_EO_N01_HOLD_GATE5_SCHEMA_MAPPING__PORTFOLIO_RESELECTION_REQUIRED`

US-IRS-EO-N01 is terminal scientific HOLD at frozen Gate 5. The authorized 2019 Form-990-only XML source cannot deterministically enforce the frozen application-pending eligibility exclusion. No historical organization-return row or Automatic Revocation row was opened.

## Exact next action / 정확한 다음 행동

Execute independent outcome-blind `PORTFOLIO-R40` reselection. Do not rescue N01 by dropping the application-pending criterion, changing the source year, admitting 990-EZ/PF, using a proxy, or opening revocation membership. E01 remains unauthorized.

Incremental monetary cost remains **0 USD**.
''',encoding='utf-8')
(ROOT/'context/SESSION_HANDOFF.md').write_text(front+f'''
# Session Handoff / 세션 인계

`US_IRS_EO_N01_HOLD_GATE5_SCHEMA_MAPPING__PORTFOLIO_RESELECTION_REQUIRED`

- Issue #164 completed.
- Contract: `{CONTRACT}`.
- Terminal disposition: `{DISP}`.
- Failed frozen requirement: Gate 5 — deterministic official-IRS semantic mapping.
- 2019 schema SHA-256: `{p1['schema_sha256']}`.
- `ApplicationPendingInd`: absent from scanned 2019v5.1 schema.
- `ApplicationPending`: declared only in IRS990EZ and IRS990PF, not IRS990.
- Historical organization-return rows opened: 0.
- Automatic Revocation rows opened: 0; entity-body bytes consumed: 0.
- E01 not authorized.
- Next: independent outcome-blind `PORTFOLIO-R40`.
- Cost: 0 USD.
''',encoding='utf-8')
print(DISP)
