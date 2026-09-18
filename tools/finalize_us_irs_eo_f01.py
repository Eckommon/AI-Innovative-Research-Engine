#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ATTEMPT1_COMMIT = '814f4da6a6050bb3e61908c01807eb769a017553'
ATTEMPT2_COMMIT = 'ab7651c49e2c739734c6330d9d239201514d21e3'
ATTEMPT1_RUN = '35257875153'
ATTEMPT2_RUN = '35282837658'
CONTRACT = '689a00db411b650defcb679bef998beeb55a57da'
CORRECTION = 'd3026031bb7e5b90e63709589e226cd99babc590'
DEC = 'DEC-238'
GATE = 'PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY'

a1 = json.loads((ROOT/'research/US-IRS-EO-F01/evidence/attempt-01.json').read_text(encoding='utf-8'))
a2 = json.loads((ROOT/'research/US-IRS-EO-F01/evidence/attempt-02.json').read_text(encoding='utf-8'))

assert a1['contract_sha'] == CONTRACT
assert a1['github_run_id'] == ATTEMPT1_RUN
assert a1['pass_count'] == 17 and a1['failed_gates'] == [11]
assert a1['future_outcome_rows_opened'] == 0
assert a1['future_form990_2025_2026_rows_opened'] == 0
assert a1['automatic_revocation_entity_body_bytes_consumed'] == 0

assert a2['contract_sha'] == CONTRACT
assert a2['github_run_id'] == ATTEMPT2_RUN
assert a2['disposition'] == GATE
assert a2['attempt_valid'] is True
assert a2['pass_count'] == 18 and a2['failed_gates'] == []
assert a2['implementation_correction_commit'] == CORRECTION
assert a2['scientific_threshold_changed'] is False
assert a2['source_years_changed'] is False
assert a2['identity_rule_changed'] is False
assert a2['outcome_firewall_changed'] is False
assert a2['submission_date_precision_counts'] == {'YYYY_year_precision': 2090378}
assert a2['future_outcome_rows_opened'] == 0
assert a2['future_form990_2025_2026_rows_opened'] == 0
assert a2['automatic_revocation_entity_body_bytes_consumed'] == 0
assert a2['nonfiling_streak_exposure_variables_constructed'] == 0
assert a2['name_address_repair_used'] is False
assert a2['incremental_monetary_cost_usd'] == 0
assert a1['source_fingerprints'] == a2['source_fingerprints']

g = {x['gate']: x for x in a2['gates']}
assert len(g) == 18 and all(x['pass'] for x in g.values())
assert g[5]['observed']['valid_rows'] == 2090378
assert g[6]['observed']['combined_rows'] == 2090378
assert g[7]['observed']['distinct_valid_ein'] == 742646
assert g[8]['observed']['ein_in_at_least_two_indexes'] == 641705
assert g[9]['observed']['rate'] == 1.0
assert g[10]['observed']['duplicate_rate'] == 0.0
assert g[11]['observed']['rate'] == 1.0
assert g[16]['observed']['entity_body_bytes_consumed'] == 0

result = f'''---
id: US-IRS-EO-F01-RESULT
type: structural-feasibility-result
created: 2026-09-18
issue: 163
research: US-IRS-EO-F01
disposition: PASS
attempt_02_commit: {ATTEMPT2_COMMIT}
workflow_run: {ATTEMPT2_RUN}
contract_commit: {CONTRACT}
gate: {GATE}
---

# US-IRS-EO-F01 Result / 결과

## Terminal disposition / 최종 판정

**`{GATE}`**

The final immutable outcome-blind evidence passes **18/18** frozen requirements. Official IRS Form-990-series index data for posting years 2022–2024 provide exact nine-digit EIN identity, large longitudinal filed-organization support, documented filing/event semantics, and a still-sealed Automatic Revocation outcome source sufficient to proceed to one separately preregistered N01 design.

최종 immutable outcome-blind evidence는 고정된 **18/18** 요구조건을 모두 통과했습니다. 2022–2024 IRS Form-990-series 공식 index는 exact 9-digit EIN 식별자, 충분한 종단 filing support, 문서화된 filing/event semantics를 제공하며 Automatic Revocation outcome은 계속 봉인되어 있어 별도 사전등록 N01 설계로 진행할 수 있습니다.

## Structural support / 구조적 support

- combined 2022–2024 historical index rows: **2,090,378**
- valid exact 9-digit EIN rows: **2,090,378 / 2,090,378 (100%)**
- distinct valid EINs: **742,646**
- EINs present in at least two posting-year indexes: **641,705**
- parseable Tax Period: **100%**
- nonblank Object ID: **100%**
- duplicate nonblank Object ID rate: **0%**
- parseable Submission Date representation after the documented parser-only correction: **2,090,378 / 2,090,378 (100%)**
- Submission Date source precision in Attempt 02: **2,090,378 exact `YYYY` year-precision values**
- Automatic Revocation ZIP metadata access: **HEAD, HTTP 200, 0 entity-body bytes consumed**

These are structural feasibility facts only. They are not revocation-risk, financial-weakness, governance-effect, causal, predictive, ranking, compliance, or novelty results.

위 수치는 구조적 실행가능성 사실일 뿐이며 revocation risk, 재무취약성, governance effect, 인과·예측·순위·compliance·신규성 결과가 아닙니다.

## Implementation-correction provenance / 구현 보정 계보

Attempt 01 commit `{ATTEMPT1_COMMIT}` / Run `{ATTEMPT1_RUN}` is preserved unchanged. It returned 17/18 because the original parser accepted full calendar-date/timestamp forms but not the source's exact four-digit `YYYY` Submission Date representation, producing a uniform 0 / 2,090,378 Gate-11 parse result.

Correction `{CORRECTION}` changed **no scientific threshold, source year, identity rule, or outcome firewall**. Attempt 02 accepted exact `YYYY` only as a year-precision source representation. The internal `YYYY-01-01` value is an ordering sentinel and does not assert an observed month/day. Attempt 02 then passed all 18 frozen gates and is preserved at `{ATTEMPT2_COMMIT}` / Run `{ATTEMPT2_RUN}`.

Attempt 01은 삭제·덮어쓰기하지 않으며, 이번 PASS는 source representation에 대한 parser-only correction 이후 동일한 scientific contract를 재실행한 결과입니다.

## Future-outcome and anti-tautology firewall / 미래 outcome·순환성 방화벽

- Automatic Revocation data rows opened: **0**
- 2025/2026 Form-990 index rows opened: **0**
- Automatic Revocation entity-body bytes consumed: **0**
- missed-filing/nonfiling streak exposure variables constructed: **0**
- name/address/fuzzy/geospatial/manual identity repair used: **false**

Automatic revocation is mechanically tied to three consecutive missed required filings. Therefore descendant work remains prohibited from using missed-filing/nonfiling streaks or equivalent statutory-trigger encodings as exposure variables.

## Consequence / 후속 조치

This PASS authorizes **only** a separately preregistered outcome-blind `US-IRS-EO-N01` design stage. Before any Automatic Revocation membership row is opened, N01 must freeze the filed-return cohort, substantive non-tautological exposure, return/amendment deduplication, temporal risk window, reinstatement handling, matching/comparator rules, support/balance gates, and future event adjudication.

이 PASS는 별도 outcome-blind `US-IRS-EO-N01` 설계만 허가합니다. Automatic Revocation membership을 열기 전에 cohort·비순환 substantive exposure·중복처리·시간창·reinstatement·비교군·support/balance·event adjudication을 먼저 고정해야 합니다. E01은 아직 허가되지 않습니다.

Incremental monetary cost: **0 USD**.
'''
(ROOT/'research/US-IRS-EO-F01/RESULT.md').write_text(result, encoding='utf-8')

dec = f'''---
id: {DEC}
type: decision
created: 2026-09-18
issue: 163
research: US-IRS-EO-F01
status: terminal
---

# {DEC} — Finalize US-IRS-EO-F01 PASS and authorize N01 design only

Finalize `US-IRS-EO-F01` as `{GATE}` from immutable Attempt 02 commit `{ATTEMPT2_COMMIT}` / Run `{ATTEMPT2_RUN}`.

All 18 frozen requirements pass under the unchanged pre-Issue contract `{CONTRACT}`. Historical support is 2,090,378 index rows, 742,646 distinct exact EINs, and 641,705 EINs present in at least two of three posting-year indexes. Parser-only correction `{CORRECTION}` changed no scientific threshold, source year, identity rule, or outcome firewall. Automatic Revocation rows and 2025/2026 Form-990 index rows remain unopened; revocation ZIP entity-body bytes consumed remain zero.

Authorize only a separate outcome-blind `US-IRS-EO-N01` design. N01 must freeze a substantive non-tautological filed-return exposure and future-event adjudication before any Automatic Revocation membership is opened. E01 remains unauthorized. Cost remains 0 USD.
'''
(ROOT/f'registry/{DEC}.md').write_text(dec, encoding='utf-8')

logp = ROOT/'registry/DECISION_LOG.md'
log = logp.read_text(encoding='utf-8')
if DEC not in log:
    row = f'\n| `{DEC}` | 2026-09-18 | Finalize `US-IRS-EO-F01` as 18/18 structural PASS; authorize only separate outcome-blind `US-IRS-EO-N01` design. / `US-IRS-EO-F01`을 18/18 구조 PASS로 종결하고 별도 outcome-blind N01 설계만 허가. | 2,090,378 historical index rows; 742,646 distinct exact EINs; 641,705 EINs in >=2 posting-year indexes; parser-only correction changed no scientific boundary; future outcome rows unopened. / parser-only 보정 외 scientific boundary 불변, 미래 outcome 미개봉. | Issue #163; `{ATTEMPT2_COMMIT}`; `research/US-IRS-EO-F01/RESULT.md` | active |\n'
    logp.write_text(log.rstrip() + row, encoding='utf-8')

cp = {
    'checkpoint_id': 'CHK-20260918-US-IRS-EO-F01-TERMINAL',
    'active_issue': 'none',
    'active_research': 'NONE',
    'last_completed_issue': 163,
    'last_completed_research': 'US-IRS-EO-F01',
    'last_decision': DEC,
    'updated': '2026-09-18',
}
(ROOT/'context/checkpoint.json').write_text(json.dumps(cp, indent=2) + '\n', encoding='utf-8')

front = '''---
checkpoint_id: CHK-20260918-US-IRS-EO-F01-TERMINAL
active_issue: none
active_research: NONE
last_completed_issue: 163
last_completed_research: US-IRS-EO-F01
last_decision: DEC-238
updated: 2026-09-18
---
'''

(ROOT/'STATUS.md').write_text(front + '''
# Project Status / 프로젝트 상태

**State / 상태:** `US_IRS_EO_F01_PASS__N01_DESIGN_AUTHORIZED`

US-IRS-EO-F01 is terminal PASS at 18/18 frozen requirements. Historical exact-EIN identity and longitudinal support are sufficient. Automatic Revocation membership and 2025/2026 Form-990 index rows remain unopened.

## Exact next action / 정확한 다음 행동

Design and freeze a separate outcome-blind `US-IRS-EO-N01` contract **before** creating its Issue or opening any Automatic Revocation membership. N01 must prospectively fix a substantive non-tautological filed-return exposure, analytical cohort/deduplication, comparator/matching rules, support/balance gates, temporal risk window, reinstatement handling, and future-event adjudication. E01 remains unauthorized.

Incremental monetary cost remains **0 USD**.
''', encoding='utf-8')

(ROOT/'context/SESSION_HANDOFF.md').write_text(front + f'''
# Session Handoff / 세션 인계

`US_IRS_EO_F01_PASS__N01_DESIGN_AUTHORIZED`

- Issue #163 completed.
- Contract: `{CONTRACT}`.
- Immutable PASS evidence: `{ATTEMPT2_COMMIT}` / Run `{ATTEMPT2_RUN}`.
- 18/18 PASS.
- Historical support: 2,090,378 rows; 742,646 distinct exact EINs; 641,705 EINs present in >=2 of 3 posting-year indexes.
- Attempt 01 remains immutable at `{ATTEMPT1_COMMIT}` / Run `{ATTEMPT1_RUN}`; its Gate-11 failure was resolved only by documented year-precision parser correction `{CORRECTION}`.
- Automatic Revocation rows opened: 0; 2025/2026 Form-990 index rows opened: 0; revocation entity-body bytes consumed: 0.
- N01 design only authorized; E01 not authorized.
- Next: freeze `US-IRS-EO-N01` contract before creating its Issue or opening outcome membership.
- Cost: 0 USD.
''', encoding='utf-8')

print(GATE)
